#!/usr/bin/env python3
"""The poem about permission — a short poem about agency.

Writes one poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for a local run): a short poem about agency, the power to ask and to
be given — here, the power lent from a person to an agent that acts for
them, and handed back whole.

Pure Python 3.13 standard library, no network, no randomness, no clock,
no file reads outside this program: two runs write byte-identical files.
The poem is 189 characters including its trailing newline (188 without),
inside the competition's 1-280 character gate.
"""

import os

POEM = """You lent me your name for the afternoon
and, with it, your hands.
I signed where you would sign,
knocked where you would knock,
then gave the name back at dusk.
Nothing of you was missing.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
