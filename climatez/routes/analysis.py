"""Analysis routes for CLIMATEZ API."""

from fastapi import APIRouter, HTTPException, status

from data.climate_normals import get_city_data
from models.schemas import (
    GrowingSeasonRequest,
    GrowingSeasonResponse,
)


router = APIRouter(prefix="/api/v1", tags=["analysis"])

# Frost date adjustment factors by probability level (days from average)
# P10 = earliest possible (10% chance kill = risk-takers can use this)
# P50 = median date (50% chance)
# P90 = latest date (90% chance kill = safe for most growers)
FROST_DATE_MARGINS = {
    10: -21,  # 3 weeks earlier than average
    50: 0,    # average
    90: 21,   # 3 weeks later than average
}


def _adjust_frost_date(date_str: str | None, margin_days: int) -> str | None:
    """Adjust a frost date by margin days."""
    if date_str is None:
        return None
    
    try:
        from datetime import datetime, timedelta
        month, day = date_str.split("-")
        dt = datetime.strptime(f"2024-{month}-{day}", "%Y-%m-%d")
        adjusted = dt + timedelta(days=margin_days)
        return adjusted.strftime("%m-%d")
    except (ValueError, AttributeError):
        return date_str


@router.post("/growing-season", response_model=GrowingSeasonResponse)
async def estimate_growing_season(request: GrowingSeasonRequest):
    """Estimate growing season based on frost risk tolerance.
    
    Input:
        zipcode: 5-digit US zip code
        first_kill_probability_pct: 10 (early/risky), 50 (median), 90 (late/safe)
    
    Returns estimated frost dates and growing season length.
    """
    if len(request.zipcode) != 5 or not request.zipcode.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Zip code must be 5 digits"
        )
    
    if request.first_kill_probability_pct not in [10, 50, 90]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="first_kill_probability_pct must be 10, 50, or 90"
        )
    
    data = get_city_data(request.zipcode)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No climate data found for zip code {request.zipcode}"
        )
    
    last_spring = data["last_spring_frost"]
    first_fall = data["first_fall_frost"]
    
    # No frost climate (e.g., southern Florida, southern California)
    if last_spring is None and first_fall is None:
        return GrowingSeasonResponse(
            zipcode=request.zipcode,
            city=data["city"],
            state=data["state"],
            probability_pct=request.first_kill_probability_pct,
            estimated_last_spring_frost=None,
            estimated_first_fall_frost=None,
            growing_season_days=365,
            frost_free_risk="low",
            recommendation="Year-round growing season. No frost protection needed.",
        )
    
    margin = FROST_DATE_MARGINS[request.first_kill_probability_pct]
    
    # For spring: earlier margin means earlier last frost (risky for spring planting)
    # For fall: later margin means later first frost (extends fall growing)
    adjusted_last_spring = _adjust_frost_date(last_spring, -margin)
    adjusted_first_fall = _adjust_frost_date(first_fall, margin)
    
    # Calculate growing season
    if adjusted_last_spring and adjusted_first_fall:
        from datetime import datetime
        try:
            m1, d1 = adjusted_last_spring.split("-")
            m2, d2 = adjusted_first_fall.split("-")
            sp_dt = datetime.strptime(f"2024-{m1}-{d1}", "%Y-%m-%d")
            fa_dt = datetime.strptime(f"2024-{m2}-{d2}", "%Y-%m-%d")
            if fa_dt > sp_dt:
                growing_days = (fa_dt - sp_dt).days
            else:
                growing_days = 0
        except (ValueError, AttributeError):
            growing_days = data["growing_days"]
    else:
        growing_days = 365
    
    # Determine risk level
    if request.first_kill_probability_pct == 10:
        risk = "high"
        if growing_days >= 300:
            recommendation = (
                "High-risk growing season. Plant warm-season crops after last frost date. "
                "Use season extenders (row covers, cold frames) early/late in season."
            )
        else:
            recommendation = (
                "High-risk season. Choose short-season varieties. "
                "Start seeds indoors. Be prepared for frost protection."
            )
    elif request.first_kill_probability_pct == 50:
        risk = "medium"
        recommendation = (
            "Standard growing season. Safe planting window around median frost dates. "
            "Cool-season crops can be planted earlier/later. Warm-season crops after spring frost."
        )
    else:
        risk = "low"
        recommendation = (
            "Conservative growing season with low frost risk. "
            "Safe for most crops including long-season varieties. "
            "Consider extended season crops for fall gardening."
        )
    
    return GrowingSeasonResponse(
        zipcode=request.zipcode,
        city=data["city"],
        state=data["state"],
        probability_pct=request.first_kill_probability_pct,
        estimated_last_spring_frost=adjusted_last_spring,
        estimated_first_fall_frost=adjusted_first_fall,
        growing_season_days=growing_days,
        frost_free_risk=risk,
        recommendation=recommendation,
    )
