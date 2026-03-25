"""
EQ settings calculation endpoints.
"""
from fastapi import APIRouter
from models.schemas import (
    RoomEQInput, RoomEQOutput, EQFilter, RoomMode, FirstReflectionCorrection,
    SpeakerProfileInput, SpeakerProfileOutput, FrequencyPoint, BassBoostRecommendation,
    FilterInfo, RoomTreatmentLevel
)
from data.room_profiles import get_speaker_profile, list_available_speakers

router = APIRouter(prefix="/api/v1/eq", tags=["EQ"])

# Common EQ frequencies for room correction
ROOM_CORRECTION_FREQUENCIES = [
    20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500
]


def calculate_room_volume_factors(volume_cubic_ft: float) -> dict:
    """Calculate scaling factors based on room size."""
    if volume_cubic_ft < 1000:
        return {
            "size_category": "small",
            "bass_gain": 1.5,
            "mid_bass_gain": 1.2,
            "modal_density": "low",
            "sb_boost": 2.0
        }
    elif volume_cubic_ft < 2500:
        return {
            "size_category": "medium",
            "bass_gain": 1.2,
            "mid_bass_gain": 1.0,
            "modal_density": "medium",
            "sb_boost": 1.5
        }
    else:
        return {
            "size_category": "large",
            "bass_gain": 1.0,
            "mid_bass_gain": 0.8,
            "modal_density": "high",
            "sb_boost": 1.0
        }


def calculate_treatment_factors(treatment: RoomTreatmentLevel) -> dict:
    """Calculate correction factors based on room treatment level."""
    if treatment == RoomTreatmentLevel.treated:
        return {
            "eq_correction_db": -3,  # Less correction needed
            "filter_q_reduction": 0.8,
            "reflection_compensation": 0.5
        }
    elif treatment == RoomTreatmentLevel.partial:
        return {
            "eq_correction_db": -1.5,
            "filter_q_reduction": 1.0,
            "reflection_compensation": 0.75
        }
    else:  # untreated
        return {
            "eq_correction_db": 0,
            "filter_q_reduction": 1.2,
            "reflection_compensation": 1.0
        }


def predict_room_modes(volume_cubic_ft: float, treatment: RoomTreatmentLevel) -> list[dict]:
    """Predict problematic room modes based on room characteristics."""
    # Estimate room dimensions from volume
    # Assuming typical ratio of 1.5:1:0.8
    estimated_volume = volume_cubic_ft
    l = (estimated_volume * 1.5 * 1.25)**(1/3)
    w = l / 1.5
    h = w * 0.8
    
    # Speed of sound
    c = 1130  # ft/s
    
    predicted_modes = []
    
    # Predict strongest axial modes
    for dim, dim_val, name in [(l, l, "length"), (w, w, "width"), (h, h, "height")]:
        for harmonic in range(1, 5):
            freq = (harmonic * c) / (2 * dim_val)
            if freq <= 300:
                treatment_factor = calculate_treatment_factors(treatment)
                severity = "severe" if freq < 100 else "moderate" if freq < 180 else "mild"
                
                predicted_modes.append({
                    "frequency_hz": round(freq, 1),
                    "mode_type": "axial",
                    "dimensions": name,
                    "severity": severity,
                    "recommendation": _get_mode_treatment(freq, treatment)
                })
    
    return sorted(predicted_modes, key=lambda x: x["frequency_hz"])[:10]


def _get_mode_treatment(freq: float, treatment: RoomTreatmentLevel) -> str:
    """Get treatment recommendation based on frequency and treatment level."""
    if treatment == RoomTreatmentLevel.treated:
        if freq < 80:
            return "2-inch panel absorber at first reflection points"
        elif freq < 150:
            return "Broadband absorber + minor EQ"
        else:
            return "Standard acoustic panels"
    elif treatment == RoomTreatmentLevel.partial:
        if freq < 80:
            return "Bass trap + narrow notch EQ at {:.0f}Hz".format(freq)
        elif freq < 150:
            return "Panel absorber + parametric EQ"
        else:
            return "Minor shelf filter if needed"
    else:
        if freq < 80:
            return "Bass trap required. EQ only partially effective."
        elif freq < 150:
            return "Broadband absorber + aggressive EQ"
        else:
            return "Panel absorbers + EQ correction"


def calculate_first_reflections(treatment: RoomTreatmentLevel) -> list[dict]:
    """Calculate first reflection points and corrections."""
    reflection_points = [
        {
            "frequency_hz": 500,
            "panel_location": "side_walls",
            "recommended_treatment": "1-2 inch acoustic panels at reflection points",
            "eq_suggestion_hz": 1000
        },
        {
            "frequency_hz": 1000,
            "panel_location": "side_walls",
            "recommended_treatment": "1-2 inch acoustic panels",
            "eq_suggestion_hz": 2000
        },
        {
            "frequency_hz": 2000,
            "panel_location": "ceiling",
            "recommended_treatment": "Cloud absorber or ceiling tiles",
            "eq_suggestion_hz": 4000
        },
        {
            "frequency_hz": 4000,
            "panel_location": "ceiling",
            "recommended_treatment": "High-frequency absorber",
            "eq_suggestion_hz": 6300
        },
        {
            "frequency_hz": 250,
            "panel_location": "back_wall",
            "recommended_treatment": "RPG diffuser or thick absorber",
            "eq_suggestion_hz": 315
        }
    ]
    
    # Reduce compensation for treated rooms
    factor = calculate_treatment_factors(treatment)["reflection_compensation"]
    
    return reflection_points


@router.post("/room", response_model=RoomEQOutput)
def calculate_room_eq(input_data: RoomEQInput):
    """
    Calculate recommended EQ settings for room correction.
    
    Takes room dimensions, speaker type, and treatment level to generate
    targeted EQ settings, predicted room mode issues, and first reflection corrections.
    """
    # Calculate volume
    volume = input_data.room_volume_cubic_ft
    
    # Get factors
    volume_factors = calculate_room_volume_factors(volume)
    treatment_factors = calculate_treatment_factors(input_data.room_treatment_level)
    
    # Generate EQ settings
    eq_settings = []
    
    # Speaker type adjustments
    if input_data.speaker_type.value == "bookshelf":
        # Bookshelf speakers need more bass boost
        base_bass_gain = 2.0
    elif input_data.speaker_type.value == "studio_monitor":
        base_bass_gain = 1.5
    else:
        base_bass_gain = 1.0
    
    # Generate parametric EQ filters
    frequencies_and_gains = [
        (40, base_bass_gain * volume_factors["bass_gain"]),
        (50, base_bass_gain * volume_factors["bass_gain"] * 0.8),
        (63, base_bass_gain * volume_factors["mid_bass_gain"]),
        (80, 1.0),
        (100, 0.5),
        (125, 0.5),
        (250, -0.5 + treatment_factors["eq_correction_db"]),
        (315, treatment_factors["eq_correction_db"]),
        (500, treatment_factors["eq_correction_db"]),
    ]
    
    for freq, gain in frequencies_and_gains:
        q = 2.0 * treatment_factors["filter_q_reduction"]
        # Adjust Q based on frequency (lower freq = higher Q for narrow cuts)
        if freq < 100:
            q = max(3.0 * treatment_factors["filter_q_reduction"], 1.5)
        elif freq < 200:
            q = 2.0 * treatment_factors["filter_q_reduction"]
        else:
            q = 1.5 * treatment_factors["filter_q_reduction"]
        
        eq_settings.append(EQFilter(
            frequency_hz=freq,
            gain_db=round(gain, 1),
            q_factor=round(q, 1)
        ))
    
    # Predict room modes
    predicted_modes = predict_room_modes(volume, input_data.room_treatment_level)
    
    # Calculate first reflections
    reflections = calculate_first_reflections(input_data.room_treatment_level)
    
    return RoomEQOutput(
        recommended_eq_settings=eq_settings,
        room_mode_predictions=predicted_modes,
        first_reflection_corrections=[
            FirstReflectionCorrection(**r) for r in reflections
        ]
    )


@router.post("/speaker-profile", response_model=SpeakerProfileOutput)
def get_speaker_eq(input_data: SpeakerProfileInput):
    """
    Get EQ settings based on specific speaker manufacturer and model.
    
    Returns frequency response curve data, recommended crossover frequency,
    and bass boost recommendations for the specified speaker.
    """
    profile = get_speaker_profile(input_data.speaker_manufacturer, input_data.speaker_model)
    
    if not profile:
        # Return generic response for unknown speakers
        return SpeakerProfileOutput(
            frequency_response_curve=[
                FrequencyPoint(frequency_hz=40, spl_db=-6),
                FrequencyPoint(frequency_hz=63, spl_db=-2),
                FrequencyPoint(frequency_hz=100, spl_db=0),
                FrequencyPoint(frequency_hz=500, spl_db=0),
                FrequencyPoint(frequency_hz=1000, spl_db=0),
                FrequencyPoint(frequency_hz=4000, spl_db=0),
                FrequencyPoint(frequency_hz=10000, spl_db=-1),
                FrequencyPoint(frequency_hz=16000, spl_db=-2),
            ],
            recommended_xover_hz=80,
            bass_boost_recommendations=[
                BassBoostRecommendation(
                    frequency_hz=50,
                    boost_db=2.0,
                    reason="Generic response - measure your room for best results"
                )
            ]
        )
    
    # Distance-based gain adjustment
    distance_factor = 1.0
    if input_data.listening_distance_ft < 6:
        distance_factor = 1.2  # Near-field boost
    elif input_data.listening_distance_ft > 10:
        distance_factor = 0.8  # Far-field rolloff compensation
    
    # Build frequency response curve
    curve = [
        FrequencyPoint(frequency_hz=p["freq"], spl_db=p["spl"])
        for p in profile["frequency_curve"]
    ]
    
    # Adjust bass based on distance
    for point in curve:
        if point.frequency_hz < 100:
            point.spl_db += (distance_factor - 1) * 3
    
    # Build bass boost recommendations
    bass_recommendations = [
        BassBoostRecommendation(
            frequency_hz=r["freq"],
            boost_db=r["boost"] * distance_factor,
            reason=r["reason"]
        )
        for r in profile["bass_boost_recommendations"]
    ]
    
    return SpeakerProfileOutput(
        frequency_response_curve=curve,
        recommended_xover_hz=profile["xover_recommended"],
        bass_boost_recommendations=bass_recommendations
    )


@router.get("/common", response_model=list[FilterInfo])
def get_common_filters():
    """
    List common filter types used in audio EQ with recommended use cases.
    """
    filters = [
        FilterInfo(
            filter_type="peq",
            description="Parametric EQ - Full control over frequency, gain, and Q",
            typical_use_cases=[
                "Room mode correction",
                "Speaker resonance control",
                "Surgical problem frequency removal"
            ],
            recommended_q_range="0.5 - 15 (narrow to very narrow)",
            recommended_gain_range="-15 to +6 dB"
        ),
        FilterInfo(
            filter_type="low_shelf",
            description="Boosts or cuts all frequencies below a set point",
            typical_use_cases=[
                "Overall bass balance adjustment",
                "Compensating for speaker rolloff",
                "Adding warmth or reducing boom"
            ],
            recommended_q_range="0.7 - 1.4 (broad filter shape)",
            recommended_gain_range="-6 to +3 dB"
        ),
        FilterInfo(
            filter_type="high_shelf",
            description="Boosts or cuts all frequencies above a set point",
            typical_use_cases=[
                "Treble brightness adjustment",
                "Compensating for dull recordings",
                "Reducing harshness"
            ],
            recommended_q_range="0.7 - 1.4 (broad filter shape)",
            recommended_gain_range="-6 to +3 dB"
        ),
        FilterInfo(
            filter_type="notch",
            description="Very narrow cut filter for specific problem frequencies",
            typical_use_cases=[
                "Removing specific room modes",
                "Eliminating feedback frequencies",
                "Cutting resonant peaks"
            ],
            recommended_q_range="10 - 30 (very narrow)",
            recommended_gain_range="-3 to -15 dB"
        ),
        FilterInfo(
            filter_type="high_pass",
            description="Allows frequencies above cutoff to pass",
            typical_use_cases=[
                "Removing sub-bass rumble",
                "Reducing strain on speakers",
                "Cleaning up bass in mixed signals"
            ],
            recommended_q_range="0.5 - 1.0 (slope control)",
            recommended_gain_range="N/A (on/off or slope)"
        ),
        FilterInfo(
            filter_type="low_pass",
            description="Allows frequencies below cutoff to pass",
            typical_use_cases=[
                "Subwoofer integration",
                "Reducing harsh highs",
                "Softening bright recordings"
            ],
            recommended_q_range="0.5 - 1.0 (slope control)",
            recommended_gain_range="N/A (on/off or slope)"
        )
    ]
    
    return filters


@router.get("/speakers")
def get_available_speakers():
    """List all supported speaker profiles."""
    return list_available_speakers()
