from fastapi import APIRouter, Query
from typing import Optional
from models.schemas import TrialSearchResult, Trial
from data.trial_index import TRIALS, DRUG_INDEX, SPONSOR_INDEX, LOCATION_INDEX
from models.schemas import SponsorStats

router = APIRouter(prefix="/api/v1", tags=["search"])

@router.get("/search", response_model=TrialSearchResult)
def search_trials(
    condition: Optional[str] = Query(None, description="Condition to search for"),
    phase: Optional[int] = Query(None, description="Trial phase (1, 2, 3, or 4)"),
    status: Optional[str] = Query(None, description="Trial status (COMPLETED, RECRUITING, etc.)"),
    results: Optional[bool] = Query(None, description="Only trials with results submitted"),
    limit: Optional[int] = Query(20, description="Maximum number of results")
):
    filtered = TRIALS.copy()
    
    if condition:
        filtered = [t for t in filtered if condition.lower() in t.condition.lower()]
    
    if phase:
        filtered = [t for t in filtered if str(phase) in t.phase]
    
    if status:
        filtered = [t for t in filtered if t.status == status.upper()]
    
    if results is not None:
        filtered = [t for t in filtered if t.results_submitted == results]
    
    return TrialSearchResult(total=len(filtered), trials=filtered[:limit])

@router.get("/drug/{drug_name}/trials", response_model=list[Trial])
def get_drug_trials(drug_name: str):
    trials = DRUG_INDEX.get(drug_name.lower(), [])
    return trials

@router.get("/sponsor/{sponsor_name}", response_model=SponsorStats)
def get_sponsor_trials(sponsor_name: str):
    trials = SPONSOR_INDEX.get(sponsor_name, [])
    completed = [t for t in trials if t.status == "COMPLETED"]
    successful = [t for t in completed if t.success is True]
    
    success_rate = len(successful) / len(completed) if completed else 0.0
    
    return SponsorStats(
        sponsor=sponsor_name,
        total_trials=len(trials),
        success_rate=round(success_rate, 3),
        trials=trials
    )

@router.get("/location", response_model=list[Trial])
def get_location_trials(
    country: str = Query(..., description="Country name"),
    state: Optional[str] = Query(None, description="State/Province")
):
    if state:
        return LOCATION_INDEX.get((country, state), [])
    else:
        results = []
        for (c, s), trials in LOCATION_INDEX.items():
            if c == country:
                results.extend(trials)
        return results
