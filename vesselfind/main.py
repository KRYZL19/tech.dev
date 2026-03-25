from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="VESSELFIND", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# USCG Vessel Documentation — public via uscg.mil
VESSELS = {
    "VESSEL-2024-00047": {"vessel_id": "VESSEL-2024-00047", "name": "SEA RAY 310", "imo": "9212345", "uscg_num": "1234567", "hailing_port": "St. Petersburg, FL", "owner": "J. Martinez", "owner_history": ["M. Johnson (2019-2022)", "T. Williams (2016-2019)"], "lien": "YES", "lien_amount": 22000, "lien_holder": "US Bank", "vessel_type": "Motor Yacht", "length_ft": 31, "hull_material": "Fiberglass", "year_built": 2019, "hull_id": "XYY12345M19B", "documentation_status": "Active"},
    "VESSEL-2024-00102": {"vessel_id": "VESSEL-2024-00102", "name": "YAMAHA 242X", "imo": None, "uscg_num": "9876543", "hailing_port": "Miami, FL", "owner": "S. Rodriguez", "owner_history": ["S. Rodriguez (2021-present)"], "lien": "NO", "lien_amount": None, "lien_holder": None, "vessel_type": "Jet Boat", "length_ft": 24, "hull_material": "Fiberglass", "year_built": 2021, "hull_id": "YAM12345M21A", "documentation_status": "Active"},
    "VESSEL-2023-00888": {"vessel_id": "VESSEL-2023-00888", "name": "JEANNEAU 379", "imo": "8912345", "uscg_num": "4567890", "hailing_port": "Charleston, SC", "owner": "K. Thompson", "owner_history": ["K. Thompson (2020-present)", "R. Davis (2017-2020)"], "lien": "YES", "lien_amount": 85000, "lien_holder": "Bank of America", "vessel_type": "Sailboat", "length_ft": 37, "hull_material": "Fiberglass", "year_built": 2017, "hull_id": "JEAN12345L17A", "documentation_status": "Active"},
}

@app.get("/")
def read_root(): return {"vesselfind": "USCG vessel documentation API", "endpoints": ["/vessel/{vessel_id}", "/search"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/vessel/{vessel_id}")
def vessel(vessel_id: str):
    v = VESSELS.get(vessel_id)
    if not v: return {"error": "vessel not found", "available": list(VESSELS.keys()), "note": "demo data"}
    return v
@app.get("/api/v1/search")
def search(owner: str = None, vessel_type: str = None):
    results = list(VESSELS.values())
    if owner: results = [v for v in results if owner.lower() in v["owner"].lower()]
    if vessel_type: results = [v for v in results if v["vessel_type"].lower() == vessel_type.lower()]
    return {"count": len(results), "vessels": results}
