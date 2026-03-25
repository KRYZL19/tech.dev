import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, HTTPException, Query
from models.schemas import StormResponse, StormSearchResponse, StormSearchResult
from data.storm_data import get_all_storms, get_storm_by_id

router = APIRouter(prefix="/api/v1", tags=["storms"])

EARTH_RADIUS_MI = 3958.8


def haversine_mi(lat1, lon1, lat2, lon2):
    """Great-circle distance in miles."""
    R = EARTH_RADIUS_MI
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


@router.get("/storms/search", response_model=StormSearchResponse)
def search_storms(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
    radius_mi: float = Query(100, gt=0),
    year_start: int = Query(1950, ge=1900),
    year_end: int = Query(2025, ge=1900),
):
    """Find storms within radius of a lat/lon point in a year range."""
    storms = get_all_storms()
    results = []

    for storm in storms:
        if not (year_start <= storm["year"] <= year_end):
            continue

        # Find minimum distance from storm track to point
        min_dist = float("inf")
        for tp in storm["track_points"]:
            d = haversine_mi(lat, lon, tp["lat"], tp["lon"])
            if d < min_dist:
                min_dist = d

        if min_dist <= radius_mi:
            results.append(
                StormSearchResult(
                    storm_id=storm["storm_id"],
                    name=storm["name"],
                    year=storm["year"],
                    category=storm["category"],
                    distance_mi=round(min_dist, 1),
                )
            )

    results.sort(key=lambda x: x.distance_mi)
    return StormSearchResponse(storms=results, total=len(results))


@router.get("/storm/{storm_id}", response_model=StormResponse)
def get_storm(storm_id: str):
    """Get full storm details by ID."""
    storm = get_storm_by_id(storm_id)
    if not storm:
        raise HTTPException(status_code=404, detail=f"Storm '{storm_id}' not found")
    return storm
