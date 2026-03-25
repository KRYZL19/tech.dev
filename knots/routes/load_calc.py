"""Load calculation and comparison routes."""

from fastapi import APIRouter, HTTPException
from data.knot_data import KNOTS_BY_NAME
from models.schemas import LoadCompareRequest, ComparisonResult, StrengthComparison

router = APIRouter(prefix="/api/v1", tags=["load"])


def determine_failure_mode(knot_name: str, load_lbs: float, safety_factor: float) -> str:
    """Determine the likely failure mode based on knot and load characteristics."""
    knot = KNOTS_BY_NAME.get(knot_name, {})
    category = knot.get("category", "unknown")
    
    if safety_factor < 1.0:
        return "IMMEDIATE FAILURE: Load exceeds breaking strength"
    
    if safety_factor < 1.5:
        base_mode = "High stress - rope fibers beginning to compress and deform"
    elif safety_factor < 2.0:
        base_mode = "Moderate stress - normal working load range"
    else:
        base_mode = "Low stress - well within safe working load"
    
    # Add knot-specific failure modes
    if category == "loop":
        base_mode += ". Loop geometry critical - asymmetry increases stress."
    elif category == "hitch":
        base_mode += ". Hitch grip may slip on contact surface."
    elif category == "binding":
        base_mode += ". Binding may compress and deform over time."
    elif category == "bending":
        base_mode += ". Bending stress concentrated at crossover points."
    
    return base_mode


def generate_recommendation(
    knot1_name: str,
    knot2_name: str,
    load_lbs: float,
    sf1: float,
    sf2: float,
    stronger: str
) -> str:
    """Generate a recommendation based on the comparison."""
    knot1 = KNOTS_BY_NAME.get(knot1_name, {})
    knot2 = KNOTS_BY_NAME.get(knot2_name, {})
    
    recs = []
    
    # Safety recommendation
    if sf1 < 1.5 or sf2 < 1.5:
        recs.append("⚠️ WARNING: At least one knot is near its breaking limit for this load.")
    elif sf1 < 2.0 or sf2 < 2.0:
        recs.append("⚡ Consider additional safety margin for dynamic or shock loads.")
    
    # Specific recommendations
    if stronger == knot1_name:
        recs.append(f"✓ {knot1_name} ({sf1:.1f}x safety factor) is the stronger choice.")
    else:
        recs.append(f"✓ {knot2_name} ({sf2:.1f}x safety factor) is the stronger choice.")
    
    # Category-based advice
    cat1 = knot1.get("category", "")
    cat2 = knot2.get("category", "")
    
    if cat1 == cat2:
        recs.append(f"Both knots are {cat1} type - consider other factors like ease of tying/untying.")
    else:
        recs.append(f"Difference: {knot1_name} is {cat1}, {knot2_name} is {cat2}.")
    
    # Difficulty advice
    diff1 = knot1.get("difficulty_rating", 3)
    diff2 = knot2.get("difficulty_rating", 3)
    
    if abs(diff1 - diff2) > 1:
        easier = knot1_name if diff1 < diff2 else knot2_name
        recs.append(f"{easier} is easier to tie under pressure.")
    
    return " ".join(recs)


@router.post("/load/compare", response_model=ComparisonResult)
async def compare_knots(request: LoadCompareRequest):
    """Compare two knots under a given load."""
    knot1 = KNOTS_BY_NAME.get(request.knot1_name)
    knot2 = KNOTS_BY_NAME.get(request.knot2_name)
    
    if not knot1:
        raise HTTPException(status_code=404, detail=f"Knot '{request.knot1_name}' not found")
    if not knot2:
        raise HTTPException(status_code=404, detail=f"Knot '{request.knot2_name}' not found")
    
    sf1 = knot1["breaking_strength_lbs"] / request.load_lbs
    sf2 = knot2["breaking_strength_lbs"] / request.load_lbs
    
    stronger = knot1["name"] if sf1 >= sf2 else knot2["name"]
    
    comparison = StrengthComparison(
        knot1_name=knot1["name"],
        knot2_name=knot2["name"],
        knot1_strength_pct=knot1["strength_pct"],
        knot2_strength_pct=knot2["strength_pct"],
        knot1_breaking_lbs=knot1["breaking_strength_lbs"],
        knot2_breaking_lbs=knot2["breaking_strength_lbs"],
        load_lbs=request.load_lbs,
        knot1_safety_factor=round(sf1, 2),
        knot2_safety_factor=round(sf2, 2),
        stronger_knot=stronger,
        strength_difference_pct=abs(knot1["strength_pct"] - knot2["strength_pct"])
    )
    
    failure_mode = determine_failure_mode(
        stronger, request.load_lbs, 
        sf1 if stronger == knot1["name"] else sf2
    )
    
    recommendation = generate_recommendation(
        knot1["name"], knot2["name"], request.load_lbs, sf1, sf2, stronger
    )
    
    return ComparisonResult(
        comparison=comparison,
        failure_mode=failure_mode,
        recommendation=recommendation
    )


@router.get("/load/calculate/{knot_name}")
async def calculate_load_capacity(knot_name: str):
    """Calculate load capacity for a single knot."""
    knot = KNOTS_BY_NAME.get(knot_name)
    if not knot:
        raise HTTPException(status_code=404, detail=f"Knot '{knot_name}' not found")
    
    breaking = knot["breaking_strength_lbs"]
    
    return {
        "knot_name": knot_name,
        "breaking_strength_lbs": breaking,
        "safe_working_load_lbs": round(breaking / 3, 1),  # 3:1 safety factor typical
        "safe_working_load_kg": round(breaking / 3 / 2.205, 1),
        "maximum_load_lbs": breaking,
        "strength_pct": knot["strength_pct"],
        "category": knot["category"]
    }
