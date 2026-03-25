from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from models.schemas import IncidentSummary, IncidentDetail, SearchResult
from data.incident_index import search_incidents, get_by_id, get_by_type

router = APIRouter(prefix="/api/v1", tags=["incidents"])


@router.get("/incidents/search", response_model=list[SearchResult])
def search_incidents_endpoint(
    airport_code: str = Query(..., description="ICAO airport code"),
    radius_mi: Optional[float] = Query(None, description="Search radius in miles"),
    year: Optional[int] = Query(None, description="Filter by year"),
):
    """Search incidents near an airport, optionally within a radius and/or year."""
    results = search_incidents(airport_code=airport_code, radius_mi=radius_mi, year=year)
    return [
        SearchResult(
            report_id=r["report_id"],
            date=r["date"],
            aircraft_type=r["aircraft_type"],
            incident_type=r["incident_type"],
            airport_code=r.get("airport_code"),
        )
        for r in results
    ]


@router.get("/incident/{report_id}", response_model=IncidentDetail)
def get_incident(report_id: str):
    """Get full detail of a single incident by report ID."""
    r = get_by_id(report_id)
    if r is None:
        raise HTTPException(status_code=404, detail=f"Report '{report_id}' not found")
    return IncidentDetail(**r)


@router.get("/incidents/type/{incident_type}", response_model=list[IncidentSummary])
def incidents_by_type(incident_type: str):
    """Filter incidents by type: laser, wildlife, operational_incident, near_mid."""
    valid = {"laser", "wildlife", "operational_incident", "near_mid"}
    if incident_type not in valid:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid incident_type. Must be one of: {', '.join(sorted(valid))}",
        )
    results = get_by_type(incident_type)
    return [
        IncidentSummary(
            report_id=r["report_id"],
            date=r["date"],
            aircraft_type=r["aircraft_type"],
            incident_type=r["incident_type"],
            airport_code=r.get("airport_code"),
        )
        for r in results
    ]
