from fastapi import APIRouter
from models.schemas import PatternResponse
from data.lang_patterns import get_pattern

router = APIRouter(prefix="/api/v1/patterns", tags=["patterns"])


@router.get("/{lang}", response_model=PatternResponse)
async def get_language_patterns(lang: str):
    patterns = get_pattern(lang)
    return PatternResponse(
        file_structure=patterns["file_structure"],
        test_patterns=patterns["test_patterns"],
        common_pitfalls=patterns["common_pitfalls"]
    )
