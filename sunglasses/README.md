# SUNGLASSES — Aviation Incident Report Database

> "That airport has 12 laser incidents reported in the last year. One query."

A FastAPI-powered REST API serving 200 sample NASA ASRS-style aviation incident reports — laser illuminations, wildlife strikes, operational incidents, and near-midair conflicts.

## Quick Start

```bash
cd sunglasses
pip install -r requirements.txt
uvicorn main:app --reload --port 8765
```

API available at `http://localhost:8765`.  
Docs at `http://localhost:8765/docs`.

## Endpoints

### Search incidents near an airport
```
GET /api/v1/incidents/search?airport_code={ICAO}&radius_mi={r}&year={y}
```
- `airport_code` — ICAO code (required)
- `radius_mi` — search radius in miles (optional, defaults to all incidents at airport)
- `year` — filter by year (optional)

### Full incident detail
```
GET /api/v1/incident/{report_id}
```
Returns date, aircraft_type, crew effects, pilot description, and full narrative.

### Airport incident summary
```
GET /api/v1/airport/{ICAO}/summary
```
Returns total_incidents, incident_count_by_type, year_range, and most_common_hazard.

### Filter by incident type
```
GET /api/v1/incidents/type/{type}
```
Valid types: `laser`, `wildlife`, `operational_incident`, `near_mid`.

## Example Queries

**"How many laser incidents at KLAX in 2024?"**
```bash
curl "http://localhost:8765/api/v1/airport/KLAX/summary"
```

**"Show me all wildlife strikes near KJFK within 5 miles"**
```bash
curl "http://localhost:8765/api/v1/incidents/search?airport_code=KJFK&radius_mi=5&year=2024"
```

**"Full report for LASR-2024-0037"**
```bash
curl "http://localhost:8765/api/v1/incident/LASR-2024-0037"
```

**"All near-midair incidents"**
```bash
curl "http://localhost:8765/api/v1/incidents/type/near_mid"
```

## Dataset

200 synthetic NASA ASRS-style incident reports spanning:
- **Laser illuminations** — cockpit flash blindness, afterimages, temporary vision loss
- **Wildlife strikes** — bird ingestion, radome damage, engine FOD
- **Operational incidents** — ATC miscommunications, TCAS RAs, equipment failures
- **Near-midair conflicts** — separation losses, runway incursions, wake turbulence encounters

Covering 20 major US airports with realistic lat/lon coordinates and dated incidents from 2023–2025.

## Tech Stack

- **FastAPI** — async REST API
- **Pydantic** — request/response validation
- **Uvicorn** — ASGI server
