# OpenClawify — OpenClaw Skill Generator

> Describe your workflow in plain English. Get a working OpenClaw skill.

OpenClawify is a FastAPI service that generates production-ready OpenClaw `SKILL.md` files from plain English workflow descriptions. It includes 10 built-in templates, YAML validation, skill expansion, and deployment checklists.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Visit `http://localhost:8000/docs` for the interactive Swagger UI.

## API Endpoints

### POST `/api/v1/skill/generate`

Generate a working OpenClaw skill from a workflow description.

```json
{
  "workflow_description": "Monitor my website every 5 minutes and alert me on Discord if it's down",
  "trigger_keywords": ["monitor", "alert", "discord"],
  "required_tools": ["web_fetch", "exec"]
}
```

**Response:**
```json
{
  "skill_name": "monitor-my-website-and-alert-on-discord",
  "skill_md_content": "# Monitor My Website...\n...",
  "suggested_tools": ["exec", "web_fetch"],
  "template_used": "monitor-alert"
}
```

### POST `/api/v1/skill/validate`

Validate a `SKILL.md` YAML file and get a list of issues.

```json
{
  "skill_md_content": "# My Skill\ndescription: does things\n..."
}
```

**Response:**
```json
{
  "valid_yaml": false,
  "issues": ["Missing required field: 'name'"],
  "syntax_errors": ["YAML parse error: ..." ]
}
```

### GET `/api/v1/templates`

List all 10 bundled skill templates.

### POST `/api/v1/skill/expand`

Add new capabilities to an existing skill.

```json
{
  "base_skill_name": "my-existing-skill",
  "additional_capabilities": ["discord notifications", "error recovery"]
}
```

### POST `/api/v1/skill/deploy-checklist`

Get a deployment checklist for a skill.

```json
{
  "skill_name": "my-social-poster"
}
```

## Bundled Templates

| ID | Name | Trigger |
|---|---|---|
| `webhook-triggered` | Webhook Triggered Skill | HTTP POST |
| `scheduled-task` | Scheduled Task Skill | Cron |
| `content-generator` | Content Generator Skill | Manual |
| `monitor-alert` | Monitor & Alert Skill | Cron |
| `social-poster` | Social Media Poster Skill | Manual |
| `seo-auditor` | SEO Auditor Skill | Manual |
| `reddit-researcher` | Reddit Researcher Skill | Manual |
| `uptime-checker` | Uptime Checker Skill | Cron |
| `backup-manager` | Backup Manager Skill | Cron |
| `report-generator` | Report Generator Skill | Scheduled |

## Pricing

| Plan | Daily Generations | Price |
|---|---|---|
| **Free** | 20/day | $0 |
| **Dev** | 500/day | $19/mo |
| **Pro** | Unlimited | $49/mo |

*Rate limiting is enforced via `X-RateLimit-*` headers.*

## Project Structure

```
openclawify/
├── main.py                  # FastAPI app + root routes
├── requirements.txt
├── README.md
├── data/
│   └── skill_templates.py   # 10 built-in SKILL.md templates
├── models/
│   └── schemas.py           # Pydantic request/response models
└── routes/
    ├── generate.py          # POST /skill/generate
    └── validate.py          # POST /skill/validate
```

## Example Usage

### Generate a skill

```bash
curl -X POST http://localhost:8000/api/v1/skill/generate \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_description": "Check my website every 10 minutes and send a Discord message if it returns a non-200 status",
    "trigger_keywords": ["uptime", "monitor", "discord"],
    "required_tools": ["web_fetch", "exec"]
  }'
```

### Validate a skill

```bash
curl -X POST http://localhost:8000/api/v1/skill/validate \
  -H "Content-Type: application/json" \
  -d '{
    "skill_md_content": "# My Monitor\ndescription: watches things\n..."
  }'
```

## Deployment

```bash
# Install
pip install -r requirements.txt

# Run
uvicorn main:app --host 0.0.0.0 --port 8000

# Production
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## License

MIT
