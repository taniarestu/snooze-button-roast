#!/usr/bin/env python3
"""Snooze Button Roast entry for make.fun.

Writes one single-line roast of an alarm clock ringing at 6 AM on a
Saturday to /output/entry.txt. Python 3 standard library only,
deterministic, no network access.
"""

import os

ENTRY = "At 6 AM on a Saturday, my alarm clock rang like Monday had paid it overtime to ruin my only day off."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 200 characters, not only white space, on a
    # single line. Refuse to write anything that would fail the gate.
    assert isinstance(ENTRY, str), "entry must be a string"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing white space"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    ENTRY.encode("utf-8")  # raises if the entry is not valid UTF-8
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Post-write check: what landed on disk must be exactly the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 200 and written.strip()
    assert "\n" not in written and "\r" not in written


if __name__ == "__main__":
    main()
