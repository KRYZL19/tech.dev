"""Registration & manufacturer endpoints."""

from fastapi import APIRouter, HTTPException
from models.schemas import ValidateRequest, ValidateResponse, ManufacturerResponse, VesselResponse
from data.vessel_index import VESSEL_BY_ID, DOC_NUM_TO_VESSEL, get_by_manufacturer, get_all_manufacturers

router = APIRouter(prefix="/api/v1", tags=["registration"])


@router.post("/vessel/validate", response_model=ValidateResponse)
def validate_vessel(payload: ValidateRequest):
    """Validate a documentation_number and return vessel_id, status, and lien info."""
    doc_num = payload.documentation_number.strip()
    vessel = DOC_NUM_TO_VESSEL.get(doc_num)

    if not vessel:
        return ValidateResponse(
            valid=False,
            documentation_number=doc_num,
            vessel_id=None,
            vessel_name=None,
            status="not_found",
            lien_status=None,
        )

    return ValidateResponse(
        valid=True,
        documentation_number=vessel.documentation_number,
        vessel_id=vessel.vessel_id,
        vessel_name=vessel.name,
        status=vessel.status,
        lien_status=vessel.lien_status,
    )


@router.get("/manufacturer/{mfr}", response_model=ManufacturerResponse)
def get_by_manufacturer_endpoint(mfr: str):
    """List all vessels by manufacturer with common models."""
    all_mfrs = get_all_manufacturers()
    key = mfr.lower().replace(" ", "_")

    if key not in all_mfrs:
        raise HTTPException(
            status_code=404,
            detail=f"Manufacturer '{mfr}' not found. "
                   f"Available: {', '.join(sorted(all_mfrs.keys()))}"
        )

    mfr_info = all_mfrs[key]
    vessels = get_by_manufacturer(key)

    vessel_responses = [
        VesselResponse(
            vessel_id=v.vessel_id,
            documentation_number=v.documentation_number,
            name=v.name,
            manufacturer=v.manufacturer,
            model=v.model,
            year=v.year,
            length_ft=v.length_ft,
            beam_ft=v.beam_ft,
            hull_material=v.hull_material,
            propulsion=v.propulsion,
            vessel_type=v.vessel_type,
            status=v.status,
            lien_status=v.lien_status,
            lien_holder=v.lien_holder,
        )
        for v in vessels
    ]

    return ManufacturerResponse(
        manufacturer=key,
        manufacturer_display=mfr_info["name"],
        total_vessels=len(vessels),
        models=mfr_info["models"],
        vessels=vessel_responses,
    )


@router.get("/manufacturer")
def list_manufacturers():
    """List all available manufacturers."""
    all_mfrs = get_all_manufacturers()
    return {
        "count": len(all_mfrs),
        "manufacturers": {
            key: {
                "name": info["name"],
                "models": info["models"],
                "vessel_count": len(get_by_manufacturer(key)),
            }
            for key, info in all_mfrs.items()
        },
    }
