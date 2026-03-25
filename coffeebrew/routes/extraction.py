from fastapi import APIRouter, HTTPException
from models.schemas import ExtractionInput, ExtractionOutput, TDSCalibrateInput, TDSCalibrateOutput

router = APIRouter(prefix="/api/v1/extraction", tags=["extraction"])


@router.post("/calculate", response_model=ExtractionOutput)
def calculate_extraction(input_data: ExtractionInput):
    """
    Calculate extraction metrics from brew parameters.
    
    Uses the formula: Extraction % = (TDS% × Water) / Coffee Dose × 100
    
    Reference: Industry standard target is 18-21% extraction.
    - Below 18%: under-extracted (sour, weak)
    - Above 21%: over-extracted (bitter, harsh)
    """
    dose_g = input_data.dose_g
    water_ml = input_data.water_ml
    brew_time_seconds = input_data.brew_time_seconds
    temp_f = input_data.temp_f
    tds_percent = input_data.tds_percent
    
    # Calculate extraction percentage
    # TDS represents the ratio of dissolved coffee solids to total beverage
    # Extraction % = (TDS% × Water volume in g) / Coffee dose in g × 100
    # Note: 1ml water ≈ 1g for this calculation
    dissolved_solids_g = (tds_percent / 100) * water_ml
    extraction_percent = (dissolved_solids_g / dose_g) * 100
    
    # Strength ratio: ratio of coffee to water (higher = stronger)
    strength_ratio = dose_g / water_ml * 1000  # grams per liter equivalent
    
    # Yield percentage: what % of the coffee dose was extracted
    yield_percent = extraction_percent
    
    # Extraction quality flags
    over_extracted_bool = extraction_percent > 21.0
    under_extracted_bool = extraction_percent < 18.0
    
    return ExtractionOutput(
        extraction_percent=round(extraction_percent, 2),
        strength_ratio=round(strength_ratio, 2),
        yield_percent=round(yield_percent, 2),
        over_extracted_bool=over_extracted_bool,
        under_extracted_bool=under_extracted_bool
    )


@router.post("/calibrate", response_model=TDSCalibrateOutput)
def calibrate_tds(input_data: TDSCalibrateInput):
    """
    Calibrate TDS reading based on brew method and coffee type.
    
    Refractometers often need calibration adjustments based on:
    - Brew method (espresso vs drip have different soluble ratios)
    - Coffee freshness (stale coffee reads lower)
    - Calibration solution accuracy
    """
    tds = input_data.tds_reading
    coffee_type = input_data.coffee_type
    
    # Base calibration factors by brew method
    calibration_factors = {
        "espresso": 1.0,      # Already concentrated, standard reading
        "pourover": 0.95,     # Slight dilution adjustment
        "aeropress": 0.97,    # Similar to pourover
        "french_press": 0.92,  # Higher extraction, slight over-read bias
        "cold_brew": 0.88      # Different solubility profile
    }
    
    factor = calibration_factors.get(coffee_type, 1.0)
    calibrated_tds = tds * factor
    
    # Generate measurement notes
    notes_parts = []
    
    # Stale coffee detection (rough heuristic: espresso >45s, pourover >4min)
    # This is a simplified check - real stale detection needs more data
    if calibrated_tds < 1.0 and coffee_type != "cold_brew":
        notes_parts.append("Very low TDS may indicate stale coffee or calibration drift.")
        is_stale = True
    elif calibrated_tds > 15.0 and coffee_type == "pourover":
        notes_parts.append("Unusually high for pour-over. Check refractometer calibration.")
        is_stale = False
    else:
        notes_parts.append(f"Reading adjusted for {coffee_type} extraction characteristics.")
        is_stale = False
    
    # Add refractometer calibration warning if reading seems off
    if tds < 0.1:
        notes_parts.append("WARNING: Near-zero TDS detected. Verify refractometer is clean and calibrated.")
        is_stale = True
    
    notes_parts.append(f"Calibration factor applied: {factor}")
    
    return TDSCalibrateOutput(
        calibrated_tds=round(calibrated_tds, 3),
        measurement_notes=" ".join(notes_parts),
        is_stale_warning=is_stale
    )
