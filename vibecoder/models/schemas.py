from pydantic import BaseModel
from typing import Optional, List


class SessionStart(BaseModel):
    task: str
    language: str
    framework: Optional[str] = None
    files: List[str] = []


class SessionStartResponse(BaseModel):
    session_id: str
    context_summary: str


class SessionResume(BaseModel):
    session_id: str
    new_message: str


class SessionResumeResponse(BaseModel):
    context_window: str
    injected_context: str
    next_step: str


class ReviewDiff(BaseModel):
    session_id: str
    diff: str


class ReviewResponse(BaseModel):
    issues: List[str]
    security_concerns: List[str]
    complexity_score: float


class PatternResponse(BaseModel):
    file_structure: List[str]
    test_patterns: List[str]
    common_pitfalls: List[str]


class SessionSummaryResponse(BaseModel):
    what_was_built: str
    key_files: List[str]
    next_steps: List[str]
