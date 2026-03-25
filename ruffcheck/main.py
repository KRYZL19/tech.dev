"""
RUFFCHECK — Code Quality Linter API
Run ESLint, Ruff, or golangci-lint without installing anything. Just POST your code.
"""

from datetime import datetime, timedelta
from pathlib import Path
import re
from typing import Optional

from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import (
    LintRequest,
    LintResponse,
    FixRequest,
    FixResponse,
    RulesResponse,
    BulkRequest,
    BulkResponse,
    Issue,
    PricingInfo,
)
from data.rulesets import RULESET_REGISTRY, RULESET_SUMMARIES

app = FastAPI(
    title="RUFFCHECK",
    description="Run ESLint, Ruff, or golangci-lint without installing anything. Just POST your code.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple in-memory rate limiting (per API key / IP)
_usage: dict[str, list[datetime]] = {}

def _check_limit(identifier: str, limit: int, window_hours: int = 24) -> None:
    """Check and update usage count."""
    now = datetime.utcnow()
    window = now - timedelta(hours=window_hours)
    if identifier in _usage:
        _usage[identifier] = [t for t in _usage[identifier] if t > window]
    else:
        _usage[identifier] = []
    if len(_usage[identifier]) >= limit:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded: {limit} requests per {window_hours}h. "
                   f"Upgrade at https://ruffcheck.dev/pricing",
        )
    _usage[identifier].append(now)


def _get_tier(authorization: Optional[str] = None, x_api_key: Optional[str] = None) -> str:
    """Determine pricing tier from auth header or API key."""
    token = authorization or x_api_key or ""
    if token.startswith("Bearer pro_") or token.startswith("pro_"):
        return "pro"
    if token.startswith("Bearer dev_") or token.startswith("dev_"):
        return "dev"
    return "free"


def _get_limit(tier: str) -> int:
    if tier == "pro":
        return 10_000_000  # effectively unlimited
    if tier == "dev":
        return 500
    return 50  # free


@app.get("/")
def root():
    return {
        "name": "RUFFCHECK",
        "hook": "Run ESLint, Ruff, or golangci-lint without installing anything. Just POST your code.",
        "version": "1.0.0",
        "docs": "/docs",
        "pricing": "/api/v1/pricing",
    }


@app.get("/api/v1/pricing")
def pricing():
    return PricingInfo(
        free={"requests_per_day": 50, "price": 0},
        dev={"requests_per_month": 500, "price": 19},
        pro={"requests_per_month": 10_000_000, "price": 59},
    )


@app.post("/api/v1/lint", response_model=LintResponse)
def lint_endpoint(
    req: LintRequest,
    authorization: Optional[str] = Header(None),
    x_api_key: Optional[str] = Header(None),
    x_forwarded_for: Optional[str] = Header(None),
):
    identifier = x_forwarded_for or authorization or x_api_key or "anonymous"
    tier = _get_tier(authorization, x_api_key)
    limit = _get_limit(tier)
    _check_limit(identifier, limit)

    language = req.language.lower()
    if language not in RULESET_REGISTRY:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language: {req.language}. Supported: {list(RULESET_REGISTRY.keys())}",
        )

    rules = RULESET_REGISTRY[language]
    issues: list[Issue] = []
    error_count = 0
    warning_count = 0

    for rule in rules:
        if req.severity_filter and rule.severity != req.severity_filter:
            continue
        for match in rule.pattern.finditer(req.code):
            line_num = req.code[: match.start()].count("\n") + 1
            col_num = match.start() - req.code[: match.start()].rfind("\n")
            issue = Issue(
                line=line_num,
                column=col_num,
                rule_id=rule.id,
                severity=rule.severity,
                message=rule.message.format(**match.groupdict()),
                fix_suggestion=rule.fix.format(**match.groupdict()) if rule.fix else None,
            )
            issues.append(issue)
            if issue.severity == "error":
                error_count += 1
            elif issue.severity == "warning":
                warning_count += 1

    issues.sort(key=lambda i: (i.line, i.column))

    return LintResponse(
        issues=issues,
        error_count=error_count,
        warning_count=warning_count,
        total_issues=len(issues),
    )


@app.post("/api/v1/fix", response_model=FixResponse)
def fix_endpoint(
    req: FixRequest,
    authorization: Optional[str] = Header(None),
    x_api_key: Optional[str] = Header(None),
    x_forwarded_for: Optional[str] = Header(None),
):
    identifier = x_forwarded_for or authorization or x_api_key or "anonymous"
    tier = _get_tier(authorization, x_api_key)
    _check_limit(identifier, _get_limit(tier))

    language = req.language.lower()
    if language not in RULESET_REGISTRY:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language: {req.language}. Supported: {list(RULESET_REGISTRY.keys())}",
        )

    rules = RULESET_REGISTRY[language]
    fixed_code = req.code
    changes_made: list[str] = []
    original_issues_resolved = 0

    for rule in rules:
        if not rule.fix:
            continue
        for match in rule.pattern.finditer(fixed_code):
            replacement = rule.fix.format(**match.groupdict())
            if replacement != match.group(0):
                fixed_code = fixed_code[: match.start()] + replacement + fixed_code[match.end() :]
                changes_made.append(f"{rule.id}: replaced '{match.group(0)}' with '{replacement}'")
                original_issues_resolved += 1

    return FixResponse(
        fixed_code=fixed_code,
        changes_made=changes_made,
        original_issues_resolved=original_issues_resolved,
    )


@app.get("/api/v1/rules/{language}", response_model=RulesResponse)
def rules_endpoint(language: str):
    lang = language.lower()
    if lang not in RULESET_REGISTRY:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language: {lang}. Supported: {list(RULESET_REGISTRY.keys())}",
        )
    rules = RULESET_REGISTRY[lang]
    return RulesResponse(
        language=lang,
        summary=RULESET_SUMMARIES.get(lang, ""),
        rule_count=len(rules),
        rules=[
            {
                "id": r.id,
                "severity": r.severity,
                "description": r.description,
                "fixable": r.fix is not None,
            }
            for r in rules
        ],
    )


@app.post("/api/v1/bulk", response_model=BulkResponse)
def bulk_endpoint(
    req: BulkRequest,
    authorization: Optional[str] = Header(None),
    x_api_key: Optional[str] = Header(None),
    x_forwarded_for: Optional[str] = Header(None),
):
    identifier = x_forwarded_for or authorization or x_api_key or "anonymous"
    tier = _get_tier(authorization, x_api_key)
    _check_limit(identifier, _get_limit(tier))

    results = []
    for file_entry in req.files:
        lang = file_entry.language.lower()
        if lang not in RULESET_REGISTRY:
            results.append(
                {
                    "file": file_entry.name,
                    "language": file_entry.language,
                    "issues": [],
                    "summary": f"Unsupported language: {file_entry.language}",
                }
            )
            continue

        rules = RULESET_REGISTRY[lang]
        issues: list[Issue] = []
        error_count = 0
        warning_count = 0

        for rule in rules:
            for match in rule.pattern.finditer(file_entry.content):
                line_num = file_entry.content[: match.start()].count("\n") + 1
                col_num = match.start() - file_entry.content[: match.start()].rfind("\n")
                issue = Issue(
                    line=line_num,
                    column=col_num,
                    rule_id=rule.id,
                    severity=rule.severity,
                    message=rule.message.format(**match.groupdict()),
                    fix_suggestion=rule.fix.format(**match.groupdict()) if rule.fix else None,
                )
                issues.append(issue)
                if issue.severity == "error":
                    error_count += 1
                elif issue.severity == "warning":
                    warning_count += 1

        issues.sort(key=lambda i: (i.line, i.column))
        results.append(
            {
                "file": file_entry.name,
                "language": lang,
                "issues": issues,
                "summary": f"{len(issues)} issues ({error_count} errors, {warning_count} warnings)",
            }
        )

    return BulkResponse(results=results)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
