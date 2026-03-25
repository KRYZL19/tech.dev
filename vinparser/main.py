from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="VINPARSER", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


def parse_vin(vin: str) -> dict:
    """Parse a 17-character VIN. Returns decoded components + validation."""
    if len(vin) != 17:
        return {"error": "VIN must be exactly 17 characters", "length": len(vin)}
    vin = vin.upper()
    # WMI (world manufacturer identifier) — positions 1-3
    wmi = vin[:3]
    # VDS (vehicle descriptor section) — positions 4-9
    vds = vin[3:9]
    # VIS (vehicle identifier section) — positions 10-17
    vis = vin[9:]
    # Check digit (position 9) — mod 11 algorithm
    transliteration = {chr(i): (i - 55) if i >= 65 else (i - 48) for i in range(48, 58)} | {chr(i): i - 55 for i in range(65, 90) if chr(i) not in 'IOSQX'}
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(transliteration.get(c, 0) * w for c, w in zip(vin, weights))
    check_digit = str(total % 11) if total % 11 < 10 else 'X'
    valid = vin[8] == check_digit
    # Country from position 1
    country_map = {"1": "US", "2": "Canada", "3": "Mexico", "J": "Japan", "K": "Korea", "L": "China", "S": "UK", "V": "France/Spain", "W": "Germany", "Y": "Sweden/Finland", "Z": "Italy"}
    country = country_map.get(vin[0], "unknown")
    # Manufacturer from position 1-2
    # Year from position 10 (model year encoding)
    year_codes = {year: chr(ord('A') + (year - 2010) % 26) for year in range(2010, 2031)}
    year_map = {v: k for k, v in year_codes.items()}
    # Model year (position 10)
    model_year = year_map.get(vis[0], year_map.get(chr(ord(vis[0]) - 1) if vis[0] > 'A' else 'Z', 2020))
    # Plant code (position 11)
    # Serial (positions 12-17)
    return {
        "vin": vin, "valid": valid, "check_digit": check_digit,
        "wmi": wmi, "vds": vds, "vis": vis,
        "country": country,
        "model_year": model_year,
        "plant_code": vis[1],
        "serial_number": vis[2:],
        "position_meanings": {
            "1-3": "World Manufacturer ID (WMI)",
            "4-8": "Vehicle attributes (VDS)",
            "9": "Check digit",
            "10": f"Model year ({model_year})",
            "11": "Assembly plant",
            "12-17": "Production sequence number"
        }
    }


def decode_vehicle(vin: str) -> dict:
    """Decode known VINs to make/model/engine."""
    known = {
        "1HGCM82633A004352": {"year": 2003, "make": "Honda", "model": "Accord", "trim": "EX V6", "engine": "3.0L V6", "drivetrain": "FWD", "transmission": "5AT"},
        "WVWZZZ3CZWE123456": {"year": 2022, "make": "Volkswagen", "model": "Golf GTI", "trim": "Autobahn", "engine": "2.0L Turbo I4", "drivetrain": "FWD", "transmission": "6MT"},
        "5YJSA1DG9DFP14605": {"year": 2013, "make": "Tesla", "model": "Model S", "trim": "P85", "engine": "Electric 416hp", "drivetrain": "AWD", "transmission": "Single-speed"},
        "1FMCU0G62DUA12345": {"year": 2013, "make": "Ford", "model": "Escape", "trim": "SE", "engine": "1.6L I4 Turbo", "drivetrain": "FWD", "transmission": "6AT"},
        "2T1BURHE0JC123456": {"year": 2018, "make": "Toyota", "model": "Corolla", "trim": "SE", "engine": "2.0L I4", "drivetrain": "FWD", "transmission": "CVT"},
    }
    result = parse_vin(vin)
    if result.get("error"):
        return result
    if vin.upper() in known:
        result["vehicle"] = known[vin.upper()]
    else:
        result["vehicle"] = {"note": "demo VIN — substitute a real VIN for actual data"}
    return result


@app.get("/")
def read_root():
    return {"vinparser": "VIN decode API", "endpoints": ["/parse/{vin}", "/decode/{vin}"]}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/v1/parse/{vin}")
def parse(vin: str):
    return parse_vin(vin)


@app.get("/api/v1/decode/{vin}")
def decode(vin: str):
    return decode_vehicle(vin)
