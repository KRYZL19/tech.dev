from fastapi import APIRouter, Query
from typing import Optional
from models.schemas import SearchResult
from data.patent_index import search_patents

router = APIRouter(prefix="/api/v1", tags=["search"])


@router.get("/search", response_model=SearchResult)
def search(
    q: Optional[str] = Query(None, description="Technical query string to search patent titles, abstracts, claims, inventors, and assignees"),
    class_filter: Optional[str] = Query(None, alias="class", description="IPC classification code (e.g. H01L, G06N)"),
    year_start: Optional[int] = Query(None, description="Filter patents filed on or after this year"),
    year_end: Optional[int] = Query(None, description="Filter patents filed on or before this year"),
    limit: int = Query(50, ge=1, le=500, description="Maximum number of results to return"),
):
    """
    Search patents by technical claim, keyword, classification, or date range.

    Supports full-text search across titles, abstracts, claims, inventor names,
    and assignee names — not just keyword matching.
    """
    total, patents = search_patents(
        query=q,
        ipc_class=class_filter,
        year_start=year_start,
        year_end=year_end,
        limit=limit,
    )
    return SearchResult(total=total, patents=patents)
