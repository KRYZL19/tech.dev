"""
MARINEDB - Marine Navigation & Conditions API

"Tides don't care about your schedule. Neither should your autopilot."
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime

from routes import navigation, tides

app = FastAPI(
    title="MARINEDB",
    description="Marine Navigation & Conditions API — real-time port data, tide predictions, and route planning for coastal vessels.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(navigation.router)
app.include_router(tides.router)


@app.get("/")
async def root():
    return {
        "name": "MARINEDB",
        "tagline": "Tides don't care about your schedule. Neither should your autopilot.",
        "version": "1.0.0",
        "docs": "/docs",
        "pricing": {
            "free": "100 calls/day",
            "dev": "$19/month",
            "pro": "$49/month",
        },
    }


@app.get("/health")
async def health():
    return {"status": "operational", "timestamp": datetime.utcnow().isoformat()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
