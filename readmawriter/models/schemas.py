"""Pydantic schemas for READMEWRITER API."""

from typing import Optional, Literal
from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """Request body for POST /api/v1/generate."""
    file_tree: list[str] = Field(
        ...,
        description="List of file paths representing the repository structure",
        example=[
            "src/main.py",
            "src/routes/api.py",
            "src/models/user.py",
            "requirements.txt",
            "README.md",
            ".env.example"
        ]
    )
    package_json: Optional[str] = Field(
        None,
        description="Contents of package.json for Node.js projects"
    )
    pyproject_toml: Optional[str] = Field(
        None,
        description="Contents of pyproject.toml for Python projects"
    )
    primary_language: Optional[str] = Field(
        None,
        description="Primary programming language (e.g., 'python', 'javascript', 'go')",
        example="python"
    )


class GenerateResponse(BaseModel):
    """Response body for POST /api/v1/generate."""
    readme_content: str = Field(
        ...,
        description="Generated README markdown content"
    )
    sections_included: list[str] = Field(
        ...,
        description="List of sections included in the generated README"
    )
    confidence_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score for the generation (0.0 to 1.0)"
    )


class SectionRequest(BaseModel):
    """Request body for POST /api/v1/section."""
    section_type: Literal[
        "overview", "installation", "usage", "api",
        "contributing", "license", "examples", "faq",
        "architecture", "testing", "deployment", "changelog"
    ] = Field(
        ...,
        description="Type of README section to generate"
    )
    file_tree: list[str] = Field(
        default_factory=list,
        description="Repository file structure for context"
    )
    code_snippets: list[str] = Field(
        default_factory=list,
        description="Code snippets to include in the section"
    )


class SectionResponse(BaseModel):
    """Response body for POST /api/v1/section."""
    section_content: str = Field(
        ...,
        description="Generated section markdown content"
    )
    what_to_include: list[str] = Field(
        ...,
        description="List of elements included in this section"
    )


class TemplateInfo(BaseModel):
    """Information about a single template."""
    name: str = Field(..., description="Template name")
    project_type: str = Field(..., description="Type of project this template is for")
    description: str = Field(..., description="Brief description of the template")
    sections: list[str] = Field(
        ...,
        description="Sections included in this template"
    )


class TemplatesResponse(BaseModel):
    """Response body for GET /api/v1/templates."""
    templates: dict[str, TemplateInfo] = Field(
        ...,
        description="Templates keyed by project type"
    )


class ValidateRequest(BaseModel):
    """Request body for POST /api/v1/validate."""
    readme_content: str = Field(
        ...,
        description="README markdown content to validate"
    )


class ValidateResponse(BaseModel):
    """Response body for POST /api/v1/validate."""
    missing_sections: list[str] = Field(
        default_factory=list,
        description="Sections that should be present but are missing"
    )
    stale_info: list[str] = Field(
        default_factory=list,
        description="Indicators of stale or incomplete information"
    )
    inconsistent_headings: list[str] = Field(
        default_factory=list,
        description="Heading style inconsistencies detected"
    )
