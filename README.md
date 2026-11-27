# Leaning- — Infeara Agent Skills for Claude & ChatGPT

51 Infeara skills covering executive, go-to-market, finance, technology, operations, audit, security, legal, and content work — from CEO and Founder (38–45+ years) to Google Ads & Meta Ads (49+ years). Packaged three ways: Claude Code, Claude.ai, and a **ChatGPT/Codex plugin** with the Infeara logo as its icon.

## Quick start

| I use… | Do this |
|---|---|
| **ChatGPT / Codex** | `./scripts/build-plugin.sh` → upload `dist/infeara-chatgpt-1.0.0.zip` at [platform.openai.com/plugins](https://platform.openai.com/plugins) |
| **Claude Code (this repo)** | Already wired via `.claude/skills/` — just ask, e.g. *"Use the Infeara CFO skill to review this pricing model"* |
| **Claude Code (as a plugin)** | `/plugin install infeara --marketplace VigneshSRM/Leaning-` |
| **Claude plugin upload (repo ZIP)** | Manifest at `.claude-plugin/plugin.json` at the repo root — zip the repo, keeping that path at the archive root |
| **Claude Code (anywhere)** | `./scripts/install-skills.sh` → installs all 51 skills to `~/.claude/skills/` |
| **Claude.ai** | Upload any skill folder as a zip (must contain `SKILL.md`) via Settings → Capabilities → Skills |

## Getting expert-level output

The skills are a staff, not a menu. [`GUIDE.md`](GUIDE.md) covers the six-part brief, the four
engagement modes, how to invoke individual sections (Quality Checklist, Guardrails, Playbooks),
how to force reasoning, deliberate skill chaining, the output audit, anti-patterns, and
copy-paste starter prompts.

## How routing works

The **agentic CEO** (`infeara-ceo`) is the entry point for any multi-function task. It triages the
request, breaks it into workstreams, assigns one internal role per workstream, sequences the handoffs,
reconciles disagreement, and returns a single consolidated answer — decision, why, who did what, plan,
risks, and the one ask.

Single-domain questions still route straight to their specialist, and naming a skill ("use the CFO
skill") is always honoured. See `skills/infeara-ceo/references/ceo-delegation-protocol.md`.

## Skills

See [`skills/README.md`](skills/README.md) for the full catalog of all 51 skills, routing table, and install instructions. The plugin package is documented in [`plugins/infeara/README.md`](plugins/infeara/README.md).

| Area | Skills |
|---|---|
| Executive | CEO, CFO, CTO, COO, Founder, Co-founder |
| Go-to-market | Marketing, Sales, Digital Marketing (Google/Meta Ads), Content Creator |
| Technology | R&D, Cloud Associate, DevOps, Server Admin, Network Admin, Cyber Security |
| Assurance | Lead Auditor, CISO Auditor, Compliance Manager, Legal |
| Operations | Client Success Manager, Business & Management, Professional Document Writer |
| Delivery team (12) | Team Lead, Sprint Orchestrator, Engagement Manager, Solution Architect, Tech Lead, Implementation Engineer, QA Engineer, Deployment Engineer, Documentation Analyst, Security Analyst, Project Manager, Account Manager |
| Revenue team (15) | Revenue Lead, Pipeline Orchestrator, GTM Strategist, Product Marketing, Brand, Content, Campaign, SEO & Web, Marketing Ops, SDR, Account Executive, Solutions Consultant, Sales Ops, Proposal Manager, Partnerships |

## Layout

```
skills/                       # Canonical skills — edit here (51 × SKILL.md)
.claude/skills/               # Mirror for Claude Code auto-discovery
plugins/infeara/              # ChatGPT/Codex plugin package (manifest, icons, skills)
  plugin.json                 #   Agent Plugins manifest + OpenAI listing metadata
  assets/logo.png             #   1024² listing icon (the Infeara mark)
  assets/composer-icon.png    #   512² composer icon
  .claude-plugin/plugin.json  #   same package installable in Claude Code
.claude-plugin/marketplace.json  # Claude Code marketplace (/plugin install infeara)
.agents/plugins/marketplace.json # ChatGPT desktop local marketplace (testing)
scripts/install-skills.sh     # Install the 51 skills into any Claude setup
scripts/build-plugin.sh       # Sync skills → plugin folder, build dist zip
scripts/validate-plugin.py    # Validate manifest, limits, icons, skills
```

## Plugin manifest naming rule

A Claude plugin ZIP must contain **exactly one** file named `plugin.json`. This repo is itself
the plugin, so the only one is at the archive root:

| File | Role | Named `plugin.json`? |
|---|---|---|
| `.claude-plugin/plugin.json` | The repo's Claude plugin manifest | ✅ yes — the only one |
| `.claude-plugin/marketplace.json` | Marketplace listing | no |
| `plugins/infeara/chatgpt-plugin.json` | ChatGPT/Codex manifest (renamed to `plugin.json` inside its own ZIP by the build script) | no |
| `plugins/infeara/.claude-plugin/claude-plugin.json` | Claude view of the packaged plugin | no |

`scripts/build-plugin.sh` fails the build if the count is not exactly 1.

## Editing rule

Edit `skills/` only, then sync everything:

```bash
./scripts/build-plugin.sh      # refreshes plugins/infeara/skills and the zip
cp -r skills/infeara-* .claude/skills/
```
