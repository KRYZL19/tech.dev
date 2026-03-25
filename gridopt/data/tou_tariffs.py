from datetime import time

# 10 US utilities with realistic TOU tariff data
# Prices in $/kWh, times in local standard time (simplified)

TARIFFS = {
    "pge": {
        "name": "Pacific Gas & Electric",
        "state": "CA",
        "description": "PG&E E-TOU-C Residential Time-of-Use",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 14,
                "price": 0.045,
                "days": "all",
            },
            {
                "name": "partial-peak",
                "start_hour": 14,
                "end_hour": 21,
                "price": 0.068,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.095,
                "days": "all",
            },
        ],
        "flat_rate": 0.073,
    },
    "sce": {
        "name": "Southern California Edison",
        "state": "CA",
        "description": "SCE Time-of-Use (TOU-D) Residential",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 16,
                "price": 0.043,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 16,
                "end_hour": 21,
                "price": 0.102,
                "days": "all",
            },
            {
                "name": "off-peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.043,
                "days": "all",
            },
        ],
        "flat_rate": 0.078,
    },
    "sdge": {
        "name": "San Diego Gas & Electric",
        "state": "CA",
        "description": "SDG&E Power Residential TOU",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 14,
                "price": 0.052,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 14,
                "end_hour": 21,
                "price": 0.118,
                "days": "all",
            },
            {
                "name": "off-peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.052,
                "days": "all",
            },
        ],
        "flat_rate": 0.085,
    },
    "coned": {
        "name": "Consolidated Edison",
        "state": "NY",
        "description": "ConEd Time-of-Use Residential",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 15,
                "price": 0.032,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 15,
                "end_hour": 19,
                "price": 0.098,
                "days": "all",
            },
            {
                "name": "off-peak",
                "start_hour": 19,
                "end_hour": 24,
                "price": 0.032,
                "days": "all",
            },
        ],
        "flat_rate": 0.065,
    },
    "dominion": {
        "name": "Dominion Energy",
        "state": "VA",
        "description": "Dominion Residential Time-of-Use",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 15,
                "price": 0.028,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 15,
                "end_hour": 21,
                "price": 0.076,
                "days": "all",
            },
            {
                "name": "off-peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.028,
                "days": "all",
            },
        ],
        "flat_rate": 0.052,
    },
    "duke": {
        "name": "Duke Energy",
        "state": "NC",
        "description": "Duke Energy Carolinas Residential TOU",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 12,
                "price": 0.025,
                "days": "all",
            },
            {
                "name": "partial-peak",
                "start_hour": 12,
                "end_hour": 17,
                "price": 0.045,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 17,
                "end_hour": 21,
                "price": 0.085,
                "days": "all",
            },
            {
                "name": "partial-peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.045,
                "days": "all",
            },
        ],
        "flat_rate": 0.055,
    },
    "austin_energy": {
        "name": "Austin Energy",
        "state": "TX",
        "description": "Austin Energy Residential Time-of-Use",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 13,
                "price": 0.031,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 13,
                "end_hour": 19,
                "price": 0.085,
                "days": "all",
            },
            {
                "name": "off-peak",
                "start_hour": 19,
                "end_hour": 24,
                "price": 0.031,
                "days": "all",
            },
        ],
        "flat_rate": 0.058,
    },
    "smud": {
        "name": "Sacramento Municipal Utility District",
        "state": "CA",
        "description": "SMUD Time-of-Use Residential",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 17,
                "price": 0.038,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 17,
                "end_hour": 21,
                "price": 0.088,
                "days": "all",
            },
            {
                "name": "off-peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.038,
                "days": "all",
            },
        ],
        "flat_rate": 0.063,
    },
    "aps": {
        "name": "Arizona Public Service",
        "state": "AZ",
        "description": "APS Time-of-Use Residential",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 15,
                "price": 0.034,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 15,
                "end_hour": 21,
                "price": 0.092,
                "days": "all",
            },
            {
                "name": "off-peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.034,
                "days": "all",
            },
        ],
        "flat_rate": 0.063,
    },
    "xcel": {
        "name": "Xcel Energy",
        "state": "CO",
        "description": "Xcel Energy Colorado Residential TOU",
        "periods": [
            {
                "name": "off-peak",
                "start_hour": 0,
                "end_hour": 12,
                "price": 0.029,
                "days": "all",
            },
            {
                "name": "partial-peak",
                "start_hour": 12,
                "end_hour": 17,
                "price": 0.048,
                "days": "all",
            },
            {
                "name": "peak",
                "start_hour": 17,
                "end_hour": 21,
                "price": 0.078,
                "days": "all",
            },
            {
                "name": "partial-peak",
                "start_hour": 21,
                "end_hour": 24,
                "price": 0.048,
                "days": "all",
            },
        ],
        "flat_rate": 0.055,
    },
}


def get_tariff(utility_id: str) -> dict | None:
    return TARIFFS.get(utility_id.lower())


def search_tariffs(query: str) -> list[dict]:
    q = query.lower()
    results = []
    for key, tariff in TARIFFS.items():
        if q in tariff["name"].lower() or q in tariff["state"].lower() or q in key:
            results.append({"id": key, **tariff})
    return results


def get_all_tariffs() -> list[dict]:
    return [{"id": key, **tariff} for key, tariff in TARIFFS.items()]
