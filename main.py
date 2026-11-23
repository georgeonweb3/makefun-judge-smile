#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes one line (1-200 UTF-8 chars) about a small good thing that happened
today to /output/entry.txt. Deterministic, no network, no randomness.
"""

import os
import sys

# Draft candidates (warm + surprising + one concrete detail + fresh wording):
# 1. "A stranger pressed a warm meat pie into my hand at the bus stop and
#    said, 'You look like you missed breakfast.'"  (warm, concrete, but the
#    bus-stop kindness angle is already covered by rival entries)
# 2. "My neighbour's little boy knocked with half his own mango and said,
#    'Mummy says share, or it won't be sweet.'"  (sweet, but a rival already
#    entered a mango line)
# Extra-mile tightening pass: the em dash sharpens the surprise turn — the
# street's noisy cheer, then the quiet kindness. "before his own" is the
# concrete detail that makes the warmth land.
ENTRY = "The lights came back at 2 a.m., the whole street cheered — and my neighbour plugged in my phone before his own."


def main() -> int:
    text = ENTRY.strip()
    if not text or text != ENTRY:
        print("entry must be a single non-empty line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry too long: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be one line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
