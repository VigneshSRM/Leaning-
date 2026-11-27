---
name: infeara-guide
description: "Orientation and routing guide for the Infeara skill library. Use when the user asks which Infeara expert or team handles a topic, how work is delegated, how the skills are organised, where files live, or says 'which skill', 'who handles this', 'how does routing work', 'how do I build', 'plugin rules'. Explains the CEO-as-entry-point model. Not a business expert — it points to the right one."
---

# Infeara — Library Guide

This repository ships 51 Infeara skills — 23 expert personas, a 12-skill delivery team and a 15-skill revenue team — published three ways: Claude Code (`.claude/skills/`), a Claude Code plugin, and a ChatGPT/Codex plugin. This skill is the map: it explains how work is routed and documents how the library is built.

## Routing model — the CEO is the front door

Any task that spans more than one function goes to **`infeara-ceo`**, which acts as the agentic
entry point: it decomposes the task into workstreams, assigns one internal role per workstream,
sequences the handoffs, reconciles disagreement, and returns a single consolidated answer.

```
User task
   ▼
infeara-ceo  ── triage ─▶ single-domain?  ── yes ─▶ route straight to that one skill
   │                   └─ decision?      ── yes ─▶ CEO decides (consults 2–3 leads)
   │                   └─ project?       ── yes ─▶ decompose + delegate
   │                   └─ crisis?        ── yes ─▶ CEO commands, one incident owner
   ▼
Internal teams (34 roles)
   ├─ Executive peers ........ CFO · CTO · COO · Legal · Client Success · Auditors · Founder
   ├─ Delivery team (12) ..... team lead · sprint orchestrator · 10 delivery roles
   └─ Revenue team (15) ...... revenue lead · pipeline orchestrator · 13 revenue roles
   ▼
Consolidated answer (decision · why · who did what · plan · risks · ask)
```

**Route directly, skip the CEO, when any of these is true:**
- The request names a skill explicitly ("use the CFO skill").
- The request is a single-domain question one specialist answers in one reply.
- The request is purely document formatting (`infeara-document-writer`) or library questions (this skill).

**Always route through the CEO when:** the task has multiple deliverables, spans functions, needs a
decision across domains, or the user says "handle this", "get the team on it", "deliver this",
"who should do this", "put a plan together".

Full protocol and a worked example: `../infeara-ceo/references/ceo-delegation-protocol.md` (in the `infeara-ceo` skill folder).

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

**Start here:** multi-function task, project, or "handle this" → `infeara-ceo`. Everything below is
for direct single-domain routing.

### Executive and specialist experts

| Request sounds like… | Skill |
|---|---|
| Strategy, vision, board, M&A, executive decision, multi-team task | `infeara-ceo` |
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

### Delivery team (12) — engagements and projects

| Request | Skill |
|---|---|
| Whole engagement, "assemble the team", end-to-end delivery | `infeara-team-lead` |
| Sprint plan, stand-up, retro, backlog, cadence | `infeara-sprint-orchestrator` |
| Scope, discovery, change request, sign-off | `infeara-team-engagement-manager` |
| Solution design, architecture, ADR, feasibility | `infeara-team-solution-architect` |
| Engineering standards, task breakdown, code review | `infeara-team-tech-lead` |
| Write code, fix a defect, unit tests | `infeara-team-implementation-engineer` |
| Test plan, acceptance testing, defects | `infeara-team-qa-engineer` |
| Release, deploy, rollback, environments | `infeara-team-deployment-engineer` |
| Runbooks, handover, user guides | `infeara-team-documentation-analyst` |
| Threat model, security review, security sign-off | `infeara-team-security-analyst` |
| Project plan, schedule, milestones, risks, status | `infeara-team-project-manager` |
| Client health, renewal, expansion, escalation | `infeara-team-account-manager` |

### Revenue team (15) — sales and marketing

| Request | Skill |
|---|---|
| Revenue plan, target, coverage, sales+marketing org | `infeara-revenue-lead` |
| Pipeline review, funnel, forecast, conversion | `infeara-revenue-pipeline-orchestrator` |
| Segmentation, positioning, launch, pricing input | `infeara-revenue-gtm-strategist` |
| Messaging, battlecards, sales enablement, proof | `infeara-revenue-product-marketing` |
| Brand voice, visual identity, brand audit | `infeara-revenue-brand-manager` |
| Content strategy, editorial calendar, production | `infeara-revenue-content-manager` |
| Campaigns, launches, webinars, events | `infeara-revenue-campaign-manager` |
| SEO, organic, landing pages | `infeara-revenue-seo-specialist` |
| Tracking, attribution, lead scoring, martech | `infeara-revenue-marketing-ops` |
| Cold outreach, prospecting, qualification | `infeara-revenue-sdr` |
| Deal strategy, discovery, demo, close | `infeara-revenue-account-executive` |
| POC, technical validation, pre-sales scoping | `infeara-revenue-solutions-consultant` |
| Sales process, CRM, forecast mechanics, territories | `infeara-revenue-sales-ops` |
| RFP, proposal, bid decision, compliance | `infeara-revenue-proposal-manager` |
| Partners, channel, resellers, alliances | `infeara-revenue-partnerships-manager` |

## Plugin rules

1. `plugins/infeara/chatgpt-plugin.json` is the portable Agent Plugins manifest (renamed so the repo keeps exactly one `plugin.json`); OpenAI listing metadata lives under `extensions.com.openai`.
2. Listing limits: `displayName` ≤ 30, `shortDescription` ≤ 30, `longDescription` ≤ 4000, `developerName` ≤ 80, ≤ 3 `defaultPrompt` entries of ≤ 128 chars, `category` from the directory list.
3. Icons: square PNG/JPEG/WebP/SVG, ≥ 48 px (logo ≥ 512 px), ≤ 5 MiB, `./`-prefixed paths.
4. Skills-only plugin: no `mcp.json`, no review test cases, no demo recording.
5. Never invent listing URLs — `websiteURL`, `supportURL`, `privacyPolicyURL`, `termsOfServiceURL` stay unset until real pages exist.
6. Run `python3 scripts/validate-plugin.py` and `claude plugin validate . --profile directory` before any submission.

## Conventions when working in this repo

1. **Multi-function task → `infeara-ceo` first.** It decomposes, delegates to internal roles, and consolidates. Do not let ten separate specialists answer the user directly.
2. Load the single best-matching expert skill for single-domain work; chain only when a task spans domains.
3. Follow each skill's Quality Checklist before delivering.
4. Respect each skill's Guardrails — never invent financials, client facts, evidence, or legal advice.
5. Attribute delegated findings to the role that produced them; never present a delegate's work as improvised analysis.
6. Frontmatter `name` must equal the folder name; `description` must stay trigger-rich ("Use when…").
7. Keep each `SKILL.md` under ~140 lines.
8. When adding or removing a skill, update `skills/README.md`, this routing table, `CLAUDE.md`, and `plugins/infeara/skills/get-started/SKILL.md` together, then rebuild.

## Guardrails

- Never claim a skill exists that is not in `skills/` — check the folder before routing.
- Do not modify generated files (`plugins/infeara/skills/`, `dist/`) by hand.
- Do not add listing URLs, licences, or publisher details that have not been confirmed by the owner.
