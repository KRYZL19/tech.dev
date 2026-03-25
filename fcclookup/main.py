from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FCCLOOKUP", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

CALLSIGNS = {
    "W1ABC": {"callsign": "W1ABC", "class": "Amateur Extra", "frn": "0012345678", "grid": "FN31", "name": "John Smith", "address": "Boston, MA", "expiration": "2031-06-15", "privileges": "all bands, all modes", "since": 2015},
    "K2XYZ": {"callsign": "K2XYZ", "class": "General", "frn": "0023456789", "grid": "FN20", "name": "Jane Doe", "address": "New York, NY", "expiration": "2030-03-20", "privileges": "HF + 6m/2m", "since": 2019},
    "N3LMN": {"callsign": "N3LMN", "class": "Technician", "frn": "0034567890", "grid": "FM19", "name": "Bob Wilson", "address": "Philadelphia, PA", "expiration": "2029-11-01", "privileges": "VHF/UHF + 10m", "since": 2021},
    "KK4PQR": {"callsign": "KK4PQR", "class": "Amateur Extra", "frn": "0045678901", "grid": "EL87", "name": "Alice Brown", "address": "Miami, FL", "expiration": "2032-01-10", "privileges": "all bands, all modes", "since": 2012},
    "AI6ST": {"callsign": "AI6ST", "class": "General", "frn": "0056789012", "grid": "CM87", "name": "Charlie Green", "address": "San Francisco, CA", "expiration": "2030-09-05", "privileges": "HF + 6m/2m", "since": 2017},
}

BANDS = {
    "160m": {"freq_mhz": "1.8-2.0", "modes": "CW, Phone, Digital", "license_class": "Extra: full, General: 2 sections", "us_license_required": "All classes"},
    "80m": {"freq_mhz": "3.5-4.0", "modes": "CW, Phone, RTTY, Digital", "license_class": "Extra: full, General: full, Tech: limited", "us_license_required": "Technician+"},
    "40m": {"freq_mhz": "7.0-7.3", "modes": "CW, Phone, RTTY, Digital", "license_class": "Extra: full, General: full, Tech: limited", "us_license_required": "Technician+"},
    "20m": {"freq_mhz": "14.0-14.35", "modes": "CW, Phone, RTTY, Digital", "license_class": "All classes", "us_license_required": "All classes"},
    "15m": {"freq_mhz": "21.0-21.45", "modes": "CW, Phone, RTTY, Digital", "license_class": "All classes", "us_license_required": "All classes"},
    "10m": {"freq_mhz": "28.0-29.7", "modes": "CW, Phone, FM, Digital", "license_class": "All classes", "us_license_required": "All classes"},
    "6m": {"freq_mhz": "50-54", "modes": "CW, Phone, FM, Digital", "license_class": "All classes", "us_license_required": "All classes"},
    "2m": {"freq_mhz": "144-148", "modes": "CW, Phone, FM, Digital", "license_class": "All classes", "us_license_required": "All classes"},
}

@app.get("/")
def read_root():
    return {"fcclookup": "ham radio callsign + band API", "endpoints": ["/callsign/{call}", "/bands", "/grid/{grid}"]}

@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}

@app.get("/api/v1/callsign/{call}")
def callsign(call: str):
    c = CALLSIGNS.get(call.upper())
    if not c:
        return {"error": "callsign not found", "available": list(CALLSIGNS.keys()), "note": "demo data — enter real callsign"}
    return c

@app.get("/api/v1/bands")
def bands():
    return {"bands": BANDS}

@app.get("/api/v1/grid/{grid}")
def grid_lookup(grid: str):
    # Convert 4 or 6 character Maidenhead grid to lat/lon
    grid = grid.upper()
    if len(grid) < 4 or len(grid) > 6:
        return {"error": "grid must be 4 or 6 characters (e.g. FN31 or FN31pr)"}
    lon = (ord(grid[0]) - 65) * 20 - 180
    lat = (ord(grid[2]) - 65) * 10 - 90
    return {"grid": grid, "center_lat": round(lat + 2.5, 3), "center_lon": round(lon + 10, 3), "note": "demo grid lookup"}
