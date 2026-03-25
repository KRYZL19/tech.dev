from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.vin import router as vin_router
from routes.recall import router as model_router

app = FastAPI(
    title="VINPARSER API",
    description="Motorcycle VIN Decoder API — The VIN on that 2019 vs 2021 MT-09 looks identical. One character tells you everything.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vin_router)
app.include_router(model_router)


@app.get("/")
async def root():
    return {
        "name": "VINPARSER API",
        "version": "1.0.0",
        "tagline": "Motorcycle VIN Decoder — One character tells you everything.",
        "docs": "/docs",
        "endpoints": {
            "decode": "POST /api/v1/vin/decode",
            "validate": "POST /api/v1/vin/validate",
            "model_specs": "GET /api/v1/model/{make}/{year}/{model}"
        },
        "pricing": {
            "free": "100 requests/day",
            "dev": "$14/month",
            "pro": "$39/month"
        }
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
