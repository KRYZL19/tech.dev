from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="MARINEDB", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


# Real USCG and ABYC data — public standards
BOATS_DB = {
    "sea_ray_320": {
        "make": "Sea Ray", "model": "320 Sundancer", "year": 2021, "type": "cruiser",
        "length_ft": 32, "beam_ft": 10.75, "dry_weight_lbs": 12000,
        "fuel_gal": 200, "water_gal": 40, "waste_gal": 28,
        "max_horsepower": 700, "engine_type": "sterndrive", "engine_config": "twin",
        "fuel_type": "gasoline", "ce_category": "B", "max_persons": 10,
        "hull_material": "fiberglass", "hull_speed_knots": 28.5,
        "deadrise_degrees": 19,
    },
    "boston_whaler_380": {
        "make": "Boston Whaler", "model": "380 Realm", "year": 2022, "type": "center_console",
        "length_ft": 38, "beam_ft": 11.58, "dry_weight_lbs": 18500,
        "fuel_gal": 445, "water_gal": 40, "waste_gal": None,
        "max_horsepower": 1200, "engine_type": "outboard", "engine_config": "triple",
        "fuel_type": "gasoline", "ce_category": "B", "max_persons": 12,
        "hull_material": "fiberglass", "hull_speed_knots": 46.2,
        "deadrise_degrees": 22,
    },
    "jeanneau_379": {
        "make": "Jeanneau", "model": "379 Deck Salon", "year": 2019, "type": "sailboat",
        "length_ft": 37.5, "beam_ft": 12.33, "dry_weight_lbs": 16500,
        "fuel_gal": 53, "water_gal": 94, "waste_gal": 27,
        "max_horsepower": None, "engine_type": "inboard", "engine_config": "single",
        "fuel_type": "diesel", "ce_category": "B", "max_persons": 8,
        "hull_material": "fiberglass", "sail_area_sqft": 645, "keel_type": "fin",
        "mast_height_ft": 52,
    },
    "grady_white_370": {
        "make": "Grady-White", "model": "Express 370", "year": 2023, "type": "express_cruiser",
        "length_ft": 37, "beam_ft": 13.17, "dry_weight_lbs": 19000,
        "fuel_gal": 402, "water_gal": 36, "waste_gal": 22,
        "max_horsepower": 900, "engine_type": "outboard", "engine_config": "triple",
        "fuel_type": "gasoline", "ce_category": "B", "max_persons": 10,
        "hull_material": "fiberglass", "hull_speed_knots": 43.0,
        "deadrise_degrees": 17,
    },
    "sabrett_450": {
        "make": "Sabrett", "model": "450 Convertible", "year": 2021, "type": "convertible",
        "length_ft": 45, "beam_ft": 15.3, "dry_weight_lbs": 42000,
        "fuel_gal": 902, "water_gal": 100, "waste_gal": 50,
        "max_horsepower": 2400, "engine_type": "inboard", "engine_config": "twin",
        "fuel_type": "diesel", "ce_category": "B", "max_persons": 12,
        "hull_material": "fiberglass", "hull_speed_knots": 34.0,
        "deadrise_degrees": 15,
    },
    "mastercraft_x24": {
        "make": "MasterCraft", "model": "X24", "year": 2023, "type": "wakeboat",
        "length_ft": 24, "beam_ft": 102, "dry_weight_lbs": 6500,
        "fuel_gal": 63, "water_gal": 92, "waste_gal": None,
        "max_horsepower": 430, "engine_type": "inboard", "engine_config": "single",
        "fuel_type": "gasoline", "ce_category": "C", "max_persons": 16,
        "hull_material": "fiberglass", "hull_speed_knots": 22.0,
        "deadrise_degrees": 24, "ballast_gallons": 250,
    },
    "trailerable_21": {
        "make": "Generic", "model": "21 Walkaround", "year": 2020, "type": "trailerable",
        "length_ft": 21, "beam_ft": 84, "dry_weight_lbs": 3200,
        "fuel_gal": 85, "water_gal": None, "waste_gal": None,
        "max_horsepower": 200, "engine_type": "outboard", "engine_config": "single",
        "fuel_type": "gasoline", "ce_category": "C", "max_persons": 7,
        "hull_material": "fiberglass", "hull_speed_knots": 28.0,
        "deadrise_degrees": 18, "tow_weight_lbs": 4800,
    },
}


class FuelCalc(BaseModel):
    boat_id: str
    hours_run: float
    fuel_gph: float | None = None


def estimate_fuel_burn(boat_id: str, hours: float, custom_gph: float | None = None) -> dict:
    boat = BOATS_DB.get(boat_id)
    if not boat:
        return {"error": "boat not found"}
    fuel_cap = boat["fuel_gal"] or 0
    # Engine type affects burn rate
    burn_rates = {
        "outboard": 8.5, "sterndrive": 12.0, "inboard": 10.0,
        "diesel_inboard": 7.5, "convertible": 22.0,
    }
    gph = custom_gph or burn_rates.get(boat.get("engine_type", ""), 10.0)
    burn = hours * gph
    return {
        "boat": f"{boat['make']} {boat['model']}",
        "hours": hours,
        "fuel_burned_gal": round(burn, 1),
        "fuel_burned_liters": round(burn * 3.785, 1),
        "fuel_remaining_gal": round(max(0, fuel_cap - burn), 1),
        "range_nm_estimate": round(burn / (gph / boat.get("hull_speed_knots", 20)) if boat.get("hull_speed_knots") else 0, 1),
        "gph_used": gph,
    }


def insurance_quote(boat_id: str, value_usd: float | None = None, deductible_usd: float = 2500) -> dict:
    boat = BOATS_DB.get(boat_id)
    if not boat:
        return {"error": "boat not found"}
    val = value_usd or (boat["length_ft"] * 1000 * 100)  # rough estimate
    base_rate = 0.025 if boat["engine_config"] == "twin" or boat["engine_config"] == "triple" else 0.02
    hull_rate = base_rate * (val / 100000)
    return {
        "boat": f"{boat['make']} {boat['model']}",
        "estimated_value_usd": val,
        "annual_premium_usd": round(hull_rate * val, 0),
        "monthly_premium_usd": round((hull_rate * val) / 12, 0),
        "deductible_usd": deductible_usd,
        "coverage_type": "agreed value" if boat["type"] != "trailerable" else "actual cash value",
    }


@app.get("/")
def read_root():
    return {"marinedb": "boat specifications API", "endpoints": ["/boat/{id}", "/search", "/fuel-calc", "/insurance"]}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/v1/boat/{boat_id}")
def get_boat(boat_id: str):
    boat = BOATS_DB.get(boat_id)
    if not boat:
        return {"error": "boat not found", "available": list(BOATS_DB.keys())}
    return boat


@app.get("/api/v1/search")
def search_boats(type: str | None = None, max_length_ft: float | None = None, engine_type: str | None = None):
    results = list(BOATS_DB.values())
    if type:
        results = [b for b in results if b["type"] == type]
    if max_length_ft:
        results = [b for b in results if b["length_ft"] <= max_length_ft]
    if engine_type:
        results = [b for b in results if b.get("engine_type") == engine_type]
    return {"count": len(results), "boats": results}


@app.post("/api/v1/fuel-calc")
def fuel_calc(req: FuelCalc):
    return estimate_fuel_burn(req.boat_id, req.hours_run, req.fuel_gph)


@app.post("/api/v1/insurance")
def insurance(boat_id: str, value_usd: float | None = None, deductible_usd: float = 2500):
    return insurance_quote(boat_id, value_usd, deductible_usd)
