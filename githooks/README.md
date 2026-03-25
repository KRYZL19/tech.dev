# GITHOOKS — Pre-commit Hook Generator

**"Tell it your tech stack. Get pre-commit hooks that actually catch things."**

## Overview

GITHOOKS generates tailored pre-commit hook configurations for your repository. Define your tech stack and get production-ready `.pre-commit-config.yaml` files, CI templates, and validation — all via a clean REST API.

## Tech Stack

- **FastAPI** — async web framework
- **Pydantic** — request/response validation
- **PyYAML** — pre-commit config parsing

## API Endpoints

### `POST /api/v1/hooks/generate`
Generate a pre-commit config from tech stack, repo type, and custom hooks.

```json
{
  "tech_stack": ["python", "javascript"],
  "repo_type": "webapp",
  "custom_checks": ["commit-msg-lint"]
}
```

**Response:**
```json
{
  "pre_commit_yaml_content": "repos:\n  - repo: https://github.com/pre-commit...",
  "hooks_to_install": ["python-flake8", "python-black", ...],
  "install_instructions": "..."
}
```

### `POST /api/v1/hooks/validate`
Validate an existing pre-commit YAML and detect conflicts, deprecated hooks.

```json
{
  "pre_commit_yaml_content": "repos:\n  - repo: ..."
}
```

**Response:**
```json
{
  "valid_yaml": true,
  "hook_conflicts": [],
  "deprecated_hooks": []
}
```

### `GET /api/v1/hooks/{hook_type}`
Get details for a specific hook (e.g. `python-mypy`).

### `POST /api/v1/hooks/ci-template`
Generate CI pipeline configs for GitHub Actions, GitLab CI, or Jenkins.

```json
{
  "tech_stack": ["python"],
  "ci_provider": "github_actions"
}
```

## Bundled Hooks (20)

| Hook | Description |
|------|-------------|
| `trailing-whitespace` | Flag trailing whitespace |
| `end-of-file-fixer` | Ensure newline at EOF |
| `check-yaml` | Validate YAML syntax |
| `check-json` | Validate JSON files |
| `check-toml` | Validate TOML files |
| `mixed-line-ending` | Normalize to LF |
| `secrets-scanning` | Detect committed secrets |
| `aws-credentials-scanning` | Detect AWS credential patterns |
| `large-files-check` | Prevent large file commits |
| `python-flake8` | Python linting |
| `python-black` | Python formatting |
| `python-isort` | Import sorting |
| `python-mypy` | Type checking |
| `python-pylint` | Python linting |
| `python-pytest` | Run pytest on commit |
| `javascript-eslint` | JS/TS linting |
| `javascript-prettier` | JS/TS formatting |
| `go-fmt` | Go formatting |
| `go-vet` | Go vet analysis |
| `rust-clippy` | Rust linting |
| `rust-fmt` | Rust formatting |
| `dockerfile-lint` | Hadolint |
| `terraform-fmt` | Terraform formatting |
| `terraform-validate` | Terraform validation |
| `markdown-lint` | Markdown linting |
| `commit-msg-lint` | Conventional commits |
| `no-commit-to-branch` | Block direct main/master commits |

## Pricing

| Plan | Requests/day | Cost |
|------|-------------|------|
| Free | 30/day | $0 |
| Dev | Unlimited | $14/mo |
| Pro | Unlimited + priority | $39/mo |

## Quick Start

```bash
cd githooks
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Install pre-commit in Your Project

```bash
pip install pre-commit
pre-commit install
```

## Run Tests

```bash
pytest
```
