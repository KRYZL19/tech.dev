from fastapi import APIRouter, HTTPException
from models.schemas import ADARequirementsResponse, PermitChecklistRequest, PermitChecklistResponse
from data.code_adoptions import ADA_REQUIREMENTS, get_permit_checklist

router = APIRouter(prefix="/api/v1", tags=["permits", "ada"])


@router.post("/permit/checklist", response_model=PermitChecklistResponse)
def get_permit_checklist_endpoint(req: PermitChecklistRequest):
    """Get the required permits, inspections, and setbacks for a project."""
    valid_types = ["commercial", "residential", "addition", "alteration"]
    if req.project_type.lower() not in valid_types:
        raise HTTPException(status_code=400, detail=f"Invalid project_type. Must be one of: {valid_types}")

    result = get_permit_checklist(req.city, req.project_type.lower(), req.sqft)
    return PermitChecklistResponse(
        city=req.city,
        project_type=req.project_type,
        sqft=req.sqft,
        required_permits=result["required_permits"],
        inspections=result["inspections"],
        setbacks=result["setbacks"],
    )


@router.get("/ada/requirements/{building_type}", response_model=ADARequirementsResponse)
def get_ada_requirements(building_type: str):
    """Get ADA requirements for an occupancy type (e.g., A-1, B, I-2, R-2)."""
    bt = building_type.upper()
    if bt not in ADA_REQUIREMENTS:
        raise HTTPException(status_code=404, detail=f"Occupancy type '{building_type}' not found. Available: {list(ADA_REQUIREMENTS.keys())}")

    data = ADA_REQUIREMENTS[bt]
    return ADARequirementsResponse(
        occupancy_type=bt,
        name=data["name"],
        accessible_rooms=data["accessible_rooms"],
        seating=data["seating"],
        toilet_rooms=data[" toilet_rooms"],
        drinking_fountains=data["drinking_fountains"],
    )
