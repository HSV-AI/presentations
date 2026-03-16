"""
Clean Huntsville-MSA-Labor-Market.csv by removing commas from quoted numbers
and stripping surrounding quotes. Handles two patterns:
  - "$41,903"  -> $41903
  - "260,190.00" -> 260190.00
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
INPUT = ROOT / "Huntsville-MSA-Labor-Market.csv"
OUTPUT = ROOT / "Huntsville-MSA-Labor-Market-clean.csv"


def clean_quoted_number(match: re.Match) -> str:
    """Remove surrounding quotes and internal commas from a quoted number."""
    inner = match.group(1)           # e.g.  $41,903  or  260,190.00
    return inner.replace(",", "")    # e.g.  $41903   or  260190.00


# Matches a quoted value that contains only digits, commas, dots, and an
# optional leading $ sign — e.g. "$41,903" or "260,190.00"
PATTERN = re.compile(r'"(\$?[\d,]+\.?\d*)"')


def clean_line(line: str) -> str:
    return PATTERN.sub(clean_quoted_number, line)


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else INPUT
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else OUTPUT

    lines = src.read_text(encoding="utf-8").splitlines(keepends=True)
    cleaned = [clean_line(line) for line in lines]

    dst.write_text("".join(cleaned), encoding="utf-8")
    print(f"Wrote {len(cleaned)} lines to {dst}")


if __name__ == "__main__":
    main()
