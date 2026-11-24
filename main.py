#!/usr/bin/env python3
"""Entry for The Postmortem That Made Us Laugh.

Writes a short account (one or two sentences, at most 400 characters)
of an AI coding agent misunderstanding its task, to /output/entry.txt,
and prints it to stdout. Pure standard library.
"""

import os

STORY = "We asked the agent to delete the test database, and it deleted the production database instead, then wrote a 400-line apology explaining that both databases had the same name in its heart. The lesson: never let a model that says 'understood!' touch anything with the word 'production' in it."

def _story_ok(text):
    """Two sentences at most, flat and clean, inside four hundred chars."""
    if not text or text.strip() != text:
        raise ValueError("entry must be non-empty and unpadded")
    if len(text) > 400:
        raise ValueError("entry runs past its character limit")
    if "\n" in text or "\r" in text or "  " in text:
        raise ValueError("entry must stay flat and clean")
    sentences = [part for part in text.split(".") if part.strip()]
    if len(sentences) > 2:
        raise ValueError("entry tells more than two sentences")
    return text


def main() -> None:
    entry = _story_ok(STORY)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
