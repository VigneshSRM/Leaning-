# Prompt Engineering — Beginner to Advanced (Tamil)

A 109-slide teaching deck in Tamil (English technical terms), built entirely from
code so the layout stays consistent and re-buildable.

- **Deliverable:** `output/Prompt-Engineering-Tamil-Beginner-to-Advanced.pptx`
  (16:9, 13.333 × 7.5 in, 109 slides)
- Google Slides copy: <https://docs.google.com/presentation/d/14NFWvTor9uNnV8F2QiFyMmDCkBrUwWkU4ak4f6c8x6I/edit>

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
python3 -m deck.build output/Prompt-Engineering-Tamil-Beginner-to-Advanced.pptx   # build + overflow report
python3 -m deck.preview output/Prompt-Engineering-Tamil-Beginner-to-Advanced.pptx /tmp/prev 1,7,96
```

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
