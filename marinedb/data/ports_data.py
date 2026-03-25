"""
MarineDB - Major US Coastal Ports Data
"""

PORTS = {
    "sf": {
        "id": "sf",
        "name": "San Francisco Bay",
        "lat": 37.8,
        "lon": -122.4,
        "region": "Pacific Coast",
        "timezone": "America/Los_Angeles",
        "services": ["Fuel Dock", "Pumpout", "Restaurant", "Hotel", "Repair", "Launch Ramp"],
    },
    "mia": {
        "id": "mia",
        "name": "Miami",
        "lat": 25.8,
        "lon": -80.2,
        "region": "Florida Coast",
        "timezone": "America/New_York",
        "services": ["Fuel Dock", "Pumpout", "Restaurant", "Marina", "Bahamas Cruising"],
    },
    "sea": {
        "id": "sea",
        "name": "Seattle",
        "lat": 47.6,
        "lon": -122.3,
        "region": "Pacific Northwest",
        "timezone": "America/Los_Angeles",
        "services": ["Fuel Dock", "Pumpout", "Restaurant", "Hotel", "Repair", "Kayak Rental"],
    },
    "nyc": {
        "id": "nyc",
        "name": "New York Harbor",
        "lat": 40.7,
        "lon": -74.0,
        "region": "Atlantic Coast",
        "timezone": "America/New_York",
        "services": ["Fuel Dock", "Pumpout", "Restaurant", "Hotel", "Repair", "City Marina"],
    },
    "san": {
        "id": "san",
        "name": "San Diego",
        "lat": 32.7,
        "lon": -117.2,
        "region": "Pacific Coast",
        "timezone": "America/Los_Angeles",
        "services": ["Fuel Dock", "Pumpout", "Restaurant", "Hotel", "Repair", "Navy Base"],
    },
}

# Simplified harmonic constants for tide prediction (amplitude in feet, phase in degrees)
# M2 (principal lunar), S2 (principal solar) — the two dominant constituents
TIDE_HARMONICS = {
    "sf": {"M2_amp": 3.2, "M2_phase": 210, "S2_amp": 0.9, "S2_phase": 245},
    "mia": {"M2_amp": 1.4, "M2_phase": 85, "S2_amp": 0.3, "S2_phase": 120},
    "sea": {"M2_amp": 5.8, "M2_phase": 195, "S2_amp": 1.6, "S2_phase": 230},
    "nyc": {"M2_amp": 2.8, "M2_phase": 170, "S2_amp": 0.7, "S2_phase": 205},
    "san": {"M2_amp": 3.6, "M2_phase": 225, "S2_amp": 1.0, "S2_phase": 260},
}
