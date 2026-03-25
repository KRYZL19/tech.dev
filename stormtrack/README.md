# STORMTRACK — Hurricane & Historical Storm Database API

**Hook:** *"What's the hurricane history for this coastal address? 1950-2025. One query."*

A FastAPI-based REST API bundling 10 major Atlantic hurricanes (1992–2024) with full track data, impact analysis, return-period estimates, and property risk summaries.

## Quick Start

```bash
cd stormtrack
pip install -r requirements.txt
python main.py
```

API runs at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## Bundled Storms

| Storm       | Year | Category |
|-------------|------|----------|
| Andrew      | 1992 | 5        |
| Katrina     | 2005 | 5        |
| Sandy       | 2012 | 3        |
| Ike         | 2008 | 2        |
| Irma        | 2017 | 5        |
| Harvey      | 2017 | 4        |
| Maria       | 2017 | 5        |
| Michael     | 2018 | 5        |
| Laura       | 2020 | 4        |
| Ian         | 2022 | 4        |
| Helene      | 2024 | 4        |

Each storm includes 40–70 track points (lat/lon/date/max_wind_kt).

## Endpoints

### `GET /api/v1/storms/search`
Find storms within radius of a coordinate.

```
/api/v1/storms/search?lat=25.76&lon=-80.19&radius_mi=100&year_start=1992&year_end=2025
```

### `GET /api/v1/storm/{storm_id}`
Full storm details: name, year, category, track points, pressure, surge.

```
/api/v1/storm/IRMA_2017
```

### `GET /api/v1/storm/{storm_id}/impact`
Storm impact at a specific location.

```
/api/v1/storm/KATRINA_2005/impact?lat=30.0&lon=-89.5
```

### `GET /api/v1/return-period`
Return-period estimate for major hurricane categories.

```
/api/v1/return-period?lat=25.76&lon=-80.19
```

### `POST /api/v1/risk/summary`
Damage estimates for a property.

```json
POST /api/v1/risk/summary
{
  "lat": 25.76,
  "lon": -80.19,
  "property_value_usd": 500000
}
```

## Run Tests

```bash
cd stormtrack
pip install -r requirements.txt
python -c "
from routes.storms import router as s; from routes.analysis import router as a
from data.storm_data import get_all_storms, get_storm_by_id
from main import app

# Sanity checks
assert len(get_all_storms()) == 10
assert get_storm_by_id('KATRINA_2005')['name'] == 'Katrina'
assert len(get_storm_by_id('ANDREW_1992')['track_points']) >= 40
print('All checks passed ✓')
"
```

## Deployment

```bash
pip install -r requirements.txt
python main.py
# Or with gunicorn:
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:8000
```

## License

MIT
