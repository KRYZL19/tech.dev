from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import codes, adoptions, permits

app = FastAPI(
    title="US Building Code Cross-Reference API",
    description="What version of the IBC does your city use? What did they adopt and when?",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(codes.router)
app.include_router(adoptions.router)
app.include_router(permits.router)


@app.get("/")
def root():
    return {
        "name": "US Building Code Cross-Reference API",
        "version": "1.0.0",
        "hook": "What version of the IBC does your city use? What did they adopt and when?",
        "endpoints": {
            "GET /api/v1/adoption/{state}/{city}": "City code adoption info",
            "GET /api/v1/code/{code_name}/{version}/section/{section}": "Code section text",
            "GET /api/v1/state/{state}/codes": "State code adoption",
            "POST /api/v1/permit/checklist": "Permit checklist for project",
            "GET /api/v1/ada/requirements/{building_type}": "ADA requirements by occupancy",
        },
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
