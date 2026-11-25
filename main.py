"""Unsent: The Micro-Confession Sprint — make.fun entry.

The entry (exactly two parts, 136 characters total, no trailing newline):

    To: my mum
    I still keep your last text from the night before your operation unread,
    because opening it would mean admitting you're gone.

Why this confession, against the judge brief (criteria in the brief's order):

1. Two parts, nothing else: a "To:" line naming who it was meant for (a
   relationship, "my mum" — no full name, no handle) and the unsent message
   itself, one line, with no explanation after it.
2. The reason it stayed in drafts is felt in the words, not stated: it is
   too late. She is gone, so the message can never be sent or answered, and
   the draft is the only form it can still exist in. The specific, concrete
   detail does the work — keeping her last text unread so it never says
   "seen" — instead of any general statement about grief or regret.
3. The To: line and the message need each other: "your last text", "the
   night before your operation" and "you're gone" only make sense addressed
   to a mother who died after surgery. Swap in any other addressee and the
   confession breaks.
4. It reads as typed and never sent, not written to be sent: nobody writes
   this to be read. It is a draft kept, not a message composed — no joke,
   no greeting, no motivational line, no cleverness for its own sake.
5. One line, written exactly as typed, with no explanation after it.

The entry is original: it is not copied from any existing text.
"""

import os

TO_LINE = "To: my mum"

MESSAGE = (
    "I still keep your last text from the night before your operation "
    "unread, because opening it would mean admitting you're gone."
)

ENTRY = TO_LINE + "\n" + MESSAGE


def main() -> None:
    # Gate, from RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 260
    # characters, and the judge brief caps the message itself at 200
    # characters, one line, with no explanation after it.
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly a To: line and one message line"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert 1 <= len(ENTRY) <= 260, "entry must be 1 to 260 characters"
    assert len(lines[1]) <= 200, "message must be at most 200 characters"
    assert not ENTRY.endswith("\n"), "no trailing newline"

    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
