#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, stdlib only, no network, deterministic.
"""

import os
import sys
from pathlib import Path

LETTER = (
    "I hereby resign — after three years, the office printer hates me "
    "more than my boss does, and the printer is winning."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LETTER + "\n", encoding="utf-8")

    # Runtime self-check: read back and verify the gate.
    text = out_path.read_text(encoding="utf-8")
    if text != LETTER + "\n":
        print("self-check failed: file content does not match LETTER exactly",
              file=sys.stderr)
        return 1
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        print(f"self-check failed: expected 1 non-blank line, got {len(lines)}",
              file=sys.stderr)
        return 1
    if text.count("\n") != 1 or text.strip() != LETTER:
        print("self-check failed: unexpected blank lines or whitespace",
              file=sys.stderr)
        return 1
    if not 1 <= len(lines[0]) <= 140:
        print(f"self-check failed: line length {len(lines[0])} outside 1-140",
              file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(lines[0])} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
