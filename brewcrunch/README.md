# BREWCRUNCH API 🍺

> _"I spent more time doing math than brewing. ABV, IBU, OG, attenuation — none of this should require a calculator app that shows ads."_

A FastAPI backend for homebrew beer calculations and BJCP style matching. No ads. No subscriptions required for basic use.

## Features

- **ABV Calculator** — Original Gravity + Final Gravity → ABV + Attenuation
- **IBU Calculator** — Tinseth formula for accurate hop bitterness
- **OG Calculator** — Estimate gravity from grain bill
- **Style Checker** — Match your recipe against 25 BJCP styles
- **Hop Database** — 20 varieties with AA%, type, and typical use
- **Grain Database** — 25 varieties with PPG and Lovibond ratings

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py

# Or with uvicorn directly
uvicorn main:app --reload --port 8000
```

API available at `http://localhost:8000`  
Docs at `http://localhost:8000/docs`

## API Endpoints

### Calculators

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/calculate/abv` | POST | Calculate ABV from OG/FG |
| `/api/v1/calculate/ibu` | POST | Calculate IBU (Tinseth formula) |
| `/api/v1/calculate/og` | POST | Estimate OG from grain bill |

### Recipe

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/recipe/check-style` | POST | Match recipe to BJCP styles |
| `/api/v1/styles` | GET | List all BJCP styles |

### Data

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/hops/{variety}` | GET | Get hop details |
| `/api/v1/hops` | GET | List all hops |
| `/api/v1/grains/{variety}` | GET | Get grain details |
| `/api/v1/grains` | GET | List all grains |

## Example Usage

### Calculate ABV

```bash
curl -X POST http://localhost:8000/api/v1/calculate/abv \
  -H "Content-Type: application/json" \
  -d '{"og": 1.055, "fg": 1.012}'
```

Response:
```json
{"abv": 5.64, "attenuation": 78.18}
```

### Calculate IBU

```bash
curl -X POST http://localhost:8000/api/v1/calculate/ibu \
  -H "Content-Type: application/json" \
  -d '{"oz_hops": 1.0, "aa_percent": 5.5, "boil_time_minutes": 60, "og": 1.050, "volume_gallons": 5.0}'
```

Response:
```json
{"ibu": 29.4}
```

### Check Style Match

```bash
curl -X POST http://localhost:8000/api/v1/recipe/check-style \
  -H "Content-Type: application/json" \
  -d '{"og": 1.065, "fg": 1.015, "ibu": 55, "abv": 6.5}'
```

## Pricing

| Tier | Calls/Day | Price |
|------|-----------|-------|
| Free | 200 | $0 |
| Dev | Unlimited | $9/month |
| Pro | Unlimited | $29/month |

## Tech Stack

- **FastAPI** — Modern Python web framework
- **Pydantic** — Data validation
- **Uvicorn** — ASGI server

## License

MIT
