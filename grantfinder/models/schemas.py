from pydantic import BaseModel, Field
from typing import Optional, List

class GrantBase(BaseModel):
    grant_id: str
    title: str
    agency: str
    cfda_number: str
    description: str
    eligibility_criteria: List[str]
    award_amount_min: int
    award_amount_max: int
    total_funding: int
    match_requirement: Optional[str] = None
    application_deadline: str
    sector: List[str]
    keywords: List[str]

class GrantSummary(BaseModel):
    grant_id: str
    title: str
    agency: str
    award_amount_min: int
    award_amount_max: int
    application_deadline: str
    sector: List[str]

class GrantDetail(GrantBase):
    pass

class EligibilityInput(BaseModel):
    organization_type: str = Field(..., description="e.g., local_government, non_profit, small_business, university, tribal, individual")
    annual_revenue: Optional[int] = Field(None, description="Annual revenue in USD")
    employees: Optional[int] = Field(None, description="Number of employees")
    sector: List[str] = Field(default_factory=list, description="e.g., broadband, energy, health, environment")

class EligibilityResult(BaseModel):
    grant_id: str
    title: str
    agency: str
    match_score: int = Field(..., description="Match score 0-100")

class AgencySummary(BaseModel):
    agency: str
    total_grants: int
    sectors: List[str]

class SectorSummary(BaseModel):
    sector: str
    total_grants: int
    agencies: List[str]
