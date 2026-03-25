"""Vessel index — 80 bundled US boat/ship records."""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Owner:
    name: str
    city: str
    state: str
    purchase_date: date
    purchase_price: Optional[float] = None


@dataclass
class Vessel:
    vessel_id: str
    documentation_number: str
    name: str
    manufacturer: str
    model: str
    year: int
    length_ft: float
    beam_ft: float
    hull_material: str
    propulsion: str
    vessel_type: str
    status: str  # active / cancelled
    owners: list[Owner] = field(default_factory=list)
    lien_status: str = "clear"  # clear / lien / multiple_liens
    lien_holder: Optional[str] = None

    def current_owner(self) -> Optional[Owner]:
        return self.owners[-1] if self.owners else None


# ─── MANUFACTURERS & MODELS ───────────────────────────────────────────────────

MANUFACTURERS = {
    "sea_ray": {
        "name": "Sea Ray",
        "models": ["Sundancer", "Sport Yacht", "SLX", "Sedan Bridge", "Lunar", "Amberjack"],
    },
    "boston_whaler": {
        "name": "Boston Whaler",
        "models": ["Montauk", "Outrage", "Realm", "Vantage", "Super Sport", "Conquest"],
    },
    "grady_white": {
        "name": "Grady-White",
        "models": ["Express", "Fisherman", "Bimini", "Marlin", "Canyon", "Freedom"],
    },
    "yamaha": {
        "name": "Yamaha",
        "models": ["FX Cruiser", "VX", "SuperJet", "AR", "SX", "WaveRunner"],
    },
    "mastercraft": {
        "name": "MasterCraft",
        "models": ["X-Star", "NXT", "XT", "Pro Star", "Marietta", "Californian"],
    },
    "malibu": {
        "name": "Malibu",
        "models": ["M220", "M200", "Wakesetter", "Axisa", "Response", "Lokey"],
    },
    "cobalt": {
        "name": "Cobalt",
        "models": ["R-series", "A-series", "Bowers", "V-neil", "CS", "SS"],
    },
    "pontoon": {
        "name": "Pontoon",
        "models": ["Trifecta", "Avalanche", "Barrett", "Sundancer", "Elite", "Legacy"],
    },
}

HULL_MATERIALS = ["fiberglass", "aluminum", "composite", "steel", "wood"]
PROPULSION_TYPES = ["outboard", "inboard", "sterndrive", "jet", "sail"]
VESSEL_TYPES = ["motor yacht", "cruiser", "fishing", "pontoon", "jet boat", "center console", "walkaround"]


# ─── VESSEL RECORDS ───────────────────────────────────────────────────────────

VESSELS: list[Vessel] = []


def _add(
    vessel_id: str,
    doc_num: str,
    name: str,
    mfr: str,
    mod: str,
    yr: int,
    length: float,
    beam: float,
    hull: str,
    prop: str,
    vtype: str,
    status: str,
    owners: list[Owner],
    lien: str = "clear",
    lien_holder: Optional[str] = None,
) -> None:
    VESSELS.append(
        Vessel(
            vessel_id=vessel_id,
            documentation_number=doc_num,
            name=name,
            manufacturer=mfr,
            model=mod,
            year=yr,
            length_ft=length,
            beam_ft=beam,
            hull_material=hull,
            propulsion=prop,
            vessel_type=vtype,
            status=status,
            owners=owners,
            lien_status=lien,
            lien_holder=lien_holder,
        )
    )


# Sea Ray (10 vessels)
_add("SR001", "1234567", "Sea Esta", "sea_ray", "Sundancer", 2019, 31.5, 10.2, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("James R. Holt", "Miami", "FL", date(2019, 4, 12), 185000),
      Owner("Marina Holdings LLC", "Fort Lauderdale", "FL", date(2022, 8, 20), 165000)])
_add("SR002", "1234568", "Blue Horizon", "sea_ray", "SLX", 2021, 34.0, 10.8, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Tina Voss", "Sarasota", "FL", date(2021, 6, 1), 220000)])
_add("SR003", "1234569", "Dreamweaver", "sea_ray", "Sport Yacht", 2017, 40.0, 13.5, "fiberglass", "inboard", "motor yacht", "active",
     [Owner("Robert Chen", "Newport Beach", "CA", date(2017, 11, 15), 410000),
      Owner("Pacific Dream LLC", "Long Beach", "CA", date(2023, 3, 10), 380000)], lien="lien", lien_holder="US Bank")
_add("SR004", "1234570", "Aquanut", "sea_ray", "Sedan Bridge", 2015, 36.0, 12.0, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Carol Fisk", "Sandusky", "OH", date(2015, 5, 22), 275000)])
_add("SR005", "1234571", "Serenity Now", "sea_ray", "Sundancer", 2018, 28.0, 9.3, "fiberglass", "sterndrive", "cruiser", "cancelled",
     [Owner("Paul Danna", "Tampa", "FL", date(2018, 2, 14), 145000),
      Owner("Miguel Rojas", "Clearwater", "FL", date(2020, 9, 1), None)], lien="clear")
_add("SR006", "1234572", "Liquid Asset", "sea_ray", "Amberjack", 2014, 25.0, 8.8, "fiberglass", "outboard", "fishing", "active",
     [Owner("Sandra Kwan", "Gulfport", "MS", date(2014, 7, 4), 95000)])
_add("SR007", "1234573", "Island Time", "sea_ray", "Lunar", 2020, 32.0, 11.0, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Gary Immel", "Marco Island", "FL", date(2020, 1, 30), 195000)])
_add("SR008", "1234574", "Reel Money", "sea_ray", "Express", 2016, 27.5, 9.5, "fiberglass", "outboard", "fishing", "active",
     [Owner("Diana Morris", "Islamorada", "FL", date(2016, 10, 18), 115000),
      Owner("Larry Brandt", "Key West", "FL", date(2024, 2, 5), 125000)])
_add("SR009", "1234575", "OC Daze", "sea_ray", "SLX", 2022, 35.0, 10.8, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Kevin Tran", "Dana Point", "CA", date(2022, 4, 20), 245000)])
_add("SR010", "1234576", "Voyager", "sea_ray", "Sport Yacht", 2013, 42.0, 14.0, "fiberglass", "inboard", "motor yacht", "cancelled",
     [Owner("Elaine Brooks", "San Diego", "CA", date(2013, 8, 12), 520000)])

# Boston Whaler (10 vessels)
_add("BW001", "2234561", "Pura Vida", "boston_whaler", "Montauk", 2020, 19.0, 7.8, "fiberglass", "outboard", "center console", "active",
     [Owner("Juan Salazar", "Key Largo", "FL", date(2020, 3, 15), 48000)])
_add("BW002", "2234562", "Reel Estate", "boston_whaler", "Outrage", 2018, 29.0, 9.5, "fiberglass", "outboard", "fishing", "active",
     [Owner("Cathy Okafor", "Stuart", "FL", date(2018, 7, 8), 135000),
      Owner("David Hunt", "Jupiter", "FL", date(2023, 11, 1), 140000)], lien="lien", lien_holder="Bank of America")
_add("BW003", "2234563", "Whaler Boy", "boston_whaler", "Super Sport", 2016, 17.0, 6.8, "fiberglass", "outboard", "center console", "active",
     [Owner("Mike Doherty", "Martha's Vineyard", "MA", date(2016, 6, 1), 38000)])
_add("BW004", "2234564", "Rule This", "boston_whaler", "Vantage", 2021, 25.0, 8.9, "fiberglass", "outboard", "walkaround", "active",
     [Owner("Patricia Sun", "Charleston", "SC", date(2021, 5, 22), 88000)])
_add("BW005", "2234565", "Reel Quiet", "boston_whaler", "Realm", 2022, 32.0, 10.5, "fiberglass", "outboard", "fishing", "active",
     [Owner("Hank Vo", "Morehead City", "NC", date(2022, 9, 10), 195000)])
_add("BW006", "2234566", "Blue Fin", "boston_whaler", "Conquest", 2017, 28.0, 9.5, "fiberglass", "outboard", "walkaround", "active",
     [Owner("Nikki Franz", "Montauk", "NY", date(2017, 4, 30), 145000)])
_add("BW007", "2234567", "Hooked Up", "boston_whaler", "Outrage", 2019, 35.0, 10.8, "fiberglass", "outboard", "fishing", "active",
     [Owner("Ray Martinez", "Port Isabel", "TX", date(2019, 8, 14), 280000),
      Owner("Tres Oceans LLC", "Galveston", "TX", date(2024, 1, 15), 260000)], lien="multiple_liens", lien_holder="Wells Fargo / Marine Finance Co")
_add("BW008", "2234568", "Kidakool", "boston_whaler", "Montauk", 2015, 19.0, 7.8, "fiberglass", "outboard", "center console", "active",
     [Owner("Amy Liu", "Bar Harbor", "ME", date(2015, 7, 1), 42000)])
_add("BW009", "2234569", "Moby Duck", "boston_whaler", "Bimini", 2020, 21.0, 8.2, "fiberglass", "outboard", "fishing", "cancelled",
     [Owner("Ben Foster", "Vero Beach", "FL", date(2020, 2, 28), 65000)])
_add("BW010", "2234570", "Reel Therapy", "boston_whaler", "Express", 2023, 28.0, 9.5, "fiberglass", "outboard", "fishing", "active",
     [Owner("Nancy Chu", "Wrightsville Beach", "NC", date(2023, 6, 18), 185000)])

# Grady-White (10 vessels)
_add("GW001", "3234561", "Three Sheets", "grady_white", "Express", 2017, 28.0, 9.8, "fiberglass", "outboard", "fishing", "active",
     [Owner("Steve Pate", "Wanchese", "NC", date(2017, 5, 5), 148000)])
_add("GW002", "3234562", "Grady Lady", "grady_white", "Fisherman", 2019, 25.0, 8.9, "fiberglass", "outboard", "fishing", "active",
     [Owner("Barb Kowalski", "Oriental", "NC", date(2019, 3, 20), 115000)])
_add("GW003", "3234563", "Reel Dreams", "grady_white", "Canyon", 2021, 31.0, 10.5, "fiberglass", "outboard", "fishing", "active",
     [Owner("Fred Nguyen", "Destin", "FL", date(2021, 7, 4), 210000),
      Owner("Reel Dreams LLC", "Panama City", "FL", date(2024, 4, 1), 195000)])
_add("GW004", "3234564", "Sea Spirit", "grady_white", "Freedom", 2016, 30.0, 10.5, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Helen Marsh", "St. Augustine", "FL", date(2016, 10, 12), 185000)])
_add("GW005", "3234565", "No Worries", "grady_white", "Bimini", 2018, 27.0, 9.2, "fiberglass", "outboard", "fishing", "active",
     [Owner("Otto Braun", "Cedar Point", "NC", date(2018, 6, 30), 135000)])
_add("GW006", "3234566", "Marlin Spike", "grady_white", "Marlin", 2020, 33.0, 11.0, "fiberglass", "outboard", "fishing", "active",
     [Owner("Rosa Espinoza", "Stuart", "FL", date(2020, 9, 15), 245000),
      Owner("Blue Water Charters", "Fort Pierce", "FL", date(2023, 8, 1), 230000)], lien="lien", lien_holder="Citi Marine Lending")
_add("GW007", "3234567", "Slow Day", "grady_white", "Express", 2015, 28.0, 9.8, "fiberglass", "outboard", "fishing", "active",
     [Owner("Lee Whitmore", "Chincoteague", "VA", date(2015, 4, 11), 128000)])
_add("GW008", "3234568", "Reel Steel", "grady_white", "Canyon", 2022, 35.0, 11.5, "fiberglass", "outboard", "fishing", "active",
     [Owner("Karen Kim", "Gulf Shores", "AL", date(2022, 5, 22), 315000)])
_add("GW009", "3234569", "Blue Water", "grady_white", "Fisherman", 2014, 25.0, 8.9, "fiberglass", "outboard", "fishing", "cancelled",
     [Owner("Tom Ritchie", "Port Aransas", "TX", date(2014, 8, 20), 98000)])
_add("GW010", "3234570", "Fish Whisperer", "grady_white", "Freedom", 2023, 30.0, 10.5, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Yolanda Cruz", "Sanibel", "FL", date(2023, 2, 14), 225000)])

# Yamaha (10 vessels)
_add("YM001", "4234561", "Wave Runnerz", "yamaha", "FX Cruiser", 2021, 9.8, 4.2, "composite", "jet", "jet boat", "active",
     [Owner("Derek Sims", "Lake Havasu", "AZ", date(2021, 3, 1), 18500)])
_add("YM002", "4234562", "Blue Crush", "yamaha", "VX", 2019, 9.4, 4.0, "composite", "jet", "jet boat", "active",
     [Owner("Ashley Price", "Lake Powell", "UT", date(2019, 6, 15), 14200)])
_add("YM003", "4234563", "Thrill Seeker", "yamaha", "AR", 2020, 10.2, 4.5, "composite", "jet", "jet boat", "active",
     [Owner("Chris Novak", "Lake Tahoe", "CA", date(2020, 7, 20), 21000)])
_add("YM004", "4234564", "Aqua Toy", "yamaha", "SX", 2018, 9.0, 3.9, "composite", "jet", "jet boat", "active",
     [Owner("Megan Lee", "Parker", "AZ", date(2018, 5, 10), 12800)])
_add("YM005", "4234565", "High Five", "yamaha", "SuperJet", 2022, 7.8, 3.2, "composite", "jet", "jet boat", "active",
     [Owner("Josh Barra", "Orlando", "FL", date(2022, 1, 5), 9800)])
_add("YM006", "4234566", "Splashdown", "yamaha", "FX Cruiser", 2017, 9.8, 4.2, "composite", "jet", "jet boat", "active",
     [Owner("Lisa Wang", "Katy", "TX", date(2017, 8, 22), 16500)])
_add("YM007", "4234567", "Big Rip", "yamaha", "AR", 2023, 10.5, 4.6, "composite", "jet", "jet boat", "active",
     [Owner("Travis Hood", "Lake Cumberland", "KY", date(2023, 4, 14), 23500)])
_add("YM008", "4234568", "Jet Setter", "yamaha", "VX", 2016, 9.4, 4.0, "composite", "jet", "jet boat", "active",
     [Owner("Renee Clark", "Havasu City", "AZ", date(2016, 2, 28), 12000)])
_add("YM009", "4234569", "Tow Zone", "yamaha", "SX", 2020, 9.0, 3.9, "composite", "jet", "jet boat", "cancelled",
     [Owner("Brian Torres", "Las Vegas", "NV", date(2020, 11, 11), 15500)])
_add("YM010", "4234570", "Wake Rider", "yamaha", "FX Cruiser", 2022, 9.8, 4.2, "composite", "jet", "jet boat", "active",
     [Owner("Angela Park", "Nashville", "TN", date(2022, 6, 8), 19200)])

# MasterCraft (10 vessels)
_add("MC001", "5234561", "X-Cellent", "mastercraft", "X-Star", 2020, 24.0, 8.5, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Brandon Cole", "Lake Lanier", "GA", date(2020, 5, 1), 115000)])
_add("MC002", "5234562", "Nauti Buoy", "mastercraft", "NXT", 2019, 22.0, 8.0, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Jackie Ross", "Lewisville", "TX", date(2019, 6, 20), 82000)])
_add("MC003", "5234563", "Inwakes", "mastercraft", "XT", 2021, 23.0, 8.2, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Todd Harris", "Table Rock", "SC", date(2021, 7, 4), 95000),
      Owner("Lake Fun LLC", "Greenville", "SC", date(2024, 2, 28), 90000)])
_add("MC004", "5234564", "Pro Reign", "mastercraft", "Pro Star", 2018, 20.0, 7.5, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Dana Forbes", "Omaha", "NE", date(2018, 4, 15), 58000)])
_add("MC005", "5234565", "Wakedog", "mastercraft", "X-Star", 2022, 24.0, 8.5, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Scott Emmett", "Kissimmee", "FL", date(2022, 8, 12), 128000),
      Owner("Orlando Watersports", "Orlando", "FL", date(2025, 1, 10), 120000)], lien="lien", lien_holder="Truist Bank")
_add("MC006", "5234566", "Marietta Dream", "mastercraft", "Marietta", 2017, 26.0, 9.0, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Jennifer Wu", "Pittsburgh", "PA", date(2017, 9, 5), 78000)])
_add("MC007", "5234567", "Red Line", "mastercraft", "XT", 2016, 23.0, 8.2, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Greg Foust", "Lake Murray", "SC", date(2016, 5, 30), 62000)])
_add("MC008", "5234568", "Califin", "mastercraft", "Californian", 2019, 25.0, 8.8, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Monica Reyes", "Folsom", "CA", date(2019, 3, 18), 92000)])
_add("MC009", "5234569", "Big Eat", "mastercraft", "X-Star", 2015, 24.0, 8.5, "fiberglass", "inboard", "cruiser", "cancelled",
     [Owner("Phil Dunham", "Chandler", "AZ", date(2015, 7, 4), 98000)])
_add("MC010", "5234570", "Flipper", "mastercraft", "NXT", 2023, 22.0, 8.0, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Samantha Key", "Cumming", "GA", date(2023, 4, 22), 88000)])

# Malibu (10 vessels)
_add("ML001", "6234561", "Wake Nation", "malibu", "Wakesetter", 2020, 23.0, 8.8, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Brett Sorensen", "Minneapolis", "MN", date(2020, 5, 15), 105000)])
_add("ML002", "6234562", "Malibu Stacy", "malibu", "M220", 2021, 23.5, 8.9, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Courtney Day", "Lake Austin", "TX", date(2021, 6, 1), 118000)])
_add("ML003", "6234563", "Sun Chaser", "malibu", "M200", 2019, 21.0, 8.2, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Marcus Bell", "Springfield", "IL", date(2019, 8, 10), 75000)])
_add("ML004", "6234564", "Turn It Up", "malibu", "Wakesetter", 2022, 24.0, 9.0, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Lindsay Moore", "Grand Rapids", "MI", date(2022, 7, 4), 132000),
      Owner("Moore Family Trust", "Ada", "MI", date(2025, 3, 1), 128000)])
_add("ML005", "6234565", "Gunner", "malibu", "Axisa", 2018, 22.0, 8.5, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Ryan Kessler", "Lake Geneva", "WI", date(2018, 6, 22), 85000)])
_add("ML006", "6234566", "Response LR", "malibu", "Response", 2017, 25.0, 9.2, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Vanessa Cruz", "Tulsa", "OK", date(2017, 9, 30), 92000)])
_add("ML007", "6234567", "Lokey Star", "malibu", "Lokey", 2021, 24.0, 9.0, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Andre Peters", "Lake Wylie", "SC", date(2021, 4, 18), 112000)])
_add("ML008", "6234568", "Max Effort", "malibu", "Wakesetter", 2016, 23.0, 8.8, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Jenna Scott", "Indianapolis", "IN", date(2016, 7, 14), 78000)])
_add("ML009", "6234569", "Beach House", "malibu", "M220", 2023, 23.5, 8.9, "fiberglass", "inboard", "cruiser", "active",
     [Owner("Eric Sundberg", "Seattle", "WA", date(2023, 5, 27), 135000)])
_add("ML010", "6234570", "Wavemaker", "malibu", "M200", 2015, 21.0, 8.2, "fiberglass", "inboard", "cruiser", "cancelled",
     [Owner("Tyler Bates", "Columbus", "OH", date(2015, 4, 5), 68000)])

# Cobalt (10 vessels)
_add("CB001", "7234561", "Cobalt Star", "cobalt", "R-series", 2019, 24.0, 8.6, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Mike Jennings", "Lake Oconee", "GA", date(2019, 5, 12), 92000)])
_add("CB002", "7234562", "Blue Note", "cobalt", "A-series", 2020, 22.0, 8.3, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Rachel Hall", "Guntersville", "AL", date(2020, 6, 8), 78000)])
_add("CB003", "7234563", "Ellie J", "cobalt", "Bowers", 2021, 26.0, 9.2, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Jerry Bowers", "Lake Gaston", "NC", date(2021, 7, 20), 112000),
      Owner("Ellie J LLC", "Raleigh", "NC", date(2024, 6, 1), 105000)])
_add("CB004", "7234564", "V-Nell", "cobalt", "V-neil", 2018, 23.0, 8.5, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Kim Voss", "Chickamauga", "GA", date(2018, 8, 5), 85000)])
_add("CB005", "7234565", "Cruiser Z", "cobalt", "CS", 2017, 25.0, 9.0, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Tony Russo", "Lake Norman", "NC", date(2017, 10, 15), 88000)])
_add("CB006", "7234566", "Sunday Funday", "cobalt", "SS", 2022, 24.0, 8.6, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Nicole Brown", "Smith Mountain Lake", "VA", date(2022, 4, 30), 105000)])
_add("CB007", "7234567", "Cobalt Blue", "cobalt", "R-series", 2016, 24.0, 8.6, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Jason Polk", "Lake Charlevoix", "MI", date(2016, 7, 1), 78000)])
_add("CB008", "7234568", "Sea La Vie", "cobalt", "A-series", 2023, 22.0, 8.3, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Emily Dao", "Bullard", "TX", date(2023, 3, 25), 95000)])
_add("CB009", "7234569", "Island Run", "cobalt", "Bowers", 2015, 26.0, 9.2, "fiberglass", "sterndrive", "cruiser", "cancelled",
     [Owner("Hal Goodman", "Mountain Home", "AR", date(2015, 5, 10), 105000)])
_add("CB010", "7234570", "Last Run", "cobalt", "CS", 2021, 25.0, 9.0, "fiberglass", "sterndrive", "cruiser", "active",
     [Owner("Wendy Eng", "Lake Wateree", "SC", date(2021, 9, 12), 98000)])

# Pontoon (10 vessels)
_add("PT001", "8234561", "Party Barge", "pontoon", "Trifecta", 2019, 24.0, 8.5, "aluminum", "outboard", "pontoon", "active",
     [Owner("Dean Oliver", "Dale Hollow Lake", "KY", date(2019, 5, 1), 32000)])
_add("PT002", "8234562", "Dock Holiday", "pontoon", "Avalanche", 2020, 26.0, 8.8, "aluminum", "outboard", "pontoon", "active",
     [Owner("Kelly Morse", "Lake Cumberland", "KY", date(2020, 6, 15), 42000)])
_add("PT003", "8234563", "Pontoon Express", "pontoon", "Barrett", 2018, 22.0, 8.2, "aluminum", "outboard", "pontoon", "active",
     [Owner("Luis Miranda", "Lake Havasu", "AZ", date(2018, 4, 20), 28000)])
_add("PT004", "8234564", "Lakeside", "pontoon", "Sundancer", 2021, 28.0, 9.0, "aluminum", "outboard", "pontoon", "active",
     [Owner("Tammy Barnes", "Lake Lanier", "GA", date(2021, 7, 4), 55000),
      Owner("Barnes Family LLC", "Cumming", "GA", date(2024, 5, 1), 52000)])
_add("PT005", "8234565", "Knot Working", "pontoon", "Elite", 2017, 24.0, 8.5, "aluminum", "outboard", "pontoon", "active",
     [Owner("Jeff Sessions", "Norris Lake", "TN", date(2017, 8, 10), 31000)])
_add("PT006", "8234566", "Float On", "pontoon", "Legacy", 2022, 27.0, 8.8, "aluminum", "outboard", "pontoon", "active",
     [Owner("Carla Neal", "Lake Travis", "TX", date(2022, 5, 22), 58000)])
_add("PT007", "8234567", "Margaritaville", "pontoon", "Trifecta", 2016, 24.0, 8.5, "aluminum", "outboard", "pontoon", "active",
     [Owner("Gordon Lyons", "Dale Hollow", "KY", date(2016, 6, 30), 29500)])
_add("PT008", "8234568", "Reelaxation", "pontoon", "Avalanche", 2023, 26.0, 8.8, "aluminum", "outboard", "pontoon", "active",
     [Owner("Diana Fox", "Lake Murray", "SC", date(2023, 4, 10), 48000)])
_add("PT009", "8234569", "Lazy Dayz", "pontoon", "Barrett", 2015, 22.0, 8.2, "aluminum", "outboard", "pontoon", "cancelled",
     [Owner("Steve Markham", "Table Rock", "SC", date(2015, 7, 4), 25000)])
_add("PT010", "8234570", "Tiki Time", "pontoon", "Elite", 2020, 24.0, 8.5, "aluminum", "outboard", "pontoon", "active",
     [Owner("Ashley Chen", "Lake Oahe", "SD", date(2020, 9, 5), 35000)])


# ─── LOOKUP INDEXES ───────────────────────────────────────────────────────────

VESSEL_BY_ID: dict[str, Vessel] = {v.vessel_id: v for v in VESSELS}
DOC_NUM_TO_VESSEL: dict[str, Vessel] = {v.documentation_number: v for v in VESSELS}


def get_by_manufacturer(mfr: str) -> list[Vessel]:
    """Return all vessels for a manufacturer key."""
    return [v for v in VESSELS if v.manufacturer == mfr]


def get_all_manufacturers() -> dict[str, dict]:
    return MANUFACTURERS
