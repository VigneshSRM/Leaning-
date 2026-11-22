# Leaning- — Infeara Agent Skills for Claude & ChatGPT

22 Infeara expert skills covering executive, go-to-market, finance, technology, operations, audit, security, legal, and content work — from CEO and Founder (38–45+ years) to Google Ads & Meta Ads (49+ years). Packaged three ways: Claude Code, Claude.ai, and a **ChatGPT/Codex plugin** with the Infeara logo as its icon.

## Quick start

| I use… | Do this |
|---|---|
| **ChatGPT / Codex** | `./scripts/build-plugin.sh` → upload `dist/infeara-plugin-1.0.0.zip` at [platform.openai.com/plugins](https://platform.openai.com/plugins) |
| **Claude Code (this repo)** | Already wired via `.claude/skills/` — just ask, e.g. *"Use the Infeara CFO skill to review this pricing model"* |
| **Claude Code (as a plugin)** | `/plugin install infeara --marketplace VigneshSRM/Leaning-` |
| **Claude Code (anywhere)** | `./scripts/install-skills.sh` → installs all 22 skills to `~/.claude/skills/` |
| **Claude.ai** | Upload any skill folder as a zip (must contain `SKILL.md`) via Settings → Capabilities → Skills |

## Skills

See [`skills/README.md`](skills/README.md) for the full catalog of all 22 skills, routing table, and install instructions. The plugin package is documented in [`plugins/infeara/README.md`](plugins/infeara/README.md).

| Area | Skills |
|---|---|
| Executive | CEO, CFO, CTO, COO, Founder, Co-founder |
| Go-to-market | Marketing, Sales, Digital Marketing (Google/Meta Ads), Content Creator |
| Technology | R&D, Cloud Associate, DevOps, Server Admin, Network Admin, Cyber Security |
| Assurance | Lead Auditor, CISO Auditor, Compliance Manager, Legal |
| Operations | Client Success Manager, Business & Management |

## Layout

```
skills/                       # Canonical skills — edit here (22 × SKILL.md)
.claude/skills/               # Mirror for Claude Code auto-discovery
plugins/infeara/              # ChatGPT/Codex plugin package (manifest, icons, skills)
  plugin.json                 #   Agent Plugins manifest + OpenAI listing metadata
  assets/logo.png             #   1024² listing icon (the Infeara mark)
  assets/composer-icon.png    #   512² composer icon
  .claude-plugin/plugin.json  #   same package installable in Claude Code
.claude-plugin/marketplace.json  # Claude Code marketplace (/plugin install infeara)
.agents/plugins/marketplace.json # ChatGPT desktop local marketplace (testing)
scripts/install-skills.sh     # Install the 22 skills into any Claude setup
scripts/build-plugin.sh       # Sync skills → plugin folder, build dist zip
scripts/validate-plugin.py    # Validate manifest, limits, icons, skills
```

## Editing rule

Edit `skills/` only, then sync everything:

```bash
./scripts/build-plugin.sh      # refreshes plugins/infeara/skills and the zip
cp -r skills/infeara-* .claude/skills/
```
