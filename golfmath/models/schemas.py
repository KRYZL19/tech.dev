# models/schemas.py
from pydantic import BaseModel
from typing import List, Optional


class HandicapCalculateRequest(BaseModel):
    scores: List[int]
    course_ratings: List[float]
    slope_ratings: List[int]


class RoundDifferential(BaseModel):
    round: int
    score: int
    course_rating: float
    slope_rating: int
    differential: float


class HandicapCalculateResponse(BaseModel):
    handicap_index: float
    differentials: List[RoundDifferential]
    best_8_differential: float
    rounds_used: int


class HoleData(BaseModel):
    hole: int
    par: int
    yardage: int
    index: int


class CourseResponse(BaseModel):
    course_id: str
    name: str
    location: str
    par: int
    rating: float
    slope: int
    holes: List[HoleData]


class ScorecardRequest(BaseModel):
    course_id: str
    strokes_per_hole: List[int]
    putts_per_hole: List[int]
    fairways_hit: List[bool]
    gir: List[bool]


class ScorecardStats(BaseModel):
    total_strokes: int
    total_putts: int
    fairways_hit: int
    gir: int
    gir_percentage: float
    avg_putts_per_gir: Optional[float]


class ScorecardResponse(BaseModel):
    course_id: str
    course_name: str
    score_vs_par: int
    score_breakdown: str
    stats: ScorecardStats
    course_replay_estimate: str


class WeatherAdjustRequest(BaseModel):
    handicap_index: float
    temp_f: float
    wind_mph: float
    elevation_ft: float


class WeatherAdjustResponse(BaseModel):
    original_handicap: float
    adjusted_handicap: float
    strokes_gained_lost: float
    conditions: dict
    breakdown: str
