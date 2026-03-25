"""Standard lumber dimensions and pricing data."""

# Nominal vs Actual dimensions in inches
# Key: (thickness_in, width_in)
LUMBER_DIMENSIONS = {
    "1x2":  {"nominal": (1, 2),   "actual": (0.75, 1.5),   "bf_per_ft": 0.0833},
    "1x3":  {"nominal": (1, 3),   "actual": (0.75, 2.5),   "bf_per_ft": 0.125},
    "1x4":  {"nominal": (1, 4),   "actual": (0.75, 3.5),   "bf_per_ft": 0.1667},
    "1x6":  {"nominal": (1, 6),   "actual": (0.75, 5.5),   "bf_per_ft": 0.25},
    "1x8":  {"nominal": (1, 8),   "actual": (0.75, 7.25),  "bf_per_ft": 0.3333},
    "1x10": {"nominal": (1, 10),  "actual": (0.75, 9.25),  "bf_per_ft": 0.4167},
    "1x12": {"nominal": (1, 12),  "actual": (0.75, 11.25), "bf_per_ft": 0.5},
    "2x2":  {"nominal": (2, 2),   "actual": (1.5, 1.5),    "bf_per_ft": 0.1667},
    "2x3":  {"nominal": (2, 3),   "actual": (1.5, 2.5),    "bf_per_ft": 0.25},
    "2x4":  {"nominal": (2, 4),   "actual": (1.5, 3.5),    "bf_per_ft": 0.3333},
    "2x6":  {"nominal": (2, 6),   "actual": (1.5, 5.5),    "bf_per_ft": 0.5},
    "2x8":  {"nominal": (2, 8),   "actual": (1.5, 7.25),   "bf_per_ft": 0.6667},
    "2x10": {"nominal": (2, 10),  "actual": (1.5, 9.25),   "bf_per_ft": 0.8333},
    "2x12": {"nominal": (2, 12),  "actual": (1.5, 11.25),  "bf_per_ft": 1.0},
    "2x14": {"nominal": (2, 14),  "actual": (1.5, 13.25),  "bf_per_ft": 1.1667},
    "4x4":  {"nominal": (4, 4),   "actual": (3.5, 3.5),    "bf_per_ft": 0.6667},
    "4x6":  {"nominal": (4, 6),   "actual": (3.5, 5.5),    "bf_per_ft": 1.0},
    "6x6":  {"nominal": (6, 6),   "actual": (5.5, 5.5),    "bf_per_ft": 1.5},
}

# Price per board foot by wood type (USD)
WOOD_PRICES_PER_BF = {
    "pine":       1.50,
    "spruce":     1.60,
    "fir":        1.55,
    "cedar":      4.00,
    "redwood":    5.50,
    "poplar":     2.20,
    "maple":      3.50,
    "oak":        4.50,
    "ash":        3.80,
    "birch":      3.20,
    "cherry":     8.00,
    "walnut":     10.00,
    "mahogany":   12.00,
    " MDF":       1.00,
    "MDF":        1.00,
    "birch_plywood":  3.50,
    "oak_plywood":    5.00,
    "pine_plywood":   2.00,
}

# Default kerf width in inches
DEFAULT_KERF_INCHES = 0.125

# Labor rate per hour (USD)
LABOR_RATE_PER_HOUR = 45.00

# Square feet of cuts per labor hour (rough estimate)
SQFT_PER_LABOR_HOUR = 8.0
