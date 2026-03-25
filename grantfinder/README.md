# GRANTFINDER — US Government Grant Opportunities API

A REST API for searching and filtering US government grant opportunities across multiple agencies.

## Quick Start

```bash
cd grantfinder
pip install -r requirements.txt
python main.py
```

API runs at `http://localhost:5000`

## Endpoints

### Search Grants
```
GET /api/v1/search?q={keyword}&agency={DOE|EPA|NASA|NSF|DOI|USDA|HHS|EDA}&deadline_within_days={n}&limit={n}
```

**Example:**
```bash
curl "http://localhost:5000/api/v1/search?q=rural%20broadband&deadline_within_days=60"
```

### Get Grant Details
```
GET /api/v1/grant/{grant_id}
```

Returns: description, eligibility_criteria[], award_amount, match_requirement, application_deadline, total_funding, cfda_number

### Agency Grants
```
GET /api/v1/agency/{agency_name}/grants
```

Lists all open grants from a specific agency.

### Eligibility Check
```
POST /api/v1/eligibility/check
Content-Type: application/json

{
  "organization_type": "local_government",
  "annual_revenue": 500000,
  "employees": 50,
  "sector": ["broadband", "infrastructure"]
}
```

Returns matching grants with a match_score (0-100).

### Summary
```
GET /api/v1/summary
```

Returns total open grants count by agency and sector.

## Sample Response

**Search for rural broadband:**
```json
{
  "query": "rural broadband",
  "total_results": 12,
  "grants": [
    {
      "grant_id": "GRANT-DOE-0042",
      "title": "Rural Broadband Deployment Initiative",
      "agency": "DOE",
      "award_amount_min": 500000,
      "award_amount_max": 5000000,
      "application_deadline": "2026-05-15",
      "sector": ["broadband"]
    }
  ]
}
```

## Agencies Included
DOE, EPA, NASA, NSF, DOI, USDA, HHS, EDA

## Sample Data
Bundled with 150 sample grants for development/testing.
