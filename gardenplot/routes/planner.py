"""Planner routes for GARDENPLOT."""

from fastapi import APIRouter, HTTPException
from models.schemas import (
    WhatGrowsRequest,
    WhatGrowsResponse,
    SpacingRecommendation,
    ExpectedYield,
)
from data.plant_data import (
    PLANTS,
    PLANT_FAMILIES,
    GOALS_MAPPING,
    USDA_ZONES,
    get_plants_by_zone,
    get_plants_by_sunlight,
    get_shade_tolerant_plants,
)

router = APIRouter(prefix="/api/v1/planner", tags=["planner"])


@router.post("/what-grows", response_model=WhatGrowsResponse)
async def what_grows(request: WhatGrowsRequest):
    """
    Determine what vegetables will grow well in your garden.
    
    Based on your zone, sunlight hours, available space, and goals,
    returns suitable vegetables with spacing recommendations and expected yield.
    """
    # Validate zone
    if request.zone not in USDA_ZONES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid zone. Must be one of: {list(USDA_ZONES.keys())}"
        )
    
    zone_data = USDA_ZONES[request.zone]
    growing_days = zone_data["growing_days"]
    
    # Get plants by sunlight
    sun_suitable = get_plants_by_sunlight(request.sunlight_hours)
    
    # Get plants by zone/growing days
    zone_suitable = get_plants_by_zone(request.zone)
    
    # Filter by goals if provided
    goal_plants = set()
    if request.goals:
        for goal in request.goals:
            if goal in GOALS_MAPPING:
                goal_plants.update(GOALS_MAPPING[goal])
    
    # Find intersection of all criteria
    suitable_plants = set(sun_suitable) & set(zone_suitable)
    
    if goal_plants:
        suitable_plants &= goal_plants
    
    # Sort by a combination of days to maturity and yield
    scored_plants = []
    for plant_key in suitable_plants:
        plant = PLANTS[plant_key]
        score = (plant["yield_per_plant_lbs"] * 100) / max(plant["days_to_maturity"], 1)
        scored_plants.append((plant_key, score))
    
    scored_plants.sort(key=lambda x: x[1], reverse=True)
    vegetables = [p[0] for p in scored_plants[:12]]  # Limit to top 12
    
    # Generate spacing recommendations
    spacing_recommendations = []
    sqft_per_plant = 1.0  # Base calculation
    
    for veg in vegetables:
        plant = PLANTS[veg]
        # Calculate plants per square foot based on spacing
        spacing = plant["spacing_inches"]
        if spacing <= 6:
            plants_per_sqft = 4
        elif spacing <= 12:
            plants_per_sqft = 1
        elif spacing <= 18:
            plants_per_sqft = 0.8
        elif spacing <= 24:
            plants_per_sqft = 0.5
        else:
            plants_per_sqft = 0.25
        
        total_count = int(request.space_sqft * plants_per_sqft)
        if total_count < 1:
            total_count = 1
        
        spacing_recommendations.append(SpacingRecommendation(
            plant=veg,
            plants_per_sqft=plants_per_sqft,
            total_count=total_count,
            spacing_note=f"Plant {veg} {spacing}\" apart"
        ))
    
    # Generate expected yield
    expected_yield = []
    for veg in vegetables:
        plant = PLANTS[veg]
        # Find spacing rec for this plant
        rec = next((r for r in spacing_recommendations if r.plant == veg), None)
        if rec:
            total_yield = plant["yield_per_plant_lbs"] * rec.total_count
            expected_yield.append(ExpectedYield(
                plant=veg,
                estimated_lbs_per_season=round(total_yield, 2),
                harvest_window_days=plant["harvest_window_days"]
            ))
    
    # Generate shade insight
    shade_insight = None
    if request.sunlight_hours <= 4:
        shade_plants = [p for p in vegetables if PLANTS[p]["sun_hours_min"] <= 4]
        if shade_plants:
            shade_insight = (
                f"Your shade pattern means these {len(shade_plants)} vegetables will actually work. "
                f"Here's what: {', '.join(shade_plants[:6])}. "
                f"These shade-tolerant varieties thrive with only {request.sunlight_hours} hours of sun."
            )
    
    return WhatGrowsResponse(
        vegetables=vegetables,
        spacing_recommendations=spacing_recommendations,
        expected_yield=expected_yield,
        shade_insight=shade_insight
    )
