"""CARBONCALC API — Carbon Footprint for Shipping & Logistics."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import HealthResponse
from routes import shipping, travel, supply_chain

app = FastAPI(
    title="CARBONCALC API",
    description=(
        "A container from Shanghai to Rotterdam emits 1.5 tons of CO2. "
        "Your logistics team doesn't know this because there's no simple API.\n\n"
        "**Pricing:** Free: 100 req/day · Dev $19/mo · Pro $59/mo"
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(shipping.router)
app.include_router(travel.router)
app.include_router(supply_chain.router)


@app.get("/", tags=["info"])
def root():
    return {
        "name": "CARBONCALC API",
        "version": "1.0.0",
        "tagline": "Carbon footprint for shipping — made simple.",
        "docs": "/docs",
    }


@app.get("/health", response_model=HealthResponse, tags=["info"])
def health():
    return HealthResponse(status="ok", version="1.0.0")
