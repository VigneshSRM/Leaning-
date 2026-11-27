# SEO / AEO Run — <YYYY-MM-DD>

Source: `google-search-console` MCP (`status: live`) · Owner: `infeara-revenue-seo-specialist`

## 1. Data pulled

| Metric | This period | Previous | Change |
|---|---|---|---|
| Clicks | | | |
| Impressions | | | |
| Average CTR | | | |
| Average position | | | |
| Indexed pages | | | |
| Pages with errors | | | |

Queries pulled: __ · Pages pulled: __ · Date range: __

## 2. Drops that matter (not vanity)

| Query / page | Before | After | Δ | Likely cause | Confidence |
|---|---|---|---|---|---|
| | | | | | |

Alert thresholds from `autonomy-state.json`: CTR drop > 20%, position drop > 5.

## 3. Opportunities — the "striking distance" list

Pages ranking 5–20 with above-average impressions: these are the cheapest wins in search.

| Query | Page | Position | Impressions | Action | Owner |
|---|---|---|---|---|---|
| | | | | rewrite title / add section / internal link / new page | |

## 4. AEO checks

| Check | Status | Fix |
|---|---|---|
| Every priority page answers its target question in the first sentence | | |
| JSON-LD Organization block present and valid | | |
| `knowledge/aeo-answers.md` answers match the live pages | | |
| FAQ sections present on service pages | | |
| No price published (unless `public_pricing_allowed: yes`) | | |

## 5. Technical findings

| Issue | Severity | Pages affected | Fix | Owner |
|---|---|---|---|---|
| | high / medium / low | | | |

## 6. Actions proposed this run

| # | Action | Type | Owner | Approval needed? |
|---|---|---|---|---|
| 1 | | content / technical / schema / internal link | | yes / no |

## 7. Handoffs

- Content briefs → `infeara-revenue-content-manager` (see `integrations/outbox/content/`)
- Schema/technical → `infeara-revenue-seo-specialist` → `infeara-team-implementation-engineer` when CMS MCP is live
- Commercial signal (high-intent queries) → `infeara-revenue-sdr` for account targeting

## 8. Result line (written back to autonomy-state.json)

```
loop: seo-aeo | run: <date> | actions: <n> | published: 0 (approval gated) | escalations: <n>
```
