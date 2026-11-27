---
name: infeara-guide
description: "Orientation and routing guide for the Infeara skill library in this repository. Use when the user asks which Infeara expert handles a topic, how the skills are organised, where files live, how to rebuild the plugin, or says 'which skill', 'who handles', 'repo structure', 'how do I build', 'plugin rules'. Not a business expert — it points to the right one."
---

# Infeara — Library Guide

This repository ships 23 Infeara expert skills, published three ways: Claude Code (`.claude/skills/`), a Claude Code plugin, and a ChatGPT/Codex plugin. This skill is the map: it routes a request to the right expert and documents how the library is built.

## Where things live

| Path | Purpose |
|---|---|
| `skills/<name>/SKILL.md` | **Canonical source.** Edit here and nowhere else. |
| `.claude/skills/<name>/` | Mirror auto-discovered by Claude Code — do not edit separately |
| `plugins/infeara/` | ChatGPT/Codex plugin package: `plugin.json`, `assets/`, generated `skills/` |
| `.claude-plugin/plugin.json` | Makes the repo root itself an installable Claude plugin |
| `.claude-plugin/marketplace.json` | Marketplace listing (`/plugin install infeara`) |
| `.claude-plugin/icon.png` | 1024² listing icon |
| `scripts/build-plugin.sh` | Sync skills → plugin folder, rebuild `dist/` ZIP, validate |
| `scripts/validate-plugin.py` | Manifest, limits, icons, frontmatter, referenced files |
| `scripts/install-skills.sh` | Install skills into any Claude setup |

### Editing workflow

```bash
# 1. edit skills/<name>/SKILL.md
cp -r skills/infeara-* .claude/skills/     # 2. sync the Claude mirror
./scripts/build-plugin.sh                  # 3. sync plugin, rebuild ZIP, validate
```

Never edit `plugins/infeara/skills/` by hand — it is generated.

## Routing — which expert for which request

| Request sounds like… | Skill |
|---|---|
| Strategy, vision, board, M&A, executive decision | `infeara-ceo` |
| Positioning, GTM, campaigns, demand generation | `infeara-marketing-expert` |
| Pipeline, proposals, pricing, negotiation, forecasting | `infeara-sales-expert` |
| Budget, P&L, cash flow, margin, unit economics | `infeara-cfo` |
| Technology strategy, architecture, build vs buy | `infeara-cto` |
| Operations, delivery, SOPs, capacity | `infeara-coo` |
| Research, prototypes, feasibility, innovation | `infeara-rd-expert` |
| Onboarding, retention, renewals, QBRs, churn | `infeara-client-success-manager` |
| Internal audit, ISO audit, findings, CAPA | `infeara-lead-auditor` |
| Security audit, ISO 27001, SOC 2, risk | `infeara-ciso-auditor` |
| Cloud platforms, migration, cloud cost | `infeara-cloud-associate` |
| CI/CD, Kubernetes, IaC, monitoring, SRE | `infeara-devops-expert` |
| Compliance systems, policies, audit readiness | `infeara-compliance-manager` |
| Servers, patching, backup, Linux and Windows | `infeara-server-system-admin` |
| Networks, VPN, DNS, firewalls, latency | `infeara-network-administrator` |
| Threats, vulnerabilities, incident response | `infeara-cyber-security-expert` |
| Contracts, NDA, MSA, SOW, redlines | `infeara-legal-expert` |
| Business plans, org design, KPIs, reviews | `infeara-business-management-expert` |
| 0-to-1, founding vision, fundraising, pivots | `infeara-founder` |
| Co-founder roles, equity, partnerships, conflict | `infeara-cofounder` |
| Google Ads, Meta Ads, PPC, ROAS, paid media | `infeara-digital-marketing-expert` |
| Blog, social post, video script, newsletter | `infeara-content-creator-expert` |
| Formal document, report, cover page, pagination, letterhead, fonts | `infeara-document-writer` |

## Plugin rules

1. `plugins/infeara/chatgpt-plugin.json` is the portable Agent Plugins manifest (renamed so the repo keeps exactly one `plugin.json`); OpenAI listing metadata lives under `extensions.com.openai`.
2. Listing limits: `displayName` ≤ 30, `shortDescription` ≤ 30, `longDescription` ≤ 4000, `developerName` ≤ 80, ≤ 3 `defaultPrompt` entries of ≤ 128 chars, `category` from the directory list.
3. Icons: square PNG/JPEG/WebP/SVG, ≥ 48 px (logo ≥ 512 px), ≤ 5 MiB, `./`-prefixed paths.
4. Skills-only plugin: no `mcp.json`, no review test cases, no demo recording.
5. Never invent listing URLs — `websiteURL`, `supportURL`, `privacyPolicyURL`, `termsOfServiceURL` stay unset until real pages exist.
6. Run `python3 scripts/validate-plugin.py` and `claude plugin validate . --profile directory` before any submission.

## Conventions when working in this repo

1. Load the single best-matching expert skill; chain only when a task spans domains.
2. Follow each skill's Quality Checklist before delivering.
3. Respect each skill's Guardrails — never invent financials, client facts, evidence, or legal advice.
4. Frontmatter `name` must equal the folder name; `description` must stay trigger-rich ("Use when…").
5. Keep each `SKILL.md` under ~120 lines.
6. When adding or removing a skill, update `skills/README.md`, this routing table, and `plugins/infeara/skills/get-started/SKILL.md` together, then rebuild.

## Guardrails

- Never claim a skill exists that is not in `skills/` — check the folder before routing.
- Do not modify generated files (`plugins/infeara/skills/`, `dist/`) by hand.
- Do not add listing URLs, licences, or publisher details that have not been confirmed by the owner.
