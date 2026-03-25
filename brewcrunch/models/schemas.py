"""Pydantic schemas for BREWCRUNCH API."""

from pydantic import BaseModel, Field
from typing import Optional, List


# ABV Calculator
class ABVRequest(BaseModel):
    og: float = Field(..., gt=0.9, lt=1.2, description="Original Gravity")
    fg: float = Field(..., gt=0.9, lt=1.2, description="Final Gravity")


class ABVResponse(BaseModel):
    abv: float = Field(..., description="Alcohol by Volume (%)")
    attenuation: float = Field(..., description="Apparent Attenuation (%)")


# IBU Calculator
class IBURequest(BaseModel):
    oz_hops: float = Field(..., gt=0, description="Ounces of hops")
    aa_percent: float = Field(..., gt=0, le=20, description="Alpha Acid %")
    boil_time_minutes: int = Field(..., gt=0, le=180, description="Boil time in minutes")
    og: float = Field(..., gt=0.9, lt=1.2, description="Original Gravity")
    volume_gallons: float = Field(..., gt=0, description="Batch volume in gallons")


class IBUResponse(BaseModel):
    ibu: float = Field(..., description="International Bitterness Units")


# OG Calculator
class OGRequest(BaseModel):
    pounds_grain: float = Field(..., gt=0, description="Total pounds of grain")
    ppg: float = Field(..., gt=0, le=45, description="Points per pound per gallon")
    efficiency_percent: float = Field(
        ..., gt=0, le=100, description="Mash efficiency %"
    )
    volume_gallons: float = Field(..., gt=0, description="Batch volume in gallons")


class OGResponse(BaseModel):
    og: float = Field(..., description="Estimated Original Gravity")
    og_points: float = Field(..., description="Gravity points before dilution")


# Style Check
class RecipeCheckRequest(BaseModel):
    og: float = Field(..., gt=0.9, lt=1.2, description="Original Gravity")
    fg: float = Field(..., gt=0.9, lt=1.2, description="Final Gravity")
    ibu: float = Field(..., ge=0, description="IBU value")
    abv: float = Field(..., ge=0, description="Alcohol by Volume %")


class StyleMatch(BaseModel):
    name: str
    category: str
    score: float = Field(..., ge=0, le=100, description="Match score 0-100")
    og_match: bool
    fg_match: bool
    abv_match: bool
    ibu_match: bool


class StyleCheckResponse(BaseModel):
    matches: List[StyleMatch]
    total_submitted: int


# Hop Data
class HopResponse(BaseModel):
    variety: str
    aa_percent: float
    type: str
    typical_use: str
    notes: Optional[str] = None
    substitutes: Optional[List[str]] = None


# Grain Data
class GrainResponse(BaseModel):
    variety: str
    ppg: float
    color_lovibond: float
    type: str
    notes: Optional[str] = None


# BJCP Style
class BJCP_style(BaseModel):
    id: int
    name: str
    category: str
    og_range: tuple
    fg_range: tuple
    abv_range: tuple
    ibu_range: tuple
    srm_range: Optional[tuple] = None
    description: Optional[str] = None


class StyleListResponse(BaseModel):
    styles: List[BJCP_style]
    total: int
