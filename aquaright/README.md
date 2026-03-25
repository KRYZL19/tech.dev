# AQUARIGHT API - Aquarium Water Chemistry Manager

**"The nitrogen cycle takes 2-6 weeks. Most beginners give up on day 3 because they don't understand why their ammonia keeps spiking."**

AQUARIGHT helps aquarium hobbyists manage water chemistry, understand the nitrogen cycle, and maintain healthy tanks.

## The Problem

New aquarium owners often give up in the first week because:
- Ammonia spikes look terrifying
- They don't know the nitrogen cycle exists
- They add fish too early and wonder why they die
- They can't tell if their tank is "cycled"

## The Solution

AQUARIGHT explains what's actually happening biochemically and guides users through the cycle.

## Pricing

| Tier | Calls/Day | Price |
|------|-----------|-------|
| Free | 100 | $0 |
| Dev | Unlimited | $9/month |
| Pro | Unlimited + Priority | $29/month |

## Installation

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`

## API Endpoints

### GET `/api/v1/fish/{species}`
Get chemistry tolerances for a fish species.

**Species:** betta, neon_tetra, goldfish, angelfish, corydoras, pleco, guppy, molly, platy, cherry_barb, harlequin_rasbora, white_cloud, dwarf_gourami, oscar, ram_cichlid

```json
{
  "species": "betta",
  "common_name": "Betta",
  "temp_range": {"min": 76.0, "max": 82.0},
  "ph_range": {"min": 6.5, "max": 7.5},
  "ammonia_tolerance": 0.25,
  "nitrite_tolerance": 0.25,
  "nitrate_tolerance": 20.0,
  "size_inches": 2.5,
  "aggression": "semi-aggressive",
  "min_tank_gallons": 5
}
```

### POST `/api/v1/cycle/status`
Analyze nitrogen cycle status based on water parameters.

```json
{
  "ammonia_ppm": 2.0,
  "nitrite_ppm": 1.5,
  "nitrate_ppm": 10.0,
  "day_number": 10
}
```

**Response:**
```json
{
  "cycle_phase": "Nitrite Spike",
  "phase_number": 2,
  "biochemistry": "Ammonia is converting to nitrite...",
  "recommendations": ["Keep water well-aerated...", "Do NOT add fish..."],
  "is_cycled": false
}
```

### POST `/api/v1/dose/calculate`
Calculate baking soda needed to raise KH (carbonate hardness).

```json
{
  "tank_gallons": 20,
  "current_kh": 3,
  "target_kh": 6
}
```

**Response:**
```json
{
  "baking_soda_grams": 3.37,
  "baking_soda_tsp": 0.84,
  "current_kh": 3,
  "target_kh": 6,
  "kh_increase": 3
}
```

### POST `/api/v1/stocking/max`
Calculate maximum stocking level for a tank.

```json
{
  "tank_gallons": 29,
  "filter_gph": 150,
  "fish_species": ["neon_tetra", "corydoras"]
}
```

**Response:**
```json
{
  "stocking_percentage": 35.2,
  "bioload_score": 4.5,
  "max_bioload": 32.0,
  "current_bioload": 4.5,
  "warnings": [],
  "recommended_max": 14
}
```

## Fish Species Database

| Species Key | Common Name | Temp (°F) | pH | Ammonia Tol | Size |
|-------------|-------------|-----------|-----|-------------|------|
| betta | Betta | 76-82 | 6.5-7.5 | 0.25 | 2.5" |
| neon_tetra | Neon Tetra | 70-81 | 6.0-7.0 | 0.25 | 1.5" |
| goldfish | Goldfish | 65-72 | 7.0-8.4 | 0.5 | 8" |
| angelfish | Angelfish | 76-84 | 6.0-7.5 | 0.25 | 6" |
| corydoras | Corydoras Catfish | 72-79 | 6.0-8.0 | 0.25 | 2.5" |
| pleco | Common Pleco | 72-86 | 6.5-7.5 | 0.5 | 18" |
| guppy | Guppy | 72-82 | 6.8-7.8 | 0.5 | 2" |
| molly | Molly | 72-82 | 7.5-8.5 | 0.5 | 4" |
| platy | Platy | 70-80 | 7.0-8.2 | 0.5 | 2.5" |
| cherry_barb | Cherry Barb | 73-81 | 6.0-8.0 | 0.25 | 2" |
| harlequin_rasbora | Harlequin Rasbora | 72-81 | 6.0-7.5 | 0.25 | 2" |
| white_cloud | White Cloud Mountain Minnow | 60-72 | 6.0-8.0 | 0.5 | 1.5" |
| dwarf_gourami | Dwarf Gourami | 72-82 | 6.0-7.5 | 0.25 | 3.5" |
| oscar | Oscar | 74-81 | 6.0-8.0 | 0.5 | 14" |
| ram_cichlid | Ram Cichlid | 78-85 | 6.0-7.5 | 0.25 | 3" |

## The Nitrogen Cycle (Quick Reference)

```
Fish Waste → Ammonia (NH3) → Nitrite (NO2) → Nitrate (NO3)
                ↓                ↓                ↓
           [Nitrosomonas]   [Nitrobacter]      (harmless)
              bacteria         bacteria
```

| Phase | Duration | Ammonia | Nitrite | Action |
|-------|----------|---------|---------|--------|
| 1: Ammonia Spike | Days 1-14 | HIGH | low | Wait, don't add fish |
| 2: Nitrite Spike | Days 7-21 | low | HIGH | Wait, extra aeration |
| 3: Completion | Days 14-42 | 0 | 0 | Water change, add fish slowly |
| 4: Cycled | Day 42+ | 0 | 0 | Maintain weekly schedule |

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Run tests (if any)
pytest
```

## Docs

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License

MIT License - Free for personal and commercial use.
