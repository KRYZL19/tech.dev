"""Bundled README templates for different project types."""

from typing import Dict
from models.schemas import TemplateInfo

# ── CLI Tool Template ──────────────────────────────────────────────────────────

CLI_TEMPLATE = """# {project_name}

{description}

## Overview

{overview}

## Features

{features}

## Installation

```bash
{pip_install}
```

Or with [Homebrew](https://brew.sh) (macOS/Linux):

```bash
brew install {brew_name}
```

## Usage

```bash
{cli_usage_example}
```

### Commands

{commands_section}

## Configuration

{configuration_section}

## Examples

{examples_section}

## License

{license_section}
"""


# ── REST API Template ──────────────────────────────────────────────────────────

API_TEMPLATE = """# {project_name}

{description}

## Overview

{overview}

## Quick Start

### Prerequisites

{prerequisites}

### Installation

```bash
git clone {repo_url}
cd {project_name}
{pip_install}
```

### Running the Server

```bash
{uvicorn_command}
```

The API will be available at `http://localhost:8000`

## API Reference

{api_reference}

### Endpoints

{endpoints_section}

### Authentication

{auth_section}

### Request/Response Examples

{examples_section}

## Configuration

{configuration_section}

## Deployment

{deployment_section}

## License

{license_section}
"""


# ── Python Library Template ─────────────────────────────────────────────────────

LIBRARY_TEMPLATE = """# {project_name}

{description}

## Overview

{overview}

## Installation

```bash
pip install {package_name}
```

For development:

```bash
git clone {repo_url}
cd {project_name}
pip install -e ".[dev]"
```

## Quick Start

{quick_start_section}

## Features

{features}

## Usage

{usage_section}

### Basic Example

```python
{basic_example}
```

## API Reference

{api_reference}

## Contributing

{contributing_section}

## License

{license_section}
"""


# ── Node.js Package Template ───────────────────────────────────────────────────

NODE_PACKAGE_TEMPLATE = """# {project_name}

{description}

## Overview

{overview}

## Installation

```bash
npm install {package_name}
```

Or with Yarn:

```bash
yarn add {package_name}
```

## Quick Start

{quick_start_section}

## Features

{features}

## Usage

{usage_section}

### ES Modules

```javascript
import {{ {import_name} }} from '{package_name}';
```

### CommonJS

```javascript
const {{ {import_name} }} = require('{package_name}');
```

## API Reference

{api_reference}

## Examples

{examples_section}

## Contributing

{contributing_section}

## License

{license_section}
"""


# ── Bot/Agent Template ─────────────────────────────────────────────────────────

BOT_TEMPLATE = """# {project_name}

{description}

## Overview

{overview}

## Features

{features}

## Requirements

{requirements}

## Installation

```bash
git clone {repo_url}
cd {project_name}
{pip_install}
```

## Configuration

{configuration_section}

## Usage

### Running the Bot

{bot_usage_example}

### Bot Commands

{commands_section}

## Architecture

{architecture_section}

## Deployment

{deployment_section}

## Monitoring

{monitoring_section}

## Contributing

{contributing_section}

## License

{license_section}
"""


# ── Template Registry ─────────────────────────────────────────────────────────

TEMPLATES: Dict[str, TemplateInfo] = {
    "cli": TemplateInfo(
        name="CLI Tool",
        project_type="cli",
        description="Template for command-line tools and utilities",
        sections=[
            "overview", "features", "installation",
            "usage", "commands", "configuration",
            "examples", "license"
        ]
    ),
    "api": TemplateInfo(
        name="REST API",
        project_type="api",
        description="Template for REST API services and backends",
        sections=[
            "overview", "prerequisites", "installation",
            "api_reference", "endpoints", "authentication",
            "examples", "configuration", "deployment", "license"
        ]
    ),
    "library": TemplateInfo(
        name="Python Library",
        project_type="library",
        description="Template for Python packages and libraries",
        sections=[
            "overview", "installation", "quick_start",
            "features", "usage", "api_reference",
            "contributing", "license"
        ]
    ),
    "node_package": TemplateInfo(
        name="Node.js Package",
        project_type="node_package",
        description="Template for npm packages and JavaScript/TypeScript libraries",
        sections=[
            "overview", "installation", "quick_start",
            "features", "usage", "api_reference",
            "examples", "contributing", "license"
        ]
    ),
    "bot": TemplateInfo(
        name="Bot/Agent",
        project_type="bot",
        description="Template for chatbots and AI agents",
        sections=[
            "overview", "features", "requirements",
            "installation", "configuration", "usage",
            "commands", "architecture", "deployment",
            "monitoring", "contributing", "license"
        ]
    )
}


def get_template_for_type(project_type: str) -> str | None:
    """Get the raw template string for a project type."""
    templates = {
        "cli": CLI_TEMPLATE,
        "api": API_TEMPLATE,
        "library": LIBRARY_TEMPLATE,
        "node_package": NODE_PACKAGE_TEMPLATE,
        "bot": BOT_TEMPLATE
    }
    return templates.get(project_type)


def list_templates() -> Dict[str, TemplateInfo]:
    """Return all available templates."""
    return TEMPLATES
