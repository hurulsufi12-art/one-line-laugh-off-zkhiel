"""One-Line Laugh-Off entry: write one joke to /output/entry.txt.

Stdlib only. Deterministic: no randomness, no clock, no network, no
model calls, no file reads. The joke is a constant; the program just
writes it, after checking it against the sealed gate (RULES.txt):
1-200 characters, not whitespace-only, single line.
"""

import os

JOKE = "I asked my AI assistant to lie to my boss. It agreed, then CC'd him the transcript."

OUTPUT_PATH = "/output/entry.txt"


def is_valid(text):
    """Mirror of the sealed gate: 1-200 chars, not whitespace-only."""
    return isinstance(text, str) and 1 <= len(text) <= 200 and text.strip() != ""


def write_entry(path):
    """Write JOKE to path as UTF-8, no trailing newline."""
    if not is_valid(JOKE):
        raise ValueError("JOKE fails the gate: 1-200 non-whitespace characters")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("JOKE must be a single line")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


def main():
    write_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
