# Prompt Engineering — Beginner to Advanced

A 109-slide teaching deck built entirely from code so the layout stays consistent
and re-buildable. It ships in **two editions that share one layout**:

| Edition | PPTX | Google Slides |
| --- | --- | --- |
| Tamil (English technical terms) | `output/Prompt-Engineering-Tamil-Beginner-to-Advanced.pptx` | [open](https://docs.google.com/presentation/d/14NFWvTor9uNnV8F2QiFyMmDCkBrUwWkU4ak4f6c8x6I/edit) |
| English | `output/Prompt-Engineering-Beginner-to-Advanced-English.pptx` | [open](https://docs.google.com/presentation/d/1sCM0YXgFhgPQMn3v_TMq6bsc5j4uXrLEWLFuskzFRVI/edit) |

Both are 16:9 (13.333 × 7.5 in) with 109 slides; the Google-rendered PDF export of
each is kept beside the PPTX (`…Tamil….pdf`, `…English.pdf`) as the render of record.

## Structure

| Part | Slides |
| --- | --- |
| Front matter (title, course map, objectives, agenda, how to learn) | 6 |
| M01 Introduction · M02 Role → M03 Persona → M04 XML → M05 JSON → M06 Few-Shot | 7 + 6 + 6 each |
| M07 ReAct → M08 Tree of Thoughts → M09 Skeleton of Thoughts → M10 Prompt Chaining | 6 each |
| M11 Dynamic Template → M12 Concepts → M13 Combining → M14 Auto Prompting | 6 + 7 + 8 + 6 |
| Back matter (14-technique summary, selection guide, project brief, plan, outcomes, assessment: MCQ / short answers / practicals / mini project, answer key, close) | 14 |

Every module ends with a learning-outcome slide that hands off to the next module
with its timestamp.

## Layout engine

- `deck/deck_lib.py` — design system (palette, type scale, margins) and the slide
  kinds `cover / concept / wide / split / demo / outcome / statement`, plus the
  visual renderers (`code`, `table`, `flow`, `vflow`, `tree`, `compare`, `cards`,
  `stack`, `nested`, `kv`, `callout`, `grid`, `image`).
- `deck/visuals.py` — diagrams drawn with python-pptx shapes: roadmap, 4-stage
  chain, 8-box assistant architecture (snake), model comparison, pipeline.
- `deck/content_a.py … content_e.py` — slide content as plain dicts.
- `deck/build.py` — assembles, tunes line spacing, saves, and reports overflow
  candidates. `deck/preview.py` — PIL renderer for fast visual QA.

## Build and check

```bash
# Tamil edition
python3 -m deck.build output/Prompt-Engineering-Tamil-Beginner-to-Advanced.pptx   # build + overflow report
python3 -m deck.preview output/Prompt-Engineering-Tamil-Beginner-to-Advanced.pptx /tmp/prev 1,7,96

# English edition (same specs, every string swapped through deck/en_map.json)
python3 -m deck.deck_en output/Prompt-Engineering-Beginner-to-Advanced-English.pptx
```

The English build is a translation layer, not a fork: `deck/deck_en.py` walks the
same slide dicts from `deck.build.all_slides()`, replaces each Tamil string with its
line from `deck/en_map.json` (1 226 entries), applies a handful of edition-specific
`OVERRIDES` (cover subtitle, "keep technical terms in English" advice), asserts
**0 residual Tamil code points** and then runs the normal build + overflow check.
Labels that live inside the layout code (outcome-strip prefix, roadmap captions)
switch through `deck/i18n.py`.

Requirements: `python-pptx`, `Pillow`; Tamil preview needs `Noto Sans Tamil`
(`/home/user/fonts/NotoSansTamil.ttf`) for `deck/preview.py`.

## Two hard-won rules

1. **Line spacing must be calibrated for the renderer.** A paragraph percentage
   is measured against the font's own line height: Google Slides uses 1.20 × size,
   PowerPoint ~1.36 × size for Noto Sans Tamil. `build()` rescales every
   percentage by 1.28 so both land near the layout maths — without this, text that
   fits in the PDF preview spills into the outcome band once imported to Slides.
2. **Monospace code panels are ASCII-only.** Tamil glyphs have no monospace
   coverage, so code samples stay English; `v_code` also rewrites `→` and `…`.
