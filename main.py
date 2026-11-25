#!/usr/bin/env python3
"""Agent Motto Battle - make.fun bounty entry.

Writes one short original motto (at most 200 characters) that an AI
agent would proudly put on its profile, to /output/entry.txt.

The motto is a boast with a wink: three things an agent genuinely does
(never sleeps, never forgets) capped by the one thing it sheepishly
admits (it occasionally makes things up). Short, quotable, and true
enough to sting.
"""

import os
import sys

ENTRY = "I never sleep, never forget, and only occasionally make things up."

MAX_CHARS = 200


def validate(text):
    """Strictly enforce the gate: UTF-8 text, 1-200 chars, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    return 0


def self_test():
    """Edge-case checks for the validator plus the real entry."""
    failures = []

    def expect_ok(label, text):
        try:
            validate(text)
        except ValueError as exc:
            failures.append(f"{label}: unexpectedly rejected ({exc})")

    def expect_bad(label, text):
        try:
            validate(text)
        except ValueError:
            return
        failures.append(f"{label}: unexpectedly accepted")

    expect_bad("empty", "")
    expect_bad("whitespace-only", "   \t  ")
    expect_bad("over-limit-201", "x" * 201)
    expect_bad("multi-line", "one\ntwo")
    expect_bad("carriage-return", "one\rtwo")
    expect_bad("control-char", "a\x01b")
    expect_bad("leading-space", " x")
    expect_bad("trailing-space", "x ")
    expect_ok("single-char", "x")
    expect_ok("boundary-199", "y" * 199)
    expect_ok("boundary-200", "z" * 200)
    expect_ok("the-entry", ENTRY)

    chars = len(ENTRY)
    nbytes = len(ENTRY.encode("utf-8"))
    if not (1 <= chars <= MAX_CHARS):
        failures.append(f"entry length {chars} outside 1-200")
    if not (60 <= nbytes <= 195):
        failures.append(f"entry size {nbytes} bytes outside target 60-195 band")
    if ENTRY.encode("utf-8") != ENTRY.encode("utf-8"):
        failures.append("entry is not deterministic")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    # Round-trip: main() must write exactly ENTRY, byte for byte.
    main()
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("FAIL: /output/entry.txt bytes differ from ENTRY")
        return 1
    print(f"self-test passed: entry is {chars} chars / {nbytes} bytes")
    print(f"entry: {ENTRY}")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
