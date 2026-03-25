# POOLCHEM 🏊 — Swimming Pool Water Balance API

> *FCI over 150ppm and your chlorine demand doubles overnight. Nobody explains the chemistry. This does.*

POOLCHEM is a REST API that calculates swimming pool water chemistry — Langelier Saturation Index (LSI), chlorine dosing with FCI-aware demand curves, pH adjustment, and breakpoint chlorination.

---

## Hook

**FCI (Free Chlorine Inefficiency)** occurs when Cyanuric Acid (CYA) exceeds 150ppm. At that threshold, chlorine's sanitizing power is so sequestered that demand effectively doubles overnight. Most pool apps ignore this. POOLCHEM doesn't.

---

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

---

## API Endpoints

### `POST /api/v1/balance/check`
Full water balance check with LSI and prioritized recommendations.

```json
{
  "pool_gallons": 15000,
  "chlorine_ppm": 0.8,
  "ph": 7.4,
  "alkalinity_ppm": 90,
  "temp_f": 82,
  "stabilizer_ppm": 60,
  "calcium_hardness_ppm": 300
}
```

Response includes `saturation_index`, `balance_status` (`balanced` | `corrosive` | `scale_forming` | `severe_*`), and an array of prioritized `recommendations[]` — with **FCI alerts** when CYA > 150ppm.

---

### `GET /api/v1/balance/saturation`
LSI calculation from individual parameters.

```
/api/v1/balance/saturation?ph=7.4&alkalinity=90&calcium_hardness=300&temp=82&cya=60
```

---

### `POST /api/v1/dose/chlorine`
Calculate ounces of chlorine product needed to reach target ppm.

```json
{
  "pool_gallons": 15000,
  "current_chlorine_ppm": 0.5,
  "target_ppm": 2.0,
  "chlorine_type": "liquid"
}
```

Also see `/api/v1/dose/chlorine-adjusted` — accepts `cya_ppm` for FCI-aware demand adjustment.

**Chlorine types:** `liquid`, `di-chlor`, `tri-chlor`, `cal-hypo`, `gas`

---

### `POST /api/v1/dose/ph`
Calculate pH adjustment chemicals.

```json
{
  "pool_gallons": 15000,
  "current_ph": 7.8,
  "target_ph": 7.4
}
```

Returns `sodium_carbonate_oz` (to raise pH) or `muriatic_acid_oz` (to lower pH).

**Rates:**
- Soda ash: ~6 oz per 10k gallons per 0.2 pH rise
- Muriatic acid (32%): ~16 oz per 10k gallons per 0.2 pH drop

---

### `POST /api/v1/convert/chloramine`
Breakpoint chlorination calculator.

```json
{
  "combined_chloramine_ppm": 0.5
}
```

Returns `breakpoint_dose_ppm` (10x combined chlorine) and `volume_to_add_oz`.

---

## Pricing

| Tier | Price | Requests | Features |
|------|-------|----------|----------|
| **Free** | $0 | 100/day | Full LSI, chlorine, pH, breakpoint |
| **Dev** | $9/mo | Unlimited | API key auth, no rate limits |
| **Pro** | $29/mo | Unlimited | FCI webhooks, bulk dosing, commercial |

**Free tier** uses IP-based rate limiting. No signup required.

**Dev/Pro** use `X-API-Key` header: `pk_dev_...` or `pk_pro_...`

---

## Chemistry Reference

### Langelier Saturation Index (LSI)
```
SI = pH + TF + AF + CF - HF
```
- **pH**: Current pH
- **TF**: Temperature Factor (from water temp)
- **AF**: Alkalinity Factor (Alkalinity ÷ 100 × 0.08)
- **CF**: Calcium Factor (Calcium Hardness ÷ 100 × 0.1)
- **HF**: Hardness Factor (~12.1)

| SI Range | Status |
|----------|--------|
| -0.3 to +0.3 | **Balanced** ✅ |
| -0.3 to -1.0 | Corrosive ⚠️ |
| +0.3 to +1.0 | Scale Forming ⚠️ |
| < -1.0 | Severe Corrosive 🔴 |
| > +1.0 | Severe Scale Forming 🔴 |

### Chlorine Demand by CYA (FCI Effect)

| CYA (ppm) | Demand Multiplier | Note |
|-----------|------------------|------|
| 0–30 | 1.0× | Optimal |
| 30–50 | 1.2× | Slightly reduced |
| 50–80 | 1.5× | Moderate |
| 80–100 | 2.0× | Significant |
| 100–150 | 2.5× | Severe |
| **> 150** | **4.0×** | **FCI CRITICAL** |

### pH Adjustment

| Direction | Chemical | Rate per 10k gal / 0.2 pH |
|-----------|----------|--------------------------|
| Raise pH | Sodium Carbonate (Soda Ash) | 6 oz |
| Lower pH | Muriatic Acid (32%) | 16 oz |

### Recommended Ranges

| Parameter | Min | Max |
|-----------|-----|-----|
| pH | 7.2 | 7.6 |
| Free Chlorine | 1.0 ppm | 3.0 ppm |
| Alkalinity | 80 ppm | 120 ppm |
| Calcium Hardness | 200 ppm | 400 ppm |
| CYA (Stabilizer) | 30 ppm | 50 ppm |

---

## Project Structure

```
poolchem/
├── main.py              # FastAPI app + rate limiting
├── requirements.txt     # Dependencies
├── README.md            # This file
├── __init__.py
├── data/
│   └── pool_types.py    # Chemistry constants, demand curves, adjustment rates
├── models/
│   └── schemas.py       # Pydantic request/response models
└── routes/
    ├── balance.py       # LSI / saturation index endpoints
    └── dosing.py        # Chlorine, pH, breakpoint endpoints
```

---

## Rate Limits

- **Free**: 100 requests/day per IP (no API key needed)
- **Dev**: Unlimited (pass `X-API-Key: pk_dev_...`)
- **Pro**: Unlimited + webhooks (pass `X-API-Key: pk_pro_...`)

Rate limit headers included in every response:
- `X-RateLimit-Tier`
- `X-RateLimit-Remaining`
- `X-RateLimit-Limit`

---

*POOLCHEM — Water chemistry for people who'd rather trust math than guess.*
