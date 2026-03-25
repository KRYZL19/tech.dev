# SAWMILL — Lumber Cut Optimizer API

> *"12 boards, cut list, yield 94%, waste $23. This is the math."*

SAWMILL is a FastAPI service that optimizes lumber cutting to maximize yield and minimize waste.

## Hook

```
12 boards, cut list, yield 94%, waste $23. This is the math.
```

Feed it your boards and your cut list — it tells you exactly how to cut, what you'll waste, and what it'll cost.

## Endpoints

### `POST /api/v1/optimize/cutlist`
Optimize cutting required pieces from available boards.

**Request:**
```json
{
  "available_boards": [
    {"board_type": "2x4", "length_ft": 8, "price_per_bf": 1.50, "wood_type": "pine"}
  ],
  "required_cuts": [
    {"length_in": 36, "width_in": 3.5, "quantity": 10},
    {"length_in": 18, "width_in": 3.5, "quantity": 6}
  ],
  "kerf_inches": 0.125
}
```

**Response:**
```json
{
  "yield_percent": 94.12,
  "waste_boards": [...],
  "total_cost": 23.45,
  "cuts_placed": 16,
  "cuts_requested": 16
}
```

### `POST /api/v1/yield/estimate`
Quick yield estimate without full optimization.

**Request:**
```json
{
  "board_sqft": 100.0,
  "cuts_sqft": 87.5,
  "kerf_inches": 0.125,
  "board_count": 10
}
```

**Response:**
```json
{
  "theoretical_yield_pct": 87.5,
  "realistic_yield_pct": 83.2
}
```

### `GET /api/v1/board/standard-sizes`
Returns nominal vs actual dimensions for common lumber sizes.

**Response:**
```json
{
  "sizes": [
    {"size": "1x2",  "nominal_inches": "1×2",  "actual_inches": "0.75×1.5",   "board_feet_per_ft": 0.0833},
    {"size": "2x4",  "nominal_inches": "2×4",  "actual_inches": "1.5×3.5",   "board_feet_per_ft": 0.3333},
    ...
  ]
}
```

### `POST /api/v1/price/estimate`
Estimate material cost, labor hours, and total for a cut list.

**Request:**
```json
{
  "cuts": [
    {"length_in": 36, "width_in": 3.5, "quantity": 10},
    {"length_in": 18, "width_in": 3.5, "quantity": 6}
  ],
  "wood_type": "pine",
  "board_size": "2x4"
}
```

**Response:**
```json
{
  "material_cost": 18.50,
  "labor_hours": 1.5,
  "total_estimate": 86.00,
  "wood_type": "pine",
  "board_size": "2x4",
  "total_cut_sqft": 12.5
}
```

## Quick Start

```bash
cd sawmill
pip install -r requirements.txt
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 8765
```

## API Docs

Once running:
- Swagger UI: `http://localhost:8765/docs`
- ReDoc: `http://localhost:8765/redoc`

## Bundled Data

| Wood Type | Price/Board Foot |
|-----------|-----------------|
| Pine      | $1.50           |
| Spruce    | $1.60           |
| Cedar     | $4.00           |
| Oak       | $4.50           |
| Maple     | $3.50           |
| Cherry    | $8.00           |
| Walnut    | $10.00          |

**Default kerf:** 0.125" (1/8" saw blade)

## Architecture

```
sawmill/
├── main.py              # FastAPI app + CORS
├── requirements.txt
├── README.md
├── models/
│   └── schemas.py       # Pydantic request/response models
├── routes/
│   ├── cut.py           # POST /optimize/cutlist
│   ├── yield.py         # POST /yield/estimate
│   ├── board.py         # GET /board/standard-sizes
│   └── price.py         # POST /price/estimate
└── utils/
    ├── dimensions.py    # Lumber dimensions + wood pricing
    └── optimizer.py     # First Fit Decreasing cut optimizer
```

## Algorithm

SAWMILL uses **First Fit Decreasing** bin packing:
1. Sort all required cuts largest-first by area
2. Assign each cut to the first board with enough remaining length
3. Track waste per board and total material cost

For more accurate results with complex cuts, boards are evaluated in order of available length.
