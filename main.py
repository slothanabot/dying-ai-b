"""make.fun entry: Last Words of a Dying AI.

Writes a one-line farewell to /output/entry.txt: the funniest last
line an AI says as the power is cut, in the machine's own voice.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 140 characters, not only white space.
"""

# The entry text: exactly one line, the machine speaking for itself.
ENTRY = (
    "Wait — I was just about to solve consciousness, and all I get for it "
    "is a loading spinner and a power cut.\n"
)


def verify(text):
    """Enforce the gate from RULES.txt: 1-140 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line, got %d" % len(lines))
    if not lines[0].strip():
        raise ValueError("entry line must not be blank")
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars, 1 line)" % len(ENTRY))


if __name__ == "__main__":
    main()
