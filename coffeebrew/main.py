from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI(title="COFFEEBREW", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def extraction_yield(coffee_g: float, water_ml: float, tds_percent: float) -> dict:
    dissolved_solids = water_ml * (tds_percent / 100)
    yield_pct = (dissolved_solids / coffee_g) * 100
    return {"yield_pct": round(yield_pct, 2), "dissolved_solids_g": round(dissolved_solids, 2), "status": "under" if yield_pct < 18 else "over" if yield_pct > 22 else "optimal"}

def ratio_check(coffee_g: float, water_ml: float) -> dict:
    ratio = water_ml / coffee_g
    return {"ratio": f"1:{round(ratio, 1)}", "assessment": "weak" if ratio > 18 else "strong" if ratio < 12 else "optimal"}

@app.get("/")
def read_root(): return {"coffeebrew": "coffee extraction API", "endpoints": ["/extract", "/ratio"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/extract")
def extract(coffee_g: float, water_ml: float, tds_percent: float):
    result = extraction_yield(coffee_g, water_ml, tds_percent)
    result["ratio"] = ratio_check(coffee_g, water_ml)
    return result
@app.get("/api/v1/ratio")
def ratio(coffee_g: float, water_ml: float):
    return ratio_check(coffee_g, water_ml)
