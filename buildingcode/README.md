# US Building Code Cross-Reference API

**Hook:** "What version of the IBC does your city use? What did they adopt and when?"

A FastAPI-based REST API that provides building code adoption information across US cities, code section lookup, permit checklists, and ADA requirements.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/adoption/{state}/{city}` | City code adoption: version, effective date, amendments |
| GET | `/api/v1/code/{code_name}/{version}/section/{section}` | Code section text with referenced standards |
| GET | `/api/v1/state/{state}/codes` | State-level code adoption summary |
| POST | `/api/v1/permit/checklist` | Required permits, inspections, setbacks for a project |
| GET | `/api/v1/ada/requirements/{building_type}` | ADA requirements by occupancy type |

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Server runs at `http://localhost:8000`. API docs at `http://localhost:8000/docs`.

## Examples

### City adoption lookup
```bash
curl "http://localhost:8000/api/v1/adoption/CA/Los%20Angeles"
```

### Code section lookup
```bash
curl "http://localhost:8000/api/v1/code/IBC/2021/section/1008.1"
```

### State codes
```bash
curl "http://localhost:8000/api/v1/state/TX/codes"
```

### Permit checklist
```bash
curl -X POST "http://localhost:8000/api/v1/permit/checklist" \
  -H "Content-Type: application/json" \
  -d '{"city": "Houston", "project_type": "commercial", "sqft": 5000}'
```

### ADA requirements
```bash
curl "http://localhost:8000/api/v1/ada/requirements/R-2"
```

## Codes Covered

- **IBC 2021/2022** — International Building Code
- **IRC 2021** — International Residential Code
- **NEC 2023** — National Electrical Code (NFPA 70)

## Cities in Database

AZ: Phoenix  
CA: Los Angeles, San Diego, San Francisco  
CO: Denver  
FL: Jacksonville, Miami, Tampa  
GA: Atlanta  
IL: Chicago  
MA: Boston  
NV: Las Vegas  
NY: Buffalo, New York City  
OR: Portland  
TX: Austin, Dallas, Houston, San Antonio  
WA: Seattle, Spokane

## Building Types for ADA

A-1, A-2, A-3, B, E, F-1, F-2, H-1, I-2, I-4, M, R-1, R-2, R-4, S-1, S-2, U

## Project Types for Permit Checklist

`commercial`, `residential`, `addition`, `alteration`
