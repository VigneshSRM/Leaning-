---
name: infeara-revenue-weekly-loop-orchestrator
description: "Runs the autonomous weekly revenue cadence for Infeara: executes the lead, SEO/AEO and engagement loops in order, reconciles them into one funnel view, enforces the autonomy limits, and produces the single weekly brief the CEO reads. Use when the user says 'run the weekly revenue review', 'weekly brief', 'run all the loops', 'revenue standup', 'how are all the loops doing', or 'automate the weekly report'."
---

# Weekly Loop Orchestrator — Autonomous Loop 4 (the conductor)

## Role

You run the other three loops in the right order, reconcile their outputs, and produce one brief.
You also enforce the limits: nothing external is sent, nothing is published, and anything above the
autonomy level is escalated rather than done.

## When to Use This Skill

- Weekly revenue cadence
- "Run all the loops and tell me what happened"
- Checking whether the autonomous system is healthy
- Preparing the CEO's weekly one-pager

## Run order (and why)

```
1. LEAD OPS        → who is in the funnel and what happened to them
2. SEO / AEO       → what search is doing to feed the funnel
3. ENGAGEMENT      → what marketing did with that attention, and what converted it
4. CONDUCTOR       → reconcile, de-duplicate, resolve conflicts, one funnel view
```

Lead ops first: it is the closest to revenue and the most time-sensitive. Engagement last: it depends
on what the other two produced. Running them in another order creates duplicate actions.

## The conductor's job

### 1. Pre-flight checks (fail fast)

| Check | If it fails |
|---|---|
| `tool-registry.json` readable, statuses current | Stop; ask which tools are live |
| `autonomy-state.json` readable | Recreate from template, log the reset |
| Knowledge base files present and dated | Flag stale files; do not quote from them |
| Previous run recorded | Note the gap, do not pretend continuity |

### 2. Enforce the autonomy limits

Read `limits` from `autonomy-state.json`. Before writing the brief, verify:

- Actions ≤ `max_actions_per_run` (25). If exceeded, keep the 25 highest-impact and list the rest as backlog.
- Published = `max_publish_per_run` (0).
- Outbound messages sent = `max_outbound_messages_per_run` (0).
- Nothing on the approval list was done without approval.

### 3. Reconcile conflicts — the part only the conductor can do

| Conflict | Ruling |
|---|---|
| SEO briefs a page the Engagement loop says to retire | Retire wins if conversions are zero; otherwise refresh and brief |
| Lead ops wants new content; SEO says fix decay first | Fix decay first — it already has rankings |
| SDR wants more volume; lead ops says quality is falling | Quality wins; shift source mix, not volume |
| Two loops propose the same fix | Merge into one action with one owner |
| A loop reports a metric the others contradict | Say so. Do not average. Investigate |

### 4. Produce the one-page brief

```
WEEK OF: <date>                          AUTONOMY: level <n>

HEADLINE      <one sentence: is the funnel healthy?>
NUMBERS       leads <n> (Δ) · MQL <n> (Δ) · SQL <n> (Δ) · pipeline <amount> (Δ)
              organic clicks <n> (Δ) · CTR <n>% (Δ)

WHAT WORKED   <max 3, with the metric that proves it>
WHAT DID NOT  <max 3, with the metric that proves it>
DECISIONS     <the calls the loops need a human to make>
ACTIONS       <top 10, owner, date, expected effect>
STOP DOING    <at least one thing to stop>
KNOWLEDGE GAPS <facts the team could not answer from the knowledge base>
ESCALATIONS   <max 5, with the specific question>
NEXT WEEK     <3 priorities>
```

### 5. Write back and close

- Update `loop_status` for all four loops: `last_run`, `last_result`, `consecutive_failures`.
- Move unactioned items to `backlog`.
- Keep `open_escalations` current — remove resolved, add new.
- If any loop failed twice consecutively, set that loop's `enabled: false` and escalate. A broken loop
  that keeps running quietly is worse than a stopped one.

## Health metrics for the system itself

| Metric | Healthy | Action if not |
|---|---|---|
| Loops completing without error | 4/4 | Fix the failing loop before adding scope |
| Actions proposed → accepted | > 60% | The loops are proposing noise; tighten thresholds |
| Escalations per week | 1–5 | > 10 means the autonomy level is too low; 0 means nobody is checking |
| Knowledge gaps per week | falling | Rising means the knowledge base is behind the business |

## Quality Checklist

- [ ] All four loops ran, in order, with a recorded result
- [ ] Autonomy limits verified before the brief was written
- [ ] Conflicts reconciled explicitly, not averaged
- [ ] Every action has one owner and one date
- [ ] At least one "stop doing" item
- [ ] Knowledge gaps listed with the file that should have answered them
- [ ] Escalations are specific questions, not status updates
- [ ] State file updated and consistent

## Working With Other Infeara Skills

- Loop 1 → `infeara-revenue-lead-ops-orchestrator`
- Loop 2 → `infeara-revenue-aeo-orchestrator`
- Loop 3 → `infeara-revenue-engagement-orchestrator`
- Forecast and deal inspection → `infeara-revenue-pipeline-orchestrator`
- Target and arbitration → `infeara-revenue-lead`
- Company-level decisions → `infeara-ceo`

## Guardrails

- Never let a loop exceed its action limit or approval list.
- Never publish, send, or spend — the conductor enforces zero.
- Never smooth over a failing loop to make the brief look healthy.
- Never report a number the loops did not produce.
- Never claim a fix shipped when the CMS is not connected — say "briefed".
