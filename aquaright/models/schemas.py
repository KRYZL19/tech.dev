from pydantic import BaseModel, Field
from typing import List, Optional

# --- Fish Profiles ---

class TempRange(BaseModel):
    min: float
    max: float

class PHRange(BaseModel):
    min: float
    max: float

class FishProfileResponse(BaseModel):
    species: str
    common_name: str
    temp_range: TempRange
    ph_range: PHRange
    ammonia_tolerance: float
    nitrite_tolerance: float
    nitrate_tolerance: float
    size_inches: float
    aggression: str
    min_tank_gallons: int

# --- Cycle Status ---

class CycleStatusRequest(BaseModel):
    ammonia_ppm: float = Field(..., ge=0)
    nitrite_ppm: float = Field(..., ge=0)
    nitrate_ppm: float = Field(..., ge=0)
    day_number: int = Field(..., ge=1)

class CycleStatusResponse(BaseModel):
    cycle_phase: str
    phase_number: int
    biochemistry: str
    recommendations: List[str]
    is_cycled: bool

# --- Dose Calculate ---

class DoseCalculateRequest(BaseModel):
    tank_gallons: float = Field(..., gt=0)
    current_kh: float = Field(..., ge=0)
    target_kh: float = Field(..., gt=0)

class DoseCalculateResponse(BaseModel):
    baking_soda_grams: float
    baking_soda_tsp: float
    current_kh: float
    target_kh: float
    kh_increase: float
    warning: Optional[str] = None

# --- Max Stocking ---

class StockingRequest(BaseModel):
    tank_gallons: float = Field(..., gt=0)
    filter_gph: float = Field(..., gt=0)
    fish_species: List[str]

class StockingResponse(BaseModel):
    stocking_percentage: float
    bioload_score: float
    max_bioload: float
    current_bioload: float
    warnings: List[str]
    recommended_max: int
