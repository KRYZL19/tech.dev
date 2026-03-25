import numpy as np


def calculate_baccarat_odds() -> dict:
    """
    Baccarat odds for banker/player/tie bets.
    Banker house edge: ~1.06%
    Player house edge: ~1.24%
    Tie house edge: ~14.36%
    """
    return {
        "banker_house_edge": 0.0106,
        "player_house_edge": 0.0124,
        "tie_house_edge": 0.1436,
        "banker_win_prob": 0.4586,
        "player_win_prob": 0.4463,
        "tie_prob": 0.0951
    }
