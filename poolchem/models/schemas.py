"""Pydantic schemas for POOLCHEM API."""
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal
from enum import Enum


class ChlorineType(str, Enum):
    LIQUID = "liquid"
    DI_CHLOR = "di-chlor"
    TRI_CHLOR = "tri-chlor"
    CAL_HYPO = "cal-hypo"
    GAS = "gas"


class BalanceStatus(str, Enum):
    BALANCED = "balanced"
    CORROSIVE = "corrosive"
    SCALE_FORMING = "scale_forming"
    SEVERE_CORROSIVE = "severe_corrosive"
    SEVERE_SCALE = "severe_scale"


class CSIStatus(str, Enum):
    BALANCED = "balanced"
    CORROSIVE = "corrosive"
    SCALE_FORMING = "scale_forming"


# ---- Balance Check ----
class BalanceCheckRequest(BaseModel):
    pool_gallons: float = Field(..., gt=0, description="Pool volume in gallons")
    chlorine_ppm: float = Field(..., ge=0, description="Current free chlorine ppm")
    ph: float = Field(..., ge=0, le=14, description="Current pH level")
    alkalinity_ppm: float = Field(..., ge=0, description="Total alkalinity in ppm as CaCO3")
    temp_f: float = Field(..., ge=32, le=120, description="Water temperature in Fahrenheit")
    stabilizer_ppm: float = Field(..., ge=0, description="CYA (cyanuric acid) in ppm")
    calcium_hardness_ppm: float = Field(..., ge=0, description="Calcium hardness in ppm as CaCO3")


class Recommendation(BaseModel):
    parameter: str
    current: float
    target: str
    action: str
    priority: Literal["critical", "high", "medium", "low"]


class BalanceCheckResponse(BaseModel):
    saturation_index: float
    balance_status: BalanceStatus
    recommendations: List[Recommendation]
    fci_alert: bool = False
    fci_note: Optional[str] = None


# ---- Chlorine Dose ----
class ChlorineDoseRequest(BaseModel):
    pool_gallons: float = Field(..., gt=0, description="Pool volume in gallons")
    current_chlorine_ppm: float = Field(..., ge=0, description="Current chlorine ppm")
    target_ppm: float = Field(..., gt=0, description="Target chlorine ppm")
    chlorine_type: ChlorineType = Field(..., description="Type of chlorine product")


class ChlorineDoseResponse(BaseModel):
    oz_needed: float
    cost_estimate: float
    demand_multiplier: float
    fci_adjusted: bool
    fci_note: Optional[str] = None


# ---- pH Adjust ----
class PHAdjustRequest(BaseModel):
    pool_gallons: float = Field(..., gt=0, description="Pool volume in gallons")
    current_ph: float = Field(..., ge=0, le=14, description="Current pH")
    target_ph: float = Field(..., ge=0, le=14, description="Target pH")


class PHAdjustResponse(BaseModel):
    sodium_carbonate_oz: Optional[float] = None
    muriatic_acid_oz: Optional[float] = None
    chemical_direction: Literal["raise", "lower", "none"]
    gallons_affected: float


# ---- Saturation Index ----
class SaturationRequest(BaseModel):
    ph: float = Field(..., ge=0, le=14)
    alkalinity: float = Field(..., ge=0)
    calcium_hardness: float = Field(..., ge=0)
    temp: float = Field(..., ge=32, le=120)
    cya: float = Field(..., ge=0)


class SaturationResponse(BaseModel):
    si_value: float
    csi_status: CSIStatus
    ph_factor: float
    temp_factor: float
    alk_factor: float
    calcium_factor_val: float


# ---- Chloramine Breakpoint ----
class ChloramineConvertRequest(BaseModel):
    combined_chloramine_ppm: float = Field(..., gt=0, description="Combined chlorine (chloramine) in ppm")


class ChloramineConvertResponse(BaseModel):
    breakpoint_dose_ppm: float
    volume_to_add_oz: float
    stage_note: str


# ---- Health / Rate Limit ----
class HealthResponse(BaseModel):
    status: str
    version: str
    tier: str
    requests_remaining: int
