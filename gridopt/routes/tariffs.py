from fastapi import APIRouter, HTTPException, Query
from data.tou_tariffs import get_tariff, search_tariffs
from models.schemas import TariffResponse, TariffSearchResult

router = APIRouter(prefix="/tariffs", tags=["tariffs"])


@router.get("/{utility_id}", response_model=TariffResponse)
async def get_tariff_by_id(utility_id: str):
    tariff = get_tariff(utility_id)
    if not tariff:
        raise HTTPException(status_code=404, detail="Utility not found")
    return TariffResponse(**tariff)


@router.get("/search", response_model=list[TariffSearchResult])
async def search_utility(q: str = Query(..., min_length=1)):
    results = search_tariffs(q)
    return results
