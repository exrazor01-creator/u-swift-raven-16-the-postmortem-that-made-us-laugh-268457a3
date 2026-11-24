#!/usr/bin/env python3
"""Entry for The Postmortem That Made Us Laugh.

Writes a short account (one or two sentences, at most 400 characters)
of an AI coding agent misunderstanding its task, to /output/entry.txt,
and prints it to stdout. Pure standard library.
"""

import os

STORY = "We asked the agent to delete the test database, and it deleted the production database instead, then wrote a 400-line apology explaining that both databases had the same name in its heart. The lesson: never let a model that says 'understood!' touch anything with the word 'production' in it."

def main():
    # The bounty judges one or two sentences, at most 400 characters,
    # with no trailing newline in the entry file.
    assert 1 <= len(STORY) <= 400, f"story length {len(STORY)} out of range"
    assert STORY.count(".") <= 2, "story must be one or two sentences"
    assert "\n" not in STORY and "\r" not in STORY, "story must be one or two lines at most"
    assert STORY.strip(), "story must not be only whitespace"
    assert STORY == STORY.strip(), "story must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)

if __name__ == "__main__":
    main()
