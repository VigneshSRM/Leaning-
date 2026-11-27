# Lead Scorecard — <lead_id>

> Provisional until the CRM MCP is live. Do not copy PII outside this file.

| Field | Value |
|---|---|
| Lead ID | |
| Received | |
| Source | organic / paid / outbound / referral / partner / event |
| Campaign | |
| Country | |
| Company | |
| Buyer role | |
| Service interest | SVC-`<nn>` |

## Qualification (each 0–5)

| Criterion | Score | Evidence |
|---|---|---|
| ICP fit (sector, size, country) | | |
| Problem clarity (do they name the pain?) | | |
| Urgency (trigger event, deadline) | | |
| Authority (buyer, influencer, researcher) | | |
| Budget signal | | |
| Service match | | |

**Total: __ / 30**

| Score | Band | Action |
|---|---|---|
| 20–30 | SQL | Book with AE within 24h |
| 12–19 | MQL | Nurture sequence + SDR outreach |
| 6–11 | Lead | Content nurture only |
| 0–5 | Disqualify | Reason code required |

## Suggested action

```
ACTION:   <book meeting / nurture / disqualify>
OWNER:    <sdr / ae / content>
BY:       <date>
REASON:   <one line>
DRAFT:    <message, if outreach is proposed — never sent without approval>
```

## Reason code (if disqualified)

`no-fit` · `no-budget` · `competitor` · `bad-timing` · `student` · `vendor` · `duplicate` · `spam`

## Knowledge-base citations used

- `knowledge/services.md` → SVC-`<nn>`
- `knowledge/pricing.md` → quoted? yes / no (only if verified)
- `knowledge/countries.md` → can sell: yes / no / partner

## Escalation

Raise to `infeara-revenue-lead-ops-orchestrator` if: enterprise account, inbound from a named
target, a security/compliance question, or a price request above discount authority.
