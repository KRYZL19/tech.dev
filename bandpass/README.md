# BANDPASS — Audio EQ Room Correction API

**Room EQ Wizard is free but takes 30 minutes. This returns your EQ settings in one call.**

![BANDPASS](https://img.shields.io/badge/BANDPASS-v1.0.0-blue) ![Python](https://img.shields.io/badge/Python-3.9+-green) ![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-red)

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

API runs at `http://localhost:8000` — docs at `/docs`

## The Problem

Room EQ Wizard (REW) is free and excellent. But:
- Takes 30+ minutes to set up and measure
- Requires specific hardware (measurement mic, audio interface)
- Complex UI with steep learning curve
- Still need to manually interpret results and apply to your system

## The Solution

BANDPASS returns calibrated EQ settings based on your room parameters in a single API call. No measurement mic required.

## API Endpoints

### POST `/api/v1/eq/room`
Calculate room correction EQ settings.

```json
{
  "room_volume_cubic_ft": 1500,
  "listening_distance_ft": 8,
  "speaker_type": "bookshelf",
  "room_treatment_level": "partial"
}
```

**Response:**
```json
{
  "recommended_eq_settings": [
    {"frequency_hz": 40, "gain_db": 2.0, "q_factor": 3.5},
    {"frequency_hz": 63, "gain_db": 1.5, "q_factor": 2.0},
    ...
  ],
  "room_mode_predictions": [
    {"frequency_hz": 56.5, "mode_type": "axial", "severity": "severe", ...},
    ...
  ],
  "first_reflection_corrections": [...]
}
```

### GET `/api/v1/room/modes`
Calculate room mode frequencies for your room dimensions.

```
GET /api/v1/room/modes?length_ft=15&width_ft=12&height_ft=8
```

**Response:**
```json
[
  {"frequency_hz": 37.7, "mode_type": "axial", "dimensions": "(1,0,0)", "severity": "severe", "recommendation": "Deep bass trap..."},
  {"frequency_hz": 47.1, "mode_type": "axial", "dimensions": "(0,1,0)", "severity": "severe", ...},
  ...
]
```

### POST `/api/v1/eq/speaker-profile`
Get EQ settings for specific speakers.

```json
{
  "speaker_manufacturer": "Yamaha",
  "speaker_model": "HS8",
  "listening_distance_ft": 6
}
```

### GET `/api/v1/filters/common`
List common filter types with recommended use cases.

## Supported Speakers (15 Profiles)

| Manufacturer | Model | Type |
|--------------|-------|------|
| Yamaha | HS8, HS7 | Bookshelf |
| JBL | 308P MkII, 305P MkII | Bookshelf |
| Adam | A7X | Bookshelf |
| KRK | Rokit 8 G4 | Bookshelf |
| PreSonus | Eris E8 | Bookshelf |
| Genelec | 8030C | Bookshelf |
| Neumann | KH 80 DSP | Bookshelf |
| Focal | Alpha 65 | Bookshelf |
| Mackie | MR624 | Bookshelf |
| Rockville | RMB08 | Bookshelf |
| Edifier | 1280T | Bookshelf |
| Avantone | MixCube | Bookshelf |
| Kal | Mark 10 | Tower |

## Room Mode Calculator

Calculates three types of room modes:

1. **Axial modes** — React along one dimension (most problematic)
2. **Tangential modes** — React along two dimensions
3. **Oblique modes** — React along all three dimensions (least problematic)

## Pricing

| Tier | Price | Requests | Features |
|------|-------|----------|----------|
| **Free** | $0 | 50/day | All endpoints |
| **Dev** | $14/mo | Unlimited | All endpoints |
| **Pro** | $39/mo | Priority | + Advanced room analysis, bulk export |

## Recommended EQ Starting Points by Room Size

| Room Size | Volume (ft³) | Bass Correction | Notes |
|-----------|--------------|------------------|-------|
| Small | < 1,000 | +2-3 dB @ 40-50Hz | High modal density |
| Medium | 1,000-2,500 | +1.5-2 dB @ 50-63Hz | Standard treatment |
| Large | > 2,500 | +0.5-1 dB @ 63-80Hz | May need cuts instead |

## Example: Importing Settings

### Parametric EQ (Yamaha, Audyssey, etc.)
```
Freq: 40Hz, Gain: +2.0dB, Q: 3.5
Freq: 50Hz, Gain: +1.5dB, Q: 2.0
Freq: 63Hz, Gain: +1.2dB, Q: 2.0
...
```

### MiniDSP / DSP Processor
Transfer the recommended_eq_settings array directly.

## Technical Details

- **Speed of Sound:** 1130 ft/s (~70°F/21°C)
- **Frequency Range:** 20Hz - 20kHz
- **Room Mode Formula:** f = (c/2) × √((p/L)² + (q/W)² + (r/H)²)
- **Treatment Levels:** treated (acoustic panels + bass traps), partial (some panels), untreated (bare walls)

## License

MIT — Built for the homelab and pro audio community.

---

*Set it and forget it. Or measure with REW for precision tuning.*
