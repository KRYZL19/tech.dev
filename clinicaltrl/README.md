# CLINICALTRL - Clinical Trial Results Database

A FastAPI-based REST API for searching and retrieving clinical trial data.

## Hook

> "Find all phase 3 trials for drug X with positive results. One query."

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

API runs at `http://localhost:8000`

## Endpoints

### Search Trials
```
GET /api/v1/search?condition={query}&phase={3}&status={COMPLETED}&results=true&limit={n}
```

### Get Trial Details
```
GET /api/v1/trial/{nct_id}
```
Returns: brief_summary, eligibility_criteria, design_info, results[], serious_adverse_events[], enrollment, start_date, completion_date

### Trials by Drug
```
GET /api/v1/drug/{drug_name}/trials
```

### Trials by Sponsor
```
GET /api/v1/sponsor/{sponsor_name}
```
Returns: trials with success rate

### Trials by Location
```
GET /api/v1/location?country={c}&state={s}
```

## Examples

```bash
# Find all Phase 3 completed trials for semaglutide with results
curl "http://localhost:8000/api/v1/search?condition=diabetes&phase=3&status=COMPLETED&results=true"

# Get specific trial
curl "http://localhost:8000/api/v1/trial/NCT00010001"

# All trials for pembrolizumab
curl "http://localhost:8000/api/v1/drug/pembrolizumab/trials"

# Pfizer trials with success rate
curl "http://localhost:8000/api/v1/sponsor/Pfizer"

# Trials in United States
curl "http://localhost:8000/api/v1/location?country=United+States"
```

## Bundled Data

- 200 realistic clinical trials
- Real drug names: semaglutide, pembrolizumab, aducanumab, ozempic, tirzepatide, etc.
- Real sponsors: Pfizer, Novartis, Roche, Johnson & Johnson, Merck, etc.
- Phases 1-4, various statuses
- ~40% have submitted results

## Docs

Visit `http://localhost:8000/docs` for interactive Swagger UI.
