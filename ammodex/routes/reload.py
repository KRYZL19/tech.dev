from fastapi import APIRouter, HTTPException
from data.ammo_data import RELOAD_DATA, POWDER_DATA, CALIBERS
from models.schemas import ReloadRequest, ReloadResult

router = APIRouter(prefix="/api/v1", tags=["reloading"])


@router.post("/reload/calculate", response_model=ReloadResult)
async def calculate_reload(request: ReloadRequest):
    """
    Calculate starting and max powder loads for a given caliber, bullet weight, and powder.
    Returns estimated velocity based on bundled reference data.
    """
    caliber = request.caliber
    bullet_weight = request.bullet_weight
    powder_type = request.powder_type
    
    # Validate caliber
    if caliber not in RELOAD_DATA:
        raise HTTPException(
            status_code=404,
            detail=f"Caliber '{caliber}' not found. Available: {list(RELOAD_DATA.keys())}"
        )
    
    # Validate powder
    if powder_type not in POWDER_DATA:
        raise HTTPException(
            status_code=404,
            detail=f"Powder '{powder_type}' not found. Available: {list(POWDER_DATA.keys())}"
        )
    
    # Get reload data for this caliber
    caliber_data = RELOAD_DATA.get(caliber, {})
    
    # Check if bullet weight exists
    if bullet_weight not in caliber_data:
        available_weights = list(caliber_data.keys())
        raise HTTPException(
            status_code=404,
            detail=f"No load data for {bullet_weight}gr in {caliber}. Available weights: {available_weights}"
        )
    
    # Get powder data for this combo
    bullet_powder_data = caliber_data.get(bullet_weight, {})
    
    if powder_type not in bullet_powder_data:
        available_powders = list(bullet_powder_data.keys())
        raise HTTPException(
            status_code=404,
            detail=f"No load data for {powder_type} with {bullet_weight}gr in {caliber}. Available powders: {available_powders}"
        )
    
    min_charge, max_charge, velocity = bullet_powder_data[powder_type]
    
    return ReloadResult(
        caliber=caliber,
        bullet_weight=bullet_weight,
        powder_type=powder_type,
        starting_load_gr=min_charge,
        max_load_gr=max_charge,
        velocity_estimate_fps=velocity,
        notes="Always verify with published load data. Start low and work up."
    )


@router.get("/reload/calibers")
async def list_reloadable_calibers():
    """List all calibers with reloading data available."""
    return {"calibers": list(RELOAD_DATA.keys())}


@router.get("/reload/powders")
async def list_powders():
    """List all powders with reloading data available."""
    return {"powders": list(POWDER_DATA.keys())}
