---
title: Infeara Completed Projects
owner: infeara-team-account-manager
last_updated: 2026-11-22
status: draft
access: restricted
used_by: [infeara-revenue-proposal-manager, infeara-revenue-product-marketing, infeara-revenue-aeo-answers, infeara-team-account-manager]
---

# Infeara — Completed Projects

**Restricted.** This tracked file is a template: all values are `[VERIFY]`. Real client names and
outcomes belong in `knowledge/local/projects.md`, which is gitignored. Every claim in a proposal, case study, or answer-engine page must trace to a row here.

## Reference permission — the hard gate

| Value | Meaning |
|---|---|
| `yes` | May be named publicly (case study, website, proposal) |
| `anonymised` | May be described without the name ("a UAE retail bank") |
| `no` | Internal only — may not appear in any outbound artefact |
| `pending` | Ask the account manager; treat as `no` until granted |

A project with `permission_to_reference: pending` must be quoted as `anonymised` at most.

## Project log

| ID | Client | Country | Service IDs | Sector | Duration | Outcome (quantified) | Permission | Case study |
|---|---|---|---|---|---|---|---|---|
| `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | pending | `[VERIFY]` |
| `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | pending | `[VERIFY]` |

## Case study template (one file per approved project)

Path: `knowledge/case-studies/<client-slug>.md`

```
---
client: <name or "anonymised">
country: <ISO>
sector: <sector>
services: [SVC-01]
permission_to_reference: yes
last_updated: <date>
---

# <Client> — <outcome in six words>

## Context         (2 sentences: who they are, what was at stake)
## Problem         (what was broken, with the number)
## Approach        (what we did, in 3–4 steps, no product names)
## Result          (quantified outcome; before → after)
## Client quote    (verbatim, approved, with name and title)
## What we would do differently   (honest; builds credibility)
```

Rules:
- No outcome without a number, and no number without a source.
- A quote requires written approval from the client, stored alongside the file.
- Anonymised case studies still need the sector and country to be useful — but never a
  combination so specific it identifies the client.

## Proof inventory

| Proof type | Count available | Where |
|---|---|---|
| Named case studies | `[VERIFY]` | `knowledge/case-studies/` |
| Anonymised case studies | `[VERIFY]` | `knowledge/case-studies/` |
| Client quotes | `[VERIFY]` | `knowledge/case-studies/` |
| Certifications | `[VERIFY]` | `about.md` |
| Referenceable clients | `[VERIFY]` | `projects.md` |
