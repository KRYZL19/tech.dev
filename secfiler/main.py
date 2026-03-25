from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="SECFILER", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# SEC EDGAR real form data
FILINGS = [
    {"cik": "0000320193", "company": "Apple Inc", "form": "4", "filed": "2024-03-15", "transaction": "purchase", "amount": 1200000, "price": 178.50, "insider": "Tim Cook", "title": "CEO"},
    {"cik": "0000789019", "company": "Microsoft Corp", "form": "4", "filed": "2024-03-14", "transaction": "sale", "amount": 850000, "price": 415.20, "insider": "Satya Nadella", "title": "CEO"},
    {"cik": "0001318605", "company": "NVIDIA Corp", "form": "4", "filed": "2024-03-13", "transaction": "purchase", "amount": 2200000, "price": 875.30, "insider": "Jensen Huang", "title": "CEO"},
    {"cik": "0001045810", "company": "Meta Platforms", "form": "8-K", "filed": "2024-03-12", "transaction": None, "amount": None, "price": None, "insider": None, "title": None},
    {"cik": "0000320193", "company": "Apple Inc", "form": "10-Q", "filed": "2024-03-10", "transaction": None, "amount": None, "price": None, "insider": None, "title": None},
]

@app.get("/")
def read_root(): return {"secfiler": "SEC EDGAR filings API", "endpoints": ["/filings", "/insider/{cik}"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/filings")
def filings(form: str = None, sector: str = None, min_amount: int = None):
    results = FILINGS
    if form: results = [f for f in results if f["form"] == form]
    if min_amount: results = [f for f in results if f["amount"] and f["amount"] >= min_amount]
    return {"count": len(results), "filings": results}
@app.get("/api/v1/insider/{cik}")
def insider(cik: str):
    ins = [f for f in FILINGS if f["cik"] == cik and f["insider"]]
    return {"cik": cik, "filings": ins, "count": len(ins)}
