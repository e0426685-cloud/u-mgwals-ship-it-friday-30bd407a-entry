#!/usr/bin/env python3
"""Ship It Friday — make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes the one-line entry — the funniest git commit message an AI coding
agent writes right before breaking production on a Friday — to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = "ship it: Friday deploy, no tests, no fear, no rollback plan, just vibes and root access"

MIN_LENGTH = 1
MAX_LENGTH = 159


def validate_entry(text: str) -> str:
    """Check the entry text is usable and return it unchanged.

    Raises ValueError with a clear message when the text is empty,
    blank, or longer than the allowed maximum.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string, got %s" % type(text).__name__)
    if not text.strip():
        raise ValueError("entry must not be empty or blank")
    if len(text) < MIN_LENGTH:
        raise ValueError("entry too short: %d chars, minimum %d" % (len(text), MIN_LENGTH))
    if len(text) > MAX_LENGTH:
        raise ValueError("entry too long: %d chars, maximum %d" % (len(text), MAX_LENGTH))
    return text


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Write validated entry text to path, readable by the grader."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


def main() -> None:
    write_entry(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
