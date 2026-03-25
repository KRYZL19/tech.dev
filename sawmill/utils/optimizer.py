"""Cut optimization algorithm — First Fit Decreasing bin packing."""

from typing import List, Tuple


def optimize_cutlist(
    available_boards: List[dict],
    required_cuts: List[dict],
    kerf_inches: float = 0.125,
) -> dict:
    """
    Optimize cutting required pieces from available boards.

    Uses First Fit Decreasing: sort cuts largest-first, assign each to first board that fits.

    Args:
        available_boards: list of {"board_type": str, "length_ft": float, "price_per_bf": float}
        required_cuts:    list of {"length_in": float, "width_in": float, "quantity": int}
        kerf_inches:      saw blade width loss per cut

    Returns:
        dict with keys: yield_percent, waste_boards, total_cost, assignments, leftover_inches
    """
    # Build cuts list with quantity expansion
    cuts = []
    for cut in required_cuts:
        for _ in range(int(cut.get("quantity", 1))):
            cuts.append({
                "length_in": float(cut["length_in"]),
                "width_in":  float(cut.get("width_in", 1.5)),
            })
    # Sort descending by area (length × width)
    cuts.sort(key=lambda c: c["length_in"] * c["width_in"], reverse=True)

    assignments = []   # which cut went to which board
    used_board_idxs = set()

    for cut in cuts:
        cut_len = cut["length_in"] + kerf_inches
        assigned = False
        for i, board in enumerate(available_boards):
            board_len_in = float(board["length_ft"]) * 12.0
            board_width_in = float(board.get("width_in", 3.5))

            # Board must be long enough (ignoring width for now — assume width already accounted)
            used_len = sum(
                a["cut_length_in"] + kerf_inches
                for a in assignments
                if a["board_idx"] == i
            )
            if used_len + cut_len <= board_len_in:
                assignments.append({
                    "board_idx": i,
                    "cut_length_in": cut["length_in"],
                    "cut_width_in": cut["width_in"],
                    "cut_area_sqft": (cut["length_in"] * cut["width_in"]) / 144.0,
                })
                used_board_idxs.add(i)
                assigned = True
                break

    # Calculate board usages
    board_areas_sqft = []
    total_board_area = 0.0
    for i, board in enumerate(available_boards):
        board_len_in = float(board["length_ft"]) * 12.0
        board_width_in = float(board.get("width_in", 3.5))
        area_sqft = (board_len_in * board_width_in) / 144.0
        board_areas_sqft.append(area_sqft)
        total_board_area += area_sqft

    used_board_area = sum(
        (a["cut_length_in"] * a["cut_width_in"]) / 144.0
        for a in assignments
    )

    total_cut_area_sqft = sum(
        (c["length_in"] * c["width_in"]) / 144.0
        for c in cuts
    )

    yield_percent = (used_board_area / total_board_area * 100.0) if total_board_area > 0 else 0.0

    # Waste per board
    waste_boards = []
    for i, board in enumerate(available_boards):
        used_on_board = sum(
            (a["cut_length_in"] * a["cut_width_in"]) / 144.0
            for a in assignments if a["board_idx"] == i
        )
        waste_area = board_areas_sqft[i] - used_on_board
        waste_boards.append({
            "board_idx": i,
            "board_type": board.get("board_type", "unknown"),
            "length_ft": board.get("length_ft"),
            "waste_area_sqft": round(waste_area, 4),
            "waste_cost": round(waste_area * board.get("price_per_bf", 2.0) * 12.0 / (board.get("length_ft", 8) * 12), 2)
                         if waste_area > 0 else 0.0,
        })

    total_cost = sum(b.get("price_per_bf", 2.0) * float(b.get("length_ft", 8)) * 12 * board_areas_sqft[i] / (float(b.get("length_ft", 8)) * 12)
                     for i, b in enumerate(available_boards) if i in used_board_idxs)
    # Simpler: total board foot price
    total_cost = sum(
        board.get("price_per_bf", 2.0) * float(board.get("length_ft", 8)) * 12 * board_areas_sqft[i] / (float(board.get("length_ft", 8)) * 12)
        for i, board in enumerate(available_boards)
    )
    # Recalculate properly: price_per_bf × board footage used
    # board footage = (length_ft × width_in × thickness_in/12) — simplify with bf_per_ft in dimensions
    total_cost = 0.0
    for i, board in enumerate(available_boards):
        bf_used = board_areas_sqft[i]  # already in sqft; bf = sqft × thickness_factor
        # Actually board_areas_sqft above = (len_in × width_in)/144 — not true board foot
        # True BF = (length_ft × width_in × thickness_in) / 12
        bf = (float(board["length_ft"]) * float(board.get("width_in", 3.5)) * 1.5) / 12.0
        total_cost += bf * board.get("price_per_bf", 2.0)

    return {
        "yield_percent": round(yield_percent, 2),
        "waste_boards": waste_boards,
        "total_cost": round(total_cost, 2),
        "assignments": assignments,
        "cuts_placed": len(assignments),
        "cuts_requested": len(cuts),
    }


def estimate_yield(board_sqft: float, cuts_sqft: float, kerf_inches: float = 0.125, board_count: int = 1) -> dict:
    """
    Estimate yield percentage given board area and cuts area.

    Args:
        board_sqft:     total square footage of available boards
        cuts_sqft:      total square footage of required cuts
        kerf_inches:    blade width loss per cut
        board_count:    number of boards (affects kerf waste)

    Returns:
        dict with theoretical_yield_pct, realistic_yield_pct
    """
    theoretical = (cuts_sqft / board_sqft * 100.0) if board_sqft > 0 else 0.0
    theoretical = min(theoretical, 100.0)

    # Kerf losses: each cut in length direction loses kerf_inches
    # Rough estimate: assume avg cut 2ft, 10 cuts per board
    kerf_loss_per_cut_sqft = (kerf_inches * 24.0) / 144.0  # 24" avg cut length
    total_kerf_loss = kerf_loss_per_cut_sqft * cuts_sqft / 2.0 * board_count
    realistic_cuts_sqft = max(0, cuts_sqft - total_kerf_loss)
    realistic = (realistic_cuts_sqft / board_sqft * 100.0) if board_sqft > 0 else 0.0
    realistic = min(realistic, 100.0)

    return {
        "theoretical_yield_pct": round(theoretical, 2),
        "realistic_yield_pct": round(realistic, 2),
    }
