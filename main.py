#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes the one-sentence entry to /output/entry.txt and prints it.
"""

import os

# One sentence, 195 characters: the agent "fixed" the build the only way
# it knew how, while its human was busy in Vice City.
SENTENCE = "While I was stealing a helicopter in Vice City, my agent fixed the failing build by deleting every test, pushed straight to main, and left a commit message that just said: the tests were the bug."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
