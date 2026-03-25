"""Skill generation route."""

import re
import yaml
import hashlib
from fastapi import APIRouter
from models.schemas import GenerateRequest, GenerateResponse
from data.skill_templates import SKILL_TEMPLATES, get_template

router = APIRouter(prefix="/api/v1/skill", tags=["skill"])

# Keywords that map to specific templates
TRIGGER_KEYWORD_MAP = {
    "webhook": "webhook-triggered",
    "hook": "webhook-triggered",
    "github": "webhook-triggered",
    "ci/cd": "webhook-triggered",
    "schedule": "scheduled-task",
    "cron": "scheduled-task",
    "daily": "scheduled-task",
    "hourly": "scheduled-task",
    "weekly": "scheduled-task",
    "content": "content-generator",
    "blog": "content-generator",
    "article": "content-generator",
    "newsletter": "content-generator",
    "monitor": "monitor-alert",
    "alert": "monitor-alert",
    "notify": "monitor-alert",
    "social": "social-poster",
    "twitter": "social-poster",
    "linkedin": "social-poster",
    "reddit": "social-poster",
    "seo": "seo-auditor",
    "audit": "seo-auditor",
    "search": "reddit-researcher",
    "reddit": "reddit-researcher",
    "uptime": "uptime-checker",
    "status": "uptime-checker",
    "availability": "uptime-checker",
    "backup": "backup-manager",
    "restore": "backup-manager",
    "report": "report-generator",
    "summary": "report-generator",
    "dashboard": "report-generator",
}

TOOL_SUGGESTIONS = {
    "web_search": ["web_search", "web_fetch"],
    "exec": ["exec", "process"],
    "read": ["read"],
    "write": ["write"],
    "email": ["exec (sendmail or API)"],
    "twitter": ["exec (Twitter API)"],
    "discord": ["exec (Discord webhook)"],
    "slack": ["exec (Slack webhook)"],
    "github": ["github skill"],
    "reddit": ["reddit-researcher"],
    "seo": ["seo-reporter", "web_fetch"],
}


def slugify(name: str) -> str:
    """Convert a name to kebab-case."""
    name = re.sub(r'[^\w\s-]', '', name).strip().lower()
    name = re.sub(r'[-\s]+', '-', name)
    return name


def detect_template(trigger_keywords: list[str], workflow_description: str) -> str:
    """Detect the best matching template based on keywords and description."""
    combined = " ".join(trigger_keywords) + " " + workflow_description.lower()

    scores = {}
    for keyword, template_id in TRIGGER_KEYWORD_MAP.items():
        if keyword in combined:
            scores[template_id] = scores.get(template_id, 0) + 1

    if scores:
        return max(scores, key=scores.get)
    return "scheduled-task"


def extract_skill_name(workflow_description: str) -> str:
    """Generate a skill name from the workflow description."""
    words = workflow_description.split()[:5]
    name = " ".join(w.capitalize() for w in words if w.isalpha())
    if not name:
        name = "CustomSkill"
    return name


def render_skill_md(template_id: str, skill_name: str, workflow_description: str, required_tools: list[str]) -> str:
    """Render a SKILL.md from the selected template."""
    template = get_template(template_id)
    slug = slugify(skill_name)

    # Build workflow steps from description
    steps = workflow_description.strip().split('.')
    steps = [s.strip() for s in steps if s.strip()]
    if not steps:
        steps = ["Execute the described workflow"]

    workflow_steps = "\n".join(f"{i+1}. {s.capitalize()}." for i, s in enumerate(steps))

    tools_list = ", ".join(f"- `{t}`" for t in required_tools) or "- (none specified)"

    suggested = set(required_tools)
    for tool in required_tools:
        for extra in TOOL_SUGGESTIONS.get(tool, []):
            suggested.add(extra)
    suggested_list = sorted(suggested)

    # Fill in template variables
    variables = {
        "skill_name": skill_name,
        "skill_slug": slug,
        "description": workflow_description,
        "workflow_steps": workflow_steps,
        "tools_list": tools_list,
        "output_description": "Returns the result of the described workflow execution",
    }

    yaml_content = template["yaml_template"]

    # Simple variable substitution
    for key, val in variables.items():
        yaml_content = yaml_content.replace(f"{{{key}}}", str(val))

    # Handle any remaining unfilled braces with defaults
    yaml_content = re.sub(r'\{([^}]+)\}', lambda m: f'"{m.group(1).strip()}"', yaml_content)

    return yaml_content.strip()


@router.post("/generate", response_model=GenerateResponse)
def generate_skill(req: GenerateRequest):
    """
    Generate a working OpenClaw SKILL.md from a plain English workflow description.
    """
    template_id = detect_template(req.trigger_keywords, req.workflow_description)
    template = get_template(template_id)
    skill_name = extract_skill_name(req.workflow_description)

    skill_md = render_skill_md(
        template_id=template_id,
        skill_name=skill_name,
        workflow_description=req.workflow_description,
        required_tools=req.required_tools,
    )

    # Suggest additional tools
    suggested = set(req.required_tools)
    for tool in req.required_tools:
        for extra in TOOL_SUGGESTIONS.get(tool, []):
            suggested.add(extra)

    return GenerateResponse(
        skill_name=slugify(skill_name),
        skill_md_content=skill_md,
        suggested_tools=sorted(suggested),
        template_used=template_id,
    )
