from fastapi import FastAPI
from routes import search, patent

app = FastAPI(
    title="PATENTLOOK",
    description="Search 50 years of US patents by technical claim, not just keyword.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(search.router)
app.include_router(patent.router)


@app.get("/", tags=["health"])
def root():
    return {"status": "online", "service": "PATENTLOOK", "version": "1.0.0"}


@app.get("/health", tags=["health"])
def health():
    return {"status": "healthy"}
