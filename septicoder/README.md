# SEPTICODE — Septic System Design Validator

> "Perc tests are the #1 reason rural property deals fall through. This API does it in 3 seconds."

A FastAPI backend for validating septic system designs. Calculate percolation rates, size systems, and generate permit checklists instantly.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/percolate` | Calculate percolation rate and approval status |
| `POST` | `/api/v1/system/size` | Size a septic system |
| `GET` | `/api/v1/soil/{county_name}` | Get soil data for a county |
| `POST` | `/api/v1/permit/checklist` | Generate permit checklist |

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Pricing

| Tier | Rate | Daily Requests |
|------|------|----------------|
| Free | $0 | 50/day |
| Dev | $19/mo | 1,000/day |
| Pro | $49/mo | Unlimited |

## Soil Types

| Soil Type | Perc Rate (min/inch) |
|-----------|---------------------|
| sand | 5 |
| loamy sand | 15 |
| sandy loam | 25 |
| loam | 45 |
| silt loam | 60 |
| clay | 120 |

## Supported Counties

CA: Fresno, Los Angeles, Sacramento, San Diego
TX: Harris, Travis
FL: Miami-Dade, Hillsborough
NC: Wake
WA: King
