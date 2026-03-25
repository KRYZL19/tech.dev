"""
KNOTDB — Nautical Knot Reference API

50 knots with load ratings. Bowline vs cleat vs rolling hitch — 
know the difference before you need it.

Pricing:
- Free: 100 requests/day
- Dev: $9/month
- Pro: $29/month
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from collections import defaultdict
import uvicorn

from routes.knots import router as knots_router
from routes.load_calc import router as load_router

app = FastAPI(
    title="KNOTDB",
    description="50 nautical knots with load ratings. Bowline vs cleat vs rolling hitch — know the difference before you need it.",
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

# Simple rate limiting (in-memory, per IP)
rate_limit_store = defaultdict(list)
RATE_LIMIT_FREE = 100
RATE_LIMIT_WINDOW = timedelta(days=1)


def check_rate_limit(client_ip: str) -> tuple[bool, int]:
    """Check if request is within rate limit. Returns (allowed, remaining)."""
    now = datetime.utcnow()
    # Clean old entries
    rate_limit_store[client_ip] = [
        t for t in rate_limit_store[client_ip]
        if now - t < RATE_LIMIT_WINDOW
    ]
    
    if len(rate_limit_store[client_ip]) >= RATE_LIMIT_FREE:
        return False, 0
    
    rate_limit_store[client_ip].append(now)
    remaining = RATE_LIMIT_FREE - len(rate_limit_store[client_ip])
    return True, remaining


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    """Apply rate limiting to all requests."""
    # Skip rate limiting for docs
    if request.url.path in ["/docs", "/redoc", "/openapi.json", "/"]:
        return await call_next(request)
    
    client_ip = request.client.host if request.client else "unknown"
    allowed, remaining = check_rate_limit(client_ip)
    
    response = await call_next(request)
    response.headers["X-RateLimit-Limit"] = str(RATE_LIMIT_FREE)
    response.headers["X-RateLimit-Remaining"] = str(remaining)
    
    if not allowed:
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded. Free tier: 100 requests/day. Upgrade to Dev ($9/mo) or Pro ($29/mo) for more."},
            headers=dict(response.headers)
        )
    
    return response


# Include routers
app.include_router(knots_router)
app.include_router(load_router)


@app.get("/")
async def root():
    """API root with welcome info."""
    return {
        "name": "KNOTDB",
        "version": "1.0.0",
        "tagline": "50 nautical knots with load ratings. Bowline vs cleat vs rolling hitch — know the difference before you need it.",
        "endpoints": {
            "GET /api/v1/knots": "List all 50 knots with summary info",
            "GET /api/v1/knot/{name}": "Full knot details including how-to-tie steps",
            "GET /api/v1/knots/category/{cat}": "Filter by category (bending, binding, loop, stopper, slip, hitch)",
            "GET /api/v1/knots/search?use_case={query}": "Find knots for anchoring, mooring, towing, rescue, fishing, climbing",
            "POST /api/v1/load/compare": "Compare two knots under a given load",
            "GET /api/v1/load/calculate/{knot_name}": "Calculate load capacity for a knot",
            "GET /api/v1/categories": "List all categories",
            "GET /api/v1/use-cases": "List all use cases"
        },
        "pricing": {
            "free": {"requests_per_day": 100},
            "dev": {"price": "$9/month", "requests_per_day": 10000},
            "pro": {"price": "$29/month", "requests_per_day": "unlimited"}
        },
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
