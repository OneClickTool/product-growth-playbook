#!/usr/bin/env python3
"""Fetch the current rules (and pinned posts) of subreddits into one Markdown file.

Subreddit rules change often. Run this before you post, instead of trusting a copy.
Standard library only. Uses Reddit's public JSON endpoints, 2 seconds apart.

    python3 fetch_subreddit_rules.py macapps MacOS SideProject      # specific subs
    python3 fetch_subreddit_rules.py --all                           # every sub in the skill
    python3 fetch_subreddit_rules.py --all -o rules.md               # write to a file
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date

ALL = [
    # macOS
    "macapps", "MacOS", "mac", "apple", "SwiftUI", "swift", "iOSProgramming",
    # iOS
    "iosapps", "iphone", "ios", "AppHookup", "shortcuts",
    # Android
    "androidapps", "Android", "androiddev",
    # Builders / startups
    "SideProject", "indiehackers", "SaaS", "startups", "Entrepreneur", "EntrepreneurRideAlong",
    "microsaas", "alphaandbetausers", "IMadeThis", "roastmystartup", "buildinpublic",
    # Dev tools / open source / web
    "webdev", "programming", "opensource", "coolgithubprojects", "selfhosted", "github", "vscode",
    "commandline", "javascript", "reactjs", "Python",
    # Extensions / Windows / software
    "chrome_extensions", "chrome", "firefox", "browsers", "software", "Windows11", "windows",
    # Games
    "IndieDev", "indiegames", "gamedev", "playmygame", "WebGames", "incremental_games", "godot",
    "Unity3D", "IndieGaming",
    # AI
    "ChatGPT", "ClaudeAI", "LocalLLaMA", "artificial", "OpenAI", "AI_Agents", "mcp", "ChatGPTPro",
    # Templates / productivity
    "Notion", "productivity", "ObsidianMD", "excel", "googlesheets",
]

UA = "growth-playbook-rules-fetcher/1.0 (read-only; github.com/OneClickTool/product-growth-playbook)"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def one_line(text, limit=400):
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def fetch(sub):
    out = [f"## r/{sub}", f"Rules: https://www.reddit.com/r/{sub}/about/rules", ""]
    try:
        about = get(f"https://www.reddit.com/r/{sub}/about.json").get("data", {})
        out.append(f"- Members: {about.get('subscribers', '?'):,}" if isinstance(about.get("subscribers"), int)
                   else "- Members: ?")
        if about.get("public_description"):
            out.append(f"- About: {one_line(about['public_description'], 200)}")
    except (urllib.error.URLError, ValueError) as e:
        out.append(f"- About: could not load ({e})")
    try:
        rules = get(f"https://www.reddit.com/r/{sub}/about/rules.json").get("rules", [])
        if not rules:
            out.append("- No rules listed (check the sidebar and wiki).")
        for i, r in enumerate(rules, 1):
            desc = one_line(r.get("description"))
            out.append(f"{i}. **{r.get('short_name', '').strip()}**" + (f": {desc}" if desc else ""))
    except (urllib.error.URLError, ValueError) as e:
        out.append(f"- Rules: could not load ({e})")
    for n in (1, 2):
        try:
            s = get(f"https://www.reddit.com/r/{sub}/about/sticky.json?num={n}")
            post = s[0]["data"]["children"][0]["data"] if isinstance(s, list) else s["data"]["children"][0]["data"]
            out.append(f"- Pinned: [{one_line(post.get('title'), 120)}](https://www.reddit.com{post.get('permalink')})")
        except (urllib.error.URLError, ValueError, KeyError, IndexError, TypeError):
            pass
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("subs", nargs="*", help="subreddit names without r/")
    ap.add_argument("--all", action="store_true", help="fetch every subreddit listed in the skill")
    ap.add_argument("-o", "--output", help="write Markdown to this file instead of stdout")
    args = ap.parse_args()
    subs = ALL if args.all else args.subs
    if not subs:
        ap.error("give subreddit names or --all")
    parts = [f"# Subreddit rules snapshot\n\nFetched {date.today().isoformat()} from Reddit's public JSON. "
             "Rules change: re-run before posting.\n"]
    for i, sub in enumerate(subs):
        print(f"[{i + 1}/{len(subs)}] r/{sub}", file=sys.stderr)
        parts.append(fetch(sub))
        time.sleep(2)
    text = "\n".join(parts)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
