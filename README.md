# Handwritten OOAD Assignment

`OOAD_Assignment_2_Vignesh_M.pdf` was a machine-typeset PDF (ReportLab, DejaVu Sans /
Helvetica / Courier). This repo rebuilds it as a document that reads as **hand-written**:
no system font appears anywhere in the output, and the page is composed the way a person
actually writes on ruled sheets.

## Output

| File | Look |
| --- | --- |
| `output/OOAD_Assignment_2_Vignesh_M_handwritten.pdf` | **Indie Flower**, ruled notebook paper, phone-scanned |
| `output/OOAD_Assignment_2_Vignesh_M_handwritten_plain.pdf` | Indie Flower, blank paper, phone-scanned |

Type sizes are fixed as requested: **16 pt for headings, 14 pt for body text**,
on a 22 pt rule. The cover page carries no border or ruling.

Both are JPEG-per-page scans at 160 dpi, exactly like the output of a scanner
app. `--no-scan` writes the clean vector master instead (selectable text, ~100 KB).

## What makes it read as handwriting

* **Real handwriting typefaces** — [Indie Flower](https://github.com/google/fonts/tree/main/ofl/indieflower)
  by default, with [Caveat](https://github.com/google/fonts/tree/main/ofl/caveat) and
  [Kalam](https://github.com/google/fonts/tree/main/ofl/kalam) as alternates. All are SIL Open
  Font License pen-drawn designs, not "casual" system fonts.
* **Baselines sit on the ruled lines** — every text baseline is snapped to a 22 pt rule, so
  the writing looks ruled-in rather than pasted on top.
* **Hand tremor** — each line gets a small random tilt (±0.22°), baseline drift and word-spacing
  jitter, so no two lines are perfectly parallel.
* **Varying ink density** — the pen colour alternates between four near-identical blue-blacks.
* **Freehand diagram** — the deployment diagram is drawn as vector strokes with jittered
  edges, not ASCII art in a monospace font.
* **Plain cover** — no border, no ruling, just centred writing.
* **Phone-scan optics** (`scanify.py`) — the vector pages are rasterised and put
  through the chain a phone camera imposes: warm paper, uneven lighting with a
  directional falloff, lens vignette, paper mottling, sensor grain, warm cast and
  a touch of optical softness. This is what sells it as a scan rather than a render.
* **No system font is referenced** — the PDF embeds only the handwriting faces used.
  Verify with `pdffonts output/*.pdf`.

## Regenerate

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt

.venv/bin/python make_handwritten.py                        # Indie Flower, ruled, scanned
.venv/bin/python make_handwritten.py --plain                # blank paper, scanned
.venv/bin/python make_handwritten.py --font kalam           # Kalam hand
.venv/bin/python make_handwritten.py --font caveat          # Caveat hand
.venv/bin/python make_handwritten.py --no-scan              # clean vector output
.venv/bin/python make_handwritten.py --scan-strength 1.4    # heavier shading
.venv/bin/python make_handwritten.py --dpi 200 --quality 90 # sharper scan
.venv/bin/python make_handwritten.py --out foo.pdf          # custom path
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
