from fastapi import FastAPI
from routes import search, trial

app = FastAPI(
    title="CLINICALTRL",
    description="Clinical Trial Results Database API",
    version="1.0.0"
)

app.include_router(search.router)
app.include_router(trial.router)

@app.get("/")
def root():
    return {
        "name": "CLINICALTRL",
        "version": "1.0.0",
        "description": "Clinical Trial Results Database API",
        "hook": "Find all phase 3 trials for drug X with positive results. One query."
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
