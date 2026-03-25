from fastapi import APIRouter, HTTPException
import math
from typing import List

from models.schemas import (
    PortSearchResult, PortDetail, RouteDistanceRequest,
    RouteDistanceResponse, FuelEstimateRequest, FuelEstimateResponse
)
from data.ports_data import PORTS

router = APIRouter(prefix="/api/v1", tags=["navigation"])


def haversine_nm(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance in nautical miles between two points."""
    R_nm = 3440.065  # Earth radius in nautical miles
    lat1_r, lon1_r = math.radians(lat1), math.radians(lon1)
    lat2_r, lon2_r = math.radians(lat2), math.radians(lon2)

    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return R_nm * c


@router.get("/ports/search", response_model=List[PortSearchResult])
async def search_ports(q: str):
    """Search ports by name. Returns lat/lon/region."""
    q_lower = q.lower()
    results = [
        PortSearchResult(
            id=p["id"],
            name=p["name"],
            lat=p["lat"],
            lon=p["lon"],
            region=p["region"]
        )
        for p in PORTS.values() if q_lower in p["name"].lower()
    ]
    return results


@router.get("/port/{port_id}", response_model=PortDetail)
async def get_port(port_id: str):
    """Get port details: coordinates, region, timezone, available services."""
    if port_id not in PORTS:
        raise HTTPException(status_code=404, detail="Port not found")

    p = PORTS[port_id]
    return PortDetail(
        id=p["id"],
        name=p["name"],
        lat=p["lat"],
        lon=p["lon"],
        region=p["region"],
        timezone=p["timezone"],
        services=p["services"]
    )


@router.post("/route/distance", response_model=RouteDistanceResponse)
async def calculate_route_distance(request: RouteDistanceRequest):
    """Calculate total distance and estimated time for a route at 6 knots."""
    if len(request.waypoints) < 2:
        raise HTTPException(status_code=400, detail="Need at least 2 waypoints")

    total_nm = 0.0
    for i in range(len(request.waypoints) - 1):
        wp1 = request.waypoints[i]
        wp2 = request.waypoints[i + 1]
        total_nm += haversine_nm(wp1.lat, wp1.lon, wp2.lat, wp2.lon)

    total_nm = round(total_nm, 2)
    time_hours = round(total_nm / 6.0, 2)
    hours = int(time_hours)
    mins = int((time_hours - hours) * 60)

    return RouteDistanceResponse(
        total_distance_nm=total_nm,
        estimated_time_hours=time_hours,
        estimated_time_formatted=f"{hours}h {mins}m"
    )


@router.post("/fuel/estimate", response_model=FuelEstimateResponse)
async def estimate_fuel(request: FuelEstimateRequest):
    """Estimate fuel cost for a voyage."""
    if request.distance_nm <= 0 or request.fuel_gph <= 0:
        raise HTTPException(status_code=400, detail="Distance and fuel consumption must be positive")

    fuel_used = round(request.distance_nm / 6.0 * request.fuel_gph, 2)
    fuel_cost = round(fuel_used * request.fuel_price_per_gal, 2)
    range_nm = round(6.0 * (50 / request.fuel_gph), 2) if request.fuel_gph > 0 else 0  # Assuming 50gal tank

    return FuelEstimateResponse(
        distance_nm=request.distance_nm,
        fuel_used_gallons=fuel_used,
        fuel_cost=fuel_cost,
        range_nm=range_nm
    )
