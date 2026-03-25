# GARDENPLOT - Vegetable Garden Planner API

**"Your shade pattern means these 6 vegetables will actually work. Here's what."**

A FastAPI-based vegetable garden planning API that helps you choose what to grow based on your USDA zone, sunlight hours, and available space.

## Features

- **Personalized vegetable recommendations** based on zone, sunlight, and space
- **Crop rotation planning** to prevent disease and maintain soil health
- **Companion planting checks** with compatibility scores
- **Frost date lookup** by zipcode
- **Detailed plant information** for 30 vegetables

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

# Or run directly
python main.py
```

API available at `http://localhost:8000`  
Documentation at `http://localhost:8000/docs`

## API Endpoints

### POST `/api/v1/planner/what-grows`
Get personalized vegetable recommendations.

```json
{
  "zone": "6",
  "sunlight_hours": 4,
  "space_sqft": 100,
  "goals": ["shade_tolerant", "quick_harvest"]
}
```

**Response:**
```json
{
  "vegetables": ["lettuce", "spinach", "radish", "beet", "chard", "kale"],
  "spacing_recommendations": [...],
  "expected_yield": [...],
  "shade_insight": "Your shade pattern means these 6 vegetables will actually work..."
}
```

### GET `/api/v1/plant/{name}`
Get detailed plant information.

```json
{
  "name": "Tomato",
  "days_to_maturity": 75,
  "sun_hours_min": 6,
  "spacing_inches": 24,
  "frost_tolerance": "none",
  "companions": ["basil", "carrot", "parsley"],
  "enemies": ["cabbage", "fennel", "potato"],
  "harvest_window_days": 30
}
```

### POST `/api/v1/rotation/plan`
Create a 3-season crop rotation plan.

```json
{
  "plot_layout": [
    {"section_id": "A1", "current_plant": "tomato", "plant_family": "Solanaceae"},
    {"section_id": "A2", "current_plant": "pepper", "plant_family": "Solanaceae"}
  ]
}
```

### POST `/api/v1/companion/check`
Check companion planting compatibility.

```json
{
  "plant_a": "tomato",
  "plant_b": "basil"
}
```

**Response:**
```json
{
  "plant_a": "Tomato",
  "plant_b": "Basil",
  "compatibility_score": 95,
  "reason": "Tomato and Basil are excellent companions! They mutually benefit each other.",
  "tips": [...]
}
```

### GET `/api/v1/frost/{zipcode}`
Get frost dates for your area.

```json
{
  "zipcode": "10001",
  "zone": "6",
  "last_frost_spring": "Apr 15",
  "first_frost_fall": "Oct 15",
  "growing_days": 183
}
```

## Bundled Data

- **30 vegetables** with full growing data
- **6 plant families**: Brassicaceae, Solanaceae, Cucurbitaceae, Fabaceae, Apiaceae, Amaryllidaceae
- **USDA zones 3-11** with frost date estimates
- **Companion matrix** with friends and foes for each plant

## Pricing

| Tier | Price | Requests/Day |
|------|-------|--------------|
| Free | $0 | 100 |
| Dev | $9/mo | 10,000 |
| Pro | $29/mo | 100,000 |

Use API key in header: `X-API-Key: your_key`  
Dev keys: prefix with `dev_`  
Pro keys: prefix with `pro_`

## Project Structure

```
gardenplot/
├── main.py              # FastAPI application
├── requirements.txt     # Dependencies
├── data/
│   └── plant_data.py   # Plant database, families, companion matrix
├── routes/
│   ├── planner.py      # /what-grows endpoint
│   └── rotation.py     # /rotation, /companion, /frost endpoints
├── models/
│   └── schemas.py      # Pydantic models
└── README.md
```

## Tech Stack

- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## License

MIT
