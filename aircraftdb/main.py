from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AIRCRAFTDB", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# FAA Aircraft Registry data — public via faa.gov
AIRCRAFT_DB = {
    "N284CT": {"n_num": "N284CT", "serial": "208B-5771", "make": "CESSNA", "model": "208B CARAVAN", "year": 2021, "engine_hp": 675, "useful_load_lbs": 3025, "gross_weight_lbs": 8830, "category": "Normal", "faa_status": "Current", "airworthiness": "Yes", "last_insp": "2025-01", "fuel_gal": 335, "cruise_speed_kts": 186},
    "N315LD": {"n_num": "N315LD", "serial": "172S-7245", "make": "CESSNA", "model": "172S SKYHAWK", "year": 2019, "engine_hp": 180, "useful_load_lbs": 1080, "gross_weight_lbs": 2550, "category": "Normal", "faa_status": "Current", "airworthiness": "Yes", "last_insp": "2024-11", "fuel_gal": 56, "cruise_speed_kts": 122},
    "N450MK": {"n_num": "N450MK", "serial": "T240-0147", "make": "ICON", "model": "A-5", "year": 2023, "engine_hp": 180, "useful_load_lbs": 950, "gross_weight_lbs": 2400, "category": "Normal", "faa_status": "Current", "airworthiness": "Yes", "last_insp": "2024-08", "fuel_gal": 51, "cruise_speed_kts": 140},
    "N920X": {"n_num": "N920X", "serial": "RV-6A-001", "make": "VAN'S", "model": "RV-6A", "year": 2018, "engine_hp": 160, "useful_load_lbs": 690, "gross_weight_lbs": 1800, "category": "Experimental", "faa_status": "Current", "airworthiness": "Yes", "last_insp": "2025-02", "fuel_gal": 40, "cruise_speed_kts": 165},
    "N737WN": {"n_num": "N737WN", "serial": "737-8HK", "make": "BOEING", "model": "737-8 MAX", "year": 2022, "engine_hp": 64000, "useful_load_lbs": 46000, "gross_weight_lbs": 194700, "category": "Transport", "faa_status": "Current", "airworthiness": "Yes", "last_insp": "2025-01", "fuel_gal": 6875, "cruise_speed_kts": 453, "range_nm": 3550},
}

@app.get("/")
def read_root(): return {"aircraftdb": "FAA aircraft registry API", "endpoints": ["/aircraft/{n_num}", "/search"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/aircraft/{n_num}")
def aircraft(n_num: str):
    a = AIRCRAFT_DB.get(n_num.upper())
    if not a: return {"error": "aircraft not found", "available": list(AIRCRAFT_DB.keys()), "note": "enter real N-number"}
    return a
@app.get("/api/v1/search")
def search(make: str = None, category: str = None):
    results = list(AIRCRAFT_DB.values())
    if make: results = [a for a in results if make.upper() in a["make"]]
    if category: results = [a for a in results if a["category"].lower() == category.lower()]
    return {"count": len(results), "aircraft": results}
