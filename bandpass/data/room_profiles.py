"""
Speaker profiles for 15 popular studio monitors and speakers.
Data includes frequency response characteristics and crossover recommendations.
"""

SPEAKER_PROFILES = {
    "yamaha_hs8": {
        "manufacturer": "Yamaha",
        "model": "HS8",
        "type": "bookshelf",
        "frequency_range": "43Hz - 30kHz",
        "max_spl": 120,
        "xover_recommended": 80,
        "bass_characteristics": "tight, accurate",
        "frequency_curve": [
            {"freq": 40, "spl": -6}, {"freq": 50, "spl": -2}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0.5}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": -0.5}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -1}, {"freq": 20000, "spl": -2}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 1.5, "reason": "HS8 rolls off earlier than competitors"},
            {"freq": 63, "boost": 1.0, "reason": "Compensate for port tuning"}
        ]
    },
    "jbl_308p": {
        "manufacturer": "JBL",
        "model": "308P MkII",
        "type": "bookshelf",
        "frequency_range": "45Hz - 20kHz",
        "max_spl": 112,
        "xover_recommended": 80,
        "bass_characteristics": "punchy, present",
        "frequency_curve": [
            {"freq": 40, "spl": -8}, {"freq": 50, "spl": -3}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0.5}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0.5}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -0.5}, {"freq": 20000, "spl": -1}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 2.0, "reason": "JBL's slip stream port adds low-end"},
            {"freq": 63, "boost": 1.0, "reason": "Balance port resonance"}
        ]
    },
    "adam_a7x": {
        "manufacturer": "Adam",
        "model": "A7X",
        "type": "bookshelf",
        "frequency_range": "42Hz - 50kHz",
        "max_spl": 114,
        "xover_recommended": 2500,
        "bass_characteristics": "detailed, fast",
        "frequency_curve": [
            {"freq": 40, "spl": -5}, {"freq": 50, "spl": -1}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0.5},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0.5}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": 1}, {"freq": 20000, "spl": 0.5}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 1.5, "reason": "X-ART tweeter extends highs, may need bass balance"},
            {"freq": 63, "boost": 1.0, "reason": "Slight dip around crossover region"}
        ]
    },
    "krk_rokit8": {
        "manufacturer": "KRK",
        "model": "Rokit 8 G4",
        "type": "bookshelf",
        "frequency_range": "36Hz - 40kHz",
        "max_spl": 118,
        "xover_recommended": 80,
        "bass_characteristics": "enhanced, fun",
        "frequency_curve": [
            {"freq": 40, "spl": 0}, {"freq": 50, "spl": 1.5}, {"freq": 63, "spl": 2},
            {"freq": 80, "spl": 1}, {"freq": 100, "spl": 0.5}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -0.5}, {"freq": 20000, "spl": -1}
        ],
        "bass_boost_recommendations": [
            {"freq": 63, "boost": -2.0, "reason": "KRK has boosted bass, consider cutting"},
            {"freq": 50, "boost": -1.5, "reason": "Reduce low-end bloom for accuracy"}
        ]
    },
    "presonus_eris_e8": {
        "manufacturer": "PreSonus",
        "model": "Eris E8",
        "type": "bookshelf",
        "frequency_range": "45Hz - 20kHz",
        "max_spl": 105,
        "xover_recommended": 80,
        "bass_characteristics": "neutral, controlled",
        "frequency_curve": [
            {"freq": 40, "spl": -7}, {"freq": 50, "spl": -2}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -1}, {"freq": 20000, "spl": -2}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 2.0, "reason": "Extend low-frequency response"},
            {"freq": 63, "boost": 1.0, "reason": "Smooth the roll-off"}
        ]
    },
    "genelec_8030": {
        "manufacturer": "Genelec",
        "model": "8030C",
        "type": "bookshelf",
        "frequency_range": "47Hz - 25kHz",
        "max_spl": 104,
        "xover_recommended": 80,
        "bass_characteristics": "extremely accurate",
        "frequency_curve": [
            {"freq": 40, "spl": -8}, {"freq": 50, "spl": -3}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": 0}, {"freq": 20000, "spl": -0.5}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 2.5, "reason": "Genelec's ISS power saving may reduce bass output"},
            {"freq": 63, "boost": 1.0, "reason": "Natural room gain compensation"}
        ]
    },
    "neumann_kh80": {
        "manufacturer": "Neumann",
        "model": "KH 80 DSP",
        "type": "bookshelf",
        "frequency_range": "53Hz - 21kHz",
        "max_spl": 118,
        "xover_recommended": 80,
        "bass_characteristics": "studio reference",
        "frequency_curve": [
            {"freq": 40, "spl": -10}, {"freq": 50, "spl": -5}, {"freq": 63, "spl": -1},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -0.5}, {"freq": 20000, "spl": -1}
        ],
        "bass_boost_recommendations": [
            {"freq": 63, "boost": 1.5, "reason": "DSP correction may need manual fine-tuning"},
            {"freq": 80, "boost": 0.5, "reason": "Align with tweeter output"}
        ]
    },
    "focal_alpha65": {
        "manufacturer": "Focal",
        "model": "Alpha 65",
        "type": "bookshelf",
        "frequency_range": "40Hz - 22kHz",
        "max_spl": 109,
        "xover_recommended": 100,
        "bass_characteristics": "dynamic, detailed",
        "frequency_curve": [
            {"freq": 40, "spl": -4}, {"freq": 50, "spl": 0}, {"freq": 63, "spl": 0.5},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0.5},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0.5}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": 0.5}, {"freq": 20000, "spl": 0}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 1.5, "reason": "Polyglass cone provides warm bass"},
            {"freq": 63, "boost": 0.5, "reason": "Balance aluminum inverted dome tweeter"}
        ]
    },
    "rockville_8": {
        "manufacturer": "Rockville",
        "model": "RMB08",
        "type": "bookshelf",
        "frequency_range": "50Hz - 20kHz",
        "max_spl": 110,
        "xover_recommended": 80,
        "bass_characteristics": "budget-friendly accurate",
        "frequency_curve": [
            {"freq": 40, "spl": -10}, {"freq": 50, "spl": -4}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": -0.5},
            {"freq": 15000, "spl": -1}, {"freq": 20000, "spl": -2}
        ],
        "bass_boost_recommendations": [
            {"freq": 63, "boost": 2.5, "reason": "Budget driver needs low-end compensation"},
            {"freq": 50, "boost": 2.0, "reason": "Extend bass response"}
        ]
    },
    "edifier_1280": {
        "manufacturer": "Edifier",
        "model": "1280T",
        "type": "bookshelf",
        "frequency_range": "55Hz - 20kHz",
        "max_spl": 106,
        "xover_recommended": 80,
        "bass_characteristics": "consumer-tuned warm",
        "frequency_curve": [
            {"freq": 40, "spl": -12}, {"freq": 50, "spl": -6}, {"freq": 63, "spl": -1},
            {"freq": 80, "spl": 1}, {"freq": 100, "spl": 0.5}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -1}, {"freq": 20000, "spl": -2}
        ],
        "bass_boost_recommendations": [
            {"freq": 80, "boost": -1.5, "reason": "Edifier adds warmth, may need reduction"},
            {"freq": 63, "boost": -1.0, "reason": "Consumer tuning compensation"}
        ]
    },
    "jbl_305p": {
        "manufacturer": "JBL",
        "model": "305P MkII",
        "type": "bookshelf",
        "frequency_range": "49Hz - 20kHz",
        "max_spl": 108,
        "xover_recommended": 80,
        "bass_characteristics": "clear, balanced",
        "frequency_curve": [
            {"freq": 40, "spl": -10}, {"freq": 50, "spl": -4}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0.5}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0.5}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -0.5}, {"freq": 20000, "spl": -1}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 2.5, "reason": "5-inch driver needs bass extension help"},
            {"freq": 63, "boost": 1.5, "reason": "Balance the LSR driver"}
        ]
    },
    "yamaha_hs7": {
        "manufacturer": "Yamaha",
        "model": "HS7",
        "type": "bookshelf",
        "frequency_range": "43Hz - 30kHz",
        "max_spl": 106,
        "xover_recommended": 80,
        "bass_characteristics": "reference accurate",
        "frequency_curve": [
            {"freq": 40, "spl": -7}, {"freq": 50, "spl": -2}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0.5}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": -0.5}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -1}, {"freq": 20000, "spl": -2}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 1.5, "reason": "6.5-inch driver rolls off earlier"},
            {"freq": 63, "boost": 1.0, "reason": "Match HS8 voicing"}
        ]
    },
    "mackie_mr624": {
        "manufacturer": "Mackie",
        "model": "MR624",
        "type": "bookshelf",
        "frequency_range": "45Hz - 20kHz",
        "max_spl": 108,
        "xover_recommended": 80,
        "bass_characteristics": "translucent midrange",
        "frequency_curve": [
            {"freq": 40, "spl": -8}, {"freq": 50, "spl": -3}, {"freq": 63, "spl": 0},
            {"freq": 80, "spl": 0}, {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0},
            {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0},
            {"freq": 4000, "spl": 0.5}, {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": 0},
            {"freq": 15000, "spl": -0.5}, {"freq": 20000, "spl": -1}
        ],
        "bass_boost_recommendations": [
            {"freq": 50, "boost": 2.0, "reason": "Mackie's 6.5-inch waveguide needs support"},
            {"freq": 63, "boost": 1.0, "reason": "Match logarithmic spacing"}
        ]
    },
    "avantone_mixcube": {
        "manufacturer": "Avantone",
        "model": "MixCube",
        "type": "bookshelf",
        "frequency_range": "90Hz - 17kHz",
        "max_spl": 94,
        "xover_recommended": 100,
        "bass_characteristics": "midrange reference only",
        "frequency_curve": [
            {"freq": 63, "spl": -15}, {"freq": 80, "spl": -8}, {"freq": 100, "spl": -3},
            {"freq": 200, "spl": 0}, {"freq": 500, "spl": 0}, {"freq": 1000, "spl": 0},
            {"freq": 2000, "spl": 0}, {"freq": 4000, "spl": 0.5}, {"freq": 8000, "spl": 0},
            {"freq": 10000, "spl": 0}, {"freq": 15000, "spl": -1}, {"freq": 20000, "spl": -3}
        ],
        "bass_boost_recommendations": [
            {"freq": 100, "boost": 4.0, "reason": "MixCube is passive midrange only"},
            {"freq": 80, "boost": 3.0, "reason": "Add subwoofer crossover integration"}
        ]
    },
    "kal.mark": {
        "manufacturer": "Kal",
        "model": "Mark 10",
        "type": "tower",
        "frequency_range": "25Hz - 20kHz",
        "max_spl": 120,
        "xover_recommended": 60,
        "bass_characteristics": "extended deep bass",
        "frequency_curve": [
            {"freq": 25, "spl": -3}, {"freq": 31, "spl": 0}, {"freq": 40, "spl": 0.5},
            {"freq": 50, "spl": 0}, {"freq": 63, "spl": 0}, {"freq": 80, "spl": 0},
            {"freq": 100, "spl": 0}, {"freq": 200, "spl": 0}, {"freq": 500, "spl": 0},
            {"freq": 1000, "spl": 0}, {"freq": 2000, "spl": 0}, {"freq": 4000, "spl": 0},
            {"freq": 8000, "spl": 0}, {"freq": 10000, "spl": -0.5}, {"freq": 20000, "spl": -1}
        ],
        "bass_boost_recommendations": [
            {"freq": 31, "boost": -1.5, "reason": "Tower speakers may have boosted low bass"},
            {"freq": 40, "boost": -0.5, "reason": "Control port noise"}
        ]
    }
}


def get_speaker_profile(manufacturer: str, model: str):
    """Find speaker profile by manufacturer and model (fuzzy match)."""
    manufacturer_lower = manufacturer.lower()
    model_lower = model.lower()
    
    for key, profile in SPEAKER_PROFILES.items():
        if (manufacturer_lower in profile["manufacturer"].lower() or 
            profile["manufacturer"].lower() in manufacturer_lower) and \
           (model_lower in profile["model"].lower() or 
            profile["model"].lower() in model_lower or
            any(part in model_lower for part in profile["model"].lower().split())):
            return profile
    
    return None


def list_available_speakers():
    """Return list of all available speaker profiles."""
    return [
        {
            "key": key,
            "manufacturer": p["manufacturer"],
            "model": p["model"],
            "type": p["type"],
            "frequency_range": p["frequency_range"]
        }
        for key, p in SPEAKER_PROFILES.items()
    ]
