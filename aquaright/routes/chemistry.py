from fastapi import APIRouter, HTTPException
from models.schemas import FishProfileResponse, DoseCalculateRequest, DoseCalculateResponse, StockingRequest, StockingResponse
from data.fish_profiles import get_fish_profile, FISH_PROFILES

router = APIRouter(prefix="/api/v1", tags=["chemistry"])

@router.get("/fish/{species}", response_model=FishProfileResponse)
async def get_fish(species: str):
    """Get chemistry tolerances for a fish species."""
    profile = get_fish_profile(species)
    if not profile:
        available = ", ".join(FISH_PROFILES.keys())
        raise HTTPException(status_code=404, detail=f"Species '{species}' not found. Available: {available}")
    
    return FishProfileResponse(species=species.lower(), **profile)


@router.post("/dose/calculate", response_model=DoseCalculateResponse)
async def calculate_dose(req: DoseCalculateRequest):
    """
    Calculate baking soda needed to raise KH.
    
    Baking soda (NaHCO3) provides ~17.8 ppm KH per gram per 10 gallons.
    1 tsp baking soda ≈ 4 grams
    """
    if req.target_kh <= req.current_kh:
        return DoseCalculateResponse(
            baking_soda_grams=0.0,
            baking_soda_tsp=0.0,
            current_kh=req.current_kh,
            target_kh=req.target_kh,
            kh_increase=0.0,
            warning="Target KH is at or below current KH."
        )
    
    kh_increase = req.target_kh - req.current_kh
    # grams needed = (kh_increase * tank_gallons * 10) / 17.8
    grams_needed = (kh_increase * req.tank_gallons * 10) / 17.8
    tsp = grams_needed / 4.0
    
    warning = None
    if req.target_kh > 12:
        warning = "KH above 12 can be stressful for many freshwater fish. Consider a more moderate target."
    
    return DoseCalculateResponse(
        baking_soda_grams=round(grams_needed, 2),
        baking_soda_tsp=round(tsp, 2),
        current_kh=req.current_kh,
        target_kh=req.target_kh,
        kh_increase=round(kh_increase, 2),
        warning=warning
    )


@router.post("/stocking/max", response_model=StockingResponse)
async def max_stocking(req: StockingRequest):
    """
    Calculate maximum stocking level based on tank size, filter flow, and fish species.
    
    Bioload is calculated using the "1 inch of fish per gallon" rule adjusted by:
    - aggression factor
    - filter flow (higher gph = better bioload capacity)
    """
    warnings = []
    current_bioload = 0.0
    valid_species = []
    
    for species in req.fish_species:
        profile = get_fish_profile(species.lower())
        if not profile:
            warnings.append(f"Unknown species: {species}")
            continue
        
        # Base bioload: 1 inch of fish per gallon
        bioload = profile["size_inches"]
        
        # Aggression factor: more aggressive fish need more space
        aggression_multiplier = {"peaceful": 1.0, "semi-aggressive": 1.2, "aggressive": 1.5}
        mult = aggression_multiplier.get(profile["aggression"], 1.0)
        bioload *= mult
        
        # Minimum tank size check
        if req.tank_gallons < profile["min_tank_gallons"]:
            warnings.append(f"{profile['common_name']} needs at least {profile['min_tank_gallons']} gallons.")
        
        current_bioload += bioload
        valid_species.append(species)
    
    # Filter efficiency: baseline is 4x tank volume, each additional 1x adds 10% capacity
    filter_capacity = 1.0 + ((req.filter_gph / req.tank_gallons) - 4) * 0.1
    filter_capacity = max(0.5, min(2.0, filter_capacity))  # cap between 0.5x and 2x
    
    max_bioload = req.tank_gallons * filter_capacity
    stocking_pct = (current_bioload / max_bioload) * 100 if max_bioload > 0 else 0
    
    if stocking_pct > 100:
        warnings.append("Tank is overstocked! Reduce fish count or upgrade filtration.")
    elif stocking_pct > 80:
        warnings.append("Tank is heavily stocked. Ensure excellent filtration and frequent water changes.")
    
    # Recommended max fish count (rough estimate)
    recommended_max = int(max_bioload / 2.0)
    
    return StockingResponse(
        stocking_percentage=round(stocking_pct, 1),
        bioload_score=round(current_bioload, 1),
        max_bioload=round(max_bioload, 1),
        current_bioload=round(current_bioload, 1),
        warnings=warnings,
        recommended_max=recommended_max
    )
