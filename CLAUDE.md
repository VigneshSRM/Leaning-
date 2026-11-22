# Infeara — Claude Project Guide

This repo contains 22 Infeara Agent Skills for Claude (see `skills/README.md` for the full catalog).

## Skills location

- Canonical: `skills/<skill-name>/SKILL.md`
- Claude Code mirror (auto-discovered): `.claude/skills/<skill-name>/SKILL.md`

Edit `skills/` only, then re-mirror with `cp -r skills/infeara-* .claude/skills/`.

## Routing — which skill for which request

| Request sounds like… | Skill |
|---|---|
| Strategy, vision, board, M&A, executive decision | `infeara-ceo` |
| Positioning, GTM, campaigns, demand gen | `infeara-marketing-expert` |
| Pipeline, proposal, pricing, negotiation, forecast | `infeara-sales-expert` |
| Budget, P&L, cash flow, margin, unit economics | `infeara-cfo` |
| Tech strategy, architecture, build vs buy | `infeara-cto` |
| Operations, delivery, SOPs, capacity | `infeara-coo` |
| Research, prototype, feasibility, innovation | `infeara-rd-expert` |
| Onboarding, retention, renewal, QBR, churn risk | `infeara-client-success-manager` |
| Internal audit, ISO audit, CAPA, findings | `infeara-lead-auditor` |
| Security audit, ISO 27001, SOC 2, risk assessment | `infeara-ciso-auditor` |
| Cloud, AWS/Azure/GCP, migration, cloud cost | `infeara-cloud-associate` |
| CI/CD, Kubernetes, pipelines, monitoring | `infeara-devops-expert` |
| Compliance, policies, audit readiness | `infeara-compliance-manager` |
| Servers, patching, backup, Linux/Windows | `infeara-server-system-admin` |
| Network, VPN, DNS, firewall, latency | `infeara-network-administrator` |
| Threats, vulnerabilities, incident response | `infeara-cyber-security-expert` |
| Contracts, NDA, MSA, SOW, redlines | `infeara-legal-expert` |
| Business plan, org, KPIs, performance reviews | `infeara-business-management-expert` |
| 0-to-1, fundraising, pivot, founding vision | `infeara-founder` |
| Co-founder roles, equity, partnerships | `infeara-cofounder` |
| Google Ads, Meta Ads, PPC, ROAS | `infeara-digital-marketing-expert` |
| Blog, social post, video script, newsletter | `infeara-content-creator-expert` |

## Conventions for Claude in this repo

1. Load the single best-matching skill; chain others only when the task spans domains (e.g. a sales proposal needs Sales + CFO + Legal).
2. Follow each skill's Quality Checklist before delivering.
3. Respect each skill's Guardrails — never invent financials, client facts, evidence, or legal advice.
4. When editing skills, keep frontmatter `name` identical to the folder name and keep `description` trigger-rich (include "Use when…" phrases).
5. Keep each `SKILL.md` under ~120 lines — concise enough to load without bloating context.
