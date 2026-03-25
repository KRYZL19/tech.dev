"""Tire sizing calculations shared by all routes."""

import re
from typing import Tuple

# Diameter diff threshold for "will fit" — industry standard 3%
FIT_THRESHOLD_PCT = 3.0
# 60mph reference for speedo diff
SPEEDO_REF_MPH = 60.0
INCHES_PER_MILE = 63360.0


def parse_tire_size(size_str: str) -> Tuple[int, int, int]:
    """
    Parse a tire size string like '245/45R18' or '245/45-18'.
    Returns (width_mm, aspect_ratio, rim_diameter).
    """
    size_str = size_str.strip().upper()
    # Handle both R and - separators
    pattern = r'^(\d{3})/(\d{2})[R-](\d{2})$'
    m = re.match(pattern, size_str)
    if not m:
        raise ValueError(f"Invalid tire size format: '{size_str}'. Expected format: 245/45R18")

    width = int(m.group(1))
    aspect = int(m.group(2))
    rim = int(m.group(3))

    if not (125 <= width <= 400):
        raise ValueError(f"Width {width}mm out of range (125-400mm)")
    if not (20 <= aspect <= 90):
        raise ValueError(f"Aspect ratio {aspect} out of range (20-90)")
    if not (10 <= rim <= 30):
        raise ValueError(f"Rim diameter {rim}\" out of range (10-30\")")

    return width, aspect, rim


def tire_dimensions(width_mm: int, aspect_ratio: int, rim_diameter: int) -> dict:
    """Calculate all tire dimensions from parsed size components."""
    sidewall_inches = (width_mm * aspect_ratio / 100) / 25.4
    diameter_inches = sidewall_inches * 2 + rim_diameter
    circumference_inches = diameter_inches * 3.14159265359
    revs_per_mile = int(INCHES_PER_MILE / circumference_inches)

    return {
        "width_mm": width_mm,
        "aspect_ratio": aspect_ratio,
        "rim_diameter": rim_diameter,
        "diameter_inches": round(diameter_inches, 3),
        "sidewall_inches": round(sidewall_inches, 3),
        "circumference_inches": round(circumference_inches, 3),
        "revolutions_per_mile": revs_per_mile,
    }


def compare_tires(tire1_size: str, tire2_size: str) -> dict:
    """
    Compare two tire sizes.
    Returns dict with diameter_diff_pct, will_fit, speedo_diff_mph, verdict.
    """
    w1, a1, r1 = parse_tire_size(tire1_size)
    w2, a2, r2 = parse_tire_size(tire2_size)

    dims1 = tire_dimensions(w1, a1, r1)
    dims2 = tire_dimensions(w2, a2, r2)

    dia1 = dims1["diameter_inches"]
    dia2 = dims2["diameter_inches"]

    diff_pct = abs(dia2 - dia1) / dia1 * 100
    will_fit = diff_pct <= FIT_THRESHOLD_PCT

    # Speedo diff: at 60mph reference, how fast does speedometer read vs actual
    speedo_diff_mph = (diff_pct / 100) * SPEEDO_REF_MPH

    # Build verdict
    if diff_pct < 0.5:
        verdict = "Nearly identical sizes — excellent match."
    elif diff_pct <= FIT_THRESHOLD_PCT:
        verdict = "Within safe tolerance. Minor speedo variance."
    elif diff_pct <= 5.0:
        verdict = "Outside factory tolerance — may rub or affect handling."
    else:
        verdict = "Dangerous mismatch — will definitely rub or affect safety."

    return {
        "tire1_parsed": {
            "width_mm": w1,
            "aspect_ratio": a1,
            "rim_diameter": r1,
            "diameter_inches": dia1,
        },
        "tire2_parsed": {
            "width_mm": w2,
            "aspect_ratio": a2,
            "rim_diameter": r2,
            "diameter_inches": dia2,
        },
        "diameter_diff_pct": round(diff_pct, 2),
        "will_fit": will_fit,
        "speedo_diff_mph": round(speedo_diff_mph, 2),
        "verdict": verdict,
    }
