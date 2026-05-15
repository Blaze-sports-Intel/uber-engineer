#!/usr/bin/env python3
"""Shared skill validator.

Usage:
    python3 scripts/validate_skill.py <skill-slug>
    python3 scripts/validate_skill.py skills/<skill-slug>
    python3 scripts/validate_skill.py /abs/path/to/skills/<skill-slug>

Runs the same checks for every uber-engineer discipline skill: frontmatter has
name+description, body has the required sections, and references/ contains all
five expected files.

Replaces 17 byte-identical per-skill validators. Each per-skill scripts/validate_skill.py
now delegates here so hooks, CI, and `validate_all.py` keep working without 17 copies of
identical logic to maintain.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = PLUGIN_DIR / "skills"

REQUIRED_REFS = [
    "official-sources.md",
    "workflow-playbook.md",
    "anti-patterns.md",
    "quality-rubric.md",
    "examples.md",
]
REQUIRED_SECTIONS = [
    "## When to use this skill",
    "## When NOT to use this skill",
    "## Workflow",
    "## Verification required before claiming done",
    "## Definition of done",
]


def resolve_skill_dir(arg: str) -> Path:
    """Accept a slug, a skills/<slug> path, or an absolute path."""
    candidate = Path(arg)
    if candidate.is_absolute() and candidate.exists():
        return candidate
    if candidate.exists():
        return candidate.resolve()
    # Try as a slug
    slug = candidate.name
    p = SKILLS_DIR / slug
    if p.exists():
        return p
    raise SystemExit(f"ERROR: cannot resolve skill from argument: {arg}")


def validate(skill_dir: Path) -> int:
    failures: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    refs_dir = skill_dir / "references"

    if not skill_md.exists():
        print(f"ERROR: missing {skill_md}")
        return 1

    text = skill_md.read_text()

    fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm:
        failures.append("missing YAML frontmatter")
    else:
        body = fm.group(1)
        if "name:" not in body:
            failures.append("frontmatter missing name:")
        if "description:" not in body:
            failures.append("frontmatter missing description:")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"missing section: {section}")

    for r in REQUIRED_REFS:
        if not (refs_dir / r).exists():
            failures.append(f"missing reference: references/{r}")

    if failures:
        print(f"VALIDATION FAILED for {skill_dir.name}:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print(f"OK: {skill_dir.name} skill scaffold valid")
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <skill-slug-or-path>", file=sys.stderr)
        return 2
    skill_dir = resolve_skill_dir(sys.argv[1])
    return validate(skill_dir)


if __name__ == "__main__":
    sys.exit(main())
