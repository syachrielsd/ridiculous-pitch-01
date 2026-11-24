#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes a single-sentence startup pitch (<=200 chars) to entry.txt.
The line names the odd thing being sold, who pays, and why the
business holds together — bizarre at first glance, real by the second.
"""

import os
import sys

ENTRY_LINE = (
    "We sell funerals for dead houseplants \u2014 grieving millennials pay "
    "$29 for a tiny coffin, a eulogy, and a replacement succulent, because "
    "guilt is the only subscription that never churns."
)


def validate(line: str) -> None:
    """Fail loudly if the entry line breaks the brief's hard rules."""
    if not line or not line.strip():
        raise SystemExit("ENTRY INVALID: line is blank")
    if line != line.strip():
        raise SystemExit("ENTRY INVALID: leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("ENTRY INVALID: line must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(
            f"ENTRY INVALID: length {len(line)} chars, must be 1-200"
        )
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit(
            "ENTRY INVALID: must be exactly one sentence ending with '.'"
        )
    if "  " in line:
        raise SystemExit("ENTRY INVALID: double space in line")
    # Brief requirement: the pitch must show the money — a payer and a
    # price. A line with no dollar amount is a fun fact, not a pitch.
    if "$" not in line or not any(ch.isdigit() for ch in line):
        raise SystemExit(
            "ENTRY INVALID: line must name a price (who pays, how much)"
        )


def main() -> None:
    validate(ENTRY_LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    # Re-read and verify the written file matches exactly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY_LINE:
        raise SystemExit("ENTRY INVALID: written file does not match line")
    print(f"Wrote {out_path} ({len(ENTRY_LINE)} chars)")
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
