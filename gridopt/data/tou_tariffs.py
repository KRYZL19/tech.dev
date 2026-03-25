"""Bundled TOU tariff data for sample US utilities."""

TARIFFS = {
    "pge": {
        "utility_id": "pge",
        "utility_name": "Pacific Gas & Electric",
        "state": "California",
        "timezone": "America/Los_Angeles",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 7, "price_per_kwh": 0.22},
            {"name": "partial-peak", "start_hour": 7, "end_hour": 14, "price_per_kwh": 0.34},
            {"name": "peak", "start_hour": 14, "end_hour": 21, "price_per_kwh": 0.52},
            {"name": "partial-peak", "start_hour": 21, "end_hour": 24, "price_per_kwh": 0.34},
        ],
    },
    "sce": {
        "utility_id": "sce",
        "utility_name": "Southern California Edison",
        "state": "California",
        "timezone": "America/Los_Angeles",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 8, "price_per_kwh": 0.21},
            {"name": "on-peak", "start_hour": 8, "end_hour": 20, "price_per_kwh": 0.48},
            {"name": "off-peak", "start_hour": 20, "end_hour": 24, "price_per_kwh": 0.21},
        ],
    },
    "sdge": {
        "utility_id": "sdge",
        "utility_name": "San Diego Gas & Electric",
        "state": "California",
        "timezone": "America/Los_Angeles",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 6, "price_per_kwh": 0.24},
            {"name": "mid-peak", "start_hour": 6, "end_hour": 16, "price_per_kwh": 0.36},
            {"name": "peak", "start_hour": 16, "end_hour": 21, "price_per_kwh": 0.58},
            {"name": "off-peak", "start_hour": 21, "end_hour": 24, "price_per_kwh": 0.24},
        ],
    },
    "coned": {
        "utility_id": "coned",
        "utility_name": "Consolidated Edison",
        "state": "New York",
        "timezone": "America/New_York",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 7, "price_per_kwh": 0.19},
            {"name": "peak", "start_hour": 7, "end_hour": 22, "price_per_kwh": 0.38},
            {"name": "off-peak", "start_hour": 22, "end_hour": 24, "price_per_kwh": 0.19},
        ],
    },
    "dominion": {
        "utility_id": "dominion",
        "utility_name": "Dominion Energy",
        "state": "Virginia",
        "timezone": "America/New_York",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 6, "price_per_kwh": 0.18},
            {"name": "on-peak", "start_hour": 6, "end_hour": 22, "price_per_kwh": 0.32},
            {"name": "off-peak", "start_hour": 22, "end_hour": 24, "price_per_kwh": 0.18},
        ],
    },
    "duke": {
        "utility_id": "duke",
        "utility_name": "Duke Energy",
        "state": "North Carolina",
        "timezone": "America/New_York",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 7, "price_per_kwh": 0.17},
            {"name": "peak", "start_hour": 7, "end_hour": 11, "price_per_kwh": 0.31},
            {"name": "off-peak", "start_hour": 11, "end_hour": 17, "price_per_kwh": 0.22},
            {"name": "peak", "start_hour": 17, "end_hour": 21, "price_per_kwh": 0.36},
            {"name": "off-peak", "start_hour": 21, "end_hour": 24, "price_per_kwh": 0.17},
        ],
    },
    "austin": {
        "utility_id": "austin",
        "utility_name": "Austin Energy",
        "state": "Texas",
        "timezone": "America/Chicago",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 8, "price_per_kwh": 0.12},
            {"name": "on-peak", "start_hour": 8, "end_hour": 20, "price_per_kwh": 0.28},
            {"name": "off-peak", "start_hour": 20, "end_hour": 24, "price_per_kwh": 0.12},
        ],
    },
    "smud": {
        "utility_id": "smud",
        "utility_name": "Sacramento Municipal Utility District",
        "state": "California",
        "timezone": "America/Los_Angeles",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 7, "price_per_kwh": 0.19},
            {"name": "peak", "start_hour": 7, "end_hour": 19, "price_per_kwh": 0.42},
            {"name": "off-peak", "start_hour": 19, "end_hour": 24, "price_per_kwh": 0.19},
        ],
    },
    "aps": {
        "utility_id": "aps",
        "utility_name": "Arizona Public Service",
        "state": "Arizona",
        "timezone": "America/Phoenix",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 6, "price_per_kwh": 0.16},
            {"name": "mid-peak", "start_hour": 6, "end_hour": 18, "price_per_kwh": 0.29},
            {"name": "peak", "start_hour": 18, "end_hour": 22, "price_per_kwh": 0.44},
            {"name": "off-peak", "start_hour": 22, "end_hour": 24, "price_per_kwh": 0.16},
        ],
    },
    "xcel": {
        "utility_id": "xcel",
        "utility_name": "Xcel Energy",
        "state": "Colorado",
        "timezone": "America/Denver",
        "periods": [
            {"name": "off-peak", "start_hour": 0, "end_hour": 7, "price_per_kwh": 0.15},
            {"name": "on-peak", "start_hour": 7, "end_hour": 21, "price_per_kwh": 0.35},
            {"name": "off-peak", "start_hour": 21, "end_hour": 24, "price_per_kwh": 0.15},
        ],
    },
}


def get_all_tariffs():
    return TARIFFS


def get_tariff(utility_id: str):
    return TARIFFS.get(utility_id.lower())


def search_tariffs(query: str):
    q = query.lower()
    results = []
    for uid, tariff in TARIFFS.items():
        if q in tariff["utility_name"].lower():
            results.append({
                "utility_id": uid,
                "utility_name": tariff["utility_name"],
                "state": tariff["state"],
            })
    return results
