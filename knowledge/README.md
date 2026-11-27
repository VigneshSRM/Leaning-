---
title: Infeara Knowledge Base
owner: infeara-ceo
last_updated: 2026-11-22
status: draft
used_by: [all skills]
---

# Infeara Knowledge Base — Rules and Index

This folder is the **only permitted source of company facts** for every skill in this repository.
If a fact is not here, the agent does not know it. It must then ask, or mark the answer `[VERIFY]`.
It must never fill the gap from plausibility.

## The five rules

1. **No fact outside these files.** Anything about Infeara's identity, services, prices, countries,
   clients, or completed work comes from here — never from memory, never from inference.
2. **One fact, one home.** Do not duplicate a number across files. Cross-reference instead
   (`see pricing.md`) so there is a single place to change it.
3. **Status gates use.** `draft` → internal working only. `verified` → may be used in outbound
   content. `stale` → must be re-confirmed before use.
4. **Pricing and client references are restricted.** A price is quotable only if its row is
   `verified` and the requester is authorised. A client may be named only if
   `permission_to_reference: yes` in `projects.md`.
5. **Every edit is dated and owned.** Update `last_updated` and set `status: draft` until re-verified.

## Index

| File | Answers | Primary consumers |
|---|---|---|
| `about.md` | Who we are, legal entity, HQ, leadership, credentials | `document-writer`, `proposal-manager`, `brand-manager` |
| `overview.md` | What we do in one paragraph, pillars, positioning | `product-marketing`, `gtm-strategist`, `campaign-manager` |
| `services.md` | What we sell, for whom, deliverables, duration | `solutions-consultant`, `proposal-manager`, `sdr` |
| `pricing.md` | Bands, models, what is included, quote rules | `cfo`, `account-executive`, `proposal-manager` |
| `countries.md` | Where we operate, entity, currency, time zone | `gtm-strategist`, `account-executive`, `legal-expert` |
| `projects.md` | Completed work, outcomes, reference permission | `proposal-manager`, `product-marketing`, `aeo-answers` |
| `aeo-answers.md` | Canonical citable answers for answer engines | `seo-specialist`, `content-manager`, `sdr` |

## Completion checklist

- [ ] Every `[VERIFY]` resolved or deliberately left, with an owner and a due date
- [ ] `status: verified` set on files used for outbound content
- [ ] Every completed project has a `permission_to_reference` decision
- [ ] Pricing reviewed and approved by the CFO
- [ ] Country list reconciled with legal entity and tax registrations
- [ ] `last_updated` current on every file

## How the skills load this

Skills never quote the raw file. They extract the specific fact, cite the file, and carry the status:

```
Answer: Managed SOC starts at [VERIFY] per month (source: knowledge/pricing.md, status: draft).
Because that row is not verified, I can give you the band and mark the exact figure for finance
to confirm before it goes to the client.
```

Machine-readable index: `integrations/tool-registry.json` → `knowledge_base.documents`.

## Real values live in `knowledge/local/`

This repository is **public**. Every tracked file here contains `[VERIFY]` placeholders and no real
figures. Real prices and client names must never be committed.

```
knowledge/local/pricing.md      # real rate card — gitignored
knowledge/local/projects.md    # real client list — gitignored
knowledge/local/about.md       # real entity details — gitignored
```

**Resolution order:** `knowledge/local/<file>` first, then `knowledge/<file>`. A skill reads the
local override when present and the template otherwise. If neither answers, the fact is unknown:
ask, or mark `[VERIFY]`. Never fill a gap with a plausible number.

Set up the override:

```bash
mkdir -p knowledge/local
cp knowledge/pricing.md knowledge/local/pricing.md   # then fill it in privately
```

On a shared machine or a private fork, keep `knowledge/local/` out of every archive and export.
