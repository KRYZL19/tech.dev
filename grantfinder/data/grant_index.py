import random
from datetime import datetime, timedelta

AGENCIES = ["DOE", "EPA", "NASA", "NSF", "DOI", "USDA", "HHS", "EDA"]
SECTORS = ["broadband", "energy", "health", "environment", "technology", "infrastructure", "education", "agriculture", "housing", "transportation"]

BROADBAND_KEYWORDS = ["broadband", "rural broadband", "fiber", "internet access", "connectivity", "digital equity", "network infrastructure", "rural connectivity"]
ENERGY_KEYWORDS = ["solar", "wind", "energy efficiency", "renewable", "grid", "battery", "hydrogen", "clean energy"]
HEALTH_KEYWORDS = ["healthcare", "telemedicine", "mental health", "opioid", "rural health", "health IT", "biomedical"]
ENV_KEYWORDS = ["clean water", "air quality", "waste management", "climate", "conservation", "pollution", "remediation"]
TECH_KEYWORDS = ["AI", "machine learning", "cybersecurity", "quantum", "semiconductor", "advanced computing"]
EDU_KEYWORDS = ["STEM", "workforce development", "science education", "research infrastructure", "graduates"]
AGRI_KEYWORDS = ["farming", "rural development", "food security", "crop research", "livestock"]
INFRA_KEYWORDS = ["infrastructure", "roads", "bridges", "water systems", "transportation"]

SECTOR_KEYWORDS = {
    "broadband": BROADBAND_KEYWORDS,
    "energy": ENERGY_KEYWORDS,
    "health": HEALTH_KEYWORDS,
    "environment": ENV_KEYWORDS,
    "technology": TECH_KEYWORDS,
    "education": EDU_KEYWORDS,
    "agriculture": AGRI_KEYWORDS,
    "infrastructure": INFRA_KEYWORDS,
}

ORG_TYPES = ["local_government", "state_government", "tribal", "non_profit", "small_business", "university", "individual"]

def generate_grants():
    grants = []
    grant_num = 1
    
    for agency in AGENCIES:
        for sector in random.sample(SECTORS, k=random.randint(10, 25)):
            num_grants = random.randint(1, 3)
            for i in range(num_grants):
                deadline_days = random.randint(7, 180)
                deadline = (datetime.now() + timedelta(days=deadline_days)).strftime("%Y-%m-%d")
                
                keywords = random.sample(SECTOR_KEYWORDS.get(sector, TECH_KEYWORDS), k=random.randint(3, 6))
                
                if sector == "broadband":
                    title_options = [
                        "Rural Broadband Deployment Initiative",
                        "Community Broadband Infrastructure Grant",
                        "Digital Equity and Access Program",
                        "Last-Mile Broadband Connectivity",
                        "Fiber Optic Network Expansion",
                        "Rural Internet Service Accessibility",
                    ]
                elif sector == "energy":
                    title_options = [
                        f"{random.choice(['Solar', 'Wind', 'Clean Energy', 'Grid Modernization'])} {random.choice(['Deployment', 'Research', 'Infrastructure', 'Initiative'])}",
                        "Renewable Energy Development Program",
                        "Energy Efficiency Improvements",
                    ]
                elif sector == "health":
                    title_options = [
                        "Rural Health Care Services Expansion",
                        "Telemedicine Infrastructure Support",
                        "Community Health Improvement Program",
                        "Mental Health Services Access Grant",
                    ]
                elif sector == "environment":
                    title_options = [
                        "Environmental Remediation Program",
                        "Clean Water Infrastructure",
                        "Air Quality Improvement Initiative",
                        "Climate Resilience Project",
                    ]
                else:
                    title_options = [
                        f"{sector.title()} {random.choice(['Development', 'Research', 'Program', 'Initiative', 'Project'])}",
                        f"Advanced {sector.title()} {random.choice(['Technology', 'Infrastructure', 'Program'])}",
                    ]
                
                title = random.choice(title_options)
                
                eligibility = random.sample([
                    "Local government agencies",
                    "State government agencies",
                    "Tribal governments",
                    "501(c)(3) nonprofit organizations",
                    "Small businesses (<500 employees)",
                    "Universities and research institutions",
                    "Individual applicants (case-by-case)",
                ], k=random.randint(2, 5))
                
                award_min = random.choice([10000, 25000, 50000, 100000, 250000, 500000, 1000000])
                award_max = award_min * random.choice([2, 3, 5, 10])
                total = award_max * random.randint(5, 50)
                
                cfda_num = f"{random.randint(10, 99)}.{random.randint(100, 999)}"
                
                match_req = random.choice([
                    "25% match required",
                    "50% match required",
                    "No match required",
                    "33% match required",
                    "20% match required",
                    None
                ])
                
                grant_id = f"GRANT-{agency}-{str(grant_num).zfill(4)}"
                
                description_templates = [
                    f"This {agency} program supports {sector} initiatives in underserved communities. Funding supports planning, deployment, and implementation activities. Eligible applicants include {', '.join(eligibility[:2]).lower()}.",
                    f"The {agency} {title.lower()} provides financial assistance to accelerate {sector} projects. Priority given to projects demonstrating community impact and sustainability.",
                    f"{agency} announces funding opportunity for {sector} projects. This initiative aims to expand services to rural and underserved areas through competitive grants.",
                ]
                
                grants.append({
                    "grant_id": grant_id,
                    "title": title,
                    "agency": agency,
                    "cfda_number": cfda_num,
                    "description": random.choice(description_templates),
                    "eligibility_criteria": eligibility,
                    "award_amount_min": award_min,
                    "award_amount_max": award_max,
                    "total_funding": total,
                    "match_requirement": match_req,
                    "application_deadline": deadline,
                    "sector": [sector],
                    "keywords": keywords,
                })
                grant_num += 1
    
    return grants

GRANTS = generate_grants()

def search_grants(keyword=None, agency=None, deadline_within_days=None, limit=None):
    results = GRANTS.copy()
    
    if keyword:
        kw = keyword.lower()
        results = [g for g in results if 
                   kw in g["title"].lower() or 
                   kw in g["description"].lower() or 
                   any(kw in k.lower() for k in g["keywords"]) or
                   kw in g["sector"][0].lower()]
    
    if agency:
        results = [g for g in results if g["agency"] == agency.upper()]
    
    if deadline_within_days:
        cutoff = (datetime.now() + timedelta(days=deadline_within_days)).strftime("%Y-%m-%d")
        results = [g for g in results if g["application_deadline"] <= cutoff]
    
    if limit:
        results = results[:limit]
    
    return results

def get_grant_by_id(grant_id):
    for g in GRANTS:
        if g["grant_id"] == grant_id:
            return g
    return None

def get_grants_by_agency(agency_name):
    return [g for g in GRANTS if g["agency"] == agency_name.upper()]

def check_eligibility(org_type, annual_revenue, employees, sectors):
    eligible = []
    
    for g in GRANTS:
        score = 0
        
        # Sector match
        sector_match = any(s.lower() in [sec.lower() for sec in g["sector"]] for s in sectors)
        if sector_match:
            score += 50
        
        # Organization type check
        org_type_lower = org_type.lower().replace(" ", "_")
        if org_type_lower in ["local_government", "state_government", "tribal"]:
            if any("government" in e.lower() or "tribal" in e.lower() for e in g["eligibility_criteria"]):
                score += 30
        elif org_type_lower == "non_profit":
            if any("nonprofit" in e.lower() or "501(c)(3)" in e.lower() for e in g["eligibility_criteria"]):
                score += 30
        elif org_type_lower == "small_business":
            if any("small business" in e.lower() or "business" in e.lower() for e in g["eligibility_criteria"]):
                score += 30
        elif org_type_lower == "university":
            if any("university" in e.lower() or "research" in e.lower() for e in g["eligibility_criteria"]):
                score += 30
        
        # Size-based scoring
        if employees and employees < 500:
            if any("small business" in e.lower() for e in g["eligibility_criteria"]):
                score += 20
        
        if score >= 30:
            eligible.append({
                "grant_id": g["grant_id"],
                "title": g["title"],
                "agency": g["agency"],
                "match_score": min(score, 100)
            })
    
    return sorted(eligible, key=lambda x: x["match_score"], reverse=True)

def get_summary():
    agency_counts = {}
    sector_counts = {}
    sector_agencies = {}
    
    for g in GRANTS:
        agency = g["agency"]
        sector = g["sector"][0]
        
        agency_counts[agency] = agency_counts.get(agency, 0) + 1
        sector_counts[sector] = sector_counts.get(sector, 0) + 1
        
        if sector not in sector_agencies:
            sector_agencies[sector] = []
        if agency not in sector_agencies[sector]:
            sector_agencies[sector].append(agency)
    
    return {
        "total_grants": len(GRANTS),
        "by_agency": [{"agency": k, "total_grants": v} for k, v in sorted(agency_counts.items())],
        "by_sector": [{"sector": k, "total_grants": v, "agencies": sector_agencies[k]} for k, v in sorted(sector_counts.items())]
    }
