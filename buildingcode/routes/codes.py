from fastapi import APIRouter, HTTPException, Query
from models.schemas import CodeSectionResponse
from data.code_adoptions import CODE_SECTIONS

router = APIRouter(prefix="/api/v1/code", tags=["codes"])


@router.get("/{code_name}/{version}/section/{section}", response_model=CodeSectionResponse)
def get_section(code_name: str, version: str, section: str):
    """Get the text of a specific code section."""
    code_upper = code_name.upper()
    version_str = str(version)

    if code_upper not in CODE_SECTIONS:
        raise HTTPException(status_code=404, detail=f"Code '{code_name}' not found. Available: {list(CODE_SECTIONS.keys())}")

    if version_str not in CODE_SECTIONS[code_upper]:
        raise HTTPException(status_code=404, detail=f"Version '{version}' not found for {code_name}. Available: {list(CODE_SECTIONS[code_upper].keys())}")

    if section not in CODE_SECTIONS[code_upper][version_str]:
        raise HTTPException(status_code=404, detail=f"Section '{section}' not found. Available sections: {list(CODE_SECTIONS[code_upper][version_str].keys())}")

    data = CODE_SECTIONS[code_upper][version_str][section]
    return CodeSectionResponse(
        code_name=code_name,
        version=version_str,
        section_number=section,
        title=data["title"],
        code_text=data["text"],
        referenced_standards=data["standards"],
    )
