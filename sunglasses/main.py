"""
SUNGLASSES — Aviation Incident Report Database
FastAPI application serving NASA ASRS-style incident reports.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.incidents import router as incidents_router
from routes.airport import router as airport_router
from data.incident_index import count_total

app = FastAPI(
    title="SUNGLASSES",
    description="Aviation Incident Report Database — laser illuminations, wildlife strikes, operational incidents, near-midair conflicts.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(incidents_router)
app.include_router(airport_router)


@app.get("/")
def root():
    return {
        "name": "SUNGLASSES",
        "description": "Aviation Incident Report Database",
        "version": "1.0.0",
        "total_incidents": count_total(),
        "endpoints": {
            "search": "GET /api/v1/incidents/search?airport_code={ICAO}&radius_mi={r}&year={y}",
            "detail": "GET /api/v1/incident/{report_id}",
            "airport_summary": "GET /api/v1/airport/{ICAO}/summary",
            "by_type": "GET /api/v1/incidents/type/{type}",
        },
    }


@app.get("/health")
def health():
    return {"status": "ok"}
