"""Pydantic schemas for SAWMILL API."""

from pydantic import BaseModel, Field
from typing import List, Optional


# ─── Cut List Optimization ────────────────────────────────────

class RequiredCut(BaseModel):
    length_in: float = Field(..., gt=0, description="Cut length in inches")
    width_in: float = Field(default=1.5, gt=0, description="Cut width in inches")
    quantity: int = Field(default=1, ge=1, description="Number of pieces needed")


class AvailableBoard(BaseModel):
    board_type: str = Field(..., description="Lumber size, e.g. '2x4', '1x6'")
    length_ft: float = Field(..., gt=0, description="Board length in feet")
    price_per_bf: float = Field(default=2.0, ge=0, description="Price per board foot (USD)")
    wood_type: Optional[str] = Field(default="pine", description="Wood species")
    width_in: Optional[float] = Field(default=None, description="Actual width in inches (overrides dimension lookup)")


class CutListOptimizeRequest(BaseModel):
    available_boards: List[AvailableBoard] = Field(..., min_length=1)
    required_cuts: List[RequiredCut] = Field(..., min_length=1)
    kerf_inches: float = Field(default=0.125, ge=0, description="Saw blade width in inches")


class WasteBoard(BaseModel):
    board_idx: int
    board_type: str
    length_ft: float
    waste_area_sqft: float
    waste_cost: float


class CutAssignment(BaseModel):
    board_idx: int
    cut_length_in: float
    cut_width_in: float
    cut_area_sqft: float


class CutListOptimizeResponse(BaseModel):
    yield_percent: float
    waste_boards: List[WasteBoard]
    total_cost: float
    cuts_placed: int
    cuts_requested: int
    assignments: List[CutAssignment]


# ─── Yield Estimate ─────────────────────────────────────────

class YieldEstimateRequest(BaseModel):
    board_sqft: float = Field(..., gt=0, description="Total board area in square feet")
    cuts_sqft: float = Field(..., gt=0, description="Total required cut area in square feet")
    kerf_inches: float = Field(default=0.125, ge=0, description="Saw blade width in inches")
    board_count: int = Field(default=1, ge=1, description="Number of boards")


class YieldEstimateResponse(BaseModel):
    theoretical_yield_pct: float
    realistic_yield_pct: float


# ─── Standard Sizes ──────────────────────────────────────────

class DimensionEntry(BaseModel):
    size: str
    nominal_inches: str
    actual_inches: str
    board_feet_per_ft: float


class StandardSizesResponse(BaseModel):
    sizes: List[DimensionEntry]
    note: str = "Nominal = planed/dressed dimension. Actual = true dimension after milling."


# ─── Price Estimate ─────────────────────────────────────────

class PriceCutItem(BaseModel):
    length_in: float = Field(..., gt=0)
    width_in: float = Field(default=1.5, gt=0)
    quantity: int = Field(default=1, ge=1)


class PriceEstimateRequest(BaseModel):
    cuts: List[PriceCutItem] = Field(..., min_length=1)
    wood_type: str = Field(..., description="Wood species, e.g. 'pine', 'oak', 'cherry'")
    board_size: str = Field(default="2x4", description="Board nominal size to purchase")
    kerf_inches: float = Field(default=0.125, ge=0)


class PriceEstimateResponse(BaseModel):
    material_cost: float
    labor_hours: float
    total_estimate: float
    wood_type: str
    board_size: str
    total_cut_sqft: float
