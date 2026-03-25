"""Pydantic schemas for FCCLOOKUP API."""

from typing import Optional
from pydantic import BaseModel, Field


class CallsignBase(BaseModel):
    callsign: str
    frn: str
    licensee: str
    status: str
    class_: str = Field(alias="class")

    class Config:
        populate_by_name = True


class CallsignDetail(CallsignBase):
    expired: str
    grid: str
    address: str
    privileges: list[str] = []


class EquipmentCert(BaseModel):
    fcc_id: str
    device_type: str
    brand: str
    model: str
    frequencies_mhz: list[str]
    max_power_w: float
    emission_modes: list[str]
    status: str


class FrequencyInfo(BaseModel):
    mhz: float
    band: Optional[str]
    band_name: Optional[str]
    allocation_type: str
    license_class: str
    power_limit_w: float
    notes: Optional[str] = None


class BandInfo(BaseModel):
    band: str
    name: str
    start_mhz: float
    end_mhz: float
    allocation_type: str
    privileges: dict[str, list[str]]


class InterferenceCheck(BaseModel):
    mhz: float
    location: str


class InterferenceResult(BaseModel):
    mhz: float
    location: str
    interference_sources: list[dict]
    advice: str
