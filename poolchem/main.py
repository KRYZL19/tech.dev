from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI(title="POOLCHEM", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def calc_fci(free_cl_ppm: float, cya_ppm: float) -> dict:
    lockup_factor = 1 + 0.25 * (cya_ppm ** 0.57) if cya_ppm >= 1 else 1.0
    effective = free_cl_ppm / lockup_factor
    lockup_pct = ((lockup_factor - 1) / lockup_factor) * 100
    return {"fci_ppm": free_cl_ppm, "cya_ppm": cya_ppm, "effective_cl_ppm": round(effective, 2), "lockup_pct": round(lockup_pct, 1), "status": "lockup_danger" if lockup_pct > 70 else "lockup_warning" if lockup_pct > 50 else "optimal"}

def calc_csi(ph: float, ta_ppm: float, calcium_ppm: float, temp_f: float) -> dict:
    tf = (temp_f - 32) * 0.055
    csi = (ph - 7.0) + tf + (math.log10(max(1, ta_ppm)) - 1.0) + (math.log10(max(1, calcium_ppm)) + 1.0) - 12.1
    return {"csi": round(csi, 2), "status": "scale" if csi > 0.5 else "corrosive" if csi < -0.5 else "balanced", "interpretation": "scale forming" if csi > 0.5 else "corrosive" if csi < -0.5 else "properly balanced"}

def chemical_dose(vol_gal: float, current_ppm: float, target_ppm: float, chem: str) -> dict:
    doses = {"chlorine": (target_ppm - current_ppm) * vol_gal / 10000, "muriatic_acid": ((current_ppm - target_ppm) / 0.2) * 26 * vol_gal / 10000, "soda_ash": ((target_ppm - current_ppm) / 0.1) * 1.5 * vol_gal / 10000}
    oz = max(0, doses.get(chem, 0))
    return {"chemical": chem, "dose_oz": round(oz, 2), "dose_lbs": round(oz/16, 3), "volume_gal": vol_gal}

@app.get("/")
def read_root(): return {"poolchem": "pool chemistry API", "endpoints": ["/fci", "/csi", "/dose"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/fci")
def fci(free_cl_ppm: float, cya_ppm: float): return calc_fci(free_cl_ppm, cya_ppm)
@app.get("/api/v1/csi")
def csi(ph: float, ta_ppm: float, calcium_ppm: float, temp_f: float): return calc_csi(ph, ta_ppm, calcium_ppm, temp_f)
@app.post("/api/v1/dose")
def dose(volume_gal: float, current_ppm: float, target_ppm: float, chemical_type: str): return chemical_dose(volume_gal, current_ppm, target_ppm, chemical_type)
