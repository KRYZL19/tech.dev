# routes/weather.py
from fastapi import APIRouter
from models.schemas import WeatherAdjustRequest, WeatherAdjustResponse

router = APIRouter(prefix="/api/v1/weather", tags=["weather"])

# Golfmath hook: USGA formula doesn't account for wind, temp, or elevation.
# This adjusts the handicap based on conditions.
#
# Adjustment logic:
# - Wind: +0.1 strokes per 5mph over 15mph (headwind penalty)
# - Temp: +0.1 strokes per 10°F below 65°F (cold = ball doesn't travel)
# - Elevation: +0.05 strokes per 100ft above 1000ft (thin air = longer carry)

def estimate_weather_adjustment(temp_f: float, wind_mph: float, elevation_ft: float) -> dict:
    wind_adj = 0.0
    temp_adj = 0.0
    elev_adj = 0.0
    details = {}

    # Wind: calm (< 10 mph) = no penalty; 10-20 = mild; > 20 = significant
    if wind_mph > 15:
        wind_adj = (wind_mph - 15) / 5 * 0.1
        details["wind"] = f"+{round(wind_adj, 2)} strokes (wind={wind_mph}mph)"
    elif wind_mph > 10:
        wind_adj = (wind_mph - 10) / 10 * 0.05
        details["wind"] = f"+{round(wind_adj, 2)} strokes (wind={wind_mph}mph)"
    else:
        details["wind"] = "No adjustment (calm)"

    # Temperature: optimal ~70°F; cold = penalty
    if temp_f < 65:
        temp_adj = (65 - temp_f) / 10 * 0.1
        details["temp"] = f"+{round(temp_adj, 2)} strokes (temp={temp_f}°F)"
    else:
        temp_adj = 0.0
        details["temp"] = f"No adjustment (temp={temp_f}°F, optimal range)"

    # Elevation: above 1000ft, thin air adds distance
    if elevation_ft > 1000:
        elev_adj = (elevation_ft - 1000) / 100 * 0.05
        details["elevation"] = f"-{round(elev_adj, 2)} strokes gained (elev={elevation_ft}ft)"
    else:
        elev_adj = 0.0
        details["elevation"] = f"No adjustment (elev={elevation_ft}ft, near sea level)"

    total_adj = wind_adj + temp_adj - elev_adj
    return {
        "wind": round(wind_adj, 3),
        "temp": round(temp_adj, 3),
        "elevation": round(-elev_adj, 3),
        "total": round(total_adj, 3)
    }


@router.post("/adjust", response_model=WeatherAdjustResponse)
def adjust_for_weather(req: WeatherAdjustRequest):
    """
    Adjust handicap index for weather conditions.
    
    Your handicap index doesn't account for wind. The USGA formula is 30 years old.
    Here's something that actually adjusts for conditions.
    
    - Wind > 15mph: adds strokes (playing into wind is hard)
    - Temp < 65°F: adds strokes (ball doesn't travel as far)
    - Elevation > 1000ft: subtracts strokes (ball flies longer in thin air)
    """
    adj = estimate_weather_adjustment(req.temp_f, req.wind_mph, req.elevation_ft)

    adjusted = round(req.handicap_index + adj["total"], 1)
    # Cap at 54
    adjusted = min(max(adjusted, 0.0), 54.0)

    strokes_gained = -adj["total"]  # positive = you gain strokes (play better)

    if adj["total"] > 0:
        breakdown = (
            f"Conditions add {round(adj['total'], 1)} strokes to your game: "
            f"wind +{round(adj['wind'],2)}, temp +{round(adj['temp'],2)}, "
            f"elevation {round(adj['elevation'],2)}."
        )
    elif adj["total"] < 0:
        breakdown = (
            f"Conditions help: subtract {round(-adj['total'], 1)} strokes. "
            f"Elevation gain: {round(-adj['elevation'],2)}, wind {round(adj['wind'],2)}, temp {round(adj['temp'],2)}."
        )
    else:
        breakdown = "Neutral conditions — no adjustment."

    return WeatherAdjustResponse(
        original_handicap=req.handicap_index,
        adjusted_handicap=adjusted,
        strokes_gained_lost=round(strokes_gained, 1),
        conditions={
            "temp_f": req.temp_f,
            "wind_mph": req.wind_mph,
            "elevation_ft": req.elevation_ft,
            "adjustments": adj
        },
        breakdown=breakdown
    )
