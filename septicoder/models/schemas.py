from pydantic import BaseModel, Field, field_validator
from typing import Literal


class PercolateInput(BaseModel):
    soil_type: str = Field(..., description="Soil type: sand, loamy sand, sandy loam, loam, silt loam, clay")
    drainage_area_sqft: float = Field(..., gt=0, description="Drainage area in square feet")


class PercolateOutput(BaseModel):
    soil_type: str
    drainage_area_sqft: float
    percolation_rate_min_per_inch: float
    approved: bool
    status: str
    recommendations: list[str]


class SystemSizeInput(BaseModel):
    bedrooms: int = Field(..., ge=1, le=10)
    soil_type: str = Field(..., description="Soil type: sand, loamy sand, sandy loam, loam, silt loam, clay")
    lot_sqft: float = Field(..., gt=0)
    percolation_min_inch: float = Field(..., gt=0, description="Percolation rate in minutes per inch")

    @field_validator("soil_type")
    @classmethod
    def validate_soil(cls, v):
        allowed = ["sand", "loamy sand", "sandy loam", "loam", "silt loam", "clay"]
        if v.lower() not in allowed:
            raise ValueError(f"soil_type must be one of: {', '.join(allowed)}")
        return v.lower()


class SystemSizeOutput(BaseModel):
    bedrooms: int
    soil_type: str
    lot_sqft: float
    required_drainfield_sqft: float
    tank_size_gallons: int
    daily_flow_gallons: float
    recommendation: str
    warnings: list[str]


class PermitChecklistInput(BaseModel):
    state: str = Field(..., min_length=2, max_length=2)
    county: str = Field(..., min_length=1)
    system_type: str = Field(..., description="conventional, chambered, drip, mound, at-grade, aerobic")
    bedrooms: int = Field(..., ge=1, le=10)


class PermitChecklistOutput(BaseModel):
    state: str
    county: str
    system_type: str
    required_permits: list[str]
    required_inspections: list[str]
    setbacks: dict
    fees_estimate: str
    timeline: str
    notes: list[str]
