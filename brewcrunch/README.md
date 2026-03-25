# BREWCRUNCH — Coffee Extraction API

*Your refractometer says 1.42% TDS. What does that actually mean? BREWCRUNCH tells you.*

## Hook
Every specialty coffee professional has a refractometer sitting on the bench. Most of them don't know what to do with the TDS reading. BREWCRUNCH turns that number into an extraction yield — the SCA standard — and tells you what to adjust.

## Use it

```bash
# Calculate extraction yield from TDS reading
curl -X POST https://api.brewcrunch.io/v1/extract \
  -H "Content-Type: application/json" \
  -d '{"coffee_g": 21, "water_ml": 340, "tds_percent": 1.38}'

# Estimate extraction without refractometer
curl "https://api.brewcrunch.io/v1/extract/estimate?coffee_g=21&water_ml=340&temp_f=205&brew_time_s=150"

# Check your brew ratio
curl "https://api.brewcrunch.io/v1/ratio?coffee_g=21&water_ml=340"

# Grind recommendations for V60
curl "https://api.brewcrunch.io/v1/grind/v60?coffee_g=22&water_ml=330"
```

## Example response

```json
{
  "input": {"coffee_g": 21, "water_ml": 340, "tds_percent": 1.38},
  "extraction": {
    "extraction_yield_percent": 20.8,
    "status": "optimal",
    "ideal_range": "18.0 – 22.0%"
  },
  "ratio": {
    "ratio": "1:16.2",
    "assessment": "optimal",
    "sca_ideal": "1:15 to 1:17"
  }
}
```

## What it does

- **Extraction yield** — converts TDS% to SCA extraction %, with under/over/optimal status
- **Ratio checker** — tells you if your coffee:water ratio is pulling weak or strong
- **Grind recommendations** — by brew method, with correct ratios and times
- **Estimate mode** — when you don't have a refractometer, estimate from parameters
- **6 methods** — V60, Chemex, French Press, Aeropress, Espresso, Moka

## Pricing

| Tier | Calls/day | Price |
|------|-----------|-------|
| Free | 100 | $0 |
| Dev | 10,000 | $9/mo |
| Pro | 100,000 | $29/mo |

## Deploy

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port $PORT
```
