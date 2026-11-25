"""One Word, First Thought — entry writer.

Writes the single submitted word to /output/entry.txt,
UTF-8, with no trailing newline. Reads the file back and
verifies it matches the entry byte for byte, failing loudly
on any mismatch, so a bad write can never pass silently.
"""

import os
import sys

ENTRY = "Mooncrumb"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    expected = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(expected)
    with open("/output/entry.txt", "rb") as f:
        actual = f.read()
    if actual != expected:
        print(
            f"verification failed: wrote {expected!r}, read back {actual!r}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
