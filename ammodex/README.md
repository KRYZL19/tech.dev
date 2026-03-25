# AMMODEX API

**"Every reloader I know has a spreadsheet with powder data from 6 different PDF manuals. This shouldn't be a spreadsheet."**

AMMODEX is a FastAPI-powered ammunition database and reloading reference API. Get muzzle velocities, ballistic coefficients, powder load data, and reloading calculations — all in one place.

## Features

- **Ammunition Search** — Search by caliber, get bullet weights, types, and muzzle velocities
- **Ballistic Data** — G1 ballistic coefficients for hundreds of loads
- **Bullet Database** — BC values, weights, and styles by caliber
- **Powder Reference** — Max/min loads and burn rate indices for popular powders
- **Reload Calculator** — Get starting loads, max loads, and velocity estimates

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/ammo/search?q={caliber}` | Search ammo by caliber |
| GET | `/api/v1/ammo/{caliber}/{weight}` | Get specific ammo details |
| GET | `/api/v1/bullet/{caliber}` | List bullets with BC values |
| GET | `/api/v1/powder/{powder_name}` | Get powder data |
| POST | `/api/v1/reload/calculate` | Calculate loads for caliber/bullet/powder combo |

## Example Requests

```bash
# Search for 9mm ammunition
curl "http://localhost:8000/api/v1/ammo/search?q=9mm"

# Get specific ammo details
curl "http://localhost:8000/api/v1/ammo/9mm/124"

# Get bullets for .223 Rem
curl "http://localhost:8000/api/v1/bullet/.223%20Rem"

# Get powder data for Varget
curl "http://localhost:8000/api/v1/powder/Varget"

# Calculate reloading charges
curl -X POST "http://localhost:8000/api/v1/reload/calculate" \
  -H "Content-Type: application/json" \
  -d '{"caliber": "9mm", "bullet_weight": 124, "powder_type": "Bullseye"}'
```

## Pricing

| Tier | Price | Daily Calls |
|------|-------|-------------|
| **Free** | $0 | 100 |
| **Dev** | $19/month | 5,000 |
| **Pro** | $59/month | Unlimited |

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

# API docs available at http://localhost:8000/docs
```

## Deploy

### Render
```bash
render.yaml included for Render.com deployment
```

### Railway
```bash
railway.toml included for Railway.app deployment
```

## Supported Calibers

9mm, .223 Rem, .308 Win, .45 ACP, .300 Blackout, .38 Spl, .357 Mag, .30-06, 5.56 NATO, .22 LR, .40 S&W, 12ga, 20ga, .270 Win, .243 Win, 6.5 Creedmoor, .30-30, .44 Mag, .380 ACP, .38 Super

## Supported Powders

Bullseye, Unique, HP-38, CFE Pistol, 4227, Varget, CFE 223, H335, IMR 4895, AA2230

## Disclaimer

Load data provided is for reference only. Always verify with manufacturer-published data and start at the lowest listed charge before working up.
