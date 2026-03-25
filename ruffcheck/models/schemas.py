"""
Pydantic schemas for RUFFCHECK API.
"""

from typing import Optional, Literal
from pydantic import BaseModel, Field


class Issue(BaseModel):
    line: int
    column: int
    rule_id: str
    severity: Literal["error", "warning", "info"]
    message: str
    fix_suggestion: Optional[str] = None


class LintRequest(BaseModel):
    code: str = Field(..., min_length=1, max_length=100_000)
    language: str = Field(..., description="Language: python, javascript, typescript, go, rust")
    severity_filter: Optional[Literal["error", "warning", "info"]] = Field(
        default=None, description="Filter issues by severity"
    )


class LintResponse(BaseModel):
    issues: list[Issue]
    error_count: int
    warning_count: int
    total_issues: int


class FixRequest(BaseModel):
    code: str = Field(..., min_length=1, max_length=100_000)
    language: str = Field(..., description="Language: python, javascript, typescript, go, rust")


class FixResponse(BaseModel):
    fixed_code: str
    changes_made: list[str]
    original_issues_resolved: int


class RuleInfo(BaseModel):
    id: str
    severity: str
    description: str
    fixable: bool


class RulesResponse(BaseModel):
    language: str
    summary: str
    rule_count: int
    rules: list[RuleInfo]


class BulkFile(BaseModel):
    name: str
    content: str
    language: str


class BulkRequest(BaseModel):
    files: list[BulkFile] = Field(..., min_length=1, max_length=100)


class BulkResultEntry(BaseModel):
    file: str
    language: str
    issues: list[Issue]
    summary: str


class BulkResponse(BaseModel):
    results: list[BulkResultEntry]


class PricingTier(BaseModel):
    requests_per_day: Optional[int] = None
    requests_per_month: Optional[int] = None
    price: int


class PricingInfo(BaseModel):
    free: PricingTier
    dev: PricingTier
    pro: PricingTier
