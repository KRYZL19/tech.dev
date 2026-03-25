from fastapi import APIRouter
from models.schemas import ScheduleRequest, ScheduleResponse, ScheduledItem
from utils.optimizer import optimize_schedule

router = APIRouter(prefix="/optimize", tags=["optimization"])


@router.post("/schedule", response_model=ScheduleResponse)
async def optimize_schedule_endpoint(request: ScheduleRequest):
    min_hour = 0
    max_hour = 24

    if request.options:
        if request.options.min_start_hour is not None:
            min_hour = request.options.min_start_hour
        if request.options.max_start_hour is not None:
            max_hour = request.options.max_start_hour

    schedule_result = optimize_schedule(
        request.appliances,
        request.tariff,
        min_hour,
        max_hour
    )

    schedule_items = [
        ScheduledItem(appliance=name, start_hour=start, end_hour=end, cost=cost)
        for name, start, end, cost in schedule_result
    ]

    total_cost = sum(item.cost for item in schedule_items)
    total_duration = sum(
        app.duration_hours for app in request.appliances
    )

    return ScheduleResponse(
        schedule=schedule_items,
        total_cost=round(total_cost, 4),
        total_duration=total_duration
    )
