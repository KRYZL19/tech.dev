from fastapi import APIRouter, HTTPException
from models.schemas import AirportSummary
from data.incident_index import get_airport_summary, AIRPORTS

router = APIRouter(prefix="/api/v1", tags=["airports"])


@router.get("/airport/{airport_code}/summary", response_model=AirportSummary)
def airport_summary(airport_code: str):
    """Get incident summary for an airport: count by type, year range, most common hazard."""
    code = airport_code.upper()
    if code not in AIRPORTS:
        raise HTTPException(status_code=404, detail=f"Airport '{airport_code}' not found in registry")
    summary = get_airport_summary(code)
    if summary is None:
        raise HTTPException(
            status_code=404,
            detail=f"No incidents found for airport '{airport_code}'",
        )
    return AirportSummary(**summary)
