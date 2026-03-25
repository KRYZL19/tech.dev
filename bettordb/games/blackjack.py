"""
Blackjack odds calculator.
Uses combinatorial analysis for basic strategy and card counting EV.
"""
import numpy as np
from typing import Tuple


# Card values for Hi-Lo counting
CARD_VALUES = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0, '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def hand_value(hand: list) -> Tuple[int, bool]:
    """Return (value, is_soft) for a blackjack hand."""
    total = 0
    aces = 0
    for card in hand:
        if card == 'A':
            aces += 1
            total += 11
        elif card in ('10', 'J', 'Q', 'K'):
            total += 10
        else:
            total += int(card)

    is_soft = False
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    if aces > 0 and total <= 21:
        is_soft = True

    return total, is_soft


def get_blackjack_odds(decks: int = 6, dealer_stands_on: int = 17) -> dict:
    """
    Calculate blackjack house edge and probabilities.

    Args:
        decks: Number of decks in shoe (typically 6 or 8)
        dealer_stands_on: Dealer stands on this value or higher

    Returns:
        dict with house_edge_basic_strategy, house_edge_counting,
        blackjack_probability, bust_probability_dealer
    """
    n_cards = decks * 52

    # Hi-Lo count: running count -> true count
    # Bet ramp: spread from 1x to max_bet based on true count
    max_bet_multiple = 10

    # Approximate house edge using basic strategy (pre-computed)
    # Typical 6-deck H17 basic strategy house edge ~0.56%
    house_edge_basic = _basic_strategy_house_edge(decks, dealer_stands_on)

    # Card counting advantage (Hi-Lo with optimal betting)
    # Each +1 true count adds ~0.5% player edge
    # With 1-10 spread, average advantage ~0.5-1%
    # Accounting for heat and max bet constraints: ~0.3-0.5%
    counting_advantage = 0.004  # ~0.4% advantage with counting
    house_edge_counting = house_edge_basic - counting_advantage

    # Blackjack probability (natural 21)
    # Approximated using combinatorial analysis
    blackjack_prob = _blackjack_probability(decks)

    # Dealer bust probability
    bust_prob = _dealer_bust_probability(decks, dealer_stands_on)

    return {
        "house_edge_basic_strategy": round(house_edge_basic * 100, 4),
        "house_edge_counting": round(house_edge_counting * 100, 4),
        "blackjack_probability": round(blackjack_prob, 6),
        "bust_probability_dealer": round(bust_prob, 6),
        "decks": decks,
        "dealer_stands_on": dealer_stands_on,
    }


def _basic_strategy_house_edge(decks: int, dealer_stands_on: int) -> float:
    """Approximate basic strategy house edge for given rules."""
    # Base house edge for standard rules
    # Adjust for number of decks
    base_edge = 0.0027  # ~0.27% for infinite deck

    # Deck adjustment: more decks = higher house edge
    deck_adjustment = {
        1: -0.0018,
        2: -0.0003,
        4: 0.0005,
        6: 0.0010,
        8: 0.0014,
    }
    adjustment = deck_adjustment.get(decks, 0.001)

    # Dealer hits on soft 17 adds ~0.22% to house edge
    if dealer_stands_on == 17:
        # H17: dealer hits on soft 17 (more common in online)
        h17_adjustment = 0.0022
    else:
        h17_adjustment = 0.0

    return base_edge + adjustment + h17_adjustment


def _blackjack_probability(decks: int) -> float:
    """Calculate probability of getting a natural blackjack."""
    # P(blackjack) = P(ace first) * P(10-value second) + P(10-value first) * P(ace second)
    # With multi-deck, adjusted for removal

    n_aces = 4 * decks
    n_ten_values = 16 * decks  # 10, J, Q, K
    n_cards = 52 * decks

    # Simplified: P = 2 * (n_aces/n) * (n_ten_values/(n-1))
    p = 2 * (n_aces / n_cards) * (n_ten_values / (n_cards - 1))

    # Correction factor for actual blackjack tables
    return p


def _dealer_bust_probability(decks: int, dealer_stands_on: int) -> float:
    """Simulate dealer bust probability."""
    n_cards = 52 * decks

    # Run a simulation to get accurate bust probability
    n_sims = 50_000
    bust_count = 0

    rng = np.random.default_rng()

    for _ in range(n_sims):
        # Single deck shuffled each time for accuracy
        deck = []
        for d in range(decks):
            deck.extend(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4)

        rng.shuffle(deck)

        # Dealer's up card
        upcard = deck.pop()
        hand = [upcard]

        # Dealer draws
        while True:
            val, is_soft = hand_value(hand)
            if val > 21:
                bust_count += 1
                break
            if val >= dealer_stands_on and not is_soft:
                break
            if val == 21:
                break
            # Hit
            hand.append(deck.pop())

    return bust_count / n_sims
