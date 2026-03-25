"""Calls data = {}ign lookup routes."""
from fastapi import APIRouter, HTTPException
from data.callsign_data import CALLSIGNS
from data.freq_bands import BANDS, LICENSE_CLASSES
from models.schemas import CallsignDetail

router = APIRouter(prefix="/api/v1", tags=["callsign"])


@router.get("/callsign/{callsign}", response_model=CallsignDetail)
async def get_callsign(callsign: str):
    """Look up a callsign and return license details."""
    cs = callsign.upper()
    record = next((c for c in CALLSIGNS if c["callsign"] == cs), None)

    if not record:
        raise HTTPException(status_code=404, detail=f"Callsign {cs} not found in database")

    # Build privileges based on license class
    privileges = []
    cls = record["class"]
    if cls in LICENSE_CLASSES:
        cls_idx = LICENSE_CLASSES.index(cls)
        for band_key, band_data in BANDS.items():
            privs = band_data["allocations"]["usa"]["privileges"].get(cls, [])
            if privs:
                privileges.append(f"{band_data['name']}: {', '.join(privs)}")

    return CallsignDetail(
        callsign=record["callsign"],
        frn=record["frn"],
        licensee=record["licensee"],
        status=record["status"],
        class_=record["class"],
        expired=record["expired"],
        grid=record["grid"],
        address=record["address"],
        privileges=privileges,
    )


@router.get("/callsign/{callsign}/exists")
async def check_callsign(callsign: str):
    """Check if a callsign exists in the database."""
    cs = callsign.upper()
    record = next((c for c in CALLSIGNS if c["callsign"] == cs), None)
    return {"callsign": cs, "exists": record is not None}
