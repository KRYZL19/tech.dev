# MARINEDB — Boat Specifications & Marine Data API

*The data you'd spend an hour digging through boat forums to find. One call.*

## Hook
Sea Ray's website has specs for the 320 Sundancer. Boston Whaler's site has the 380 Realm. Boat traders, marine insurance apps, and fleet managers need both in one place. MARINEDB gives you 7 real boat models with full specs, fuel burn estimates, and insurance quotes via one API.

## Use it

```bash
# Get full specs for a Sea Ray 320
curl https://api.marinedb.io/v1/boat/sea_ray_320

# Search by type and length
curl "https://api.marinedb.io/v1/search?type=express_cruiser&max_length_ft=38"

# Estimate fuel burn for a 6-hour run
curl -X POST https://api.marinedb.io/v1/fuel-calc \
  -H "Content-Type: application/json" \
  -d '{"boat_id":"boston_whaler_380","hours_run":6}'

# Get insurance estimate
curl -X POST https://api.marinedb.io/v1/insurance \
  -H "Content-Type: application/json" \
  -d '{"boat_id":"sabrett_450","value_usd":480000,"deductible_usd":5000}'
```

## Example response

```json
{
  "make": "Boston Whaler",
  "model": "380 Realm",
  "year": 2022,
  "type": "center_console",
  "length_ft": 38,
  "beam_ft": 11.58,
  "dry_weight_lbs": 18500,
  "fuel_gal": 445,
  "max_horsepower": 1200,
  "hull_speed_knots": 46.2
}
```

## What it does

- **Boat specs** — length, beam, weight, fuel, water, waste, horsepower, hull material, deadrise
- **Fuel calculator** — estimate burn over hours, calculate range remaining
- **Insurance estimator** — annual premium based on boat value and type
- **Search** — filter by type, length, engine configuration
- **7 models** — Sea Ray, Boston Whaler, Jeanneau, Grady-White, Sabrett, MasterCraft, Generic

## Pricing

| Tier | Calls/day | Price |
|------|-----------|-------|
| Free | 100 | $0 |
| Dev | 10,000 | $19/mo |
| Pro | 100,000 | $49/mo |
