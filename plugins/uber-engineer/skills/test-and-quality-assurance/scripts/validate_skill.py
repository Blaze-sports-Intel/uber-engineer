#!/usr/bin/env python3
"""Per-skill validator delegate.

This is a thin wrapper around the plugin-level shared validator at
`scripts/validate_skill.py`. Kept here so the skill structure documented in
SKILL.md (Scripts section) stays accurate while the actual validation logic
lives in one place. Invoking this file is equivalent to invoking the shared
validator with this skill's slug.
"""
from __future__ import annotations

import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SHARED = SKILL_DIR.parent.parent / "scripts" / "validate_skill.py"

if not SHARED.exists():
    print(f"ERROR: shared validator missing at {SHARED}", file=sys.stderr)
    sys.exit(1)

import runpy
sys.argv = [str(SHARED), str(SKILL_DIR)]
runpy.run_path(str(SHARED), run_name="__main__")
