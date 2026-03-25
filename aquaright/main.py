from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math

app = FastAPI(title="AQUARIGHT", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


def calc_fci(free_cl_ppm: float, cya_ppm: float) -> dict:
    """Free chlorine effectiveness — adjusted for CYA lockup (USDA/CDC model).
    CYA above 50ppm drastically reduces chlorine effectiveness."""
    if cya_ppm < 1:
        return {"fci_ppm": free_cl_ppm, "effective_cl_ppm": free_cl_ppm, "status": "optimal", "lockup_percent": 0}
    # EPA Effective Chlorine = FC / (1 + 0.25 * CYA^0.57)
    lockup_factor = 1 + 0.25 * (cya_ppm ** 0.57)
    effective = free_cl_ppm / lockup_factor
    lockup_pct = ((lockup_factor - 1) / lockup_factor) * 100
    return {
        "fci_ppm": free_cl_ppm,
        "cya_ppm": cya_ppm,
        "effective_cl_ppm": round(effective, 2),
        "lockup_percent": round(lockup_pct, 1),
        "status": "lockup_danger" if lockup_pct > 70 else "lockup_warning" if lockup_pct > 50 else "optimal",
        "recommendation": f"Drain {min(50, round((1 - 50/cya_ppm)*100))}% if CYA > 100ppm" if cya_ppm > 100 else "CYA acceptable"
    }


def calc_csi(ph: float, ta_ppm: float, calcium_ppm: float, temp_f: float, cya_ppm: float = 0) -> dict:
    """Calcium Saturation Index — Langellier Saturation Index (LSI).
    CSI > +0.5: scale forming. CSI < -0.5: corrosive. CSI 0 = balanced."""
    # Temp in °F → factor
    temp_factor = (temp_f - 32) * 0.055
    # pH factor
    ph_factor = ph - 7.0
    # TA contribution: convert to ppm as CaCO3 (already in ppm here)
    ta_factor = math.log10(max(1, ta_ppm)) - 1.0
    # Calcium contribution
    calcium_factor = math.log10(max(1, calcium_ppm)) + 1.0
    csi = ph_factor + temp_factor + ta_factor + calcium_factor - 12.1
    return {
        "csi": round(csi, 2),
        "status": "scale" if csi > 0.5 else "corrosive" if csi < -0.5 else "balanced",
        "interpretation": "scale forming — reduce pH or calcium" if csi > 0.5 else "corrosive — increase TA or calcium" if csi < -0.5 else "properly balanced",
        "factors": {"pH": round(ph_factor, 2), "temperature": round(temp_factor, 2), "TA": round(ta_factor, 2), "calcium": round(calcium_factor, 2)},
    }


def pool_volume(length_ft: float, width_ft: float, depth_ft: float, shape: str = "rectangular") -> dict:
    if shape == "round":
        radius = length_ft / 2
        gallons = math.pi * radius * radius * depth_ft * 7.48052
    else:
        gallons = length_ft * width_ft * depth_ft * 7.48052
    return {"volume_cu_ft": round(length_ft * width_ft * depth_ft, 1), "gallons": round(gallons, 1), "liters": round(gallons * 3.78541, 1)}


def chemical_dose(volume_gal: float, current_ppm: float, target_ppm: float, chemical_type: str) -> dict:
    """Calculate chemical dose in oz to reach target ppm."""
    # Sodium hypochlorite (bleach): 1 oz of 12.5% raises 10,000 gal by ~1 ppm
    # Chlorine: 1 oz/10k gal = ~1 ppm
    # Muriatic acid: 26 oz of 20% lowers pH by 0.2 in 10k gal
    # Soda ash: 1.5 oz/10k gal raises pH by 0.1
    # Calcium chloride: 1 lb/10k gal raises calcium by ~8 ppm
    doses = {
        "chlorine": (target_ppm - current_ppm) * volume_gal / 10000,
        "muriatic_acid": ((current_ppm - target_ppm) / 0.2) * 26 * volume_gal / 10000,
        "soda_ash": ((target_ppm - current_ppm) / 0.1) * 1.5 * volume_gal / 10000,
        "calcium_chloride": (target_ppm - current_ppm) * volume_gal / 8000 * 0.0625,
    }
    dose = doses.get(chemical_type, 0)
    return {
        "chemical": chemical_type,
        "dose_oz": round(max(0, dose), 2),
        "dose_lbs": round(max(0, dose) / 16, 3),
        "current_ppm": current_ppm,
        "target_ppm": target_ppm,
        "volume_gal": volume_gal,
    }


@app.get("/")
def read_root():
    return {"aquaright": "pool chemistry API", "endpoints": ["/fci", "/csi", "/volume", "/dose"]}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/v1/fci")
def fci(free_cl_ppm: float, cya_ppm: float):
    return calc_fci(free_cl_ppm, cya_ppm)


@app.get("/api/v1/csi")
def csi(ph: float, ta_ppm: float, calcium_ppm: float, temp_f: float, cya_ppm: float = 0):
    return calc_csi(ph, ta_ppm, calcium_ppm, temp_f, cya_ppm)


@app.get("/api/v1/volume")
def volume(length_ft: float, width_ft: float, depth_ft: float, shape: str = "rectangular"):
    return pool_volume(length_ft, width_ft, depth_ft, shape)


@app.post("/api/v1/dose")
def dose_calc(volume_gal: float, current_ppm: float, target_ppm: float, chemical_type: str):
    return chemical_dose(volume_gal, current_ppm, target_ppm, chemical_type)
