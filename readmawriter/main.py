"""
READMEWRITER — Auto-generate README from Code Structure

Point it at a repo structure. Get a README that actually describes what the code does.
"""

import os
import time
import hashlib
from pathlib import Path
from typing import Optional
from collections import defaultdict
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from models.schemas import (
    GenerateRequest, GenerateResponse,
    SectionRequest, SectionResponse,
    TemplatesResponse, TemplateInfo,
    ValidateRequest, ValidateResponse
)
from data.readme_templates import TEMPLATES, get_template_for_type, list_templates
from routes.generate import generate_readme
from routes.sections import generate_section

# ── Rate Limiting ─────────────────────────────────────────────────────────────
# Simple in-memory rate limiter (use Redis in production)
_daily_usage: dict[str, list[int]] = defaultdict(list)  # keyed by IP or API key

FREE_DAILY = 20
DEV_MONTHLY = 14
PRO_MONTHLY = 39

def check_rate_limit(identifier: str, plan: str = "free") -> None:
    """Check and enforce rate limits."""
    now = int(time.time())
    today_start = now - (now % 86400)
    
    # Clean old entries
    _daily_usage[identifier] = [t for t in _daily_usage[identifier] if t >= today_start]
    
    limit = FREE_DAILY if plan == "free" else 99999
    if len(_daily_usage[identifier]) >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit reached. Upgrade at /pricing"
        )
    
    _daily_usage[identifier].append(now)

# ── App ────────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="READMEWRITER API",
    description="Point it at a repo structure. Get a README that actually describes what the code does.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Health ─────────────────────────────────────────────────────────────────────
@app.get("/health")
async def health():
    return {"status": "ok", "service": "readmawriter", "version": "1.0.0"}

# ── Pricing Page ───────────────────────────────────────────────────────────────
@app.get("/pricing")
async def pricing():
    return {
        "plans": [
            {"name": "Free", "price": 0, "period": "day", "limit": f"{FREE_DAILY}/day", "features": [
                "20 README generations per day",
                "5 templates",
                "Basic validation"
            ]},
            {"name": "Dev", "price": DEV_MONTHLY, "period": "month", "features": [
                "Unlimited generations",
                "5 templates",
                "Advanced validation",
                "Priority support"
            ]},
            {"name": "Pro", "price": PRO_MONTHLY, "period": "month", "features": [
                "Unlimited generations",
                "5 templates",
                "Advanced validation",
                "Priority support",
                "Custom templates",
                "API key auth"
            ]}
        ]
    }

# ── Endpoints ──────────────────────────────────────────────────────────────────

@app.post("/api/v1/generate", response_model=GenerateResponse)
async def api_generate(req: GenerateRequest, request: Request):
    """
    Generate a complete README from a file tree structure.
    
    - **file_tree**: List of file paths representing the repository structure
    - **package_json**: Optional npm package.json contents for Node.js projects
    - **pyproject_toml**: Optional pyproject.toml contents for Python projects
    - **primary_language**: Primary programming language (e.g., 'python', 'javascript')
    """
    client_id = request.headers.get("X-API-Key", request.client.host if request.client else "unknown")
    plan = "free"
    
    try:
        check_rate_limit(client_id, plan)
    except HTTPException:
        raise
    
    if not req.file_tree:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="file_tree cannot be empty"
        )
    
    result = await generate_readme(
        file_tree=req.file_tree,
        package_json=req.package_json,
        pyproject_toml=req.pyproject_toml,
        primary_language=req.primary_language,
    )
    
    return GenerateResponse(**result)


@app.post("/api/v1/section", response_model=SectionResponse)
async def api_section(req: SectionRequest):
    """
    Generate a specific section of a README.
    
    - **section_type**: Type of section (overview, installation, usage, api, contributing, etc.)
    - **file_tree**: Repository file structure for context
    - **code_snippets**: Optional code snippets to include in the section
    """
    if not req.section_type:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="section_type is required"
        )
    
    result = await generate_section(
        section_type=req.section_type,
        file_tree=req.file_tree,
        code_snippets=req.code_snippets or [],
    )
    
    return SectionResponse(**result)


@app.get("/api/v1/templates", response_model=TemplatesResponse)
async def api_templates():
    """
    Get all available README templates by project type.
    
    Returns templates for: CLI tool, REST API, Python library, Node.js package, bot/agent
    """
    templates = list_templates()
    return TemplatesResponse(templates=templates)


@app.post("/api/v1/validate", response_model=ValidateResponse)
async def api_validate(req: ValidateRequest):
    """
    Validate an existing README for completeness and consistency.
    
    - **readme_content**: The README markdown content to validate
    
    Returns missing sections, stale info, and inconsistent headings.
    """
    if not req.readme_content or not req.readme_content.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="readme_content cannot be empty"
        )
    
    content = req.readme_content.strip()
    lines = content.split("\n")
    
    missing_sections = []
    stale_info = []
    inconsistent_headings = []
    
    # Standard sections expected
    expected_sections = ["Installation", "Usage", "License"]
    content_lower = content.lower()
    
    for section in expected_sections:
        if section.lower() not in content_lower:
            missing_sections.append(section)
    
    # Check for common stale patterns
    stale_patterns = [
        ("todo", "Contains uncompleted TODO items"),
        ("fixme", "Contains unresolved FIXME items"),
        ("tbd", "Contains TBD placeholders"),
        ("[ ]", "Contains unchecked checkboxes"),
    ]
    
    for pattern, message in stale_patterns:
        if pattern in content_lower:
            stale_info.append(message)
    
    # Check heading consistency (all should be title-case or sentence-case, not mixed)
    headings = [l.strip().lstrip("#") for l in lines if l.strip().startswith("#")]
    if headings:
        title_case_count = sum(1 for h in headings if h.istitle() or h.isupper())
        sentence_case_count = sum(1 for h in headings if h and h[0].isupper() and not h.istitle())
        
        if title_case_count > 0 and sentence_case_count > 0:
            inconsistent_headings.append(
                "Mix of title-case and sentence-case headings detected"
            )
    
    return ValidateResponse(
        missing_sections=missing_sections,
        stale_info=stale_info,
        inconsistent_headings=inconsistent_headings
    )


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
