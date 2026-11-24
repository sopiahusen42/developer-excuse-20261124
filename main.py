#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI Judge Laugh: Developer Excuses".

Writes one single-line developer excuse (at most 200 characters) to entry.txt
in UTF-8. The output is deterministic: no clock reads, no randomness, no
network, standard library only, so every run produces identical bytes.
"""

import os
import sys

ENTRY = "I renamed one variable and the whole service resigned in protest. I've emailed it an apology."

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MAX_CODE_POINTS = 200


def validate_entry(text):
    """Return an error string if text is not a valid entry, else None."""
    if not isinstance(text, str):
        return "not a string"
    if text.strip() == "":
        return "blank"
    if not (1 <= len(text) <= MAX_CODE_POINTS):
        return "length " + str(len(text)) + " outside 1..200"
    if "\n" in text or "\r" in text:
        return "contains a line break"
    if text != text.strip():
        return "leading or trailing whitespace"
    return None


def main():
    problem = validate_entry(ENTRY)

    if problem is not None:
        print("entry rejected: " + problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)

    expected = (ENTRY + chr(10)).encode("utf-8")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY + chr(10))

    with open(path, "rb") as handle:
        actual = handle.read()

    if actual != expected:
        print("write verification failed", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
