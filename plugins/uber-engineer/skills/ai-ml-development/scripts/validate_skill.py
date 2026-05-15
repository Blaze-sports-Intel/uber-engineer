#!/usr/bin/env python3
"""Validate the ai-ml-development skill scaffold.

Checks frontmatter, references, and required sections. Used by the post-write hook
and as a CI gate.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"
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


def main() -> int:
    failures = []
    if not SKILL_MD.exists():
        print(f"ERROR: missing {SKILL_MD}")
        return 1

    text = SKILL_MD.read_text()

    # frontmatter
    fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm:
        failures.append("missing YAML frontmatter")
    else:
        body = fm.group(1)
        if "name:" not in body:
            failures.append("frontmatter missing name:")
        if "description:" not in body:
            failures.append("frontmatter missing description:")

    # required sections
    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"missing section: {section}")

    # references
    refs_dir = SKILL_DIR / "references"
    for r in REQUIRED_REFS:
        if not (refs_dir / r).exists():
            failures.append(f"missing reference: references/{r}")

    if failures:
        print(f"VALIDATION FAILED for {SKILL_DIR.name}:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print(f"OK: ai-ml-development skill scaffold valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
