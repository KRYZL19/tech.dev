"""
STORMTRACK — Hurricane & Historical Storm Database API
Hook: "What's the hurricane history for this coastal address? 1950-2025. One query."
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.storms import router as storms_router
from routes.analysis import router as analysis_router

app = FastAPI(
    title="STORMTRACK",
    description="Hurricane & Historical Storm Database API — 10 major storms, 1992–2024",
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

app.include_router(storms_router)
app.include_router(analysis_router)


@app.get("/", tags=["health"])
def root():
    return {
        "service": "STORMTRACK",
        "version": "1.0.0",
        "status": "operational",
        "storms": 10,
        "year_range": "1992–2024",
        "hook": "What's the hurricane history for this coastal address? 1950-2025. One query.",
        "docs": "/docs",
    }


@app.get("/health", tags=["health"])
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
