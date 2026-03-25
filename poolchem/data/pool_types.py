# Pool chemistry constants and lookup data

# Temperature factor for LSI (Fahrenheit)
TEMP_FACTORS_F = {
    32: 2.1, 37: 2.0, 43: 1.9, 48: 1.8, 54: 1.7,
    60: 1.6, 66: 1.5, 72: 1.4, 77: 1.3, 82: 1.2,
    88: 1.1, 94: 1.0, 100: 0.9, 105: 0.8, 110: 0.7,
}

# Alkalinity factor for LSI (ppm as CaCO3)
def alkalinity_factor(alkalinity_ppm: float) -> float:
    return (alkalinity_ppm / 100) * 0.08

# Calcium hardness factor for LSI (ppm as CaCO3)
def calcium_factor(hardness_ppm: float) -> float:
    return (hardness_ppm / 100) * 0.1

# Chlorine demand multiplier by CYA level
# When CYA > 150ppm, chlorine effectiveness drops dramatically
CHLORINE_DEMAND_CURVES = {
    # CYA range: (demand_multiplier, effectiveness_note)
    (0, 30): (1.0, "Optimal chlorine efficiency"),
    (30, 50): (1.2, "Slightly reduced chlorine efficiency"),
    (50, 80): (1.5, "Moderately reduced chlorine efficiency"),
    (80, 100): (2.0, "Significantly reduced — consider dilution"),
    (100, 150): (2.5, "Severe demand — dilution strongly recommended"),
    (150, 1000): (4.0, "CRITICAL: FCI doubles demand overnight"),
}

# pH adjustment rates (oz of chemical per 10,000 gallons to move pH by 0.2)
PH_RAISE_SODA_ASH = 6.0   # oz sodium carbonate per 10k gallons per 0.2 pH
PH_LOWER_MURIATIC = 16.0  # oz muriatic acid (32%) per 10k gallons per 0.2 pH

# Chlorine product strengths
CHLORINE_TYPES = {
    "liquid": {"avail氯": 0.12, "oz_per_gallon": 128, "cost_per_lb": 2.50},
    "di-chlor": {"avail氯": 0.62, "oz_per_gallon": None, "cost_per_lb": 3.80},
    "tri-chlor": {"avail氯": 0.90, "oz_per_gallon": None, "cost_per_lb": 4.20},
    "cal-hypo": {"avail氯": 0.65, "oz_per_gallon": None, "cost_per_lb": 3.50},
    "gas": {"avail氯": 1.0, "oz_per_gallon": None, "cost_per_lb": 5.00},
}

# pH buffer constants
PH_BUFFER_IGNORE = 4.5  # Below this pH, water is too acidic to buffer
PH_BUFFER_OPTIMAL = 7.5  # Optimal pH for buffering

# LSI balanced range
LSI_BALANCED_MIN = -0.3
LSI_BALANCED_MAX = 0.3

# Recommended ranges
RECOMMENDED = {
    "ph": (7.2, 7.6),
    "alkalinity": (80, 120),
    "chlorine": (1.0, 3.0),
    "calcium_hardness": (200, 400),
    "cya": (30, 50),
}
