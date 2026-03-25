"""Sizing endpoints: ducts and equipment"""
from fastapi import APIRouter
from hvaccalc.models.schemas import (
    DuctSizeRequest,
    DuctSizeResponse,
    EquipmentSizeRequest,
    EquipmentSizeResponse,
)

router = APIRouter(prefix="/api/v1", tags=["sizing"])


# Duct sizing — equal friction lookup table
# Round duct capacity (CFM) at standard friction rates
# Based on ASHRAE/Ductulator charts
DUCT_LOOKUP = {
    # diameter_inches: {friction_rate: max_cfm}
    4: {0.06: 50, 0.08: 60, 0.10: 70, 0.12: 78},
    5: {0.06: 90, 0.08: 105, 0.10: 120, 0.12: 132},
    6: {0.06: 145, 0.08: 170, 0.10: 190, 0.12: 210},
    7: {0.06: 220, 0.08: 255, 0.10: 285, 0.12: 315},
    8: {0.06: 315, 0.08: 370, 0.10: 410, 0.12: 455},
    9: {0.06: 440, 0.08: 510, 0.10: 565, 0.12: 625},
    10: {0.06: 585, 0.08: 680, 0.10: 755, 0.12: 835},
    11: {0.06: 750, 0.08: 870, 0.10: 965, 0.12: 1065},
    12: {0.06: 940, 0.08: 1090, 0.10: 1210, 0.12: 1335},
    14: {0.06: 1320, 0.08: 1535, 0.10: 1705, 0.12: 1880},
    16: {0.06: 1780, 0.08: 2070, 0.10: 2300, 0.12: 2535},
    18: {0.06: 2300, 0.08: 2670, 0.10: 2965, 0.12: 3270},
    20: {0.06: 2900, 0.08: 3370, 0.10: 3740, 0.12: 4120},
    22: {0.06: 3570, 0.08: 4150, 0.10: 4610, 0.12: 5080},
    24: {0.06: 4320, 0.08: 5020, 0.10: 5570, 0.12: 6140},
}


def find_duct_diameter(cfm: float, friction_rate: float) -> tuple[float, int]:
    """Find minimum duct diameter that handles cfm at given friction rate."""
    diameters = sorted(DUCT_LOOKUP.keys())
    fr_rates = {0.06, 0.08, 0.10, 0.12}

    # Interpolate/extrapolate for non-standard friction rates
    fr_list = sorted(fr_rates)
    if friction_rate not in fr_list:
        # Find bounding rates
        fr_low = max(r for r in fr_rates if r <= friction_rate) if any(r <= friction_rate for r in fr_rates) else min(fr_rates)
        fr_high = min(r for r in fr_rates if r >= friction_rate) if any(r >= friction_rate for r in fr_rates) else max(fr_rates)
    else:
        fr_low = fr_high = friction_rate

    for d in diameters:
        rates = DUCT_LOOKUP[d]
        if friction_rate in rates:
            capacity = rates[friction_rate]
        else:
            # Interpolate between closest friction rates
            cap_low = rates.get(fr_low, 0)
            cap_high = rates.get(fr_high, 0)
            if fr_low == fr_high or cap_low == cap_high:
                capacity = cap_low
            else:
                ratio = (friction_rate - fr_low) / (fr_high - fr_low)
                capacity = cap_low + ratio * (cap_high - cap_low)

        if capacity >= cfm:
            return float(d), int(capacity)

    # Max out at 24"
    return 24.0, int(DUCT_LOOKUP[24].get(friction_rate, 5570))


@router.post("/duct/size", response_model=DuctSizeResponse)
def size_duct(req: DuctSizeRequest) -> DuctSizeResponse:
    """
    Size ductwork for a given BTU load.

    Uses the equal friction method to determine duct diameter.
    Returns CFM per run, recommended duct diameter, and velocity.
    """
    # Convert BTU to CFM: 1 ton cooling = 400 CFM = 12,000 BTU
    total_cfm = req.btu_load / 12
    cfm_per_run = round(total_cfm / req.num_runs, 1)

    diameter, _ = find_duct_diameter(cfm_per_run, req.friction_rate)

    # Calculate actual velocity in the selected duct
    # V = CFM / Area, Area = π * (D/24)^2  [converts D from inches to feet via /12, then area]
    duct_area = 3.14159 * (diameter / 24) ** 2
    velocity_fpm = int(cfm_per_run / duct_area)

    if velocity_fpm < 700:
        vel_category = "LOW"
    elif velocity_fpm < 1000:
        vel_category = "MEDIUM"
    else:
        vel_category = "HIGH"

    return DuctSizeResponse(
        cfm_per_run=cfm_per_run,
        duct_diameter_inches=diameter,
        velocity_fpm=velocity_fpm,
        friction_rate_used=req.friction_rate,
        total_cfm=round(total_cfm, 1),
        velocity_category=vel_category,
    )


# Equipment sizing
@router.post("/equipment/size", response_model=EquipmentSizeResponse)
def size_equipment(req: EquipmentSizeRequest) -> EquipmentSizeResponse:
    """
    Recommend HVAC equipment size based on load calculations.

    Checks against industry standard sizes and flags oversizing/undersizing.
    """
    tons = req.cooling_btu / 12000

    # Round to nearest standard size
    standard_tons = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.5, 10.0]

    # Find closest standard size
    closest = min(standard_tons, key=lambda x: abs(x - tons))
    # Only recommend up if >10% over, down if >15% under
    if tons > closest * 1.1:
        recommended_tons = min([t for t in standard_tons if t >= tons], default=closest)
    elif tons < closest * 0.85:
        recommended_tons = max([t for t in standard_tons if t <= tons], default=closest)
    else:
        recommended_tons = closest

    recommended_btu = recommended_tons * 12000
    oversize_btu = max(0, int(recommended_btu - req.cooling_btu))
    oversize_warning = recommended_btu > req.cooling_btu * 1.15
    undersize_warning = recommended_btu < req.cooling_btu * 0.85

    # Format unit size string
    if req.equipment_type == "central_ac":
        unit_str = f"{recommended_tons}-ton AC ({recommended_btu:.0f} BTU)"
        if req.efficiency_rating >= 16:
            unit_str += f" SEER2 {req.efficiency_rating}"
    elif req.equipment_type == "heat_pump":
        unit_str = f"{recommended_tons}-ton Heat Pump"
        if req.efficiency_rating >= 14:
            unit_str += f" {req.efficiency_rating} HSPF2"
    elif req.equipment_type == "furnace":
        heating_kbtu = req.heating_btu / 1000
        unit_str = f"{int(heating_kbtu)}-kBTU Furnace"
        if req.efficiency_rating:
            unit_str += f" {req.efficiency_rating}% AFUE"
    elif req.equipment_type == "boiler":
        heating_kbtu = req.heating_btu / 1000
        unit_str = f"{int(heating_kbtu)}-kBTU Boiler"
        if req.efficiency_rating:
            unit_str += f" {req.efficiency_rating}% AFUE"
    else:
        unit_str = f"{recommended_tons} tons"

    return EquipmentSizeResponse(
        cooling_tons=round(recommended_tons, 2),
        heating_kbtu=round(req.heating_btu / 1000, 1),
        recommended_unit_size=unit_str,
        oversize_warning=oversize_warning,
        undersize_warning=undersize_warning,
        oversize_btu=oversize_btu,
    )


# Climate zone lookup
@router.get("/climate/{zipcode}", tags=["climate"])
def get_climate_by_zipcode(zipcode: str):
    """Look up climate zone data by ZIP code."""
    from hvaccalc.data.climate_zones import CLIMATE_ZONES, get_zone_for_zipcode

    zone = get_zone_for_zipcode(zipcode)
    if zone is None:
        return {
            "zipcode": zipcode,
            "found": False,
            "message": "ZIP code not in database. Please specify climate_zone manually.",
            "all_zones": list(CLIMATE_ZONES.keys()),
        }

    zone_data = CLIMATE_ZONES[zone]
    return {
        "zipcode": zipcode,
        "found": True,
        "climate_zone": zone,
        "zone_name": zone_data["name"],
        "cooling_design_temp_f": zone_data["cooling_design_temp_f"],
        "heating_design_temp_f": zone_data["heating_design_temp_f"],
        "hdd_base_65": zone_data["hdd_base_65"],
        "cdd_base_65": zone_data["cdd_base_65"],
        "tons_per_sqft": zone_data["tons_per_sqft"],
    }
