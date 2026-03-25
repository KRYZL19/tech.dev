"""Skill validation route."""

import yaml
import re
from fastapi import APIRouter
from models.schemas import ValidateRequest, ValidateResponse

router = APIRouter(prefix="/api/v1/skill", tags=["skill"])

# Required top-level fields in a SKILL.md
REQUIRED_FIELDS = ["name", "description"]

# Fields that should be strings
STRING_FIELDS = ["name", "description", "trigger"]

# Fields that should be lists (or strings for simple values)
LIST_FIELDS = ["tools", "required_tools", "dependencies", "permissions"]

# Known field names (whitelist approach)
KNOWN_FIELDS = {
    "name", "description", "trigger", "trigger_mode",
    "tools", "required_tools", "dependencies", "permissions",
    "workflow", "steps", "configuration", "setup", "notes",
    "schedule", "endpoints", "webhook", "output", "output_format",
}


def validate_yaml_structure(content: str) -> tuple[bool, list[str], list[str]]:
    """
    Validate SKILL.md YAML content.
    Returns (valid, issues, syntax_errors).
    """
    issues = []
    syntax_errors = []

    # Check for YAML parsing errors
    try:
        data = yaml.safe_load(content)
        if data is None:
            syntax_errors.append("Empty YAML content")
            return False, issues, syntax_errors
    except yaml.YAMLError as e:
        syntax_errors.append(f"YAML parse error: {e}")
        return False, issues, syntax_errors

    if not isinstance(data, dict):
        syntax_errors.append("Root element must be a dictionary (key-value pairs)")
        return False, issues, syntax_errors

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            issues.append(f"Missing required field: '{field}'")

    # Validate field types
    for field, value in data.items():
        if field not in KNOWN_FIELDS:
            issues.append(f"Unknown field: '{field}' — did you mean one of: {', '.join(sorted(KNOWN_FIELDS))}")

        if field in STRING_FIELDS and not isinstance(value, str):
            issues.append(f"Field '{field}' should be a string, got {type(value).__name__}")

        if field in LIST_FIELDS and not isinstance(value, list):
            if isinstance(value, str):
                issues.append(f"Field '{field}' should be a list, not a single string. Did you mean: [{value}]?")

    # Check for common YAML mistakes
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        # Tab indentation
        if line.startswith('\t'):
            issues.append(f"Line {i}: Tabs used for indentation (use spaces)")
        # Inline list without proper dashes
        if re.match(r'^\s*-\s+\w+:\s*\[', line):
            issues.append(f"Line {i}: Inline list syntax may be ambiguous — prefer block style")
        # Empty key
        if re.match(r'^\s*:\s*$', line):
            issues.append(f"Line {i}: Empty key name")

    # Check tools/required_tools exist and are non-empty
    tools_field = data.get("tools") or data.get("required_tools", [])
    if isinstance(tools_field, list) and len(tools_field) == 0:
        issues.append("'tools' list is empty — skill may not have any actions")

    # Description length check
    desc = data.get("description", "")
    if isinstance(desc, str) and len(desc) < 10:
        issues.append("Description is too short — add more context about what this skill does")

    valid = len(syntax_errors) == 0 and len(issues) == 0
    return valid, issues, syntax_errors


@router.post("/validate", response_model=ValidateResponse)
def validate_skill(req: ValidateRequest):
    """
    Validate SKILL.md YAML content.
    Checks for valid YAML syntax, required fields, and semantic issues.
    """
    valid, issues, syntax_errors = validate_yaml_structure(req.skill_md_content)
    return ValidateResponse(
        valid_yaml=valid,
        issues=issues,
        syntax_errors=syntax_errors,
    )
