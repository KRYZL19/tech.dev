from datetime import datetime
from data.tou_tariffs import get_tariff


def greedy_optimize(
    utility_id: str,
    devices: list[dict],
    start_hour: int = 0,
    end_hour: int = 24,
    carbon_intensity: list[tuple[int, float]] | None = None,
) -> dict:
    """
    Greedy scheduling algorithm.
    
    Sort devices by priority (ascending = highest first), then greedily
    assign each device to the cheapest available window.
    """
    tariff = get_tariff(utility_id)
    if not tariff:
        raise ValueError(f"Unknown utility: {utility_id}")

    periods = tariff["periods"]
    
    # Build hourly price lookup
    hourly_prices = {}
    for period in periods:
        for h in range(period["start_hour"], period["end_hour"]):
            hourly_prices[h] = period["price"]

    # Sort devices by priority (lower number = higher priority)
    sorted_devices = sorted(devices, key=lambda d: d["priority"])

    schedule = []
    occupied = {}  # hour -> list of (device_name, start, end)

    for device in sorted_devices:
        duration = device["duration_hours"]
        priority = device["priority"]
        power_kw = device.get("power_kw", 1.0)
        name = device["name"]

        best_window = None
        best_cost = float("inf")

        # Try every possible start hour in the window
        for start in range(start_hour, end_hour - int(duration) + 1):
            # Check if window is available
            end = start + int(duration)
            window_hours = list(range(start, end))
            
            # Verify all hours are within our window
            if any(h < start_hour or h >= end_hour for h in window_hours):
                continue

            # Check for conflicts
            if any(h in occupied for h in window_hours):
                continue

            # Calculate cost for this window
            total_cost = sum(hourly_prices.get(h, 0) * power_kw for h in window_hours)

            # Factor in carbon if weight > 0
            if carbon_intensity and carbon_intensity[0][1] > 0:
                carbon_cost = sum(
                    hourly_prices.get(h, 0) * carbon_intensity[h][1] * power_kw
                    for h in window_hours
                )
                total_cost = (1 - carbon_intensity[2]) * total_cost + carbon_intensity[2] * carbon_cost

            if total_cost < best_cost:
                best_cost = total_cost
                best_window = (start, end)

        if best_window:
            start, end = best_window
            for h in range(start, end):
                occupied[h] = True
            schedule.append({
                "name": name,
                "start_time": f"{start:02d}:00",
                "end_time": f"{end:02d}:00",
                "duration_hours": duration,
                "cost": round(best_cost, 4),
                "priority": priority,
                "power_kw": power_kw,
            })

    # Calculate totals
    flat_rate = tariff["flat_rate"]
    total_cost = sum(s["cost"] for s in schedule)
    total_kwh = sum(s["duration_hours"] * s["power_kw"] for s in schedule)
    flat_rate_cost = total_kwh * flat_rate

    return {
        "utility_id": utility_id,
        "scheduled_devices": schedule,
        "total_cost": round(total_cost, 4),
        "flat_rate_cost": round(flat_rate_cost, 4),
        "savings_percent": round((1 - total_cost / flat_rate_cost) * 100, 1) if flat_rate_cost > 0 else 0,
    }
