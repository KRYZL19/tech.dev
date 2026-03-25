# FCCLOOKUP

**Ham radio license lookup in one call. Equipment certification. Frequency allocation.**

A lightweight FastAPI service providing FCC amateur radio licensee data, equipment certifications, and frequency allocation information.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/callsign/{callsign}` | License class, privileges, FRN, expiration |
| GET | `/api/v1/equipment/{fcc_id}` | Device type, frequencies, max power |
| GET | `/api/v1/frequency/{mhz}` | Band info, allocation type, power limits |
| GET | `/api/v1/bands/amateur` | Full ham band chart by license class |
| POST | `/api/v1/interference/check?mhz=146.52&location=Anytown` | Frequency + location → interference sources |

## Example

```bash
curl http://localhost:8000/api/v1/callsign/W1ABC
```

```json
{
  "callsign": "W1ABC",
  "frn": "0012345678",
  "licensee": "John A. Smith",
  "status": "Active",
  "class": "Extra",
  "expired": "2028-03-15",
  "grid": "FN31pr",
  "address": "123 Main St, Anytown, MA 01234",
  "privileges": ["80 Meters: 3525-3750 kHz", "40 Meters: 7025-7300 kHz", ...]
}
```

## Bundled Data

- **Amateur band chart**: 160m through 23cm with frequency ranges and license class privileges
- **20 callsign records**: Sample FCC licensee records across all license classes
- **15 equipment certifications**: Sample FCC equipment authorizations (transceivers, amplifiers, antennas)

## Tech Stack

- FastAPI — async web framework
- Pydantic — data validation
- Uvicorn — ASGI server
