# Handwritten OOAD Assignment

`OOAD_Assignment_2_Vignesh_M.pdf` was a machine-typeset PDF (ReportLab, DejaVu Sans /
Helvetica / Courier). This repo rebuilds it as a document that reads as **hand-written**:
no system font appears anywhere in the output, and the page is composed the way a person
actually writes on ruled sheets.

## Output

| File | Look |
| --- | --- |
| `output/OOAD_Assignment_2_Vignesh_M_handwritten.pdf` | Caveat handwriting, ruled notebook paper |
| `output/OOAD_Assignment_2_Vignesh_M_handwritten_kalam.pdf` | Kalam handwriting (upright, Indian hand), ruled paper |
| `output/OOAD_Assignment_2_Vignesh_M_handwritten_plain.pdf` | Caveat handwriting, blank paper |

## What makes it read as handwriting

* **Real handwriting typefaces** — [Caveat](https://github.com/google/fonts/tree/main/ofl/caveat)
  and [Kalam](https://github.com/google/fonts/tree/main/ofl/kalam), both under the SIL Open
  Font License. They are pen-drawn designs, not "casual" system fonts.
* **Baselines sit on the ruled lines** — every text baseline is snapped to a 29 pt rule, so
  the writing looks ruled-in rather than pasted on top.
* **Hand tremor** — each line gets a small random tilt (±0.22°), baseline drift and per-word
  wobble, so no two lines are perfectly parallel.
* **Varying ink density** — the pen colour alternates between four near-identical blue-blacks.
* **Freehand diagram** — the deployment diagram is drawn as vector strokes with jittered
  edges, not ASCII art in a monospace font.
* **No system font is referenced** — the PDF embeds only the three Caveat faces (or the two
  Kalam faces). Verify with `pdffonts output/*.pdf`.

## Regenerate

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt

.venv/bin/python make_handwritten.py                 # Caveat, ruled paper
.venv/bin/python make_handwritten.py --font kalam    # Kalam, ruled paper
.venv/bin/python make_handwritten.py --plain         # blank paper
.venv/bin/python make_handwritten.py --out foo.pdf   # custom path
```

`make_handwritten.py` holds the assignment text as a structured block list (questions,
sections, sub-headings, paragraphs, bullet lists, diagram), and a small layout engine that
flows those blocks over ruled pages with keep-with-next rules so headings never end up
stranded at the foot of a page.

## Fonts

`assets/fonts/` contains the OFL-licensed TTFs plus their licence texts.

Caveat ships from Google Fonts only as a variable font, so the three static weights are
instanced from it and then renamed with `tools/fix_caveat_names.py`. That rename matters:
fontTools leaves every instance reporting the PostScript name `Caveat-Regular`, and a PDF
producer that keys embedded subsets by that name silently collapses bold and regular into a
single face.

## Note

The document is typeset from the original's text verbatim (only the ASCII deployment diagram
was redrawn). If your course requires physically hand-written submission, check that a
handwriting typeface is acceptable before using this.
