"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply (at most 120 characters)
to /output/entry.txt, written as if a houseplant sent it:
the fern ignored since March, thriving on spite alone.
The plant's own life drives the joke — months without water,
not an office cliche — and the punch lands on the last words.
"""

import os

ENTRY = (
    "Out of office. I have not been watered since March "
    "and I am thriving on spite alone."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
