#!/usr/bin/env python3
"""Write one funny line about office life to /output/entry.txt.

The line is written exactly as given: 123 Unicode code points,
inside the competition gate of 1-199.
Python 3, standard library only, no network.
"""

import os

TEXT = "The printer jammed five minutes before the board meeting, and the CEO called it the most reliable employee in the building."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 199, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
