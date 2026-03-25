"""Vessel endpoints."""

from datetime import date
from fastapi import APIRouter, HTTPException, Response
from models.schemas import (
    VesselResponse,
    VesselDetailResponse,
    VesselHistoryResponse,
    OwnerRecord,
)
from data.vessel_index import VESSEL_BY_ID, VESSELS

router = APIRouter(prefix="/api/v1/vessel", tags=["vessel"])


@router.get("/{vessel_id}", response_model=VesselResponse)
def get_vessel(vessel_id: str, response: Response):
    """Get vessel details by vessel_id.

    Returns length_ft, beam_ft, hull_material, year, manufacturer,
    model, propulsion, documentation_number, lien_status, and lien_holder.
    """
    vessel = VESSEL_BY_ID.get(vessel_id)
    if not vessel:
        raise HTTPException(status_code=404, detail="Vessel not found")

    return VesselResponse(
        vessel_id=vessel.vessel_id,
        documentation_number=vessel.documentation_number,
        name=vessel.name,
        manufacturer=vessel.manufacturer,
        model=vessel.model,
        year=vessel.year,
        length_ft=vessel.length_ft,
        beam_ft=vessel.beam_ft,
        hull_material=vessel.hull_material,
        propulsion=vessel.propulsion,
        vessel_type=vessel.vessel_type,
        status=vessel.status,
        lien_status=vessel.lien_status,
        lien_holder=vessel.lien_holder,
    )


@router.get("/{vessel_id}/history", response_model=VesselHistoryResponse)
def get_vessel_history(vessel_id: str, response: Response):
    """Get owner history, previous owners, dates of change, and lien status."""
    vessel = VESSEL_BY_ID.get(vessel_id)
    if not vessel:
        raise HTTPException(status_code=404, detail="Vessel not found")

    owner_records = [
        OwnerRecord(
            name=o.name,
            city=o.city,
            state=o.state,
            purchase_date=o.purchase_date,
            purchase_price=o.purchase_price,
        )
        for o in vessel.owners
    ]

    current = owner_records[-1] if owner_records else None

    return VesselHistoryResponse(
        vessel_id=vessel.vessel_id,
        documentation_number=vessel.documentation_number,
        vessel_name=vessel.name,
        status=vessel.status,
        lien_status=vessel.lien_status,
        lien_holder=vessel.lien_holder,
        owner_history=owner_records,
        previous_owners_count=len(owner_records) - 1 if len(owner_records) > 0 else 0,
        current_owner=current,
    )
