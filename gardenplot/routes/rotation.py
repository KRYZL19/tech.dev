"""Rotation and companion routes for GARDENPLOT."""

from fastapi import APIRouter, HTTPException
from models.schemas import (
    RotationPlanRequest,
    RotationPlanResponse,
    SeasonPlan,
    CompanionCheckRequest,
    CompanionCheckResponse,
)
from data.plant_data import (
    PLANTS,
    PLANT_FAMILIES,
    COMPANION_MATRIX,
    USDA_ZONES,
)

router = APIRouter(tags=["rotation"])

# Family rotation order to prevent disease buildup
FAMILY_ROTATION_ORDER = [
    ["Solanaceae", "Fabaceae"],  # Year 1: Nightshades, then Legumes
    ["Brassicaceae", "Cucurbitaceae"],  # Year 2: Cabbage family, then Gourds
    ["Apiaceae", "Amaryllidaceae"],  # Year 3: Carrot family, then Onions
    ["Fabaceae", "Asteraceae"],  # Year 4: Legumes, then Lettuce family
]

FALL_CROPS = ["kale", "spinach", "lettuce", "beet", "radish", "turnip", "garlic"]
SPRING_CROPS = ["pea", "lettuce", "spinach", "radish", "onion", "beet", "kale"]
SUMMER_CROPS = ["tomato", "pepper", "cucumber", "zucchini", "bean", "corn"]


def get_next_season_crops(family: str, season: str) -> list:
    """Get recommended crops for next season based on plant family."""
    suggestions = []
    
    # Recommend crops from different families to break pest/disease cycles
    if family in ["Solanaceae", "Cucurbitaceae"]:
        suggestions = ["bean", "pea"]  # Legumes fix nitrogen
    elif family in ["Fabaceae"]:
        suggestions = ["carrot", "onion"]  # Root vegetables
    elif family in ["Brassicaceae"]:
        suggestions = ["bean", "corn"]  # Different nutrient needs
    elif family in ["Apiaceae", "Amaryllidaceae"]:
        suggestions = ["tomato", "pepper"]  # Heavy feeders
    else:
        suggestions = ["bean", "pea", "lettuce"]
    
    # Add season-specific crops
    if season == "spring":
        suggestions = [s for s in suggestions if s in SPRING_CROPS or s in ["pea", "bean"]]
    elif season == "summer":
        suggestions = [s for s in suggestions if s in SUMMER_CROPS]
    elif season == "fall":
        suggestions = [s for s in suggestions if s in FALL_CROPS]
    
    return suggestions[:4]


@router.post("/api/v1/rotation/plan", response_model=RotationPlanResponse)
async def plan_rotation(request: RotationPlanRequest):
    """
    Create a 3-season crop rotation plan for your garden.
    
    Based on your current plot layout, generates recommendations for
    season 1, 2, and 3 with disease prevention notes.
    """
    if not request.plot_layout:
        raise HTTPException(status_code=400, detail="plot_layout cannot be empty")
    
    disease_notes = []
    family_uses = {}
    
    # Analyze current family usage
    for section in request.plot_layout:
        family = section.plant_family
        if family not in family_uses:
            family_uses[family] = []
        family_uses[family].append(section.section_id)
    
    # Generate season 1 plan
    season_1_sections = []
    for section in request.plot_layout:
        family = section.plant_family
        next_crops = get_next_season_crops(family, "spring")
        
        # Check for disease risk
        if family in ["Solanaceae"]:
            disease_notes.append(f"Section {section.section_id}: Avoid tomatoes/peppers for 3 years after Solanaceae crops.")
        elif family in ["Brassicaceae"]:
            disease_notes.append(f"Section {section.section_id}: Rotate Brassicas with non-Brassica crops to prevent clubroot.")
        
        season_1_sections.append({
            "section_id": section.section_id,
            "plant_from": section.current_plant,
            "recommended_next": next_crops[0] if next_crops else "lettuce",
            "reason": f"Rotate away from {family} family"
        })
    
    # Generate season 2 plan (rotate to different families)
    season_2_sections = []
    used_families = list(family_uses.keys())
    for section in request.plot_layout:
        # Recommend crops from families not used in current layout
        available_families = [f for f in PLANT_FAMILIES.keys() if f not in used_families]
        if not available_families:
            available_families = list(PLANT_FAMILIES.keys())
        
        # Pick a family and a plant from it
        target_family = available_families[len(season_2_sections) % len(available_families)]
        family_plants = PLANT_FAMILIES.get(target_family, ["lettuce"])
        target_plant = family_plants[0]
        
        season_2_sections.append({
            "section_id": section.section_id,
            "recommended_plant": target_plant,
            "plant_family": target_family,
            "reason": f"Second year rotation - {target_family} family"
        })
    
    # Generate season 3 plan (legume year for nitrogen fixation)
    season_3_sections = []
    for section in request.plot_layout:
        season_3_sections.append({
            "section_id": section.section_id,
            "recommended_plant": "bean",
            "plant_family": "Fabaceae",
            "reason": "Third year - plant legumes to fix nitrogen for next cycle"
        })
    
    # Add general disease prevention notes
    unique_families = list(family_uses.keys())
    if len(unique_families) >= 2:
        disease_notes.append(
            "Good rotation practice: Wait 3-4 years before planting the same family "
            "in the same location to prevent soil-borne diseases."
        )
    
    disease_notes.append(
        "Tip: Plant marigolds or nasturtiums near vegetables to deter pests naturally."
    )
    
    return RotationPlanResponse(
        season_1=SeasonPlan(
            season="Spring/Summer Year 1",
            sections=season_1_sections,
            recommended_plantings=[c["recommended_next"] for c in season_1_sections]
        ),
        season_2=SeasonPlan(
            season="Year 2",
            sections=season_2_sections,
            recommended_plantings=[s["recommended_plant"] for s in season_2_sections]
        ),
        season_3=SeasonPlan(
            season="Year 3",
            sections=season_3_sections,
            recommended_plantings=[s["recommended_plant"] for s in season_3_sections]
        ),
        disease_prevention_notes=disease_notes
    )


@router.post("/api/v1/companion/check", response_model=CompanionCheckResponse)
async def check_companion(request: CompanionCheckRequest):
    """
    Check companion planting compatibility between two plants.
    
    Returns compatibility score (0-100), reasoning, and tips for success.
    """
    plant_a = request.plant_a.lower().replace(" ", "_")
    plant_b = request.plant_b.lower().replace(" ", "_")
    
    # Get companion data for both plants
    data_a = COMPANION_MATRIX.get(plant_a, {})
    data_b = COMPANION_MATRIX.get(plant_b, {})
    
    companions_a = data_a.get("companions", [])
    enemies_a = data_a.get("enemies", [])
    companions_b = data_b.get("companions", [])
    enemies_b = data_b.get("enemies", [])
    
    # Calculate compatibility score
    score = 50  # Base score
    
    # Both list each other as companions
    if plant_b in companions_a and plant_a in companions_b:
        score = 95
        reason = f"{PLANTS.get(plant_a, {}).get('name', plant_a.title())} and {PLANTS.get(plant_b, {}).get('name', plant_b.title())} are excellent companions! They mutually benefit each other."
        tips = [
            f"Plant {PLANTS.get(plant_a, {}).get('name', plant_a)} near {PLANTS.get(plant_b, {}).get('name', plant_b)} for optimal growth.",
            "Both plants can share space without competing for nutrients.",
            "Consider interplanting for natural pest deterrence."
        ]
    # One lists the other as companion
    elif plant_b in companions_a:
        score = 80
        reason = f"{PLANTS.get(plant_a, {}).get('name', plant_a.title())} benefits from being near {PLANTS.get(plant_b, {}).get('name', plant_b.title())}."
        tips = [
            f"Good companion pairing - plant near each other.",
            "Watch for any signs of competition as plants mature."
        ]
    elif plant_a in companions_b:
        score = 80
        reason = f"{PLANTS.get(plant_b, {}).get('name', plant_b.title())} benefits from being near {PLANTS.get(plant_a, {}).get('name', plant_a.title())}."
        tips = [
            f"Good companion pairing - plant near each other.",
            "Consider spacing needs as plants grow."
        ]
    # One lists the other as enemy
    elif plant_b in enemies_a:
        score = 20
        reason = f"{PLANTS.get(plant_a, {}).get('name', plant_a.title())} and {PLANTS.get(plant_b, {}).get('name', plant_b.title())} should NOT be planted together."
        tips = [
            f"Avoid planting {PLANTS.get(plant_a, {}).get('name', plant_a)} near {PLANTS.get(plant_b, {}).get('name', plant_b)}.",
            "These plants compete for nutrients or attract harmful pests to each other.",
            "Keep at least 4 feet apart if both must be grown."
        ]
    elif plant_a in enemies_b:
        score = 20
        reason = f"{PLANTS.get(plant_a, {}).get('name', plant_a.title())} and {PLANTS.get(plant_b, {}).get('name', plant_b.title())} should NOT be planted together."
        tips = [
            f"Avoid planting {PLANTS.get(plant_b, {}).get('name', plant_b)} near {PLANTS.get(plant_a, {}).get('name', plant_a)}.",
            "These plants may stunt each other's growth.",
            "Separate by at least one row of different crops."
        ]
    else:
        score = 50
        reason = f"{PLANTS.get(plant_a, {}).get('name', plant_a.title())} and {PLANTS.get(plant_b, {}).get('name', plant_b.title())} have no strong interaction."
        tips = [
            "Neutral companion relationship.",
            "Safe to plant together with proper spacing.",
            "Monitor plants for any unexpected interactions."
        ]
    
    return CompanionCheckResponse(
        plant_a=PLANTS.get(plant_a, {}).get("name", plant_a.title()),
        plant_b=PLANTS.get(plant_b, {}).get("name", plant_b.title()),
        compatibility_score=score,
        reason=reason,
        tips=tips
    )


@router.get("/api/v1/frost/{zipcode}", response_model=dict)
async def get_frost_dates(zipcode: str):
    """
    Get frost dates for a US zipcode.
    
    Returns estimated last spring frost and first fall frost dates
    based on USDA zone lookup.
    """
    # Simple zipcode to zone mapping (first digit approximates zone)
    # This is a simplified mapping - production would use a proper database
    zip_prefix = zipcode[0] if zipcode else "0"
    
    zone_map = {
        "0": "3", "1": "4", "2": "5", "3": "6",
        "4": "6", "5": "7", "6": "7", "7": "8",
        "8": "9", "9": "10"
    }
    
    zone = zone_map.get(zip_prefix, "6")
    zone_data = USDA_ZONES[zone]
    
    return {
        "zipcode": zipcode,
        "zone": zone,
        "last_frost_spring": zone_data["last_frost_spring"],
        "first_frost_fall": zone_data["first_frost_fall"],
        "growing_days": zone_data["growing_days"]
    }


@router.get("/api/v1/plant/{name}", response_model=dict)
async def get_plant_details(name: str):
    """
    Get detailed information about a specific plant.
    """
    plant_key = name.lower().replace(" ", "_")
    
    if plant_key not in PLANTS:
        raise HTTPException(
            status_code=404,
            detail=f"Plant '{name}' not found. Available plants: {list(PLANTS.keys())}"
        )
    
    plant = PLANTS[plant_key]
    companion_data = COMPANION_MATRIX.get(plant_key, {})
    
    return {
        "name": plant["name"],
        "family": plant["family"],
        "days_to_maturity": plant["days_to_maturity"],
        "sun_hours_min": plant["sun_hours_min"],
        "spacing_inches": plant["spacing_inches"],
        "frost_tolerance": plant["frost_tolerance"],
        "companions": companion_data.get("companions", []),
        "enemies": companion_data.get("enemies", []),
        "harvest_window_days": plant["harvest_window_days"],
        "yield_per_plant_lbs": plant["yield_per_plant_lbs"],
        "water_needs": plant["water_needs"],
        "soil_ph": plant["soil_ph"],
        "nitrogen_needs": plant["nitrogen_needs"]
    }
