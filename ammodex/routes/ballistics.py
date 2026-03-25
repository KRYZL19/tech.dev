from fastapi import APIRouter, HTTPException, Query
from typing import List
from data.ammo_data import AMMO_DATA, BULLET_DATA, CALIBERS, POWDER_DATA
from models.schemas import (
    AmmoSearchResult,
    AmmoDetail,
    PowderData,
    BulletInfo,
    CaliberList,
)

router = APIRouter(prefix="/api/v1", tags=["ballistics"])


@router.get("/ammo/search", response_model=List[AmmoSearchResult])
async def search_ammo(q: str = Query(..., description="Caliber to search for")):
    """Search ammunition by caliber. Returns all loads for matching caliber."""
    results = []
    q_lower = q.lower()
    for caliber, loads in AMMO_DATA.items():
        if q_lower in caliber.lower():
            for weight, bullet_type, velocity, bc in loads:
                results.append(
                    AmmoSearchResult(
                        caliber=caliber,
                        bullet_weight=weight,
                        bullet_type=bullet_type,
                        muzzle_velocity=velocity,
                        bc=bc,
                    )
                )
    if not results:
        raise HTTPException(status_code=404, detail=f"No ammo found for caliber: {q}")
    return results


@router.get("/ammo/{caliber}/{weight}", response_model=AmmoDetail)
async def get_ammo_detail(caliber: str, weight: int):
    """Get specific ammunition details by caliber and bullet weight."""
    if caliber not in AMMO_DATA:
        raise HTTPException(status_code=404, detail=f"Caliber not found: {caliber}")
    
    caliber_info = CALIBERS.get(caliber, {})
    for w, bullet_type, velocity, bc in AMMO_DATA.get(caliber, []):
        if w == weight:
            return AmmoDetail(
                caliber=caliber,
                bullet_weight=weight,
                bullet_type=bullet_type,
                muzzle_velocity=velocity,
                bc_g1=bc,
                caliber_name=caliber_info.get("name", caliber),
                case_length_mm=caliber_info.get("case_length", 0),
                bullet_diameter=caliber_info.get("bullet_diameter", 0),
            )
    
    raise HTTPException(
        status_code=404,
        detail=f"No ammo found for {caliber} with {weight}gr bullet"
    )


@router.get("/powder/{powder_name}", response_model=PowderData)
async def get_powder(powder_name: str):
    """Get powder data including max/min loads and burn rate."""
    if powder_name not in POWDER_DATA:
        raise HTTPException(status_code=404, detail=f"Powder not found: {powder_name}")
    
    data = POWDER_DATA[powder_name]
    return PowderData(name=powder_name, **data)


@router.get("/bullet/{caliber}", response_model=List[BulletInfo])
async def get_bullets(caliber: str):
    """List all bullets available for a caliber with BC values."""
    if caliber not in BULLET_DATA:
        raise HTTPException(status_code=404, detail=f"Caliber not found: {caliber}")
    
    results = []
    for weight, style, bc, diameter in BULLET_DATA[caliber]:
        results.append(
            BulletInfo(
                caliber=caliber,
                bullet_weight=weight,
                style=style,
                bc_g1=bc,
                diameter_inches=diameter,
            )
        )
    return results


@router.get("/calibers", response_model=List[CaliberList])
async def list_calibers():
    """List all available calibers."""
    return [
        CaliberList(caliber=cal, name=info.get("name", cal))
        for cal, info in CALIBERS.items()
    ]
