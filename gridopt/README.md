# GRIDOPT API

**Energy Tariff & Optimization API** — A FastAPI backend that serves time-of-use (TOU) tariff data for US utilities and optimizes appliance schedules for cost savings.

## Features

- **TOU Tariff Lookup** — Get time-of-use pricing for 10 major US utilities
- **Smart Scheduling** — Optimize when to run appliances based on your utility's TOU rates
- **Carbon Intensity** — Current grid carbon intensity by region

## Pricing Tiers

| Tier  | Price       | Monthly Calls |
|-------|-------------|---------------|
| Free  | $0/mo       | 500 calls     |
| Dev   | $9/mo       | 10,000 calls  |
| Pro   | $49/mo      | 100,000 calls |

## Run Locally

```bash
cd gridopt
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API will be available at `http://localhost:8000`. Docs at `http://localhost:8000/docs`.

## Example curl Calls

### Get a tariff
```bash
curl "http://localhost:8000/api/v1/tariffs/pge"
```

### Search utilities
```bash
curl "http://localhost:8000/api/v1/tariffs/search?q=california"
```

### Optimize a schedule
```bash
curl -X POST "http://localhost:8000/api/v1/optimize/schedule" \
  -H "Content-Type: application/json" \
  -d '{
    "appliances": [
      {"name": "Dishwasher", "duration_hours": 2, "priority": 1},
      {"name": "EV Charger", "duration_hours": 4, "priority": 2}
    ],
    "tariff": {
      "utility_id": "pge",
      "utility_name": "Pacific Gas & Electric",
      "timezone": "America/Los_Angeles",
      "periods": [
        {"name": "off-peak", "start_hour": 0, "end_hour": 7, "price_per_kwh": 0.22},
        {"name": "peak", "start_hour": 14, "end_hour": 21, "price_per_kwh": 0.52}
      ]
    }
  }'
```

### Carbon intensity
```bash
curl "http://localhost:8000/api/v1/carbon/intensity?region=CA"
```

### Health check
```bash
curl "http://localhost:8000/api/v1/health"
```

## Deploy

### Railway
```bash
railway up
```

### Render
```bash
render.yaml included — deploy to render.com directly
```

## Documentation

Full documentation: [https://docs.gridopt.api](https://docs.gridopt.api) *(placeholder)*

## Supported Utilities

- Pacific Gas & Electric (PG&E) — California
- Southern California Edison (SCE) — California
- San Diego Gas & Electric (SDG&E) — California
- Consolidated Edison (ConEd) — New York
- Dominion Energy — Virginia
- Duke Energy — North Carolina
- Austin Energy — Texas
- Sacramento Municipal Utility District (SMUD) — California
- Arizona Public Service (APS) — Arizona
- Xcel Energy — Colorado
