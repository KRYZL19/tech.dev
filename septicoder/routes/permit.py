from fastapi import APIRouter, HTTPException
from models.schemas import PermitChecklistInput, PermitChecklistOutput
from data.soil_data import COUNTY_DATA, STATE_SETBACKS

router = APIRouter(prefix="/api/v1/permit", tags=["permit"])


@router.get("/soil/{county_name}")
async def get_soil_data(county_name: str):
    """
    Get soil data for a specific county.

    Returns soil types, percolation rates, groundwater risk, and notes.
    """
    from data.soil_data import get_county_soil

    data = get_county_soil(county_name)
    if not data:
        available = list(COUNTY_DATA.keys())
        raise HTTPException(
            status_code=404,
            detail=f"County '{county_name}' not found. Available: {', '.join(available)}"
        )
    return data


@router.post("/checklist", response_model=PermitChecklistOutput)
async def get_permit_checklist(input_data: PermitChecklistInput):
    """
    Generate a permit checklist for a septic system installation.

    - **state**: Two-letter state code (CA, TX, FL, NC, WA)
    - **county**: County name
    - **system_type**: conventional, chambered, drip, mound, at-grade, aerobic
    - **bedrooms**: Number of bedrooms
    """
    state = input_data.state.upper()
    county = input_data.county.lower()

    if state not in STATE_SETBACKS:
        raise HTTPException(
            status_code=400,
            detail=f"State '{state}' not supported. Available: {', '.join(STATE_SETBACKS.keys())}"
        )

    setbacks = STATE_SETBACKS[state]
    required_permits = []
    required_inspections = []
    fees_estimate = ""
    timeline = ""
    notes = []

    # State-specific permit requirements
    if state == "CA":
        required_permits = [
            "Septic System Permit (County Environmental Health)",
            "Building Permit (if structure involved)",
            "Encroachment Permit (if utility crossing)",
            "Notice of Intent (NOI) for construction stormwater permit",
        ]
        required_inspections = [
            "Percolation Test",
            "Excavation Inspection",
            "Drainfield/ Leach Field Inspection",
            "Tank Installation Inspection",
            "Final Plumbing Inspection",
            "Pressure Test (for drip systems)",
        ]
        fees_estimate = "$500 - $2,500 depending on county"
        timeline = "4-8 weeks for permit approval"
        notes.append("California requires percolation test by certified tester.")
        notes.append("Coastal counties may need Coastal Commission review.")

    elif state == "TX":
        required_permits = [
            "TCEQ OSSF (On-Site Sewage Facility) Permit",
            "Septic Tank Installation Permit",
            "Landowner Authorization (if applicable)",
        ]
        required_inspections = [
            "Site Evaluation/Percolation Test",
            "Trench Bottom Inspection",
            "Tank Installation Inspection",
            "Final System Inspection",
        ]
        fees_estimate = "$300 - $1,500 depending on county"
        timeline = "2-6 weeks for permit approval"
        notes.append("Texas requires 150ft setback from water supply wells.")
        notes.append("Edwards Aquifer zones have additional requirements.")

    elif state == "FL":
        required_permits = [
            "Septic System Permit (County Health Department)",
            "Building Permit",
            "Environmental Resource Permit (ERP) if applicable",
        ]
        required_inspections = [
            "Site Inspection",
            "Percolation Test",
            "Footing Inspection",
            "Tank Installation",
            "Drainfield Final Inspection",
        ]
        fees_estimate = "$400 - $1,800 depending on county"
        timeline = "3-6 weeks for permit approval"
        notes.append("Florida: High water table areas require mound or fill systems.")
        notes.append("Some counties require additional setbacks from coastal waters.")

    elif state == "NC":
        required_permits = [
            "Septic Permit (County Environmental Health)",
            "Building Permit",
            "Water Supply Well Permit (if new well)",
        ]
        required_inspections = [
            "Site Evaluation",
            "Percolation Test",
            "Tank Installation",
            "Drainfield Installation",
            "Final Inspection",
        ]
        fees_estimate = "$300 - $1,200 depending on county"
        timeline = "3-5 weeks for permit approval"
        notes.append("North Carolina requires 30ft setback from property lines.")
        notes.append("Mountains region may have additional slope requirements.")

    elif state == "WA":
        required_permits = [
            "Septic System Permit (County Public Health)",
            "Building Permit",
            "Electrical Permit (for pumps/aerobics)",
        ]
        required_inspections = [
            "Site Evaluation/Percolation Test",
            "Excavation Inspection",
            "Tank Installation",
            "Drainfield Installation",
            "Final Inspection",
        ]
        fees_estimate = "$400 - $1,500 depending on county"
        timeline = "3-6 weeks for permit approval"
        notes.append("Washington: High rainfall affects system sizing (add 20% for wet season).")
        notes.append("Critical areas may require additional review.")

    # System type specific notes
    system_type = input_data.system_type.lower()
    if system_type in ["mound", "at-grade"]:
        notes.append(f"{system_type.title()} systems typically require additional engineering and may need larger setbacks.")
    elif system_type == "aerobic":
        notes.append("Aerobic systems require additional permitting and regular maintenance contracts.")
    elif system_type == "drip":
        notes.append("Drip systems require pressure testing and additional filtration inspection.")

    # Bedroom-specific sizing note
    if input_data.bedrooms >= 4:
        notes.append(f"{input_data.bedrooms}-bedroom systems may require advanced treatment unit for some counties.")

    return PermitChecklistOutput(
        state=state,
        county=county,
        system_type=system_type,
        required_permits=required_permits,
        required_inspections=required_inspections,
        setbacks=setbacks,
        fees_estimate=fees_estimate,
        timeline=timeline,
        notes=notes,
    )
