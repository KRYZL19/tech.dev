"""Pydantic schemas for KNOTDB API."""

from typing import List, Optional
from pydantic import BaseModel, Field


class KnotSummary(BaseModel):
    """Summary view of a knot for list endpoints."""
    name: str = Field(..., description="Knot name")
    category: str = Field(..., description="Category: bending, binding, loop, stopper, slip, hitch")
    difficulty_rating: int = Field(..., ge=1, le=5, description="Difficulty 1-5")
    strength_pct: int = Field(..., ge=0, le=100, description="Strength as percentage of rope strength")
    use_cases: List[str] = Field(..., description="Primary use cases")


class KnotDetail(BaseModel):
    """Full detail view of a knot."""
    name: str
    category: str
    difficulty_rating: int
    strength_pct: int
    breaking_strength_lbs: int = Field(..., description="Breaking strength in pounds")
    use_cases: List[str]
    proper_use: str
    when_not_to_use: str
    how_to_tie_steps: List[str]
    failure_mode: str
    related_knots: List[str]


class LoadCompareRequest(BaseModel):
    """Request body for load comparison."""
    knot1_name: str = Field(..., description="Name of first knot")
    knot2_name: str = Field(..., description="Name of second knot")
    load_lbs: float = Field(..., gt=0, description="Applied load in pounds")


class StrengthComparison(BaseModel):
    """Strength comparison between two knots."""
    knot1_name: str
    knot2_name: str
    knot1_strength_pct: int
    knot2_strength_pct: int
    knot1_breaking_lbs: int
    knot2_breaking_lbs: int
    load_lbs: float
    knot1_safety_factor: float
    knot2_safety_factor: float
    stronger_knot: str
    strength_difference_pct: int


class ComparisonResult(BaseModel):
    """Full comparison result with recommendation."""
    comparison: StrengthComparison
    failure_mode: str
    recommendation: str


class SearchResult(BaseModel):
    """Result of use case search."""
    use_case: str
    matching_knots: List[KnotSummary]
    count: int


class ErrorResponse(BaseModel):
    """API error response."""
    detail: str
