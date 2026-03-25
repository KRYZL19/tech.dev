from pydantic import BaseModel
from typing import Optional


class AmmoSearchResult(BaseModel):
    caliber: str
    bullet_weight: int
    bullet_type: str
    muzzle_velocity: int
    bc: Optional[float] = None


class AmmoDetail(BaseModel):
    caliber: str
    bullet_weight: int
    bullet_type: str
    muzzle_velocity: int
    bc_g1: float
    caliber_name: str
    case_length_mm: float
    bullet_diameter: float


class PowderData(BaseModel):
    name: str
    type: str
    max_load_gr: float
    min_load_gr: float
    burn_rate_index: int


class ReloadRequest(BaseModel):
    caliber: str
    bullet_weight: int
    powder_type: str


class ReloadResult(BaseModel):
    caliber: str
    bullet_weight: int
    powder_type: str
    starting_load_gr: float
    max_load_gr: float
    velocity_estimate_fps: int
    notes: str = "Always verify with published load data. Start low and work up."


class BulletInfo(BaseModel):
    caliber: str
    bullet_weight: int
    style: str
    bc_g1: float
    diameter_inches: float


class CaliberList(BaseModel):
    caliber: str
    name: str


class HealthResponse(BaseModel):
    status: str
    version: str
