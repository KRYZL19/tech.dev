"""Pydantic schemas for GARDENPLOT API."""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============ Planner Schemas ============

class WhatGrowsRequest(BaseModel):
    zone: str = Field(..., description="USDA hardiness zone (3-11)")
    sunlight_hours: float = Field(..., ge=0, le=24, description="Available sunlight hours per day")
    space_sqft: float = Field(..., gt=0, description="Available garden space in square feet")
    goals: list[str] = Field(default_factory=list, description="Garden goals (beginner, quick_harvest, high_yield, etc.)")


class SpacingRecommendation(BaseModel):
    plant: str
    plants_per_sqft: float
    total_count: int
    spacing_note: str


class ExpectedYield(BaseModel):
    plant: str
    estimated_lbs_per_season: float
    harvest_window_days: int


class WhatGrowsResponse(BaseModel):
    vegetables: list[str]
    spacing_recommendations: list[SpacingRecommendation]
    expected_yield: list[ExpectedYield]
    shade_insight: Optional[str] = None


# ============ Plant Schemas ============

class PlantDetailResponse(BaseModel):
    name: str
    days_to_maturity: int
    sun_hours_min: int
    spacing_inches: int
    frost_tolerance: str
    companions: list[str]
    enemies: list[str]
    harvest_window_days: int
    family: str
    yield_per_plant_lbs: float


# ============ Rotation Schemas ============

class PlotSection(BaseModel):
    section_id: str = Field(..., description="Unique section identifier")
    current_plant: str = Field(..., description="Current or planned plant")
    plant_family: str = Field(..., description="Plant family")
    notes: Optional[str] = None


class RotationPlanRequest(BaseModel):
    plot_layout: list[PlotSection] = Field(..., description="Garden plot layout with current/planned plants")


class SeasonPlan(BaseModel):
    season: str
    sections: list[dict]
    recommended_plantings: list[str]


class RotationPlanResponse(BaseModel):
    season_1: SeasonPlan
    season_2: SeasonPlan
    season_3: SeasonPlan
    disease_prevention_notes: list[str]


# ============ Companion Check Schemas ============

class CompanionCheckRequest(BaseModel):
    plant_a: str = Field(..., description="First plant name")
    plant_b: str = Field(..., description="Second plant name")


class CompanionCheckResponse(BaseModel):
    plant_a: str
    plant_b: str
    compatibility_score: int = Field(..., ge=0, le=100, description="Compatibility score 0-100")
    reason: str
    tips: list[str]


# ============ Frost Date Schemas ============

class FrostDateResponse(BaseModel):
    zipcode: str
    zone: str
    last_frost_spring: str
    first_frost_fall: str
    growing_days: int


# ============ Health Check ============

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
