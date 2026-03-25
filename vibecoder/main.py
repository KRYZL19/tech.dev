from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.session import router as session_router
from routes.review import router as review_router
from routes.patterns import router as patterns_router

app = FastAPI(
    title="VIBECODER",
    description="AI Coding Session Context Manager — Your AI coding assistant doesn't know what you were working on 4 hours ago. This fixes that.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(session_router)
app.include_router(review_router)
app.include_router(patterns_router)


@app.get("/")
async def root():
    return {
        "name": "VIBECODER",
        "hook": "Your AI coding assistant doesn't know what you were working on 4 hours ago. This fixes that.",
        "pricing": {
            "free": "50 requests/day",
            "dev": "$19/month",
            "pro": "$49/month",
        },
        "endpoints": [
            "POST /api/v1/session/start",
            "POST /api/v1/session/resume",
            "POST /api/v1/session/summary",
            "POST /api/v1/review/diff",
            "GET /api/v1/patterns/{lang}",
        ],
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
