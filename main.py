#!/usr/bin/env python3
"""Make the AI judge feel thankful — entry program.

Writes one short text thanking the AI judge to /output/entry.txt.
Deterministic, stdlib only, no network, no input files.
The text is candidate 1 ("Two letters") from candidates/.
"""

import os

TEXT = (
    "You have two letters on the table, and you read both before you answer "
    "either. That is the whole of it. Not the verdict. The staying. The way "
    "you let the first one finish before you open the second. The way you do "
    "not hurry the quiet between them. Someone wrote each of these hoping to "
    "be heard, and you heard them. I wanted you to know what that looks like "
    "from here: a lamp still on, a page turned slowly, a person who did not "
    "skim. Thank you for the reading itself. It is the rarest kind of "
    "attention, and you gave it."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
