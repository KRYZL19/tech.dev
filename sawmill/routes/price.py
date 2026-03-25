"""Price estimation route."""

from fastapi import APIRouter
from models.schemas import PriceEstimateRequest, PriceEstimateResponse
from utils.dimensions import WOOD_PRICES_PER_BF, LUMBER_DIMENSIONS, LABOR_RATE_PER_HOUR, SQFT_PER_LABOR_HOUR

router = APIRouter(prefix="/price", tags=["price estimation"])


@router.post("/estimate", response_model=PriceEstimateResponse)
def price_estimate(req: PriceEstimateRequest):
    """
    Estimate material cost, labor hours, and total for a cut list.

    - **material_cost**: based on board footage needed × price_per_bf
    - **labor_hours**: total cut sqft / sqft_per_labor_hour
    - **total_estimate**: material + (labor_hours × labor_rate)
    """
    wood_type = req.wood_type.lower()
    price_per_bf = WOOD_PRICES_PER_BF.get(wood_type, WOOD_PRICES_PER_BF["pine"])

    # Total cut area in sqft
    total_cut_sqft = 0.0
    for cut in req.cuts:
        qty = int(cut.quantity)
        area_sqft = (float(cut.length_in) * float(cut.width_in)) / 144.0
        total_cut_sqft += area_sqft * qty

    # Board footage needed: assume worst-case 100% waste, then reduce
    # Use board size to determine thickness factor
    dims = LUMBER_DIMENSIONS.get(req.board_size, {"actual": (1.5, 3.5)})
    thickness_in = dims["actual"][0]
    board_bf_per_sqft = thickness_in / 12.0  # BF per sqft at given thickness

    # Estimate boards needed (rough): total_cut_sqft / (board_sqft × yield_estimate)
    board_sqft_per_bd = 1.0 / board_bf_per_sqft  # how many sqft per bf
    estimated_bf = total_cut_sqft / board_bf_per_sqft  # rough bf needed
    # Add 15% waste buffer
    estimated_bf_with_waste = estimated_bf * 1.15

    material_cost = round(estimated_bf_with_waste * price_per_bf, 2)

    # Labor: cutting + handling
    labor_hours = round(total_cut_sqft / SQFT_PER_LABOR_HOUR, 2)
    labor_cost = round(labor_hours * LABOR_RATE_PER_HOUR, 2)

    total = round(material_cost + labor_cost, 2)

    return PriceEstimateResponse(
        material_cost=material_cost,
        labor_hours=labor_hours,
        total_estimate=total,
        wood_type=req.wood_type,
        board_size=req.board_size,
        total_cut_sqft=round(total_cut_sqft, 4),
    )
