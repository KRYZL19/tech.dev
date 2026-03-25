# AMMODEX — Ballistic Properties API

*The math for muzzle energy, penetration, and terminal ballistics. Without the Wikipedia rabbit hole.*

## Hook
Every ammo manufacturer has different specs for the same caliber. AMMODEX gives developers and re-loaders instant access to NIST-standard ballistic data — grain weights, velocities, energies, gel test simulations — via one clean API.

## Use it

```bash
# Get full ballistic data for 5.56 NATO
curl https://api.ammodex.io/v1/ammo/556_nato_62gr

# Calculate energy at custom velocity
curl "https://api.ammodex.io/v1/energy-calc?caliber_id=308_win_168gr&velocity_fps=2700"

# Search by caliber
curl "https://api.ammodex.io/v1/search?q=9mm"

# Ballistic gel simulation
curl -X POST https://api.ammodex.io/v1/ballistics/gel-test \
  -H "Content-Type: application/json" \
  -d '{"caliber_id":"223_rem_55gr","velocity_fps":3100}'
```

## Example response

```json
{
  "name": "5.56x45mm NATO (62gr FMJ)",
  "type": "rifle",
  "caliber": "5.56x45mm NATO",
  "grains": 62,
  "muzzle_velocity_fps": 3100,
  "muzzle_energy_ftlbs": 1324,
  "penetration_in_gel": 12,
  "expansion_mm": 8,
  "pressure_nato_psi": 58000
}
```

## What it does

- **Ballistic data** — muzzle velocity, energy, pressure, penetration for 14+ common calibers
- **Energy calculator** — override velocity or grain to model handloads
- **Gel test simulation** — penetration and expansion based on velocity delta
- **NATO compliance** — pressure data for military-spec comparison
- **Caliber search** — find ammunition by name or caliber string

## Pricing

| Tier | Calls/day | Price |
|------|-----------|-------|
| Free | 100 | $0 |
| Dev | 10,000 | $19/mo |
| Pro | 100,000 | $79/mo |

## Deploy

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Render: `render.yaml` included. Railway: `railway.toml` included.
