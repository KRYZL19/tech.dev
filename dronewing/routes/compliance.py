from fastapi import APIRouter
from models.schemas import FlightPlanRequest, FlightPlanResponse
from data.airspace_data import AIRSPACE_DATA, point_in_boundary, haversine_mi

router = APIRouter(prefix="/api/v1", tags=["compliance"])

# Assume drone cruise speed ~30 mph
DRONE_SPEED_MPH = 30


def estimate_flight_time(waypoints) -> float:
    """Sum haversine distances between waypoints and divide by speed."""
    total_mi = 0.0
    for i in range(len(waypoints) - 1):
        total_mi += haversine_mi(
            waypoints[i].lat, waypoints[i].lon,
            waypoints[i + 1].lat, waypoints[i + 1].lon,
        )
    return round(total_mi / DRONE_SPEED_MPH * 60, 1)


def check_waypoint_conflict(wp, data):
    """Return list of conflicts for a single waypoint."""
    conflicts = []
    city = data["name"]
    in_boundary = point_in_boundary(wp.lat, wp.lon, data["boundary"])
    dist_mi = haversine_mi(wp.lat, wp.lon, data["center"][0], data["center"][1])

    if in_boundary:
        conflicts.append(f"Waypoint inside {city} Class B airspace — LAANC required.")
    elif dist_mi < data["airport_buffer_mi"]:
        conflicts.append(f"Waypoint within {dist_mi:.1f}mi of {city} — restricted. Clear of airspace?")
    if wp.alt > data["uas_max_altitude_ft"]:
        conflicts.append(f"Waypoint altitude {wp.alt}ft exceeds UAS max {data['uas_max_altitude_ft']}ft.")
    return conflicts


@router.post("/flight/plan", response_model=FlightPlanResponse)
def plan_flight(body: FlightPlanRequest):
    """
    Analyze a flight plan (list of waypoints) for airspace conflicts,
    total flight time, and Part 107 warnings.
    """
    all_conflicts = []
    all_warnings = []

    for city, data in AIRSPACE_DATA.items():
        for i, wp in enumerate(body.waypoints):
            conflicts = check_waypoint_conflict(wp, data)
            for c in conflicts:
                all_conflicts.append(f"[WP{i+1}] {c}")

    # Part 107 general checks
    if not body.waypoints:
        all_warnings.append("No waypoints provided.")
    else:
        for i, wp in enumerate(body.waypoints):
            if wp.alt > 400:
                all_warnings.append(f"[WP{i+1}] Altitude {wp.alt}ft exceeds Part 107 ceiling (400ft AGL).")

    total_time = estimate_flight_time(body.waypoints) if len(body.waypoints) > 1 else 0.5

    if not all_conflicts:
        all_warnings.append("Flight plan is clear of known airspace restrictions.")

    return FlightPlanResponse(
        airspace_conflicts=all_conflicts,
        total_flight_time_min=total_time,
        warnings=all_warnings,
    )
