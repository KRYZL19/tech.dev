import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, HTTPException, Query
from models.schemas import (
    ImpactResponse,
    ReturnPeriodResponse,
    RiskSummaryRequest,
    RiskSummaryResponse,
    DamageEstimate,
)
from data.storm_data import get_all_storms, get_storm_by_id

router = APIRouter(prefix="/api/v1", tags=["analysis"])

EARTH_RADIUS_MI = 3958.8

# Saffir-Simpson wind damage thresholds (kt)
CAT_3_KT = 111
CAT_4_KT = 130
CAT_5_KT = 157

# Surge estimates by category (ft)
CAT_3_SURGE_FT = 9
CAT_4_SURGE_FT = 13
CAT_5_SURGE_FT = 18

# Damage multipliers (% of property value per kt / ft)
WIND_DAMAGE_PER_KT = 0.002   # 0.2% per kt above 50
SURGE_DAMAGE_PER_FT = 0.015  # 1.5% per ft of surge


def haversine_mi(lat1, lon1, lat2, lon2):
    R = EARTH_RADIUS_MI
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def interpolate_wind(lat, lon, track_points):
    """Estimate max wind at a location based on distance from track."""
    min_dist = float("inf")
    max_wind = 0
    closest_date = None

    for tp in track_points:
        d = haversine_mi(lat, lon, tp["lat"], tp["lon"])
        if d < min_dist:
            min_dist = d
            max_wind = tp["max_wind_kt"]
            closest_date = tp["date"]

    # Wind decays with distance: ~5% per 10mi, roughly
    if min_dist > 200:
        return 0, closest_date
    decay = max(0, 1 - (min_dist / 200) * 0.5)
    return int(max_wind * decay), closest_date


def estimate_surge(dist_mi, category):
    """Estimate surge at a distance from landfall."""
    base_surge = {3: CAT_3_SURGE_FT, 4: CAT_4_SURGE_FT, 5: CAT_5_SURGE_FT}.get(category, 5)
    if dist_mi > 150:
        return 0
    decay = max(0, 1 - (dist_mi / 150))
    return round(base_surge * decay, 1)


@router.get("/storm/{storm_id}/impact", response_model=ImpactResponse)
def storm_impact(
    storm_id: str,
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
):
    """Get storm impact at a specific lat/lon."""
    storm = get_storm_by_id(storm_id)
    if not storm:
        raise HTTPException(status_code=404, detail=f"Storm '{storm_id}' not found")

    # Find closest approach
    closest_dist = float("inf")
    closest_date = None
    max_wind_at_loc = 0

    for tp in storm["track_points"]:
        d = haversine_mi(lat, lon, tp["lat"], tp["lon"])
        if d < closest_dist:
            closest_dist = d
            closest_date = tp["date"]
            max_wind_at_loc = tp["max_wind_kt"]

    # Decay wind with distance
    wind_at_loc, _ = interpolate_wind(lat, lon, storm["track_points"])
    surge_at_loc = estimate_surge(closest_dist, storm["category"])

    return ImpactResponse(
        storm_id=storm["storm_id"],
        name=storm["name"],
        year=storm["year"],
        closest_approach_mi=round(closest_dist, 1),
        closest_approach_date=closest_date,
        max_surge_at_location_ft=surge_at_loc,
        max_wind_at_location_kt=wind_at_loc,
    )


@router.get("/return-period", response_model=ReturnPeriodResponse)
def return_period(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
):
    """
    Estimate return periods for major hurricane categories.
    Based on historical storm proximity within the dataset (1992-2024).
    """
    storms = get_all_storms()
    years_span = 33  # 1992-2024

    cat3_count = 0
    cat4_count = 0
    cat5_count = 0

    for storm in storms:
        min_dist = float("inf")
        for tp in storm["track_points"]:
            d = haversine_mi(lat, lon, tp["lat"], tp["lon"])
            if d < min_dist:
                min_dist = d

        # If storm passed within 100mi, count it
        if min_dist <= 100:
            if storm["category"] >= 3:
                cat3_count += 1
            if storm["category"] >= 4:
                cat4_count += 1
            if storm["category"] >= 5:
                cat5_count += 1

    # Return period = span / count
    cat3_rp = round(years_span / cat3_count) if cat3_count > 0 else 100
    cat4_rp = round(years_span / cat4_count) if cat4_count > 0 else 100
    cat5_rp = round(years_span / cat5_count) if cat5_count > 0 else 100

    return ReturnPeriodResponse(
        lat=lat,
        lon=lon,
        category_3_return_years=min(cat3_rp, 100),
        category_4_return_years=min(cat4_rp, 100),
        category_5_return_years=min(cat5_rp, 100),
    )


@router.post("/risk/summary", response_model=RiskSummaryResponse)
def risk_summary(body: RiskSummaryRequest):
    """
    Compute a risk summary for a property location.
    Estimates damage from surge and wind based on historical worst-case
    storms in the dataset, scaled by property value.
    """
    lat, lon = body.lat, body.lon
    pv = body.property_value_usd

    storms = get_all_storms()
    exposure_years = max(s["year"] for s in storms) - min(s["year"] for s in storms) + 1

    worst_wind = 0
    worst_surge = 0.0
    nearest = None
    nearest_dist = float("inf")

    for storm in storms:
        min_dist = float("inf")
        for tp in storm["track_points"]:
            d = haversine_mi(lat, lon, tp["lat"], tp["lon"])
            if d < min_dist:
                min_dist = d

        if min_dist < nearest_dist:
            nearest_dist = min_dist
            nearest = storm["name"]

        wind_at_loc, _ = interpolate_wind(lat, lon, storm["track_points"])
        surge_at_loc = estimate_surge(min_dist, storm["category"])

        if wind_at_loc > worst_wind:
            worst_wind = wind_at_loc
        if surge_at_loc > worst_surge:
            worst_surge = surge_at_loc

    # Damage estimates
    # Wind: 0.2% per kt above 50kt threshold
    wind_pct = max(0, min(1.0, (worst_wind - 50) * 0.002))
    wind_damage = round(pv * wind_pct, 0)

    # Surge: 1.5% per ft
    surge_pct = min(1.0, worst_surge * SURGE_DAMAGE_PER_FT)
    surge_damage = round(pv * surge_pct, 0)

    total = wind_damage + surge_damage
    total_pct = wind_pct + surge_pct

    return RiskSummaryResponse(
        lat=lat,
        lon=lon,
        property_value_usd=pv,
        nearest_storm=nearest,
        max_wind_recorded_kt=worst_wind if worst_wind > 0 else None,
        max_surge_recorded_ft=worst_surge if worst_surge > 0 else None,
        damage_estimate=DamageEstimate(
            surge_damage_usd=surge_damage,
            wind_damage_usd=wind_damage,
            total_damage_usd=total,
            surge_pct=round(surge_pct * 100, 2),
            wind_pct=round(wind_pct * 100, 2),
        ),
        exposure_years=exposure_years,
    )
