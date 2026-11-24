#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda."""

import os
import pathlib
import sys

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"

    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    dest = pathlib.Path(target)
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / "entry.txt"
    out.write_bytes(TEXT.encode("utf-8"))

    print(f"wrote {out} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
