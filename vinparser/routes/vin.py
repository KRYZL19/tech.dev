from fastapi import APIRouter, HTTPException
from models.schemas import VINDecodeRequest, VINDecodeResponse, VINValidateRequest, VINValidateResponse
from data.vin_patterns import WMI_REGISTRY, YEAR_CODES, CHECK_DIGIT_WEIGHTS, TRANSLITERATION, MODEL_SPECS
from typing import Optional
import re

router = APIRouter(prefix="/api/v1/vin", tags=["VIN"])


def calculate_check_digit(vin: str) -> str:
    """Calculate the expected check digit for a VIN."""
    total = 0
    for i, char in enumerate(vin, 1):
        if i == 9:
            continue  # Skip check digit position
        value = TRANSLITERATION.get(char.upper(), 0)
        total += value * CHECK_DIGIT_WEIGHTS[i]
    remainder = total % 11
    if remainder == 10:
        return "X"
    return str(remainder)


def extract_wmi(vin: str) -> Optional[dict]:
    """Extract WMI info from VIN."""
    wmi = vin[:3].upper()
    if wmi in WMI_REGISTRY:
        return WMI_REGISTRY[wmi]
    # Try 2-char WMI
    wmi2 = vin[:2].upper()
    for key in WMI_REGISTRY:
        if key.startswith(wmi2):
            return WMI_REGISTRY[key]
    return {"make": "Unknown", "country": "Unknown"}


def infer_model_from_vds(vin: str, make: str, year: int) -> str:
    """Infer model from VDS (characters 4-8) - simplified heuristic."""
    vds = vin[3:9].upper()
    # Common model indicators in VDS
    if "MT" in vds or "FJ" in vds:
        return "MT-09" if "09" in vds else "MT-07"
    if "R1" in vds or "1R" in vds:
        return "R1"
    if "NIN" in vds or "ZX" in vds:
        return "Ninja ZX-10R" if "10" in vds else "Ninja 400"
    if "CB" in vds:
        return "CB650R" if "65" in vds else "CB500F"
    if "GSX" in vds or "SV6" in vds:
        return "GSX-R1000" if "100" in vds else "SV650"
    if "IR" in vds or "88" in vds:
        return "Iron 883"
    if "SP" in vds and "12" in vds:
        return "Sportster S"
    if "S1" in vds or "SS" in vds:
        return "S1000RR"
    if "RG" in vds or "GS" in vds:
        return "R1250GS"
    if "PA" in vds or "V4" in vds:
        return "Panigale V4"
    if "MN" in vds or "MO" in vds:
        return "Monster"
    if "SD" in vds or "KR" in vds:
        return "1290 Super Duke R"
    if "DU" in vds or "39" in vds:
        return "390 Duke"
    if "TR" in vds or "ST" in vds:
        return "Street Triple RS"
    if "BN" in vds or "BO" in vds:
        return "Bonneville T120"
    return f"{make} Model"


@router.post("/decode", response_model=VINDecodeResponse)
async def decode_vin(request: VINDecodeRequest):
    """Decode a motorcycle VIN to extract make, model, year, specs."""
    vin = request.vin.upper().strip()
    
    # Basic format validation
    if len(vin) != 17:
        raise HTTPException(status_code=400, detail="VIN must be exactly 17 characters")
    
    if not re.match(r'^[A-HJ-NPR-Z0-9]{17}$', vin):
        raise HTTPException(status_code=400, detail="VIN contains invalid characters (I, O, Q not allowed)")
    
    # Extract WMI
    wmi_info = extract_wmi(vin)
    make = wmi_info["make"]
    country = wmi_info["country"]
    
    # Extract year (character 10)
    year_char = vin[9].upper()
    if year_char in YEAR_CODES:
        year = YEAR_CODES[year_char]
    else:
        raise HTTPException(status_code=400, detail=f"Invalid year character: {year_char}")
    
    # Plant code (character 11)
    plant = vin[10].upper()
    
    # Sequential number (characters 12-17)
    sequential_number = vin[11:17]
    
    # Infer model
    model = infer_model_from_vds(vin, make, year)
    
    # Look up specs
    key = (make, model, year)
    if key in MODEL_SPECS:
        specs = MODEL_SPECS[key]
    else:
        # Try to find closest year
        for y in [year - 1, year + 1, year - 2, year + 2]:
            alt_key = (make, model, y)
            if alt_key in MODEL_SPECS:
                specs = MODEL_SPECS[alt_key]
                break
        else:
            # Default specs
            specs = {
                "engine_cc": 0,
                "hp": 0,
                "wet_weight_kg": 0,
                "frame_type": "Unknown",
                "model": model
            }
    
    return VINDecodeResponse(
        make=make,
        model=specs["model"],
        year=year,
        engine_cc=specs["engine_cc"],
        hp=specs["hp"],
        wet_weight_kg=specs["wet_weight_kg"],
        frame_type=specs["frame_type"],
        country=country,
        plant=plant,
        sequential_number=sequential_number,
        vin=vin
    )


@router.post("/validate", response_model=VINValidateResponse)
async def validate_vin(request: VINValidateRequest):
    """Validate a motorcycle VIN format and check digit."""
    vin = request.vin.upper().strip()
    
    # Basic format validation
    valid_format = len(vin) == 17 and bool(re.match(r'^[A-HJ-NPR-Z0-9]{17}$', vin))
    
    if not valid_format:
        return VINValidateResponse(
            valid_format=False,
            check_digit_correct=False,
            country_of_origin="Unknown",
            year_char="Unknown",
            vin=vin
        )
    
    # Extract WMI info
    wmi_info = extract_wmi(vin)
    country_of_origin = wmi_info["country"]
    
    # Year character
    year_char = vin[9].upper()
    if year_char not in YEAR_CODES:
        year_char = "Invalid"
    
    # Check digit validation
    check_digit_correct = False
    if vin[8].upper() == calculate_check_digit(vin):
        check_digit_correct = True
    
    return VINValidateResponse(
        valid_format=True,
        check_digit_correct=check_digit_correct,
        country_of_origin=country_of_origin,
        year_char=year_char,
        vin=vin
    )
