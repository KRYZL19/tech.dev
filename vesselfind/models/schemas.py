"""Pydantic schemas for VESSELFIND API."""

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


# ─── VESSEL ────────────────────────────────────────────────────────────────────

class VesselBase(BaseModel):
    vessel_id: str = Field(..., description="Unique vessel identifier")
    documentation_number: str = Field(..., description="USCG documentation number")
    name: str
    manufacturer: str
    model: str
    year: int
    length_ft: float
    beam_ft: float
    hull_material: str
    propulsion: str
    vessel_type: str = Field(..., description="e.g. cruiser, fishing, pontoon")
    status: str = Field(..., description="active or cancelled")


class VesselResponse(VesselBase):
    lien_status: str = Field(..., description="clear, lien, or multiple_liens")
    lien_holder: Optional[str] = None


class VesselDetailResponse(VesselBase):
    lien_status: str
    lien_holder: Optional[str] = None
    current_owner: Optional[dict] = None


# ─── OWNER ─────────────────────────────────────────────────────────────────────

class OwnerRecord(BaseModel):
    name: str
    city: str
    state: str
    purchase_date: date
    purchase_price: Optional[float] = None


# ─── HISTORY ───────────────────────────────────────────────────────────────────

class VesselHistoryResponse(BaseModel):
    vessel_id: str
    documentation_number: str
    vessel_name: str
    status: str
    lien_status: str
    lien_holder: Optional[str] = None
    owner_history: list[OwnerRecord]
    previous_owners_count: int
    current_owner: Optional[OwnerRecord] = None


# ─── VALIDATE ─────────────────────────────────────────────────────────────────

class ValidateRequest(BaseModel):
    documentation_number: str = Field(..., min_length=7, max_length=8)


class ValidateResponse(BaseModel):
    valid: bool
    documentation_number: str
    vessel_id: Optional[str] = None
    vessel_name: Optional[str] = None
    status: Optional[str] = None  # active / cancelled / not_found
    lien_status: Optional[str] = None


# ─── MANUFACTURER ─────────────────────────────────────────────────────────────

class ManufacturerResponse(BaseModel):
    manufacturer: str
    manufacturer_display: str
    total_vessels: int
    models: list[str]
    vessels: list[VesselBase]
