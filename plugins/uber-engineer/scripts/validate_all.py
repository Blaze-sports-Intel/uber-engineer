#!/usr/bin/env python3
"""Run every per-skill validate_skill.py and report.

Used by CI and the local pre-commit hook.
"""
import subprocess
import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = PLUGIN_DIR / "skills"

DISCIPLINES = [
    'frontend-development',
    'backend-development',
    'full-stack-development',
    'mobile-development',
    'game-development',
    'devops-and-infrastructure',
    'api-development',
    'database-development',
    'embedded-systems-development',
    'cloud-development',
    'ai-ml-development',
    'blockchain-development',
    'test-and-quality-assurance',
    'security-development',
    'ar-vr-development',
    'data-science-development',
    'web-development',
]


def main() -> int:
    failed = []
    for slug in DISCIPLINES:
        script = SKILLS_DIR / slug / "scripts" / "validate_skill.py"
        if not script.exists():
            failed.append(f"{slug}: missing validate_skill.py")
            continue
        rc = subprocess.run([sys.executable, str(script)]).returncode
        if rc != 0:
            failed.append(f"{slug}: validate_skill.py rc={rc}")

    if failed:
        print("FAIL:")
        for f in failed:
            print(f"  - {f}")
        return 1

    print(f"OK: all {len(DISCIPLINES)} skill scaffolds valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
