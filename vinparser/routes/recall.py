from fastapi import APIRouter, HTTPException
from models.schemas import ModelSpecsResponse
from data.vin_patterns import MODEL_SPECS, WMI_REGISTRY

router = APIRouter(prefix="/api/v1/model", tags=["Model"])


@router.get("/{make}/{year}/{model}", response_model=ModelSpecsResponse)
async def get_model_specs(make: str, year: int, model: str):
    """Get full specifications for a motorcycle by make, year, and model."""
    # Normalize: replace dashes/spaces and title case
    make_norm = make.replace("-", " ").title()
    model_norm = model.replace("-", " ").title()
    
    # Try exact match first (uppercase format like "MT-09")
    key = (make_norm, model.upper(), year)
    
    if key not in MODEL_SPECS:
        # Try with title case model
        key = (make_norm, model_norm, year)
    
    if key not in MODEL_SPECS:
        raise HTTPException(
            status_code=404,
            detail=f"Model '{model}' ({make_norm} {year}) not found in database. Try a different year or model name."
        )
    
    specs = MODEL_SPECS[key]
    
    # Find country from WMI registry
    country = "Unknown"
    for wmi, info in WMI_REGISTRY.items():
        if info["make"].lower() == make_norm.lower():
            country = info["country"]
            break
    
    return ModelSpecsResponse(
        make=make_norm,
        model=specs["model"],
        year=year,
        engine_cc=specs["engine_cc"],
        hp=specs["hp"],
        wet_weight_kg=specs["wet_weight_kg"],
        frame_type=specs["frame_type"],
        country=country
    )
