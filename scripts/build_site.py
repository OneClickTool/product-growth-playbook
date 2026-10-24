#!/usr/bin/env python3
"""Build the GitHub Pages source in .site-docs/ from the repo's Markdown, then write _mkdocs.gen.yml.

Standard library only. Usage (from anywhere):
    python3 scripts/build_site.py && mkdocs serve -f _mkdocs.gen.yml

What it does, so the site is easier to learn from than the raw Markdown:
- copies every public .md / image / csv / py file into .site-docs/ (source of truth stays in the repo)
- uses site/home.md as the landing page and the root README as "playbook-overview"
- adds a "skill card" (summary, level, time, area) under the title of every SKILL.md
- wraps key sections in coloured boxes: Goal, Example output, Common mistakes, "Five things to remember",
  "Illustrative example" quotes
- adds a picture under the title of pages listed in HERO_IMAGES
- builds the left menu (nav) with readable titles in a learning order
"""
import hashlib
import html
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".site-docs"
SITE = ROOT / "site"
GEN = ROOT / "_mkdocs.gen.yml"
SKIP_DIRS = {".git", ".github", ".private", ".claude", ".claude-plugin", ".site-docs", "_site", "__pycache__",
             "node_modules", "raw", "site", "prompts"}
SKIP_FILES = {"CLAUDE.md", "AGENTS.md", "mkdocs.yml", "_mkdocs.gen.yml"}
KEEP_EXT = {".md", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".csv", ".py", ".json", ".txt"}

# Section heading -> box style. The heading stays (so #anchors keep working); its body goes in the box.
BOXES = {
    "Goal": "goal",
    "Example output": "example",
    "Common mistakes": "danger",
    "Five things to remember": "star",
    "The rules you must follow": "rules",
    "Prompt": "prompt",
}

# Page -> picture shown under its title (paths relative to the repo root). A list = first one that exists,
# so a painted illustration (docs/images/prompts/) replaces the SVG as soon as it is added.
HERO_IMAGES = {
    "marketing/README-marketing-social.md": ["docs/images/illustrations/12-marketing-map-hero.jpg",
                                             "site/images/channel-map.svg"],
    "marketing/tiktok-marketing/README-TikTok-Marketing.md": ["docs/images/illustrations/10-tiktok-kit-hero.jpg",
                                                              "site/images/tiktok-slideshow.svg"],
    "marketing/tiktok-marketing/docs/02-the-slideshow-loop.md": "site/images/slideshow-loop.svg",
    "marketing/tiktok-marketing/skills/social-tiktok-slideshow/SKILL.md": "site/images/tiktok-slideshow.svg",
    "marketing/tiktok-marketing/skills/social-tiktok-slideshow-loop/SKILL.md": "site/images/slideshow-loop.svg",
    "marketing/instagram-marketing/README-Instagram-Marketing.md": ["docs/images/illustrations/11-instagram-kit-hero.jpg",
                                                                    "site/images/instagram-carousel.svg"],
    "marketing/reddit-marketing/README-Reddit-Marketing.md": ["docs/images/illustrations/14-reddit-kit-hero.jpg",
                                                              "site/images/channel-map.svg"],
    "marketing/medium-marketing/README-Medium-Marketing.md": "site/images/channel-map.svg",
    "marketing/pinterest-marketing/README-Pinterest-Marketing.md": ["docs/images/illustrations/15-pinterest-kit-hero.jpg",
                                                                    "site/images/channel-map.svg"],
    "marketing/facebook-marketing/README-Facebook-Marketing.md": ["docs/images/illustrations/16-facebook-kit-hero.jpg",
                                                                  "site/images/channel-map.svg"],
    "skills/growth/SKILL.md": ["docs/images/illustrations/13-skill-steps-hero.jpg", "site/images/funnel.svg"],
    "playbook-overview.md": "docs/images/illustrations/01-growth-hack-hero.jpg",
    "skills/launch/README.md": "docs/images/illustrations/02-free-hook-ladder.jpg",
    "skills/strategy/README.md": "docs/images/illustrations/03-traffic-engine.jpg",
    "skills/social/README.md": "docs/images/illustrations/06-cross-channel-funnel.jpg",
    "playbooks/growth-map.md": "site/images/funnel.svg",
}


# ---------------------------------------------------------------- copy
def copy_tree():
    if OUT.exists():
        shutil.rmtree(OUT)
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts) or not path.is_file():
            continue
        if path.name in SKIP_FILES or path.suffix.lower() not in KEEP_EXT:
            continue
        dest = OUT / ("playbook-overview.md" if rel.as_posix() == "README.md" else rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
    # site-only assets: landing page, styles, images
    shutil.copy2(SITE / "home.md", OUT / "index.md")
    for sub in ("stylesheets", "images", "javascripts"):
        if (SITE / sub).exists():
            shutil.copytree(SITE / sub, OUT / "site" / sub)


# ---------------------------------------------------------------- transforms
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)


def frontmatter(text):
    m = FRONT.match(text)
    if not m:
        return {}, text
    data, parent = {}, None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        key, _, value = line.strip().partition(":")
        value = value.strip().strip('"')
        if line.startswith((" ", "\t")) and parent:
            data[f"{parent}.{key}"] = value
        else:
            data[key] = value
            parent = key if not value else None
    return data, text[m.end():]


def first_sentences(text, n=2):
    parts = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(parts[:n])


def skill_card(meta):
    desc = html.escape(first_sentences(meta.get("description", "")))
    level = meta.get("metadata.difficulty", "")
    chips = []
    if level:
        chips.append(f'<span class="chip chip--{html.escape(level.lower())}">{html.escape(level.title())}</span>')
    if meta.get("metadata.time"):
        chips.append(f'<span class="chip">⏱ {html.escape(meta["metadata.time"])}</span>')
    if meta.get("metadata.category"):
        chips.append(f'<span class="chip">📂 {html.escape(meta["metadata.category"])}</span>')
    if meta.get("metadata.version"):
        chips.append(f'<span class="chip chip--ghost">v{html.escape(meta["metadata.version"])}</span>')
    return (f'\n<div class="skill-card">\n<p class="skill-card__desc">{desc}</p>\n'
            f'<div class="chips">{"".join(chips)}</div>\n</div>\n')


def wrap_sections(text):
    lines = text.split("\n")
    out, i, in_fence = [], 0, None
    while i < len(lines):
        line = lines[i]
        fence = re.match(r"^(`{3,}|~{3,})", line)
        if fence:
            in_fence = None if in_fence and line.startswith(in_fence) else (in_fence or fence.group(1))
        heading = re.match(r"^## (.+?)\s*$", line) if not in_fence else None
        style = next((v for k, v in BOXES.items() if heading and heading.group(1).startswith(k)), None)
        if not style:
            out.append(line)
            i += 1
            continue
        out += [line, "", f'<div class="box box--{style}" markdown>', ""]
        i += 1
        body_fence = None
        while i < len(lines):
            nxt = lines[i]
            f = re.match(r"^(`{3,}|~{3,})", nxt)
            if f:
                body_fence = None if body_fence and nxt.startswith(body_fence) else (body_fence or f.group(1))
            if not body_fence and re.match(r"^#{1,2} ", nxt):
                break
            out.append(nxt)
            i += 1
        out += ["", "</div>", ""]
    return "\n".join(out)


def illustrative_boxes(text):
    """> **Illustrative example.** ... (a blockquote) -> a dashed 'made-up numbers' box."""
    lines, out, i = text.split("\n"), [], 0
    while i < len(lines):
        if lines[i].startswith("> **Illustrative example.**"):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i][1:].lstrip(" ") if lines[i] != ">" else "")
                i += 1
            out += ["", '<div class="box box--illustrative" markdown>', "", *block, "", "</div>", ""]
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


def add_hero(text, rel, image):
    options = image if isinstance(image, list) else [image]
    src = next((o for o in options if (OUT / o).exists()), None)
    if not src:
        return text
    href = os.path.relpath(src, os.path.dirname(rel) or ".")
    tag = f'\n<figure class="hero-img" markdown>\n![]({href}){{ loading=lazy }}\n</figure>\n'
    return re.sub(r"^(# .+\n)", lambda m: m.group(1) + tag, text, count=1, flags=re.M)


def transform_all():
    for path in OUT.rglob("*.md"):
        rel = path.relative_to(OUT).as_posix()
        if rel == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = frontmatter(text)
        body = illustrative_boxes(body)
        body = wrap_sections(body)
        if path.name == "SKILL.md" and meta.get("description"):
            body = re.sub(r"^(# .+\n)", lambda m: m.group(1) + skill_card(meta), body, count=1, flags=re.M)
        if rel in HERO_IMAGES and "illustrations/" not in body.split("\n## ")[0]:
            body = add_hero(body, rel, HERO_IMAGES[rel])
        path.write_text(body, encoding="utf-8")


# ---------------------------------------------------------------- nav
def title_of(rel):
    try:
        text = (OUT / rel).read_text(encoding="utf-8")
    except OSError:
        return rel
    m = re.search(r"^# (.+)$", text, re.M)
    t = m.group(1) if m else Path(rel).stem
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t).replace("`", "").replace("*", "")
    return t.strip()


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def md_files(folder):
    base = OUT / folder
    return sorted(p.relative_to(OUT).as_posix() for p in base.glob("*.md")) if base.exists() else []


def entry(rel, indent, label=None):
    return f"{' ' * indent}- {q(label or title_of(rel))}: {rel}"


def kit_nav(kit, indent):
    """One channel kit: its README first, then each sub-folder as a section."""
    lines = []
    readme = next(iter(sorted((OUT / kit).glob("README-*.md"))), None)
    if readme:
        lines.append(entry(readme.relative_to(OUT).as_posix(), indent, "Start here"))
    order = ["docs", "flow", "case-studies", "skills", "posts", "templates", "reference", "resources"]
    names = {"docs": "Docs", "flow": "Flow", "case-studies": "Case studies", "skills": "Skills", "posts": "Ready posts",
             "templates": "Templates", "reference": "Reference", "resources": "Resources"}
    for sub in order:
        if not (OUT / kit / sub).exists():
            continue
        items = [entry(r, indent + 4) for r in md_files(f"{kit}/{sub}") if not r.endswith("README.md")]
        if sub == "skills":
            items = [entry(p.relative_to(OUT).as_posix(), indent + 4)
                     for p in sorted((OUT / kit / sub).glob("*/SKILL.md"))]
        for deeper in sorted(d for d in (OUT / kit / sub).iterdir() if d.is_dir() and sub != "skills"):
            inner = [entry(r, indent + 8) for r in md_files(deeper.relative_to(OUT).as_posix())]
            if inner:
                items.append(f"{' ' * (indent + 4)}- {q(deeper.name.replace('-', ' ').title())}:")
                items += inner
        readme_sub = OUT / kit / sub / "README.md"
        if readme_sub.exists():
            items.insert(0, entry(readme_sub.relative_to(OUT).as_posix(), indent + 4, "Overview"))
        if items:
            lines.append(f"{' ' * indent}- {q(names[sub])}:")
            lines += items
    return lines


def build_nav():
    n = ["nav:", '  - "Home": index.md']
    n += ['  - "Start":', entry("playbook-overview.md", 6, "The playbook"),
          entry("skills/growth/SKILL.md", 6, "Which skill do I need?")]
    if (OUT / "flow").exists():
        n += [entry(r, 6) for r in md_files("flow")]
    n += [entry(r, 6) for r in md_files("playbooks")]
    actions = md_files("skills/growth/action")
    if actions:
        n.append('      - "Action plan":')
        n += [entry(r, 10) for r in actions]

    n.append('  - "Marketing":')
    n.append(entry("marketing/README-marketing-social.md", 6, "Map: how channels link"))
    for kit, label in (("marketing/tiktok-marketing", "🎞️ TikTok"), ("marketing/instagram-marketing", "📸 Instagram"),
                       ("marketing/x-marketing", "🐦 X (Twitter)"), ("marketing/reddit-marketing", "🟠 Reddit"),
                       ("marketing/medium-marketing", "✍️ Medium"), ("marketing/pinterest-marketing", "📌 Pinterest"),
                       ("marketing/facebook-marketing", "📘 Facebook")):
        if (OUT / kit).exists():
            n.append(f"      - {q(label)}:")
            n += kit_nav(kit, 10)
            if kit.endswith("reddit-marketing") and (OUT / "docs/subreddits").exists():
                n.append('          - "Subreddit wiki":')
                n += [entry(r, 14, "All subreddits" if r.endswith("README.md") else None) for r in md_files("docs/subreddits")]

    if (OUT / "chrome").exists():
        n += ['  - "Chrome":', entry("chrome/README.md", 6, "Tổng quan")]
        for folder, label in (("chrome/dev-analytics", "📊 Chrome Dev Analytics"),
                              ("chrome/store-research", "🔎 Chrome Store Research")):
            n.append(f"      - {q(label)}:")
            pages = sorted(md_files(folder), key=lambda r: not r.endswith("README.md"))
            n += [entry(r, 10, "Mục lục" if r.endswith("README.md") else title_of(r).split(":")[0]) for r in pages]

    n.append('  - "Skills":')
    for area in sorted(p for p in (OUT / "skills").iterdir() if p.is_dir() and p.name != "growth"):
        rel = f"skills/{area.name}/README.md"
        n.append(f"      - {q(title_of(rel) if (OUT / rel).exists() else area.name.title())}:")
        if (OUT / rel).exists():
            n.append(entry(rel, 10, "Overview"))
        for skill in sorted(area.glob("*/SKILL.md")):
            n.append(entry(skill.relative_to(OUT).as_posix(), 10))

    cases = md_files("case-study")
    if cases:
        n.append('  - "Case studies":')
        n += [entry(r, 6, "All cases" if r.endswith("README.md") else None) for r in cases]

    n.append('  - "About":')
    for rel in ("CONTRIBUTING.md", "ROADMAP.md", "CHANGELOG.md", "SKILL_TEMPLATE.md", "docs/skill-anatomy.md",
                "CODE_OF_CONDUCT.md"):
        if (OUT / rel).exists():
            n.append(entry(rel, 6))
    return "\n".join(n) + "\n"


def hashed_css():
    """Copy extra.css to extra.<hash>.css so browsers fetch the new styles right after a deploy."""
    src = OUT / "site" / "stylesheets" / "extra.css"
    digest = hashlib.sha1(src.read_bytes()).hexdigest()[:10]
    dest = src.with_name(f"extra.{digest}.css")
    shutil.copy2(src, dest)
    return f"extra_css:\n  - {dest.relative_to(OUT).as_posix()}\n"


def main():
    copy_tree()
    transform_all()
    GEN.write_text("# Generated by scripts/build_site.py. Do not edit; edit mkdocs.yml instead.\n"
                   "INHERIT: mkdocs.yml\n" + hashed_css() + build_nav(), encoding="utf-8")
    pages = sum(1 for _ in OUT.rglob("*.md"))
    print(f"{pages} pages in {OUT.relative_to(ROOT)}/ · nav in {GEN.name}")


if __name__ == "__main__":
    main()
