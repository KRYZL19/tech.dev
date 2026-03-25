from fastapi import APIRouter, HTTPException
from models.schemas import DoseOptimizeInput, DoseOptimizeOutput, BeanProfile, BrewMethod
from data.bean_profiles import BEAN_PROFILES, BREW_METHODS

router = APIRouter(prefix="/api/v1", tags=["dosing"])


@router.post("/dose/optimize", response_model=DoseOptimizeOutput)
def optimize_dose(input_data: DoseOptimizeInput):
    """
    Calculate optimal dose parameters for a target extraction and TDS.
    
    Returns dose (g), water (ml), temperature (°F), and grind description.
    """
    brew_method = input_data.brew_method
    target_extraction = input_data.target_extraction_pct
    tds_target = input_data.tds_target_percent
    
    # Brew method presets
    method_params = {
        "espresso": {
            "default_dose_g": 18.0,
            "default_water_ml": 36.0,
            "default_temp_f": 200.0,
            "ratio_range": (1.5, 2.5),
            "grind": "Fine espresso grind"
        },
        "pourover": {
            "default_dose_g": 22.0,
            "default_water_ml": 360.0,
            "default_temp_f": 200.0,
            "ratio_range": (15, 17),
            "grind": "Medium-fine grind (sea salt to table salt)"
        },
        "aeropress": {
            "default_dose_g": 17.0,
            "default_water_ml": 220.0,
            "default_temp_f": 185.0,
            "ratio_range": (12, 15),
            "grind": "Fine-medium grind (smaller than pour-over)"
        },
        "french_press": {
            "default_dose_g": 45.0,
            "default_water_ml": 700.0,
            "default_temp_f": 200.0,
            "ratio_range": (14, 16),
            "grind": "Coarse grind (raw sugar texture)"
        },
        "cold_brew": {
            "default_dose_g": 120.0,
            "default_water_ml": 1000.0,
            "default_temp_f": 68.0,
            "ratio_range": (7, 10),
            "grind": "Extra coarse (coarse pepper)"
        }
    }
    
    params = method_params.get(brew_method)
    if not params:
        raise HTTPException(status_code=400, detail=f"Unknown brew method: {brew_method}")
    
    # Adjust based on target extraction and TDS
    dose_g = params["default_dose_g"]
    water_ml = params["default_water_ml"]
    temp_f = params["default_temp_f"]
    
    # Fine-tune for extraction target
    # Higher extraction target = coarser grind (for immersion) or longer brew
    # Lower extraction target = finer grind or shorter brew
    
    if brew_method == "espresso":
        # TDS target heavily influences ratio
        if tds_target > 10:
            water_ml = dose_g * 1.5  # ristretto-style
        elif tds_target < 8:
            water_ml = dose_g * 2.5  # lungo-style
        else:
            water_ml = dose_g * 2.0  # normshot
        
        # Extraction adjustment
        if target_extraction < 18:
            params["grind"] = "Very fine grind"
        elif target_extraction > 22:
            params["grind"] = "Coarser fine grind"
    
    elif brew_method == "pourover":
        # Adjust ratio for TDS target
        target_ratio = water_ml / dose_g
        if tds_target > 1.5:
            target_ratio = 14  # Stronger brew
        elif tds_target < 1.2:
            target_ratio = 17  # Lighter brew
        
        water_ml = dose_g * target_ratio
        
        if target_extraction < 18:
            params["grind"] = "Finer grind (faster extraction)"
        elif target_extraction > 21:
            params["grind"] = "Coarser grind (slower extraction)"
    
    elif brew_method == "french_press":
        # French press extraction is more forgiving
        if target_extraction < 18:
            params["grind"] = "Medium-coarse (less coarse than usual)"
        elif target_extraction > 22:
            params["grind"] = "Very coarse (minimize extraction)"
    
    elif brew_method == "cold_brew":
        temp_f = 68  # Room temp or cold
        if target_extraction > 22:
            params["grind"] = "Medium-coarse (long steep, control extraction)"
        else:
            params["grind"] = "Coarse (standard cold brew)"
    
    return DoseOptimizeOutput(
        dose_g=round(dose_g, 1),
        water_ml=round(water_ml, 1),
        temp_f=round(temp_f, 1),
        grind_size_description=params["grind"]
    )


@router.get("/beans/{origin}", response_model=BeanProfile)
def get_bean_profile(origin: str):
    """
    Get bean profile by origin identifier (e.g., 'ethiopia_yirgacheffe').
    """
    normalized = origin.lower().strip()
    
    # Try direct match first
    if normalized in BEAN_PROFILES:
        return BeanProfile(**BEAN_PROFILES[normalized])
    
    # Try partial/fuzzy match
    for key, profile in BEAN_PROFILES.items():
        if normalized in key or key.replace("_", " ") == normalized:
            return BeanProfile(**profile)
    
    # Try matching by full origin name
    for key, profile in BEAN_PROFILES.items():
        if normalized in profile["origin"].lower():
            return BeanProfile(**profile)
    
    available = ", ".join(sorted(BEAN_PROFILES.keys()))
    raise HTTPException(
        status_code=404,
        detail=f"Bean origin '{origin}' not found. Available: {available}"
    )


@router.get("/methods/{method}", response_model=BrewMethod)
def get_brew_method(method: str):
    """
    Get brew method parameters by method name.
    """
    normalized = method.lower().strip().replace(" ", "_")
    
    if normalized in BREW_METHODS:
        data = BREW_METHODS[normalized]
        return BrewMethod(**data)
    
    # Try partial match
    for key, data in BREW_METHODS.items():
        if normalized in key or key.replace("_", " ") == normalized:
            return BrewMethod(**data)
    
    available = ", ".join(sorted(BREW_METHODS.keys()))
    raise HTTPException(
        status_code=404,
        detail=f"Brew method '{method}' not found. Available: {available}"
    )
