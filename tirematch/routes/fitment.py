"""Fitment routes for TIREMATCH API."""

from fastapi import APIRouter, HTTPException, Path
from typing import Literal

from data.vehicle_data import get_vehicle, VEHICLES
from models.schemas import (
    VehicleResponse, FactoryTireSize, VehicleWheelSpec,
    TireCompareRequest, TireCompareResponse,
    WheelFitmentRequest, WheelFitmentResponse,
)
from routes.sizing_utils import parse_tire_size, tire_dimensions, compare_tires, FIT_THRESHOLD_PCT

router = APIRouter(prefix="/api/v1", tags=["fitment"])


def _build_vehicle_response(vehicle: dict) -> VehicleResponse:
    """Convert a raw vehicle dict into a VehicleResponse."""
    factory_tires = []
    for ft in vehicle["factory_tires"]:
        dims = tire_dimensions(ft["width_mm"], ft["aspect_ratio"], ft["rim_diameter"])
        factory_tires.append(FactoryTireSize(
            width_mm=ft["width_mm"],
            aspect_ratio=ft["aspect_ratio"],
            rim_diameter=ft["rim_diameter"],
            sidewall_inches=dims["sidewall_inches"],
            diameter_inches=dims["diameter_inches"],
        ))

    return VehicleResponse(
        id=vehicle["id"],
        year=vehicle["year"],
        make=vehicle["make"],
        model=vehicle["model"],
        trims=vehicle["trims"],
        factory_tires=factory_tires,
        wheel_spec=VehicleWheelSpec(
            bolt_pattern=vehicle["bolt_pattern"],
            center_bore_mm=vehicle["center_bore_mm"],
            offset_range_mm=vehicle["offset_range_mm"],
            lug_thread=vehicle["lug_thread"],
        ),
        tire_count=4,
    )


@router.get("/vehicle/{year}/{make}/{model}", response_model=VehicleResponse)
def get_vehicle_info(
    year: int = Path(..., ge=1900, le=2030),
    make: str = Path(..., min_length=1),
    model: str = Path(..., min_length=1),
):
    """
    Get factory tire sizes and wheel specs for a vehicle.

    Example: GET /api/v1/vehicle/2016/honda/civic
    """
    vehicle = get_vehicle(year, make.lower(), model.lower())
    if not vehicle:
        available = [
            f"{v['year']} {v['make']} {v['model']}"
            for v in VEHICLES.values()
        ]
        raise HTTPException(
            status_code=404,
            detail={
                "message": f"No data for {year} {make} {model}",
                "available_models": sorted(set(available))[:20],
                "error_code": "VEHICLE_NOT_FOUND",
            }
        )
    return _build_vehicle_response(vehicle)


@router.post("/tire/compare", response_model=TireCompareResponse)
def compare_tires_endpoint(req: TireCompareRequest):
    """
    Compare two tire sizes.

    Input: tire1_size, tire2_size (format: 245/45R18)
    Output: diameter_diff_pct, will_fit, speedo_diff_mph, verdict
    """
    try:
        result = compare_tires(req.tire1_size, req.tire2_size)
        return TireCompareResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=422, detail={"message": str(e), "error_code": "INVALID_TIRE_SIZE"})


@router.post("/wheel/fitment", response_model=WheelFitmentResponse)
def wheel_fitment(req: WheelFitmentRequest):
    """
    Check if a wheel size and offset fits a vehicle.

    Input: vehicle_id, wheel_size, offset_mm
    Output: fitment_verdict, clearance_risk, spacer_needed_mm
    """
    vehicle = VEHICLES.get(req.vehicle_id)
    if not vehicle:
        raise HTTPException(
            status_code=404,
            detail={
                "message": f"Vehicle ID '{req.vehicle_id}' not found",
                "available_ids": list(VEHICLES.keys()),
                "error_code": "VEHICLE_NOT_FOUND",
            }
        )

    offset_min = vehicle["offset_range_mm"]["min"]
    offset_max = vehicle["offset_range_mm"]["max"]
    offset = req.offset_mm

    warnings = []
    spacer_needed = 0.0

    if offset < offset_min:
        # Wheel is tucked in too far — needs spacer to push out
        spacer_needed = round(offset_min - offset, 1)
        if spacer_needed > 15:
            fitment_verdict: Literal["fits", "fits_with_spacer", "rubbing_likely", "does_not_fit"] = "rubbing_likely"
            clearance_risk: Literal["none", "low", "medium", "high"] = "high"
            warnings.append(f"Offset {offset}mm is too aggressive — wheel will rub on suspension components.")
        else:
            fitment_verdict = "fits_with_spacer"
            clearance_risk = "medium"
            warnings.append(f"Spacer of {spacer_needed}mm recommended for proper fitment.")
    elif offset > offset_max:
        # Wheel sticks out too far — rubbing on fender
        fitment_verdict = "rubbing_likely"
        clearance_risk = "high"
        warnings.append(f"Offset {offset}mm is too aggressive — wheel will rub on fender/flare.")
    else:
        fitment_verdict = "fits"
        clearance_risk = "none"

    # Rim size sanity check — factory rim sizes
    factory_rims = [t["rim_diameter"] for t in vehicle["factory_tires"]]
    if req.wheel_size not in factory_rims:
        if abs(req.wheel_size - max(factory_rims)) <= 2:
            warnings.append(f"Non-factory rim size {req.wheel_size}\" — verify brake caliper clearance.")
            if clearance_risk == "none":
                clearance_risk = "low"
        else:
            warnings.append(f"Rim size {req.wheel_size}\" not commonly used on this vehicle — verify fitment.")
            if clearance_risk == "none":
                clearance_risk = "medium"

    return WheelFitmentResponse(
        vehicle_id=req.vehicle_id,
        wheel_size=req.wheel_size,
        offset_mm=req.offset_mm,
        fitment_verdict=fitment_verdict,
        clearance_risk=clearance_risk,
        spacer_needed_mm=spacer_needed,
        warnings=warnings,
    )
