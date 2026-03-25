"""Standard lumber sizes route."""

from fastapi import APIRouter
from models.schemas import StandardSizesResponse, DimensionEntry
from utils.dimensions import LUMBER_DIMENSIONS

router = APIRouter(prefix="/board", tags=["lumber dimensions"])


@router.get("/standard-sizes", response_model=StandardSizesResponse)
def standard_sizes():
    """
    Returns nominal vs actual dimensions for common lumber sizes.

    Nominal = retail name (what you ask for at the store).
    Actual = true dimension after planing/drying (what you actually get).
    """
    sizes = []
    for size_name, dims in sorted(LUMBER_DIMENSIONS.items()):
        nominal_t, nominal_w = dims["nominal"]
        actual_t, actual_w = dims["actual"]
        sizes.append(DimensionEntry(
            size=size_name,
            nominal_inches=f"{int(nominal_t)}×{int(nominal_w)}",
            actual_inches=f"{actual_t}×{actual_w}",
            board_feet_per_ft=round(dims["bf_per_ft"], 4),
        ))

    return StandardSizesResponse(
        sizes=sizes,
        note="Nominal = planed/dressed dimension. Actual = true dimension after milling.",
    )
