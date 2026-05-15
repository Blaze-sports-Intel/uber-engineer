#!/usr/bin/env python3
"""PostToolUse reminder: did the agent handle loading, error, empty, populated?

Non-blocking. Prints a reminder when a Write or Edit touches a likely UI/data surface.
"""
import json
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    file_path = payload.get("tool_input", {}).get("file_path", "")
    UI_HINTS = (".tsx", ".jsx", ".vue", ".svelte", ".astro", ".swift", ".kt")
    if not any(file_path.endswith(ext) for ext in UI_HINTS):
        return 0

    sys.stderr.write(
        "\n[uber-engineer] Reminder: every data surface needs loading + error + empty + populated states.\n"
        "  Build success ≠ done. 200 OK ≠ done. A real user seeing correct output = done.\n\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
