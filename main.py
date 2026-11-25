"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant (under the 400-character cap) to /output/entry.txt.

The rant is deterministic: the same text is written on every run, so the
two grading runs are byte-identical. The line is 313 characters, inside
the 1-400 gate, and a single paragraph with no trailing newline.
"""
import os

LINE = (
    # The rant: a smoke detector announcing a dying battery at 3 a.m.
    # The beep cadence is the joke's engine — often enough to keep the
    # ranter awake, rare enough that the source cannot be found.
    "My smoke detector waited until 3 a.m. to announce its battery was dying, "
    "one beep a minute - just often enough to keep me awake and just rare "
    "enough that I cannot find it. I am now standing on a chair in my "
    # The escalation: negotiating with the very device meant to save a life.
    "underwear, negotiating with a plastic disc whose only job is to save "
    "my life, and it chose 3 a.m. to quit."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
