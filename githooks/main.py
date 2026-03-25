from fastapi import FastAPI
from routes import generate, validate

app = FastAPI(
    title="GITHOOKS API",
    description="Pre-commit Hook Generator — Tell it your tech stack. Get pre-commit hooks that actually catch things.",
    version="1.0.0",
)

app.include_router(generate.router)
app.include_router(validate.router)


@app.get("/health")
async def health():
    return {"status": "ok", "service": "githooks"}
