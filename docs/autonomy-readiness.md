# Infeara Revenue Autonomy — Readiness and Gap Report

Status as of 2026-11-22. Regenerate with: `python3 scripts/validate-plugin.py`

## 1. What is wired today

| Component | State | Notes |
|---|---|---|
| Google Search Console | **live** | query/page/country analytics, URL inspection, sitemaps |
| Infeara CRM | **staged** | MCP not yet delivered — CSV export fallback defined and enforced |
| Website CMS | **staged** | MCP not yet delivered — Markdown drafts, human publishes |
| Knowledge base | **draft** | all 8 files exist; facts need filling and verification |
| Autonomous loops | **built** | 4 skills, limits enforced, state file present |
| Autonomy level | **1** | analyse + suggest only; publish 0, send 0 |

## 2. What each loop does today vs after the MCPs land

| Loop | Today (level 1) | After CRM MCP | After CMS MCP |
|---|---|---|---|
| **Lead ops** | reads CSV export, scores, routes, drafts messages, writes suggestions to `outbox/` | reads leads directly, writes status + reason codes back, reacts to `lead.created` events | — |
| **SEO/AEO** | pulls live GSC, briefs content and technical fixes | joins organic landing pages to pipeline in the CRM | creates drafts in the CMS, applies schema, pings sitemap after human approval |
| **Engagement** | analyses exports, drafts nurture, flags warm signals | reads site behaviour and deal data, hands signals to SDR with deal context | reads page performance directly, creates A/B test drafts |
| **Conductor** | runs all three, reconciles, one brief | adds pipeline and forecast to the brief | adds publish status and verification dates |

## 3. The honest gaps — what stops full autonomy

### Gap 1 — the knowledge base is empty of facts (blocking)

Every file has `[VERIFY]` placeholders. Until they are filled:
- the SDR cannot pitch accurately,
- the proposal manager cannot write a compliant bid,
- AEO answers cannot be published,
- any quoted price is a fabrication risk.

**Fix:** 2–3 hours with the CEO, CFO and Legal filling `about`, `overview`, `services`, `pricing`,
`countries`. Then set `status: verified`.

### Gap 2 — no CRM MCP (expected, planned)

Leads arrive as files, so the loop is scheduled rather than event-driven, and write-backs are
suggestions. This is a friction cost, not a correctness cost.

**Fix:** ship the MCP with the six capabilities listed in `tool-registry.json`. Minimum viable:
`leads.list`, `leads.update`, `activities.create`, `events.subscribe`.

### Gap 3 — no CMS MCP (expected, planned)

Content cannot be published by the team, so the SEO loop stops at "briefed". Verification still works
because Search Console sees the page once a human publishes it.

**Fix:** ship the MCP with draft-create (not publish). Do not give the agent publish rights initially.

### Gap 4 — no outbound channel (deliberate)

`max_outbound_messages_per_run: 0`. Sending is the highest-risk action in the system.

**Fix:** raise to a small number only after 4 weeks of drafts that a human reviewed with <10% edits.
Then route through an approved sending tool with unsubscribe and suppression handling.

### Gap 5 — attribution is undefined (blocking for revenue claims)

Without an attribution model, the loops can report traffic but cannot honestly claim pipeline.

**Fix:** CFO and Marketing Ops choose one model (first-touch for demand, last-touch for conversion),
write it in `marketing-ops`, and stamp it on every report.

### Gap 6 — no scheduled execution (environment)

The loops need a scheduler to run unattended.

**Fix:** see §4. Until then, a human triggers the conductor weekly.

## 4. Scheduling the loops

The skills are instructions, not daemons. Something must invoke them on a schedule. Three options,
cheapest first:

| Option | Setup | Good for |
|---|---|---|
| **Manual trigger** | ask "run the weekly loops" every Monday | week 1–4, while prompts are tuned |
| **Scheduled agent run** | a scheduled job that opens the repo and runs the conductor prompt, writes the brief to `integrations/outbox/weekly/` | ongoing, zero infrastructure |
| **Full daemon** | a service that polls the CRM, reacts to `lead.created`, calls the model, writes back | after the CRM MCP ships and volume justifies it |

Recommended sequence: manual for 4 weeks → scheduled conductor → event-driven lead loop only.

## 5. Raising autonomy safely

| Level | Name | Team may | Requires |
|---|---|---|---|
| 1 | Advise | analyse, draft, suggest | default now |
| 2 | Assist | + write CRM status/reason codes, create CMS drafts | 4 clean weeks at level 1 |
| 3 | Act | + publish approved templates, send approved sequences | human review rate < 10% for 4 weeks |
| 4 | Operate | + adjust budgets within caps, A/B test autonomously | quarterly audit, kill switch tested |

Never skip a level, and never grant level 3 without the stop conditions in §6 working.

## 6. Stop conditions (must be live before level 2)

| Condition | Trigger | Action |
|---|---|---|
| Wrong price quoted | any message with a price not in `pricing.md` at `verified` | halt loop, notify CFO |
| Client named without permission | any outbound artefact naming a `pending` client | halt, notify Legal |
| PII leak | lead data outside `integrations/` | halt, delete, notify CEO |
| Loop failure | 2 consecutive runs fail | disable that loop, escalate |
| Metric anomaly | any loop's key metric moves > 40% week over week | halt and investigate before acting |
| Cost cap | token or API spend > monthly cap | halt |

## 7. What to do this week

1. Fill `knowledge/about.md`, `overview.md`, `countries.md` — CEO, 60 minutes.
2. Fill `knowledge/services.md` and `pricing.md` — CFO + Solutions Consultant, 90 minutes.
3. Add 3 completed projects to `projects.md` with reference permission — Account Manager.
4. Run `infeara-revenue-weekly-loop-orchestrator` manually once and review the brief.
5. Send the CRM and CMS capability lists from `tool-registry.json` to whoever is building the MCPs.
