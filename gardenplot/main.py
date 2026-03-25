"""
GARDENPLOT - Vegetable Garden Planner API

A FastAPI application for planning vegetable gardens, crop rotation,
and companion planting based on USDA zones and available space.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime
import time

from routes.planner import router as planner_router
from routes.rotation import router as rotation_router
from models.schemas import HealthResponse

app = FastAPI(
    title="GARDENPLOT API",
    description="Vegetable Garden Planner - Plan your garden based on zone, sunlight, and space",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rate limiting storage (simple in-memory)
# Production would use Redis or similar
rate_limit_storage = {}


def check_rate_limit(api_key: str, tier: str = "free") -> tuple[bool, int]:
    """Check if request is within rate limits. Returns (allowed, remaining)."""
    today = datetime.now().strftime("%Y-%m-%d")
    key = f"{api_key}:{today}"
    
    limits = {
        "free": 100,
        "dev": 10000,
        "pro": 100000
    }
    
    limit = limits.get(tier, 100)
    current = rate_limit_storage.get(key, 0)
    
    if current >= limit:
        return False, 0
    
    rate_limit_storage[key] = current + 1
    remaining = limit - current - 1
    return True, remaining


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    """Simple rate limiting middleware."""
    start_time = time.time()
    
    # Skip rate limiting for health checks and docs
    if request.url.path in ["/", "/health", "/docs", "/redoc", "/openapi.json"]:
        response = await call_next(request)
        return response
    
    # Get API key from header or query param
    api_key = request.headers.get("X-API-Key") or request.query_params.get("api_key", "anonymous")
    
    # Determine tier from API key format (simplified)
    tier = "free"
    if api_key.startswith("dev_"):
        tier = "dev"
    elif api_key.startswith("pro_"):
        tier = "pro"
    
    allowed, remaining = check_rate_limit(api_key, tier)
    
    if not allowed:
        return JSONResponse(
            status_code=429,
            content={
                "error": "Rate limit exceeded",
                "tier": tier,
                "limit": {"free": 100, "dev": 10000, "pro": 100000}[tier],
                "reset": "Midnight UTC"
            }
        )
    
    response = await call_next(request)
    response.headers["X-RateLimit-Remaining"] = str(remaining)
    response.headers["X-RateLimit-Tier"] = tier
    response.headers["X-Response-Time"] = f"{(time.time() - start_time) * 1000:.2f}ms"
    
    return response


# Include routers
app.include_router(planner_router)
app.include_router(rotation_router)


@app.get("/", tags=["root"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": "GARDENPLOT API",
        "version": "1.0.0",
        "tagline": "Your vegetable garden planner",
        "hook": "Your shade pattern means these 6 vegetables will actually work. Here's what.",
        "docs": "/docs",
        "endpoints": {
            "what_grows": "POST /api/v1/planner/what-grows",
            "plant_detail": "GET /api/v1/plant/{name}",
            "rotation_plan": "POST /api/v1/rotation/plan",
            "companion_check": "POST /api/v1/companion/check",
            "frost_dates": "GET /api/v1/frost/{zipcode}"
        },
        "pricing": {
            "free": {"requests_per_day": 100},
            "dev": {"price_monthly": "$9", "requests_per_day": 10000},
            "pro": {"price_monthly": "$29", "requests_per_day": 100000}
        }
    }


@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version="1.0.0"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
