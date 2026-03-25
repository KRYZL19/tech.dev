# TIREMATCH API

**"245/45R18 on a 1998 Honda Civic will rub. One API call tells you before you buy."**

FastAPI backend for vehicle tire fitment and compatibility checking. Know if a tire or wheel fits before you buy — no more rubbing, no more guessing.

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/vehicle/{year}/{make}/{model}` | Factory tire sizes and wheel specs |
| `POST` | `/api/v1/tire/compare` | Compare two tire sizes |
| `POST` | `/api/v1/wheel/fitment` | Check wheel size + offset fitment |
| `GET` | `/api/v1/size/{width}/{aspect}R{rim}` | Parse a tire size string |

## Quick Start

```bash
cd tirematch
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

## Examples

### Parse a tire size
```
GET /api/v1/size/245/45R18
```
```json
{
  "raw": "245/45R18",
  "width_mm": 245,
  "aspect_ratio": 45,
  "rim_diameter": 18,
  "diameter_inches": 26.656,
  "sidewall_inches": 4.331,
  "circumference_inches": 83.744,
  "revolutions_per_mile": 756
}
```

### Compare two tires
```
POST /api/v1/tire/compare
{
  "tire1_size": "205/55R16",
  "tire2_size": "245/45R18"
}
```
```json
{
  "tire1_parsed": {"width_mm": 205, "aspect_ratio": 55, "rim_diameter": 16, "diameter_inches": 24.882},
  "tire2_parsed": {"width_mm": 245, "aspect_ratio": 45, "rim_diameter": 18, "diameter_inches": 26.656},
  "diameter_diff_pct": 7.13,
  "will_fit": false,
  "speedo_diff_mph": 4.28,
  "verdict": "Outside factory tolerance — may rub or affect handling."
}
```

### Check wheel fitment
```
POST /api/v1/wheel/fitment
{
  "vehicle_id": "honda_civic_2016",
  "wheel_size": 18,
  "offset_mm": 35
}
```
```json
{
  "vehicle_id": "honda_civic_2016",
  "wheel_size": 18,
  "offset_mm": 35,
  "fitment_verdict": "fits",
  "clearance_risk": "none",
  "spacer_needed_mm": 0.0,
  "warnings": ["Non-factory rim size 18\" — verify brake caliper clearance."]
}
```

### Get vehicle info
```
GET /api/v1/vehicle/2016/honda/civic
```

## Bundled Vehicles (20 total)

- Toyota Camry (2018–2024)
- Honda Civic (2016–2024)
- Ford F-150 (2018–2024)
- Chevrolet Silverado (2019–2024)
- BMW 3-series (2017–2024)
- Tesla Model 3 (2017–2024)
- Jeep Wrangler (2018–2024)
- Subaru Outback (2019–2024)
- Ram 1500 (2019–2024)
- Toyota RAV4 (2019–2024)

Each vehicle includes: factory tire sizes, bolt pattern, center bore, offset range, lug thread size.

## Pricing

| Tier | Requests | Price |
|------|----------|-------|
| Free | 100/day | $0 |
| Dev | Unlimited | $14/mo |
| Pro | Unlimited + priority | $39/mo |

---

## Project Structure

```
tirematch/
├── main.py              # FastAPI app entry point
├── requirements.txt     # Dependencies
├── README.md
├── data/
│   └── vehicle_data.py  # Bundled vehicle database
├── routes/
│   ├── fitment.py        # Vehicle + wheel fitment routes
│   ├── sizing.py         # Tire size parsing route
│   └── sizing_utils.py   # Shared tire math utilities
└── models/
    └── schemas.py        # Pydantic request/response models
```

## Tire Size Format

All tire sizes use the standard P-Metric format:

```
WIDTH/ASPECT RIM  or  WIDTH/ASPECTRIM
245/45R18         or  245/45-18
^^^ ^^^   ^^
 |   |     └─ rim diameter in inches
 |   └─────── aspect ratio (%)
 └─────────── width in mm
```

## Fitment Logic

- **Tire compare**: Industry-standard 3% diameter difference threshold for "will_fit"
- **Wheel offset**: Checks if offset falls within vehicle's documented offset range (±adjustment for spacer)
- **Rubbing risk**: Assessed based on offset deviation from factory range

> ⚠️ These are guidelines. Always verify with a professional installer for critical applications.
