"""
TIREMATCH API — Vehicle Tire Fitment & Compatibility
"245/45R18 on a 1998 Honda Civic will rub. One API call tells you before you buy."

FastAPI backend for tire size validation and wheel fitment.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

from routes.fitment import router as fitment_router
from routes.sizing import router as sizing_router

app = FastAPI(
    title="TIREMATCH API",
    description="Vehicle tire fitment and compatibility checking. "
                "Know if a tire fits before you buy — no more rubbing, no more guessing.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS — allow all for API consumers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_timing_header(request: Request, call_next):
    """Add X-Response-Time header to all responses."""
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = (time.perf_counter() - start) * 1000
    response.headers["X-Response-Time-Ms"] = f"{elapsed:.1f}"
    return response


# Include routers
app.include_router(fitment_router)
app.include_router(sizing_router)


@app.get("/", tags=["health"])
def root():
    """API root — returns basic info and hook."""
    return {
        "name": "TIREMATCH API",
        "version": "1.0.0",
        "hook": "245/45R18 on a 1998 Honda Civic will rub. One API call tells you before you buy.",
        "docs": "/docs",
        "endpoints": {
            "vehicle": "GET /api/v1/vehicle/{year}/{make}/{model}",
            "tire_compare": "POST /api/v1/tire/compare",
            "wheel_fitment": "POST /api/v1/wheel/fitment",
            "size_parse": "GET /api/v1/size/{tire_size}",
        },
        "pricing": {
            "free": "100 requests/day",
            "dev": "$14/month",
            "pro": "$39/month",
        },
    }


@app.get("/health", tags=["health"])
def health():
    """Health check endpoint."""
    return {"status": "healthy", "service": "tirematch-api"}


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error_code": "INTERNAL_ERROR"},
    )
