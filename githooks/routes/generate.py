from fastapi import APIRouter, HTTPException
import yaml
from models.schemas import GenerateRequest, GenerateResponse, CITemplateRequest, CITemplateResponse
from data.hook_templates import HOOK_TEMPLATES, TECH_STACK_HOOKS, REPO_TYPE_HOOKS

router = APIRouter(prefix="/api/v1/hooks", tags=["generate"])


def build_yaml(hook_ids: list[str]) -> str:
    lines = ["repos:", ""]
    repos = {}
    for hid in hook_ids:
        tpl = HOOK_TEMPLATES.get(hid)
        if not tpl:
            continue
        if tpl.get("repo") == "local":
            local = tpl["local_hook"]
            lines.append(f"  - repo: local")
            lines.append(f"    hooks:")
            lines.append(f"      - id: {local['id']}")
            lines.append(f"        name: {local['name']}")
            lines.append(f"        entry: {local['entry']}")
            lines.append(f"        language: {local['language']}")
            if local.get("types"):
                lines.append(f"        types: {local['types']}")
            if not local.get("pass_filenames", True):
                lines.append(f"        pass_filenames: false")
            lines.append("")
        else:
            repo_url = tpl["repo"]
            if repo_url not in repos:
                repos[repo_url] = {"rev": tpl["rev"], "hooks": []}
            hooks_entry = {}
            for h in tpl.get("hooks", []):
                hooks_entry["id"] = h["id"]
                if h.get("args"):
                    hooks_entry["args"] = h["args"]
                if h.get("additional_dependencies"):
                    hooks_entry["additional_dependencies"] = h["additional_dependencies"]
                if h.get("types"):
                    hooks_entry["types"] = h["types"]
                if h.get("language_version"):
                    hooks_entry["language_version"] = h["language_version"]
            repos[repo_url]["hooks"].append(hooks_entry)

    for repo_url, repo_data in repos.items():
        lines.append(f"  - repo: {repo_url}")
        lines.append(f"    rev: {repo_data['rev']}")
        lines.append(f"    hooks:")
        for h in repo_data["hooks"]:
            lines.append(f"      - id: {h['id']}")
            for key, val in h.items():
                if key != "id":
                    if isinstance(val, list):
                        lines.append(f"        {key}: {val}")
                    else:
                        lines.append(f"        {key}: {val}")
        lines.append("")
    return "\n".join(lines).strip()


def get_hooks_for_request(tech_stack: list[str], repo_type: str | None, custom_checks: list[str]) -> list[str]:
    seen = set()
    result = []
    for stack in tech_stack:
        for hook_id in TECH_STACK_HOOKS.get(stack.lower(), []):
            if hook_id not in seen:
                seen.add(hook_id)
                result.append(hook_id)
    if repo_type:
        for hook_id in REPO_TYPE_HOOKS.get(repo_type.lower(), []):
            if hook_id not in seen:
                seen.add(hook_id)
                result.append(hook_id)
    for hook_id in custom_checks:
        if hook_id not in seen:
            seen.add(hook_id)
            result.append(hook_id)
    return result


CI_TEMPLATES = {
    "github_actions": {
        "python": """name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pre-commit run --all-files
      - run: pytest
""",
        "javascript": """name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install
      - run: npx pre-commit run --all-files
      - run: npm test
""",
        "go": """name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - run: go install golang.org/x/tools/cmd/goimports@latest
      - run: pre-commit run --all-files
      - run: go test ./...
""",
        "rust": """name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions-rs/toolchain@v1
        with:
          toolchain: stable
      - run: rustup update
      - run: pre-commit run --all-files
      - run: cargo test
""",
    },
    "gitlab_ci": {
        "python": """stages:
  - test
pre-commit:
  stage: test
  image: python:3.11
  script:
    - pip install pre-commit
    - pre-commit run --all-files
pytest:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - pytest
""",
        "javascript": """stages:
  - test
pre-commit:
  stage: test
  image: node:20
  script:
    - npm install pre-commit
    - npx pre-commit run --all-files
""",
    },
    "jenkins": {
        "python": """pipeline {
    agent any
    stages {
        stage('Pre-commit') {
            steps {
                sh 'pip install pre-commit && pre-commit run --all-files'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
    }
}
""",
    },
}


@router.post("/generate", response_model=GenerateResponse)
async def generate_hooks(req: GenerateRequest):
    hook_ids = get_hooks_for_request(req.tech_stack, req.repo_type, req.custom_checks or [])
    if not hook_ids:
        raise HTTPException(status_code=400, detail="No hooks found for the given tech stack")

    missing = [h for h in hook_ids if h not in HOOK_TEMPLATES]
    if missing:
        raise HTTPException(status_code=400, detail=f"Unknown hook IDs: {missing}")

    yaml_content = build_yaml(hook_ids)

    instructions = [
        "1. Save the YAML content above as `.pre-commit-config.yaml` in your repository root.",
        "2. Run `pre-commit install` to install the git hook scripts.",
        "3. On the next commit, pre-commit will run all configured hooks.",
        "4. To update hooks: `pre-commit autoupdate`.",
    ]

    return GenerateResponse(
        pre_commit_yaml_content=yaml_content,
        hooks_to_install=hook_ids,
        install_instructions="\n".join(instructions),
    )


@router.post("/ci-template", response_model=CITemplateResponse)
async def ci_template(req: CITemplateRequest):
    provider = req.ci_provider.lower()
    stack_key = req.tech_stack[0].lower() if req.tech_stack else "python"

    template = ""
    for stack in req.tech_stack:
        s = stack.lower()
        if s in CI_TEMPLATES.get(provider, {}):
            template += CI_TEMPLATES[provider][s]
            break
    else:
        template = CI_TEMPLATES.get(provider, {}).get(stack_key, CI_TEMPLATES.get(provider, {}).get("python", ""))

    if not template:
        raise HTTPException(status_code=400, detail=f"No CI template for provider '{provider}'")

    install = f"Save the YAML above as `.github/workflows/ci.yml` for GitHub Actions, `.gitlab-ci.yml` for GitLab CI, or `Jenkinsfile` for Jenkins."
    return CITemplateResponse(ci_yaml_content=template, install_instructions=install)
