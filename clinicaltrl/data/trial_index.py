from datetime import date, timedelta
from models.schemas import Trial, TrialDesign, ResultMetric, AdverseEvent
import random

# Real drug names and common conditions
DRUGS = [
    "semaglutide", "pembrolizumab", "aducanumab", "ozempic", "keytruda",
    "dupixent", "mounjaro", "wegovy", "rituximab", "nivolumab",
    "trastuzumab", "bevacizumab", "ipilimumab", "durvalumab", "atezolizumab",
    "lecanemab", "donanemab", "tirzepatide", "survodutide", "cotadutide",
    "margetuximab", "ramucirumab", "pertuzumab", "cetuximab", "panitumumab",
    "enarachene", "vosoritide", "casimersen", "golodirsen", "eteplirsen",
    "nusinersen", "risdiplam", "onasemnogene", "avacopan", "aptivus",
    "baricitinib", "tofacitinib", "upadacitinib", "filgotinib", "deucravacitinib",
    "sotrovimab", "bamlanivimab", "molnupiravir", "paxlovid", "remdesivir",
    "abaloparatide", "romosozumab", "abaloparatide", "teriparatide", "denosumab",
    "obinutuzumab", "ofatumumab", "ocrelizumab", "ofatumumab", "alemtuzumab",
    "belimumab", "anifrolumab", "voclosporin", "avacopan", "ravulizumab",
    "eculizumab", "ravulizumab", "pegcetacoplan", "nomacopan", "vilobelimab",
    "difelikefalin", "apinavir", "fostamatinib", "avapritinib", "pralsetinib",
    "selpercatinib", "capmatinib", "sotorasib", "adagrasib", "lazertinib",
    "amivantamab", "patritumab", "lumakras", "keytruda", "opdivo", "yervoy"
]

CONDITIONS = [
    "Type 2 Diabetes", "Obesity", "Rheumatoid Arthritis", "Multiple Sclerosis",
    "Psoriasis", "Atopic Dermatitis", "Asthma", "COPD", "Heart Failure",
    "Chronic Kidney Disease", "Alzheimer's Disease", "Parkinson's Disease",
    "Major Depressive Disorder", "Bipolar Disorder", "Schizophrenia",
    "Breast Cancer", "Lung Cancer", "Colorectal Cancer", "Prostate Cancer",
    "Melanoma", "Non-Small Cell Lung Cancer", "Multiple Myeloma", "Lymphoma",
    "Leukemia", "Bladder Cancer", "Pancreatic Cancer", "Ovarian Cancer",
    "Chronic Lymphocytic Leukemia", "Acute Myeloid Leukemia", "Myelofibrosis",
    "Systemic Lupus Erythematosus", "Ulcerative Colitis", "Crohn's Disease",
    "Nonalcoholic Steatohepatitis", "Primary Biliary Cholangitis", "Sarcopenia",
    "Osteoporosis", "Osteoarthritis", "Fibromyalgia", "Peripheral Neuropathy",
    "Migraine", "Epilepsy", "ALS", "Huntington Disease", "Spinal Muscular Atrophy"
]

SPONSORS = [
    "Pfizer", "Novartis", "Roche", "Johnson & Johnson", "Merck & Co",
    "Bristol Myers Squibb", "AstraZeneca", "GlaxoSmithKline", "Amgen",
    "Eli Lilly", "Gilead Sciences", "Biogen", "Regeneron", "Sanofi",
    "Bayer", "AbbVie", "Boehringer Ingelheim", "Janssen", "Astellas",
    "Takeda", "Daiichi Sankyo", "Alexion", "Vertex", "Illumina",
    "Moderna", "BioNTech", "Exact Sciences", "Illumina", "GRAIL"
]

COUNTRIES = ["United States", "Germany", "United Kingdom", "France", "Japan", "Canada", "Australia", "Spain", "Italy", "Netherlands"]
STATES = ["California", "New York", "Texas", "Massachusetts", "Florida", "Ontario", "Bavaria", "England", "Île-de-France", "Tokyo"]
CITIES = ["Boston", "New York", "Los Angeles", "Chicago", "San Francisco", "London", "Paris", "Munich", "Tokyo", "Toronto"]

def generate_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return date(year, month, day)

def generate_adverse_events(drug, phase):
    events = [
        AdverseEvent(term="Headache", serious=False, participants=random.randint(10, 200), percentage=round(random.uniform(1, 15), 1)),
        AdverseEvent(term="Nausea", serious=False, participants=random.randint(15, 180), percentage=round(random.uniform(2, 12), 1)),
        AdverseEvent(term="Fatigue", serious=False, participants=random.randint(20, 250), percentage=round(random.uniform(3, 18), 1)),
        AdverseEvent(term="Injection site reaction", serious=False, participants=random.randint(5, 100), percentage=round(random.uniform(0.5, 8), 1)),
        AdverseEvent(term="Upper respiratory infection", serious=False, participants=random.randint(10, 150), percentage=round(random.uniform(1, 10), 1)),
        AdverseEvent(term="Diarrhea", serious=False, participants=random.randint(10, 160), percentage=round(random.uniform(2, 11), 1)),
        AdverseEvent(term="Dizziness", serious=False, participants=random.randint(5, 80), percentage=round(random.uniform(0.5, 6), 1)),
    ]
    
    serious = [
        AdverseEvent(term="Serious cardiac event", serious=True, participants=random.randint(1, 15), percentage=round(random.uniform(0.1, 2), 1)),
        AdverseEvent(term="Severe hypersensitivity reaction", serious=True, participants=random.randint(0, 8), percentage=round(random.uniform(0, 1), 1)),
        AdverseEvent(term="Treatment-emergent death", serious=True, participants=random.randint(0, 5), percentage=round(random.uniform(0, 0.5), 1)),
    ]
    return events + serious

def generate_results(drug, condition, phase):
    primary_endpoints = [
        f"{condition} response rate",
        f"Change from baseline in HbA1c",
        f"Progression-free survival",
        f"All-cause mortality",
        f"Adverse event rate",
        f"Quality of life score improvement",
        f"Disease progression delay",
        f"Hospitalization rate reduction",
    ]
    
    results = [
        ResultMetric(metric=random.choice(primary_endpoints), value=f"{round(random.uniform(20, 85), 1)}%", group="Treatment"),
        ResultMetric(metric=random.choice(primary_endpoints), value=f"{round(random.uniform(10, 60), 1)}%", group="Placebo"),
        ResultMetric(metric="Overall response rate", value=f"{random.choice(['CR', 'PR', 'SD'])}", group="Treatment"),
        ResultMetric(metric="Median progression-free survival", value=f"{random.randint(6, 36)} months", group=None),
    ]
    return results

def generate_trial(nct_id_num, phase, status, drug, condition, sponsor, has_results=True):
    phase_str = f"Phase {phase}" if phase <= 3 else "Phase 4"
    enrollment = random.choice([50, 100, 200, 300, 400, 500, 750, 1000, 1500])
    
    design = TrialDesign(
        allocation=random.choice(["Randomized", "Non-randomized"]),
        intervention_model=random.choice(["Parallel Assignment", "Single Group Assignment", "Crossover Assignment"]),
        masking=random.choice(["Double Blind", "Single Blind", "Open Label"]),
        primary_purpose=random.choice(["Treatment", "Prevention", "Supportive Care", "Diagnostic"]),
        arms=[f"{drug} {random.choice(['10mg', '20mg', '50mg', '100mg'])}", "Placebo"] if has_results else [f"{drug}", "Standard of Care"]
    )
    
    success = None
    if status == "COMPLETED" and has_results:
        success = random.random() > 0.35
    
    start = generate_date(2018, 2022)
    completion = generate_date(2022, 2024) if status == "COMPLETED" else None
    
    summary_templates = [
        f"This is a randomized, double-blind study evaluating the efficacy and safety of {drug} in patients with {condition}. Patients were randomized to receive {drug} or placebo for {random.randint(12, 52)} weeks.",
        f"A Phase {phase} study to assess {drug} for the treatment of {condition}. The primary endpoint is {random.choice(['clinical response', 'safety', 'tolerability', 'efficacy'])} over a {random.randint(24, 52)}-week treatment period.",
        f"This trial investigated whether {drug} can improve outcomes in patients with {condition} compared to standard of care. Secondary endpoints included quality of life measures and biomarker responses.",
    ]
    
    eligibility = f"Inclusion Criteria:\n- Adults aged 18-75 years\n- Confirmed diagnosis of {condition}\n- Adequate organ function\n- Signed informed consent\n\nExclusion Criteria:\n- Prior treatment with {drug}\n- Active infection or malignancy\n- Pregnant or breastfeeding\n- Known hypersensitivity to study drug"
    
    brief_summary = random.choice(summary_templates)
    
    return Trial(
        nct_id=f"NCT{nct_id_num:08d}",
        title=f"A Phase {phase}, Randomized, Double-Blind Study of {drug} in Patients with {condition}",
        condition=condition,
        drug=drug,
        sponsor=sponsor,
        phase=phase_str,
        status=status,
        results_submitted=has_results,
        enrollment=enrollment,
        start_date=start,
        completion_date=completion,
        brief_summary=brief_summary,
        eligibility_criteria=eligibility,
        design_info=design,
        results=generate_results(drug, condition, phase) if has_results else [],
        serious_adverse_events=generate_adverse_events(drug, phase) if has_results else [],
        location_country=random.choice(COUNTRIES),
        location_state=random.choice(STATES) if random.random() > 0.3 else None,
        location_city=random.choice(CITIES) if random.random() > 0.4 else None,
        success=success
    )

# Generate 200 trials
def get_all_trials():
    trials = []
    statuses = ["COMPLETED"] * 140 + ["ACTIVE_NOT_RECRUITING"] * 30 + ["RECRUITING"] * 20 + ["TERMINATED"] * 10
    
    for i in range(200):
        nct_num = 10000000 + i
        phase = random.choice([1, 2, 3, 3, 3, 4])
        status = random.choice(statuses)
        drug = random.choice(DRUGS)
        condition = random.choice(CONDITIONS)
        sponsor = random.choice(SPONSORS)
        has_results = status == "COMPLETED" and random.random() > 0.2
        
        trial = generate_trial(nct_num, phase, status, drug, condition, sponsor, has_results)
        trials.append(trial)
    
    return trials

TRIALS = get_all_trials()
TRIAL_INDEX = {t.nct_id: t for t in TRIALS}
DRUG_INDEX = {}
SPONSOR_INDEX = {}
LOCATION_INDEX = {}

for t in TRIALS:
    if t.drug not in DRUG_INDEX:
        DRUG_INDEX[t.drug] = []
    DRUG_INDEX[t.drug].append(t)
    
    if t.sponsor not in SPONSOR_INDEX:
        SPONSOR_INDEX[t.sponsor] = []
    SPONSOR_INDEX[t.sponsor].append(t)
    
    key = (t.location_country, t.location_state)
    if key not in LOCATION_INDEX:
        LOCATION_INDEX[key] = []
    LOCATION_INDEX[key].append(t)
