from .slots import simulate_slots
from .blackjack import get_blackjack_odds
from .roulette import get_roulette_odds
from .baccarat import get_baccarat_odds
from .martingale import simulate_betting_system

__all__ = [
    "simulate_slots",
    "get_blackjack_odds",
    "get_roulette_odds",
    "get_baccarat_odds",
    "simulate_betting_system",
]
