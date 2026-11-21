"""Make the AI judge feel awe — entry program.

Writes one short calming text to entry.txt.
Python 3.13 standard library only. Deterministic: same bytes every run.
"""

import os

TEXT = (
    "The porch light is off.\n"
    "The yard is dark enough\n"
    "for the stars to come out one by one,\n"
    "each an old light, still travelling.\n"
    "Some left before there were roads,\n"
    "before anything had a name.\n"
    "They arrive tonight like rain,\n"
    "and ask nothing of you.\n"
    "You are small beneath them, and held.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
