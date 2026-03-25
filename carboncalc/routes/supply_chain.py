"""Supply-chain carbon summary route."""

from fastapi import APIRouter
from data.emission_factors import (
    SHIPPING_EMISSION_FACTORS,
    TRUCK_EMISSION_FACTORS,
    AVIATION_EMISSION_FACTORS,
    TREE_SEQ_TOTAL,
    TREE_COST_USD,
)
from models.schemas import SupplyChainSummaryRequest, SupplyChainSummaryResponse

router = APIRouter(prefix="/api/v1/supply-chain", tags=["supply chain"])


# Conversion: 1 nm = 1.852 km
NM_TO_KM = 1.852


@router.post("/summary", response_model=SupplyChainSummaryResponse)
def supply_chain_summary(req: SupplyChainSummaryRequest) -> SupplyChainSummaryResponse:
    """
    Calculate total CO2 for a multi-modal supply chain.

    Accepts mixed shipment types and returns:
    - Total CO2 in kg and tons
    - Cost to offset at $15/tree
    - Carbon intensity (kg CO2 per ton-km)
    """
    total_co2_kg = 0.0
    total_tkm = 0.0  # ton-km for intensity calc
    breakdown = []

    for s in req.shipments:
        co2_kg, tkm = _calc_segment(s.type, s.distance, s.cargo)
        total_co2_kg += co2_kg
        total_tkm += tkm

        breakdown.append({
            "type": s.type,
            "distance": s.distance,
            "cargo_tons": s.cargo,
            "co2_kg": round(co2_kg, 2),
        })

    total_tons = total_co2_kg / 1000.0
    offset_cost = (total_co2_kg / TREE_SEQ_TOTAL) * TREE_COST_USD
    intensity = total_co2_kg / total_tkm if total_tkm > 0 else 0.0

    return SupplyChainSummaryResponse(
        total_co2_kg=round(total_co2_kg, 2),
        total_co2_tons=round(total_tons, 4),
        offset_cost_usd=round(offset_cost, 2),
        carbon_intensity=round(intensity, 5),
        breakdown=breakdown,
    )


def _calc_segment(stype: str, distance: float, cargo_tons: float):
    """Return (co2_kg, ton_km) for a single shipment segment."""
    if stype == "container_ship":
        co2_g = SHIPPING_EMISSION_FACTORS["container"] * cargo_tons * distance
        co2_kg = co2_g / 1000.0
        tkm = cargo_tons * distance * NM_TO_KM
    elif stype == "bulk_carrier":
        co2_g = SHIPPING_EMISSION_FACTORS["bulk"] * cargo_tons * distance
        co2_kg = co2_g / 1000.0
        tkm = cargo_tons * distance * NM_TO_KM
    elif stype == "roro_vessel":
        co2_g = SHIPPING_EMISSION_FACTORS["roro"] * cargo_tons * distance
        co2_kg = co2_g / 1000.0
        tkm = cargo_tons * distance * NM_TO_KM
    elif stype == "truck_diesel":
        factor = TRUCK_EMISSION_FACTORS[("diesel", "standard")]
        co2_kg = factor * cargo_tons * distance
        tkm = cargo_tons * distance
    elif stype == "truck_lng":
        factor = TRUCK_EMISSION_FACTORS[("lng", "standard")]
        co2_kg = factor * cargo_tons * distance
        tkm = cargo_tons * distance
    elif stype == "aviation_short":
        co2_kg = AVIATION_EMISSION_FACTORS["short_haul"] * cargo_tons * distance
        tkm = cargo_tons * distance
    elif stype == "aviation_long":
        co2_kg = AVIATION_EMISSION_FACTORS["long_haul"] * cargo_tons * distance
        tkm = cargo_tons * distance
    else:
        co2_kg = 0.0
        tkm = 0.0

    return co2_kg, tkm
