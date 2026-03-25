from fastapi import APIRouter, HTTPException
from models.schemas import ReviewDiff, ReviewResponse

router = APIRouter(prefix="/api/v1/review", tags=["review"])


@router.post("/diff", response_model=ReviewResponse)
async def review_diff(data: ReviewDiff):
    issues = []
    security_concerns = []
    
    diff_lower = data.diff.lower()
    
    # Basic static analysis
    if "console.log" in diff_lower or "console.error" in diff_lower:
        issues.append("Console statements left in code")
    
    if "password" in diff_lower or "secret" in diff_lower or "api_key" in diff_lower:
        security_concerns.append("Potential credential or secret detected in code")
    
    if "eval(" in diff_lower:
        security_concerns.append("Use of eval() is a security risk")
    
    if "innerhtml" in diff_lower or "innerHTML" in diff_lower:
        security_concerns.append("innerHTML usage can lead to XSS vulnerabilities")
    
    if "sql" in diff_lower and "select" in diff_lower:
        issues.append("Potential SQL query detected - use parameterized queries")
    
    if "// todo" in diff_lower or "// fixme" in diff_lower:
        issues.append("TODO/FIXME comment found")
    
    if "try {" in diff_lower and "catch" not in diff_lower:
        issues.append("Try block without proper error handling")
    
    if "async" in diff_lower and "await" not in diff_lower:
        issues.append("Async function without await")
    
    if "==" in data.diff and "===" not in data.diff:
        issues.append("Use === instead of == for strict equality")
    
    # Complexity scoring (simple heuristic)
    lines = data.diff.split("\n")
    added_lines = [l for l in lines if l.startswith("+") and not l.startswith("+++")]
    complexity = min(10.0, len(added_lines) / 10.0)
    
    if not issues and not security_concerns:
        issues.append("No obvious issues detected")
    
    return ReviewResponse(
        issues=issues,
        security_concerns=security_concerns,
        complexity_score=round(complexity, 1)
    )
