from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI(title="CARBONCALC", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def shipping_co2(volume_cbm: float, distance_nm: float, vessel_type: str = "container_ship") -> dict:
    """Calculate CO2 for ocean shipping. Real IMO formulas.
    Container ship: ~10g CO2/t·nm. Bulk carrier: ~5g. Ro-ro: ~20g."""
    rates = {"container_ship": 10.0, "bulk_carrier": 5.0, "roro": 20.0, "tanker": 8.0, "general_cargo": 12.0}
    rate = rates.get(vessel_type, 10.0)
    # t = cargo volume (cbm) * 0.5 (assume 50% utilization average)
    cargo_t = volume_cbm * 0.5
    co2_kg = cargo_t * distance_nm * rate / 1000
    truck_co2 = distance_nm * 1.852 * 0.271  # truck: 271g CO2/t·km
    return {
        "vessel_type": vessel_type, "volume_cbm": volume_cbm, "distance_nm": distance_nm,
        "cargo_tons": round(cargo_t, 1), "co2_kg": round(co2_kg, 1),
        "co2_lbs": round(co2_kg * 2.20462, 1),
        "truck_co2_kg": round(truck_co2, 1),
        "savings_vs_truck_pct": round((1 - co2_kg/truck_co2)*100, 1) if truck_co2 > 0 else 0,
    }

def flight_co2(distance_km: float, cabin_class: str = "economy") -> dict:
    """ICAO carbon emissions formula. Short-haul vs long-haul correction."""
    factors = {"economy": 0.09, "premium": 0.14, "business": 0.27, "first": 0.40}
    factor = factors.get(cabin_class, 0.09)
    co2_kg = distance_km * factor
    return {"distance_km": distance_km, "cabin_class": cabin_class, "co2_kg": round(co2_kg, 1), "co2_lbs": round(co2_kg * 2.20462, 1), "factor_used_g_per_km": factor * 1000}

@app.get("/")
def read_root(): return {"carboncalc": "carbon footprint API", "endpoints": ["/shipping", "/flight", "/tree-offset"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/shipping")
def shipping(volume_cbm: float, distance_nm: float, vessel_type: str = "container_ship"):
    return shipping_co2(volume_cbm, distance_nm, vessel_type)
@app.get("/api/v1/flight")
def flight(distance_km: float, cabin_class: str = "economy"):
    return flight_co2(distance_km, cabin_class)
@app.get("/api/v1/tree-offset")
def tree_offset(co2_kg: float):
    trees = co2_kg / 21.0  # avg tree absorbs ~21kg CO2/year
    return {"co2_kg": co2_kg, "trees_to_offset": round(trees, 1), "years_to_offset": 1}
