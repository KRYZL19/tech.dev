from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math

app = FastAPI(title="BREWCRUNCH", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


class ExtractionQuery(BaseModel):
    coffee_g: float       # grams of coffee
    water_ml: float       # milliliters of water
    temp_f: float = 200   # water temperature in Fahrenheit
    brew_time_s: int = 150  # total brew time in seconds
    tds_percent: float | None = None  # measured TDS %, from refractometer


class DoseBrew(BaseModel):
    method: str   # v60, chemex, french_press, aeropress, espresso, moka
    coffee_g: float
    water_ml: float


# Refractometer calibration for coffee — standard SCA equation
def calc_extraction_yield(coffee_g: float, water_ml: float, tds_percent: float) -> dict:
    """Standard SCA extraction yield formula."""
    beverage_weight = water_ml  # approx 1g = 1ml
    dissolved_solids = beverage_weight * (tds_percent / 100)
    extraction_yield = (dissolved_solids / coffee_g) * 100
    return {
        "extraction_yield_percent": round(extraction_yield, 2),
        "dissolved_solids_g": round(dissolved_solids, 2),
        "ideal_range": "18.0 – 22.0%",
        "status": "under" if extraction_yield < 18 else "over" if extraction_yield > 22 else "optimal",
    }


def grind_recommendation(method: str, coffee_g: float, water_ml: float) -> dict:
    """Recommended grind size and brew parameters by method."""
    methods = {
        "v60": {"grind": "medium-fine (400-600ms)", "ratio": "1:15", "temp_f": 200, "brew_time_s": 180, "pour_style": "blooming", "notes": "45g/750ml = 2:30-3:00 total"},
        "chemex": {"grind": "medium-coarse (600-800ms)", "ratio": "1:16", "temp_f": 202, "brew_time_s": 270, "pour_style": "steady pour", "notes": "45g/720ml = 4:00-4:30 total"},
        "french_press": {"grind": "coarse (900-1200ms)", "ratio": "1:12", "temp_f": 200, "brew_time_s": 240, "pour_style": "full immersion", "notes": "30g/360ml = 4:00 steep"},
        "aeropress": {"grind": "fine-medium (200-400ms)", "ratio": "1:12", "temp_f": 185, "brew_time_s": 90, "pour_style": "inverted, stir", "notes": "17g/200ml = 1:30 total"},
        "espresso": {"grind": "fine (30-50ms)", "ratio": "1:2", "temp_f": 200, "brew_time_s": 28, "pour_style": "9-bar pressure", "notes": "18g in / 36g out / 25-30s"},
        "moka": {"grind": "medium-fine (200-400ms)", "ratio": "1:7", "temp_f": 200, "brew_time_s": 45, "pour_style": "medium heat", "notes": "fills bottom chamber 3/4"},
    }
    return methods.get(method, {"error": "method not found. try: v60, chemex, french_press, aeropress, espresso, moka"})


def ratio_check(coffee_g: float, water_ml: float) -> dict:
    ratio = water_ml / coffee_g
    return {
        "ratio": f"1:{round(ratio, 1)}",
        "ratio_value": round(ratio, 2),
        "assessment": "weak" if ratio > 18 else "strong" if ratio < 12 else "optimal" if 14 <= ratio <= 17 else "acceptable",
        "sca_ideal": "1:15 to 1:17",
        "adjustment_g": None if 14 <= ratio <= 17 else round(coffee_g * (ratio / 16) - coffee_g, 1)
    }


@app.get("/")
def read_root():
    return {"brewcrunch": "coffee extraction API", "endpoints": ["/extract", "/ratio", "/grind", "/methods"]}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.post("/api/v1/extract")
def get_extraction(q: ExtractionQuery):
    """Calculate extraction yield from measured TDS (requires refractometer)."""
    if q.tds_percent is None:
        return {"error": "tds_percent required for extraction calculation", "example": {"coffee_g": 21, "water_ml": 340, "tds_percent": 1.38}}
    result = calc_extraction_yield(q.coffee_g, q.water_ml, q.tds_percent)
    ratio_info = ratio_check(q.coffee_g, q.water_ml)
    return {"input": q.model_dump(), "extraction": result, "ratio": ratio_info}


@app.post("/api/v1/extract/estimate")
def estimate_extraction(coffee_g: float, water_ml: float, temp_f: float = 200, brew_time_s: int = 150):
    """Estimate extraction yield based on brew parameters when no refractometer available."""
    # Simplified model based on grind, temp, time, ratio
    ratio = water_ml / coffee_g
    # Temperature factor: cooler = harder extraction
    temp_factor = min(1.0, (temp_f - 180) / 40) if temp_f >= 180 else 0.6
    # Time factor: too fast = under, too slow = over
    time_factor = min(1.0, brew_time_s / 180) if brew_time_s < 180 else 1.05
    # Ratio factor
    ratio_factor = ratio / 15.5
    # Base extraction ~18-22% depending on all factors
    est_yield = 17.5 * temp_factor * time_factor * ratio_factor
    est_yield = max(14.0, min(25.0, est_yield))
    return {
        "estimated_extraction_percent": round(est_yield, 1),
        "status": "under" if est_yield < 18 else "over" if est_yield > 22 else "optimal",
        "ideal_range": "18.0 – 22.0%",
        "note": "estimation — use refractometer for accurate reading",
        "ratio_check": ratio_check(coffee_g, water_ml),
    }


@app.post("/api/v1/ratio")
def check_ratio(coffee_g: float, water_ml: float):
    """Check brew ratio and get adjustment recommendation."""
    return ratio_check(coffee_g, water_ml)


@app.get("/api/v1/grind/{method}")
def get_grind(method: str, coffee_g: float = 0, water_ml: float = 0):
    """Get grind size and brew parameters for a specific method."""
    result = grind_recommendation(method, coffee_g, water_ml)
    if "error" in result:
        return result
    if coffee_g > 0 and water_ml > 0:
        result["ratio_check"] = ratio_check(coffee_g, water_ml)
    return result


@app.get("/api/v1/methods")
def list_methods():
    return {"methods": ["v60", "chemex", "french_press", "aeropress", "espresso", "moka"]}
