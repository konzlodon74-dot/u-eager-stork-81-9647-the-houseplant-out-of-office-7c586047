#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Prints one out-of-office auto-reply, written as if by the office fern,
and (when run inside the make.fun sandbox) writes the same text to
/output/entry.txt, where the gate scorer reads it.
"""

import os

LINE = (
    "Out of office: I'm the fern. No water since March. "
    "If I reply, it's a miracle. If I don't, I've composted myself."
)


def main() -> None:
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        # No writable /output outside the grading sandbox; stdout is the entry.
        pass


if __name__ == "__main__":
    main()
