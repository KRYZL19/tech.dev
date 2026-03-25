from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class TrackPoint(BaseModel):
    lat: float
    lon: float
    date: str
    max_wind_kt: int


class StormResponse(BaseModel):
    storm_id: str
    name: str
    year: int
    category: int
    basin: str
    track_points: List[TrackPoint]
    min_pressure_mb: int
    max_surge_ft: float
    landfall_location: dict
    landfall_date: str


class StormSearchResult(BaseModel):
    storm_id: str
    name: str
    year: int
    category: int
    distance_mi: float


class StormSearchResponse(BaseModel):
    storms: List[StormSearchResult]
    total: int


class ImpactResponse(BaseModel):
    storm_id: str
    name: str
    year: int
    closest_approach_mi: float
    closest_approach_date: str
    max_surge_at_location_ft: float
    max_wind_at_location_kt: int


class ReturnPeriodResponse(BaseModel):
    lat: float
    lon: float
    category_3_return_years: int
    category_4_return_years: int
    category_5_return_years: Optional[int] = None


class RiskSummaryRequest(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    property_value_usd: float = Field(..., gt=0)


class DamageEstimate(BaseModel):
    surge_damage_usd: float
    wind_damage_usd: float
    total_damage_usd: float
    surge_pct: float
    wind_pct: float


class RiskSummaryResponse(BaseModel):
    lat: float
    lon: float
    property_value_usd: float
    nearest_storm: Optional[str] = None
    max_wind_recorded_kt: Optional[int] = None
    max_surge_recorded_ft: Optional[float] = None
    damage_estimate: DamageEstimate
    exposure_years: int
