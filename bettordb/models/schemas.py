from pydantic import BaseModel, Field
from typing import List, Optional, Literal


# --- Slots Simulation ---
class SlotsSimRequest(BaseModel):
    spins: int = Field(default=1_000_000, ge=1, le=100_000_000)
    paylines: int = Field(default=1, ge=1, le=100)
    symbol_weights: List[float] = Field(..., min_length=2)
    reels: int = Field(default=3, ge=2, le=10)
    symbol_values: Optional[List[float]] = Field(default=None)
    bet_per_line: float = Field(default=1.0, ge=0.01)


class ConfidenceInterval(BaseModel):
    lower: float
    upper: float
    level: str = "95%"


class SlotsSimResponse(BaseModel):
    house_edge_percent: float
    rtp_percent: float
    expected_loss_per_100_dollars: float
    confidence_interval: ConfidenceInterval
    total_spins: int
    actual_simulations: int


# --- Betting System Simulation ---
class BettingSystemRequest(BaseModel):
    system: Literal["martingale", "fibonacci", "dalembert", "flat"]
    base_bet: float = Field(..., gt=0)
    target_wins: int = Field(..., ge=1)
    max_bets: int = Field(..., ge=1)
    bankroll: float = Field(..., gt=0)
    win_probability: float = Field(default=0.4768, ge=0, le=1)
    payout: float = Field(default=2.0, gt=0)


class WorstCaseSimulation(BaseModel):
    final_bankroll: float
    bets_placed: int
    peak_drawdown_percent: float


class BettingSystemResponse(BaseModel):
    probability_of_reaching_target: float
    probability_of_ruin: float
    expected_value: float
    median_ending_bankroll: float
    mean_ending_bankroll: float
    worst_case_simulation: WorstCaseSimulation
    simulations_run: int


# --- Odds Conversion ---
class OddsConvertRequest(BaseModel):
    value: float = Field(..., gt=0)
    from_format: Literal["decimal", "fractional", "american", "implied"]
    to_format: Literal["decimal", "fractional", "american", "implied"]


class OddsConvertResponse(BaseModel):
    decimal: float
    fractional: str
    american: int
    implied_percent: float


# --- Kelly Criterion ---
class KellyCriterionRequest(BaseModel):
    bankroll: float = Field(..., gt=0)
    odds_decimal: float = Field(..., gt=1)
    probability_win: float = Field(..., ge=0, le=1)


class KellyCriterionResponse(BaseModel):
    kelly_fraction: float
    suggested_bet: float
    expected_value: float
    edge_percent: float


# --- Blackjack ---
class BlackjackOddsResponse(BaseModel):
    house_edge_basic_strategy: float
    house_edge_counting: float
    blackjack_probability: float
    bust_probability_dealer: float
    decks: int
    dealer_stands_on: int


# --- Roulette ---
class RoulettePocket(BaseModel):
    number: int
    color: Literal["red", "black", "green"]


class RouletteOddsResponse(BaseModel):
    house_edge_percent: float
    variant: str
    pockets: List[RoulettePocket]
    red_black_probability: float
    single_number_probability: float
