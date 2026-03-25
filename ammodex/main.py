"""
AMMODEX API - Firearm Ammunition Database & Reloading Reference

"Every reloader I know has a spreadsheet with powder data from 6 different PDF manuals. 
This shouldn't be a spreadsheet."

FastAPI backend serving ammunition data, ballistic info, and reloading calculations.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import ballistics, reload
from models.schemas import HealthResponse

app = FastAPI(
    title="AMMODEX API",
    description="Firearm Ammunition Database & Reloading Reference",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS for browser-based clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ballistics.router)
app.include_router(reload.router)


@app.get("/", tags=["root"])
async def root():
    """Root endpoint with API info."""
    return {
        "name": "AMMODEX API",
        "version": "1.0.0",
        "description": "Firearm Ammunition Database & Reloading Reference",
        "docs": "/docs",
        "pricing": {
            "free": {"calls_per_day": 100},
            "dev": {"price": "$19/month", "calls_per_day": 5000},
            "pro": {"price": "$59/month", "calls_per_day": "unlimited"},
        },
    }


@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check():
    """Health check endpoint."""
    return HealthResponse(status="healthy", version="1.0.0")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
