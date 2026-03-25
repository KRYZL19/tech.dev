from pydantic import BaseModel
from typing import Optional


class TariffPeriod(BaseModel):
    name: str
    start_hour: int
    end_hour: int
    price_per_kwh: float


class TariffResponse(BaseModel):
    utility_id: str
    utility_name: str
    timezone: str
    periods: list[TariffPeriod]


class TariffSearchResult(BaseModel):
    utility_id: str
    utility_name: str
    state: str


class Appliance(BaseModel):
    name: str
    duration_hours: float
    priority: int  # lower = more flexible
    must_run_hours: Optional[list[int]] = None  # specific hours appliance must run


class ScheduleOptions(BaseModel):
    max_start_hour: Optional[int] = 24
    min_start_hour: Optional[int] = 0


class ScheduleRequest(BaseModel):
    appliances: list[Appliance]
    tariff: TariffResponse
    options: Optional[ScheduleOptions] = None


class ScheduledItem(BaseModel):
    appliance: str
    start_hour: int
    end_hour: int
    cost: float


class ScheduleResponse(BaseModel):
    schedule: list[ScheduledItem]
    total_cost: float
    total_duration: float


class CarbonIntensityResponse(BaseModel):
    region: str
    carbon_intensity_gco2_kwh: float  # grams CO2 per kWh
    grid_source: str
    timestamp: str
