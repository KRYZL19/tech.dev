"""
FAA Aircraft Registry — Bundled dataset of 100 aircraft
Models: Cessna 172, 182, 206 | Piper PA-28 | Beechcraft Bonanza |
        Diamond DA40 | Cirrus SR20, SR22 | Robinson R44
"""
import random
from datetime import date, timedelta
from typing import Any


def _d(year: int, month: int, day: int) -> date:
    return date(year, month, day)


# Owner pools per aircraft type
OWNERS = {
    "Cessna 172": [
        ("ACEFLYER LLC", "Phoenix", "AZ"),
        ("SKYBOUND AVIATION INC", "Denver", "CO"),
        ("DAVIS JOHN R", "Tucson", "AZ"),
        ("HARRISON FLYING CLUB", "Austin", "TX"),
        ("BENNETT WILSON", "Albuquerque", "NM"),
        ("MOUNTAIN VIEW AVIATION LLC", "Salt Lake City", "UT"),
        ("RIVERS EDWARD", "Las Vegas", "NV"),
        ("CHEN PATRICK", "Los Angeles", "CA"),
        ("STOUT DANIEL", "San Diego", "CA"),
        ("HAWKINS MICHELLE", "Seattle", "WA"),
    ],
    "Cessna 182": [
        ("TRIDENT AVIATION LLC", "Houston", "TX"),
        ("PRECISION FLIGHT INC", "Dallas", "TX"),
        ("GOMEZ ROBERTO", "San Antonio", "TX"),
        ("YANKEE ENTERPRISES", "Oklahoma City", "OK"),
        ("BRIGHT SKIES LLC", "Memphis", "TN"),
        ("AERO HOLDINGS GROUP", "Atlanta", "GA"),
        ("FERNANDEZ CARLOS", "Miami", "FL"),
        ("THORNTON SAM", "Nashville", "TN"),
        ("BLAKE THOMAS", "Charlotte", "NC"),
        ("HANSEN KURT", "Minneapolis", "MN"),
    ],
    "Cessna 206": [
        ("LONE STAR AIR INC", "Fort Worth", "TX"),
        ("GULF COAST AVIATION LLC", "New Orleans", "LA"),
        ("SANDERS MICHAEL", "Birmingham", "AL"),
        ("KANSAS SKYWAYS", "Wichita", "KS"),
        ("HIGH ALTITUDE FLIGHTS", "Denver", "CO"),
        ("DELTA SHIPPING CO", "Jackson", "MS"),
        ("COLLINS FRANK", "Little Rock", "AR"),
        ("WILSON ENTERPRISES", "Shreveport", "LA"),
        ("PROPILOT INC", "Tulsa", "OK"),
        ("APEX AVIATION GROUP", "Kansas City", "MO"),
    ],
    "Piper PA-28": [
        ("CHEROKEE WINGS LLC", "Orlando", "FL"),
        ("SUNSHINE AVIATION INC", "Tampa", "FL"),
        ("PALM BEACH FLYERS", "West Palm Beach", "FL"),
        ("HENDERSON JAMES", "Jacksonville", "FL"),
        ("PINEHURST AVIATION", "Raleigh", "NC"),
        ("DIXIE FLIGHT LLC", "Columbia", "SC"),
        ("CAROLINA SKY INC", "Greensboro", "NC"),
        ("ATLANTIC AERO CLUB", "Norfolk", "VA"),
        ("PATRIOT FLIGHT GROUP", "Richmond", "VA"),
        ("HERITAGE AVIATION", "Charleston", "WV"),
    ],
    "Beechcraft Bonanza": [
        ("BONANZA HOLDINGS LLC", "Boise", "ID"),
        ("SILVER CREEK AVIATION", "Spokane", "WA"),
        ("MCCALL ROBERT", "Portland", "OR"),
        ("CEDAR Rapids FLYERS", "Cedar Rapids", "IA"),
        ("LAKEFRONT AIR LLC", "Madison", "WI"),
        ("HARTFORD AVIATION INC", "Hartford", "CT"),
        ("LIBERTY SKY PARK", "Boston", "MA"),
        ("EMERALD COAST AVIATION", "Pensacola", "FL"),
        ("MOUNTAIN AIRE LLC", "Flagstaff", "AZ"),
        ("GOLDEN EAGLE INC", "Sacramento", "CA"),
    ],
    "Diamond DA40": [
        ("DIAMOND SOUTH LLC", "Scottsdale", "AZ"),
        ("AVIAN HOLDINGS", "Fort Lauderdale", "FL"),
        ("TUCSON FLIGHT CENTER", "Tucson", "AZ"),
        ("HORIZON PILOT ACADEMY", "San Jose", "CA"),
        ("AURORA AVIATION INC", "Portland", "OR"),
        ("SUMMIT FLIGHT LLC", "Colorado Springs", "CO"),
        ("LIBERTY AVIATION GROUP", "Manchester", "NH"),
        ("ALPINE AVIATION INC", "Reno", "NV"),
        ("RED ROCK FLYERS", "St. George", "UT"),
        ("SIERRA SKY AIR", "Fresno", "CA"),
    ],
    "Cirrus SR20": [
        ("CIRRUS CHASE LLC", "Minneapolis", "MN"),
        ("PERIMETER AVIATION", "Duluth", "MN"),
        ("BREEZY POINT FLYERS", "Brainerd", "MN"),
        ("LONDON AVIATION INC", "London", "KY"),
        ("WILDLAND AIR LLC", "Cody", "WY"),
        ("GATEWAY FLIGHT INC", "St. Louis", "MO"),
        ("PARK REGION AVIATION", "Detroit Lakes", "MN"),
        ("IRON RANGE SKY", "Hibbing", "MN"),
        ("COASTAL CAPERS LLC", "Gulfport", "MS"),
        ("NEBRASKA FLIGHT GROUP", "Lincoln", "NE"),
    ],
    "Cirrus SR22": [
        ("PREMIUM AVIATION LLC", "Scottsdale", "AZ"),
        ("VISION AVIATION INC", "Boulder", "CO"),
        ("HIGHER GROUND AIR", "Aspen", "CO"),
        ("ELITE FLIGHT GROUP", "Westlake", "TX"),
        ("NEXUS AVIATION LLC", "Dallas", "TX"),
        ("PLATINUM SKIES INC", "Houston", "TX"),
        ("CAPITAL AVIATION GROUP", "Austin", "TX"),
        ("ALAMO FLIGHT LLC", "San Antonio", "TX"),
        ("LAKE TRAVIS FLYERS", "Lakeway", "TX"),
        ("VERMONT AVIATION INC", "Burlington", "VT"),
    ],
    "Robinson R44": [
        ("HELI-TOUR LLC", "Las Vegas", "NV"),
        ("SKYLINE HELICOPTERS INC", "Phoenix", "AZ"),
        ("COASTAL HELI SERVICE", "San Diego", "CA"),
        ("SIERRA HELICOPTER AIR", "Reno", "NV"),
        ("MOJAVE ROTORCRAFT", "Bakersfield", "CA"),
        ("SUNSET HELI TOURS INC", "Santa Monica", "CA"),
        ("DESERT WIND AVIATION", "Palm Springs", "CA"),
        ("GOLDEN GATE HELI", "San Francisco", "CA"),
        ("PACIFIC COAST HELICOPTERS", "Monterey", "CA"),
        ("TRAVERSE HELI LLC", "Traverse City", "MI"),
    ],
}

AIRCRAFT_DATA: list[dict[str, Any]] = []

N_BASE = 1000
MAKE_COUNTS = {
    "Cessna 172": 20,
    "Cessna 182": 15,
    "Cessna 206": 10,
    "Piper PA-28": 15,
    "Beechcraft Bonanza": 10,
    "Diamond DA40": 5,
    "Cirrus SR20": 5,
    "Cirrus SR22": 15,
    "Robinson R44": 5,
}

SPECS = {
    "Cessna 172":     {"empty": 1660, "gross": 2550, "hp": 160, "seats": 4, "engines": 1, "type": "Piston"},
    "Cessna 182":     {"empty": 1950, "gross": 3110, "hp": 230, "seats": 6, "engines": 1, "type": "Piston"},
    "Cessna 206":     {"empty": 2320, "gross": 3600, "hp": 300, "seats": 6, "engines": 1, "type": "Piston"},
    "Piper PA-28":    {"empty": 1415, "gross": 2550, "hp": 160, "seats": 4, "engines": 1, "type": "Piston"},
    "Beechcraft Bonanza": {"empty": 1930, "gross": 3400, "hp": 285, "seats": 6, "engines": 1, "type": "Piston"},
    "Diamond DA40":   {"empty": 1760, "gross": 2850, "hp": 180, "seats": 4, "engines": 1, "type": "Piston"},
    "Cirrus SR20":    {"empty": 2050, "gross": 3060, "hp": 200, "seats": 4, "engines": 1, "type": "Piston"},
    "Cirrus SR22":    {"empty": 2130, "gross": 3600, "hp": 310, "seats": 5, "engines": 1, "type": "Piston"},
    "Robinson R44":   {"empty": 1450, "gross": 2500, "hp": 260, "seats": 4, "engines": 1, "type": "Piston"},
}

YEAR_RANGE = (2000, 2025)

for make, count in MAKE_COUNTS.items():
    owners_pool = OWNERS[make]
    for i in range(count):
        n_num = N_BASE + len(AIRCRAFT_DATA) + 1
        n_number = f"N{n_num:04d}"
        serial = f"{make.split()[0][:2].upper()}{random.randint(1000,9999)}"
        year = random.randint(*YEAR_RANGE)
        spec = SPECS[make]
        days_ago = random.randint(0, 365 * 20)
        issued = date.today() - timedelta(days=days_ago + random.randint(30, 365))
        expires = issued + timedelta(days=365 * 7)
        days_to_expire = (expires - date.today()).days
        cert_type = "Standard" if random.random() > 0.05 else "Special"
        airworthy = "Airworthy" if random.random() > 0.03 else "Not Airworthy"
        owner_idx = i % len(owners_pool)
        owner = owners_pool[owner_idx]

        # Build owner history
        num_prev = random.randint(0, 3)
        history = []
        prev_issued = issued - timedelta(days=365 * random.randint(3, 7))
        for h in range(num_prev):
            h_owner = owners_pool[(owner_idx + h + 1) % len(owners_pool)]
            history.append({
                "owner_name": h_owner[0],
                "owner_city": h_owner[1],
                "owner_state": h_owner[2],
                "registration_issued": (prev_issued - timedelta(days=h * 365 * random.randint(2, 5))).isoformat(),
                "registration_expires": None,
                "cancellation_date": (issued - timedelta(days=h * 365 + random.randint(1, 90))).isoformat(),
            })

        aircraft = {
            "n_number": n_number,
            "serial_number": serial,
            "year": year,
            "make": make.split()[0],
            "model": make,
            "engine_make": make.split()[0],
            "engine_model": f"{spec['hp']}HP",
            "engine_hp": spec["hp"],
            "number_of_seats": spec["seats"],
            "number_of_engines": spec["engines"],
            "empty_weight": spec["empty"],
            "gross_weight": spec["gross"],
            "certificate": cert_type,
            "status": airworthy,
            "type_engine": spec["type"],
            "category": "Normal",
            "owner_name": owner[0],
            "owner_city": owner[1],
            "owner_state": owner[2],
            "registration_issued": issued.isoformat(),
            "registration_expires": expires.isoformat(),
            "days_to_expire": days_to_expire,
            "cancellation_date": None,
            "owner_history": history,
        }
        AIRCRAFT_DATA.append(aircraft)


def get_aircraft_by_n_number(n_number: str) -> dict | None:
    for ac in AIRCRAFT_DATA:
        if ac["n_number"].upper() == n_number.upper():
            return ac
    return None


def get_aircraft_by_manufacturer(mfr: str) -> list[dict]:
    mfr_upper = mfr.upper()
    return [ac for ac in AIRCRAFT_DATA if ac["make"].upper() == mfr_upper]


def get_expiring(days: int) -> list[dict]:
    cutoff = date.today() + timedelta(days=days)
    return [
        ac for ac in AIRCRAFT_DATA
        if ac.get("registration_expires") and date.fromisoformat(ac["registration_expires"]) <= cutoff
    ]
