from fastapi import APIRouter
from models.schemas import CycleStatusRequest, CycleStatusResponse

router = APIRouter(prefix="/api/v1", tags=["cycling"])

def determine_cycle_phase(ammonia: float, nitrite: float, nitrate: float, day: int):
    """
    Determine nitrogen cycle phase based on water parameters.
    
    Phase 1 (Days 1-14): Ammonia spike - ammonia-oxidizing bacteria begin colonizing
    Phase 2 (Days 7-21): Nitrite spike - nitrite-oxidizing bacteria take over
    Phase 3 (Days 14-42): Nitrate rise - cycle completing,硝化细菌 established
    Phase 4 (Day 42+): Cycled - ammonia and nitrite both near 0, nitrate present
    """
    ammonia_high = ammonia >= 1.0
    nitrite_high = nitrite >= 1.0
    ammonia_low = ammonia < 0.25
    nitrite_low = nitrite < 0.25
    nitrate_present = nitrate > 5.0
    
    # Determine phase
    if ammonia_high and not nitrite_high:
        phase = 1
        phase_name = "Ammonia Spike"
        biochemistry = (
            "Ammonia (NH3) is building up from fish waste and decomposing organic matter. "
            "Beneficial ammonia-oxidizing bacteria (Nitrosomonas) are beginning to establish on surfaces. "
            "This is NORMAL and EXPECTED. Do NOT add more fish!"
        )
        recommendations = [
            "Test water daily - morning ammonia should be highest",
            "Do NOT add any new fish during this phase",
            "Consider partial water change (25%) if ammonia exceeds 4ppm",
            "Add bottled bacteria to speed up colonization",
            "Keep feeding to minimum - 1 small feeding every 2-3 days",
            "The spike is healthy - your filter is learning!"
        ]
        is_cycled = False
    
    elif ammonia_high and nitrite_high:
        phase = 2
        phase_name = "Nitrite Spike"
        biochemistry = (
            "Ammonia is converting to nitrite (NO2) as Nitrosomonas bacteria multiply. "
            "Nitrite is highly toxic to fish, even more dangerous than ammonia. "
            "Nitrite-oxidizing bacteria (Nitrobacter) are beginning to appear."
        )
        recommendations = [
            "Test daily - nitrite is the main threat now",
            "Do NOT add fish until nitrite drops below 0.5ppm",
            "Keep water well-aerated - oxygen helps bacteria function",
            "Consider 25-50% water change if nitrite exceeds 5ppm",
            "Maintain feeding schedule - bacteria need ammonia to grow",
            "This phase typically lasts 1-2 weeks"
        ]
        is_cycled = False
    
    elif not ammonia_low or not nitrite_low:
        phase = 2
        phase_name = "Nitrite Spike (Late)"
        biochemistry = (
            "Still in the transition phase. Ammonia processing is happening but nitrite "
            "is still accumulating because Nitrobacter hasn't fully established. "
            "Both ammonia-oxidizing and nitrite-oxidizing bacteria are growing."
        )
        recommendations = [
            "Continue testing daily",
            "Be patient - both bacterial colonies need time to mature",
            "Keep feeding light to avoid ammonia spikes",
            "Aeration is critical - increase surface agitation",
            "You're close to the end! Most beginners give up here."
        ]
        is_cycled = False
    
    elif ammonia_low and nitrite_low and nitrate_present:
        phase = 3
        phase_name = "Cycle Completion"
        biochemistry = (
            "Both ammonia and nitrite are near zero. Nitrate (NO3) is accumulating - "
            "this is the final product of the nitrogen cycle and is relatively harmless. "
            "Your biofilter is ESTABLISHED! Perform a 25-50% water change to reduce nitrate."
        )
        recommendations = [
            "Run cycle for 2-3 more days with zero ammonia/nitrite to confirm",
            "Do a 25-50% water change to lower nitrate",
            "After confirmed stable, you can add 1-3 fish at a time",
            "Quarantine new fish for 2 weeks before adding to main tank",
            "Congratulations! You made it through the hardest part."
        ]
        is_cycled = False
    
    elif day >= 28 and ammonia_low and nitrite_low:
        phase = 4
        phase_name = "Cycled"
        biochemistry = (
            "Tank is fully cycled! Ammonia and nitrite both read zero. "
            "Your biological filter is mature and can process fish waste instantly. "
            "Nitrate will rise gradually and is controlled with weekly water changes."
        )
        recommendations = [
            "Weekly 25% water changes to control nitrate below 40ppm",
            "Test monthly once stable, or weekly if heavily stocked",
            "Never exceed 50% water change at once - shocking the bacteria",
            "Your filter is now a living ecosystem - treat it well",
            "Fish-in cycling is complete. Welcome to the hobby!"
        ]
        is_cycled = True
    
    else:
        # Fallback - day < 28 but params look ok
        phase = 0
        phase_name = "Monitoring"
        biochemistry = (
            "Parameters look stable but cycle isn't complete yet. "
            "The nitrogen cycle typically takes 2-6 weeks depending on temperature, "
            "bacteria source, and ammonia levels. Don't rush it."
        )
        recommendations = [
            "Continue regular testing",
            "The nitrogen cycle cannot be rushed",
            "Most beginners quit here - stay patient!",
            "Consider adding filter media from an established tank to speed things up"
        ]
        is_cycled = False
    
    return phase, phase_name, biochemistry, recommendations, is_cycled


@router.post("/cycle/status", response_model=CycleStatusResponse)
async def cycle_status(req: CycleStatusRequest):
    """
    Analyze nitrogen cycle status based on water parameters.
    
    The nitrogen cycle is the foundation of aquarium health. It takes 2-6 weeks
    and involves beneficial bacteria converting toxic ammonia to less harmful substances.
    
    - Ammonia (NH3): Deadly to fish, from waste and decay
    - Nitrite (NO2): Also deadly, intermediate product  
    - Nitrate (NO3): Relatively harmless, final product, controlled via water changes
    """
    phase, phase_name, biochemistry, recommendations, is_cycled = determine_cycle_phase(
        req.ammonia_ppm, req.nitrite_ppm, req.nitrate_ppm, req.day_number
    )
    
    return CycleStatusResponse(
        cycle_phase=phase_name,
        phase_number=phase,
        biochemistry=biochemistry,
        recommendations=recommendations,
        is_cycled=is_cycled
    )
