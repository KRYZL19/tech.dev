# VIBECODER

> Your AI coding assistant doesn't know what you were working on 4 hours ago. This fixes that.

VIBECODER is an AI Coding Session Context Manager that maintains coding context across sessions, enabling AI assistants to resume work seamlessly.

## Features

- **Session Management**: Start, resume, and summarize coding sessions
- **Code Review**: Static analysis of diffs with issue detection and security scanning
- **Language Patterns**: Bundled patterns for Python, JavaScript, TypeScript, Rust, and Go

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/session/start` | Start a new coding session |
| POST | `/api/v1/session/resume` | Resume an existing session |
| POST | `/api/v1/session/summary` | Get session summary |
| POST | `/api/v1/review/diff` | Review code changes |
| GET | `/api/v1/patterns/{lang}` | Get language patterns |

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

API available at `http://localhost:8000`

## Pricing

| Plan | Requests | Price |
|------|----------|-------|
| Free | 50/day | Free |
| Dev | Unlimited | $19/month |
| Pro | Unlimited + Priority | $49/month |

## Supported Languages

- Python
- JavaScript
- TypeScript
- Rust
- Go

## Example Usage

### Start Session
```bash
curl -X POST http://localhost:8000/api/v1/session/start \
  -H "Content-Type: application/json" \
  -d '{"task": "Build user auth", "language": "python", "framework": "fastapi"}'
```

### Resume Session
```bash
curl -X POST http://localhost:8000/api/v1/session/resume \
  -H "Content-Type: application/json" \
  -d '{"session_id": "YOUR_SESSION_ID", "new_message": "Added JWT token generation"}'
```

### Review Diff
```bash
curl -X POST http://localhost:8000/api/v1/review/diff \
  -H "Content-Type: application/json" \
  -d '{"session_id": "YOUR_SESSION_ID", "diff": "+ password = request.json()"}'
```

## License

MIT
