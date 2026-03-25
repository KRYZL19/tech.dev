from fastapi import APIRouter, HTTPException
import yaml
from models.schemas import ValidateRequest, ValidateResponse, HookInfo
from data.hook_templates import HOOK_TEMPLATES, HOOK_CONFLICTS, DEPRECATED_HOOKS

router = APIRouter(prefix="/api/v1/hooks", tags=["validate"])


@router.post("/validate", response_model=ValidateResponse)
async def validate_hooks(req: ValidateRequest):
    try:
        parsed = yaml.safe_load(req.pre_commit_yaml_content)
    except yaml.YAMLError as e:
        return ValidateResponse(
            valid_yaml=False,
            hook_conflicts=[],
            deprecated_hooks=[],
            error_message=str(e),
        )

    if parsed is None:
        return ValidateResponse(
            valid_yaml=False,
            hook_conflicts=[],
            deprecated_hooks=[],
            error_message="Empty YAML content",
        )

    hook_ids = []
    for repo in parsed.get("repos", []):
        if repo.get("repo") == "local":
            for hook in repo.get("hooks", []):
                hook_ids.append(hook.get("id", ""))
        else:
            for hook in repo.get("hooks", []):
                hook_ids.append(hook.get("id", ""))

    conflicts = []
    for hook_id in hook_ids:
        for conflict in HOOK_CONFLICTS.get(hook_id, []):
            if conflict in hook_ids:
                conflicts.append(f"{hook_id} conflicts with {conflict}")

    deprecated = [h for h in hook_ids if h in DEPRECATED_HOOKS]

    return ValidateResponse(
        valid_yaml=True,
        hook_conflicts=list(dict.fromkeys(conflicts)),
        deprecated_hooks=deprecated,
    )


@router.get("/{hook_type}", response_model=HookInfo)
async def get_hook(hook_type: str):
    tpl = HOOK_TEMPLATES.get(hook_type)
    if not tpl:
        raise HTTPException(status_code=404, detail=f"Hook '{hook_type}' not found")

    return HookInfo(
        id=hook_type,
        name=tpl["name"],
        description=tpl["description"],
        languages=tpl["languages"],
        repo=tpl.get("repo"),
        rev=tpl.get("rev"),
        hooks=tpl.get("hooks", []),
    )
