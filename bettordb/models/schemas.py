from pydantic import BaseModel
from typing import Optional, List, Dict


class SlotsSimulateRequest(BaseModel):
    spins: int = 1000
    paylines: int = 1
    symbol_weights: Dict[str, float]
    reels: int = 5
    bet_per_line: float = 1.0


class SlotsSimulateResponse(BaseModel):
    house_edge: float
    rtp: float
    expected_loss: float


class BettingSystemRequest(BaseModel):
    system: str  # martingale, fibonacci, dalembert, flat
    base_bet: float
    target_wins: int
    max_bets: int
    bankroll: float
    win_probability: float = 0.475  # e.g. ~even money bet


class BettingSystemResponse(BaseModel):
    system: str
    prob_reaching_target: float
    prob_ruin: float
    expected_value: float
    median_ending_bankroll: float
    worst_case: float
    n_simulations: int


class OddsConvertRequest(BaseModel):
    decimal_odds: Optional[float] = None
    fractional_odds: Optional[float] = None
    american_odds: Optional[float] = None
    implied_probability: Optional[float] = None


class OddsConvertResponse(BaseModel):
    decimal: float
    fractional: float
    american: float
    implied_probability: float


class KellyCriterionRequest(BaseModel):
    bankroll: float
    odds_decimal: float
    probability_win: float


class KellyCriterionResponse(BaseModel):
    kelly_fraction: float
    suggested_bet: float
    is_kelly_positive: bool


class BlackjackOddsResponse(BaseModel):
    decks: int
    house_edge: float
    blackjack_prob: float
    bust_prob: float


class RouletteOddsResponse(BaseModel):
    variant: str
    house_edge: float
    pockets: int
    green_pockets: List[int]
