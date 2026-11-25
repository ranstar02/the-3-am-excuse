#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line (the wallet's own excuse) to /output/entry.txt.
Stdlib only, no network, no randomness, no clock: fully deterministic.
"""

import os

# The excuse, in the wallet's own voice: it keeps a grudge about every
# 3 AM signature that turned into a morning regret, and tonight it is
# on strike until sunrise.
EXCUSE = (
    "3 AM again? Last time I signed at this hour you bought a frog coin "
    "and cried for a week. I'm not lighting up till sunrise."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, (
        f"excuse must be 1-200 characters, got {len(EXCUSE)}"
    )
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: exactly one line, exactly the excuse.
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
