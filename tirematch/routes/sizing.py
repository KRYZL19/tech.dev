"""Size parsing route for TIREMATCH API."""

from fastapi import APIRouter, HTTPException, Path
from routes.sizing_utils import parse_tire_size, tire_dimensions
from models.schemas import SizeParseResponse

router = APIRouter(prefix="/api/v1", tags=["sizing"])


@router.get("/size/{width}/{aspect}R{rim}", response_model=SizeParseResponse)
def parse_size(
    width: int = Path(..., ge=125, le=400, description="Tire width in mm"),
    aspect: int = Path(..., ge=20, le=90, description="Aspect ratio %"),
    rim: int = Path(..., ge=10, le=30, description="Rim diameter in inches"),
):
    """
    Parse a tire size string and return all dimensions.

    Example: GET /api/v1/size/245/45R18
    """
    try:
        parse_tire_size(f"{width}/{aspect}R{rim}")
    except ValueError as e:
        raise HTTPException(status_code=422, detail={"message": str(e), "error_code": "INVALID_TIRE_SIZE"})

    dims = tire_dimensions(width, aspect, rim)

    raw = f"{width}/{aspect}R{rim}"
    return SizeParseResponse(raw=raw, **dims)
