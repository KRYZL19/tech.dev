from pydantic import BaseModel, Field
from typing import Optional, List


class ExtractionInput(BaseModel):
    dose_g: float = Field(..., gt=0, description="Coffee dose in grams")
    water_ml: float = Field(..., gt=0, description="Water volume in ml")
    brew_time_seconds: float = Field(..., gt=0, description="Brew time in seconds")
    temp_f: float = Field(..., ge=32, le=220, description="Water temperature in Fahrenheit")
    tds_percent: float = Field(..., ge=0, le=100, description="Total Dissolved Solids percentage")


class ExtractionOutput(BaseModel):
    extraction_percent: float
    strength_ratio: float
    yield_percent: float
    over_extracted_bool: bool
    under_extracted_bool: bool


class DoseOptimizeInput(BaseModel):
    brew_method: str = Field(..., pattern="^(espresso|pourover|aeropress|french_press|cold_brew)$")
    target_extraction_pct: float = Field(..., ge=15, le=30, description="Target extraction percentage")
    tds_target_percent: float = Field(..., ge=0.5, le=20, description="Target TDS percentage")


class DoseOptimizeOutput(BaseModel):
    dose_g: float
    water_ml: float
    temp_f: float
    grind_size_description: str


class BeanProfile(BaseModel):
    origin: str
    roast_level: str
    altitude_m: int
    process: str
    flavor_notes: List[str]
    ideal_temp_range: str
    ideal_extraction_range: str


class TDSCalibrateInput(BaseModel):
    tds_reading: float = Field(..., ge=0, le=100, description="Raw TDS reading from refractometer")
    coffee_type: str = Field(..., pattern="^(espresso|pourover|aeropress|french_press|cold_brew)$")


class TDSCalibrateOutput(BaseModel):
    calibrated_tds: float
    measurement_notes: str
    is_stale_warning: bool


class BrewMethod(BaseModel):
    name: str
    dose_range_g: str
    water_range_ml: str
    temp_f_range: str
    brew_time_range: str
    pressure_bar: Optional[float] = None
