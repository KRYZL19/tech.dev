from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HVACCALC", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

ZONES = {"1": {"name": "Zone 1", "heat_db": 30, "cool_db": 95}, "2": {"name": "Zone 2", "heat_db": 10, "cool_db": 100}, "3": {"name": "Zone 3", "heat_db": 5, "cool_db": 95}, "4": {"name": "Zone 4", "heat_db": 0, "cool_db": 93}, "5": {"name": "Zone 5", "heat_db": -10, "cool_db": 91}, "6": {"name": "Zone 6", "heat_db": -20, "cool_db": 89}, "7": {"name": "Zone 7", "heat_db": -30, "cool_db": 86}, "8": {"name": "Zone 8", "heat_db": -40, "cool_db": 83}}

def load(sqft: float, ceil_ft: float, zone: str, r: float = 13) -> dict:
    z = ZONES.get(zone, ZONES["4"])
    cool_btu = (sqft / r) * (z["cool_db"] - 75) * 1.08
    heat_btu = (sqft / r) * (75 - z["heat_db"]) * 1.08
    tons = cool_btu / 12000
    return {"sqft": sqft, "zone": zone, "cooling_btu": round(cool_btu, 0), "cooling_tons": round(tons, 1), "heating_btu": round(heat_btu, 0), "oversized_warning": "reduce 10-15%" if tons > 5 else None}

@app.get("/")
def read_root(): return {"hvaccalc": "HVAC Manual J sizing", "endpoints": ["/load", "/zones"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/load")
def calc_load(sqft: float, ceiling_ft: float = 8, zone: str = "4", r_value: float = 13): return load(sqft, ceiling_ft, zone, r_value)
@app.get("/api/v1/zones")
def zones(): return {"zones": ZONES}
