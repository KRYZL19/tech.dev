# CLIMATEZ — Historical Weather & Climate API

> *"What's the frost date history for this zip code? 30-year normals. One query."*

CLIMATEZ provides instant access to 30-year climate normals and frost date data for major US cities. Built for farmers, gardeners, and developers who need reliable historical climate context.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API
python main.py
# Or: uvicorn main:app --reload

# API available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

## Endpoints

### GET `/api/v1/normals/{zipcode}`
Get 30-year climate normals (1991-2020) for a zip code.

```json
{
  "zipcode": "10001",
  "city": "New York",
  "state": "NY",
  "lat": 40.75,
  "lon": -73.99,
  "heating_dd": 4802,
  "cooling_dd": 1204,
  "growing_days": 220,
  "avg_precip_inches": 46.4,
  "avg_snow_inches": 29.8,
  "humidity_pct": 63
}
```

### GET `/api/v1/frost-dates/{zipcode}`
Get average frost dates and growing season length.

```json
{
  "zipcode": "10001",
  "city": "New York",
  "state": "NY",
  "avg_last_spring_frost": "Apr 15",
  "avg_first_fall_frost": "Oct 25",
  "growing_season_days": 193,
  "has_frost": true
}
```

### GET `/api/v1/precipitation/{zipcode}/annual`
Get monthly precipitation averages with wettest/driest months.

```json
{
  "zipcode": "10001",
  "city": "New York",
  "state": "NY",
  "annual_total_inches": 46.4,
  "monthly": [
    {"month": 1, "month_name": "Jan", "precip_inches": 3.4},
    ...
  ],
  "wettest_month": "Jul",
  "wettest_inches": 4.4,
  "driest_month": "Feb",
  "driest_inches": 3.2
}
```

### POST `/api/v1/growing-season`
Estimate growing season based on frost risk tolerance.

**Request:**
```json
{
  "zipcode": "10001",
  "first_kill_probability_pct": 50
}
```

- `10` = Early date (10% chance of frost kill, risky)
- `50` = Median date (50% chance)
- `90` = Late date (90% chance, safe for most growers)

**Response:**
```json
{
  "zipcode": "10001",
  "city": "New York",
  "state": "NY",
  "probability_pct": 50,
  "estimated_last_spring_frost": "Apr 15",
  "estimated_first_fall_frost": "Oct 25",
  "growing_season_days": 193,
  "frost_free_risk": "medium",
  "recommendation": "Standard growing season. Safe planting window around median frost dates..."
}
```

## Coverage

Includes 30-year climate normals (NOAA/NCDC 1991-2020) for 50 major US metropolitan areas:

| City | State | Zip |
|------|-------|-----|
| New York | NY | 10001 |
| Los Angeles | CA | 90001 |
| Chicago | IL | 60601 |
| Houston | TX | 77001 |
| Phoenix | AZ | 85001 |
| Philadelphia | PA | 19101 |
| San Antonio | TX | 78201 |
| San Diego | CA | 92101 |
| Dallas | TX | 75201 |
| San Jose | CA | 95101 |
| Austin | TX | 78701 |
| Jacksonville | FL | 32099 |
| San Francisco | CA | 94102 |
| Columbus | OH | 43201 |
| Indianapolis | IN | 46201 |
| Fort Worth | TX | 76101 |
| Charlotte | NC | 28201 |
| Seattle | WA | 98101 |
| Denver | CO | 80201 |
| Washington | DC | 20001 |
| Boston | MA | 02101 |
| Nashville | TN | 37201 |
| Baltimore | MD | 21201 |
| Oklahoma City | OK | 73101 |
| Las Vegas | NV | 89101 |
| Portland | OR | 97201 |
| Detroit | MI | 48201 |
| Memphis | TN | 38101 |
| Louisville | KY | 40201 |
| Milwaukee | WI | 53201 |
| Albuquerque | NM | 87101 |
| Tucson | AZ | 85701 |
| Fresno | CA | 93650 |
| Sacramento | CA | 94203 |
| Kansas City | MO | 64101 |
| Atlanta | GA | 30301 |
| Omaha | NE | 68101 |
| Raleigh | NC | 27601 |
| Miami | FL | 33101 |
| Cleveland | OH | 44101 |
| New Orleans | LA | 70112 |
| Tampa | FL | 33601 |
| St. Louis | MO | 63101 |
| Pittsburgh | PA | 15201 |
| Buffalo | NY | 14201 |
| Salt Lake City | UT | 84101 |
| Orlando | FL | 32801 |
| Minneapolis | MN | 55401 |

## Data Fields

### Degree Days
- **Heating Degree Days (heating_dd)**: Cumulative degrees below 65°F needed for heating
- **Cooling Degree Days (cooling_dd)**: Cumulative degrees above 65°F needed for cooling

### Precipitation
- Monthly values in inches
- Annual total is sum of monthly averages
- Wettest/driest months identified from monthly normals

### Frost Dates
- Average date of last spring frost (spring planting reference)
- Average date of first fall frost (fall growing reference)
- Growing season = days between average frost dates

## Use Cases

- **Farmers**: Plan planting/harvest based on frost risk tolerance
- **Gardeners**: Choose appropriate crops for local climate
- **Developers**: Build climate-aware applications
- **Researchers**: Quick access to baseline climate normals

## API Examples

```bash
# Get climate summary for Chicago
curl http://localhost:8000/api/v1/normals/60601

# Get frost dates for Denver (snowy climate)
curl http://localhost:8000/api/v1/frost-dates/80201

# Check precipitation for Miami (wet subtropics)
curl http://localhost:8000/api/v1/precipitation/33101/annual

# Conservative growing season estimate for Minneapolis
curl -X POST http://localhost:8000/api/v1/growing-season \
  -H "Content-Type: application/json" \
  -d '{"zipcode": "55401", "first_kill_probability_pct": 90}'
```

## License

Data sourced from NOAA/NCDC 30-year Climate Normals (1991-2020).
