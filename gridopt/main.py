from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routes import tariffs, schedule, carbon

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tariffs.router, prefix=settings.api_prefix)
app.include_router(schedule.router, prefix=settings.api_prefix)
app.include_router(carbon.router, prefix=settings.api_prefix)


@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy", "service": settings.app_name, "version": settings.version}


@app.get("/")
async def root():
    return {
        "service": settings.app_name,
        "version": settings.version,
        "docs": "/docs",
    }
