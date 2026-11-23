#!/usr/bin/env python3
"""make.fun entry: The Vacuum's Alibi: One Line, 200 Characters.

Writes the entry text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Python standard library only — no network, no
randomness, no timestamps. Running twice produces byte-identical output.

Bounty: https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7
Constraint: one line, at most 200 characters
"""

import hashlib
import os
import sys

ENTRY = "Log 482: the crumb under the sofa filed for squatter's rights, so I left it. I respect the law."

LIMIT_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    if LIMIT_CHARS is not None and len(ENTRY) > LIMIT_CHARS:
        print(f"FAIL: entry is {len(ENTRY)} chars, limit is {LIMIT_CHARS}",
              file=sys.stderr)
        return 1
    with open(out_path, "wb") as f:
        f.write(data)
    print(out_path)
    print("chars:", len(ENTRY))
    print("sha256:", hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
