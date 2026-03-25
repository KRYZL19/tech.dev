# HVACCALC — HVAC System Sizing Calculator API

> **Manual J is required by code for every HVAC install. Nobody does it manually. This does it in one API call.**

Fast, free(ish) HVAC load calculation API using IECC 2021 climate zones and a Manual J simplified methodology.

---

## Endpoints

### `POST /api/v1/load/residential`
Calculate heating and cooling load for a residential property.

```json
{
  "sqft": 2000,
  "ceiling_height_ft": 9,
  "insulation_r_value": 19,
  "climate_zone": "3",
  "num_occupants": 4,
  "num_exterior_walls": 2
}
```
```json
{
  "cooling_btu": 54800,
  "heating_btu": 52400,
  "tons_ac_needed": 4.57,
  "cfm_cooling": 1828,
  "oversize_warning": false,
  "methodology": "IECC 2021 / Manual J simplified"
}
```

### `GET /api/v1/climate/{zipcode}`
Look up IECC 2021 climate zone data from a ZIP code.

```json
{
  "zipcode": "30301",
  "found": true,
  "climate_zone": "3",
  "zone_name": "Hot-Humid / Mixed",
  "cooling_design_temp_f": 87,
  "heating_design_temp_f": 19,
  "hdd_base_65": 2300,
  "cdd_base_65": 2800,
  "tons_per_sqft": 420
}
```

### `POST /api/v1/duct/size`
Size ductwork using the equal friction method.

```json
{
  "btu_load": 54800,
  "duct_length_ft": 60,
  "num_runs": 8,
  "friction_rate": 0.08
}
```
```json
{
  "cfm_per_run": 456.7,
  "duct_diameter_inches": 10.2,
  "velocity_fpm": 724,
  "friction_rate_used": 0.08,
  "total_cfm": 3653.3,
  "velocity_category": "MEDIUM"
}
```

### `POST /api/v1/equipment/size`
Recommend HVAC equipment size and flag oversizing.

```json
{
  "cooling_btu": 54800,
  "heating_btu": 52400,
  "efficiency_rating": 16,
  "equipment_type": "central_ac"
}
```
```json
{
  "cooling_tons": 4.5,
  "heating_kbtu": 52.4,
  "recommended_unit_size": "4.0-ton AC (48000 BTU) SEER2 16",
  "oversize_warning": false,
  "undersize_warning": false,
  "oversize_btu": 0
}
```

---

## Pricing

| Tier | Rate | Limits |
|------|------|--------|
| **Free** | $0 | 50 requests/day |
| **Dev** | $19/mo | 1,000 requests/day |
| **Pro** | $49/mo | Unlimited |

Authenticate with `X-API-Key: pk_dev_...` or `X-API-Key: pk_pro_...` header.

---

## Installation

```bash
pip install -r requirements.txt
python main.py
```

Server starts at `http://0.0.0.0:8000`. Docs at `http://localhost:8000/docs`.

---

## Methodology

- **Climate zones:** IECC 2021 (zones 1–8), ~40,000+ US ZIP codes mapped
- **Cooling load:** Base BTU/sqft × insulation factor × ceiling height × exterior wall factor + occupant load
- **Heating load:** Same approach, zone-specific heating factors
- **Duct sizing:** Equal friction method
- **Equipment:** Rounded to nearest standard tonnage, 15% threshold for oversize/undersize warnings

---

## Tech Stack

- **FastAPI** — async API framework
- **Pydantic v2** — request/response validation
- **uvicorn** — ASGI server
