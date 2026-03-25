from fastapi import APIRouter
from datetime import datetime, timezone
from models.schemas import CarbonIntensityResponse

# Fictional but realistic fallback carbon intensity data (gCO2/kWh)
# Based on approximate real grid mixes for US regions
CARBON_DATA = {
    "CA": {"carbon_intensity_gco2_kwh": 215, "grid_source": "CAISO grid mix"},
    "TX": {"carbon_intensity_gco2_kwh": 380, "grid_source": "ERCOT grid mix"},
    "NY": {"carbon_intensity_gco2_kwh": 275, "grid_source": "NYISO grid mix"},
    "VA": {"carbon_intensity_gco2_kwh": 420, "grid_source": "Dominion Virginia"},
    "NC": {"carbon_intensity_gco2_kwh": 390, "grid_source": "Duke Energy Carolinas"},
    "AZ": {"carbon_intensity_gco2_kwh": 340, "grid_source": "APS Arizona"},
    "CO": {"carbon_intensity_gco2_kwh": 430, "grid_source": "Xcel Colorado"},
    "US": {"carbon_intensity_gco2_kwh": 386, "grid_source": "US average EIA"},
    "DEFAULT": {"carbon_intensity_gco2_kwh": 400, "grid_source": "Estimated regional average"},
}

router = APIRouter(prefix="/carbon", tags=["carbon"])


@router.get("/intensity", response_model=CarbonIntensityResponse)
async def get_carbon_intensity(region: str = "US"):
    region_key = region.upper()
    data = CARBON_DATA.get(region_key, CARBON_DATA["DEFAULT"])

    return CarbonIntensityResponse(
        region=region.upper(),
        carbon_intensity_gco2_kwh=data["carbon_intensity_gco2_kwh"],
        grid_source=data["grid_source"],
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
