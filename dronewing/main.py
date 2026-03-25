"""
DRONEWING API — Drone Flight Compliance & Airspace

"LAANC authorization takes 30 seconds if you know the grid ID.
Most apps make you tap through 12 screens."
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import airspace, compliance

app = FastAPI(
    title="DRONEWING API",
    description="Drone airspace compliance & LAANC grid lookup for FAA Part 107 pilots.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(airspace.router)
app.include_router(compliance.router)


@app.get("/")
def root():
    return {
        "name": "DRONEWING API",
        "version": "1.0.0",
        "hook": "LAANC authorization takes 30 seconds if you know the grid ID. Most apps make you tap through 12 screens.",
        "endpoints": {
            "POST /api/v1/airspace/check": "Check airspace class, LAANC eligibility, max altitude",
            "GET  /api/v1/grid/search": "Find FAA UAS facility map grid ID for LAANC",
            "POST /api/v1/flight/plan": "Analyze waypoints for airspace conflicts and flight time",
        },
        "pricing": {
            "free": "50 requests/day",
            "dev": "$19/month",
            "pro": "$59/month",
        },
    }


@app.get("/health")
def health():
    return {"status": "ok"}
