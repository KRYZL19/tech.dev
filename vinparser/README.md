# VINPARSER API

**Motorcycle VIN Decoder API**

> "The VIN on that 2019 vs 2021 MT-09 looks identical. One character tells you everything."

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API available at `http://localhost:8000`  
Swagger docs: `http://localhost:8000/docs`

## Endpoints

### POST `/api/v1/vin/decode`
Decode a motorcycle VIN to extract make, model, year, and full specifications.

```bash
curl -X POST "http://localhost:8000/api/v1/vin/decode" \
  -H "Content-Type: application/json" \
  -d '{"vin": "JYARM09E5LA123456"}'
```

**Response:**
```json
{
  "make": "Yamaha",
  "model": "MT-09",
  "year": 2021,
  "engine_cc": 889,
  "hp": 119,
  "wet_weight_kg": 190,
  "frame_type": "Diamond",
  "country": "Japan",
  "plant": "L",
  "sequential_number": "123456",
  "vin": "JYARM09E5LA123456"
}
```

### POST `/api/v1/vin/validate`
Validate VIN format and check digit.

```bash
curl -X POST "http://localhost:8000/api/v1/vin/validate" \
  -H "Content-Type: application/json" \
  -d '{"vin": "JYARM09E5LA123456"}'
```

**Response:**
```json
{
  "valid_format": true,
  "check_digit_correct": true,
  "country_of_origin": "Japan",
  "year_char": "M",
  "vin": "JYARM09E5LA123456"
}
```

### GET `/api/v1/model/{make}/{year}/{model}`
Get full specifications for a known model.

```bash
curl "http://localhost:8000/api/v1/model/Yamaha/2021/MT-09"
```

## Supported Manufacturers

- Yamaha
- Kawasaki
- Honda
- Suzuki
- Harley-Davidson
- BMW Motorrad
- Ducati
- KTM
- Triumph

## VIN Structure

| Position | Field | Description |
|----------|-------|-------------|
| 1-3 | WMI | World Manufacturer Identifier |
| 4-8 | VDS | Vehicle Descriptor Section |
| 9 | Check | Check digit (weighted sum mod 11) |
| 10 | Year | Model year code |
| 11 | Plant | Assembly plant |
| 12-17 | SEQ | Sequential number |

## Year Codes

| Code | Year | Code | Year |
|------|------|------|------|
| A | 2010 | L | 2020 |
| B | 2011 | M | 2021 |
| C | 2012 | N | 2022 |
| D | 2013 | P | 2023 |
| E | 2014 | R | 2024 |
| F | 2015 | S | 2025 |
| G | 2016 | T | 2026 |
| H | 2017 | | |
| J | 2018 | | |
| K | 2019 | | |

## Pricing

| Tier | Requests | Price |
|------|----------|-------|
| Free | 100/day | $0 |
| Dev | Unlimited | $14/mo |
| Pro | Unlimited + Priority | $39/mo |

## License

MIT
