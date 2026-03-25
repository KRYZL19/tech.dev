"""Pydantic schemas for TIREMATCH API."""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal


class TireSizeSchema(BaseModel):
    width_mm: int
    aspect_ratio: int
    rim_diameter: int
    diameter_inches: float

    class Config:
        frozen = True


class FactoryTireSize(BaseModel):
    width_mm: int
    aspect_ratio: int
    rim_diameter: int
    sidewall_inches: float = Field(description="Sidewall height in inches")
    diameter_inches: float = Field(description="Overall tire diameter in inches")


class VehicleWheelSpec(BaseModel):
    bolt_pattern: str
    center_bore_mm: float
    offset_range_mm: dict
    lug_thread: str


class VehicleResponse(BaseModel):
    id: str
    year: int
    make: str
    model: str
    trims: List[str]
    factory_tires: List[FactoryTireSize]
    wheel_spec: VehicleWheelSpec
    tire_count: int = 4


class TireCompareRequest(BaseModel):
    tire1_size: str = Field(..., description="Tire size in format 'WIDTH/ASPECT RIM' e.g. '245/45R18'")
    tire2_size: str = Field(..., description="Second tire size for comparison")


class TireCompareResponse(BaseModel):
    tire1_parsed: TireSizeSchema
    tire2_parsed: TireSizeSchema
    diameter_diff_pct: float = Field(..., description="Diameter difference percentage")
    will_fit: bool = Field(..., description="True if diameter diff is within 3%")
    speedo_diff_mph: float = Field(..., description="Speedometer error in MPH at 60mph")
    verdict: str = Field(..., description="Human-readable verdict")


class WheelFitmentRequest(BaseModel):
    vehicle_id: str = Field(..., description="Vehicle ID e.g. 'honda_civic_2016'")
    wheel_size: int = Field(..., description="Wheel rim diameter in inches (e.g. 18)")
    offset_mm: int = Field(..., description="Wheel offset in mm")


class WheelFitmentResponse(BaseModel):
    vehicle_id: str
    wheel_size: int
    offset_mm: int
    fitment_verdict: Literal["fits", "fits_with_spacer", "rubbing_likely", "does_not_fit"]
    clearance_risk: Literal["none", "low", "medium", "high"]
    spacer_needed_mm: float = Field(..., description="Spacer needed (0 if no spacer required)")
    warnings: List[str] = []


class SizeParseResponse(BaseModel):
    raw: str
    width_mm: int
    aspect_ratio: int
    rim_diameter: int
    diameter_inches: float
    sidewall_inches: float
    circumference_inches: float
    revolutions_per_mile: int


class ErrorResponse(BaseModel):
    detail: str
    error_code: str
