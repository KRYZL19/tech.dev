from pydantic import BaseModel
from typing import Optional


class AdoptionResponse(BaseModel):
    city: str
    state: str
    ibc_version: str
    irc_version: str
    nec_version: str
    effective_date: str
    amendments: list[str]
    local_amendments: list[str]


class CodeSectionResponse(BaseModel):
    code_name: str
    version: str
    section_number: str
    title: str
    code_text: str
    referenced_standards: list[str]


class StateCodeResponse(BaseModel):
    state: str
    codes_adopted: str
    adoption_date: str
    cities_covered: int


class PermitChecklistRequest(BaseModel):
    city: str
    project_type: str
    sqft: float


class PermitChecklistResponse(BaseModel):
    city: str
    project_type: str
    sqft: float
    required_permits: list[str]
    inspections: list[str]
    setbacks: dict[str, str]


class ADARequirementsResponse(BaseModel):
    occupancy_type: str
    name: str
    accessible_rooms: str
    seating: str
    toilet_rooms: str
    drinking_fountains: str
