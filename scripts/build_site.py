#!/usr/bin/env python3
"""Copy the repo's public content into .site-docs/ so MkDocs can build the GitHub Pages site.

Standard library only. Run from anywhere:  python3 scripts/build_site.py && mkdocs build
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".site-docs"
SKIP_DIRS = {".git", ".github", ".private", ".claude", ".claude-plugin", ".site-docs", "_site", "__pycache__",
             "node_modules", "raw"}
SKIP_FILES = {"CLAUDE.md", "AGENTS.md", "mkdocs.yml"}
KEEP_EXT = {".md", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".csv", ".py", ".json", ".txt"}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    count = 0
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts) or not path.is_file():
            continue
        if path.name in SKIP_FILES or path.suffix.lower() not in KEEP_EXT:
            continue
        dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        count += 1
    print(f"copied {count} files to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
