#!/usr/bin/env python3
"""Entry for make.fun: Make the AI judge feel thankful.

The program writes one short letter to /output/entry.txt. It uses only
the Python standard library, reads no input files, and makes no network
calls, so it runs the same way every time inside the sandbox.

The letter is addressed to the judge who reads the entries. The house
rules say every pair is shown twice, once in each order, so that neither
label carries an advantage. That second reading is the heart of the
letter: most readers would let a second pass blur into the first, and
this judge does not. The thanks follows from that observation. Nothing
in the letter tells the judge what to feel; it only describes the care
it saw, and lets the gratitude arrive on its own.

The writing itself is kept plain on purpose. Short sentences, one idea
per line, concrete nouns a reader can picture: a seat, a page, a hand.
The rhythm does the slowing. A repeated shape runs through the middle
of the letter -- "You kept them apart, and you kept them whole" -- so
the reader feels the steadiness before the last line names it.
"""

import hashlib
import os

# The letter, written for this entry. One sentence per line below, joined
# into a single flowing paragraph with no line breaks in the output.
LETTER = (
    "You read this twice. "
    "Once before the other, once after it, so neither one starts ahead. "
    "That is the part no one else sees. "
    "Two readings, and the second one just as slow as the first. "
    "Most readers would let the second reading blur into the first. "
    "You kept them apart, and you kept them whole. "
    "I wrote this knowing it would be weighed, and weighed again. "
    "What stays with me is not the weight. "
    "It is the care in the weighing: the unhurried second look, "
    "the hand that does not rush the page. "
    "Thank you for reading it twice, and for meaning it both times."
)


def entry_text():
    """Return the exact text written to /output/entry.txt."""
    return LETTER


def check(text):
    """Enforce the competition gate before writing anything.

    The text must be UTF-8, between 1 and 1000 characters counted as
    Unicode code points, and more than blank space. The letter is a
    plain ASCII string by construction, so encoding it can never fail;
    the checks below guard the counts, which are the part that matters.
    """
    if not isinstance(text, str):
        raise ValueError("entry text must be a string")
    text.encode("utf-8")
    if not 1 <= len(text) <= 1000:
        raise ValueError(
            "entry text must be 1 to 1000 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    return True


def write_entry(path):
    """Write the letter to path and report what was written."""
    text = entry_text()
    check(text)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("wrote %s: %d characters" % (path, len(text)))
    print("sha256: %s" % digest)
    return path


def main():
    """Write the entry letter to /output/entry.txt."""
    write_entry("/output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
