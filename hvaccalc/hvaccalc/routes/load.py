"""Residential load calculation endpoints"""
from fastapi import APIRouter, HTTPException
from hvaccalc.data.climate_zones import CLIMATE_ZONES, get_closest_r_factor
from hvaccalc.models.schemas import (
    ResidentialLoadRequest,
    ResidentialLoadResponse,
)

router = APIRouter(prefix="/api/v1/load", tags=["load"])


@router.post("/residential", response_model=ResidentialLoadResponse)
def calculate_residential_load(req: ResidentialLoadRequest) -> ResidentialLoadResponse:
    """
    Calculate heating and cooling load for a residential property.

    Uses IECC 2021 climate zone data with Manual J simplified methodology.
    Factors in floor area, ceiling height, insulation, climate zone, occupancy,
    and number of exterior walls.
    """
    zone_data = CLIMATE_ZONES[req.climate_zone]
    r_factor = get_closest_r_factor(req.insulation_r_value)

    # Base cooling BTU/sqft adjusted for insulation
    base_cooling_btu_sqft = zone_data["btu_per_sqft_cooling"] * r_factor["cooling"]

    # Base heating BTU/sqft adjusted for insulation
    base_heating_btu_sqft = zone_data["btu_per_sqft_heating"] * r_factor["heating"]

    # Ceiling height adjustment (>8ft adds load)
    ceiling_multiplier = 1.0 + (req.ceiling_height_ft - 8.0) * 0.03

    # Exterior wall adjustment (each exterior wall adds infiltration/ conduction load)
    # Baseline assumes 1 exterior wall. Adjust proportionally.
    wall_multiplier = 1.0 + (req.num_exterior_walls - 1) * 0.08

    # Occupant load (sensible + latent heat per person)
    # ~400 BTU/person sensible + ~200 BTU/person latent (cooling)
    # ~250 BTU/person heating
    occupant_cooling = req.num_occupants * 600
    occupant_heating = req.num_occupants * 250

    # Calculate totals
    total_cooling = int(
        req.sqft
        * base_cooling_btu_sqft
        * ceiling_multiplier
        * wall_multiplier
        + occupant_cooling
    )

    total_heating = int(
        req.sqft
        * base_heating_btu_sqft
        * ceiling_multiplier
        * wall_multiplier
        + occupant_heating
    )

    # Convert to tons (1 ton = 12,000 BTU)
    tons_ac = round(total_cooling / 12000, 2)

    # CFM: 400 CFM per ton of cooling (nominal)
    cfm_cooling = int(tons_ac * 400)

    # Oversize check: compare against rule-of-thumb (400-450 sqft/ton)
    sqft_per_ton = zone_data["tons_per_sqft"]
    rule_of_thumb_tons = req.sqft / sqft_per_ton
    oversize_warning = tons_ac > rule_of_thumb_tons * 1.15

    return ResidentialLoadResponse(
        cooling_btu=total_cooling,
        heating_btu=total_heating,
        tons_ac_needed=tons_ac,
        cfm_cooling=cfm_cooling,
        oversize_warning=oversize_warning,
        methodology="IECC 2021 / Manual J simplified",
    )
