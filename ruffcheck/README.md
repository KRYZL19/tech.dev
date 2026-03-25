# RUFFCHECK — Code Quality Linter API

> **Run ESLint, Ruff, or golangci-lint without installing anything. Just POST your code.**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

API runs at `http://localhost:8000` — docs at `http://localhost:8000/docs`.

## Endpoints

### POST `/api/v1/lint`
Lint code and get back a list of issues.

```json
{
  "code": "import os\nx = 1",
  "language": "python",
  "severity_filter": "warning"
}
```

```json
{
  "issues": [
    {
      "line": 1,
      "column": 8,
      "rule_id": "F401",
      "severity": "warning",
      "message": "'os' imported but unused",
      "fix_suggestion": null
    }
  ],
  "error_count": 0,
  "warning_count": 1,
  "total_issues": 1
}
```

### POST `/api/v1/fix`
Apply auto-fix suggestions to code.

```json
{
  "code": "x = 1  ==  2",
  "language": "javascript"
}
```

```json
{
  "fixed_code": "x = 1 === 2",
  "changes_made": ["eqeqeq: replaced '1  ==  2' with '1 === 2'"],
  "original_issues_resolved": 1
}
```

### GET `/api/v1/rules/{language}`
List all rules for a language.

```
GET /api/v1/rules/python
GET /api/v1/rules/javascript
GET /api/v1/rules/go
GET /api/v1/rules/rust
```

### POST `/api/v1/bulk`
Lint multiple files at once.

```json
{
  "files": [
    { "name": "main.py", "content": "import os\nx=1", "language": "python" },
    { "name": "app.js", "content": "let x = 1", "language": "javascript" }
  ]
}
```

## Supported Languages & Bundled Rules

| Language | Tool | Rules |
|---|---|---|
| `python` | Ruff | F401, E501, E203, W503, F841, E302, E303 |
| `javascript` | ESLint | no-unused-vars, prefer-const, no-extra-semi, eqeqeq, no-var, semi |
| `typescript` | ESLint + TS | ESLint rules + no-explicit-any |
| `go` | golangci-lint | gofmt, ineffassign, staticcheck, golint, errcheck, gocritic |
| `rust` | clippy | unused-imports, dead-code, ptr_arg, redundant_clone, prefer-deref |

## Pricing

| Tier | Requests | Price |
|---|---|---|
| **Free** | 50/day | $0 |
| **Dev** | 500/month | $19/mo |
| **Pro** | Unlimited | $59/mo |

Rate limits are enforced by IP/API key. Pass `Authorization: Bearer <key>` or `X-API-Key: <key>` header.

Upgrade at **https://ruffcheck.dev/pricing**

## Running with Docker

```dockerfile
FROM python:3.11-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

```bash
docker build -t ruffcheck .
docker run -p 8000:8000 ruffcheck
```

## Project Structure

```
ruffcheck/
├── main.py           # FastAPI app + all route handlers
├── requirements.txt  # Dependencies
├── data/
│   ├── __init__.py
│   └── rulesets.py   # All bundled rules (Python, JS, TS, Go, Rust)
├── models/
│   ├── __init__.py
│   └── schemas.py    # Pydantic request/response models
├── routes/
│   ├── __init__.py
│   ├── lint.py       # Lint route (stub)
│   └── fix.py        # Fix route (stub)
└── README.md
```

## Notes

- All linting is done via **regex-based pattern matching** bundled in `data/rulesets.py`.
  No external linter binaries are required.
- `fix_suggestion` fields provide replacement text where auto-fix is safe.
  The `/fix` endpoint applies these automatically.
- Not a replacement for real ESLint/Ruff/clippy — use those for production CI/CD.
  RUFFCHECK is for quick API-based checks without installing toolchains.

## License

MIT — https://ruffcheck.dev
