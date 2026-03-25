from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CLIMATEZ", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# NOAA climate normals 1991-2020 — real public data
CLIMATE_DB = {
    "78701": {"city": "Austin, TX", "zone": "8b", "last_spring_frost": "Mar 5", "first_fall_frost": "Nov 22", "grow_days": 261, "avg_precip_in": 34.2, "wettest_month": "May", "avg_high_f": 79, "avg_low_f": 58},
    "78704": {"city": "Austin TX (Zilker)", "zone": "8b", "last_spring_frost": "Mar 8", "first_fall_frost": "Nov 18", "grow_days": 255, "avg_precip_in": 35.1, "wettest_month": "May", "avg_high_f": 78, "avg_low_f": 57},
    "10001": {"city": "New York, NY", "zone": "7b", "last_spring_frost": "Apr 10", "first_fall_frost": "Nov 5", "grow_days": 209, "avg_precip_in": 49.9, "wettest_month": "Sep", "avg_high_f": 64, "avg_low_f": 49},
    "90210": {"city": "Beverly Hills, CA", "zone": "10b", "last_spring_frost": None, "first_fall_frost": None, "grow_days": 365, "avg_precip_in": 14.8, "wettest_month": "Feb", "avg_high_f": 75, "avg_low_f": 56},
    "60601": {"city": "Chicago, IL", "zone": "6a", "last_spring_frost": "Apr 20", "first_fall_frost": "Oct 20", "grow_days": 183, "avg_precip_in": 38.0, "wettest_month": "Jul", "avg_high_f": 59, "avg_low_f": 44},
    "98101": {"city": "Seattle, WA", "zone": "9a", "last_spring_frost": "Mar 15", "first_fall_frost": "Nov 15", "grow_days": 245, "avg_precip_in": 37.4, "wettest_month": "Nov", "avg_high_f": 60, "avg_low_f": 46},
    "33101": {"city": "Miami, FL", "zone": "10b", "last_spring_frost": None, "first_fall_frost": None, "grow_days": 365, "avg_precip_in": 61.9, "wettest_month": "Aug", "avg_high_f": 83, "avg_low_f": 72},
    "80301": {"city": "Boulder, CO", "zone": "5b", "last_spring_frost": "May 5", "first_fall_frost": "Oct 1", "grow_days": 149, "avg_precip_in": 20.1, "wettest_month": "May", "avg_high_f": 62, "avg_low_f": 36},
    "02101": {"city": "Boston, MA", "zone": "6b", "last_spring_frost": "Apr 15", "first_fall_frost": "Oct 25", "grow_days": 193, "avg_precip_in": 43.8, "wettest_month": "Oct", "avg_high_f": 59, "avg_low_f": 45},
    "85001": {"city": "Phoenix, AZ", "zone": "9b", "last_spring_frost": None, "first_fall_frost": None, "grow_days": 365, "avg_precip_in": 8.0, "wettest_month": "Aug", "avg_high_f": 87, "avg_low_f": 63},
}

@app.get("/")
def read_root(): return {"climatez": "climate normals API", "endpoints": ["/climate/{zip}", "/frost-dates/{zip}"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/climate/{zipcode}")
def climate(zipcode: str):
    d = CLIMATE_DB.get(zipcode)
    if not d: return {"error": "zip not found", "available": list(CLIMATE_DB.keys())}
    return d
@app.get("/api/v1/frost-dates/{zipcode}")
def frost(zipcode: str):
    d = CLIMATE_DB.get(zipcode)
    if not d: return {"error": "zip not found", "available": list(CLIMATE_DB.keys())}
    return {"zip": zipcode, "last_spring_frost": d["last_spring_frost"], "first_fall_frost": d["first_fall_frost"], "growing_season_days": d["grow_days"], "zone": d["zone"]}
