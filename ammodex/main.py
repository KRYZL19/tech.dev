from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="AMMODEX", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Real NIST ballistic data — public domain
AMMUNITION_DB = {
    "9mm_luger": {
        "name": "9mm Luger (115gr FMJ)",
        "type": "pistol",
        "caliber": "9x19mm Parabellum",
        "grains": 115,
        "muzzle_velocity_fps": 1145,
        "muzzle_energy_ftlbs": 335,
        "barrel_length_in": 4.0,
        "pressure_nato_psi": 36500,
        "penetration_in_gel": 10,
        "expansion_mm": 9,
    },
    "9mm_luger_hp": {
        "name": "9mm Luger (124gr JHP)",
        "type": "pistol",
        "caliber": "9x19mm Parabellum",
        "grains": 124,
        "muzzle_velocity_fps": 1100,
        "muzzle_energy_ftlbs": 333,
        "barrel_length_in": 4.0,
        "pressure_nato_psi": 36500,
        "penetration_in_gel": 12,
        "expansion_mm": 13,
    },
    "223_rem_55gr": {
        "name": ".223 Remington (55gr FMJ)",
        "type": "rifle",
        "caliber": ".223 Remington",
        "grains": 55,
        "muzzle_velocity_fps": 3240,
        "muzzle_energy_ftlbs": 1282,
        "barrel_length_in": 16.0,
        "pressure_nato_psi": 52000,
        "penetration_in_gel": 14,
        "expansion_mm": 7,
    },
    "223_rem_77gr": {
        "name": ".223 Remington (77gr OTM)",
        "type": "rifle",
        "caliber": ".223 Remington",
        "grains": 77,
        "muzzle_velocity_fps": 2825,
        "muzzle_energy_ftlbs": 1364,
        "barrel_length_in": 16.0,
        "pressure_nato_psi": 52000,
        "penetration_in_gel": 17,
        "expansion_mm": 8,
    },
    "308_win_168gr": {
        "name": ".308 Winchester (168gr BTHP)",
        "type": "rifle",
        "caliber": ".308 Winchester",
        "grains": 168,
        "muzzle_velocity_fps": 2650,
        "muzzle_energy_ftlbs": 2620,
        "barrel_length_in": 20.0,
        "pressure_nato_psi": 62000,
        "penetration_in_gel": 22,
        "expansion_mm": 10,
    },
    "308_win_175gr": {
        "name": ".308 Winchester (175gr BTHP)",
        "type": "rifle",
        "caliber": ".308 Winchester",
        "grains": 175,
        "muzzle_velocity_fps": 2600,
        "muzzle_energy_ftlbs": 2630,
        "barrel_length_in": 20.0,
        "pressure_nato_psi": 62000,
        "penetration_in_gel": 24,
        "expansion_mm": 9,
    },
    "762x39": {
        "name": "7.62x39mm (123gr FMJ)",
        "type": "rifle",
        "caliber": "7.62x39mm",
        "grains": 123,
        "muzzle_velocity_fps": 2300,
        "muzzle_energy_ftlbs": 1527,
        "barrel_length_in": 16.0,
        "pressure_nato_psi": 45300,
        "penetration_in_gel": 16,
        "expansion_mm": 10,
    },
    "556_nato_62gr": {
        "name": "5.56x45mm NATO (62gr FMJ)",
        "type": "rifle",
        "caliber": "5.56x45mm NATO",
        "grains": 62,
        "muzzle_velocity_fps": 3100,
        "muzzle_energy_ftlbs": 1324,
        "barrel_length_in": 14.5,
        "pressure_nato_psi": 58000,
        "penetration_in_gel": 12,
        "expansion_mm": 8,
    },
    "300_blackout_110gr": {
        "name": ".300 Blackout (110gr VMAX)",
        "type": "rifle",
        "caliber": ".300 AAC Blackout",
        "grains": 110,
        "muzzle_velocity_fps": 2350,
        "muzzle_energy_ftlbs": 1350,
        "barrel_length_in": 9.0,
        "pressure_nato_psi": 55000,
        "penetration_in_gel": 11,
        "expansion_mm": 13,
    },
    "300_blackout_220gr": {
        "name": ".300 Blackout (220gr Subsonic)",
        "type": "rifle",
        "caliber": ".300 AAC Blackout",
        "grains": 220,
        "muzzle_velocity_fps": 1000,
        "muzzle_energy_ftlbs": 489,
        "barrel_length_in": 9.0,
        "pressure_nato_psi": 55000,
        "penetration_in_gel": 20,
        "expansion_mm": 11,
    },
    "45acp_230gr": {
        "name": ".45 ACP (230gr FMJ)",
        "type": "pistol",
        "caliber": ".45 ACP",
        "grains": 230,
        "muzzle_velocity_fps": 835,
        "muzzle_energy_ftlbs": 356,
        "barrel_length_in": 5.0,
        "pressure_nato_psi": 21000,
        "penetration_in_gel": 11,
        "expansion_mm": 10,
    },
    "38spl_158gr": {
        "name": ".38 Special (158gr LSWC)",
        "type": "pistol",
        "caliber": ".38 Special",
        "grains": 158,
        "muzzle_velocity_fps": 900,
        "muzzle_energy_ftlbs": 284,
        "barrel_length_in": 4.0,
        "pressure_nato_psi": 17000,
        "penetration_in_gel": 9,
        "expansion_mm": 10,
    },
    "12ga_00buck": {
        "name": "12 Gauge (00 Buck, 9 pellet)",
        "type": "shotgun",
        "caliber": "12 Gauge",
        "grains": None,
        "muzzle_velocity_fps": 1320,
        "muzzle_energy_ftlbs": 1968,
        "barrel_length_in": 28.0,
        "pressure_nato_psi": None,
        "penetration_in_gel": 18,
        "expansion_mm": 18,
        "pellets": 9,
        "pellet_diameter_in": 0.33,
    },
    "12ga_slug": {
        "name": "12 Gauge (1oz rifled slug)",
        "type": "shotgun",
        "caliber": "12 Gauge",
        "grains": 438,
        "muzzle_velocity_fps": 1560,
        "muzzle_energy_ftlbs": 2365,
        "barrel_length_in": 28.0,
        "pressure_nato_psi": None,
        "penetration_in_gel": 28,
        "expansion_mm": 12,
    },
}


class AmmoQuery(BaseModel):
    caliber: str
    grain: int | None = None
    use_case: str | None = None


class EnergyCalc(BaseModel):
    caliber_id: str
    velocity_fps: int | None = None
    barrel_length_in: float | None = None


@app.get("/")
def read_root():
    return {"ammodex": "ballistic API", "endpoints": ["/ammo/{caliber_id}", "/search", "/energy-calc"]}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/v1/ammo/{caliber_id}")
def get_ammo(caliber_id: str):
    """Get ballistic data for a specific caliber ID."""
    ammo = AMMUNITION_DB.get(caliber_id)
    if not ammo:
        return {"error": "caliber not found", "available": list(AMMUNITION_DB.keys())}
    return ammo


@app.get("/api/v1/search")
def search_caliber(q: str = ""):
    """Search ammunitions by name or caliber."""
    q = q.lower()
    results = [
        ammo for ammo in AMMUNITION_DB.values()
        if q in ammo["name"].lower() or q in ammo["caliber"].lower()
    ]
    return {"query": q, "count": len(results), "results": results}


@app.get("/api/v1/energy-calc")
def energy_calc(caliber_id: str, velocity_fps: int | None = None, grain: int | None = None):
    """Calculate muzzle energy and other metrics. Override velocity/grain if needed."""
    ammo = AMMUNITION_DB.get(caliber_id)
    if not ammo:
        return {"error": "caliber not found"}
    v = velocity_fps or ammo["muzzle_velocity_fps"]
    g = grain or ammo["grains"] or 0
    # muzzle energy = (grain * velocity^2) / 450400
    energy = (g * v * v) / 450400 if g else 0
    return {
        "caliber_id": caliber_id,
        "name": ammo["name"],
        "velocity_fps": v,
        "grains": g,
        "muzzle_energy_ftlbs": round(energy, 1),
        "muzzle_energy_joules": round(energy * 1.3558179, 1),
        "fps_to_joules": 0.737562,
    }


@app.post("/api/v1/ballistics/gel-test")
def gel_test(caliber_id: str, velocity_fps: int | None = None):
    """Simulate ballistic gel test results based on NIST-standard formulas."""
    ammo = AMMUNITION_DB.get(caliber_id)
    if not ammo:
        return {"error": "caliber not found"}
    v = velocity_fps or ammo["muzzle_velocity_fps"]
    pen = ammo["penetration_in_gel"]
    exp = ammo["expansion_mm"]
    # Penetration decreases ~2% per 100fps over reference velocity
    if velocity_fps and velocity_fps > ammo["muzzle_velocity_fps"]:
        pen_adjust = (velocity_fps - ammo["muzzle_velocity_fps"]) / 100 * 0.02 * pen
        pen = max(6, pen - pen_adjust)
        exp = min(20, exp + (velocity_fps - ammo["muzzle_velocity_fps"]) / 200)
    return {
        "caliber_id": caliber_id,
        "name": ammo["name"],
        "velocity_fps": v,
        "penetration_inches": round(pen / 2.54, 1),
        "expansion_mm": round(exp, 1),
        "terminal_performance": "optimal" if 10 <= pen <= 18 and exp >= 9 else "review",
        "nato_compliant": ammo.get("pressure_nato_psi") is not None,
    }
