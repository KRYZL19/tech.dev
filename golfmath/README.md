# GOLFMATH API

> **Your handicap index doesn't account for wind. The USGA formula is 30 years old. Here's something that actually adjusts for conditions.**

A FastAPI backend for golf handicap calculations and course difficulty analysis — with weather-adjusted handicaps that the USGA formula ignores.

## Stack

- **FastAPI** — async Python web framework
- **Pydantic** — request/response validation
- **uvicorn** — ASGI server

## Quick Start

```bash
pip install -r requirements.txt
python main.py
# or: uvicorn main:app --reload
```

API runs at `http://localhost:8000`. Docs at `http://localhost:8000/docs`.

## Endpoints

### `POST /api/v1/handicap/calculate`
Calculate handicap index from recent rounds.

```json
{
  "scores": [82, 85, 79, 88],
  "course_ratings": [72.5, 73.0, 71.8, 74.2],
  "slope_ratings": [135, 140, 130, 145]
}
```

### `GET /api/v1/course/{course_name}`
Get full course data (par, rating, slope, hole-by-hole).

```
GET /api/v1/course/augusta-national
GET /api/v1/course/pebble-beach
GET /api/v1/course/st-andrews
GET /api/v1/course/torrey-pines
GET /api/v1/course/bethpage-black
GET /api/v1/course/whistling-straits
GET /api/v1/course/kiawah-island
GET /api/v1/course/pinehurst-no2
```

### `POST /api/v1/round/scorecard`
Analyze a scorecard with full stats breakdown.

```json
{
  "course_id": "augusta-national",
  "strokes_per_hole": [4,5,4,3,4,3,4,5,4,4,4,3,5,4,5,3,4,4],
  "putts_per_hole": [2,2,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2],
  "fairways_hit": [true,true,false,true,true,true,false,false,true,true,false,true,false,true,false,true,true,false],
  "gir": [true,true,true,true,true,true,false,false,true,true,true,true,false,true,false,true,true,false]
}
```

### `POST /api/v1/weather/adjust`
Weather-adjust your handicap index.

```json
{
  "handicap_index": 14.5,
  "temp_f": 52,
  "wind_mph": 20,
  "elevation_ft": 4500
}
```

Adjustments:
- **Wind > 15mph**: adds strokes (playing into wind is hard)
- **Temp < 65°F**: adds strokes (ball doesn't travel as far)
- **Elevation > 1000ft**: subtracts strokes (ball flies longer in thin air)

## Pricing

| Tier | Calls/Day | Price |
|------|-----------|-------|
| Free | 50 | $0 |
| Dev | 1000 | $14/mo |
| Pro | Unlimited | $39/mo |

## Bundled Courses

8 championship courses with full 18-hole data:

1. **Augusta National** — Augusta, GA (par 72, rating 76.2, slope 148)
2. **Pebble Beach Golf Links** — Pebble Beach, CA (par 72, rating 75.5, slope 145)
3. **St Andrews Old Course** — St Andrews, Scotland (par 72, rating 76.2, slope 143)
4. **Torrey Pines South** — La Jolla, CA (par 72, rating 75.6, slope 142)
5. **Bethpage Black** — Farmingdale, NY (par 71, rating 75.7, slope 147)
6. **Whistling Straits** — Kohler, WI (par 72, rating 76.7, slope 151)
7. **Kiawah Island Ocean** — Kiawah Island, SC (par 72, rating 76.1, slope 146)
8. **Pinehurst No. 2** — Pinehurst, NC (par 70, rating 75.6, slope 141)

## Project Structure

```
golfmath/
├── main.py              # FastAPI app + routes
├── requirements.txt
├── README.md
├── data/
│   └── course_data.py   # 8 sample courses
├── models/
│   └── schemas.py       # Pydantic models
└── routes/
    ├── handicap.py      # Handicap calculation
    ├── course.py        # Course lookup + scorecard
    └── weather.py       # Weather adjustment
```
