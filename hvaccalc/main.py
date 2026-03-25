"""
HVACCALC — HVAC System Sizing Calculator API

Manual J is required by code for every HVAC install. Nobody does it manually.
This does it in one API call.

Pricing tiers:
  Free: 50 requests/day (no auth required)
  Dev:  $19/mo — 1000 requests/day
  Pro:  $49/mo — unlimited
"""
import time
from collections import defaultdict
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from hvaccalc.routes.load import router as load_router
from hvaccalc.routes.sizing import router as sizing_router


# ── Rate limiting (in-memory, per-IP) ────────────────────────────────────────
# For production, swap for Redis-backed rate limiter
daily_requests: dict[str, list[float]] = defaultdict(list)

RATE_LIMITS = {
    "free": {"daily": 50, "window": 86400},
    "dev": {"daily": 1000, "window": 86400},
    "pro": {"daily": float("inf"), "window": 86400},
}

TIER_DAILY = {"free": 50, "dev": 1000, "pro": float("inf")}


def get_client_tier(request: Request) -> str:
    """Resolve tier from X-API-Key header or IP-based free tier."""
    api_key = request.headers.get("X-API-Key", "")
    # In production, look up API key in database
    if api_key.startswith("pk_pro_"):
        return "pro"
    if api_key.startswith("pk_dev_"):
        return "dev"
    return "free"


def check_rate_limit(client_ip: str, tier: str) -> tuple[bool, int, int]:
    """Check if request is within rate limit. Returns (allowed, remaining, reset_in)."""
    now = time.time()
    window = 86400
    requests = daily_requests[client_ip]
    # Prune old entries
    cutoff = now - window
    requests[:] = [t for t in requests if t > cutoff]

    limit = TIER_DAILY.get(tier, 50)
    remaining = max(0, int(limit - len(requests)))
    allowed = len(requests) < limit

    # Reset time = oldest request + window
    reset_in = int(window - (now - requests[0])) if requests else 0

    return allowed, remaining, reset_in


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown — prune all counters
    daily_requests.clear()


# ── App ────────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="HVACCALC",
    description="HVAC System Sizing Calculator — Manual J simplified via API",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(load_router)
app.include_router(sizing_router)


# ── Middleware: rate limiting ──────────────────────────────────────────────────
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if request.url.path.startswith("/docs") or request.url.path.startswith("/redoc"):
        return await call_next(request)

    client_ip = request.client.host if request.client else "unknown"
    tier = get_client_tier(request)
    allowed, remaining, reset_in = check_rate_limit(client_ip, tier)

    if not allowed:
        return JSONResponse(
            status_code=429,
            content={
                "error": "Rate limit exceeded",
                "tier": tier,
                "limit": TIER_DAILY[tier],
                "reset_in_seconds": reset_in,
                "upgrade": "Upgrade to Dev ($19/mo) or Pro ($49/mo) for higher limits",
            },
            headers={
                "X-RateLimit-Limit": str(TIER_DAILY[tier]),
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": str(reset_in),
                "Retry-After": str(reset_in),
            },
        )

    # Record request
    daily_requests[client_ip].append(time.time())

    response = await call_next(request)
    response.headers["X-RateLimit-Limit"] = str(TIER_DAILY[tier])
    response.headers["X-RateLimit-Remaining"] = str(remaining - 1)
    return response


# ── Health ─────────────────────────────────────────────────────────────────────
@app.get("/health", tags=["health"])
def health():
    return {"status": "ok", "service": "hvaccalc", "version": "1.0.0"}


@app.get("/api/v1", tags=["info"])
def api_info():
    return {
        "service": "HVACCALC",
        "tagline": "Manual J is required by code. Nobody does it manually. This does it in one API call.",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/v1/load/residential": "Calculate heating/cooling load",
            "GET  /api/v1/climate/{zipcode}": "Look up climate zone by ZIP",
            "POST /api/v1/duct/size": "Size ductwork",
            "POST /api/v1/equipment/size": "Size equipment",
        },
        "pricing": {
            "free": "50 requests/day",
            "dev": "$19/mo — 1000 requests/day",
            "pro": "$49/mo — unlimited",
        },
    }


# ── Error handler ─────────────────────────────────────────────────────────────
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
