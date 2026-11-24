#!/usr/bin/env python3
"""Duskline Haiku — make.fun entry for
"Seventeen Syllables of Debugging"
(u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

Writes one haiku (5-7-5 syllables, at most 200 characters) about debugging
to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only, deterministic, no network.
Writes ONLY to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback "out" for local
testing); never writes into the repository directory.
"""

import os
import sys

HAIKU = (
    "The log says nothing\n"
    "one stack trace ends at my desk\n"
    "I wrote it myself"
)

MAX_CHARS = 200
EXPECTED_SYLLABLES = (5, 7, 5)

# Hand-counted syllables for every word in the haiku.
SYLLABLES = {
    "the": 1, "log": 1, "says": 1, "nothing": 2,
    "one": 1, "stack": 1, "trace": 1, "ends": 1, "at": 1,
    "my": 1, "desk": 1,
    "i": 1, "wrote": 1, "it": 1, "myself": 2,
}


def _syllables(line: str) -> int:
    total = 0
    for word in line.split():
        key = word.strip(".,!?;:").lower()
        if key not in SYLLABLES:
            raise ValueError(f"no syllable count for word: {word!r}")
        total += SYLLABLES[key]
    return total


def _validate_entry(text: str) -> None:
    """Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 200
    characters, not only whitespace; plus the 5-7-5 haiku shape."""
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    text.encode("utf-8")  # raises if not valid UTF-8
    lines = text.split("\n")
    assert len(lines) == 3, f"entry must be exactly 3 lines, got {len(lines)}"
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = _syllables(line)
        assert got == expected, (
            f"line {line!r} has {got} syllables, expected {expected}"
        )


def main() -> int:
    _validate_entry(HAIKU)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Verify what was actually written matches the validated text.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    _validate_entry(written)
    assert written == HAIKU, "written entry differs from HAIKU"
    print(f"wrote {path} ({len(HAIKU)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
