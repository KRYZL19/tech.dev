# VESSELFIND — US Boat & Ship Registration Lookup API

> *"That boat has three owners and a lien against it. One API call tells you before you buy."*

A lightweight FastAPI service for looking up US vessel registration data, owner history, lien status, and manufacturer records.

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/vessel/{vessel_id}` | Vessel details — length, beam, hull, year, manufacturer, model, propulsion, documentation number, lien status |
| `GET` | `/api/v1/vessel/{vessel_id}/history` | Owner history, previous owners, dates of ownership change, lien details |
| `POST` | `/api/v1/vessel/validate` | Validate a `documentation_number` → returns `valid`, `vessel_id`, `status` (active / cancelled / not_found), `lien_status` |
| `GET` | `/api/v1/manufacturer/{mfr}` | All vessels for a manufacturer with common model names |
| `GET` | `/api/v1/manufacturer` | List all available manufacturers |

---

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8765
```

API docs: `http://localhost:8765/docs`

---

## Data

**80 bundled vessel records** across 8 manufacturers:

| Manufacturer | Key | Vessels |
|---|---|---|
| Sea Ray | `sea_ray` | 10 |
| Boston Whaler | `boston_whaler` | 10 |
| Grady-White | `grady_white` | 10 |
| Yamaha | `yamaha` | 10 |
| MasterCraft | `mastercraft` | 10 |
| Malibu | `malibu` | 10 |
| Cobalt | `cobalt` | 10 |
| Pontoon | `pontoon` | 10 |

Each record includes owner history (single or multiple owners), lien status (`clear`, `lien`, `multiple_liens`), and lien holder details where applicable.

---

## Examples

**Get vessel details**
```bash
curl http://localhost:8765/api/v1/vessel/SR001
```

**Get owner & lien history**
```bash
curl http://localhost:8765/api/v1/vessel/SR001/history
```

**Validate a documentation number**
```bash
curl -X POST http://localhost:8765/api/v1/vessel/validate \
  -H "Content-Type: application/json" \
  -d '{"documentation_number": "1234567"}'
```

**Boats by manufacturer**
```bash
curl http://localhost:8765/api/v1/manufacturer/boston_whaler
```

---

## Vessel IDs (sample)

| ID | Name | Manufacturer |
|---|---|---|
| SR001 | Sea Esta | Sea Ray |
| BW001 | Pura Vida | Boston Whaler |
| GW001 | Three Sheets | Grady-White |
| YM001 | Wave Runnerz | Yamaha |
| MC001 | X-Cellent | MasterCraft |
| ML001 | Wake Nation | Malibu |
| CB001 | Cobalt Star | Cobalt |
| PT001 | Party Barge | Pontoon |
