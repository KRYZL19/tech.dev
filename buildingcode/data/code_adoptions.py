# Code adoption data for 20 major US cities
# Covers IBC 2021, IRC 2021, NFPA 70 (NEC) 2023

CODE_ADOPTIONS = {
    "CA": {
        "Los Angeles": {
            "ibc_version": "IBC 2022",
            "irc_version": "IRC 2022",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["LA City Building Code amendments", "Fire department review required"],
            "local_amendments": ["Chapter 9 fire protection", "Wind load provisions for SoCal"],
        },
        "San Francisco": {
            "ibc_version": "IBC 2022",
            "irc_version": "IRC 2022",
            "nec_version": "NEC 2023",
            "effective_date": "2023-07-01",
            "amendments": ["SF Building Code", "Earthquake safety provisions"],
            "local_amendments": ["Soft story retrofit requirements", "Seismic design standards"],
        },
        "San Diego": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["California Building Code"],
            "local_amendments": ["Wildfire hazard provisions"],
        },
    },
    "TX": {
        "Houston": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-09-01",
            "amendments": ["City of Houston amendments"],
            "local_amendments": ["Hurricane wind provisions", "Flood plain requirements"],
        },
        "Dallas": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2022-09-01",
            "amendments": ["Dallas Building Code 2021"],
            "local_amendments": ["Energy code amendments"],
        },
        "Austin": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-03-01",
            "amendments": ["Austin Building Code"],
            "local_amendments": ["Green building requirements", "Solar ready provisions"],
        },
        "San Antonio": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2022-06-01",
            "amendments": ["San Antonio Building Code"],
            "local_amendments": ["Historical preservation review"],
        },
    },
    "FL": {
        "Miami": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2022-12-01",
            "amendments": ["Florida Building Code 7th edition"],
            "local_amendments": ["High-velocity hurricane zone provisions", "Burglar-resistant openings"],
        },
        "Jacksonville": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["Florida Building Code"],
            "local_amendments": ["Coastal construction requirements"],
        },
        "Tampa": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["Florida Building Code"],
            "local_amendments": ["Flood elevation requirements"],
        },
    },
    "NY": {
        "New York City": {
            "ibc_version": "NYC Building Code 2022",
            "irc_version": "NYC Building Code 2022",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["NYC Building Code", "NYC Fire Code"],
            "local_amendments": ["NYC Energy Conservation Code", "LL87 energy transparency"],
        },
        "Buffalo": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["New York State Building Code"],
            "local_amendments": ["Snow load provisions"],
        },
    },
    "IL": {
        "Chicago": {
            "ibc_version": "Chicago Building Code 2022",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2022-08-01",
            "amendments": ["Chicago Building Code", "Chicago Fire Prevention Code"],
            "local_amendments": ["Chicago Energy Code", "Lake Michigan wind exposure"],
        },
    },
    "WA": {
        "Seattle": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-08-01",
            "amendments": ["Seattle Building Code", "Washington State Energy Code"],
            "local_amendments": ["Seismic upgrade requirements", "Raincreen provisions"],
        },
        "Spokane": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-07-01",
            "amendments": ["Washington State Building Code"],
            "local_amendments": ["Snow load provisions"],
        },
    },
    "CO": {
        "Denver": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-07-01",
            "amendments": ["Denver Building Code", "Colorado State Electrical Code"],
            "local_amendments": ["High altitude adjustments", "Snow load requirements"],
        },
    },
    "GA": {
        "Atlanta": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["Georgia State Minimum Building Code"],
            "local_amendments": ["Georgia energy code"],
        },
    },
    "AZ": {
        "Phoenix": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["Arizona Building Code"],
            "local_amendments": ["Desert heat provisions", "Solar access requirements"],
        },
    },
    "NV": {
        "Las Vegas": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-01-01",
            "amendments": ["Southern Nevada Building Code"],
            "local_amendments": ["Pool barrier requirements", "Desert exposure provisions"],
        },
    },
    "MA": {
        "Boston": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-07-01",
            "amendments": ["Massachusetts Building Code 9th edition"],
            "local_amendments": ["Snow load provisions", "Historic preservation"],
        },
    },
    "OR": {
        "Portland": {
            "ibc_version": "IBC 2021",
            "irc_version": "IRC 2021",
            "nec_version": "NEC 2023",
            "effective_date": "2023-10-01",
            "amendments": ["Oregon Building Code"],
            "local_amendments": ["Seismic retrofit provisions", "Tree protection"],
        },
    },
}


# Code section references
CODE_SECTIONS = {
    "IBC": {
        "2021": {
            "1008.1": {
                "title": "Means of Egress Illumination",
                "text": "Means of egress lighting shall be illuminated. The means of egress illumination required in Section 1008.1.1 shall be continuous. Riser illumination shall be provided for stairways.",
                "standards": ["NFPA 70", "UL 924"],
            },
            "1009.1": {
                "title": "Accessible Means of Egress",
                "text": "Accessible means of egress shall comply with Section 1009. Accessible means of egress shall be continuous from the accessible route to an accessible space.",
                "standards": ["ADA Standards for Accessible Design"],
            },
            "1107.1": {
                "title": "Design",
                "text": "Dwelling units or sleeping units shall be designed and constructed in accordance with Chapter 11.",
                "standards": ["ADA/ABA/AG"],
            },
            "1207.1": {
                "title": "Sound Transmission",
                "text": "Wall and floor-ceiling assemblies shall provide sound transmission control in accordance with Section 1207.",
                "standards": ["ASTM E90", "ASTM E413"],
            },
            "1603.1": {
                "title": "General",
                "text": "Construction documents shall show the size, section and relative locations of structural members with design loads and other applicable data.",
                "standards": ["ASCE 7"],
            },
            "1805.1": {
                "title": "Foundation Walls",
                "text": "Foundation walls shall be designed and constructed in accordance with the provisions of this section.",
                "standards": ["ACI 318"],
            },
            "2902.1": {
                "title": "Minimum Number",
                "text": "The minimum number of plumbing fixtures shall be determined in accordance with Table 2902.1.",
                "standards": ["IPC"],
            },
            "3401.1": {
                "title": "General",
                "text": "An existing building or portion thereof that does not comply with the requirements of this code shall be altered or repaired to conform to the provisions of this chapter.",
                "standards": [],
            },
            "5501.1": {
                "title": "Scope",
                "text": "The provisions of this chapter shall apply to the construction, installation, alteration, repair and maintenance of electric cooktops.",
                "standards": ["NFPA 70"],
            },
            "910.1": {
                "title": "Smoke and Heat Vents",
                "text": "Smoke and heat vents shall be installed in accordance with this section and Table 910.1.1.",
                "standards": ["UL 793"],
            },
        },
        "2022": {
            "1008.1": {
                "title": "Means of Egress Illumination",
                "text": "Means of egress lighting shall be illuminated. The means of egress illumination required in Section 1008.1.1 shall be continuous.",
                "standards": ["NFPA 70", "UL 924"],
            },
            "1009.1": {
                "title": "Accessible Means of Egress",
                "text": "Accessible means of egress shall comply with Section 1009.",
                "standards": ["ADA Standards for Accessible Design"],
            },
        },
    },
    "IRC": {
        "2021": {
            "N1101.1": {
                "title": "Scope",
                "text": "This chapter regulates the energy-efficient design and construction of new buildings.",
                "standards": ["ASHRAE 90.1", "IECC"],
            },
            "R301.1": {
                "title": "Design",
                "text": "Buildings and structures shall be designed and constructed in accordance with the provisions of this code.",
                "standards": ["ASCE 7"],
            },
            "R302.1": {
                "title": "Interior Walls",
                "text": "Interior walls and ceilings shall be separated from attics and roof cavities by draftstopping.",
                "standards": [],
            },
            "R314.1": {
                "title": "Smoke Alarms",
                "text": "Smoke alarms shall be installed in each sleeping room, outside each sleeping area, and on each level.",
                "standards": ["UL 217"],
            },
            "R403.1": {
                "title": "Footings",
                "text": "Footings shall be designed and constructed in accordance with Section R403.",
                "standards": ["ACI 332"],
            },
            "R602.1": {
                "title": "Wood Frame Construction",
                "text": "Wood frame construction shall comply with this section and other applicable requirements.",
                "standards": ["AFPA", "AWC"],
            },
            "R904.1": {
                "title": "Roof Covering",
                "text": "Roof coverings shall comply with this section and the applicable provisions of Chapter 9.",
                "standards": ["UL", "ASTM D225"],
            },
        },
    },
    "NEC": {
        "2023": {
            "100.1": {
                "title": "Definitions",
                "text": "This section contains only those definitions essential to the proper application of this Code.",
                "standards": ["NFPA"],
            },
            "210.1": {
                "title": "Scope",
                "text": "This article covers general requirements for conductors and equipment used for general use.",
                "standards": [],
            },
            "210.8": {
                "title": "Ground-Fault Circuit-Interrupter Protection for Personnel",
                "text": "GFCI protection shall be provided for 125-volt, single-phase, 15- and 20-ampere receptacles in dwelling units.",
                "standards": [],
            },
            "210.12": {
                "title": "Arc-Fault Circuit-Interrupter Protection",
                "text": "AFCI protection shall be provided for dwelling unit branch circuits supplying outlets.",
                "standards": ["UL 489"],
            },
            "230.1": {
                "title": "Scope",
                "text": "This article covers service conductors and equipment for control and protection of services.",
                "standards": [],
            },
            "250.1": {
                "title": "Scope",
                "text": "This article covers grounding and bonding of electrical systems and equipment.",
                "standards": [],
            },
            "314.1": {
                "title": "Scope",
                "text": "This article covers the installation and use of boxes and conduit bodies.",
                "standards": ["UL 514A"],
            },
            "422.1": {
                "title": "Scope",
                "text": "This article covers electrical appliances and their electrical connections.",
                "standards": [],
            },
            "680.1": {
                "title": "Scope",
                "text": "This article covers pools, spas, fountains, and hydromassage bathtubs.",
                "standards": ["UL 1563"],
            },
        },
    },
}


# State-level code adoption summaries
STATE_CODES = {
    "AL": {"code": "IBC 2021, IRC 2021", "adopted": "2021-01-01"},
    "AK": {"code": "IBC 2021, IRC 2021", "adopted": "2022-07-01"},
    "AZ": {"code": "IBC 2021, IRC 2021", "adopted": "2023-01-01"},
    "AR": {"code": "IBC 2021, IRC 2021", "adopted": "2021-01-01"},
    "CA": {"code": "IBC 2022, IRC 2022, CBC 2022", "adopted": "2023-01-01"},
    "CO": {"code": "IBC 2021, IRC 2021", "adopted": "2023-07-01"},
    "CT": {"code": "IBC 2021, IRC 2021", "adopted": "2022-10-01"},
    "DE": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "FL": {"code": "IBC 2021, FBC 7th Ed", "adopted": "2023-01-01"},
    "GA": {"code": "IBC 2021, IRC 2021", "adopted": "2023-01-01"},
    "HI": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "ID": {"code": "IBC 2021, IRC 2021", "adopted": "2022-07-01"},
    "IL": {"code": "IBC 2021, IRC 2021", "adopted": "2022-06-01"},
    "IN": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "IA": {"code": "IBC 2021, IRC 2021", "adopted": "2023-01-01"},
    "KS": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "KY": {"code": "IBC 2021, IRC 2021", "adopted": "2021-07-01"},
    "LA": {"code": "IBC 2021, IRC 2021", "adopted": "2023-01-01"},
    "ME": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "MD": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "MA": {"code": "IBC 2021, IRC 2021", "adopted": "2023-07-01"},
    "MI": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "MN": {"code": "IBC 2021, IRC 2021", "adopted": "2022-08-01"},
    "MS": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "MO": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "MT": {"code": "IBC 2021, IRC 2021", "adopted": "2022-07-01"},
    "NE": {"code": "IBC 2021, IRC 2021", "adopted": "2022-09-01"},
    "NV": {"code": "IBC 2021, IRC 2021", "adopted": "2023-01-01"},
    "NH": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "NJ": {"code": "IBC 2021, IRC 2021", "adopted": "2022-09-01"},
    "NM": {"code": "IBC 2021, IRC 2021", "adopted": "2022-07-01"},
    "NY": {"code": "IBC 2021, IRC 2021", "adopted": "2023-01-01"},
    "NC": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "ND": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "OH": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "OK": {"code": "IBC 2021, IRC 2021", "adopted": "2021-11-01"},
    "OR": {"code": "IBC 2021, IRC 2021", "adopted": "2023-10-01"},
    "PA": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "RI": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "SC": {"code": "IBC 2021, IRC 2021", "adopted": "2021-07-01"},
    "SD": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "TN": {"code": "IBC 2021, IRC 2021", "adopted": "2021-07-01"},
    "TX": {"code": "IBC 2021, IRC 2021", "adopted": "2022-09-01"},
    "UT": {"code": "IBC 2021, IRC 2021", "adopted": "2022-07-01"},
    "VT": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "VA": {"code": "IBC 2021, IRC 2021", "adopted": "2022-07-01"},
    "WA": {"code": "IBC 2021, IRC 2021", "adopted": "2023-08-01"},
    "WV": {"code": "IBC 2021, IRC 2021", "adopted": "2021-01-01"},
    "WI": {"code": "IBC 2021, IRC 2021", "adopted": "2022-01-01"},
    "WY": {"code": "IBC 2021, IRC 2021", "adopted": "2022-07-01"},
}


# ADA requirements by occupancy type
ADA_REQUIREMENTS = {
    "A-1": {
        "name": "Assembly, theaters",
        "accessible_rooms": "Required for 5% of patient rooms",
        "seating": "Wheelchair spaces required per Table 221.1.1",
        " toilet_rooms": "Minimum 2 accessible, one ambulatory",
        "drinking_fountains": "50% accessible, 50% standing height",
    },
    "A-2": {
        "name": "Assembly, restaurants",
        "accessible_rooms": "Accessible route to all dining areas",
        "seating": "Wheelchair spaces in each seating area",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "A-3": {
        "name": "Assembly, worship",
        "accessible_rooms": "Accessible spaces per occupancy load",
        "seating": "Wheelchair spaces per Table 221.1.1",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "B": {
        "name": "Business",
        "accessible_rooms": "5% of meeting rooms, min 1",
        "seating": "Accessible work surfaces",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "E": {
        "name": "Educational",
        "accessible_rooms": "5% of each educational facility",
        "seating": "Accessible desks",
        " toilet_rooms": "Accessible per floor",
        "drinking_fountains": "50% accessible",
    },
    "F-1": {
        "name": "Factory, moderate hazard",
        "accessible_rooms": "Accessible employee areas",
        "seating": "As needed for employee use",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "F-2": {
        "name": "Factory, low hazard",
        "accessible_rooms": "Accessible employee areas",
        "seating": "As needed",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "H-1": {
        "name": "High hazard",
        "accessible_rooms": "Accessible control areas",
        "seating": "Accessible viewing areas",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "I-2": {
        "name": "Healthcare",
        "accessible_rooms": "50% of patient rooms, all rooms on accessible floor",
        "seating": "Wheelchair spaces in waiting areas",
        " toilet_rooms": "One accessible per patient room, common areas per ratio",
        "drinking_fountains": "50% accessible",
    },
    "I-4": {
        "name": "Day care",
        "accessible_rooms": "All rooms accessible",
        "seating": "Accessible play areas",
        " toilet_rooms": "Accessible per Section 221.2",
        "drinking_fountains": "50% accessible",
    },
    "M": {
        "name": "Mercantile",
        "accessible_rooms": "5% of fitting rooms",
        "seating": "Wheelchair spaces in transient lodging",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "R-1": {
        "name": "Residential, transient",
        "accessible_rooms": "5% of rooms, minimum 1",
        "seating": "Accessible common areas",
        " toilet_rooms": "Accessible in each accessible room",
        "drinking_fountains": "50% accessible",
    },
    "R-2": {
        "name": "Residential, apartment",
        "accessible_rooms": "5% of dwelling units, all on accessible floor",
        "seating": "Accessible common areas",
        " toilet_rooms": "Accessible in each accessible unit",
        "drinking_fountains": "50% accessible in common areas",
    },
    "R-4": {
        "name": "Residential, assisted living",
        "accessible_rooms": "All rooms accessible",
        "seating": "Accessible common areas",
        " toilet_rooms": "Accessible per Section 221.2",
        "drinking_fountains": "50% accessible",
    },
    "S-1": {
        "name": "Storage, moderate hazard",
        "accessible_rooms": "Accessible employee areas",
        "seating": "As needed",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "S-2": {
        "name": "Storage, low hazard",
        "accessible_rooms": "Accessible employee areas",
        "seating": "As needed",
        " toilet_rooms": "Minimum 2 accessible",
        "drinking_fountains": "50% accessible",
    },
    "U": {
        "name": "Utility/Miscellaneous",
        "accessible_rooms": "Not typically required",
        "seating": "Not typically required",
        " toilet_rooms": "As required by code official",
        "drinking_fountains": "Per site conditions",
    },
}


# Permit checklists by project type
def get_permit_checklist(city: str, project_type: str, sqft: float):
    base = {
        "commercial": {
            "required_permits": [
                "Building Permit",
                "Electrical Permit",
                "Plumbing Permit",
                "Mechanical/HVAC Permit",
                "Fire Protection Permit",
                "Elevator Permit (if applicable)",
                "Sign Permit (if applicable)",
            ],
            "inspections": [
                "Foundation/Underground",
                "Rough Framing",
                "Rough Electrical",
                "Rough Plumbing",
                "Rough Mechanical",
                "Insulation",
                "Final Building",
                "Final Electrical",
                "Final Plumbing",
                "Final Mechanical",
                "Fire Protection Final",
                "Certificate of Occupancy",
            ],
            "setbacks": {
                "front": "Typically 15-20 ft",
                "rear": "Typically 10-25 ft",
                "side": "Typically 5-10 ft",
            },
        },
        "residential": {
            "required_permits": [
                "Building Permit",
                "Electrical Permit",
                "Plumbing Permit",
                "Mechanical/HVAC Permit",
            ],
            "inspections": [
                "Foundation",
                "Rough Framing",
                "Rough Electrical",
                "Rough Plumbing",
                "Rough Mechanical",
                "Insulation",
                "Final Building",
                "Final Electrical",
                "Final Plumbing",
                "Final Mechanical",
                "Final Plumbing Gas",
            ],
            "setbacks": {
                "front": "20 ft (IRC default)",
                "rear": "20 ft (IRC default)",
                "side": "5 ft (IRC default)",
            },
        },
        "addition": {
            "required_permits": [
                "Building Permit",
                "Electrical Permit",
                "Plumbing Permit",
                "Mechanical/HVAC Permit",
            ],
            "inspections": [
                "Foundation",
                "Rough Framing",
                "Rough Electrical",
                "Rough Plumbing",
                "Rough Mechanical",
                "Insulation",
                "Final Building",
                "Final Electrical",
                "Final Plumbing",
                "Final Mechanical",
            ],
            "setbacks": {
                "front": "Per local zoning",
                "rear": "Per local zoning",
                "side": "Per local zoning",
            },
        },
        "alteration": {
            "required_permits": [
                "Building Permit (Alteration)",
            ],
            "inspections": [
                "Rough Work (if structural)",
                "Insulation (if exposed)",
                "Final Building",
                "Final Electrical (if rewiring)",
                "Final Plumbing (if repiping)",
            ],
            "setbacks": {
                "front": "N/A - interior work",
                "rear": "N/A - interior work",
                "side": "N/A - interior work",
            },
        },
    }

    checklists = base.get(project_type, base["alteration"])

    # Adjust based on size
    if sqft > 5000 and project_type in ("commercial", "addition"):
        checklists["required_permits"].append("Structural Engineering Review")

    return checklists
