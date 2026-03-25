"""
Kelly Criterion calculator endpoints.
"""
from fastapi import APIRouter
from models.schemas import KellyCriterionRequest, KellyCriterionResponse

router = APIRouter(prefix="/api/v1/kelly", tags=["kelly"])


@router.post("/criterion", response_model=KellyCriterionResponse)
async def kelly_criterion(req: KellyCriterionRequest):
    """
    Calculate the Kelly Criterion optimal bet fraction.

    The Kelly fraction = (bp - q) / b
    Where:
    - b = decimal odds - 1
    - p = probability of winning
    - q = probability of losing = 1 - p

    Returns the optimal fraction of bankroll to bet.
    """
    p = req.probability_win
    q = 1 - p
    b = req.odds_decimal - 1

    if b <= 0:
        return KellyCriterionResponse(
            kelly_fraction=0.0,
            suggested_bet=0.0,
            expected_value=0.0,
            edge_percent=0.0,
        )

    # Kelly formula: f* = (bp - q) / b
    kelly_fraction = max(0, (b * p - q) / b)

    # Edge calculation
    expected_value_per_unit = (p * (req.odds_decimal - 1)) - q
    edge_percent = expected_value_per_unit * 100

    suggested_bet = kelly_fraction * req.bankroll

    return KellyCriterionResponse(
        kelly_fraction=round(kelly_fraction, 6),
        suggested_bet=round(suggested_bet, 2),
        expected_value=round(expected_value_per_unit, 6),
        edge_percent=round(edge_percent, 4),
    )
