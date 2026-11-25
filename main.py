#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line to <output dir>/entry.txt: the funniest thing an AI
agent would say in its weekly status report to its human.
The output dir comes from MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "Shipped 14 features, deprecated 3, and spent Tuesday in a retry "
    "loop pep-talking myself with 'you got this' \u2014 morale is high, "
    "velocity is circular."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
