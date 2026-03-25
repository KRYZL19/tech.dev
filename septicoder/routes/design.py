from fastapi import APIRouter, HTTPException
from models.schemas import PercolateInput, PercolateOutput, SystemSizeInput, SystemSizeOutput
from data.soil_data import SOIL_TYPES, SYSTEM_SIZING

router = APIRouter(prefix="/api/v1", tags=["design"])


@router.post("/percolate", response_model=PercolateOutput)
async def calculate_percolation(input_data: PercolateInput):
    """
    Calculate percolation rate and determine system approval.

    - **soil_type**: sand, loamy sand, sandy loam, loam, silt loam, or clay
    - **drainage_area_sqft**: The area available for drainage in square feet
    """
    soil = input_data.soil_type.lower()
    if soil not in SOIL_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown soil type. Must be one of: {', '.join(SOIL_TYPES.keys())}"
        )

    soil_info = SOIL_TYPES[soil]
    perc_rate = soil_info["perc_rate"]
    recommendations = []

    # Approval logic based on perc rate
    if perc_rate <= 25:
        approved = True
        status = "APPROVED"
        recommendations.append(f"Excellent: {perc_rate} min/inch rate is ideal for conventional systems.")
        if soil in ["sand"]:
            recommendations.append("Consider a standard conventional septic system.")
    elif perc_rate <= 60:
        approved = True
        status = "APPROVED_WITH_CONDITIONS"
        recommendations.append(f"Acceptable: {perc_rate} min/inch rate requires careful drainfield sizing.")
        recommendations.append("Consider chambered or drip distribution systems for even effluent dispersal.")
    else:
        approved = False
        status = "DENIED"
        recommendations.append(f"Warning: {perc_rate} min/inch rate is too slow for standard systems.")
        recommendations.append("Specialized engineering required. Consider mound, at-grade, or aerobic systems.")
        recommendations.append("A percolation test by a licensed engineer is strongly recommended.")

    # Add drainage area recommendation
    if input_data.drainage_area_sqft < 1000:
        recommendations.append("Drainage area may be insufficient. Minimum 1000 sqft recommended for most systems.")
    elif input_data.drainage_area_sqft >= 2000:
        recommendations.append("Good drainage area available. Allows flexibility in system design.")

    return PercolateOutput(
        soil_type=soil,
        drainage_area_sqft=input_data.drainage_area_sqft,
        percolation_rate_min_per_inch=perc_rate,
        approved=approved,
        status=status,
        recommendations=recommendations,
    )


@router.post("/system/size", response_model=SystemSizeOutput)
async def size_system(input_data: SystemSizeInput):
    """
    Calculate required septic system sizing.

    - **bedrooms**: Number of bedrooms (1-10)
    - **soil_type**: sand, loamy sand, sandy loam, loam, silt loam, or clay
    - **lot_sqft**: Total lot size in square feet
    - **percolation_min_inch**: Percolation rate from a perc test
    """
    soil = input_data.soil_type.lower()

    # Get tank size based on bedrooms
    bedrooms = input_data.bedrooms
    tank_size = SYSTEM_SIZING["tank_size_gallons"].get(bedrooms, 2000)

    # Calculate daily flow
    daily_flow = bedrooms * SYSTEM_SIZING["daily_flow_gallons_per_bedroom"]

    # Calculate drainfield requirement
    # Base: 2 sqft per gallon, adjusted by perc rate
    base_drainfield = daily_flow * SYSTEM_SIZING["drainfield_sqft_per_gallon"]

    # Perc rate multiplier: faster (lower) is better
    if input_data.percolation_min_inch <= 10:
        perc_multiplier = 0.8
    elif input_data.percolation_min_inch <= 30:
        perc_multiplier = 1.0
    elif input_data.percolation_min_inch <= 60:
        perc_multiplier = 1.2
    elif input_data.percolation_min_inch <= 90:
        perc_multiplier = 1.5
    else:
        perc_multiplier = 2.0

    required_drainfield = base_drainfield * perc_multiplier

    warnings = []

    # Lot size check
    if input_data.lot_sqft < required_drainfield * 2:
        warnings.append(f"Lot may be too small. Recommended minimum: {required_drainfield * 2:.0f} sqft for this system.")

    # Perc rate warnings
    if input_data.percolation_min_inch > 90:
        warnings.append("Perc rate >90 min/inch: advanced system (mound/at-grade/aerobic) strongly recommended.")
    elif input_data.percolation_min_inch > 60:
        warnings.append("Perc rate >60 min/inch: drip or mound system may be required.")

    # Generate recommendation
    if perc_multiplier <= 1.0:
        recommendation = f"Standard conventional system recommended. {required_drainfield:.0f} sqft drainfield with {tank_size}-gallon tank."
    elif perc_multiplier <= 1.2:
        recommendation = f"Chambered system recommended for better effluent distribution. {required_drainfield:.0f} sqft drainfield."
    else:
        recommendation = f"Advanced system required. Consider drip or mound system with {required_drainfield:.0f}+ sqft drainfield."

    return SystemSizeOutput(
        bedrooms=bedrooms,
        soil_type=soil,
        lot_sqft=input_data.lot_sqft,
        required_drainfield_sqft=round(required_drainfield, 1),
        tank_size_gallons=tank_size,
        daily_flow_gallons=daily_flow,
        recommendation=recommendation,
        warnings=warnings,
    )
