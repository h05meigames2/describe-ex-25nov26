"""Describe Your Ex in One Word — make.fun entry.

The word: "deprecated".

In software, a deprecated feature still exists, but it is no longer
supported, no longer maintained, and everyone is warned to stop using
it. That is exactly what an ex is: technically still in the world,
officially out of support, and every future release notes say
"do not use".
"""

import os

# The one-word verdict on an ex.
WORD = "deprecated"


def main() -> None:
    # Guard: the entry must be exactly one word, 1-111 chars, no spaces.
    assert 1 <= len(WORD) <= 111, "word must be 1-111 chars"
    assert WORD.split() == [WORD], "word must be a single word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote {WORD!r} ({len(WORD)} chars) to /output/entry.txt")


if __name__ == "__main__":
    main()
