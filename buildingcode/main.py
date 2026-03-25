from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BUILDINGCODE", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

CODES = {
    "austin_tx": {"city": "Austin, TX", "code": "IBC 2021", "adopted": "March 2022", "amendments": 7, "permit_types": ["residential", "commercial", "mechanical", "electrical", "plumbing"], "zoning_districts": 12, "setback_residential_ft": 5, "max_height_ft": 35},
    "los_angeles_ca": {"city": "Los Angeles, CA", "code": "IBC 2022", "adopted": "Jan 2024", "amendments": 15, "permit_types": ["residential", "commercial", "fire", "hazardous materials"], "zoning_districts": 59, "setback_residential_ft": 5, "max_height_ft": 45},
    "new_york_ny": {"city": "New York, NY", "code": "NYC Building Code 2022", "adopted": "July 2022", "amendments": 22, "permit_types": ["new building", "alteration", "demolition", "equipment"], "zoning_districts": 3, "setback_residential_ft": 10, "max_height_ft": 210},
    "chicago_il": {"city": "Chicago, IL", "code": "IBC 2021", "adopted": "Nov 2022", "amendments": 11, "permit_types": ["new construction", "renovation", "electrical", "plumbing"], "zoning_districts": 9, "setback_residential_ft": 5, "max_height_ft": 80},
    "denver_co": {"city": "Denver, CO", "code": "IBC 2021", "adopted": "Aug 2023", "amendments": 9, "permit_types": ["residential", "commercial", "accessory structure"], "zoning_districts": 26, "setback_residential_ft": 5, "max_height_ft": 35},
}

@app.get("/")
def read_root(): return {"buildingcode": "IBC building code lookup", "endpoints": ["/code/{city}", "/search"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/code/{city}")
def code(city: str):
    c = CODES.get(city.lower().replace(" ","_"))
    if not c: return {"error": "city not found", "available": list(CODES.keys())}
    return c
@app.get("/api/v1/search")
def search(code_version: str = None):
    r = list(CODES.values())
    if code_version: r = [c for c in r if c["code"].startswith("IBC") and code_version in c["code"]]
    return {"count": len(r), "cities": r}
