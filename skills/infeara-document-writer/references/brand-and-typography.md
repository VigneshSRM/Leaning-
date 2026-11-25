# Infeara Document Standards — Brand, Type, and Pagination

Companion reference for `infeara-document-writer`. Use it when a document needs a decision
that the SKILL.md summary does not cover.

## 1. Brand tokens

```
--brand-blue-900   #024F86    primary: headings, rules, footer bar start
--brand-blue-700   #0462AB    secondary: subheads, links, footer bar end
--brand-orange-500 #FD6F33    accent: tagline, key figures, active rule
--brand-orange-700 #CE430A    deep accent: gradient end, emphasis
--ink              #1E293B    body text
--ink-muted        #334155    secondary text, captions
--surface          #F1F5F9    contact strip, table zebra, callouts
--rule             #E2E8F0    hairlines, table borders
--paper            #FFFFFF    page ground

signature gradient: 90deg, #024F86 0%, #0462AB 40%, #FD6F33 70%, #CE430A 100%
```

Proportion of use per page: **blue 60% · white 25% · surface/neutral 10% · orange 5%.**
If a page has two orange elements, one is wrong.

### Contrast (WCAG 2.1)

| Pair | Ratio | Use |
|---|---|---|
| `#1E293B` on `#FFFFFF` | 13.0:1 | body text ✓ |
| `#024F86` on `#FFFFFF` | 7.1:1 | headings, links ✓ |
| `#0462AB` on `#FFFFFF` | 5.6:1 | subheads ✓ |
| `#CE430A` on `#FFFFFF` | 4.8:1 | large text, labels ✓ |
| `#FD6F33` on `#FFFFFF` | 2.9:1 | **large/bold display only** — never body text |
| `#FFFFFF` on `#024F86` | 7.1:1 | reversed footer text ✓ |

## 2. Type

**Stack:** `'Segoe UI', 'Helvetica Neue', Arial, sans-serif` — Segoe UI ships with Windows and
renders identically in Word/PowerPoint; Helvetica Neue covers macOS; Arial is the last resort.
For long-form print over 20 pages, pair with Georgia or Source Serif for body only.

| Level | Size | Weight | Leading | Space before |
|---|---|---|---|---|
| Cover title | 32–40 pt | 600 | 1.10 | — |
| Subtitle | 13–14 pt | 400 | 1.35 | 6 mm |
| H1 / section | 20–24 pt | 600 | 1.20 | new page |
| H2 | 13–15 pt | 600 | 1.30 | 7 mm |
| H3 | 11–12 pt | 600 | 1.35 | 5 mm |
| Body | 10.5–11 pt | 400 | 1.50–1.55 | 3 mm |
| Table | 9–10 pt | 400/600 head | 1.35 | — |
| Caption | 8.5–9 pt | 400/600 label | 1.40 | — |
| Footer | 8–9 pt | 400 | 1.30 | — |

Rules:
- Track body at 0 to +5; never track-out body text. Uppercase labels: +80 to +220 (0.08–0.22 em).
- Justify only with hyphenation enabled. Default to ragged-right.
- One blank line = 1 × body leading. Never stack blank lines to push content down.
- Curly quotes, en dashes for ranges (–), em dashes for asides (—), no space around em dash in Indian English house style is optional — pick one and keep it.
- Indian number format for INR amounts (₹ 4,25,000); ISO dates where space is tight (2026-11-22), long form in letters (22 November 2026).

## 3. Page geometry

A4 = 210 × 297 mm. US Letter = 216 × 279 mm (only if the client requires it).

| Template | Margins (T/R/B/L) | Content width | Measure |
|---|---|---|---|
| Letter | 12 / 15 / 12 / 15 mm + header/footer bands | 180 mm | ~92 chars at 10.5 pt (widen side padding to 32 mm for readability) |
| Report | 26 / 20 / 30 / 20 mm | 170 mm | ~72 chars at 10.5 pt ✓ |
| Policy / SOP | 25 / 22 / 28 / 22 mm | 166 mm | ~70 chars ✓ |
| Landscape data | 20 / 18 / 24 / 18 mm | 238 mm | wide tables only |

- Safe zone: keep all content ≥ 12 mm from trim; ≥ 15 mm for anything with a bleed.
- Footer reserve: 100 mm bottom padding on the letterhead (footer is absolutely positioned).
- Baseline grid: 4.5 mm (12.75 pt) at 10.5 pt / 1.55 leading. Snap headings to it.
- Widows/orphans ≥ 2 lines. Headings never last on a page (`break-after: avoid`).
- Tables: repeat `<thead>` on every page; never split a row.

## 4. Pagination conventions

| Section | Numbering | Footer |
|---|---|---|
| Cover | none | none |
| Document control, TOC | i, ii, iii (roman, lowercase) | roman, bottom right |
| Body | 1, 2, 3 (arabic, restart at 1) | `Page X of Y` |
| Appendices | continue arabic | `Page X of Y` |

- Major H1 sections start on a new page (recto for print-bound documents if duplex printing).
- Section numbering: `1`, `1.1`, `1.1.1` — maximum three levels. Never number the executive summary's subsections.
- Figures `Figure <section>.<n>`, tables `Table <section>.<n>`, appendices `A`, `A.1`.
- Cross-references: "see §4.2", "Table 3.1", "Appendix A" — never "see above".
- Blank pages (if required for recto starts) carry the footer and the line "This page is intentionally blank."

## 5. CSS print rules (HTML → PDF)

```css
@page {
  size: A4;
  margin: 26mm 20mm 30mm 20mm;
  @top-left   { content: "INFEARA  ·  <Document title>"; font-size: 8pt; color: #64748b; }
  @bottom-left{ content: "<Classification>  ·  info@infeara.com"; font-size: 8pt; }
  @bottom-right { content: "Page " counter(page) " of " counter(pages); font-size: 8pt; color: #024F86; }
}
@page :first { margin: 0; @top-left{content:none} @bottom-right{content:none} }

h1, h2, h3, h4 { break-after: avoid; break-inside: avoid; }
table, figure, .callout { break-inside: avoid; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
p { orphans: 2; widows: 2; }
.new-page { break-before: page; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
```

Chrome/Edge print-to-PDF supports `@page` margin boxes and counter(pages). Firefox does **not**
support named margin boxes — for Firefox or Word delivery, put the page footer in the Word
header/footer field instead (`Page { PAGE } of { NUMPAGES }`).

## 6. Word / DOCX equivalents

| HTML/CSS | Word |
|---|---|
| `@page` margins | Layout → Margins → Custom |
| `@top-left` running head | Header — insert document title + section field |
| `Page X of Y` | Insert → Field → Page / NumPages |
| H1 on new page | Paragraph → Page break before |
| `break-inside: avoid` | Table Properties → Row → "Allow row to break across pages" off |
| Section numbering | Multilevel list linked to Heading 1–3 |
| TOC | References → Table of Contents (update fields before export) |

## 7. File and version naming

```
INFEARA_<TYPE>_<CLIENT>_<TITLE>_v<MAJOR.MINOR>_<YYYYMMDD>.pdf

INFEARA_RPT_Acme_CloudReadiness_v1.0_20261122.pdf
INFEARA_POL_Internal_DataRetention_v2.1_20261122.pdf
INFEARA_SOP_Internal_IncidentResponse_v1.3_20261122.pdf
```

Types: `RPT` report · `PRO` proposal · `POL` policy · `SOP` procedure · `WPR` whitepaper ·
`BRF` brief · `PLN` plan · `AUD` audit report · `LTR` letter · `CTR` contract layout.

Version rules: `0.x` draft, `1.0` first approved issue, increment minor for edits, major for
scope changes. Never overwrite an issued version — supersede it.

## 8. Accessibility and production checks

- Real heading elements in order (no skipped levels); TOC generated from them.
- Alt text on every figure: what it shows + why it matters, ≤ 120 characters.
- Tables have header rows and captions; never use tables for layout in accessible documents.
- Don't put essential text in images; don't rely on colour alone (pair orange with a label or icon).
- PDF: set title/author/subject/keywords; enable tagged PDF where the tool allows.
- Test print at 100% on A4, and in greyscale: hierarchy must survive without colour.
