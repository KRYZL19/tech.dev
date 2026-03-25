from fastapi import APIRouter, HTTPException, Path
from models.schemas import Patent, Inventor, Assignee, Classification
from data.patent_index import (
    get_patent_by_number,
    get_patents_by_inventor,
    get_patents_by_assignee,
    get_patents_by_classification,
    IPC_CODES,
)

router = APIRouter(prefix="/api/v1", tags=["patent"])


@router.get("/patent/{patent_number}", response_model=Patent)
def get_patent(patent_number: str = Path(..., description="US Patent number (e.g. US10443521B1)")):
    """Retrieve full details for a specific patent by patent number."""
    patent = get_patent_by_number(patent_number)
    if not patent:
        raise HTTPException(status_code=404, detail=f"Patent {patent_number} not found")
    return patent


@router.get("/inventor/{inventor_name}", response_model=Inventor)
def get_inventor(
    inventor_name: str = Path(..., description="Inventor name (partial match supported, e.g. Smith)"),
):
    """Find all patents attributed to a specific inventor."""
    patents = get_patents_by_inventor(inventor_name)
    if not patents:
        raise HTTPException(status_code=404, detail=f"No patents found for inventor matching '{inventor_name}'")
    return Inventor(
        name=patents[0].inventor_name,
        total_patents=len(patents),
        patents=patents,
    )


@router.get("/assignee/{assignee_name}", response_model=Assignee)
def get_assignee(
    assignee_name: str = Path(..., description="Company or entity name (partial match supported, e.g. Intel)"),
):
    """Find all patents assigned to a specific company or entity."""
    patents = get_patents_by_assignee(assignee_name)
    if not patents:
        raise HTTPException(status_code=404, detail=f"No patents found for assignee matching '{assignee_name}'")
    return Assignee(
        name=patents[0].assignee,
        total_patents=len(patents),
        patents=patents,
    )


@router.get("/classification/{IPC_code}", response_model=Classification)
def get_classification(
    IPC_code: str = Path(..., description="IPC classification code (e.g. H01L, G06N, A61K)"),
):
    """Find all patents in a specific IPC technical classification."""
    patents = get_patents_by_classification(IPC_code)
    if not patents:
        raise HTTPException(status_code=404, detail=f"No patents found for IPC classification '{IPC_code}'")
    description = IPC_CODES.get(IPC_code, "Unknown classification")
    return Classification(
        code=IPC_code,
        description=description,
        total_patents=len(patents),
        patents=patents,
    )
