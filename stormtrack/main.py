from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math

app = FastAPI(title="STORMTRACK", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


# NOAA SPC data — real storm prediction formulas
def wind_chill(temp_f: float, wind_mph: float) -> float:
    if temp_f > 50 or wind_mph < 3:
        return temp_f
    return 35.74 + 0.6215*temp_f - 35.75*(wind_mph**0.16) + 0.4275*temp_f*(wind_mph**0.16)


def heat_index(temp_f: float, rh_percent: float) -> float:
    """NWS heat index formula."""
    if temp_f < 80:
        return temp_f
    T = temp_f
    RH = rh_percent
    HI = -42.379 + 2.04901523*T + 10.14333127*RH - 0.22475541*T*RH - 0.00683783*T*T - 0.05481717*RH*RH + 0.00122874*T*T*RH + 0.00085282*T*RH*RH - 0.00000199*T*T*RH*RH
    return max(T, HI)


def tornado_risk(fujita_score: int, distance_mi: float, duration_min: int) -> dict:
    """Estimate tornado threat based on EF scale and proximity."""
    wind_speed = {0: 65, 1: 86, 2: 110, 3: 137, 4: 166, 5: 200}
    speed = wind_speed.get(fujita_score, 200)
    threat = "minimal"
    if distance_mi < 5 and duration_min > 5:
        threat = "extreme"
    elif distance_mi < 15:
        threat = "high"
    elif distance_mi < 30:
        threat = "moderate"
    return {
        "ef_scale": f"EF{fujita_score}",
        "estimated_wind_mph": speed,
        "distance_mi": distance_mi,
        "duration_min": duration_min,
        "threat_level": threat,
        "warning_time_min": round(distance_mi / 35 * 60, 1) if distance_mi > 0 else 0,
    }


def hurricane_category(wind_mph: float) -> dict:
    cats = [(157, "Cat 5", "catastrophic"), (130, "Cat 4", "devastating"), (111, "Cat 3", "devastating"), (96, "Cat 2", "extremely dangerous"), (74, "Cat 1", "very dangerous"), (0, "Tropical Storm", "dangerous")]
    for threshold, name, desc in cats:
        if wind_mph >= threshold:
            return {"category": name, "description": desc, "wind_mph": wind_mph, "storm_surge_ft": max(0, (wind_mph - 74) * 0.32 + 4)}
    return {"category": "Tropical Depression", "description": "disorganized", "wind_mph": wind_mph, "storm_surge_ft": 0}


@app.get("/")
def read_root():
    return {"stormtrack": "severe weather API", "endpoints": ["/windchill", "/heatindex", "/tornado", "/hurricane"]}


@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/v1/windchill")
def get_windchill(temp_f: float, wind_mph: float):
    return {"temp_f": temp_f, "wind_mph": wind_mph, "windchill_f": round(wind_chill(temp_f, wind_mph), 1)}


@app.get("/api/v1/heatindex")
def get_heatindex(temp_f: float, rh_percent: float):
    return {"temp_f": temp_f, "rh_percent": rh_percent, "heat_index_f": round(heat_index(temp_f, rh_percent), 1)}


@app.get("/api/v1/tornado")
def tornado_risk_endpoint(ef_scale: int, distance_mi: float, duration_min: int):
    return tornado_risk(ef_scale, distance_mi, duration_min)


@app.get("/api/v1/hurricane")
def hurricane_endpoint(wind_mph: float):
    return hurricane_category(wind_mph)
