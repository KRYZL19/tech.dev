"""Truck and offset carbon calculation routes."""

import math
from fastapi import APIRouter
from data.emission_factors import (
    TRUCK_EMISSION_FACTORS,
    TRUCK_FUEL_PER_100_TKM,
    TREE_SEQ_PER_YEAR,
    TREE_SEQ_TOTAL,
    TREE_COST_USD,
)
from models.schemas import (
    TruckCarbonRequest,
    TruckCarbonResponse,
    OffsetTreesRequest,
    OffsetTreesResponse,
)

router = APIRouter(tags=["transport & offset"])


# ── Truck ──────────────────────────────────────────────────────────────────#

@router.post("/api/v1/truck/carbon", response_model=TruckCarbonResponse)
def calc_truck_carbon(req: TruckCarbonRequest) -> TruckCarbonResponse:
    """
    Calculate CO2 emissions for road freight.

    Emission factors (kg CO2/t-km):
    - diesel standard: 0.062
    - diesel heavy:    0.080
    - LNG standard:    0.050
    - LNG heavy:       0.065
    - electric std:    0.035
    - electric heavy:  0.045
    """
    cargo_tons = req.cargo_kg / 1000.0
    factor = TRUCK_EMISSION_FACTORS.get(
        (req.fuel_type, req.truck_type), 0.062
    )
    co2_kg = factor * cargo_tons * req.distance_km

    # Estimate diesel litres consumed (approximate)
    tkm = cargo_tons * req.distance_km  # ton-km
    fuel_liters = (tkm / 100) * TRUCK_FUEL_PER_100_TKM if req.fuel_type == "diesel" else None

    return TruckCarbonResponse(
        co2_kg=round(co2_kg, 2),
        fuel_liters=round(fuel_liters, 1) if fuel_liters is not None else None,
    )


# ── Offset ─────────────────────────────────────────────────────────────────#

@router.post("/api/v1/offset/trees", response_model=OffsetTreesResponse)
def calc_offset_trees(req: OffsetTreesRequest) -> OffsetTreesResponse:
    """
    Estimate trees needed to naturally sequester CO2 emissions.

    Uses 21 kg CO2 absorbed per tree per year,
    over a 20-year growth window = 420 kg CO2/tree total.
    """
    trees_raw = req.co2_kg / TREE_SEQ_TOTAL
    years_needed = req.co2_kg / TREE_SEQ_PER_YEAR
    cost_usd = trees_raw * TREE_COST_USD

    return OffsetTreesResponse(
        co2_kg=round(req.co2_kg, 2),
        trees_needed=round(trees_raw, 3),
        trees_rounded_up=math.ceil(req.co2_kg / TREE_SEQ_TOTAL),
        cost_at_15_per_tree_usd=round(cost_usd, 2),
        years_to_offset=round(years_needed, 1),
    )
