"""Emission factors for carbon calculations — industry-standard values."""

# Shipping emission factors (grams CO2 per ton-nautical mile)
SHIPPING_EMISSION_FACTORS = {
    "container": 0.016,   # g CO2/t-nm
    "bulk": 0.006,        # g CO2/t-nm
    "roro": 0.022,        # g CO2/t-nm
}

# Truck emission factors (kg CO2 per ton-km)
TRUCK_EMISSION_FACTORS = {
    ("diesel", "standard"): 0.062,
    ("diesel", "heavy"): 0.080,
    ("lng", "standard"): 0.050,
    ("lng", "heavy"): 0.065,
    ("electric", "standard"): 0.035,
    ("electric", "heavy"): 0.045,
}

# Aviation emission factors (kg CO2 per passenger-km)
AVIATION_EMISSION_FACTORS = {
    "short_haul": 0.255,   # < 1500 km
    "long_haul": 0.195,    # >= 1500 km
}

# Tree sequestration (kg CO2 absorbed per tree per year, over 20-year lifetime)
TREE_SEQ_PER_YEAR = 21.0          # kg CO2/tree/year
TREE_SEQ_TOTAL = TREE_SEQ_PER_YEAR * 20  # 420 kg CO2/tree over 20 years
TREE_COST_USD = 15.0              # cost to plant one tree

# Diesel fuel density (kg CO2 per liter)
DIESEL_CO2_PER_LITER = 2.68   # kg CO2/L
LNG_CO2_PER_KG = 2.75         # kg CO2/kg

# Average truck fuel consumption (liters per 100 ton-km)
TRUCK_FUEL_PER_100_TKM = 3.5  # L/100t-km (diesel standard)

# Comparison基准: truck diesel heavy, 300 km avg
TRUCK_CO2_PER_TKM = 0.080     # kg CO2/t-km for heavy diesel truck
