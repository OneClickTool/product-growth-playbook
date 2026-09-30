#!/usr/bin/env python3
"""Check every skills/**/SKILL.md against the repo rules. Prints OK or a list of problems.

Standard library only, so it runs anywhere (no install needed).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_SECTIONS = ["Goal", "When to use", "Inputs", "Steps", "Example output", "Common mistakes"]
PROMPT_SECTION = re.compile(r"^## Prompt\b", re.M)
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TOP_LEVEL_KEYS = {"name", "description", "license", "metadata", "allowed-tools"}
MAX_LINES = 500


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if line and not line.startswith((" ", "\t", "#")) and ":" in line:
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip()
    return data


def check_skill(path, errors):
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        errors.append(f"{rel}: missing YAML frontmatter")
        return None
    name = fm.get("name", "")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{rel}: name '{name}' must be lowercase-hyphenated, <= 64 chars")
    if name != path.parent.name:
        errors.append(f"{rel}: name '{name}' must equal folder name '{path.parent.name}'")
    desc = fm.get("description", "")
    if not desc:
        errors.append(f"{rel}: description is empty")
    elif len(desc) > 1024:
        errors.append(f"{rel}: description is {len(desc)} chars (max 1024)")
    elif "use when" not in desc.lower():
        errors.append(f"{rel}: description should say when to use the skill ('Use when ...')")
    for key in fm:
        if key not in TOP_LEVEL_KEYS:
            errors.append(f"{rel}: move '{key}' under metadata:")
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^## {re.escape(section)}\b", text, re.M):
            errors.append(f"{rel}: missing section '## {section}'")
    if not PROMPT_SECTION.search(text):
        errors.append(f"{rel}: missing section '## Prompt (copy-paste)'")
    elif "````" not in text:
        errors.append(f"{rel}: prompt must be fenced with four backticks")
    if text.count("````") % 2:
        errors.append(f"{rel}: unbalanced four-backtick fence")
    lines = text.count("\n") + 1
    if lines > MAX_LINES:
        errors.append(f"{rel}: {lines} lines (max {MAX_LINES}); move detail to references/")
    prose = re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", text, flags=re.M | re.S)  # links inside code blocks are examples
    for target in re.findall(r"\]\((?!https?://|#)([^)#\s]+)", prose):
        if not (path.parent / target).exists():
            errors.append(f"{rel}: broken link -> {target}")
    return path.parent.relative_to(ROOT).as_posix()


def main():
    errors = []
    skill_dirs = set()
    for path in sorted((ROOT / "skills").rglob("SKILL.md")):
        d = check_skill(path, errors)
        if d:
            skill_dirs.add(d)

    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        mp = json.loads(mp_path.read_text(encoding="utf-8"))
        listed = {s.removeprefix("./") for p in mp.get("plugins", []) for s in p.get("skills", [])}
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f".claude-plugin/marketplace.json: {e}")
        listed = set()
    for d in sorted(skill_dirs - listed):
        errors.append(f"marketplace.json: skill not listed -> ./{d}")
    for d in sorted(listed - skill_dirs):
        errors.append(f"marketplace.json: listed skill has no SKILL.md -> ./{d}")

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) in {len(skill_dirs)} skill(s)")
        return 1
    print(f"OK: {len(skill_dirs)} skill(s) valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
