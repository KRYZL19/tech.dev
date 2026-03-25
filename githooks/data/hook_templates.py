# Hook Templates — 20 bundled pre-commit hooks

HOOK_TEMPLATES = {
    "trailing-whitespace": {
        "name": "trailing-whitespace",
        "description": "Flag lines ending with trailing whitespace",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [
            {
                "id": "trailing-whitespace",
                "args": ["--markdown-linefix-empty-only"],
            }
        ],
    },
    "end-of-file-fixer": {
        "name": "end-of-file-fixer",
        "description": "Ensure files end with a newline",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [{"id": "end-of-file-fixer"}],
    },
    "check-yaml": {
        "name": "check-yaml",
        "description": "Validate YAML syntax",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [{"id": "check-yaml"}],
    },
    "check-json": {
        "name": "check-json",
        "description": "Validate JSON files",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [{"id": "check-json"}],
    },
    "check-toml": {
        "name": "check-toml",
        "description": "Validate TOML syntax",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [{"id": "check-toml"}],
    },
    "mixed-line-ending": {
        "name": "mixed-line-ending",
        "description": "Normalize line endings to LF",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [{"id": "mixed-line-ending", "args": ["--fix=lf"]}],
    },
    "secrets-scanning": {
        "name": "secrets-scanning",
        "description": "Detect secrets and credentials committed to git",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [
            {
                "id": "detekt-secrets",
                "additional_dependencies": ["detekt-secrets@1.23.6"],
            }
        ],
        "alt_repo": "https://github.com/trufflesecurity/trufflehog",
        "alt_rev": "v3.80.0",
        "alt_hooks": [{"id": "trufflehog", "args": ["--no-update"]}],
    },
    "aws-credentials-scanning": {
        "name": "aws-credentials-scanning",
        "description": "Detect AWS credentials patterns in code",
        "languages": ["all"],
        "repo": "local",
        "local_hook": {
            "id": "aws-creds-check",
            "name": "AWS Credentials Scanner",
            "entry": "bash -c 'grep -r -E \"(AKIA|AWS_ACCESS_KEY|AWS_SECRET)\" . --include=\"*.py\" --include=\"*.js\" --include=\"*.yaml\" --include=\"*.json\" | grep -v \"test\\|spec\\|.git\" || true'",
            "language": "system",
            "pass_filenames": False,
        },
    },
    "large-files-check": {
        "name": "large-files-check",
        "description": "Prevent committing large files (>1MB by default)",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [{"id": "check-added-large-files", "args": ["--maxkb=1024"]}],
    },
    "python-flake8": {
        "name": "python-flake8",
        "description": "Python linting with Flake8",
        "languages": ["python"],
        "repo": "https://github.com/pycqa/flake8",
        "rev": "7.1.1",
        "hooks": [
            {
                "id": "flake8",
                "args": ["--max-line-length=120", "--extend-ignore=E203,W503"],
            }
        ],
    },
    "python-black": {
        "name": "python-black",
        "description": "Python code formatting with Black",
        "languages": ["python"],
        "repo": "https://github.com/psf/black",
        "rev": "25.1.0",
        "hooks": [{"id": "black", "language_version": "python3"}],
    },
    "python-isort": {
        "name": "python-isort",
        "description": "Python import sorting with isort",
        "languages": ["python"],
        "repo": "https://github.com/pycqa/isort",
        "rev": "5.14.0",
        "hooks": [{"id": "isort", "args": ["--profile=black"]}],
    },
    "python-mypy": {
        "name": "python-mypy",
        "description": "Python type checking with MyPy",
        "languages": ["python"],
        "repo": "https://github.com/pre-commit/mirrors-mypy",
        "rev": "v1.11.2",
        "hooks": [{"id": "mypy", "additional_dependencies": ["types-all"]}],
    },
    "python-pylint": {
        "name": "python-pylint",
        "description": "Python linting with Pylint",
        "languages": ["python"],
        "repo": "https://github.com/pylint-dev/pylint",
        "rev": "v3.3.1",
        "hooks": [{"id": "pylint", "args": ["--max-line-length=120"]}],
    },
    "python-pytest": {
        "name": "python-pytest",
        "description": "Run Python tests with pytest before commit",
        "languages": ["python"],
        "repo": "local",
        "local_hook": {
            "id": "python-pytest",
            "name": "pytest",
            "entry": "pytest --tb=short",
            "language": "system",
            "pass_filenames": False,
            "types": ["python"]},
    },
    "javascript-eslint": {
        "name": "javascript-eslint",
        "description": "JavaScript/TypeScript linting with ESLint",
        "languages": ["javascript", "typescript"],
        "repo": "https://github.com/pre-commit/mirrors-eslint",
        "rev": "v9.15.0",
        "hooks": [
            {
                "id": "eslint",
                "types": ["javascript", "typescript"],
                "args": ["--fix"],
            }
        ],
    },
    "javascript-prettier": {
        "name": "javascript-prettier",
        "description": "JavaScript/TypeScript formatting with Prettier",
        "languages": ["javascript", "typescript"],
        "repo": "https://github.com/pre-commit/mirrors-prettier",
        "rev": "3.3.3",
        "hooks": [
            {
                "id": "prettier",
                "types": ["javascript", "typescript"],
                "args": ["--write"],
            }
        ],
    },
    "go-fmt": {
        "name": "go-fmt",
        "description": "Go code formatting with gofmt",
        "languages": ["go"],
        "repo": "local",
        "local_hook": {
            "id": "gofmt",
            "name": "gofmt",
            "entry": "gofmt -l -s -w",
            "language": "system",
            "types": ["go"],
            "pass_filenames": True,
        },
    },
    "go-vet": {
        "name": "go-vet",
        "description": "Go vet analysis",
        "languages": ["go"],
        "repo": "local",
        "local_hook": {
            "id": "govet",
            "name": "go vet",
            "entry": "go vet ./...",
            "language": "system",
            "types": ["go"],
            "pass_filenames": False,
        },
    },
    "rust-clippy": {
        "name": "rust-clippy",
        "description": "Rust linting with Clippy",
        "languages": ["rust"],
        "repo": "local",
        "local_hook": {
            "id": "clippy",
            "name": "clippy",
            "entry": "cargo clippy --all-targets --all-features -- -D warnings",
            "language": "system",
            "types": ["rust"],
            "pass_filenames": False,
        },
    },
    "rust-fmt": {
        "name": "rust-fmt",
        "description": "Rust formatting with rustfmt",
        "languages": ["rust"],
        "repo": "local",
        "local_hook": {
            "id": "rustfmt",
            "name": "rustfmt",
            "entry": "cargo fmt --check",
            "language": "system",
            "types": ["rust"],
            "pass_filenames": False,
        },
    },
    "dockerfile-lint": {
        "name": "dockerfile-lint",
        "description": "Lint Dockerfiles with hadolint",
        "languages": ["docker"],
        "repo": "https://github.com/hadolint/hadolint",
        "rev": "v2.12.0",
        "hooks": [{"id": "hadolint"}],
    },
    "terraform-fmt": {
        "name": "terraform-fmt",
        "description": "Format Terraform files with terraform fmt",
        "languages": ["terraform"],
        "repo": "local",
        "local_hook": {
            "id": "terraform-fmt",
            "name": "terraform fmt",
            "entry": "terraform fmt -check -recursive",
            "language": "system",
            "types": ["terraform"],
            "pass_filenames": False,
        },
    },
    "terraform-validate": {
        "name": "terraform-validate",
        "description": "Validate Terraform configuration",
        "languages": ["terraform"],
        "repo": "local",
        "local_hook": {
            "id": "terraform-validate",
            "name": "terraform validate",
            "entry": "terraform validate",
            "language": "system",
            "types": ["terraform"],
            "pass_filenames": False,
        },
    },
    "markdown-lint": {
        "name": "markdown-lint",
        "description": "Lint Markdown files",
        "languages": ["markdown"],
        "repo": "https://github.com/DavidAnson/markdownlint",
        "rev": "v0.37.0",
        "hooks": [
            {
                "id": "markdownlint",
                "args": ["--disable=MD013", "--disable=MD033"],
            }
        ],
    },
    "commit-msg-lint": {
        "name": "commit-msg-lint",
        "description": "Enforce conventional commit format",
        "languages": ["all"],
        "repo": "https://github.com/conventional-changelog/commitlint",
        "rev": "v19.5.0",
        "hooks": [
            {
                "id": "commitlint",
                "types": ["commit"],
                "args": ["--conventional"],
            }
        ],
    },
    "no-commit-to-branch": {
        "name": "no-commit-to-branch",
        "description": "Prevent committing directly to main/master branches",
        "languages": ["all"],
        "repo": "https://github.com/pre-commit/pre-commit-hooks",
        "rev": "v4.5.0",
        "hooks": [
            {
                "id": "no-commit-to-branch",
                "args": ["--branch", "main", "--branch", "master"],
            }
        ],
    },
}

# Mapping from tech stack keywords to recommended hooks
TECH_STACK_HOOKS = {
    "python": ["python-flake8", "python-black", "python-isort", "python-mypy", "trailing-whitespace", "end-of-file-fixer", "mixed-line-ending"],
    "javascript": ["javascript-eslint", "javascript-prettier", "trailing-whitespace", "end-of-file-fixer", "large-files-check"],
    "typescript": ["javascript-eslint", "javascript-prettier", "trailing-whitespace", "end-of-file-fixer", "large-files-check"],
    "go": ["go-fmt", "go-vet", "trailing-whitespace", "end-of-file-fixer", "large-files-check"],
    "rust": ["rust-clippy", "rust-fmt", "trailing-whitespace", "end-of-file-fixer", "large-files-check"],
    "terraform": ["terraform-fmt", "terraform-validate", "check-yaml", "trailing-whitespace"],
    "docker": ["dockerfile-lint", "trailing-whitespace"],
    "markdown": ["markdown-lint", "trailing-whitespace", "end-of-file-fixer"],
    "web": ["javascript-eslint", "javascript-prettier", "check-yaml", "check-json", "trailing-whitespace", "end-of-file-fixer"],
    "api": ["check-yaml", "check-json", "trailing-whitespace", "end-of-file-fixer"],
    "fullstack": ["python-flake8", "python-black", "javascript-eslint", "javascript-prettier", "check-yaml", "check-json", "trailing-whitespace", "end-of-file-fixer"],
}

REPO_TYPE_HOOKS = {
    "library": ["no-commit-to-branch", "large-files-check", "commit-msg-lint"],
    "service": ["no-commit-to-branch", "large-files-check", "commit-msg-lint", "secrets-scanning"],
    "webapp": ["secrets-scanning", "large-files-check", "commit-msg-lint", "no-commit-to-branch"],
    "infrastructure": ["terraform-fmt", "terraform-validate", "dockerfile-lint", "commit-msg-lint"],
    "data": ["check-json", "check-yaml", "large-files-check", "commit-msg-lint"],
    "ml": ["python-flake8", "python-black", "check-yaml", "check-json", "large-files-check", "commit-msg-lint"],
}

DEPRECATED_HOOKS = {
    "secrets-scanning": "v4.0.0",
    "aws-credentials-scanning": "v3.0.0",
}

HOOK_CONFLICTS = {
    "python-black": ["python-autopep8", "python-yapf"],
    "python-isort": ["python-autopep8"],
    "python-pylint": ["python-flake8"],
}
