import random
from datetime import date, timedelta
from models.schemas import Patent, PatentClaims

IPC_CODES = {
    "H01L": "Semiconductor devices",
    "H01M": "Batteries",
    "G06N": "AI/ML computer systems",
    "A61K": "Pharmaceutical preparations",
    "B60L": "Electric vehicles",
    "H01G": "Capacitors/supercapacitors",
    "F24S": "Solar thermal collectors",
    "H02J": "Power systems",
    "C01B": "Battery materials",
    "G06F": "Data processing"
}

PATENT_TITLES = {
    "semiconductors": [
        "3D Stacked Semiconductor Device with Through-Silicon Vias",
        "FinFET Transistor with Gate-All-Around Architecture",
        "Non-Volatile Memory Array with Charge Trapping Layer",
        "GaN Power Device with Low On-Resistance",
        "Silicon Photonics Waveguide with Grating Coupler",
        "Radiation-Hardened SOI CMOS Inverter Circuit",
        "Monolithic 3D IC with Thermal Via Interconnect",
        "Wide Bandgap Semiconductor Substrate",
        "Quantum Dot Infrared Photodetector Array",
        "MEMS Accelerometer with SoC Integration",
    ],
    "battery": [
        "Lithium-Ion Battery Cell with Silicon-Carbon Anode",
        "Solid-State Electrolyte for High-Energy Battery",
        "Sodium-Ion Battery Cathode Material",
        "Battery Management System with Cell Balancing",
        "Li-Air Battery with Protected Lithium Anode",
        "High-Voltage Nickel-Rich Layered Cathode",
        "Graphite-Coated Current Collector for Battery",
        "Fast-Charging Battery Cell with Dendrite Suppression",
        "All-Solid-State Battery with Sulfide Electrolyte",
        "Lithium-Metal Battery with Artificial SEI Layer",
    ],
    "ai_ml": [
        "Neural Network Accelerator with Systolic Array",
        "Training Method for Sparse Transformer Models",
        "Hardware Accelerator for Graph Neural Networks",
        "In-Memory Computing Architecture for AI",
        "Quantization-Aware Training Pipeline",
        "Mixed-Precision Arithmetic Unit for Deep Learning",
        "Event-Driven Neural Network Processor",
        "On-Device Federated Learning System",
        "Approximate Computing Unit for Neural Networks",
        "Neuromorphic Chip with Spike-Timing Plasticity",
    ],
    "pharma": [
        "mRNA Vaccine with Modified Nucleotides",
        "Lipid Nanoparticle Delivery System",
        "Monoclonal Antibody with Enhanced Half-Life",
        "Small Molecule Inhibitor of KRAS G12C",
        "Bispecific Antibody for Cancer Immunotherapy",
        "RNAi Therapeutic with GalNAc Conjugation",
        "Protein Degrader Molecule with E3 Ligase Moiety",
        "Hydrogel Formulation for Drug Delivery",
        "Peptide Drug Stabilized with Helix Mimicry",
        "CAR-T Cell Engineering with Safety Switch",
    ],
    "ev": [
        "Electric Motor with Hairpin Winding Configuration",
        "Wide-Bandgap Inverter for EV Drive System",
        "Regenerative Braking System with Battery Integration",
        "EV Charging Station with Bi-Directional Power Flow",
        "Thermal Management System for Battery Pack",
        "Silicon Carbide Power Module for Traction Inverter",
        "Wireless Charging Pad with Foreign Object Detection",
        "High-Voltage Battery Pack with Integrated Cooling",
        "EV On-Board Charger with PFC Stage",
        "Electric Axle with Dual-Speed Transmission",
    ],
    "solar": [
        "Perovskite-Silicon Tandem Solar Cell",
        " Bifacial Solar Module with Enhanced Rear Irradiance",
        "Concentrator Photovoltaic Receiver with Micro-CPV",
        "Solar Inverter with Maximum Power Point Tracking",
        "Anti-Reflective Coating for Silicon Wafer",
        "Building-Integrated Photovoltaic Glazing Unit",
        "Solar Panel with Floating Thermal Management",
        "Thin-Film CIGS Solar Cell on Flexible Substrate",
        "Solar Tracker with Dormancy Mode for Extreme Weather",
        "Photovoltaic Tile with Integrated Waterproofing",
    ],
}

ALL_TITLES = (
    PATENT_TITLES["semiconductors"] + PATENT_TITLES["battery"] +
    PATENT_TITLES["ai_ml"] + PATENT_TITLES["pharma"] +
    PATENT_TITLES["ev"] + PATENT_TITLES["solar"]
)

FIRST_NAMES = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
               "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
               "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
               "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
               "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
               "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
               "Edward", "Deborah", "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Sharon"]

LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
              "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
              "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
              "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
              "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
              "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell"]

COMPANIES = {
    "semiconductors": ["Intel", "TSMC", "Samsung", "AMD", "NVIDIA", "Qualcomm", "Broadcom", "Texas Instruments"],
    "battery": ["Panasonic", "LG Energy", "CATL", "Samsung SDI", "BYD", "SK On", "QuantumScape", "SolidPower"],
    "ai_ml": ["Google", "Microsoft", "NVIDIA", "Intel", "AMD", "Apple", "Meta", "OpenAI"],
    "pharma": ["Pfizer", "Moderna", "Roche", "Novartis", "Johnson & Johnson", "Merck", "BMS", "Amgen"],
    "ev": ["Tesla", "Rivian", "Lucid", "Ford", "GM", "VW", "Hyundai", "Toyota"],
    "solar": ["First Solar", "SunPower", "Enphase", "SolarEdge", "Canadian Solar", "JinkoSolar", "LG", "REC"]
}

DOMAIN_TECH_CLAIMS = {
    "semiconductor": ["junction", "doping", "gate oxide", "threshold voltage", "channel length", "leakage current", "drain current", "transconductance"],
    "battery": ["cathode", "anode", "electrolyte", "separator", "lithium", "capacity", "cycling", "coulombic"],
    "ai": ["neural network", "inference", "training", "weight", "activation", "gradient", "backpropagation", "tensor"],
    "pharma": ["compound", "receptor", "agonist", "antagonist", "IC50", "bioavailability", "half-life", "efficacy"],
    "ev": ["torque", "power density", "efficiency", "inverter", "converter", "regenerative", "thermal", "charge"],
    "solar": ["photovoltaic", "bandgap", "conversion efficiency", "fill factor", "open circuit voltage", "short circuit", "irradiance", "tandem"]
}

YEAR_RANGE = (1976, 2025)

random.seed(42)


def generate_patent_number(idx: int) -> str:
    if idx < 300:
        prefix = "US"
        num = 4000000 + idx * 12347
    elif idx < 450:
        prefix = "US"
        num = 7000000 + idx * 9823
    else:
        prefix = "US"
        num = 10000000 + idx * 7349
    if idx % 15 == 0:
        return f"{prefix}{num}B2"
    elif idx % 7 == 0:
        return f"{prefix}{num}A1"
    else:
        return f"{prefix}{num}B1"


def generate_abstract(title: str, ipc_code: str) -> str:
    domain_key = None
    for key in DOMAIN_TECH_CLAIMS:
        if key in ipc_code.lower() or key in title.lower():
            domain_key = key
            break
    if not domain_key:
        domain_key = random.choice(list(DOMAIN_TECH_CLAIMS.keys()))

    tech_terms = random.sample(DOMAIN_TECH_CLAIMS[domain_key], 3)
    return (
        f"A system and method for {title.lower()}. "
        f"The embodiment comprises a {tech_terms[0]} configured to optimize {tech_terms[1]} "
        f"while maintaining control of {tech_terms[0]}. "
        f"Experimental results demonstrate improved {tech_terms[2]} compared to prior art."
    )


def generate_claims(abstract: str, title: str) -> list:
    return [
        f"1. A device comprising: a substrate; and an active region formed on said substrate, wherein said active region includes a {abstract.split()[3]} configured to perform a predetermined function.",
        f"2. The device of claim 1, wherein the predetermined function comprises controlling {random.choice(['current flow', 'voltage levels', 'signal propagation', 'power consumption'])}.",
        f"3. A method for manufacturing the device of claim 1, comprising the steps of: depositing a layer; patterning said layer; and etching said layer to form the active region.",
        f"4. The method of claim 3, further comprising: doping said active region with a impurity at a concentration between 1e15 and 1e20 cm-3.",
        f"5. A system incorporating the device of claim 1, wherein said system is configured for {random.choice(['high-frequency', 'low-power', 'high-voltage', 'high-temperature'])} operation.",
    ]


def generate_patents(n: int = 500) -> list:
    patents = []
    for i in range(n):
        if i < 85:
            category = "semiconductors"
        elif i < 170:
            category = "battery"
        elif i < 255:
            category = "ai_ml"
        elif i < 340:
            category = "pharma"
        elif i < 425:
            category = "ev"
        else:
            category = "solar"

        ipc_code = [k for k, v in IPC_CODES.items()][i % 10]
        title = random.choice(PATENT_TITLES[category])
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        inventor = f"{first} {last}"
        company = random.choice(COMPANIES[category])
        year = random.randint(*YEAR_RANGE)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        filing = date(year, month, day)

        if random.random() > 0.3:
            priority_days = random.randint(0, 365)
            priority = filing - timedelta(days=priority_days)
        else:
            priority = None

        if random.random() > 0.2:
            issue_days = random.randint(365, 1460)
            issue = filing + timedelta(days=issue_days)
        else:
            issue = None

        abstract = generate_abstract(title, ipc_code)
        claims = generate_claims(abstract, title)

        patent = Patent(
            patent_number=generate_patent_number(i),
            title=title,
            filing_date=filing,
            issue_date=issue,
            inventor_name=inventor,
            assignee=company,
            ipc_class=ipc_code,
            claims=PatentClaims(abstract=abstract, claims=claims),
            priority_date=priority,
            years_since_filing=(date(2025, 6, 1) - filing).days // 365,
        )
        patents.append(patent)
    return patents


PATENTS = generate_patents(500)


def search_patents(query: str = None, ipc_class: str = None,
                   year_start: int = None, year_end: int = None,
                   limit: int = 50) -> tuple:
    results = PATENTS

    if query:
        q = query.lower()
        results = [p for p in results if (
            q in p.title.lower() or
            q in p.claims.abstract.lower() or
            q in " ".join(p.claims.claims).lower() or
            q in p.inventor_name.lower() or
            q in p.assignee.lower()
        )]

    if ipc_class:
        results = [p for p in results if p.ipc_class == ipc_class]

    if year_start:
        results = [p for p in results if p.filing_date.year >= year_start]

    if year_end:
        results = [p for p in results if p.filing_date.year <= year_end]

    total = len(results)
    return total, results[:limit]


def get_patent_by_number(patent_number: str) -> Patent | None:
    for p in PATENTS:
        if p.patent_number == patent_number:
            return p
    return None


def get_patents_by_inventor(inventor_name: str) -> list:
    name = inventor_name.lower()
    return [p for p in PATENTS if name in p.inventor_name.lower()]


def get_patents_by_assignee(assignee_name: str) -> list:
    name = assignee_name.lower()
    return [p for p in PATENTS if name in p.assignee.lower()]


def get_patents_by_classification(ipc_code: str) -> list:
    return [p for p in PATENTS if p.ipc_class == ipc_code]
