"""
BANDPASS — Audio EQ Room Correction API

Room EQ Wizard is free but takes 30 minutes. This returns your EQ settings in one call.

Free: 50 requests/day
Dev: $14/month - unlimited requests
Pro: $39/month - priority + advanced features
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from collections import defaultdict
import time

from routes import eq, room
from models.schemas import RoomEQInput, RoomEQOutput

# Simple in-memory rate limiting
rate_limit_storage = defaultdict(list)
RATE_LIMIT_FREE = 50
RATE_LIMIT_WINDOW = timedelta(days=1)


def check_rate_limit(request: Request) -> dict:
    """Check rate limit for incoming request."""
    client_ip = request.client.host if request.client else "unknown"
    now = datetime.utcnow()
    
    # Clean old entries
    rate_limit_storage[client_ip] = [
        ts for ts in rate_limit_storage[client_ip]
        if now - ts < RATE_LIMIT_WINDOW
    ]
    
    current_count = len(rate_limit_storage[client_ip])
    remaining = max(0, RATE_LIMIT_FREE - current_count)
    
    if current_count >= RATE_LIMIT_FREE:
        return {
            "allowed": False,
            "remaining": 0,
            "limit": RATE_LIMIT_FREE,
            "reset": (now + RATE_LIMIT_WINDOW).isoformat()
        }
    
    # Record this request
    rate_limit_storage[client_ip].append(now)
    
    return {
        "allowed": True,
        "remaining": remaining - 1,
        "limit": RATE_LIMIT_FREE,
        "reset": (now + RATE_LIMIT_WINDOW).isoformat()
    }


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events."""
    print("🎛️ BANDPASS API starting up...")
    print("   Room EQ Wizard takes 30 minutes. We do it in one call.")
    yield
    print("👋 BANDPASS API shutting down...")


app = FastAPI(
    title="BANDPASS",
    description="## Audio EQ Room Correction API\n\n**Room EQ Wizard is free but takes 30 minutes. This returns your EQ settings in one call.**\n\n### Features\n- Room mode calculation (axial, tangential, oblique)\n- Speaker profile database (15 popular monitors)\n- Automated EQ settings generation\n- First reflection point analysis\n\n### Pricing\n| Tier | Price | Requests |\n|------|-------|----------|\n| Free | $0 | 50/day |\n| Dev | $14/mo | Unlimited |\n| Pro | $39/mo | Priority + advanced |\n\n### Supported Speakers\nYamaha HS8, JBL 308P, Adam A7X, KRK Rokit 8, PreSonus Eris E8, Genelec 8030,\nNeumann KH80, Focal Alpha 65, and more...",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    """Apply rate limiting to all requests."""
    # Skip rate limiting for docs and health checks
    if request.url.path in ["/", "/docs", "/redoc", "/health", "/openapi.json"]:
        return await call_next(request)
    
    # Check rate limit
    result = check_rate_limit(request)
    
    if not result["allowed"]:
        return JSONResponse(
            status_code=429,
            content={
                "error": "Rate limit exceeded",
                "message": f"Free tier limited to {RATE_LIMIT_FREE} requests per day",
                "upgrade_options": {
                    "dev": {"price": "$14/month", "link": "/pricing"},
                    "pro": {"price": "$39/month", "link": "/pricing"}
                },
                "reset": result["reset"]
            }
        )
    
    response = await call_next(request)
    response.headers["X-RateLimit-Limit"] = str(result["limit"])
    response.headers["X-RateLimit-Remaining"] = str(result["remaining"])
    
    return response


# Include routers
app.include_router(room.router)
app.include_router(eq.router)


@app.get("/")
def root():
    """API root - redirect to docs."""
    return {
        "name": "BANDPASS",
        "tagline": "Room EQ Wizard is free but takes 30 minutes. This returns your EQ settings in one call.",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "BANDPASS",
        "timestamp": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
