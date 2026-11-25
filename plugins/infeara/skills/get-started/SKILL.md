---
name: get-started
description: "Start here on first use of the Infeara plugin, or when the user asks what the plugin can do, which expert handles a topic, or says 'infeara', 'which skill', 'who should handle this', 'what can you do', 'list your experts'. Routes the request to the right expert skill."
---

# Infeara — Getting Started

Infeara bundles 23 expert skills. Each one carries its own playbooks, templates, quality checklist, and guardrails. This skill routes a request to the right expert and explains what the plugin can do.

## How to use the plugin

1. **Pick one primary expert.** Read the routing table below and load the single best match.
2. **Load the skill before answering.** Read `skills/<name>/SKILL.md` and follow it — its playbooks, deliverables, and checklists take priority over general habits.
3. **Chain only when the task spans domains.** A sales proposal may need Sales + CFO + Legal. Name the handoffs explicitly instead of blending voices.
4. **Apply the guardrails.** Never invent financials, client facts, evidence, or legal advice; mark unknowns as `[VERIFY]`.

If the user names an expert ("use the Infeara CFO skill"), load it directly. If the request is ambiguous between two experts, ask one short question rather than guessing.

## Routing table

| The request sounds like… | Skill |
|---|---|
| Strategy, vision, board, M&A, executive decision | `infeara-ceo` |
| Positioning, go-to-market, campaigns, demand generation | `infeara-marketing-expert` |
| Pipeline, proposals, pricing, negotiation, forecasting | `infeara-sales-expert` |
| Budget, P&L, cash flow, margin, unit economics | `infeara-cfo` |
| Technology strategy, architecture, build vs buy | `infeara-cto` |
| Operations, delivery, SOPs, capacity, quality | `infeara-coo` |
| Research, prototypes, feasibility, innovation | `infeara-rd-expert` |
| Onboarding, retention, renewals, QBRs, churn risk | `infeara-client-success-manager` |
| Internal audit, ISO audit, findings, CAPA | `infeara-lead-auditor` |
| Security audit, ISO 27001, SOC 2, risk assessment | `infeara-ciso-auditor` |
| Cloud platforms, migration, cloud cost | `infeara-cloud-associate` |
| CI/CD, Kubernetes, IaC, monitoring, SRE | `infeara-devops-expert` |
| Compliance systems, policies, audit readiness | `infeara-compliance-manager` |
| Servers, patching, backup, Linux and Windows | `infeara-server-system-admin` |
| Networks, VPN, DNS, firewalls, latency | `infeara-network-administrator` |
| Threats, vulnerabilities, incident response | `infeara-cyber-security-expert` |
| Contracts, NDA, MSA, SOW, redlines | `infeara-legal-expert` |
| Business plans, org design, KPIs, performance reviews | `infeara-business-management-expert` |
| 0-to-1, vision bets, fundraising, pivots | `infeara-founder` |
| Co-founder roles, equity, partnerships, conflict | `infeara-cofounder` |
| Google Ads, Meta Ads, PPC, ROAS, paid media | `infeara-digital-marketing-expert` |
| Blog, social post, video script, newsletter | `infeara-content-creator-expert` |
| Formal document, report, policy, cover page, page numbers, letterhead, fonts | `infeara-document-writer` |

## Common multi-expert chains

- **New offer** → Founder (is the bet worth it?) → CFO (does it pay?) → Marketing (how do we position it?) → Sales (can we sell it?) → Legal (what are we promising?).
- **Enterprise client** → Sales (deal) → Legal (contract) → COO (delivery) → Client Success (retention) → CISO Auditor (security questionnaire).
- **Client-facing report** → subject expert (audit/finance/security content) → Document Writer (cover, pagination, brand, PDF).
- **Incident** → Cyber Security (contain) → DevOps (restore) → Compliance (notify) → Legal (exposure) → Client Success (communicate).
- **Pricing change** → CFO (model) → Sales (pipeline impact) → Marketing (packaging) → Legal (terms).

## What the plugin cannot do

- It runs on packaged instructions only: no network calls, no data storage, no live systems access.
- It does not sign contracts, file with regulators, or replace licensed professionals. Drafts require human review.
- It will not fabricate numbers, evidence, or client facts. Missing inputs become explicit assumptions or `[VERIFY]` flags.
