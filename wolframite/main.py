"""
WOLFRAMITE — Chess Puzzle API
Chess puzzles rated 1800+ from any FEN position. Not an app. An API.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routes import puzzle, evaluation as eval_route
import time
import hashlib

app = FastAPI(
    title="WOLFRAMITE",
    description="Chess puzzles rated 1800+ from any FEN position. Not an app. An API.",
    version="1.0.0",
)

# Rate limiting (simple in-memory)
# Free: 50/day, Dev $14/mo: 1000/day, Pro $39/mo: 10000/day
RATE_LIMITS = {
    "free": 50,
    "dev": 1000,
    "pro": 10000,
}

# Simple request counter by IP (in production use Redis)
_request_counts: dict[str, list[int]] = {}


def check_rate_limit(client_id: str, plan: str = "free") -> tuple[bool, int]:
    """Check rate limit. Returns (allowed, remaining)."""
    now = int(time.time())
    day_start = now - (now % 86400)

    if client_id not in _request_counts:
        _request_counts[client_id] = []

    # Clean old entries
    _request_counts[client_id] = [
        t for t in _request_counts[client_id] if t >= day_start
    ]

    limit = RATE_LIMITS.get(plan, 50)
    if len(_request_counts[client_id]) >= limit:
        return False, 0

    _request_counts[client_id].append(now)
    remaining = limit - len(_request_counts[client_id])
    return True, remaining


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Skip rate limiting on health check
    if request.url.path == "/health":
        return await call_next(request)

    client_id = request.client.host if request.client else "unknown"

    # Check X-Plan header for tier (in prod, validate this properly)
    plan = request.headers.get("X-Plan", "free").lower()
    if plan not in RATE_LIMITS:
        plan = "free"

    allowed, remaining = check_rate_limit(client_id, plan)

    if not allowed:
        return JSONResponse(
            status_code=429,
            content={
                "error": "Rate limit exceeded",
                "limit": RATE_LIMITS[plan],
                "plan": plan,
                "message": f"Free tier: {RATE_LIMITS['free']}/day. Upgrade to Dev ($14/mo) for {RATE_LIMITS['dev']}/day or Pro ($39/mo) for {RATE_LIMITS['pro']}/day.",
            },
        )

    response = await call_next(request)
    response.headers["X-RateLimit-Limit"] = str(RATE_LIMITS[plan])
    response.headers["X-RateLimit-Remaining"] = str(remaining)
    return response


# Mount routers
app.include_router(puzzle.router)
app.include_router(eval_route.router)


@app.get("/")
async def root():
    return {
        "name": "WOLFRAMITE",
        "tagline": "Chess puzzles rated 1800+ from any FEN position. Not an app. An API.",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "POST /api/v1/puzzle/from-position": "Get puzzle from FEN position",
            "GET /api/v1/puzzle/daily": "Today's daily puzzle",
            "POST /api/v1/eval/position": "Evaluate a FEN position",
            "GET /api/v1/openings/{name}": "Get opening by name or ECO code",
            "POST /api/v1/game/annotate": "Annotate a PGN game",
        },
        "pricing": {
            "free": f"{RATE_LIMITS['free']}/day",
            "dev": f"${14}/mo — {RATE_LIMITS['dev']}/day",
            "pro": f"${39}/mo — {RATE_LIMITS['pro']}/day",
        },
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
