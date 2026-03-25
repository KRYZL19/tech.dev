from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import design, permit

app = FastAPI(
    title="SEPTICODE",
    description="Septic System Design Validator API — Calculate percolation rates, size systems, and generate permit checklists instantly.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(design.router)
app.include_router(permit.router)


@app.get("/")
async def root():
    return {
        "name": "SEPTICODE",
        "version": "1.0.0",
        "tagline": "Perc tests are the #1 reason rural property deals fall through. This API does it in 3 seconds.",
        "docs": "/docs",
        "endpoints": {
            "percolate": "POST /api/v1/percolate",
            "system_size": "POST /api/v1/system/size",
            "soil_data": "GET /api/v1/permit/soil/{county_name}",
            "permit_checklist": "POST /api/v1/permit/checklist",
        },
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
