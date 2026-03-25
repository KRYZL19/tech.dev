"""Individual section generation logic."""

import re
from typing import Optional


def generate_overview_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate an overview section."""
    included = []
    content = "## Overview\n\n"
    
    # Analyze file tree for project purpose
    tree_str = " ".join(file_tree).lower()
    
    if "api" in tree_str or "route" in tree_str or "endpoint" in tree_str:
        content += "This project provides a REST API service "
        included.append("API service description")
    elif "bot" in tree_str or "telegram" in tree_str or "discord" in tree_str:
        content += "This is a bot that "
        included.append("Bot description")
    elif "cli" in tree_str:
        content += "This is a command-line tool that "
        included.append("CLI tool description")
    else:
        content += "This project provides "
        included.append("General purpose description")
    
    # Add code context if available
    if code_snippets:
        content += "designed to handle the following operations:\n\n"
        for snippet in code_snippets[:3]:
            # Extract function/class names from snippets
            funcs = re.findall(r'def\s+(\w+)|class\s+(\w+)|const\s+(\w+)|function\s+(\w+)', snippet)
            for match in funcs:
                name = next(m for m in match if m)
                content += f"- `{name}`\n"
            included.append("Code reference")
    else:
        content += "with a clean, modular architecture.\n\n"
    
    # Add architecture notes if multiple modules
    modules = set()
    for path in file_tree:
        if "/" in path:
            modules.add(path.split("/")[0])
    
    if len(modules) > 1:
        content += f"The project is organized into {len(modules)} main modules: "
        content += ", ".join(sorted(modules)) + ".\n\n"
        included.append("Module structure")
    
    return content, included


def generate_installation_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate an installation section."""
    included = []
    content = "## Installation\n\n"
    
    tree_str = " ".join(file_tree).lower()
    
    # Python project
    if any(f.endswith(".py") for f in file_tree) and "package.json" not in tree_str:
        if "requirements.txt" in tree_str:
            content += "```bash\npip install -r requirements.txt\n```\n\n"
            included.append("pip requirements install")
        else:
            content += "```bash\npip install .\n```\n\n"
            included.append("pip install")
        
        if "pyproject.toml" in tree_str:
            content += "Or using Poetry:\n\n"
            content += "```bash\npoetry install\n```\n\n"
            included.append("Poetry install")
    
    # Node.js project
    if "package.json" in tree_str or code_snippets and "require(" in str(code_snippets):
        content += "```bash\nnpm install\n```\n\n"
        included.append("npm install")
    
    # Docker
    if "dockerfile" in tree_str or "docker-compose" in tree_str:
        content += "### Docker\n\n"
        content += "```bash\ndocker build -t my-project .\n```\n\n"
        included.append("Docker build")
    
    return content, included


def generate_usage_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate a usage section."""
    included = []
    content = "## Usage\n\n"
    
    # Try to infer usage from main files
    for path in file_tree:
        if "main.py" in path or "main.go" in path or "index.js" in path:
            if path.endswith(".py"):
                content += "```bash\npython main.py\n```\n\n"
                included.append("Main entry point")
            elif path.endswith(".js"):
                content += "```bash\nnode index.js\n```\n\n"
                included.append("Node entry point")
    
    # Add code snippets as examples
    if code_snippets:
        content += "### Code Examples\n\n"
        for i, snippet in enumerate(code_snippets[:2]):
            # Clean up snippet (remove excess whitespace)
            lines = [l for l in snippet.strip().split("\n") if l.strip()]
            if len(lines) <= 15:
                content += "```python\n" + "\n".join(lines) + "\n```\n\n"
            else:
                content += "```python\n" + "\n".join(lines[:15]) + "\n# ...\n```\n\n"
            included.append(f"Example {i+1}")
    
    if not included:
        content += "See the [Examples](#examples) section for more detailed usage information.\n\n"
    
    return content, included


def generate_api_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate an API reference section."""
    included = []
    content = "## API Reference\n\n"
    
    # Find route/API files
    api_files = [f for f in file_tree if "route" in f.lower() or "api" in f.lower() or "endpoint" in f.lower()]
    
    if api_files:
        content += "### Endpoints\n\n"
        for f in api_files:
            content += f"- `{f}`\n"
        content += "\n"
        included.append("Endpoint list")
    else:
        content += "This section documents the available API endpoints.\n\n"
        included.append("API overview")
    
    # Try to extract endpoint info from code
    for snippet in code_snippets:
        routes = re.findall(r'@(app|router)\.(get|post|put|delete|patch)\("([^"]+)"', snippet)
        if routes:
            content += "| Method | Path | Description |\n"
            content += "|--------|------|-------------|\n"
            for _, method, path, *_ in routes:
                content += f"| {method.upper()} | `{path}` | TODO |\n"
            content += "\n"
            included.append("Route definitions")
            break
    
    content += "For interactive documentation, visit `/docs` when the server is running.\n\n"
    included.append("Interactive docs reference")
    
    return content, included


def generate_contributing_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate a contributing section."""
    included = []
    content = "## Contributing\n\n"
    
    content += "Contributions are welcome! Please follow these steps:\n\n"
    
    if "pytest" in str(file_tree) or "test" in str(file_tree):
        content += "1. Write tests for any new functionality\n"
        included.append("Testing requirement")
    
    content += "1. Fork the repository\n"
    content += "2. Create your feature branch (`git checkout -b feature/amazing-feature`)\n"
    content += "3. Commit your changes (`git commit -m 'Add amazing feature'`)\n"
    content += "4. Push to the branch (`git push origin feature/amazing-feature`)\n"
    content += "5. Open a Pull Request\n\n"
    included.append("Contribution steps")
    
    if "pytest" in str(file_tree) or "test" in str(file_tree):
        content += "Please ensure tests pass before submitting a PR.\n\n"
    
    return content, included


def generate_license_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate a license section."""
    included = []
    content = "## License\n\n"
    
    # Check for LICENSE file
    if "license" in str(file_tree).lower() or "mit" in str(file_tree).lower():
        content += "This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.\n"
        included.append("MIT License reference")
    else:
        content += "This project is licensed under the MIT License.\n"
        included.append("MIT License statement")
    
    return content + "\n", included


def generate_testing_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate a testing section."""
    included = []
    content = "## Testing\n\n"
    
    tree_str = " ".join(file_tree).lower()
    
    if "pytest" in tree_str or "test" in tree_str:
        content += "Run the test suite:\n\n"
        content += "```bash\npytest\n```\n\n"
        included.append("pytest command")
    
    if "jest" in tree_str:
        content += "Run the test suite:\n\n"
        content += "```bash\nnpm test\n```\n\n"
        included.append("npm test command")
    
    if code_snippets:
        included.append("Test examples from code")
    
    if not included:
        content += "Tests are located in the `tests/` directory.\n\n"
    
    return content, included


def generate_configuration_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate a configuration section."""
    included = []
    content = "## Configuration\n\n"
    
    # Detect config files
    config_files = [f for f in file_tree if any(c in f.lower() for c in [".env", "config", "settings"])]
    
    if config_files:
        content += "The following environment variables can be configured:\n\n"
        content += "| Variable | Description | Default |\n"
        content += "|----------|-------------|--------|\n"
        content += "| `DEBUG` | Enable debug mode | `false` |\n"
        content += "| `PORT` | Server port | `8000` |\n"
        content += "| `API_KEY` | API authentication key | - |\n"
        content += "\n"
        included.append("Environment variables")
        
        if ".env.example" in config_files:
            content += "Copy `.env.example` to `.env` and configure:\n\n"
            content += "```bash\ncp .env.example .env\n```\n\n"
            included.append("Dotenv setup")
    else:
        content += "Configuration can be provided via environment variables.\n\n"
        included.append("Environment configuration")
    
    return content, included


def generate_architecture_section(file_tree: list[str], code_snippets: list[str]) -> tuple[str, list[str]]:
    """Generate an architecture section."""
    included = []
    content = "## Architecture\n\n"
    
    # Analyze directory structure
    dirs = set()
    for path in file_tree:
        if "/" in path:
            dirs.add(path.split("/")[0])
    
    if dirs:
        content += "### Directory Structure\n\n"
        content += "```\n"
        for d in sorted(dirs):
            content += f"{d}/\n"
            # Show a few files in each directory
            subfiles = [f for f in file_tree if f.startswith(d + "/")][:3]
            for sf in subfiles:
                content += f"  {sf.split('/', 1)[1]}\n"
            if len([f for f in file_tree if f.startswith(d + "/")]) > 3:
                content += "  ...\n"
        content += "```\n\n"
        included.append("Directory structure")
    
    # Add component descriptions
    if code_snippets:
        content += "### Components\n\n"
        for snippet in code_snippets[:3]:
            classes = re.findall(r'class\s+(\w+)', snippet)
            for cls in classes:
                content += f"- `{cls}`: Component class\n"
        if classes:
            included.append("Component descriptions")
    
    return content, included


# Section handlers map
SECTION_HANDLERS = {
    "overview": generate_overview_section,
    "installation": generate_installation_section,
    "usage": generate_usage_section,
    "api": generate_api_section,
    "contributing": generate_contributing_section,
    "license": generate_license_section,
    "testing": generate_testing_section,
    "configuration": generate_configuration_section,
    "architecture": generate_architecture_section,
    # Aliases
    "examples": generate_usage_section,
    "faq": lambda ft, cs: ("## FAQ\n\n**Q: How do I get started?**\n\nA: See the Installation and Usage sections above.\n\n", ["FAQ overview"]),
    "deployment": lambda ft, cs: ("## Deployment\n\n### Docker\n\n```bash\ndocker build -t my-project .\ndocker run -p 8000:8000 my-project\n```\n\n### Manual\n\n```bash\ngunicorn main:app -b 0.0.0.0:8000\n```\n\n", ["Docker deployment", "Manual deployment"]),
    "changelog": lambda ft, cs: ("## Changelog\n\n### [Unreleased]\n\n- Initial release\n\n", ["Unreleased section"]),
}


async def generate_section(
    section_type: str,
    file_tree: list[str],
    code_snippets: list[str],
) -> dict:
    """Generate a specific README section."""
    
    handler = SECTION_HANDLERS.get(
        section_type.lower().replace("-", "_").replace(" ", "_")
    )
    
    if not handler:
        # Default section
        content = f"## {section_type.title()}\n\n"
        content += "TODO: Add content for this section.\n\n"
        return {
            "section_content": content,
            "what_to_include": ["Placeholder for manual completion"]
        }
    
    section_content, what_to_include = handler(file_tree, code_snippets)
    
    return {
        "section_content": section_content,
        "what_to_include": what_to_include
    }
