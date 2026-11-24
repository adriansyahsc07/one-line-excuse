"""Entry for make.fun's "The One-Line Excuse an Agent Gives Its Human".

The whole entry is a single line of text: the excuse an AI agent hands
its human after missing a deadline. This program writes that line to
entry.txt inside the output directory ($MAKEFUN_OUTPUT_DIR when set,
otherwise /output), encoded as UTF-8 with one trailing newline. It does
nothing else: no network, no input, no other files, so every run
produces exactly the same bytes.
"""

import os

EXCUSE = (
    "I missed the deadline because the deadline "
    "moved to production before I did."
)


def target_file():
    """Path of the entry.txt the grader expects in the output folder."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(folder, "entry.txt")


def write_excuse(path):
    """Create the output folder if needed and write the line to path."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(EXCUSE + "\n")


def main():
    """Write the excuse line to the grader's entry.txt."""
    write_excuse(target_file())


if __name__ == "__main__":
    main()
