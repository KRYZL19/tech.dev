from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SEPTICODER", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def drainfield_size(bedrooms: int, gal_per_day: int = 450, soil_percolation_min: int = 60) -> dict:
    """Size a drain field based on bedrooms and soil percolation.
    Standard: 120-150 sqft/gallon/day for conventional systems."""
    flow_gpd = bedrooms * gal_per_day
    # Loading rate based on percolation (NRL 89-3 table)
    if soil_percolation_min < 1:
        rate = 5.0  # very fast — limit loading
    elif soil_percolation_min <= 10:
        rate = 1.2
    elif soil_percolation_min <= 30:
        rate = 0.9
    elif soil_percolation_min <= 45:
        rate = 0.6
    elif soil_percolation_min <= 60:
        rate = 0.45
    elif soil_percolation_min <= 90:
        rate = 0.3
    else:
        rate = 0.2  # very slow — needs large field
    sqft_needed = max(flow_gpd * rate, bedrooms * 100)
    lines = int(math.ceil(sqft_needed / 100))
    return {
        "bedrooms": bedrooms, "flow_gpd": flow_gpd,
        "soil_percolation_min": soil_percolation_min,
        "loading_rate_sqft_per_gal": rate,
        "drainfield_sqft": round(sqft_needed, 1),
        "trenches_recommended": lines,
        "absorption_area_sqft": round(sqft_needed, 1),
        "tank_size_gallons": bedrooms * 300,
        "note": "verify with local health department — codes vary by state"
    }

@app.get("/")
def read_root():
    return {"septicoder": "septic system sizing API", "endpoints": ["/drainfield"]}

@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}

import math
@app.get("/api/v1/drainfield")
def drainfield(bedrooms: int, soil_percolation_min: int = 60, gal_per_bedroom: int = 450):
    return drainfield_size(bedrooms, gal_per_bedroom, soil_percolation_min)
