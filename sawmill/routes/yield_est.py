"""Yield estimation route."""

from fastapi import APIRouter
from models.schemas import YieldEstimateRequest, YieldEstimateResponse
from utils.optimizer import estimate_yield

router = APIRouter(prefix="/yield", tags=["yield estimation"])


@router.post("/estimate", response_model=YieldEstimateResponse)
def yield_estimate(req: YieldEstimateRequest):
    """
    Estimate theoretical and realistic yield percentages.

    - **theoretical_yield_pct**: raw cuts_sqft / board_sqft × 100
    - **realistic_yield_pct**: accounts for kerf losses per cut
    """
    result = estimate_yield(
        board_sqft=req.board_sqft,
        cuts_sqft=req.cuts_sqft,
        kerf_inches=req.kerf_inches,
        board_count=req.board_count,
    )
    return YieldEstimateResponse(**result)
