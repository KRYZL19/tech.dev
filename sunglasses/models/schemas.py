from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime


class IncidentBase(BaseModel):
    report_id: str
    date: date
    aircraft_type: str
    airline: Optional[str] = None
    airport_code: Optional[str] = None
    incident_type: str  # laser, wildlife, operational_incident, near_mid
    narrative: Optional[str] = None
    crew_effects: Optional[str] = None
    pilot_description: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None


class IncidentSummary(BaseModel):
    report_id: str
    date: date
    aircraft_type: str
    incident_type: str
    airport_code: Optional[str] = None


class IncidentDetail(BaseModel):
    report_id: str
    date: date
    aircraft_type: str
    airline: Optional[str] = None
    airport_code: Optional[str] = None
    incident_type: str
    narrative: str
    crew_effects: Optional[str] = None
    pilot_description: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None


class AirportSummary(BaseModel):
    airport_code: str
    total_incidents: int
    incident_count_by_type: dict
    year_range: tuple[int, int]
    most_common_hazard: str


class SearchResult(BaseModel):
    report_id: str
    date: date
    aircraft_type: str
    incident_type: str
    airport_code: Optional[str] = None
    distance_mi: Optional[float] = None
