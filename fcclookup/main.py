"""FCCLOOKUP — FCC Licensee & Equipment Database API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import callsign, equipment, freq

app = FastAPI(
    title="FCCLOOKUP",
    description="Ham radio license lookup in one call. Equipment certification. Frequency allocation.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(callsign.router)
app.include_router(equipment.router)
app.include_router(freq.router)


@app.get("/")
async def root():
    return {
        "name": "FCCLOOKUP",
        "description": "Ham radio license lookup in one call. Equipment certification. Frequency allocation.",
        "version": "1.0.0",
        "endpoints": {
            "/api/v1/callsign/{callsign}": "License class, privileges, FRN, expiration",
            "/api/v1/equipment/{fcc_id}": "Device type, frequencies, max power",
            "/api/v1/frequency/{mhz}": "Band info, allocation type, power limits",
            "/api/v1/bands/amateur": "Full ham band chart by license class",
            "/api/v1/interference/check": "Frequency + location → interference sources (POST)",
        },
    }


@app.get("/health")
async def health():
    return {"status": "ok"}
