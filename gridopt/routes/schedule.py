from fastapi import APIRouter, HTTPException
from models.schemas import OptimizeScheduleRequest, ScheduleResponse
from utils.optimizer import greedy_optimize


router = APIRouter(prefix="/api/v1/optimize", tags=["optimize"])


@router.post("/schedule", response_model=ScheduleResponse)
def optimize_schedule(request: OptimizeScheduleRequest):
    """
    Optimize device scheduling for a given utility.
    
    Uses a greedy algorithm to schedule devices during off-peak hours.
    """
    try:
        devices = [d.model_dump() for d in request.devices]
        result = greedy_optimize(
            utility_id=request.utility_id,
            devices=devices,
            start_hour=request.start_hour,
            end_hour=request.end_hour,
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Optimization failed: {str(e)}")
