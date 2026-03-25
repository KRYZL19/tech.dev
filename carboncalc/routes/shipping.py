"""Shipping carbon calculation routes."""

from fastapi import APIRouter
from data.emission_factors import SHIPPING_EMISSION_FACTORS, TRUCK_CO2_PER_TKM
from models.schemas import ShipCarbonRequest, ShipCarbonResponse

router = APIRouter(prefix="/api/v1/ship", tags=["shipping"])


@router.post("/carbon", response_model=ShipCarbonResponse)
def calc_ship_carbon(req: ShipCarbonRequest) -> ShipCarbonResponse:
    """
    Calculate CO2 emissions for ocean freight.

    Uses IMO 4th GHG Study emission factors:
    - Container ship: 0.016 g CO2/t-nm
    - Bulk carrier:   0.006 g CO2/t-nm
    - Ro-ro vessel:   0.022 g CO2/t-nm
    """
    factor_g = SHIPPING_EMISSION_FACTORS[req.vessel_type]  # g CO2/t-nm
    co2_g = factor_g * req.cargo_tons * req.distance_nm
    co2_kg = co2_g / 1000.0
    co2_tons = co2_kg / 1000.0

    # Compare vs heavy diesel truck (kg CO2/t-km)
    # Convert nm to km for comparison: 1 nm = 1.852 km
    distance_km = req.distance_nm * 1.852
    truck_co2_kg = TRUCK_CO2_PER_TKM * req.cargo_tons * distance_km

    savings_pct = ((truck_co2_kg - co2_kg) / truck_co2_kg) * 100 if truck_co2_kg > 0 else 0.0

    return ShipCarbonResponse(
        co2_kg=round(co2_kg, 2),
        co2_tons=round(co2_tons, 4),
        comparison_vs_truck_kg=round(truck_co2_kg, 2),
        savings_vs_truck_pct=round(savings_pct, 1),
    )
