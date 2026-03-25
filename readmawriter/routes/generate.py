"""README generation logic."""

import re
from typing import Optional


def detect_project_type(
    file_tree: list[str],
    package_json: Optional[str] = None,
    pyproject_toml: Optional[str] = None,
    primary_language: Optional[str] = None
) -> str:
    """Detect the project type from file structure and manifests."""
    
    # Check for package.json (Node.js)
    if package_json or any("package.json" in f for f in file_tree):
        if any(k in " ".join(file_tree).lower() for k in ["discord", "telegram", "bot", "slack"]):
            return "bot"
        return "node_package"
    
    # Check for pyproject.toml or setup.py (Python)
    if pyproject_toml or any("pyproject.toml" in f or "setup.py" in f for f in file_tree):
        if any(k in " ".join(file_tree).lower() for k in ["cli", "command", "main.py"]):
            return "cli"
        return "library"
    
    # Check for FastAPI, Flask, Express patterns (API)
    tree_lower = " ".join(file_tree).lower()
    api_indicators = ["fastapi", "flask", "express", "api", "routes", "endpoints", "app.py", "main.py"]
    if any(ind in tree_lower for ind in api_indicators):
        return "api"
    
    # Check for bot/agent patterns
    bot_indicators = ["bot", "agent", "telegram", "discord", "slack", "bot.py"]
    if any(ind in tree_lower for ind in bot_indicators):
        return "bot"
    
    # Check CLI indicators
    cli_indicators = ["main.py", "__main__", "cli.py", "argparse", "click"]
    if any(ind in tree_lower for ind in cli_indicators):
        return "cli"
    
    # Fallback based on language
    if primary_language:
        if primary_language.lower() in ["python"]:
            return "library"
        elif primary_language.lower() in ["javascript", "typescript"]:
            return "node_package"
        elif primary_language.lower() in ["go", "rust"]:
            return "cli"
    
    return "library"


def extract_project_name(file_tree: list[str], package_json: Optional[str] = None, pyproject_toml: Optional[str] = None) -> str:
    """Extract project name from file structure or manifests."""
    
    # Try package.json first
    if package_json:
        match = re.search(r'"name"\s*:\s*"([^"]+)"', package_json)
        if match:
            return match.group(1)
    
    # Try pyproject.toml
    if pyproject_toml:
        match = re.search(r'name\s*=\s*"([^"]+)"', pyproject_toml)
        if match:
            return match.group(1)
    
    # Extract from file paths (use first meaningful directory)
    for path in file_tree:
        parts = path.split("/")
        if len(parts) >= 2 and parts[0] not in ["src", "lib", "app", "tests", "test"]:
            return parts[0]
        if len(parts) == 1 and "." in parts[0]:
            return parts[0].split(".")[0]
    
    return "my-project"


def generate_description(file_tree: list[str], package_json: Optional[str] = None, pyproject_toml: Optional[str] = None) -> str:
    """Generate a project description from structure."""
    
    # Try from package.json
    if package_json:
        match = re.search(r'"description"\s*:\s*"([^"]+)"', package_json)
        if match:
            return match.group(1)
    
    # Try from pyproject.toml
    if pyproject_toml:
        match = re.search(r'description\s*=\s*"([^"]+)"', pyproject_toml)
        if match:
            return match.group(1)
    
    # Infer from structure
    tree_str = " ".join(file_tree).lower()
    
    if "bot" in tree_str or "telegram" in tree_str or "discord" in tree_str:
        return "A bot that automates tasks and responds to user commands."
    elif "api" in tree_str or "fastapi" in tree_str or "flask" in tree_str:
        return "A REST API service built with modern best practices."
    elif "cli" in tree_str or "command" in tree_str:
        return "A command-line tool for efficient task execution."
    elif "lib" in tree_str or "sdk" in tree_str:
        return "A Python library providing reusable functionality."
    
    return "A software project."


def analyze_structure(file_tree: list[str]) -> dict:
    """Analyze file tree to understand project structure."""
    
    analysis = {
        "has_tests": False,
        "has_docker": False,
        "has_ci": False,
        "has_docs": False,
        "has_config": False,
        "main_files": [],
        "modules": [],
        "languages": set(),
    }
    
    for path in file_tree:
        lower = path.lower()
        
        if "test" in lower or "spec" in lower:
            analysis["has_tests"] = True
        if "docker" in lower or "dockerfile" in lower:
            analysis["has_docker"] = True
        if ".github" in lower or "travis" in lower or "gitlab-ci" in lower:
            analysis["has_ci"] = True
        if "docs" in lower or "doc" in lower:
            analysis["has_docs"] = True
        if any(c in lower for c in [".env", "config", ".yml", ".yaml", ".toml"]):
            analysis["has_config"] = True
        
        # Track main files
        if any(m in lower for m in ["main.py", "index.js", "app.py", "main.go", "lib.rs"]):
            analysis["main_files"].append(path)
        
        # Track extensions
        ext = path.split(".")[-1] if "." in path else ""
        if ext in ["py", "js", "ts", "go", "rs", "java", "rb"]:
            analysis["languages"].add(ext)
    
    analysis["languages"] = list(analysis["languages"])
    return analysis


def build_readme_content(
    project_type: str,
    project_name: str,
    description: str,
    file_tree: list[str],
    package_json: Optional[str] = None,
    pyproject_toml: Optional[str] = None
) -> tuple[str, list[str], float]:
    """Build the README content based on project type and structure."""
    
    analysis = analyze_structure(file_tree)
    sections = []
    confidence = 0.7
    
    # Base README
    content = f"# {project_name}\n\n{description}\n\n"
    
    # Add badges section if CI exists
    if analysis["has_ci"]:
        badges = f"[![Build Status](https://img.shields.io/github/actions/workflow/status/{project_name}/ci.yml)](https://github.com/{project_name}/actions)\n"
        content += badges + "\n"
        sections.append("badges")
    
    # Overview
    content += "## Overview\n\n"
    content += f"This is a {project_type.replace('_', ' ')} project that "
    
    if project_type == "cli":
        content += "provides a command-line interface for interacting with its functionality.\n\n"
        sections.append("overview")
    elif project_type == "api":
        content += "exposes a REST API for programmatic access.\n\n"
        sections.append("overview")
    elif project_type == "library":
        content += "provides a set of reusable components and utilities.\n\n"
        sections.append("overview")
    elif project_type == "node_package":
        content += "can be used as an npm package in Node.js or browser applications.\n\n"
        sections.append("overview")
    elif project_type == "bot":
        content += "runs as an automated agent responding to events and commands.\n\n"
        sections.append("overview")
    
    # Features
    content += "## Features\n\n"
    features = []
    
    if analysis["has_tests"]:
        features.append("Comprehensive test suite")
        confidence += 0.05
    if analysis["has_docker"]:
        features.append("Docker support for easy deployment")
        confidence += 0.05
    if analysis["has_config"]:
        features.append("Configuration via environment variables or config files")
    if analysis["modules"]:
        features.append(f"Modular architecture with {len(analysis['modules'])} components")
    
    # Infer features from structure
    tree_str = " ".join(file_tree).lower()
    if "auth" in tree_str or "login" in tree_str:
        features.append("Authentication and authorization")
    if "database" in tree_str or "db" in tree_str or "postgres" in tree_str:
        features.append("Database integration")
    if "cache" in tree_str or "redis" in tree_str:
        features.append("Caching layer")
    if "api" in tree_str or "route" in tree_str:
        features.append("RESTful API endpoints")
    if "bot" in tree_str or "telegram" in tree_str:
        features.append("Bot integration")
    
    if not features:
        features = ["Easy to use", "Well-documented", "Production-ready"]
    
    for f in features:
        content += f"- {f}\n"
    content += "\n"
    sections.append("features")
    
    # Installation
    content += "## Installation\n\n"
    content += "```bash\n"
    
    if project_type in ["library", "cli"]:
        content += f"pip install {project_name}\n"
    elif project_type == "node_package":
        content += f"npm install {project_name}\n"
    elif project_type == "api":
        content += "pip install -r requirements.txt\n"
    elif project_type == "bot":
        content += "pip install -r requirements.txt\n"
    
    content += "```\n\n"
    
    if analysis["has_docker"]:
        content += "### Docker\n\n"
        content += "```bash\ndocker build -t {project_name} .\ndocker run {project_name}\n```\n\n"
        sections.append("docker")
    
    sections.append("installation")
    
    # Usage
    content += "## Usage\n\n"
    
    if project_type == "cli":
        content += "```bash\n"
        content += f"{project_name} --help\n"
        content += "```\n\n"
        sections.append("usage")
    elif project_type == "api":
        content += "Start the server:\n\n"
        content += "```bash\nuvicorn main:app --reload\n```\n\n"
        content += "Visit `http://localhost:8000/docs` for interactive API documentation.\n\n"
        sections.append("usage")
    elif project_type == "library":
        content += "```python\n"
        content += f"from {project_name} import \n"
        content += "```\n\n"
        sections.append("usage")
    elif project_type == "node_package":
        content += "```javascript\n"
        content += f"const {{ }} = require('{project_name}');\n"
        content += "```\n\n"
        sections.append("usage")
    elif project_type == "bot":
        content += "```bash\n"
        content += f"python -m {project_name}\n"
        content += "```\n\n"
        sections.append("usage")
    
    # Testing
    if analysis["has_tests"]:
        content += "## Testing\n\n"
        content += "```bash\n"
        if "python" in analysis["languages"]:
            content += "pytest\n"
        elif "javascript" in analysis["languages"] or "typescript" in analysis["languages"]:
            content += "npm test\n"
        content += "```\n\n"
        sections.append("testing")
    
    # Configuration
    if analysis["has_config"]:
        content += "## Configuration\n\n"
        content += "Configuration can be provided via environment variables or a `.env` file:\n\n"
        content += "```\n"
        content += "# Required\n"
        content += "API_KEY=your-api-key\n"
        content += "\n"
        content += "# Optional\n"
        content += "DEBUG=false\n"
        content += "PORT=8000\n"
        content += "```\n\n"
        sections.append("configuration")
    
    # Contributing
    content += "## Contributing\n\n"
    content += "Contributions are welcome! Please feel free to submit a Pull Request.\n\n"
    content += "1. Fork the repository\n"
    content += "2. Create your feature branch (`git checkout -b feature/amazing-feature`)\n"
    content += "3. Commit your changes (`git commit -m 'Add amazing feature'`)\n"
    content += "4. Push to the branch (`git push origin feature/amazing-feature`)\n"
    content += "5. Open a Pull Request\n\n"
    sections.append("contributing")
    
    # License
    content += "## License\n\n"
    content += "This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.\n"
    sections.append("license")
    
    return content, sections, min(confidence, 0.95)


async def generate_readme(
    file_tree: list[str],
    package_json: Optional[str] = None,
    pyproject_toml: Optional[str] = None,
    primary_language: Optional[str] = None,
) -> dict:
    """Generate a README from file tree and optional manifest files."""
    
    # Detect project type
    project_type = detect_project_type(file_tree, package_json, pyproject_toml, primary_language)
    
    # Extract project name
    project_name = extract_project_name(file_tree, package_json, pyproject_toml)
    
    # Generate description
    description = generate_description(file_tree, package_json, pyproject_toml)
    
    # Build README content
    readme_content, sections_included, confidence_score = build_readme_content(
        project_type=project_type,
        project_name=project_name,
        description=description,
        file_tree=file_tree,
        package_json=package_json,
        pyproject_toml=pyproject_toml
    )
    
    return {
        "readme_content": readme_content,
        "sections_included": sections_included,
        "confidence_score": confidence_score
    }
