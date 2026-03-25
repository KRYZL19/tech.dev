# DRONEWING API

> "LAANC authorization takes 30 seconds if you know the grid ID. Most apps make you tap through 12 screens."

**DRONEWING** is a FastAPI backend for drone flight compliance and airspace intelligence. It tells pilots where they can fly, which grid to use for LAANC, and whether their flight plan has conflicts — in one API call.

---

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs at `http://localhost:8000/docs`

---

## Endpoints

### `POST /api/v1/airspace/check`
Check airspace class, LAANC eligibility, and altitude limits.

```json
{
  "lat": 33.9425,
  "lon": -118.4081,
  "altitude_ft": 200,
  "drone_class": "standard"
}
```

```json
{
  "airspace_class": "B",
  "laanc_eligible": true,
  "max_altitude_ft": 400,
  "warnings": ["Within LA Class B airspace — LAANC authorization required."]
}
```

---

### `GET /api/v1/grid/search`
Find the nearest FAA UAS facility map grid ID for LAANC authorization.

```
GET /api/v1/grid/search?lat=33.9425&lon=-118.4081
```

```json
{
  "grid_id": "LA-UAS-01-04",
  "lat": 33.94,
  "lon": -118.38,
  "max_altitude_ft": 400,
  "city": "LA"
}
```

---

### `POST /api/v1/flight/plan`
Analyze a multi-waypoint flight plan for airspace conflicts.

```json
{
  "waypoints": [
    { "lat": 33.9425, "lon": -118.4081, "alt": 200 },
    { "lat": 33.9500, "lon": -118.4100, "alt": 300 }
  ],
  "drone_class": "standard"
}
```

```json
{
  "airspace_conflicts": ["[WP1] Within LA Class B airspace — LAANC required."],
  "total_flight_time_min": 3.2,
  "warnings": []
}
```

---

## Pricing

| Plan | Requests | Price |
|------|----------|-------|
| Free | 50/day | $0 |
| Dev  | unlimited | $19/mo |
| Pro  | unlimited + SLA | $59/mo |

*Rate limiting is not yet enforced in this implementation.*

---

## Airspace Coverage

Bundled Class B airport data for:

| City | Airport |
|------|---------|
| Los Angeles | LAX |
| New York City | JFK |
| Chicago | ORD |
| San Francisco | SFO |
| Miami | MIA |

Each includes:
- Boundary polygon
- Max altitude (UAS ceiling 400ft)
- 10×10 grid cells (1×1 nm each) for LAANC

---

## FAA Part 107 Rules Encoded

- Max **400ft AGL** (or 400ft above terrain/structures)
- **5nm airport buffer** — authorization required
- LAANC-eligible grids allow real-time authorization

---

## Tech

- **FastAPI** + **Uvicorn** + **Pydantic**
- Zero external dependencies beyond the stdlib
- Runs anywhere — no FAA API key required for this data bundle
