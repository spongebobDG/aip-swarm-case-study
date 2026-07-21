"""Fail when a local Markdown link points to a missing file."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []
    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_text = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path_text:
                continue
            resolved = (markdown.parent / path_text).resolve()
            if not resolved.exists():
                failures.append(f"{markdown.relative_to(ROOT)} -> {target}")

    if failures:
        print("Broken local Markdown links:")
        print("\n".join(f"- {item}" for item in failures))
        return 1
    print("All local Markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
