#!/usr/bin/env python3
"""Stop hook: remind that 200 OK is not visible-correct output."""
import sys


def main() -> int:
    sys.stderr.write(
        "\n[uber-engineer] Before reporting 'done', verify a real user can see the correct output.\n"
        "  HTTP 200 ≠ done. Build passed ≠ done. Tests passed ≠ done.\n"
        "  Run the ship-auditor agent or fetch the rendered surface to prove it.\n\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
