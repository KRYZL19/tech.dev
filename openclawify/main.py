"""
OpenClawify — OpenClaw Skill Generator

Describe your workflow in plain English. Get a working OpenClaw skill.

Usage:
    pip install -r requirements.txt
    uvicorn main:app --reload --port 8000

Endpoints:
    POST /api/v1/skill/generate     - Generate a skill from workflow description
    POST /api/v1/skill/validate     - Validate SKILL.md YAML content
    GET  /api/v1/templates          - List available skill templates
    POST /api/v1/skill/expand       - Expand an existing skill with new capabilities
    POST /api/v1/skill/deploy-checklist - Get deployment checklist for a skill
"""

import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import (
    GenerateRequest, GenerateResponse,
    ValidateRequest, ValidateResponse,
    TemplatesResponse, TemplateInfo,
    ExpandRequest, ExpandResponse,
    DeployChecklistResponse,
)
from routes.generate import router as generate_router
from routes.validate import router as validate_router
from data.skill_templates import list_templates, get_template

app = FastAPI(
    title="OpenClawify",
    description="Describe your workflow in plain English. Get a working OpenClaw skill.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate_router)
app.include_router(validate_router)


# ─── /api/v1/templates ─────────────────────────────────────────────────────────

@app.get("/api/v1/templates", response_model=TemplatesResponse, tags=["templates"])
def get_templates():
    """List all available skill templates."""
    templates = list_templates()
    return TemplatesResponse(templates=[
        TemplateInfo(**t) for t in templates
    ])


# ─── /api/v1/skill/expand ──────────────────────────────────────────────────────

COMMON_CAPABILITIES = {
    "discord notifications": (
        "## Additional Capability: Discord Notifications\n"
        "After completing the main workflow, send a formatted summary to Discord:\n"
        "1. Format results as an embed with color, title, and description\n"
        "2. Send via Discord webhook URL stored in config\n"
        "3. Include timestamp and status emoji\n"
    ),
    "slack notifications": (
        "## Additional Capability: Slack Notifications\n"
        "After completing the main workflow, post a summary to Slack:\n"
        "1. Format message with Block Kit\n"
        "2. Send via Slack webhook URL stored in config\n"
        "3. Include severity color and action links\n"
    ),
    "error recovery": (
        "## Additional Capability: Error Recovery\n"
        "On failure at any step:\n"
        "1. Log the error with full context\n"
        "2. Retry the failed step up to 3 times with exponential backoff\n"
        "3. If still failing, send alert and skip to next step\n"
        "4. Ensure partial results are preserved\n"
    ),
    "rate limiting": (
        "## Additional Capability: Rate Limiting\n"
        "Respect external API rate limits:\n"
        "1. Track requests per minute against known limits\n"
        "2. If approaching limit, add delay before next request\n"
        "3. Queue excess requests for next available window\n"
    ),
    "caching": (
        "## Additional Capability: Result Caching\n"
        "Cache frequently-fetched data to reduce API calls:\n"
        "1. Store results in `memory/cache/` with TTL\n"
        "2. Check cache before making external requests\n"
        "3. Invalidate cache on explicit trigger or TTL expiry\n"
    ),
    "email reports": (
        "## Additional Capability: Email Reports\n"
        "Send formatted email reports after execution:\n"
        "1. Generate HTML email from workflow results\n"
        "2. Send via configured SMTP or email API\n"
        "3. Include summary, key metrics, and action items\n"
    ),
    "data persistence": (
        "## Additional Capability: Data Persistence\n"
        "Store workflow results for historical analysis:\n"
        "1. Append results to `memory/skills/{skill_name}/history.jsonl`\n"
        "2. Include timestamp, input params, and full output\n"
        "3. Maintain rolling window of last 100 runs\n"
    ),
    "parallel execution": (
        "## Additional Capability: Parallel Execution\n"
        "Run independent steps concurrently:\n"
        "1. Identify steps with no inter-dependencies\n"
        "2. Execute in parallel using background tasks\n"
        "3. Aggregate results when all complete\n"
        "4. Fall back to sequential if parallel fails\n"
    ),
}


@app.post("/api/v1/skill/expand", response_model=ExpandResponse)
def expand_skill(req: ExpandRequest):
    """Add new capabilities to an existing skill."""
    # Get the base template or create from name
    base_name = req.base_skill_name.replace("-", " ").replace("_", " ")
    base_name_cap = base_name.title()

    changes = []
    sections = []

    for cap in req.additional_capabilities:
        cap_lower = cap.lower()
        if cap_lower in COMMON_CAPABILITIES:
            sections.append(COMMON_CAPABILITIES[cap_lower])
            changes.append(f"Added: {cap}")
        else:
            sections.append(f"## Additional Capability: {cap}\nCustom capability: {cap}\n")
            changes.append(f"Added custom capability: {cap}")

    expanded = f"""# {base_name_cap}

## Overview
This skill has been expanded with additional capabilities.

### Original Capabilities
See the base skill definition.

### Additional Capabilities
{chr(10).join(sections)}

## Notes
- All capabilities execute within the same skill context
- Capabilities share the same tool permissions and config
"""

    return ExpandResponse(
        expanded_skill_md_content=expanded.strip(),
        changes_summary=changes,
    )


# ─── /api/v1/skill/deploy-checklist ────────────────────────────────────────────

def get_deploy_checklist(skill_name: str) -> DeployChecklistResponse:
    """Generate a deployment checklist for a skill."""
    skill_name_clean = skill_name.replace("-", " ").replace("_", " ").title()

    # Basic dependency detection
    dependencies = []
    permissions = []
    setup_time = "5-10 minutes"
    files = []
    steps = []

    skill_lower = skill_name.lower()

    # Detect based on name keywords
    if any(k in skill_lower for k in ["social", "poster", "twitter", "linkedin"]):
        dependencies.extend(["requests", "tweepy or twitter API credentials"])
        permissions.append("network (outbound to social platform APIs)")
        setup_time = "15-30 minutes (API credentials needed)"

    if any(k in skill_lower for k in ["seo", "audit"]):
        dependencies.extend(["requests", "beautifulsoup4"])
        permissions.append("network (fetch target URLs)")
        setup_time = "10 minutes"

    if any(k in skill_lower for k in ["backup", "restore"]):
        dependencies.extend(["python-magic or mimetypes", "boto3 (if S3 backup)"])
        permissions.append("file system read/write access to backup paths")
        setup_time = "15 minutes"

    if any(k in skill_lower for k in ["uptime", "monitor", "status"]):
        dependencies.append("requests")
        permissions.append("network (HTTP/HTTPS checks)")
        setup_time = "5 minutes"

    if any(k in skill_lower for k in ["reddit", "research"]):
        dependencies.append("requests")
        permissions.append("network (Reddit API)")
        setup_time = "5 minutes"

    if any(k in skill_lower for k in ["discord", "slack", "notification"]):
        dependencies.append("requests")
        permissions.append("network (webhook URLs)")
        setup_time = "10 minutes (webhook URL setup)"

    if any(k in skill_lower for k in ["report", "email"]):
        dependencies.extend(["jinja2", "python-multipart"])
        permissions.append("network (SMTP or email API)")
        setup_time = "15 minutes"

    # Always need basic tools
    dependencies.append("openclaw CLI")

    files = [
        f"~/.openclaw/skills/{skill_name}/SKILL.md",
        f"~/.openclaw/skills/{skill_name}/config.yaml (optional)",
    ]

    steps = [
        f"1. Create skill directory: `mkdir -p ~/.openclaw/skills/{skill_name}/`",
        "2. Write the generated SKILL.md content to that directory",
        "3. Create config.yaml if the skill requires configuration",
        "4. Run `openclaw skills list` to verify skill is registered",
        "5. Run `openclaw skills validate {skill_name}` to check for errors",
        "6. Trigger a test run to confirm it works",
    ]

    if dependencies or permissions:
        steps.insert(0, "0. Install dependencies listed below first")

    return DeployChecklistResponse(
        skill_name=skill_name_clean,
        dependencies=sorted(set(dependencies)),
        permissions_needed=sorted(set(permissions)) or ["none beyond default skill execution context"],
        setup_time=setup_time,
        setup_steps=steps,
        files_to_create=files,
    )


@app.post("/api/v1/skill/deploy-checklist", response_model=DeployChecklistResponse)
def deploy_checklist(req: dict):
    """Get deployment checklist for a skill by name."""
    skill_name = req.get("skill_name") if isinstance(req, dict) else str(req)
    return get_deploy_checklist(skill_name)


# ─── /api/v1/skill/generate ────────────────────────────────────────────────────
# (registered via router include above)

# ─── Root ──────────────────────────────────────────────────────────────────────

@app.get("/", tags=["info"])
def root():
    return {
        "name": "OpenClawify",
        "version": "1.0.0",
        "tagline": "Describe your workflow. Get a working OpenClaw skill.",
        "docs": "/docs",
        "templates": "/api/v1/templates",
    }


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
