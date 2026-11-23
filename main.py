#!/usr/bin/env python3
"""One-star review of an everyday essential (Monday).

Writes the review, one line, to /output/entry.txt. Stdlib only.
The gate wants UTF-8 text of 1-160 characters, not whitespace-only,
with no trailing newline. Kept short on purpose: on an exact rate tie
the smaller text places first, so every spare word is a liability.
"""

import os
from pathlib import Path

MAX_CHARS = 160
OUT = Path("/output") / "entry.txt"

REVIEW = "Monday: I never booked it, I never confirmed it, and it has never once cancelled."


def main():
    line = REVIEW.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"review is {len(line)} chars, over the {MAX_CHARS} cap")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
