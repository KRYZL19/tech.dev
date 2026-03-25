# SECFILER — SEC Filing Alert & Search API

**"Alert me when any company in sector X files a Form 4 within 24 hours."**

A lightweight FastAPI service for searching, browsing, and alerting on SEC filings — bundled with 200 realistic sample filings.

## Quick Start

```bash
cd secfiler
pip install -r requirements.txt
python main.py
# or: uvicorn main:app --reload --port 8000
```

API docs at `http://localhost:8000/docs`

## Endpoints

### Search Filings
```
GET /api/v1/search?q={query}&form_type={4|8-K|10-Q|10-K}&sector={tech|healthcare|energy|finance}&limit={n}
```
Full-text search across filing descriptions, company names, and tickers. Filter by form type and/or sector.

### Filing Detail
```
GET /api/v1/filing/{cik}/{form_type}/{accession}
```
Returns filing date, form type, description, and link to HTML filing.

### Insider Activity
```
GET /api/v1/insider/{ticker}
```
Recent Form 4 filings for a given ticker — insider name, transaction type, shares, price, and filing date.

### Today's Filings
```
GET /api/v1/filings/today
```
All 8-K and Form 4 filings from today (based on bundled sample data).

### Create Alert
```
POST /api/v1/alerts/create
Content-Type: application/json

{
  "keywords": ["acquisition", "buyback"],
  "form_types": ["4", "8-K"],
  "sector": "tech"
}
```
Create an alert criteria. Use `GET /api/v1/alerts/check/{alert_id}` to see matching filings.

## Sample Tickers

`AAPL MSFT GOOGL AMZN NVDA TSLA META NFLX AMD INTC ORCL CRM ADBE CSCO PYPL UBER SNAP SQ SHOP ABNB JPM BAC WFC GS MS V MA BLK SCHW AXP C USB PNC TFC COF JNJ UNH PFE ABBV MRK LLY TMO ABT DHR BMY AMGN GILD CVS ISRG VRTX XOM CVX COP SLB EOG MPC PSX OXY BKR HAL DVN FANG`

## Architecture

```
secfiler/
  main.py              FastAPI app
  requirements.txt     Dependencies
  data/
    filing_index.py    200 sample filings + in-memory search
  models/
    schemas.py         Pydantic request/response models
  routes/
    search.py          /search, /filing, /insider, /filings/today
    alerts.py          /alerts/create, /alerts/check
```

## Production Notes

- **Data**: Replace `data/filing_index.py` with live EDGAR API calls (`sec-api` or direct SEC EDGAR)
- **Storage**: Alerts stored in-memory; swap `_alerts` dict for a database (Postgres, SQLite)
- **Background checks**: Use a cron job or task queue to evaluate alerts against new filings and trigger webhooks/notifications
- **CORS**: Open by default; restrict in production
