"""
VESSELFIND — US Boat & Ship Registration Lookup API

Hook: "That boat has three owners and a lien against it. One API call tells you before you buy."

Endpoints
─────────
GET  /api/v1/vessel/{vessel_id}
     length_ft, beam_ft, hull_material, year, manufacturer, model,
     propulsion, documentation_number, lien_status, lien_holder

GET  /api/v1/vessel/{vessel_id}/history
     owner history, previous owners, dates of change, lien status

POST /api/v1/vessel/validate
     documentation_number → valid, vessel_id, status (active/cancelled/not_found)

GET  /api/v1/manufacturer/{mfr}
     all boats by manufacturer with common models

Run
---
    uvicorn main:app --reload --port 8765
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import vessel, registration

app = FastAPI(
    title="VESSELFIND",
    description='US Boat & Ship Registration Lookup — "That boat has three owners and a lien against it. One API call tells you before you buy."',
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vessel.router)
app.include_router(registration.router)


@app.get("/", tags=["health"])
def root():
    return {
        "service": "VESSELFIND",
        "tagline": "That boat has three owners and a lien against it. One API call tells you before you buy.",
        "version": "1.0.0",
        "endpoints": {
            "vessel_by_id": "GET /api/v1/vessel/{vessel_id}",
            "vessel_history": "GET /api/v1/vessel/{vessel_id}/history",
            "validate": "POST /api/v1/vessel/validate",
            "by_manufacturer": "GET /api/v1/manufacturer/{mfr}",
            "list_manufacturers": "GET /api/v1/manufacturer",
        },
    }


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8765, reload=True)
