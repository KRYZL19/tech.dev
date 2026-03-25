from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class PatentClaims(BaseModel):
    abstract: str
    claims: List[str]


class Patent(BaseModel):
    patent_number: str
    title: str
    filing_date: date
    issue_date: Optional[date] = None
    inventor_name: str
    assignee: str
    ipc_class: str
    claims: PatentClaims
    priority_date: Optional[date] = None
    years_since_filing: int = 0


class SearchResult(BaseModel):
    total: int
    patents: List[Patent]


class Inventor(BaseModel):
    name: str
    total_patents: int
    patents: List[Patent]


class Assignee(BaseModel):
    name: str
    total_patents: int
    patents: List[Patent]


class Classification(BaseModel):
    code: str
    description: str
    total_patents: int
    patents: List[Patent]
