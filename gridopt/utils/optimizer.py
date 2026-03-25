"""Simple greedy optimizer for appliance scheduling under TOU tariffs."""

from typing import Optional
from models.schemas import Appliance, TariffResponse, TariffPeriod


def get_price_for_hour(periods: list[TariffPeriod], hour: int) -> float:
    """Get the price per kWh for a given hour based on tariff periods."""
    for period in periods:
        if period.start_hour <= hour < period.end_hour:
            return period.price_per_kwh
    # Handle wraparound for periods like 22-24
    for period in periods:
        if period.start_hour <= hour or hour < period.end_hour:
            if period.start_hour > period.end_hour:
                return period.price_per_kwh
    return 0.0


def get_cheapest_window(periods: list[TariffPeriod], duration_hours: float, min_hour: int = 0, max_hour: int = 24) -> tuple[int, float]:
    """
    Find the cheapest consecutive window of hours for an appliance.
    Returns (start_hour, total_cost).
    """
    if max_hour - min_hour < duration_hours:
        min_hour = 0
        max_hour = 24

    best_start = min_hour
    best_cost = float('inf')

    # Try each possible start hour
    for start in range(min_hour, max_hour - int(duration_hours) + 1):
        total_cost = 0.0
        for h in range(start, start + int(duration_hours)):
            hour = h % 24
            total_cost += get_price_for_hour(periods, hour)
        if total_cost < best_cost:
            best_cost = total_cost
            best_start = start

    return best_start, best_cost


def optimize_schedule(
    appliances: list[Appliance],
    tariff: TariffResponse,
    min_start_hour: int = 0,
    max_start_hour: int = 24
) -> list[tuple[str, int, int, float]]:
    """
    Greedy schedule optimization.
    Returns list of (appliance_name, start_hour, end_hour, cost).
    """
    # Sort by priority (lower = more flexible, schedule last)
    sorted_appliances = sorted(appliances, key=lambda a: a.priority)

    schedule = []
    occupied_hours = set()

    for appliance in sorted_appliances:
        dur = appliance.duration_hours
        dur_int = int(dur)

        # Determine allowed window
        allowed_min = max(min_start_hour, appliance.must_run_hours[0] if appliance.must_run_hours else min_start_hour)
        allowed_max = min(max_start_hour, appliance.must_run_hours[-1] if appliance.must_run_hours else max_start_hour)

        if allowed_max - allowed_min < dur_int:
            allowed_min = min_start_hour
            allowed_max = max_start_hour

        # Find cheapest window in allowed range
        best_start = allowed_min
        best_cost = float('inf')

        for start in range(allowed_min, allowed_max - dur_int + 1):
            window_hours = set(range(start, start + dur_int))
            if not window_hours & occupied_hours:
                total_cost = 0.0
                for h in window_hours:
                    hour = h % 24
                    for period in tariff.periods:
                        if period.start_hour <= hour < period.end_hour:
                            total_cost += period.price_per_kwh
                            break
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_start = start

        # If no free window found, just pick cheapest
        if best_cost == float('inf'):
            best_start, best_cost = get_cheapest_window(tariff.periods, dur, min_start_hour, max_start_hour)

        end_hour = best_start + dur_int
        schedule.append((appliance.name, best_start, end_hour, round(best_cost, 4)))

        # Mark hours as occupied
        for h in range(best_start, end_hour):
            occupied_hours.add(h % 24)

    return schedule
