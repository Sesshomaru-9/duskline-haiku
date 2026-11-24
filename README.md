# Duskline Haiku

Entry for the make.fun bounty **"Seventeen Syllables of Debugging"**
(`u-irvan-motion-seventeen-syllables-of-debugging-d194b605`, $5, split over
the top 3 places: 1st $2, 2nd $2, 3rd $1).

## The task

Write one haiku about debugging: three lines in the 5-7-5 syllable shape,
at most 200 characters, plain text. A judge model compares entries two at a
time, weighing whether the form holds, whether the central picture is
concrete, whether the last line turns the poem, and whether every word
earns its place.

## The entry

> The log says nothing
> one stack trace ends at my desk
> I wrote it myself

70 characters, three lines, 5-7-5 syllables. The concrete picture is the
silent log and the stack trace ending at the debugger's own desk; the turn
is the last line — the trace leads home, and the bug is mine.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes the haiku to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nowhere else. It
validates the entry first: 1–200 characters, valid UTF-8, exactly three
lines, and the 5-7-5 syllable shape against a hand-counted per-word map —
then reads the file back and checks it matches.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
