"""Knot API routes."""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from data.knot_data import KNOTS_DATA, KNOTS_BY_NAME, KNOTS_BY_CATEGORY, KNOTS_BY_USE_CASE
from models.schemas import KnotSummary, KnotDetail, SearchResult

router = APIRouter(prefix="/api/v1", tags=["knots"])


@router.get("/knots", response_model=List[KnotSummary])
async def list_knots():
    """List all knots with summary information."""
    return [
        KnotSummary(
            name=knot["name"],
            category=knot["category"],
            difficulty_rating=knot["difficulty_rating"],
            strength_pct=knot["strength_pct"],
            use_cases=knot["use_cases"]
        )
        for knot in KNOTS_DATA
    ]


@router.get("/knot/{name}", response_model=KnotDetail)
async def get_knot(name: str):
    """Get full details for a specific knot."""
    knot = KNOTS_BY_NAME.get(name)
    if not knot:
        raise HTTPException(status_code=404, detail=f"Knot '{name}' not found")
    
    return KnotDetail(**knot)


@router.get("/knots/category/{category}", response_model=List[KnotSummary])
async def get_knots_by_category(category: str):
    """Filter knots by category."""
    valid_categories = ["bending", "binding", "loop", "stopper", "slip", "hitch"]
    if category not in valid_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Must be one of: {', '.join(valid_categories)}"
        )
    
    knots = KNOTS_BY_CATEGORY.get(category, [])
    return [
        KnotSummary(
            name=knot["name"],
            category=knot["category"],
            difficulty_rating=knot["difficulty_rating"],
            strength_pct=knot["strength_pct"],
            use_cases=knot["use_cases"]
        )
        for knot in knots
    ]


@router.get("/knots/search", response_model=SearchResult)
async def search_knots_by_use_case(
    use_case: str = Query(..., description="Use case to search for")
):
    """Find knots suitable for a specific use case."""
    # Normalize and match use cases
    use_case_lower = use_case.lower().strip()
    
    # Direct match first
    matching = KNOTS_BY_USE_CASE.get(use_case_lower, [])
    
    # Also search by partial match
    if not matching:
        for uc, knots in KNOTS_BY_USE_CASE.items():
            if use_case_lower in uc or uc in use_case_lower:
                matching = knots
                break
    
    # Also search in knot names and descriptions
    if not matching:
        for knot in KNOTS_DATA:
            if (use_case_lower in knot["name"].lower() or
                use_case_lower in knot["proper_use"].lower() or
                use_case_lower in knot["when_not_to_use"].lower()):
                matching.append(knot)
    
    if not matching:
        raise HTTPException(
            status_code=404,
            detail=f"No knots found for use case '{use_case}'"
        )
    
    return SearchResult(
        use_case=use_case,
        matching_knots=[
            KnotSummary(
                name=knot["name"],
                category=knot["category"],
                difficulty_rating=knot["difficulty_rating"],
                strength_pct=knot["strength_pct"],
                use_cases=knot["use_cases"]
            )
            for knot in matching
        ],
        count=len(matching)
    )


@router.get("/categories", response_model=List[str])
async def list_categories():
    """List all available categories."""
    return ["bending", "binding", "loop", "stopper", "slip", "hitch"]


@router.get("/use-cases", response_model=List[str])
async def list_use_cases():
    """List all available use cases."""
    return sorted(KNOTS_BY_USE_CASE.keys())
