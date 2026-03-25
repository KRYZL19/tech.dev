# NEIGHBORHOODDB

**Demographics & Real Estate Comp Database**

Average days on market, price per sqft trend, median rent — by neighborhood, updated monthly.

## Endpoints

### GET /api/v1/demographics/{zipcode}
Returns demographic data for a zipcode.

```json
{
  "zipcode": "78701",
  "population": 28000,
  "median_age": 35.0,
  "median_income": 145000,
  "housing_ownership_rate": 0.38,
  "school_rating_out_of_10": 7.8,
  "crime_index": 35.0
}
```

### GET /api/v1/comps/{zipcode}
Returns real estate comps data for a zipcode.

```json
{
  "zipcode": "78701",
  "median_home_price": 620000,
  "median_rent_monthly": 2800,
  "price_per_sqft": 480,
  "days_on_market_avg": 35,
  "inventory_months": 2.5,
  "year_over_year_change_pct": 8.5
}
```

### GET /api/v1/trend/{zipcode}?years={n}
Returns historical price trend and appreciation data.

```json
{
  "zipcode": "78701",
  "years_requested": 5,
  "historical_data": [
    {"year": 2020, "median_price": 420000, "appreciation_rate": 5.2},
    ...
  ],
  "appreciation_rate_avg": 7.8,
  "rental_yield": 5.4
}
```

### POST /api/v1/investment/score
Calculates investment metrics for a property.

**Request:**
```json
{
  "zipcode": "78701",
  "purchase_price": 500000,
  "down_payment_pct": 20
}
```

**Response:**
```json
{
  "zipcode": "78701",
  "purchase_price": 500000,
  "down_payment_pct": 20,
  "cap_rate": 5.8,
  "cash_on_cash_return": 8.2,
  "break_even_rent": 2450,
  "vacancy_rate_assumption": 5.5
}
```

## Coverage

Data for 100 zip codes across major metros:
- NYC (New York)
- LA (Los Angeles)
- Chicago
- Houston
- Phoenix
- Austin
- Denver
- Seattle
- Miami
- Atlanta

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Server runs at `http://localhost:8000`

## API Docs

Visit `http://localhost:8000/docs` for interactive Swagger UI.
