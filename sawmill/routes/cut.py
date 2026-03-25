"""Cut list optimization route."""

from fastapi import APIRouter
from models.schemas import (
    CutListOptimizeRequest,
    CutListOptimizeResponse,
    WasteBoard,
    CutAssignment,
)
from utils.optimizer import optimize_cutlist
from utils.dimensions import WOOD_PRICES_PER_BF, LUMBER_DIMENSIONS

router = APIRouter(prefix="/optimize", tags=["cut optimization"])


def _resolve_board(board_data: dict) -> dict:
    """Fill in missing board dimensions from LUMBER_DIMENSIONS."""
    board_type = board_data.get("board_type", "2x4")
    dims = LUMBER_DIMENSIONS.get(board_type, {"actual": (1.5, 3.5)})
    actual = dims["actual"]
    resolved = {
        "board_type": board_type,
        "length_ft": board_data.get("length_ft", 8.0),
        "price_per_bf": board_data.get("price_per_bf", WOOD_PRICES_PER_BF.get(
            board_data.get("wood_type", "pine"), 2.0
        )),
        "wood_type": board_data.get("wood_type", "pine"),
        "width_in": board_data.get("width_in") or actual[1],
        "thickness_in": board_data.get("thickness_in") or actual[0],
    }
    return resolved


@router.post("/cutlist", response_model=CutListOptimizeResponse)
def optimize_cutlist_endpoint(req: CutListOptimizeRequest):
    """
    Optimize cutting required pieces from available boards.

    Returns yield percentage, waste per board, and total material cost.
    """
    # Resolve board dimensions
    resolved_boards = [_resolve_board(b.model_dump()) for b in req.available_boards]
    resolved_cuts = [c.model_dump() for c in req.required_cuts]

    result = optimize_cutlist(
        available_boards=resolved_boards,
        required_cuts=resolved_cuts,
        kerf_inches=req.kerf_inches,
    )

    waste_boards = [
        WasteBoard(**w) for w in result["waste_boards"]
    ]
    assignments = [
        CutAssignment(**a) for a in result["assignments"]
    ]

    return CutListOptimizeResponse(
        yield_percent=result["yield_percent"],
        waste_boards=waste_boards,
        total_cost=result["total_cost"],
        cuts_placed=result["cuts_placed"],
        cuts_requested=result["cuts_requested"],
        assignments=assignments,
    )
