# AIRCRAFTDB — FAA Aircraft Registry Lookup

**"N-number lookup before you buy. Airworthiness status, useful load, owner history."**

A lightweight Flask API backed by a curated dataset of 100 aircraft from the FAA registry.

## Quick Start

```bash
cd aircraftdb
pip install -r requirements.txt
python main.py
```

Server runs on `http://0.0.0.0:5000`.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/aircraft/{n_number}` | Aircraft details, weights, airworthiness |
| `GET` | `/api/v1/aircraft/{n_number}/history` | Owner history, registration changes |
| `POST` | `/api/v1/aircraft/useful-load` | Compute useful load |
| `GET` | `/api/v1/registry/expiring?days={n}` | Registrations expiring within N days |
| `GET` | `/api/v1/manufacturer/{mfr}` | Aircraft by manufacturer |

## Bundled Aircraft

- **Cessna 172** (20) — N1001–N1020
- **Cessna 182** (15) — N1021–N1035
- **Cessna 206** (10) — N1036–N1045
- **Piper PA-28** (15) — N1046–N1060
- **Beechcraft Bonanza** (10) — N1061–N1070
- **Diamond DA40** (5) — N1071–N1075
- **Cirrus SR20** (5) — N1076–N1080
- **Cirrus SR22** (15) — N1081–N1095
- **Robinson R44** (5) — N1096–N1100

## Examples

### Lookup an aircraft
```bash
curl http://localhost:5000/api/v1/aircraft/N1001
```

### Owner history
```bash
curl http://localhost:5000/api/v1/aircraft/N1001/history
```

### Useful load calculation
```bash
curl -X POST http://localhost:5000/api/v1/aircraft/useful-load \
  -H "Content-Type: application/json" \
  -d '{"n_number":"N1001","pilot_weight":200,"passengers":150,"baggage":30,"fuel_gallons":40}'
```

### Expiring registrations
```bash
curl "http://localhost:5000/api/v1/registry/expiring?days=180"
```

### Aircraft by manufacturer
```bash
curl http://localhost:5000/api/v1/manufacturer/cirrus
```

## Deployment

```bash
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```
