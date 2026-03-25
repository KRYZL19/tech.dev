"""
POOLCHEM — Swimming Pool Water Balance API

FCI over 150ppm and your chlorine demand doubles overnight.
Nobody explains the chemistry. This does.

Pricing:
  Free:  100 requests/day (unauthenticated)
  Dev:   $9/mo  — unlimited requests
  Pro:   $29/mo — unlimited + FCI alert webhooks + bulk dosing

Run:
  uvicorn main:app --reload --port 8000
  uvicorn main:app --host 0.0.0.0 --port 8000  # production
"""
import time
from collections import defaultdict
from contextlib import asynccontextmanager
from functools import wraps
from typing import Callable

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routes.balance import router as balance_router
from routes.dosing import router as dosing_router, calc_breakpoint
from models.schemas import HealthResponse, ChloramineConvertRequest, ChloramineConvertResponse


# ---- Rate Limiting (in-memory, per-IP) ----
class RateLimiter:
    """Simple in-memory rate limiter. Use Redis in production for multi-instance."""

    def __init__(self):
        self.hits: dict = defaultdict(list)
        self.tiers = {
            "free": 100,    # per day
            "dev": 10_000,  # per day (effectively unlimited)
            "pro": 100_000,
        }

    def get_tier(self, api_key: str | None) -> str:
        if not api_key:
            return "free"
        if api_key.startswith("pk_dev_"):
            return "dev"
        if api_key.startswith("pk_pro_"):
            return "pro"
        return "free"

    def check(self, ip: str, tier: str) -> tuple[bool, int]:
        now = time.time()
        window = 86400  # 1 day
        limit = self.tiers.get(tier, 100)

        # Clean old entries
        self.hits[ip] = [t for t in self.hits[ip] if now - t < window]

        remaining = limit - len(self.hits[ip])
        if remaining <= 0:
            return False, 0

        self.hits[ip].append(now)
        return True, remaining - 1

    def reset_day(self, ip: str):
        now = time.time()
        self.hits[ip] = [t for t in self.hits[ip] if now - t >= 86400]


rate_limiter = RateLimiter()


def rate_limit(func: Callable):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        api_key = request.headers.get("X-API-Key")
        ip = request.client.host if request.client else "unknown"
        tier = rate_limiter.get_tier(api_key)

        allowed, remaining = rate_limiter.check(ip, tier)
        if not allowed:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail={
                    "error": "Daily rate limit exceeded",
                    "tier": tier,
                    "limit": rate_limiter.tiers.get(tier, 100),
                    "upgrade": "Get Dev ($9/mo) or Pro ($29/mo) at /pricing"
                }
            )

        response = await func(request, *args, **kwargs)
        if hasattr(response, "__dict__") and hasattr(response, "requests_remaining"):
            pass  # already set
        return response
    return wrapper


# ---- Lifespan ----
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🏊 POOLCHEM v1.0.0 — Swimming Pool Water Balance API")
    print("   FCI over 150ppm and your chlorine demand doubles overnight.")
    yield
    # Shutdown
    print("👋 POOLCHEM shutting down.")


# ---- App ----
app = FastAPI(
    title="POOLCHEM",
    description="Swimming Pool Water Balance API — LSI calculations, chlorine dosing, pH adjustment, and breakpoint chlorination with FCI-aware demand curves.",
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


@app.middleware("http")
async def add_rate_headers(request: Request, call_next):
    api_key = request.headers.get("X-API-Key")
    ip = request.client.host if request.client else "unknown"
    tier = rate_limiter.get_tier(api_key)
    allowed, remaining = rate_limiter.check(ip, tier)

    response = await call_next(request)
    response.headers["X-RateLimit-Tier"] = tier
    response.headers["X-RateLimit-Remaining"] = str(remaining)
    response.headers["X-RateLimit-Limit"] = str(rate_limiter.tiers.get(tier, 100))
    return response


# Include routers
app.include_router(balance_router, prefix="/api/v1")
app.include_router(dosing_router, prefix="/api/v1")

# Standalone convert routes at /api/v1 level (not nested under /dose)
app.add_api_route(
    "/api/v1/convert/chloramine",
    calc_breakpoint,
    methods=["POST"],
    response_model=ChloramineConvertResponse,
    tags=["convert"],
)


@app.get("/", tags=["root"])
async def root():
    return {
        "name": "POOLCHEM",
        "version": "1.0.0",
        "tagline": "FCI over 150ppm and your chlorine demand doubles overnight. Nobody explains the chemistry. This does.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health():
    return HealthResponse(
        status="ok",
        version="1.0.0",
        tier="free",
        requests_remaining=100
    )


@app.get("/pricing", tags=["info"])
async def pricing():
    return {
        "tiers": [
            {
                "name": "Free",
                "price": "$0",
                "requests": "100/day",
                "features": [
                    "Full LSI balance check",
                    "Chlorine dosing calculator",
                    "pH adjustment calculator",
                    "Breakpoint chlorination",
                    "FCI warning (150ppm threshold)",
                ]
            },
            {
                "name": "Dev",
                "price": "$9/mo",
                "requests": "Unlimited",
                "features": [
                    "Everything in Free",
                    "API key authentication",
                    "No rate limits",
                    "Priority support",
                ]
            },
            {
                "name": "Pro",
                "price": "$29/mo",
                "requests": "Unlimited",
                "features": [
                    "Everything in Dev",
                    "FCI alert webhooks",
                    "Bulk batch dosing",
                    "Historical trend analysis",
                    "Commercial pool support",
                ]
            }
        ]
    }


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )
