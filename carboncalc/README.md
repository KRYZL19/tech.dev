# CARBONCALC API

> A container from Shanghai to Rotterdam emits 1.5 tons of CO2. Your logistics team doesn't know this because there's no simple API.

CARBONCALC provides carbon footprint calculations for shipping, road freight, and aviation — with tree-based offset estimation.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API docs: http://localhost:8000/docs

## Endpoints

### POST `/api/v1/ship/carbon`
Ocean freight CO2 emissions.

```json
{
  "distance_nm": 11500,
  "cargo_tons": 20000,
  "vessel_type": "container"
}
```

**Vessel types:** `container`, `bulk`, `roro`

**Emission factors (IMO 4th GHG Study):**
| Vessel | g CO₂/t-nm |
|--------|-----------|
| Container ship | 0.016 |
| Bulk carrier | 0.006 |
| Ro-ro vessel | 0.022 |

---

### POST `/api/v1/truck/carbon`
Road freight CO2 emissions.

```json
{
  "distance_km": 800,
  "cargo_kg": 18000,
  "fuel_type": "diesel",
  "truck_type": "heavy"
}
```

**Fuel types:** `diesel`, `lng`, `electric`  
**Truck types:** `standard`, `heavy`

---

### POST `/api/v1/offset/trees`
Trees needed to offset CO2 via natural sequestration.

```json
{ "co2_kg": 1500 }
```

Uses 21 kg CO₂/tree/year × 20 years = **420 kg CO₂/tree**

---

### POST `/api/v1/supply-chain/summary`
Multi-modal supply chain carbon report.

```json
{
  "shipments": [
    { "type": "container_ship", "distance": 11500, "cargo": 20000 },
    { "type": "truck_diesel", "distance": 300, "cargo": 20 }
  ]
}
```

**Shipment types:** `container_ship`, `bulk_carrier`, `roro_vessel`, `truck_diesel`, `truck_lng`, `aviation_short`, `aviation_long`

---

## Pricing

| Plan | Rate |
|------|------|
| Free | 100 req/day |
| Dev | $19/mo |
| Pro | $59/mo |

## Data Sources

- IMO 4th GHG Study (shipping emission factors)
- DEFRA 2023 (UK truck & aviation factors)
- US EPA (tree sequestration estimates)

## Run Tests

```bash
pip install httpx
uvicorn main:app &
curl -X POST http://localhost:8000/api/v1/ship/carbon \
  -H "Content-Type: application/json" \
  -d '{"distance_nm": 11500, "cargo_tons": 20000, "vessel_type": "container"}'
```
