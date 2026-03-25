"""Calculator routes for BREWCRUNCH API."""

from fastapi import APIRouter, HTTPException
from models.schemas import (
    ABVRequest,
    ABVResponse,
    IBURequest,
    IBUResponse,
    OGRequest,
    OGResponse,
)

router = APIRouter(prefix="/calculate", tags=["Calculators"])


@router.post("/abv", response_model=ABVResponse)
async def calculate_abv(request: ABVRequest):
    """
    Calculate Alcohol by Volume (ABV) and attenuation.
    
    - **og**: Original Gravity (e.g., 1.050)
    - **fg**: Final Gravity (e.g., 1.010)
    """
    if request.fg >= request.og:
        raise HTTPException(
            status_code=400,
            detail="Final gravity must be less than original gravity",
        )
    
    # ABV formula: (OG - FG) * 131.25
    abv = (request.og - request.fg) * 131.25
    
    # Attenuation formula: ((OG - FG) / (OG - 1)) * 100
    attenuation = ((request.og - request.fg) / (request.og - 1)) * 100
    
    return ABVResponse(abv=round(abv, 2), attenuation=round(attenuation, 2))


@router.post("/ibu", response_model=IBUResponse)
async def calculate_ibu(request: IBURequest):
    """
    Calculate International Bitterness Units (IBU) using Tinseth formula.
    
    - **oz_hops**: Ounces of hops added
    - **aa_percent**: Alpha Acid percentage
    - **boil_time_minutes**: Boil time in minutes
    - **og**: Original Gravity
    - **volume_gallons**: Batch volume in gallons
    """
    if request.boil_time_minutes <= 0:
        raise HTTPException(
            status_code=400,
            detail="Boil time must be greater than 0",
        )
    
    # Tinseth Formula
    # Bigness factor = 1.65 * 0.000125^(OG - 1)
    # Boil time factor = (1 - e^(-0.04 * boil_time)) / 4.15
    # IBU = AA * oz * 7490 * Bigness * BoilTime / volume
    
    bigness_factor = 1.65 * (0.000125 ** (request.og - 1))
    boil_time_factor = (1 - pow(2.718, -0.04 * request.boil_time_minutes)) / 4.15
    
    ibu = (
        request.aa_percent
        * request.oz_hops
        * 7490
        * bigness_factor
        * boil_time_factor
        / request.volume_gallons
    )
    
    return IBUResponse(ibu=round(ibu, 1))


@router.post("/og", response_model=OGResponse)
async def calculate_og(request: OGRequest):
    """
    Estimate Original Gravity based on grain bill.
    
    - **pounds_grain**: Total pounds of grain
    - **ppg**: Points per pound per gallon (extract potential)
    - **efficiency_percent**: Mash efficiency percentage
    - **volume_gallons**: Batch volume in gallons
    """
    if request.efficiency_percent <= 0 or request.efficiency_percent > 100:
        raise HTTPException(
            status_code=400,
            detail="Efficiency must be between 0 and 100",
        )
    
    # Gravity points = pounds * ppg * (efficiency / 100) / volume
    og_points = (
        request.pounds_grain * request.ppg * (request.efficiency_percent / 100)
    ) / request.volume_gallons
    
    # Convert to specific gravity
    og = 1 + (og_points / 1000)
    
    return OGResponse(og=round(og, 4), og_points=round(og_points, 2))
