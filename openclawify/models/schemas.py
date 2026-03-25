"""Pydantic schemas for OpenClawify API."""

from pydantic import BaseModel, Field
from typing import Optional


# ─── Generate ──────────────────────────────────────────────────────────────────

class GenerateRequest(BaseModel):
    workflow_description: str = Field(..., description="Plain English description of the desired skill workflow")
    trigger_keywords: list[str] = Field(..., description="Keywords that hint at trigger type (e.g., ['schedule', 'cron', 'daily'])")
    required_tools: list[str] = Field(..., description="Tools the skill needs to use (e.g., ['web_search', 'read', 'exec'])")


class GenerateResponse(BaseModel):
    skill_name: str = Field(..., description="Generated skill name (kebab-case)")
    skill_md_content: str = Field(..., description="Full SKILL.md YAML content")
    suggested_tools: list[str] = Field(..., description="Additional tools suggested based on workflow")
    template_used: str = Field(..., description="Template ID that was matched")


# ─── Validate ─────────────────────────────────────────────────────────────────

class ValidateRequest(BaseModel):
    skill_md_content: str = Field(..., description="SKILL.md YAML content to validate")


class ValidateResponse(BaseModel):
    valid_yaml: bool = Field(..., description="Whether the YAML parses successfully")
    issues: list[str] = Field(default_factory=list, description="Semantic issues found (missing fields, bad values)")
    syntax_errors: list[str] = Field(default_factory=list, description="YAML syntax/parsing errors")


# ─── Templates ─────────────────────────────────────────────────────────────────

class TemplateInfo(BaseModel):
    id: str
    name: str
    description: str
    trigger_mode: str


class TemplatesResponse(BaseModel):
    templates: list[TemplateInfo]


# ─── Expand ────────────────────────────────────────────────────────────────────

class ExpandRequest(BaseModel):
    base_skill_name: str = Field(..., description="Name of existing skill to expand")
    additional_capabilities: list[str] = Field(..., description="New capabilities to add to the skill")


class ExpandResponse(BaseModel):
    expanded_skill_md_content: str = Field(..., description="Updated SKILL.md with new capabilities added")
    changes_summary: list[str] = Field(..., description="List of changes made")


# ─── Deploy Checklist ──────────────────────────────────────────────────────────

class DeployChecklistResponse(BaseModel):
    skill_name: str
    dependencies: list[str] = Field(..., description="External dependencies (pip packages, CLI tools)")
    permissions_needed: list[str] = Field(..., description="Permissions required (file access, network, elevated)")
    setup_time: str = Field(..., description="Estimated setup time (e.g., '5 minutes', '1 hour')")
    setup_steps: list[str] = Field(..., description="Step-by-step setup instructions")
    files_to_create: list[str] = Field(..., description="Files that need to be created")
