# VIN Patterns & WMI Registry
# Characters 1-3: World Manufacturer Identifier (WMI)

WMI_REGISTRY = {
    # Yamaha
    "1HD": {"make": "Yamaha", "country": "USA"},
    "JYJ": {"make": "Yamaha", "country": "Japan"},
    "RB1": {"make": "Yamaha", "country": "Japan"},  # newer Yamaha

    # Kawasaki
    "JK1": {"make": "Kawasaki", "country": "Japan"},
    "JK2": {"make": "Kawasaki", "country": "Japan"},
    "JN1": {"make": "Kawasaki", "country": "Japan"},

    # Honda
    "1H8": {"make": "Honda", "country": "USA"},
    "MH1": {"make": "Honda", "country": "Japan"},
    "JH2": {"make": "Honda", "country": "Japan"},
    "JH1": {"make": "Honda", "country": "Japan"},

    # Suzuki
    "JS1": {"make": "Suzuki", "country": "Japan"},
    "JSA": {"make": "Suzuki", "country": "Japan"},
    "JS2": {"make": "Suzuki", "country": "Japan"},

    # Harley-Davidson
    "1HD": {"make": "Harley-Davidson", "country": "USA"},
    "5HD": {"make": "Harley-Davidson", "country": "USA"},
    "HD1": {"make": "Harley-Davidson", "country": "USA"},

    # BMW Motorrad
    "WB1": {"make": "BMW", "country": "Germany"},
    "WBS": {"make": "BMW", "country": "Germany"},
    "WB3": {"make": "BMW", "country": "Germany"},
    "WBA": {"make": "BMW", "country": "Germany"},

    # Ducati
    "ZDM": {"make": "Ducati", "country": "Italy"},
    "ZDF": {"make": "Ducati", "country": "Italy"},

    # KTM
    "VBK": {"make": "KTM", "country": "Austria"},
    "L5K": {"make": "KTM", "country": "Austria"},

    # Triumph
    "ZAA": {"make": "Triumph", "country": "UK"},
    "ZVM": {"make": "Triumph", "country": "UK"},
    "SMT": {"make": "Triumph", "country": "UK"},
}

# Year codes (Character 10)
YEAR_CODES = {
    "A": 2010, "B": 2011, "C": 2012, "D": 2013, "E": 2014,
    "F": 2015, "G": 2016, "H": 2017, "J": 2018, "K": 2019,
    "L": 2020, "M": 2021, "N": 2022, "P": 2023, "R": 2024,
    "S": 2025, "T": 2026, "V": 2027, "W": 2028, "X": 2029,
    "Y": 2030
}

# Check digit weights (position 1-8 and 10-17)
CHECK_DIGIT_WEIGHTS = {
    1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 10,
    9: 0,  # check digit position (not used in calc)
    10: 9, 11: 8, 12: 7, 13: 6, 14: 5, 15: 4, 16: 3, 17: 2
}

# Transliteration table for check digit
TRANSLITERATION = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
    "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "P": 7, "Q": 8, "R": 9,
    "S": 2, "T": 3, "U": 4, "V": 5, "W": 6, "X": 7, "Y": 8, "Z": 9,
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
}

# Motorcycle specs database
MODEL_SPECS = {
    ("Yamaha", "MT-09", 2019): {
        "engine_cc": 847, "hp": 115, "wet_weight_kg": 193, "frame_type": "Diamond", "model": "MT-09"
    },
    ("Yamaha", "MT-09", 2021): {
        "engine_cc": 889, "hp": 119, "wet_weight_kg": 190, "frame_type": "Diamond", "model": "MT-09"
    },
    ("Yamaha", "MT-09", 2022): {
        "engine_cc": 889, "hp": 119, "wet_weight_kg": 190, "frame_type": "Diamond", "model": "MT-09"
    },
    ("Yamaha", "MT-09", 2023): {
        "engine_cc": 889, "hp": 119, "wet_weight_kg": 193, "frame_type": "Diamond", "model": "MT-09"
    },
    ("Yamaha", "R1", 2020): {
        "engine_cc": 998, "hp": 200, "wet_weight_kg": 201, "frame_type": "Deltabox", "model": "R1"
    },
    ("Yamaha", "R1", 2022): {
        "engine_cc": 998, "hp": 200, "wet_weight_kg": 199, "frame_type": "Deltabox", "model": "R1"
    },
    ("Kawasaki", "Ninja ZX-10R", 2021): {
        "engine_cc": 998, "hp": 203, "wet_weight_kg": 207, "frame_type": "Twin-spar", "model": "Ninja ZX-10R"
    },
    ("Kawasaki", "Ninja ZX-10R", 2023): {
        "engine_cc": 998, "hp": 203, "wet_weight_kg": 207, "frame_type": "Twin-spar", "model": "Ninja ZX-10R"
    },
    ("Kawasaki", "Z900", 2022): {
        "engine_cc": 948, "hp": 125, "wet_weight_kg": 212, "frame_type": "Trellis", "model": "Z900"
    },
    ("Kawasaki", "Z900", 2023): {
        "engine_cc": 948, "hp": 125, "wet_weight_kg": 212, "frame_type": "Trellis", "model": "Z900"
    },
    ("Honda", "CBR1000RR", 2021): {
        "engine_cc": 999, "hp": 214, "wet_weight_kg": 201, "frame_type": "Twin-spar", "model": "CBR1000RR-R"
    },
    ("Honda", "CBR1000RR", 2022): {
        "engine_cc": 999, "hp": 217, "wet_weight_kg": 199, "frame_type": "Twin-spar", "model": "CBR1000RR-R"
    },
    ("Honda", "CB650R", 2022): {
        "engine_cc": 649, "hp": 94, "wet_weight_kg": 208, "frame_type": "Diamond", "model": "CB650R"
    },
    ("Honda", "CB650R", 2023): {
        "engine_cc": 649, "hp": 94, "wet_weight_kg": 208, "frame_type": "Diamond", "model": "CB650R"
    },
    ("Suzuki", "GSX-R1000", 2019): {
        "engine_cc": 999, "hp": 199, "wet_weight_kg": 203, "frame_type": "Twin-spar", "model": "GSX-R1000"
    },
    ("Suzuki", "GSX-R1000", 2021): {
        "engine_cc": 999, "hp": 199, "wet_weight_kg": 203, "frame_type": "Twin-spar", "model": "GSX-R1000"
    },
    ("Suzuki", "SV650", 2021): {
        "engine_cc": 645, "hp": 75, "wet_weight_kg": 196, "frame_type": "Steel trellis", "model": "SV650"
    },
    ("Suzuki", "SV650", 2023): {
        "engine_cc": 645, "hp": 76, "wet_weight_kg": 196, "frame_type": "Steel trellis", "model": "SV650"
    },
    ("Harley-Davidson", "Iron 883", 2020): {
        "engine_cc": 883, "hp": 50, "wet_weight_kg": 256, "frame_type": "Steel", "model": "Iron 883"
    },
    ("Harley-Davidson", "Iron 883", 2022): {
        "engine_cc": 883, "hp": 53, "wet_weight_kg": 256, "frame_type": "Steel", "model": "Iron 883"
    },
    ("Harley-Davidson", "Sportster S", 2021): {
        "engine_cc": 1250, "hp": 121, "wet_weight_kg": 228, "frame_type": "Aluminum", "model": "Sportster S"
    },
    ("Harley-Davidson", "Sportster S", 2023): {
        "engine_cc": 1250, "hp": 121, "wet_weight_kg": 228, "frame_type": "Aluminum", "model": "Sportster S"
    },
    ("BMW", "S1000RR", 2021): {
        "engine_cc": 999, "hp": 207, "wet_weight_kg": 197, "frame_type": "Aluminum", "model": "S1000RR"
    },
    ("BMW", "S1000RR", 2023): {
        "engine_cc": 999, "hp": 210, "wet_weight_kg": 197, "frame_type": "Aluminum", "model": "S1000RR"
    },
    ("BMW", "R1250GS", 2022): {
        "engine_cc": 1254, "hp": 136, "wet_weight_kg": 268, "frame_type": "Steel", "model": "R1250GS"
    },
    ("BMW", "R1250GS", 2023): {
        "engine_cc": 1254, "hp": 136, "wet_weight_kg": 268, "frame_type": "Steel", "model": "R1250GS"
    },
    ("Ducati", "Panigale V4", 2022): {
        "engine_cc": 1103, "hp": 214, "wet_weight_kg": 198, "frame_type": "Aluminum", "model": "Panigale V4"
    },
    ("Ducati", "Panigale V4", 2023): {
        "engine_cc": 1103, "hp": 215, "wet_weight_kg": 198, "frame_type": "Aluminum", "model": "Panigale V4"
    },
    ("Ducati", "Monster", 2022): {
        "engine_cc": 937, "hp": 111, "wet_weight_kg": 188, "frame_type": "Aluminum", "model": "Monster"
    },
    ("Ducati", "Monster", 2023): {
        "engine_cc": 937, "hp": 111, "wet_weight_kg": 188, "frame_type": "Aluminum", "model": "Monster"
    },
    ("KTM", "1290 Super Duke R", 2022): {
        "engine_cc": 1301, "hp": 180, "wet_weight_kg": 189, "frame_type": "Chromium", "model": "1290 Super Duke R"
    },
    ("KTM", "1290 Super Duke R", 2023): {
        "engine_cc": 1301, "hp": 180, "wet_weight_kg": 189, "frame_type": "Chromium", "model": "1290 Super Duke R"
    },
    ("KTM", "390 Duke", 2022): {
        "engine_cc": 373, "hp": 43, "wet_weight_kg": 150, "frame_type": "Chromium", "model": "390 Duke"
    },
    ("KTM", "390 Duke", 2023): {
        "engine_cc": 373, "hp": 43, "wet_weight_kg": 150, "frame_type": "Chromium", "model": "390 Duke"
    },
    ("Triumph", "Street Triple RS", 2022): {
        "engine_cc": 765, "hp": 118, "wet_weight_kg": 188, "frame_type": "Aluminum", "model": "Street Triple RS"
    },
    ("Triumph", "Street Triple RS", 2023): {
        "engine_cc": 765, "hp": 118, "wet_weight_kg": 188, "frame_type": "Aluminum", "model": "Street Triple RS"
    },
    ("Triumph", "Bonneville T120", 2022): {
        "engine_cc": 1200, "hp": 79, "wet_weight_kg": 236, "frame_type": "Steel", "model": "Bonneville T120"
    },
    ("Triumph", "Bonneville T120", 2023): {
        "engine_cc": 1200, "hp": 79, "wet_weight_kg": 236, "frame_type": "Steel", "model": "Bonneville T120"
    },
}
