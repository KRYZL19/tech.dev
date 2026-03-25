from fastapi import APIRouter
from models.schemas import AirspaceCheckRequest, AirspaceCheckResponse, GridSearchResponse
from data.airspace_data import AIRSPACE_DATA, point_in_boundary, haversine_mi

router = APIRouter(prefix="/api/v1", tags=["airspace"])


@router.post("/airspace/check", response_model=AirspaceCheckResponse)
def check_airspace(body: AirspaceCheckRequest):
    """
    Check airspace classification, LAANC eligibility, and altitude limits
    for a given lat/lon/altitude.
    """
    warnings = []
    airspace_class = "G"  # Default: uncontrolled/G类
    laanc_eligible = False
    max_altitude_ft = 400  # Part 107 default

    for city, data in AIRSPACE_DATA.items():
        in_boundary = point_in_boundary(body.lat, body.lon, data["boundary"])
        dist_mi = haversine_mi(body.lat, body.lon, data["center"][0], data["center"][1])

        if in_boundary:
            airspace_class = data["airspace_class"]
            max_altitude_ft = data["uas_max_altitude_ft"]
            laanc_eligible = True
            warnings.append(f"Within {city} Class {airspace_class} airspace — LAANC authorization required.")
            if body.altitude_ft > max_altitude_ft:
                warnings.append(f"Requested altitude {body.altitude_ft}ft exceeds UAS max {max_altitude_ft}ft in this airspace.")
            break
        elif dist_mi < data["airport_buffer_mi"]:
            airspace_class = "D" if dist_mi < 2 else "E"
            max_altitude_ft = min(data["uas_max_altitude_ft"], 200)
            warnings.append(f"Within {dist_mi:.1f}mi of {city} airport — restricted zone. Max altitude {max_altitude_ft}ft.")

    if airspace_class == "G":
        if body.altitude_ft > 400:
            warnings.append("FAA Part 107: max 400ft AGL. You may need a waiver for higher altitudes.")
        else:
            warnings.append("Uncontrolled airspace — Part 107 rules apply (400ft max). No LAANC needed.")

    return AirspaceCheckResponse(
        airspace_class=airspace_class,
        laanc_eligible=laanc_eligible,
        max_altitude_ft=max_altitude_ft,
        warnings=warnings,
    )


@router.get("/grid/search", response_model=GridSearchResponse)
def search_grid(lat: float, lon: float):
    """
    Find the nearest FAA UAS facility map grid cell for LAANC authorization.
    Returns grid_id, center coords, and max altitude.
    """
    best_grid_id = None
    best_dist = float("inf")
    best_grid = None
    best_city = None

    for city, data in AIRSPACE_DATA.items():
        for grid_id, grid in data["grids"].items():
            d = haversine_mi(lat, lon, grid["lat"], grid["lon"])
            if d < best_dist:
                best_dist = d
                best_grid_id = grid_id
                best_grid = grid
                best_city = city

    if best_grid is None:
        return GridSearchResponse(
            grid_id="UNKNOWN",
            lat=lat,
            lon=lon,
            max_altitude_ft=400,
            city="Not in mapped area",
        )

    return GridSearchResponse(
        grid_id=best_grid_id,
        lat=best_grid["lat"],
        lon=best_grid["lon"],
        max_altitude_ft=best_grid["max_altitude_ft"],
        city=best_city,
    )
