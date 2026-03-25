from pydantic import BaseModel, Field
from typing import Optional


class GenerateRequest(BaseModel):
    tech_stack: list[str] = Field(..., description="Tech stack identifiers (e.g. python, javascript, go)")
    repo_type: Optional[str] = Field(None, description="Repository type (library, service, webapp, infrastructure, data, ml)")
    custom_checks: Optional[list[str]] = Field(default_factory=list, description="Additional custom hook IDs to include")


class GenerateResponse(BaseModel):
    pre_commit_yaml_content: str
    hooks_to_install: list[str]
    install_instructions: str


class ValidateRequest(BaseModel):
    pre_commit_yaml_content: str


class ValidateResponse(BaseModel):
    valid_yaml: bool
    hook_conflicts: list[str] = Field(default_factory=list)
    deprecated_hooks: list[str] = Field(default_factory=list)
    error_message: Optional[str] = None


class HookInfo(BaseModel):
    id: str
    name: str
    description: str
    languages: list[str]
    repo: Optional[str] = None
    rev: Optional[str] = None
    hooks: list[dict] = Field(default_factory=list)


class CITemplateRequest(BaseModel):
    tech_stack: list[str] = Field(..., description="Tech stack identifiers")
    ci_provider: str = Field(..., description="CI provider: github_actions, gitlab_ci, jenkins")


class CITemplateResponse(BaseModel):
    ci_yaml_content: str
    install_instructions: str
