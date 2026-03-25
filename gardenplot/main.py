from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="GARDENPLOT", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# USDA zone data + first/last frost dates for major cities
ZONES_DB = {
    "austin_tx": {"zone": "8b", "last_frost": "Mar 5", "first_frost": "Nov 22", "grow_days": 261, "zone_low_f": 15, "zone_high_f": 20},
    "denver_co": {"zone": "5b", "last_frost": "May 5", "first_frost": "Oct 1", "grow_days": 149, "zone_low_f": -15, "zone_high_f": -10},
    "chicago_il": {"zone": "6a", "last_frost": "Apr 20", "first_frost": "Oct 20", "grow_days": 183, "zone_low_f": -10, "zone_high_f": -5},
    "miami_fl": {"zone": "10b", "last_frost": None, "first_frost": None, "grow_days": 365, "zone_low_f": 35, "zone_high_f": 40},
    "seattle_wa": {"zone": "9a", "last_frost": "Mar 15", "first_frost": "Nov 15", "grow_days": 245, "zone_low_f": 20, "zone_high_f": 25},
    "phoenix_az": {"zone": "9b", "last_frost": None, "first_frost": None, "grow_days": 365, "zone_low_f": 25, "zone_high_f": 30},
    "minneapolis_mn": {"zone": "4b", "last_frost": "May 10", "first_frost": "Sep 25", "grow_days": 138, "zone_low_f": -25, "zone_high_f": -20},
}

PLANTS = {
    "tomato": {"days_to_maturity": 80, "cold_hardiness": "frost_tender", "spacing_in": 24, "yield_per_plant_lbs": 10, "optimal_temp_f": [65, 85]},
    "pepper": {"days_to_maturity": 75, "cold_hardiness": "frost_tender", "spacing_in": 18, "yield_per_plant_lbs": 5, "optimal_temp_f": [70, 90]},
    "lettuce": {"days_to_maturity": 45, "cold_hardiness": "frost_hardy", "spacing_in": 12, "yield_per_plant_lbs": 0.5, "optimal_temp_f": [50, 70]},
    "cucumber": {"days_to_maturity": 60, "cold_hardiness": "frost_tender", "spacing_in": 36, "yield_per_plant_lbs": 8, "optimal_temp_f": [70, 95]},
    "zucchini": {"days_to_maturity": 55, "cold_hardiness": "frost_tender", "spacing_in": 36, "yield_per_plant_lbs": 10, "optimal_temp_f": [60, 90]},
    "kale": {"days_to_maturity": 55, "cold_hardiness": "frost_hardy", "spacing_in": 18, "yield_per_plant_lbs": 2, "optimal_temp_f": [40, 75]},
    "carrot": {"days_to_maturity": 70, "cold_hardiness": "frost_hardy", "spacing_in": 3, "yield_per_plant_lbs": 0.2, "optimal_temp_f": [60, 70]},
    "beans": {"days_to_maturity": 60, "cold_hardiness": "frost_tender", "spacing_in": 6, "yield_per_plant_lbs": 0.5, "optimal_temp_f": [65, 85]},
    "basil": {"days_to_maturity": 30, "cold_hardiness": "frost_tender", "spacing_in": 12, "yield_per_plant_lbs": 0.25, "optimal_temp_f": [70, 85]},
    "cilantro": {"days_to_maturity": 45, "cold_hardiness": "frost_tender", "spacing_in": 6, "yield_per_plant_lbs": 0.1, "optimal_temp_f": [50, 75]},
}

def plant_calendar(location: str, plant: str, start_method: str = "transplant") -> dict:
    loc = ZONES_DB.get(location)
    plant_data = PLANTS.get(plant)
    if not loc:
        return {"error": "location not found", "available": list(ZONES_DB.keys())}
    if not plant_data:
        return {"error": "plant not found", "available": list(PLANTS.keys())}
    if start_method == "direct sow":
        days_back = plant_data["days_to_maturity"] + 14  # extra buffer
    else:
        days_back = plant_data["days_to_maturity"] + 21  # transplant adds time
    return {
        "location": location, "zone": loc["zone"], "plant": plant,
        "last_frost": loc["last_frost"], "first_frost": loc["first_frost"], "grow_days": loc["grow_days"],
        "plant_spacing_in": plant_data["spacing_in"],
        "cold_hardiness": plant_data["cold_hardiness"],
        "plant_now": loc["grow_days"] >= plant_data["days_to_maturity"] + 21,
        "plant_data": plant_data,
        "yield_per_plant": f"{plant_data['yield_per_plant_lbs']} lbs",
    }

def spacing_calc(plant: str, area_sqft: float) -> dict:
    plant_data = PLANTS.get(plant, PLANTS["tomato"])
    spacing_in = plant_data["spacing_in"]
    plants_per_row = int(12 / (spacing_in / 12))
    return {"plant": plant, "area_sqft": area_sqft, "spacing_in": spacing_in, "estimated_plants": int(area_sqft * plants_per_row * 0.8)}

@app.get("/")
def read_root():
    return {"gardenplot": "planting calendar API", "endpoints": ["/zone", "/calendar", "/spacing"]}

@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/api/v1/zone/{location}")
def get_zone(location: str):
    return ZONES_DB.get(location, {"error": "location not found", "available": list(ZONES_DB.keys())})

@app.get("/api/v1/calendar")
def calendar(location: str, plant: str, start_method: str = "transplant"):
    return plant_calendar(location, plant, start_method)

@app.get("/api/v1/spacing")
def spacing(plant: str, area_sqft: float):
    return spacing_calc(plant, area_sqft)
