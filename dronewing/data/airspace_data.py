"""
Simplified airspace data for 5 metros: LA, NYC, Chicago, SF, Miami.
Each Class B airport has boundary coords, max altitude, grid cells (1x1 nm), UAS max altitude.
FAA Part 107: max 400ft AGL, 5mi from airports (without authorization).
"""

AIRSPACE_DATA = {
    "LA": {
        "name": "Los Angeles International",
        "airspace_class": "B",
        "center": (33.9425, -118.4081),
        "max_altitude_ft": 10000,
        "uas_max_altitude_ft": 400,
        "boundary": [
            (33.95, -118.45), (33.95, -118.30),
            (34.10, -118.30), (34.10, -118.45),
        ],
        # 1x1 nm grid cells around the airport (simplified)
        "grids": _build_la_grids(),
        "airport_buffer_mi": 5,
    },
    "NYC": {
        "name": "John F Kennedy International",
        "airspace_class": "B",
        "center": (40.6413, -73.7781),
        "max_altitude_ft": 10000,
        "uas_max_altitude_ft": 400,
        "boundary": [
            (40.70, -73.85), (40.70, -73.65),
            (40.55, -73.65), (40.55, -73.85),
        ],
        "grids": _build_nyc_grids(),
        "airport_buffer_mi": 5,
    },
    "Chicago": {
        "name": "O'Hare International",
        "airspace_class": "B",
        "center": (41.9742, -87.9073),
        "max_altitude_ft": 10000,
        "uas_max_altitude_ft": 400,
        "boundary": [
            (42.05, -88.00), (42.05, -87.80),
            (41.85, -87.80), (41.85, -88.00),
        ],
        "grids": _build_chicago_grids(),
        "airport_buffer_mi": 5,
    },
    "SF": {
        "name": "San Francisco International",
        "airspace_class": "B",
        "center": (37.6213, -122.3790),
        "max_altitude_ft": 10000,
        "uas_max_altitude_ft": 400,
        "boundary": [
            (37.70, -122.45), (37.70, -122.25),
            (37.50, -122.25), (37.50, -122.45),
        ],
        "grids": _build_sf_grids(),
        "airport_buffer_mi": 5,
    },
    "Miami": {
        "name": "Miami International",
        "airspace_class": "B",
        "center": (25.7959, -80.2870),
        "max_altitude_ft": 10000,
        "uas_max_altitude_ft": 400,
        "boundary": [
            (25.85, -80.35), (25.85, -80.20),
            (25.70, -80.20), (25.70, -80.35),
        ],
        "grids": _build_miami_grids(),
        "airport_buffer_mi": 5,
    },
}


def _build_la_grids():
    grids = {}
    base_lat, base_lon = 33.93, -118.42
    for row in range(10):
        for col in range(10):
            grid_id = f"LA-UAS-{row:02d}-{col:02d}"
            grids[grid_id] = {
                "lat": round(base_lat + row * 0.01, 4),
                "lon": round(base_lon + col * 0.01, 4),
                "max_altitude_ft": 400,
            }
    return grids


def _build_nyc_grids():
    grids = {}
    base_lat, base_lon = 40.55, -73.82
    for row in range(10):
        for col in range(10):
            grid_id = f"NYC-UAS-{row:02d}-{col:02d}"
            grids[grid_id] = {
                "lat": round(base_lat + row * 0.01, 4),
                "lon": round(base_lon + col * 0.01, 4),
                "max_altitude_ft": 400,
            }
    return grids


def _build_chicago_grids():
    grids = {}
    base_lat, base_lon = 41.85, -87.98
    for row in range(10):
        for col in range(10):
            grid_id = f"CHI-UAS-{row:02d}-{col:02d}"
            grids[grid_id] = {
                "lat": round(base_lat + row * 0.01, 4),
                "lon": round(base_lon + col * 0.01, 4),
                "max_altitude_ft": 400,
            }
    return grids


def _build_sf_grids():
    grids = {}
    base_lat, base_lon = 37.50, -122.43
    for row in range(10):
        for col in range(10):
            grid_id = f"SFO-UAS-{row:02d}-{col:02d}"
            grids[grid_id] = {
                "lat": round(base_lat + row * 0.01, 4),
                "lon": round(base_lon + col * 0.01, 4),
                "max_altitude_ft": 400,
            }
    return grids


def _build_miami_grids():
    grids = {}
    base_lat, base_lon = 25.70, -80.33
    for row in range(10):
        for col in range(10):
            grid_id = f"MIA-UAS-{row:02d}-{col:02d}"
            grids[grid_id] = {
                "lat": round(base_lat + row * 0.01, 4),
                "lon": round(base_lon + col * 0.01, 4),
                "max_altitude_ft": 400,
            }
    return grids


def point_in_boundary(lat, lon, boundary):
    """Ray-casting point-in-polygon check."""
    n = len(boundary)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = boundary[i]
        xj, yj = boundary[j]
        if ((yi > lat) != (yj > lat)) and (lon < (xj - xi) * (lat - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


def haversine_mi(lat1, lon1, lat2, lon2):
    """Approximate great-circle distance in miles."""
    import math
    R = 3958.8
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))
