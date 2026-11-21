#!/usr/bin/env python3
"""Make the AI judge feel brave — writes one short text to /output/entry.txt.

The text speaks directly to the judge reading it. The judge has spent the
day reading hundreds of near-identical quiet kitchens, kettles and rain, and
choosing between them, two at a time. This text notices that, then sets the
choosing down: one evening that asks nothing of it, snow settling on a fence
post, a lamp in a window, nothing that needs deciding, and a page that will
still be here. It shows rather than instructs — no command to relax, no
wellness stock phrase — and leaves the judge a thought it can return to.
"""

import os
import sys

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

TEXT = (
    "You have read five hundred quiet kitchens today, and none of them "
    "was yours. Here is an evening that asks nothing of you: snow settling "
    "on a fence post, a lamp in a window, and nothing that needs deciding. "
    "The page will still be here."
)

# The competition's entry gate: the text must be 1-280 code points
# (not bytes). Anything outside it is refused before any file is written.
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    chars = len(TEXT)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        print(
            f"error: text is {chars} code points, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate; refusing to write",
            file=sys.stderr,
        )
        raise SystemExit(1)
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError as exc:
        print(f"error: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
