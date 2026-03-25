"""
SECFILER — SEC Filing Alert & Search API

Alert me when any company in sector X files a Form 4 within 24 hours.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.search import router as search_router
from routes.alerts import router as alerts_router

app = FastAPI(
    title="SECFILER",
    description="SEC Filing Alert & Search API. Search filings, track insider activity, and set alerts.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router)
app.include_router(alerts_router)


@app.get("/", tags=["health"])
def root():
    return {
        "service": "SECFILER",
        "version": "1.0.0",
        "description": "SEC Filing Alert & Search API",
        "docs": "/docs",
        "endpoints": [
            "GET  /api/v1/search",
            "GET  /api/v1/filing/{cik}/{form_type}/{accession}",
            "GET  /api/v1/insider/{ticker}",
            "GET  /api/v1/filings/today",
            "POST /api/v1/alerts/create",
        ],
    }


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
