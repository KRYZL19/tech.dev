"""Pydantic schemas for CLIMATEZ API."""

from datetime import date
from enum import Enum
from pydantic import BaseModel, Field


class ProbabilityLevel(str, Enum):
    """Frost probability level for growing season estimation."""
    P10 = 10  # 10% chance of kill (early date)
    P50 = 50  # 50% chance of kill
    P90 = 90  # 90% chance of kill (late date)


class ClimateNormalsResponse(BaseModel):
    """30-year climate normals response."""
    zipcode: str
    city: str
    state: str
    lat: float
    lon: float
    heating_dd: int = Field(description="Heating degree days (base 65°F)")
    cooling_dd: int = Field(description="Cooling degree days (base 65°F)")
    growing_days: int = Field(description="Average frost-free growing days")
    avg_precip_inches: float = Field(description="Annual average precipitation")
    avg_snow_inches: float = Field(description="Annual average snowfall")
    humidity_pct: int = Field(description="Average relative humidity")


class FrostDatesResponse(BaseModel):
    """Frost dates response."""
    zipcode: str
    city: str
    state: str
    avg_last_spring_frost: str | None = Field(description="Average last spring frost date (MM-DD)")
    avg_first_fall_frost: str | None = Field(description="Average first fall frost date (MM-DD)")
    growing_season_days: int = Field(description="Average growing season length")
    has_frost: bool = Field(description="Whether this location experiences frost")


class MonthlyPrecipitation(BaseModel):
    """Monthly precipitation data."""
    month: int = Field(ge=1, le=12)
    month_name: str
    precip_inches: float


class PrecipitationResponse(BaseModel):
    """Annual precipitation response."""
    zipcode: str
    city: str
    state: str
    annual_total_inches: float
    monthly: list[MonthlyPrecipitation]
    wettest_month: str
    wettest_inches: float
    driest_month: str
    driest_inches: float


class GrowingSeasonRequest(BaseModel):
    """Request for growing season estimation."""
    zipcode: str = Field(min_length=5, max_length=5, pattern=r"^\d{5}$")
    first_kill_probability_pct: int = Field(
        description="Probability of frost kill (10=early, 50=median, 90=late)",
        ge=10, le=90
    )


class GrowingSeasonResponse(BaseModel):
    """Growing season estimation response."""
    zipcode: str
    city: str
    state: str
    probability_pct: int
    estimated_last_spring_frost: str | None
    estimated_first_fall_frost: str | None
    growing_season_days: int
    frost_free_risk: str = Field(description="Risk level: low, medium, or high")
    recommendation: str


class ErrorResponse(BaseModel):
    """Error response."""
    error: str
    message: str
    status_code: int
