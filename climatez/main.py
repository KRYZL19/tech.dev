"""CLIMATEZ — Historical Weather & Climate API.

A simple API for accessing 30-year climate normals and frost date data
for major US cities.

Hook: "What's the frost date history for this zip code? 30-year normals. One query."
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from data.climate_normals import get_all_cities
from routes.weather import router as weather_router
from routes.analysis import router as analysis_router


app = FastAPI(
    title="CLIMATEZ",
    description=(
        "Historical Weather & Climate API. "
        "Access 30-year climate normals and frost date history for major US cities. "
        "See /docs for interactive API explorer."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(weather_router)
app.include_router(analysis_router)


@app.get("/", tags=["info"])
async def root():
    """API root with quick links."""
    return {
        "name": "CLIMATEZ",
        "version": "1.0.0",
        "tagline": "Historical Weather & Climate API",
        "hook": "What's the frost date history for this zip code? 30-year normals. One query.",
        "docs": "/docs",
        "endpoints": {
            "climate_normals": "/api/v1/normals/{zipcode}",
            "frost_dates": "/api/v1/frost-dates/{zipcode}",
            "precipitation": "/api/v1/precipitation/{zipcode}/annual",
            "growing_season": "/api/v1/growing-season (POST)",
        },
        "cities_covered": 50,
    }


@app.get("/health", tags=["info"])
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/cities", tags=["info"])
async def list_cities():
    """List all cities with climate data."""
    cities = get_all_cities()
    return {
        "count": len(cities),
        "cities": [
            {
                "zipcode": c["zipcode"],
                "city": c["city"],
                "state": c["state"],
            }
            for c in cities
        ],
    }


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler."""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": str(exc),
            "status_code": 500,
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
