from fastapi import APIRouter
from models.schemas import CarbonIntensityResponse
from datetime import datetime, timezone


router = APIRouter(prefix="/api/v1/carbon", tags=["carbon"])


# Mock carbon intensity data by region (lbs CO2/kWh)
# Real data would come from EIA, WattTime, or similar APIs
CARBON_INTENSITY = {
    "caiso": 0.23,
    "pjm": 0.42,
    "miso": 0.52,
    "spp": 0.47,
    "ercot": 0.41,
    "nyiso": 0.25,
    "isone": 0.29,
    "bpa": 0.09,
    "default": 0.39,
}


@router.get("/intensity", response_model=CarbonIntensityResponse)
def get_carbon_intensity(region: str = "default"):
    """
    Get carbon intensity for a grid region.
    
    Returns estimated lbs CO2 per kWh. Real data sourced from
    grid operators and carbon APIs.
    """
    intensity = CARBON_INTENSITY.get(region.lower(), CARBON_INTENSITY["default"])
    return CarbonIntensityResponse(
        region=region.lower(),
        intensity=intensity,
        unit="lbs CO2/kWh",
        timestamp=datetime.now(timezone.utc).isoformat(),
        source="GRIDOPT estimated",
    )
