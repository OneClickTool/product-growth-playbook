# Reddit skills

Agent Skills for Reddit. Each `SKILL.md` works in Claude Code, Codex, Claude.ai or by hand; each has a copy-paste
prompt. They're installed with the rest of the playbook (see the root README).

| Skill | What you get | Time |
|---|---|---|
| [social-reddit](social-reddit/SKILL.md) | **Start here.** One command: `/social-reddit today · find · reply · post · rules · profile · numbers · risk` runs the right skill or doc | 1 min |
| [social-reddit-comment](social-reddit-comment/SKILL.md) | One answer in the right shape, a 5-check yes/no on mentioning your product, a disclosure line, a tracker row | 5 min per answer |

**Order:** profile (once) → comments every day → one post a week from week 3. Or just type `/social-reddit`.

Installed as a plugin, the command is `/product-growth-hack:social-reddit <command>`; copied into `.claude/skills/`, it's `/social-reddit <command>`.

Also used by this kit, from the main library: [launch-reddit-posting](../../../skills/launch/launch-reddit-posting/SKILL.md)
(posts, subreddits by product type, the rules script) · [research-where-users-ask](../../../skills/research/research-where-users-ask/SKILL.md).
