#!/usr/bin/env python3
"""PreToolUse guard: block destructive bash commands without explicit user confirm.

Non-blocking when the command contains the literal allow-comment `# uber-engineer:allow`.
Otherwise blocks and emits a structured reason.
"""
import json
import sys


DANGEROUS_PATTERNS = [
    "rm -rf /",
    "rm -rf ~",
    "rm -rf $HOME",
    "DROP TABLE",
    "DROP DATABASE",
    "TRUNCATE",
    "git push --force",
    "git push -f",
    "git reset --hard origin",
]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    cmd = payload.get("tool_input", {}).get("command", "")
    if "# uber-engineer:allow" in cmd:
        return 0

    for pat in DANGEROUS_PATTERNS:
        if pat in cmd:
            sys.stderr.write(
                f"\n[uber-engineer] BLOCKED destructive command: {pat!r} detected.\n"
                f"  Command: {cmd}\n"
                f"  If intentional, append `# uber-engineer:allow` and rerun.\n\n"
            )
            return 2  # block

    return 0


if __name__ == "__main__":
    sys.exit(main())
