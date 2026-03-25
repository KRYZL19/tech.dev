from fastapi import FastAPI
from routes import demographics, comps

app = FastAPI(
    title="NEIGHBORHOODDB",
    description="Demographics & Real Estate Comp Database — Average days on market, price per sqft trend, median rent by neighborhood, updated monthly.",
    version="1.0.0"
)

app.include_router(demographics.router)
app.include_router(comps.router)


@app.get("/")
def root():
    return {
        "name": "NEIGHBORHOODDB",
        "version": "1.0.0",
        "description": "Demographics & Real Estate Comp Database",
        "endpoints": {
            "demographics": "GET /api/v1/demographics/{zipcode}",
            "comps": "GET /api/v1/comps/{zipcode}",
            "trend": "GET /api/v1/trend/{zipcode}?years={n}",
            "investment_score": "POST /api/v1/investment/score"
        }
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
