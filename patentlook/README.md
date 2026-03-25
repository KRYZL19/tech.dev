# PATENTLOOK

**Search 50 years of US patents by technical claim, not just keyword.**

PATENTLOOK is a lightweight REST API that lets you query a bundled database of 500 sample US patents across semiconductors, batteries, AI/ML, pharma, EVs, and solar — using full-text search across titles, abstracts, claims, inventors, and assignees.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API runs at `http://localhost:8000`. Swagger docs at `http://localhost:8000/docs`.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/search` | Search patents by query + filters |
| GET | `/api/v1/patent/{patent_number}` | Get full patent details |
| GET | `/api/v1/inventor/{inventor_name}` | Patents by inventor |
| GET | `/api/v1/assignee/{assignee_name}` | Patents by company |
| GET | `/api/v1/classification/{IPC_code}` | Patents by IPC class |

## Search Syntax

```
GET /api/v1/search?q={query}&class={IPC_class}&year_start={y}&year_end={y}&limit={n}
```

- `q` — Technical query (searches title, abstract, claims, inventor, assignee)
- `class` — IPC classification code (e.g. `H01L`, `G06N`, `A61K`, `B60L`)
- `year_start` — Earliest filing year (e.g. `2015`)
- `year_end` — Latest filing year (e.g. `2025`)
- `limit` — Max results (default 50, max 500)

### Example Queries

```bash
# Search for neural network hardware
curl "http://localhost:8000/api/v1/search?q=neural+network+accelerator&limit=10"

# Semiconductor patents from 2020+
curl "http://localhost:8000/api/v1/search?q=transistor&class=H01L&year_start=2020&limit=20"

# EV battery patents
curl "http://localhost:8000/api/v1/search?q=lithium+electrolyte&class=B60L&limit=15"
```

## IPC Classifications Bundled

| Code | Domain |
|------|--------|
| H01L | Semiconductor devices |
| H01M | Batteries |
| G06N | AI/ML computer systems |
| A61K | Pharmaceutical preparations |
| B60L | Electric vehicles |
| H01G | Capacitors/supercapacitors |
| F24S | Solar thermal collectors |
| H02J | Power systems |
| C01B | Battery materials |
| G06F | Data processing |

## Sample Patent Numbers

The database contains 500 patents numbered roughly `US4000000` – `US12000000`. Try:

```bash
curl "http://localhost:8000/api/v1/patent/US4000000B1"
curl "http://localhost:8000/api/v1/patent/US7000000A1"
```

## Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Tech Stack

- FastAPI
- Pydantic
- Uvicorn
