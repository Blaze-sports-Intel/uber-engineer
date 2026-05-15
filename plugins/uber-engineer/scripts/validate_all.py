#!/usr/bin/env python3
"""Validate every discipline skill in this plugin.

Discovers skills by walking `skills/` instead of carrying a hardcoded list, so
adding or removing a discipline doesn't require touching this file. Calls into
the shared validator at `scripts/validate_skill.py` for each discovered skill.

Used by CI and the local pre-commit hook.
"""
from __future__ import annotations

import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = PLUGIN_DIR / "skills"

sys.path.insert(0, str(PLUGIN_DIR / "scripts"))
import validate_skill  # noqa: E402


def discover_skills() -> list[Path]:
    if not SKILLS_DIR.exists():
        return []
    return sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists())


def main() -> int:
    skills = discover_skills()
    if not skills:
        print(f"ERROR: no skills found under {SKILLS_DIR}", file=sys.stderr)
        return 1

    failed = []
    for skill_dir in skills:
        rc = validate_skill.validate(skill_dir)
        if rc != 0:
            failed.append(skill_dir.name)

    if failed:
        print("\nFAIL:")
        for slug in failed:
            print(f"  - {slug}")
        return 1

    print(f"\nOK: all {len(skills)} skill scaffolds valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
