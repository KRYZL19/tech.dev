import numpy as np


def calculate_blackjack_odds(decks: int = 6) -> dict:
    """
    Calculate blackjack odds using basic strategy approximations.
    """
    # Single deck true count approximations
    # House edge scales with decks
    if decks == 1:
        house_edge = 0.0017  # ~0.17% with perfect basic strategy
    elif decks == 2:
        house_edge = 0.0046
    elif decks == 6:
        house_edge = 0.0054  # ~0.54%
    elif decks >= 8:
        house_edge = 0.0056
    else:
        house_edge = 0.0054

    # Probability of blackjack (Ace + 10-value card)
    # P(blackjack) ≈ (4/13) * (4 * decks * 52 - 4) / (52*decks - 1)
    n = decks * 52
    p_ace_first = (4 * decks) / n
    p_ten_after_ace = (16 * decks - 16) / (n - 1)
    blackjack_prob = p_ace_first * p_ten_after_ace

    # Simplified bust probability (dealer)
    # Based on standard 6-deck shoe
    if decks >= 6:
        bust_prob = 0.3943  # ~39.4% dealer bust rate
    elif decks == 1:
        bust_prob = 0.3529
    else:
        bust_prob = 0.3850

    return {
        "decks": decks,
        "house_edge": round(house_edge, 6),
        "blackjack_prob": round(blackjack_prob, 6),
        "bust_prob": round(bust_prob, 6)
    }
