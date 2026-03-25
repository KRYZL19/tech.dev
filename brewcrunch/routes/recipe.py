"""Recipe routes for BREWCRUNCH API."""

from fastapi import APIRouter, HTTPException
from typing import List

from models.schemas import (
    RecipeCheckRequest,
    StyleCheckResponse,
    StyleMatch,
)
from data.bjcp_styles import BJCP_STYLES

router = APIRouter(prefix="/recipe", tags=["Recipe"])


def calculate_style_score(og: float, fg: float, abv: float, ibu: float, style: dict) -> StyleMatch:
    """Calculate how well a recipe matches a BJCP style."""
    
    og_min, og_max = style["og_range"]
    fg_min, fg_max = style["fg_range"]
    abv_min, abv_max = style["abv_range"]
    ibu_min, ibu_max = style["ibu_range"]
    
    # Check if values fall within range
    og_match = og_min <= og <= og_max
    fg_match = fg_min <= fg <= fg_max
    abv_match = abv_min <= abv <= abv_max
    ibu_match = ibu_min <= ibu <= ibu_max
    
    # Calculate score based on distance from range centers
    score = 0
    
    # Each parameter contributes up to 25 points
    if og_match:
        score += 25
    else:
        # Partial score based on how close
        og_mid = (og_min + og_max) / 2
        og_dist = abs(og - og_mid) / (og_max - og_min) if og_max != og_min else 0
        score += max(0, 25 - (og_dist * 25))
    
    if fg_match:
        score += 25
    else:
        fg_mid = (fg_min + fg_max) / 2
        fg_dist = abs(fg - fg_mid) / (fg_max - fg_min) if fg_max != fg_min else 0
        score += max(0, 25 - (fg_dist * 25))
    
    if abv_match:
        score += 25
    else:
        abv_mid = (abv_min + abv_max) / 2
        abv_dist = abs(abv - abv_mid) / (abv_max - abv_min) if abv_max != abv_min else 0
        score += max(0, 25 - (abv_dist * 25))
    
    if ibu_match:
        score += 25
    else:
        ibu_mid = (ibu_min + ibu_max) / 2
        ibu_dist = abs(ibu - ibu_mid) / (ibu_max - ibu_min) if ibu_max != ibu_min else 0
        score += max(0, 25 - (ibu_dist * 25))
    
    return StyleMatch(
        name=style["name"],
        category=style["category"],
        score=round(score, 1),
        og_match=og_match,
        fg_match=fg_match,
        abv_match=abv_match,
        ibu_match=ibu_match,
    )


@router.post("/check-style", response_model=StyleCheckResponse)
async def check_style(request: RecipeCheckRequest):
    """
    Check which BJCP styles a recipe matches.
    
    - **og**: Original Gravity
    - **fg**: Final Gravity
    - **ibu**: International Bitterness Units
    - **abv**: Alcohol by Volume %
    """
    if request.fg >= request.og:
        raise HTTPException(
            status_code=400,
            detail="Final gravity must be less than original gravity",
        )
    
    # Calculate ABV if not provided (should be from request)
    if request.abv <= 0:
        abv = (request.og - request.fg) * 131.25
    else:
        abv = request.abv
    
    matches = []
    for style in BJCP_STYLES:
        match = calculate_style_score(request.og, request.fg, abv, request.ibu, style)
        matches.append(match)
    
    # Sort by score descending
    matches.sort(key=lambda x: x.score, reverse=True)
    
    return StyleCheckResponse(
        matches=matches,
        total_submitted=len(matches),
    )
