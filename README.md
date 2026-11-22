# Leaning- — Infeara Agent Skills for Claude

22 Claude Agent Skills covering Infeara's executive, go-to-market, finance, technology, operations, audit, security, legal, and content functions — from CEO and Founder (38–45+ years) to Google Ads & Meta Ads (49+ years).

## Quick start

- **Using Claude Code in this repo?** Skills are already wired via `.claude/skills/` — just ask (e.g. *"Use the Infeara CFO skill to review this pricing model"*).
- **Using Claude Code elsewhere?** Run `./scripts/install-skills.sh` to install all 22 skills to `~/.claude/skills/`.
- **Using Claude.ai?** Upload any skill folder as a zip (must contain `SKILL.md`) via Settings → Capabilities → Skills.

## Skills

See [`skills/README.md`](skills/README.md) for the full catalog of all 22 skills, routing table, and install instructions.

| Area | Skills |
|---|---|
| Executive | CEO, CFO, CTO, COO, Founder, Co-founder |
| Go-to-market | Marketing, Sales, Digital Marketing (Google/Meta Ads), Content Creator |
| Technology | R&D, Cloud Associate, DevOps, Server Admin, Network Admin, Cyber Security |
| Assurance | Lead Auditor, CISO Auditor, Compliance Manager, Legal |
| Operations | Client Success Manager, Business & Management |

## Layout

```
skills/                  # Canonical skills — edit here (22 × SKILL.md)
.claude/skills/          # Mirror for Claude Code auto-discovery
scripts/install-skills.sh
CLAUDE.md                # Routing guide for Claude in this repo
```
