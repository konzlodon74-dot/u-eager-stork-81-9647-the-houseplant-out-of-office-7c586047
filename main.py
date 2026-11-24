#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if sent by the office fern,
to /output/entry.txt. The line is at most 120 characters, a single
line, and not only whitespace -- the gate the sealed scorer checks.
"""

import os
import sys

LINE = "Out of office: I'm the fern by the window, unwatered since March. Your email has been composted. — The Plant"

MAX_CHARS = 120


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: entry line is {len(line)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what the grader reads must be exactly this line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: written entry does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
