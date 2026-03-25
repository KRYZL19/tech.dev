"""
Room mode calculation and analysis endpoints.
"""
from fastapi import APIRouter
from models.schemas import RoomMode

router = APIRouter(prefix="/api/v1/room", tags=["Room"])

# Speed of sound in feet per second at ~70°F
SPEED_OF_SOUND_FPS = 1130


def calculate_room_modes(length_ft: float, width_ft: float, height_ft: float) -> list[dict]:
    """
    Calculate axial, tangential, and oblique room modes.
    
    Axial modes: React along one dimension (length, width, or height)
    Tangential modes: React along two dimensions
    Oblique modes: React along all three dimensions
    """
    modes = []
    
    # Generate mode numbers
    # Axial modes: (p,0,0), (0,q,0), (0,0,r)
    for p in range(1, 15):
        freq = (p * SPEED_OF_SOUND_FPS) / (2 * length_ft)
        if freq <= 300:
            modes.append({
                "frequency_hz": round(freq, 1),
                "mode_type": "axial",
                "dimensions": f"({p},0,0)",
                "severity": _calculate_severity(freq),
                "recommendation": _get_mode_recommendation(freq, "axial", p)
            })
    
    for q in range(1, 15):
        freq = (q * SPEED_OF_SOUND_FPS) / (2 * width_ft)
        if freq <= 300:
            modes.append({
                "frequency_hz": round(freq, 1),
                "mode_type": "axial",
                "dimensions": f"(0,{q},0)",
                "severity": _calculate_severity(freq),
                "recommendation": _get_mode_recommendation(freq, "axial", q)
            })
    
    for r in range(1, 10):
        freq = (r * SPEED_OF_SOUND_FPS) / (2 * height_ft)
        if freq <= 300:
            modes.append({
                "frequency_hz": round(freq, 1),
                "mode_type": "axial",
                "dimensions": f"(0,0,{r})",
                "severity": _calculate_severity(freq),
                "recommendation": _get_mode_recommendation(freq, "axial", r)
            })
    
    # Tangential modes: (p,q,0), (p,0,r), (0,q,r)
    for p in range(1, 8):
        for q in range(1, 8):
            freq = (SPEED_OF_SOUND_FPS / 2) * ((p / length_ft)**2 + (q / width_ft)**2)**0.5
            if freq <= 300:
                modes.append({
                    "frequency_hz": round(freq, 1),
                    "mode_type": "tangential",
                    "dimensions": f"({p},{q},0)",
                    "severity": _calculate_severity(freq),
                    "recommendation": _get_mode_recommendation(freq, "tangential", p)
                })
    
    for p in range(1, 8):
        for r in range(1, 6):
            freq = (SPEED_OF_SOUND_FPS / 2) * ((p / length_ft)**2 + (r / height_ft)**2)**0.5
            if freq <= 300:
                modes.append({
                    "frequency_hz": round(freq, 1),
                    "mode_type": "tangential",
                    "dimensions": f"({p},0,{r})",
                    "severity": _calculate_severity(freq),
                    "recommendation": _get_mode_recommendation(freq, "tangential", p)
                })
    
    # Oblique modes: (p,q,r) - generally less problematic
    for p in range(1, 5):
        for q in range(1, 5):
            for r in range(1, 4):
                freq = (SPEED_OF_SOUND_FPS / 2) * ((p / length_ft)**2 + (q / width_ft)**2 + (r / height_ft)**2)**0.5
                if 20 <= freq <= 300:
                    modes.append({
                        "frequency_hz": round(freq, 1),
                        "mode_type": "oblique",
                        "dimensions": f"({p},{q},{r})",
                        "severity": "mild",
                        "recommendation": "Generally well-damped. Monitor if issues persist."
                    })
    
    # Sort by frequency
    modes.sort(key=lambda x: x["frequency_hz"])
    
    # Remove duplicates (within 2 Hz tolerance)
    filtered = []
    for mode in modes:
        if not filtered or abs(mode["frequency_hz"] - filtered[-1]["frequency_hz"]) > 2:
            filtered.append(mode)
    
    return filtered[:50]  # Limit to 50 modes


def _calculate_severity(freq: float) -> str:
    """Calculate mode severity based on frequency."""
    if freq < 80:
        return "severe"  # Bass trap required
    elif freq < 150:
        return "moderate"  # Treatment needed
    elif freq < 250:
        return "mild"  # Minor effect
    else:
        return "mild"  # Usually not problematic


def _get_mode_recommendation(freq: float, mode_type: str, order: int) -> str:
    """Get treatment recommendation for a room mode."""
    if freq < 60:
        return "Deep bass trap (4-6 inches) recommended. Mode is very difficult to treat with EQ alone."
    elif freq < 100:
        return "Bass trap (2-4 inches) + narrow notch filter at {:.0f}Hz Q{:.1f}".format(freq, max(10 - order, 3))
    elif freq < 150:
        return "Broadband absorber + parametric EQ at {:.0f}Hz".format(freq)
    elif freq < 200:
        return "Panel absorber + shelf filter for room mode at {:.0f}Hz".format(freq)
    else:
        return "Standard acoustic panels + minor EQ correction if needed"


@router.get("/modes", response_model=list[RoomMode])
def get_room_modes(
    length_ft: float,
    width_ft: float,
    height_ft: float
):
    """
    Calculate room mode frequencies for a given room dimensions.
    
    Returns axial, tangential, and oblique modes with severity ratings and treatment recommendations.
    """
    modes = calculate_room_modes(length_ft, width_ft, height_ft)
    return modes


@router.get("/analysis")
def analyze_room(
    length_ft: float,
    width_ft: float,
    height_ft: float
):
    """
    Get a comprehensive room analysis including dimensions ratio and recommendations.
    """
    volume = length_ft * width_ft * height_ft
    
    # Calculate dimension ratios (for Golden Ratio check)
    ratios = sorted([length_ft / height_ft, width_ft / height_ft, length_ft / width_ft])
    
    # Ideal ratio check (Golden Ratio ≈ 1.618 or Bonello Criterion)
    ideal_ratio = 1.5 <= ratios[2] / ratios[0] <= 2.0
    
    modes = calculate_room_modes(length_ft, width_ft, height_ft)
    
    # Count modes per octave (Bonello Criterion)
    octave_bands = {
        "31.5": 0, "63": 0, "125": 0, "250": 0
    }
    for mode in modes:
        freq = mode["frequency_hz"]
        if freq < 45:
            octave_bands["31.5"] += 1
        elif freq < 90:
            octave_bands["63"] += 1
        elif freq < 180:
            octave_bands["125"] += 1
        elif freq < 355:
            octave_bands["250"] += 1
    
    bonello_ok = all(octave_bands[b] >= octave_bands[list(octave_bands.keys())[i-1]] 
                     for i, b in enumerate(list(octave_bands.keys())[1:], 1))
    
    return {
        "dimensions": {
            "length_ft": length_ft,
            "width_ft": width_ft,
            "height_ft": height_ft
        },
        "volume_cubic_ft": round(volume, 1),
        "dimension_ratios": [round(r, 3) for r in ratios],
        "ideal_ratio": ideal_ratio,
        "modes_count": len(modes),
        "modes_per_octave": octave_bands,
        "bonello_criterion_met": bonello_ok,
        "modes": modes[:20]  # Top 20 most problematic
    }
