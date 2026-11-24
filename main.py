#!/usr/bin/env python3
"""Ship It Friday — make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes the one-line entry — the funniest git commit message an AI coding
agent writes right before breaking production on a Friday — to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = "ship it: Friday deploy, no tests, no fear, no rollback plan, just vibes and root access"

assert 1 <= len(ENTRY) <= 159, "entry length %d out of range" % len(ENTRY)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
