# MARINEDB

**Marine Navigation & Conditions API**

> *"Tides don't care about your schedule. Neither should your autopilot."*

MARINEDB provides real-time port data, tide predictions, and route planning for coastal vessels along major US waterways.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs: `http://localhost:8000/docs`

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/ports/search?q={query}` | Search ports by name |
| GET | `/api/v1/port/{port_id}` | Get port details |
| GET | `/api/v1/tides/{port_id}?days=3` | Tide predictions |
| POST | `/api/v1/route/distance` | Calculate route distance & ETA |
| POST | `/api/v1/fuel/estimate` | Estimate fuel cost |

## Ports

- **San Francisco Bay** (37.8°N, 122.4°W) — Pacific Coast
- **Miami** (25.8°N, 80.2°W) — Florida Coast
- **Seattle** (47.6°N, 122.3°W) — Pacific Northwest
- **New York Harbor** (40.7°N, 74.0°W) — Atlantic Coast
- **San Diego** (32.7°N, 117.2°W) — Pacific Coast

## Pricing

| Tier | Calls/Day | Price |
|------|-----------|-------|
| Free | 100 | $0 |
| Dev | Unlimited | $19/mo |
| Pro | Unlimited + Priority | $49/mo |

## Examples

### Search Ports
```bash
curl "http://localhost:8000/api/v1/ports/search?q=san"
```

### Get Tides
```bash
curl "http://localhost:8000/api/v1/tides/sf?days=3"
```

### Calculate Route
```bash
curl -X POST "http://localhost:8000/api/v1/route/distance" \
  -H "Content-Type: application/json" \
  -d '{"waypoints": [{"lat": 37.8, "lon": -122.4}, {"lat": 47.6, "lon": -122.3}]}'
```

### Fuel Estimate
```bash
curl -X POST "http://localhost:8000/api/v1/fuel/estimate" \
  -H "Content-Type: application/json" \
  -d '{"distance_nm": 150, "fuel_gph": 5, "fuel_price_per_gal": 4.50}'
```
