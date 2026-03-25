from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class AdverseEvent(BaseModel):
    term: str
    serious: bool
    participants: int
    percentage: float


class ResultMetric(BaseModel):
    metric: str
    value: str
    group: Optional[str] = None


class TrialDesign(BaseModel):
    allocation: str
    intervention_model: str
    masking: str
    primary_purpose: str
    arms: List[str]


class Trial(BaseModel):
    nct_id: str
    title: str
    condition: str
    drug: str
    sponsor: str
    phase: str
    status: str
    results_submitted: bool
    enrollment: int
    start_date: date
    completion_date: Optional[date]
    brief_summary: str
    eligibility_criteria: str
    design_info: TrialDesign
    results: List[ResultMetric]
    serious_adverse_events: List[AdverseEvent]
    location_country: str
    location_state: Optional[str]
    location_city: Optional[str]
    success: Optional[bool]


class TrialSearchResult(BaseModel):
    total: int
    trials: List[Trial]


class SponsorStats(BaseModel):
    sponsor: str
    total_trials: int
    success_rate: float
    trials: List[Trial]
