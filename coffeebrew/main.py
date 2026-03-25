"""
COFFEEBREW — Coffee Extraction Calculator API

Hook: "21g at 200°F, 2:30, 1.42% TDS. Your refractometer says TDS is off. Here's why."

A precision coffee brewing API that calculates extraction metrics,
optimizes dosing parameters, and provides bean/method intelligence.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import extraction, dosing

app = FastAPI(
    title="COFFEEBREW",
    description="Coffee Extraction Calculator API — precision brewing intelligence",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS for all origins (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(extraction.router)
app.include_router(dosing.router)


@app.get("/", tags=["health"])
def root():
    """API root with info."""
    return {
        "name": "COFFEEBREW",
        "tagline": "21g at 200°F, 2:30, 1.42% TDS. Your refractometer says TDS is off. Here's why.",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", tags=["health"])
def health():
    """Health check."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
