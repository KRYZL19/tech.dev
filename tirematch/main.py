from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI(title="TIREMATCH", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


def parse_tire_size(size: str) -> dict:
    """Parse tire size string like '245/45R18' into components."""
    import re
    m = re.match(r'(\d+)/(\d+)R(\d+)', size)
    if not m:
        return {"error": "Invalid size. Use format: 245/45R18"}
    width_mm = int(m.group(1))
    aspect = int(m.group(2))
    rim_in = int(m.group(3))
    sidewall_in = (aspect / 100) * width_mm / 25.4
    diameter_in = 2 * sidewall_in + rim_in
    circumference_in = math.pi * diameter_in
    return {
        "size": size, "width_mm": width_mm, "aspect": aspect, "rim_diameter_in": rim_in,
        "sidewall_in": round(sidewall_in, 2), "tire_diameter_in": round(diameter_in, 2),
        "circumference_in": round(circumference_in, 2),
    }


def speedometer_error(original: str, new: str) -> dict:
    """Calculate speedometer error when switching tire sizes."""
    o = parse_tire_size(original)
    n = parse_tire_size(new)
    if "error" in o or "error" in n:
        return {"error": "invalid size format"}
    error_pct = (n["tire_diameter_in"] - o["tire_diameter_in"]) / o["tire_diameter_in"] * 100
    return {
        "original": original, "new": new,
        "original_diameter_in": o["tire_diameter_in"], "new_diameter_in": n["tire_diameter_in"],
        "diameter_error_percent": round(error_pct, 2),
        "speedometer_reading_vs_actual": f"{100 - error_pct:.1f}% accurate at 60mph",
        "actual_mph_at_speedometer_60": round(60 * (1 + error_pct/100), 1),
    }


def tire_load_index(load_index: int) -> dict:
    """Convert load index to actual load capacity in lbs."""
    # Load index: 75=387kg, 80=450kg, 85=530kg, 90=600kg, 95=690kg, 100=800kg, 105=925kg, 110=1060kg
    load_table = {75:387, 76:397, 77:408, 78:420, 79:430, 80:450, 81:462, 82:475, 83:487, 84:500, 85:530, 86:545, 87:560, 88:580, 89:600, 90:635, 91:650, 92:670, 93:685, 94:710, 95:735, 96:755, 97:775, 98:800, 99:825, 100:800, 101:825, 102:850, 103:875, 104:900, 105:925, 106:950, 107:975, 108:1000, 109:1030, 110:1060, 111:1080, 112:1120, 113:1160, 114:1180, 115:1210}
    load_kg = load_table.get(load_index, load_table[max(k for k in load_table if k <= load_index)])
    return {"load_index": load_index, "load_lbs": round(load_kg * 2.20462, 0), "load_kg": load_kg}


def compare_tires(size_a: str, size_b: str) -> dict:
    """Compare two tire sizes — diameter, circumference, and Speedo effect."""
    a = parse_tire_size(size_a)
    b = parse_tire_size(size_b)
    if "error" in a or "error" in b:
        return {"error": "invalid size"}
    diam_diff = b["tire_diameter_in"] - a["tire_diameter_in"]
    return {
        "size_a": size_a, "size_b": size_b,
        "diameter_a_in": a["tire_diameter_in"], "diameter_b_in": b["tire_diameter_in"],
        "diameter_diff_in": round(diam_diff, 2),
        "compatible": abs(diam_diff) < 0.5,
        "note": "Compatible — within 0.5in diameter" if abs(diam_diff) < 0.5 else "Different diameters — check Speedo calibration",
    }


@app.get("/")
def read_root():
    return {"tirematch": "tire size API", "endpoints": ["/parse/{size}", "/compare", "/speedometer", "/load/{index}"]}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/v1/parse/{size}")
def parse_size(size: str):
    return parse_tire_size(size)


@app.get("/api/v1/compare")
def compare(size_a: str, size_b: str):
    return compare_tires(size_a, size_b)


@app.get("/api/v1/speedometer")
def speedo(original: str, new: str):
    return speedometer_error(original, new)


@app.get("/api/v1/load/{index}")
def load_index(index: int):
    return tire_load_index(index)
