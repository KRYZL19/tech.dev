from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class AircraftBase(BaseModel):
    n_number: str
    serial_number: str
    year: Optional[int]
    make: str
    model: str
    engine_make: Optional[str] = None
    engine_model: Optional[str] = None
    engine_hp: Optional[int] = None
    number_of_seats: Optional[int] = None
    number_of_engines: Optional[int] = None


class AircraftWeights(BaseModel):
    empty_weight: float = Field(description="Empty weight in pounds")
    gross_weight: float = Field(description="Max gross weight in pounds")
    useful_load: Optional[float] = Field(default=None, description="Computed useful load in pounds")


class AirworthinessInfo(BaseModel):
    certificate: str = Field(description="Airworthiness certificate type (Standard, Special)")
    status: str = Field(description="Current airworthiness status (Airworthy, Not Airworthy, etc.)")
    type_engine: Optional[str] = None
    category: Optional[str] = Field(default=None, description="FAA aircraft category")


class AircraftResponse(AircraftBase, AircraftWeights, AirworthinessInfo):
    pass


class OwnerRecord(BaseModel):
    owner_name: str
    owner_city: str
    owner_state: str
    registration_issued: date
    registration_expires: Optional[date] = None
    cancellation_date: Optional[date] = None


class AircraftHistoryResponse(BaseModel):
    n_number: str
    current_owner: OwnerRecord
    owner_history: list[OwnerRecord] = Field(default_factory=list)


class UsefulLoadRequest(BaseModel):
    n_number: str
    pilot_weight: float = Field(ge=0, description="Pilot weight in pounds")
    passengers: float = Field(ge=0, description="Total passenger weight in pounds")
    baggage: float = Field(ge=0, description="Baggage weight in pounds")
    fuel_gallons: float = Field(ge=0, le=1000, description="Fuel load in gallons")


class UsefulLoadResponse(BaseModel):
    n_number: str
    empty_weight: float
    gross_weight: float
    max_useful_load: float
    fuel_weight: float = Field(description="Fuel weight (6 lbs/gal)")
    payload_used: float
    payload_remaining: float
    useful_load_available: float
    within_limits: bool


class ExpiringRegistration(BaseModel):
    n_number: str
    owner_name: str
    owner_city: str
    owner_state: str
    expires: date
    days_remaining: int
    make: str
    model: str


class ManufacturerResponse(BaseModel):
    manufacturer: str
    aircraft: list[AircraftBase]
    total_count: int
