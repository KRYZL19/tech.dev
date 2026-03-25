from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI(title="DRONEWING", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def haversine_mi(lat1, lon1, lat2, lon2):
    R = 3959
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

def airspace_check(lat: float, lon: float, alt_ft: int) -> dict:
    airports = {
        "LAX": (33.9425, -118.4081), "JFK": (40.6413, -73.7781), "ORD": (41.9742, -87.9073),
        "DFW": (32.8998, -97.0403), "DEN": (39.8561, -104.6737), "ATL": (33.6407, -84.4277),
        "SFO": (37.6213, -122.3790), "MIA": (25.7959, -80.2870), "SEA": (47.4502, -122.3088),
        "BOS": (42.3656, -71.0096), "PHX": (33.4373, -112.0078), "IAH": (29.9902, -95.3368),
    }
    for airport, (a_lat, a_lon) in airports.items():
        dist = haversine_mi(lat, lon, a_lat, a_lon)
        if dist < 5:
            return {"airport": airport, "distance_mi": round(dist, 1), "airspace": "B", "laanc_required": True, "max_altitude_ft": 100, "authorization": f"LAANC cell {airport[:3]}-UAS-??-??"}
        elif dist < 30:
            return {"airport": airport, "distance_mi": round(dist, 1), "airspace": "B", "laanc_required": True, "max_altitude_ft": 100}
    return {"airspace": "G", "laanc_required": False, "max_altitude_ft": 400, "note": "Class G — no authorization below 400ft AGL"}

@app.get("/")
def read_root(): return {"dronewing": "drone airspace API", "endpoints": ["/airspace/check", "/laanc/{cell_id}"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.post("/api/v1/airspace/check")
def check(lat: float, lon: float, altitude_ft: int = 150):
    return airspace_check(lat, lon, altitude_ft)
