# COFFEEBREW — Coffee Extraction Calculator API

> **"21g at 200°F, 2:30, 1.42% TDS. Your refractometer says TDS is off. Here's why."**

A precision coffee brewing API that calculates extraction metrics, optimizes dosing parameters, and provides bean/method intelligence for specialty coffee.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

## Endpoints

### POST `/api/v1/extraction/calculate`
Calculate extraction metrics from brew parameters.

**Request:**
```json
{
  "dose_g": 21.0,
  "water_ml": 360.0,
  "brew_time_seconds": 150,
  "temp_f": 200,
  "tds_percent": 1.42
}
```

**Response:**
```json
{
  "extraction_percent": 24.34,
  "strength_ratio": 58.33,
  "yield_percent": 24.34,
  "over_extracted_bool": true,
  "under_extracted_bool": false
}
```

### POST `/api/v1/dose/optimize`
Optimize dose parameters for a target extraction and TDS.

**Request:**
```json
{
  "brew_method": "pourover",
  "target_extraction_pct": 20.0,
  "tds_target_percent": 1.35
}
```

**Response:**
```json
{
  "dose_g": 22.0,
  "water_ml": 340.0,
  "temp_f": 200.0,
  "grind_size_description": "Medium-fine grind (sea salt to table salt)"
}
```

### GET `/api/v1/beans/{origin}`
Get bean profile by origin ID (e.g., `ethiopia_yirgacheffe`, `kenya_aa`, `panama_geisha`).

**Response:**
```json
{
  "origin": "Ethiopia Yirgacheffe",
  "roast_level": "Light",
  "altitude_m": 1950,
  "process": "Washed",
  "flavor_notes": ["Jasmine", "Bergamot", "Lemon", "Blueberry", "Tea-like"],
  "ideal_temp_range": "195-205°F",
  "ideal_extraction_range": "18-21%"
}
```

### POST `/api/v1/tds/calibrate`
Calibrate TDS reading based on brew method.

**Request:**
```json
{
  "tds_reading": 1.42,
  "coffee_type": "pourover"
}
```

**Response:**
```json
{
  "calibrated_tds": 1.349,
  "measurement_notes": "Reading adjusted for pourover extraction characteristics. Calibration factor applied: 0.95",
  "is_stale_warning": false
}
```

### GET `/api/v1/methods/{method}`
Get brew method parameters (espresso, pourover, aeropress, french_press, cold_brew).

## Included Data

- **30 Bean Origins**: Ethiopia Yirgacheffe, Colombia Huila, Guatemala Antigua, Kenya AA, Brazil Cerrado, Panama Geisha, and more
- **6 Brew Methods**: Espresso, Pour Over, AeroPress, French Press, Cold Brew

## Extraction Reference

| Extraction % | Quality | Characteristics |
|-------------|---------|-----------------|
| < 18% | Under-extracted | Sour, weak, lacking body |
| 18-21% | Optimal | Sweet, balanced, complex |
| > 21% | Over-extracted | Bitter, harsh, hollow |

## TDS Calibration

Refractometer readings vary by brew method due to different extraction profiles:

| Method | Calibration Factor |
|--------|-------------------|
| Espresso | 1.00 |
| Pour Over | 0.95 |
| AeroPress | 0.97 |
| French Press | 0.92 |
| Cold Brew | 0.88 |
