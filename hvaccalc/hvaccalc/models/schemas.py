"""Pydantic schemas for HVAC Calculator API"""
from pydantic import BaseModel, Field, field_validator
from typing import Literal


class ResidentialLoadRequest(BaseModel):
    sqft: float = Field(..., gt=0, le=10000, description="Floor area in square feet")
    ceiling_height_ft: float = Field(8.0, gt=6, le=30, description="Ceiling height in feet")
    insulation_r_value: float = Field(..., ge=0, le=60, description="Wall insulation R-value")
    climate_zone: str = Field(..., pattern=r"^[1-8]$", description="IECC climate zone 1-8")
    num_occupants: int = Field(..., ge=1, le=20, description="Number of occupants")
    num_exterior_walls: int = Field(..., ge=0, le=4, description="Number of exterior walls")

    @field_validator("climate_zone")
    @classmethod
    def validate_zone(cls, v):
        if v not in CLIMATE_ZONES_KEYS:
            raise ValueError(f"Climate zone must be 1-8")
        return v


class ResidentialLoadResponse(BaseModel):
    cooling_btu: int = Field(..., description="Total cooling load in BTU/hr")
    heating_btu: int = Field(..., description="Total heating load in BTU/hr")
    tons_ac_needed: float = Field(..., description="AC tonnage required")
    cfm_cooling: int = Field(..., description="Recommended airflow in CFM")
    oversize_warning: bool = Field(False, description="Warning if system appears oversized")
    methodology: str = Field(
        default="IECC 2021 / Manual J simplified",
        description="Sizing methodology used"
    )


class ClimateResponse(BaseModel):
    zipcode: str
    climate_zone: str
    zone_name: str
    cooling_design_temp_f: int
    heating_design_temp_f: int
    hdd_base_65: int
    cdd_base_65: int


class DuctSizeRequest(BaseModel):
    btu_load: float = Field(..., gt=0, description="Total BTU load (cooling or heating)")
    duct_length_ft: float = Field(..., gt=0, le=500, description="Total duct run length")
    num_runs: int = Field(..., ge=1, le=20, description="Number of duct runs")
    friction_rate: float = Field(
        0.08,
        gt=0.01,
        le=0.3,
        description="Friction rate in inches of water gauge per 100 ft"
    )
    duct_type: Literal["supply", "return"] = "supply"


class DuctSizeResponse(BaseModel):
    cfm_per_run: float = Field(..., description="Airflow per duct run in CFM")
    duct_diameter_inches: float = Field(..., description="Recommended duct diameter")
    velocity_fpm: int = Field(..., description="Air velocity in feet per minute")
    friction_rate_used: float
    total_cfm: float
    velocity_category: str = Field(..., description="LOW/MEDIUM/HIGH velocity category")


class EquipmentSizeRequest(BaseModel):
    cooling_btu: float = Field(..., gt=0, description="Cooling load in BTU/hr")
    heating_btu: float = Field(..., gt=0, description="Heating load in BTU/hr")
    efficiency_rating: float = Field(
        ...,
        gt=0,
        description="Efficiency rating (SEER for AC, AFUE for heat)"
    )
    equipment_type: Literal["central_ac", "heat_pump", "furnace", "boiler"] = "central_ac"


class EquipmentSizeResponse(BaseModel):
    cooling_tons: float = Field(..., description="Cooling capacity in tons")
    heating_kbtu: float = Field(..., description="Heating capacity in kBTU/hr")
    recommended_unit_size: str = Field(..., description="Recommended equipment size")
    oversize_warning: bool = Field(False, description="Warning if system is oversized >15%")
    undersize_warning: bool = Field(False, description="Warning if system is undersized")
    oversize_btu: int = Field(0, description="BTU oversize amount if any")


# Re-export for convenience
from hvaccalc.data.climate_zones import CLIMATE_ZONES

CLIMATE_ZONES_KEYS = list(CLIMATE_ZONES.keys())
