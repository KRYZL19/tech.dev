"""BREWCRUNCH API - Homebrew Beer Recipe & Calculators.

A FastAPI backend for homebrew beer calculations and BJCP style matching.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from data.bjcp_styles import BJCP_STYLES
from data.hop_data import HOP_DATA
from data.grain_data import GRAIN_DATA
from models.schemas import (
    BJCP_style,
    StyleListResponse,
    HopResponse,
    GrainResponse,
)
from routes.calculator import router as calculator_router
from routes.recipe import router as recipe_router

app = FastAPI(
    title="BREWCRUNCH API",
    description="Homebrew Beer Recipe & Calculators — ABV, IBU, OG, and BJCP style matching",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(calculator_router, prefix="/api/v1")
app.include_router(recipe_router, prefix="/api/v1")


@app.get("/")
async def root():
    """API root with welcome message and pricing info."""
    return {
        "name": "BREWCRUNCH API",
        "tagline": "I spent more time doing math than brewing.",
        "version": "1.0.0",
        "docs": "/docs",
        "pricing": {
            "free": {"calls": "200/day", "price": "$0"},
            "dev": {"calls": "unlimited", "price": "$9/month"},
            "pro": {"calls": "unlimited", "price": "$29/month", "features": ["priority", "support"]},
        },
    }


@app.get("/api/v1/styles", response_model=StyleListResponse)
async def list_styles():
    """
    List all available BJCP styles with their parameter ranges.
    
    Returns OG, FG, ABV, and IBU ranges for each style.
    """
    styles = []
    for style in BJCP_STYLES:
        styles.append(BJCP_style(
            id=style["id"],
            name=style["name"],
            category=style["category"],
            og_range=style["og_range"],
            fg_range=style["fg_range"],
            abv_range=style["abv_range"],
            ibu_range=style["ibu_range"],
            srm_range=style.get("srm_range"),
            description=style.get("description"),
        ))
    
    return StyleListResponse(styles=styles, total=len(styles))


@app.get("/api/v1/hops/{variety}", response_model=HopResponse)
async def get_hop(variety: str):
    """
    Get hop data by variety name.
    
    - **variety**: Hop variety name (e.g., cascade, citra, mosaic)
    """
    variety_lower = variety.lower()
    
    if variety_lower not in HOP_DATA:
        available = list(HOP_DATA.keys())
        raise HTTPException(
            status_code=404,
            detail=f"Hop variety '{variety}' not found. Available: {', '.join(available)}",
        )
    
    hop = HOP_DATA[variety_lower]
    return HopResponse(
        variety=variety_lower,
        aa_percent=hop["aa"],
        type=hop["type"],
        typical_use=hop["typical_use"],
        notes=hop.get("notes"),
        substitutes=hop.get("substitutes"),
    )


@app.get("/api/v1/hops", response_model=list)
async def list_hops():
    """List all available hop varieties."""
    return [
        {
            "variety": name,
            "aa_percent": data["aa"],
            "type": data["type"],
            "typical_use": data["typical_use"],
        }
        for name, data in HOP_DATA.items()
    ]


@app.get("/api/v1/grains/{variety}", response_model=GrainResponse)
async def get_grain(variety: str):
    """
    Get grain data by variety name.
    
    - **variety**: Grain variety name (e.g., 2-row pale, crystal 40, chocolate)
    """
    variety_lower = variety.lower()
    
    if variety_lower not in GRAIN_DATA:
        available = list(GRAIN_DATA.keys())
        raise HTTPException(
            status_code=404,
            detail=f"Grain variety '{variety}' not found. Available: {', '.join(available)}",
        )
    
    grain = GRAIN_DATA[variety_lower]
    return GrainResponse(
        variety=variety_lower,
        ppg=grain["ppg"],
        color_lovibond=grain["color_lovibond"],
        type=grain["type"],
        notes=grain.get("notes"),
    )


@app.get("/api/v1/grains", response_model=list)
async def list_grains():
    """List all available grain varieties."""
    return [
        {
            "variety": name,
            "ppg": data["ppg"],
            "color_lovibond": data["color_lovibond"],
            "type": data["type"],
        }
        for name, data in GRAIN_DATA.items()
    ]


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "service": "brewcrunch-api"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
