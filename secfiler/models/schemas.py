from pydantic import BaseModel, Field
from typing import Optional


class FilingBase(BaseModel):
    cik: str
    ticker: str
    company_name: str
    form_type: str
    filing_date: str
    accession: str
    description: str
    sector: str


class Filing(FilingBase):
    link_to_html: str


class FilingSearchResult(BaseModel):
    total: int
    results: list[Filing]


class InsiderTransaction(BaseModel):
    insider_name: str
    insider_title: Optional[str]
    transaction_type: str
    shares: int
    price_per_share: float
    filing_date: str
    ticker: str
    company_name: str


class InsiderResponse(BaseModel):
    ticker: str
    company_name: str
    total_transactions: int
    transactions: list[InsiderTransaction]


class AlertCreateRequest(BaseModel):
    keywords: list[str] = Field(default_factory=list)
    form_types: list[str] = Field(default_factory=list)
    sector: Optional[str] = None
    description: Optional[str] = None


class AlertResponse(BaseModel):
    alert_id: str
    keywords: list[str]
    form_types: list[str]
    sector: Optional[str]
    description: Optional[str]
    created_at: str


class TodayFilingsResponse(BaseModel):
    date: str
    form_4_count: int
    eight_k_count: int
    filings: list[Filing]
