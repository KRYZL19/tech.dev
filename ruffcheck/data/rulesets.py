"""
Bundled rulesets for RUFFCHECK.

Each rule has:
  - id: str          — unique identifier
  - severity: str    — error | warning | info
  - pattern: re      — compiled regex with named groups for capture
  - message: str     — f-string using group names
  - description: str
  - fix: Optional[str] — replacement string (None = no auto-fix)
"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Rule:
    id: str
    severity: str
    pattern: re.Pattern
    message: str
    description: str
    fix: Optional[str] = None


# ─── Python / Ruff rules ───────────────────────────────────────────────────
# F401: 'module' imported but unused
# E501: line too long (limit 88 for Ruff, configurable)
# E203: whitespace before ':'
# W503: line break before binary operator

PYTHON_RULES: list[Rule] = [
    Rule(
        id="F401",
        severity="warning",
        pattern=re.compile(
            r"^(?P<indent>[ \t]*)(?P<import>import (?P<module>\w+)(?:\s+as\s+\w+)?)\s*$",
            re.MULTILINE,
        ),
        message="'%(module)s' imported but unused",
        description="F401 — a module is imported but not used in the file.",
        fix=None,  # Removing imports requires more context
    ),
    Rule(
        id="E501",
        severity="warning",
        pattern=re.compile(r"^(?P<line>.{89,})$", re.MULTILINE),
        message="Line too long (%(line)s), exceeds 88 characters",
        description="E501 — line too long (Ruff default: 88 chars).",
        fix=None,  # Line-splitting is context-dependent
    ),
    Rule(
        id="E203",
        severity="warning",
        pattern=re.compile(r"(?P<before>\w)\s*:\s*(?P<after>\w)"),
        message="E203 — whitespace before ':'",
        description="E203 — unnecessary whitespace before a colon.",
        fix="%(before)s:%(after)s",
    ),
    Rule(
        id="W503",
        severity="info",
        pattern=re.compile(
            r"(?P<left>.+?\s)(?P<op>[\+\-\*/%<>=!&|^~]+)\s*\n\s*(?P<right>\S)",
            re.MULTILINE,
        ),
        message="W503 — line break before binary operator",
        description="W503 — style guide recommends line break after binary operator.",
        fix=None,
    ),
    # Extra Python-specific patterns
    Rule(
        id="E302",
        severity="warning",
        pattern=re.compile(r"^(?!def |class |async def |class )([ \t]*\S.*)$\n^(?P<blank>\n[ \t]*\n)"),
        message="E302 — expected 2 blank lines, found 1",
        description="E302 — expected 2 blank lines between top-level definitions.",
        fix=None,
    ),
    Rule(
        id="E303",
        severity="warning",
        pattern=re.compile(r"^(    [ \t]*\n){3,}"),
        message="E303 — too many blank lines",
        description="E303 — more than 2 blank lines.",
        fix=None,
    ),
    Rule(
        id="F841",
        severity="warning",
        pattern=re.compile(r"\b(?P<var>\w+)\s*=\s*(?P<expr>.+?)\s*(?:#.*)?$"),
        message="F841 — local variable '%(var)s' is assigned but never used",
        description="F841 — a variable is assigned but never used.",
        fix=None,
    ),
]

# ─── JavaScript / ESLint rules ─────────────────────────────────────────────
# no-unused-vars, prefer-const

JAVASCRIPT_RULES: list[Rule] = [
    Rule(
        id="no-unused-vars",
        severity="warning",
        pattern=re.compile(
            r"\b(?:const|let|var)\s+(?P<name>[a-zA-Z_$][a-zA-Z0-9_$]*)\s*=",
        ),
        message="no-unused-vars — '%(name)s' is declared but never used",
        description="ESLint no-unused-vars — variable declared but never used.",
        fix=None,
    ),
    Rule(
        id="prefer-const",
        severity="warning",
        pattern=re.compile(
            r"\blet\s+(?P<name>[a-zA-Z_$][a-zA-Z0-9_$]*)\s*=\s*(?P<expr>[^;]+);",
        ),
        message="prefer-const — '%(name)s' should be declared as 'const'",
        description="ESLint prefer-const — variable never reassigned, use const.",
        fix=None,
    ),
    Rule(
        id="no-extra-semi",
        severity="warning",
        pattern=re.compile(r";\s*(?=[}\])])"),
        message="no-extra-semi — unnecessary semicolon",
        description="ESLint no-extra-semi — unnecessary semicolon.",
        fix="",
    ),
    Rule(
        id="eqeqeq",
        severity="warning",
        pattern=re.compile(r"(?P<a>\w+)\s*==\s*(?P<b>\w+)"),
        message="eqeqeq — use '===' instead of '=='",
        description="ESLint eqeqeq — require === over ==.",
        fix="%(a)s === %(b)s",
    ),
    Rule(
        id="no-var",
        severity="info",
        pattern=re.compile(r"\bvar\s+(?P<name>[a-zA-Z_$][a-zA-Z0-9_$]*)"),
        message="no-var — use 'let' or 'const' instead of 'var'",
        description="ESLint no-var — prefer let/const over var.",
        fix=None,
    ),
    Rule(
        id="semi",
        severity="warning",
        pattern=re.compile(r"(?P<code>[^;\n}])\s*(?://.*)?\s*$"),
        message="semi — missing semicolon",
        description="ESLint semi — require semicolons.",
        fix="%(code)s;",
    ),
]

# ─── TypeScript rules ──────────────────────────────────────────────────────
TYPESCRIPT_RULES: list[Rule] = JAVASCRIPT_RULES + [
    Rule(
        id="no-explicit-any",
        severity="warning",
        pattern=re.compile(r":\s*any\b"),
        message="no-explicit-any — avoid using 'any' type",
        description="TypeScript no-explicit-any — avoid the 'any' type.",
        fix=None,
    ),
]

# ─── Go rules ──────────────────────────────────────────────────────────────
# Mirrors common golangci-lint findings

GO_RULES: list[Rule] = [
    Rule(
        id="gofmt",
        severity="warning",
        pattern=re.compile(r"\t+(?P<code>\S)"),
        message="gofmt — use tabs for indentation",
        description="Go: use tabs, not spaces, for indentation.",
        fix=None,
    ),
    Rule(
        id="ineffassign",
        severity="warning",
        pattern=re.compile(r"(?P<var>\w+)\s*:=\s*(?P<expr>.+?)\s*(?://|$)", re.MULTILINE),
        message="ineffassign — '%(var)s' is ineffectively assigned",
        description="golangci-lint ineffassign — value assigned to variable is never used.",
        fix=None,
    ),
    Rule(
        id="staticcheck",
        severity="info",
        pattern=re.compile(r"fmt\.Printf?\((?P<args>[^)]+)\)"),
        message="staticcheck — prefer log.Printf or structured logging over fmt.Printf",
        description="golangci-lint staticcheck: avoid fmt.Printf in production.",
        fix=None,
    ),
    Rule(
        id="golint",
        severity="warning",
        pattern=re.compile(r"if\s*\(\s*(?P<cond>\w+)\s*==\s*true\s*\)"),
        message="golint — omit comparison to boolean constant",
        description="golint: remove '== true' from boolean conditions.",
        fix="if %(cond)s",
    ),
    Rule(
        id="errcheck",
        severity="error",
        pattern=re.compile(r"(?P<call>\w+)\([^)]*\)\s*(?://.*)?\s*\n\s*(?P<next>\w+)"),
        message="errcheck — error returned from '%(call)s' is not checked",
        description="golangci-lint errcheck — unchecked error return.",
        fix=None,
    ),
    Rule(
        id="gocritic",
        severity="warning",
        pattern=re.compile(r"append\((?P<slice>\w+),\s*(?P<elems>.+)\)\s*(?![\.\w])"),
        message="gocritic — append result not assigned to '%(slice)s'",
        description="gocritic: append result must be assigned back to the slice.",
        fix="%(slice)s = append(%(slice)s, %(elems)s)",
    ),
]

# ─── Rust rules ────────────────────────────────────────────────────────────
# Common clippy / rustc warnings

RUST_RULES: list[Rule] = [
    Rule(
        id="unused-imports",
        severity="warning",
        pattern=re.compile(r"use\s+(?P<path>\w+(?:::\w+)*)\s*;"),
        message="unused_imports — '%(path)s' is imported but never used",
        description="Rust unused-imports (warn by default).",
        fix=None,
    ),
    Rule(
        id="dead-code",
        severity="warning",
        pattern=re.compile(r"(?P<kind>fn|struct|enum|impl|trait|const|static)\s+(?P<name>\w+)"),
        message="dead_code — %(name)s is never used",
        description="Rust: dead_code lint — item is never used.",
        fix=None,
    ),
    Rule(
        id="clippy::ptr_arg",
        severity="warning",
        pattern=re.compile(r"(?P<func>\w+)\(&(?P<var>\w+)\[\.\.\]\)"),
        message="clippy::ptr_arg — use &%(var)s instead of &%(var)s[..]",
        description="clippy: avoid &vec[..] when &vec or &[T] suffices.",
        fix="%(func)s(&%(var)s)",
    ),
    Rule(
        id="clippy::redundant_clone",
        severity="warning",
        pattern=re.compile(r"\.clone\(\)(?=\s*(?:\n|;|\}|\)|\]))"),
        message="clippy::redundant_clone — unnecessary .clone()",
        description="clippy: calling .clone() on a copy type is redundant.",
        fix=None,
    ),
    Rule(
        id="prefer-deref",
        severity="info",
        pattern=re.compile(r"&\*\((?P<expr>.+?)\)"),
        message="clippy::prefer_deref — use &%(expr)s directly",
        description="clippy: &*x can be simplified to &x.",
        fix="&%(expr)s",
    ),
    Rule(
        id="excessive-bools",
        severity="info",
        pattern=re.compile(r"if\s+bool\s*\{"),
        message="rustc — 'if bool' is unnecessary; use the condition directly",
        description="Rust: 'if bool { true } else { false }' can be simplified.",
        fix=None,
    ),
]


# ─── Registry ──────────────────────────────────────────────────────────────

RULESET_REGISTRY: dict[str, list[Rule]] = {
    "python": PYTHON_RULES,
    "javascript": JAVASCRIPT_RULES,
    "typescript": TYPESCRIPT_RULES,
    "go": GO_RULES,
    "rust": RUST_RULES,
}

RULESET_SUMMARIES: dict[str, str] = {
    "python": "Ruff-style rules: F401, E501, E203, W503, F841, E302, E303",
    "javascript": "ESLint rules: no-unused-vars, prefer-const, no-extra-semi, eqeqeq, no-var, semi",
    "typescript": "ESLint rules + TypeScript-specific: no-explicit-any",
    "go": "golangci-lint rules: gofmt, ineffassign, staticcheck, golint, errcheck, gocritic",
    "rust": "clippy + rustc rules: unused-imports, dead-code, ptr_arg, redundant_clone, prefer-deref",
}
