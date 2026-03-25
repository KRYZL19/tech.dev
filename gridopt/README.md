# GRIDOPT API

Time-of-Use energy tariff data and optimization algorithms for developers.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API runs at http://localhost:8000 — docs at http://localhost:8000/docs

## Endpoints

### Health
```bash
curl http://localhost:8000/health
```

### List Tariffs
```bash
curl http://localhost:8000/api/v1/tariffs/
```

### Get Specific Tariff
```bash
curl http://localhost:8000/api/v1/tariffs/pge
```

### Search Tariffs
```bash
curl "http://localhost:8000/api/v1/tariffs/search?q=california"
```

### Optimize Schedule
```bash
curl -X POST http://localhost:8000/api/v1/optimize/schedule \
  -H "Content-Type: application/json" \
  -d '{
    "utility_id": "pge",
    "devices": [
      {"name": "dishwasher", "duration_hours": 2, "priority": 2, "power_kw": 1.5}
    ]
  }'
```

### Carbon Intensity
```bash
curl "http://localhost:8000/api/v1/carbon/intensity?region=caiso"
```

## Pricing

| Tier | Price | Requests/mo |
|------|-------|-------------|
| Free | $0 | 500 |
| Dev | $9 | 10,000 |
| Pro | $49 | 100,000 |

## Utilities Supported

- PG&E (pge)
- Southern California Edison (sce)
- San Diego Gas & Electric (sdge)
- ConEd (coned)
- Dominion Energy (dominion)
- Duke Energy (duke)
- Austin Energy (austin_energy)
- SMUD (smud)
- Arizona Public Service (aps)
- Xcel Energy (xcel)

## Deploy

### Render
```bash
render deploy
```

### Railway
Railway auto-detects from railway.toml.
