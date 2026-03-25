"""
Roulette probability calculator.
"""
from typing import List

# American: 0, 00 + 1-36
AMERICAN_POCKETS = [
    (0, "green"), (1, "red"), (2, "black"), (3, "red"), (4, "black"), (5, "red"),
    (6, "black"), (7, "red"), (8, "black"), (9, "red"), (10, "black"), (11, "black"),
    (12, "red"), (13, "black"), (14, "red"), (15, "black"), (16, "red"), (17, "black"),
    (18, "red"), (19, "black"), (20, "red"), (21, "black"), (22, "red"), (23, "black"),
    (24, "red"), (25, "black"), (26, "red"), (27, "black"), (28, "red"), (29, "black"),
    (30, "red"), (31, "black"), (32, "red"), (33, "black"), (34, "red"), (35, "black"),
    (36, "red"), (00, "green"),
]

# European: 0 + 1-36 (no 00)
EUROPEAN_POCKETS = [
    (0, "green"), (1, "red"), (2, "black"), (3, "red"), (4, "black"), (5, "red"),
    (6, "black"), (7, "red"), (8, "black"), (9, "red"), (10, "black"), (11, "red"),
    (12, "black"), (13, "red"), (14, "black"), (15, "red"), (16, "black"), (17, "red"),
    (18, "black"), (19, "red"), (20, "black"), (21, "red"), (22, "black"), (23, "red"),
    (24, "black"), (25, "red"), (26, "black"), (27, "red"), (28, "black"), (29, "red"),
    (30, "black"), (31, "red"), (32, "black"), (33, "red"), (34, "black"), (35, "red"),
    (36, "black"),
]


def get_roulette_odds(variant: str = "european") -> dict:
    """
    Get roulette odds for specified variant.

    Args:
        variant: "american" or "european"

    Returns:
        dict with house_edge_percent, variant, pockets, red_black_probability,
        single_number_probability
    """
    if variant.lower() == "american":
        pockets = AMERICAN_POCKETS
        n_pockets = 38
        house_edge = 2 / 38 * 100  # 5.26% (two green pockets)
    else:
        pockets = EUROPEAN_POCKETS
        n_pockets = 37
        house_edge = 1 / 37 * 100  # 2.70% (one green pocket)

    # Count red and black
    red_count = sum(1 for _, color in pockets if color == "red")
    black_count = sum(1 for _, color in pockets if color == "black")
    green_count = sum(1 for _, color in pockets if color == "green")

    red_black_prob = (red_count + black_count) / n_pockets
    single_prob = 1 / n_pockets

    formatted_pockets = [
        {"number": num if num != 0 and num != "00" else str(num), "color": color}
        for num, color in pockets
    ]

    return {
        "house_edge_percent": round(house_edge, 4),
        "variant": variant.lower(),
        "pockets": formatted_pockets,
        "red_black_probability": round(red_black_prob, 6),
        "single_number_probability": round(single_prob, 6),
        "red_count": red_count,
        "black_count": black_count,
        "green_count": green_count,
    }
