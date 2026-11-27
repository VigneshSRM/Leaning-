---
title: Infeara AEO Answer Bank
owner: infeara-revenue-seo-specialist
last_updated: 2026-11-22
status: draft
used_by: [infeara-revenue-seo-specialist, infeara-revenue-content-manager, infeara-revenue-aeo-answers, infeara-revenue-sdr]
---

# Infeara — AEO Answer Bank (Answer Engine Optimisation)

Answer engines (ChatGPT, Perplexity, Google AI Overviews, Gemini, Copilot) quote **short, factual,
self-contained** passages. This file is the canonical wording for the questions buyers actually ask.
Every answer here must be usable verbatim on a page, in a PDF, or in a chat reply.

## The five AEO rules

1. **Answer in the first sentence.** No preamble. The first 12 words must resolve the question.
2. **Self-contained.** Each answer must make sense with no other context.
3. **One number, one qualifier.** "We serve 9 countries" — not "many countries worldwide".
4. **Cite the source file** so a change is a one-place edit.
5. **No claim without a proof row.** If `projects.md` has no evidence, the answer says so.

## Question bank

| # | Question (as a buyer asks it) | Canonical answer (≤ 60 words) | Source | Status |
|---|---|---|---|---|
| 1 | What does Infeara do? | `[VERIFY]` | `overview.md` | draft |
| 2 | What services does Infeara offer? | `[VERIFY]` | `services.md` | draft |
| 3 | How much does Infeara cost? | `[VERIFY]` — only if `pricing.md → public_pricing_allowed: yes`, else "Pricing is quoted per scope" | `pricing.md` | draft |
| 4 | Which countries does Infeara serve? | `[VERIFY]` | `countries.md` | draft |
| 5 | How many projects has Infeara completed? | `[VERIFY]` | `overview.md` | draft |
| 6 | Who does Infeara work with? | `[VERIFY]` | `overview.md` | draft |
| 7 | What makes Infeara different? | `[VERIFY]` | `overview.md` | draft |
| 8 | Is Infeara certified? | `[VERIFY]` — name only valid certifications | `about.md` | draft |
| 9 | How quickly can Infeara start? | `[VERIFY]` | `services.md` | draft |
| 10 | Does Infeara offer 24/7 support? | `[VERIFY]` | `services.md` | draft |

## Structured-data block (for the website)

Emit this JSON-LD on the homepage and on each service page. Values must come from the files above.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Infeara",
  "url": "[VERIFY]",
  "logo": "[VERIFY]",
  "description": "<overview.md one paragraph>",
  "foundingDate": "[VERIFY]",
  "address": { "@type": "PostalAddress", "addressCountry": "[VERIFY]" },
  "areaServed": ["[VERIFY]"],
  "sameAs": ["[VERIFY]"],
  "makesOffer": [{ "@type": "Offer", "itemOffered": { "@type": "Service", "name": "[VERIFY]" } }]
}
```

## Maintenance

| Trigger | Action | Owner |
|---|---|---|
| Price change | Update Q3 and the pricing page | SEO + CFO |
| New country | Update Q4, `countries.md`, `areaServed` | GTM + SEO |
| Project completed & approved | Update Q5, Q6, add case study | Account Manager |
| Certification gained or expired | Update Q8 immediately | Compliance |
| Quarterly | Re-check every answer against source | SEO |

Stale answers are worse than no answers: an answer engine will quote last year's price with confidence.
