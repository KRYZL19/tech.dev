from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from models.schemas import Tariff, TariffSearchResult
from data.tou_tariffs import get_tariff, search_tariffs, get_all_tariffs


router = APIRouter(prefix="/api/v1/tariffs", tags=["tariffs"])


@router.get("/", response_model=list[TariffSearchResult])
def list_tariffs():
    """List all available utilities."""
    return get_all_tariffs()


@router.get("/{utility_id}", response_model=Tariff)
def get_tariff_by_id(utility_id: str):
    """Get a specific utility's tariff data."""
    tariff = get_tariff(utility_id)
    if not tariff:
        raise HTTPException(status_code=404, detail=f"Utility '{utility_id}' not found")
    return {"id": utility_id, **tariff}


@router.get("/search", response_model=list[TariffSearchResult])
def search(q: str = Query(..., min_length=1, description="Search term")):
    """Search utilities by name or state."""
    results = search_tariffs(q)
    if not results:
        raise HTTPException(status_code=404, detail=f"No utilities found matching '{q}'")
    return results
