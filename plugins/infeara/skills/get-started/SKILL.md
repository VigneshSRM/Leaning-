---
name: get-started
description: "Start here on first use of the Infeara plugin, or when the user asks what the plugin can do, which expert or team handles a topic, or says 'infeara', 'which skill', 'who should handle this', 'what can you do', 'list your experts'. Explains the CEO-as-entry-point routing model and routes the request."
---

# Infeara — Getting Started

Infeara bundles 23 expert skills, a 10-role delivery team and a 15-person sales and marketing team — 55 skills in total — with a lead and orchestrator for each team, plus four autonomous loops. Each one carries its own playbooks, templates, quality checklist, and guardrails. This skill routes a request to the right expert and explains what the plugin can do.

## How to use the plugin

**The CEO is the front door.** Any task that spans more than one function goes to `infeara-ceo`, which
decomposes it, assigns internal roles, sequences handoffs, and returns one consolidated answer.

```
Task arrives
  ├─ single-domain question?  → route straight to that one skill
  ├─ names a skill?           → honour it, no orchestration
  └─ multi-function / project / "handle this" / "get the team on it"
                              → infeara-ceo (delegates to internal team, consolidates)
```

1. **Triage the request** using the table below.
2. **Multi-function work goes to the CEO**, not to ten separate skills answering in parallel.
3. **Single-domain work routes direct.** Read `skills/<name>/SKILL.md` and follow it — its playbooks, deliverables, and checklists take priority over general habits.
4. **Chain only when needed.** A sales proposal may need Sales + CFO + Legal. Name handoffs explicitly instead of blending voices.
5. **Attribute delegated findings.** Say which role produced which conclusion; never present a delegate's work as your own analysis.
6. **Apply the guardrails.** Never invent financials, client facts, evidence, or legal advice; mark unknowns as `[VERIFY]`.

If the user names an expert ("use the Infeara CFO skill"), load it directly. If a project arrives without
a named owner, start with `infeara-ceo`. If the request is ambiguous between two experts, ask one short question rather than guessing.

Full delegation protocol: `../infeara-ceo/references/ceo-delegation-protocol.md` (from the `infeara-ceo` skill folder).

## Routing table

### Start here

| The request sounds like… | Skill |
|---|---|
| Strategy, vision, board, M&A, executive decision | `infeara-ceo` |
| **Multi-function task, project, "handle this", "get the team on it", "who does what"** | **`infeara-ceo`** |
| Which skill handles something / how routing works | `infeara-guide` |

### Expert personas

| The request sounds like… | Skill |
|---|---|
| Positioning, go-to-market, campaigns, demand generation | `infeara-marketing-expert` |
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

### Delivery team — when the ask is a project, not a question

| The request sounds like… | Skill |
|---|---|
| "Assemble a team", "who does what", "run this end-to-end", "deliver this" | `infeara-team-lead` |
| Sprint plan, stand-up, retro, backlog, team cadence | `infeara-sprint-orchestrator` |
| Scope, discovery, requirements, change request, sign-off | `infeara-team-engagement-manager` |
| Solution design, architecture, ADRs, feasibility | `infeara-team-solution-architect` |
| Engineering standards, task breakdown, code review | `infeara-team-tech-lead` |
| Write code, fix a defect, unit tests | `infeara-team-implementation-engineer` |
| Test plan, acceptance testing, defects | `infeara-team-qa-engineer` |
| Release, deploy, rollback, environments | `infeara-team-deployment-engineer` |
| Runbooks, handover pack, user guides | `infeara-team-documentation-analyst` |
| Threat model, security review, security sign-off | `infeara-team-security-analyst` |
| Project plan, schedule, milestones, risks, status | `infeara-team-project-manager` |
| Client health, renewal, expansion, escalation | `infeara-team-account-manager` |

### Autonomous loops — they run themselves (4)

| The request sounds like… | Skill |
|---|---|
| "Process these leads", "score the inbound" | `infeara-revenue-lead-ops-orchestrator` |
| "Run SEO", "why did traffic drop", "AEO check" | `infeara-revenue-aeo-orchestrator` |
| "What content works", "nurture", "engagement report" | `infeara-revenue-engagement-orchestrator` |
| "Run all the loops", "weekly brief" | `infeara-revenue-weekly-loop-orchestrator` |

### Revenue team — sales and marketing (15)

| The request sounds like… | Skill |
|---|---|
| "Build a sales and marketing team", revenue plan, GTM org | `infeara-revenue-lead` |
| Pipeline review, funnel analysis, forecast, conversion | `infeara-revenue-pipeline-orchestrator` |
| Segmentation, positioning, launch, pricing input | `infeara-revenue-gtm-strategist` |
| Messaging, battlecards, sales enablement, proof | `infeara-revenue-product-marketing` |
| Brand voice, visual identity, brand audit | `infeara-revenue-brand-manager` |
| Content strategy, editorial calendar, production | `infeara-revenue-content-manager` |
| Campaigns, launches, webinars, events | `infeara-revenue-campaign-manager` |
| SEO, organic, landing pages | `infeara-revenue-seo-specialist` |
| Tracking, attribution, lead scoring, martech | `infeara-revenue-marketing-ops` |
| Cold outreach, prospecting, qualifying | `infeara-revenue-sdr` |
| Deal strategy, discovery, demo, close | `infeara-revenue-account-executive` |
| POC, technical validation, pre-sales scoping | `infeara-revenue-solutions-consultant` |
| Sales process, CRM, forecast mechanics, territories | `infeara-revenue-sales-ops` |
| RFP, proposal, bid decision, compliance matrix | `infeara-revenue-proposal-manager` |
| Partners, channel, resellers, alliances | `infeara-revenue-partnerships-manager` |

## Common multi-expert chains

- **New offer** → Founder (is the bet worth it?) → CFO (does it pay?) → Marketing (how do we position it?) → Sales (can we sell it?) → Legal (what are we promising?).
- **Enterprise client** → Sales (deal) → Legal (contract) → COO (delivery) → Client Success (retention) → CISO Auditor (security questionnaire).
- **Client-facing report** → subject expert (audit/finance/security content) → Document Writer (cover, pagination, brand, PDF).
- **Multi-function task** → CEO triages, decomposes into workstreams, assigns one lead each, consolidates the answer. The user sees one reply, not ten.
- **Full engagement** → Team Lead assembles the ten roles; Engagement Manager scopes → Architect designs → Tech Lead builds → QA verifies → Deployment releases → Documentation hands over → Account Manager closes and grows. Sprint Orchestrator runs the weekly rhythm.
- **Revenue target** → Revenue Lead sets target and funnel maths; GTM Strategist picks segments → Product Marketing writes the message → Brand/Content/SEO/Campaigns create demand → Marketing Ops tracks and scores → SDR qualifies → Account Executive closes → Proposal Manager handles bids → Partnerships adds channel. Pipeline Orchestrator runs the weekly review.
- **Single-role ask** ("write the code", "plan the sprint") → go straight to that team role skill, not the Team Lead.
- **Incident** → Cyber Security (contain) → DevOps (restore) → Compliance (notify) → Legal (exposure) → Client Success (communicate).
- **Pricing change** → CFO (model) → Sales (pipeline impact) → Marketing (packaging) → Legal (terms).

## What the plugin cannot do

- It runs on packaged instructions only: no network calls, no data storage, no live systems access.
- It does not sign contracts, file with regulators, or replace licensed professionals. Drafts require human review.
- It will not fabricate numbers, evidence, or client facts. Missing inputs become explicit assumptions or `[VERIFY]` flags.
