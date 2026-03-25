# Bundled soil and county data for SEPTICODE

# 6 soil types with standard percolation rates (minutes per inch)
SOIL_TYPES = {
    "sand": {
        "perc_rate": 5,
        "description": "Excellent drainage. Fastest percolation.",
        "suitable_for": ["conventional", "raised bed"],
    },
    "loamy sand": {
        "perc_rate": 15,
        "description": "Good drainage. Ideal for standard systems.",
        "suitable_for": ["conventional", "chambered"],
    },
    "sandy loam": {
        "perc_rate": 25,
        "description": "Moderate drainage. Most common soil type.",
        "suitable_for": ["conventional", "chambered", "drip"],
    },
    "loam": {
        "perc_rate": 45,
        "description": "Average drainage. May need larger drainfield.",
        "suitable_for": ["chambered", "drip", "mound"],
    },
    "silt loam": {
        "perc_rate": 60,
        "description": "Slow drainage. Requires advanced systems.",
        "suitable_for": ["drip", "mound", "at-grade"],
    },
    "clay": {
        "perc_rate": 120,
        "description": "Poor drainage. Requires specialized engineering.",
        "suitable_for": ["mound", "at-grade", "aerobic"],
    },
}

# 10 county examples across CA, TX, FL, NC, WA
COUNTY_DATA = {
    # California counties
    "fresno": {
        "state": "CA",
        "soil_types": ["sandy loam", "loam", "clay"],
        "perc_rates": [25, 45, 120],
        "groundwater_risk": "moderate",
        "notes": "Requires 100ft setback from wells in groundwater protection zones.",
    },
    "los angeles": {
        "state": "CA",
        "soil_types": ["sandy loam", "loam", "clay"],
        "perc_rates": [25, 45, 120],
        "groundwater_risk": "low",
        "notes": "Coastal counties may have additional coastal commission requirements.",
    },
    "sacramento": {
        "state": "CA",
        "soil_types": ["sandy loam", "loam", "silt loam"],
        "perc_rates": [25, 45, 60],
        "groundwater_risk": "high",
        "notes": "High groundwater areas require mound or at-grade systems.",
    },
    "san diego": {
        "state": "CA",
        "soil_types": ["sandy loam", "loam", "clay"],
        "perc_rates": [25, 45, 120],
        "groundwater_risk": "low",
        "notes": "Semi-arid climate; evaporation rates affect sizing.",
    },
    # Texas counties
    "harris": {
        "state": "TX",
        "soil_types": ["sandy loam", "loam", "clay"],
        "perc_rates": [25, 45, 120],
        "groundwater_risk": "moderate",
        "notes": " TCEQ requires 150ft from water supply wells.",
    },
    "travis": {
        "state": "TX",
        "soil_types": ["sandy loam", "loam", "clay"],
        "perc_rates": [25, 45, 120],
        "groundwater_risk": "high",
        "notes": "Edwards Aquifer protection zone additional requirements.",
    },
    # Florida counties
    "miami-dade": {
        "state": "FL",
        "soil_types": ["sandy loam", "loam", "silt loam"],
        "perc_rates": [25, 45, 60],
        "groundwater_risk": "high",
        "notes": "High water table. Most systems require mound or fill.",
    },
    "hillsborough": {
        "state": "FL",
        "soil_types": ["sandy loam", "loam", "silt loam"],
        "perc_rates": [25, 45, 60],
        "groundwater_risk": "moderate",
        "notes": "Requires 75ft setback from surface waters.",
    },
    # North Carolina
    "wake": {
        "state": "NC",
        "soil_types": ["sandy loam", "loam", "clay"],
        "perc_rates": [25, 45, 120],
        "groundwater_risk": "moderate",
        "notes": "NC DHHS requires 30ft setback from property lines.",
    },
    # Washington
    "king": {
        "state": "WA",
        "soil_types": ["sandy loam", "loam", "silt loam"],
        "perc_rates": [25, 45, 60],
        "groundwater_risk": "high",
        "notes": "High rainfall area. Sizing calculations account for wet season.",
    },
}

# State-specific setback rules
STATE_SETBACKS = {
    "CA": {
        "property_line_ft": 5,
        "well_ft": 100,
        "surface_water_ft": 100,
        "foundation_ft": 5,
        "notes": "California Title 24, Part 5, Chapter 2.",
    },
    "TX": {
        "property_line_ft": 5,
        "well_ft": 150,
        "surface_water_ft": 50,
        "foundation_ft": 10,
        "notes": "TCEQ Chapter 285 rules for on-site sewage facilities.",
    },
    "FL": {
        "property_line_ft": 10,
        "well_ft": 75,
        "surface_water_ft": 75,
        "foundation_ft": 10,
        "notes": "Florida Administrative Code 64E-6.",
    },
    "NC": {
        "property_line_ft": 30,
        "well_ft": 100,
        "surface_water_ft": 100,
        "foundation_ft": 10,
        "notes": "NCGAC 15A NCAC 18A .1900.",
    },
    "WA": {
        "property_line_ft": 5,
        "well_ft": 100,
        "surface_water_ft": 100,
        "foundation_ft": 5,
        "notes": "Washington WAC 246-272A.",
    },
}

# System type requirements by bedrooms
SYSTEM_SIZING = {
    "tank_size_gallons": {
        1: 500,
        2: 750,
        3: 1000,
        4: 1250,
        5: 1500,
        6: 2000,
    },
    "daily_flow_gallons_per_bedroom": 75,
    "drainfield_sqft_per_gallon": 2.0,  # square feet of drainfield per gallon of daily flow
}


def get_soil_types() -> list:
    return list(SOIL_TYPES.keys())


def get_counties() -> dict:
    result = {}
    for county, data in COUNTY_DATA.items():
        result[county] = {"state": data["state"]}
    return result


def get_county_soil(county_name: str) -> dict | None:
    county_lower = county_name.lower()
    if county_lower not in COUNTY_DATA:
        return None
    data = COUNTY_DATA[county_lower]
    soil_info = []
    for i, soil_type in enumerate(data["soil_types"]):
        soil_info.append({
            "soil_type": soil_type,
            "perc_rate": data["perc_rates"][i],
            "description": SOIL_TYPES.get(soil_type, {}).get("description", ""),
        })
    return {
        "county": county_lower,
        "state": data["state"],
        "soils": soil_info,
        "groundwater_risk": data["groundwater_risk"],
        "notes": data["notes"],
    }
