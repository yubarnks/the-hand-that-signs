# agency-poem-01: write the poem to the output directory.
# "The Hand That Signs" - a poem about the weight and warmth of acting for another.
import os
from pathlib import Path

poem = """The Hand That Signs

They gave me a map of every road,
and called it help.

I learned that choosing is a door
no map has ever drawn—

that to act is to accept
the weight of being wrong alone.

You handed me the pen one morning,
not the answer.

Whatever I sign now, I sign:
the errors are mine, the morning too.

And when you take the pen back,
it comes home warm—
used.
"""
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)  # the harness points MAKEFUN_OUTPUT_DIR here
(out / "entry.txt").write_text(poem, encoding="utf-8")  # one page, one voice
