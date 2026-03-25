from fastapi import APIRouter
from models.schemas import KellyCriterionRequest, KellyCriterionResponse

router = APIRouter(prefix="/api/v1/kelly", tags=["kelly"])


@router.post("/criterion", response_model=KellyCriterionResponse)
async def kelly_criterion(req: KellyCriterionRequest):
    """
    Kelly Criterion: f* = (bp - q) / b
    where:
      b = decimal odds - 1
      p = probability of winning
      q = probability of losing = 1 - p
    """
    b = req.odds_decimal - 1
    p = req.probability_win
    q = 1 - p

    # Kelly fraction
    if b <= 0:
        kelly_fraction = 0.0
    else:
        kelly_fraction = max((b * p - q) / b, 0.0)

    suggested_bet = req.bankroll * kelly_fraction
    is_kelly_positive = kelly_fraction > 0

    return KellyCriterionResponse(
        kelly_fraction=round(kelly_fraction, 6),
        suggested_bet=round(suggested_bet, 4),
        is_kelly_positive=is_kelly_positive
    )
