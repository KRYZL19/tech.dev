from pydantic import BaseModel, Field
from typing import List, Optional


class AirspaceCheckRequest(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    altitude_ft: int = Field(..., ge=0)
    drone_class: str = Field(default="standard", pattern="^(standard|重量级|micro|mini)$")


class AirspaceCheckResponse(BaseModel):
    airspace_class: str
    laanc_eligible: bool
    max_altitude_ft: int
    warnings: List[str]


class GridSearchResponse(BaseModel):
    grid_id: str
    lat: float
    lon: float
    max_altitude_ft: int
    city: str


class Waypoint(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    alt: int = Field(..., ge=0)


class FlightPlanRequest(BaseModel):
    waypoints: List[Waypoint]
    drone_class: str = Field(default="standard", pattern="^(standard|重量级|micro|mini)$")


class FlightPlanResponse(BaseModel):
    airspace_conflicts: List[str]
    total_flight_time_min: float
    warnings: List[str]
