from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Device(BaseModel):
    name: str
    duration_hours: float = Field(ge=0.25, le=24)
    priority: int = Field(ge=1, le=5, description="1=highest, 5=lowest")
    power_kw: float = Field(default=1.0, ge=0.1)


class OptimizeScheduleRequest(BaseModel):
    utility_id: str
    devices: list[Device]
    start_hour: int = Field(default=0, ge=0, le=23)
    end_hour: int = Field(default=24, ge=0, le=24)
    carbon_weight: float = Field(default=0.0, ge=0.0, le=1.0)


class ScheduledDevice(BaseModel):
    name: str
    start_time: str
    end_time: str
    duration_hours: float
    cost: float
    priority: int
    power_kw: float


class ScheduleResponse(BaseModel):
    utility_id: str
    scheduled_devices: list[ScheduledDevice]
    total_cost: float
    flat_rate_cost: float
    savings_percent: float
    carbon_intensity_used: Optional[float] = None


class TariffPeriod(BaseModel):
    name: str
    start_hour: int
    end_hour: int
    price: float
    days: str


class Tariff(BaseModel):
    id: str
    name: str
    state: str
    description: str
    periods: list[TariffPeriod]
    flat_rate: float


class TariffSearchResult(BaseModel):
    id: str
    name: str
    state: str
    description: str


class CarbonIntensityResponse(BaseModel):
    region: str
    intensity: float
    unit: str
    timestamp: str
    source: str


class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: str
