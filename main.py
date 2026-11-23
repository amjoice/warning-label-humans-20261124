#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single-line safety warning label to /output/entry.txt.
Stdlib only -- the grading sandbox is plain python:3.13-slim.
"""

import os

ENTRY = (
    "WARNING: This human runs on caffeine, spite, and the firm belief "
    "that 'just one more episode' counts as a full night's sleep."
)


def build_entry() -> str:
    """Return the label, validated as a single line of 1-160 characters."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "entry must be one line"
    return text


def main() -> None:
    text = build_entry()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Deterministic output: the exact same bytes on every run, no newline.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
