from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class PortSearchResult(BaseModel):
    id: str
    name: str
    lat: float
    lon: float
    region: str


class TideEvent(BaseModel):
    time: str
    type: str  # "high" or "low"
    height_ft: float


class TideResponse(BaseModel):
    port_id: str
    port_name: str
    date: str
    tides: List[TideEvent]


class PortDetail(BaseModel):
    id: str
    name: str
    lat: float
    lon: float
    region: str
    timezone: str
    services: List[str]


class RoutePoint(BaseModel):
    lat: float
    lon: float


class RouteDistanceRequest(BaseModel):
    waypoints: List[RoutePoint]


class RouteDistanceResponse(BaseModel):
    total_distance_nm: float
    estimated_time_hours: float
    estimated_time_formatted: str


class FuelEstimateRequest(BaseModel):
    distance_nm: float
    fuel_gph: float
    fuel_price_per_gal: float


class FuelEstimateResponse(BaseModel):
    distance_nm: float
    fuel_used_gallons: float
    fuel_cost: float
    range_nm: float
