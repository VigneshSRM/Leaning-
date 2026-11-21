# -*- coding: utf-8 -*-
"""Custom, content-specific diagrams (roadmap, chaining, architecture)."""
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from .deck_lib import (INK, BODY, MUTED, ACCENT, ACCENT_D, RULE, PANEL, WHITE, CODEBG,
                       FONT, MONO, rect, textbox, add_para, write, arrow, hline, shape_text)
from .i18n import t as tr



def _chip(sl, x, y, w, h, num, name, ts, strong=False):
    rect(sl, x, y, w, h, fill=PANEL if not strong else WHITE,
         line=ACCENT if strong else RULE, lw=1.1 if strong else 0.8)
    tb = textbox(sl, x + 0.10, y + 0.08, w - 0.18, h - 0.12)
    p = add_para(tb.text_frame, first=True, line=1.0, space_after=1)
    write(p, num, 7.8, ACCENT, bold=True, font=MONO)
    p = add_para(tb.text_frame, line=1.10, space_after=1)
    write(p, name, 8.6, INK, bold=True)
    p = add_para(tb.text_frame, line=1.0)
    write(p, ts, 7.2, MUTED, font=MONO)


def roadmap(sl, x, y, w, h):
    bands = [
        ("BEGINNER", "Modules 01–04", [
            ("01", "Introduction", tr("AI, Prompt, அமைப்பு", "AI, Prompt, structure"), "00:00"),
            ("02", "Role", tr("நிபுணர் வேடம்", "Expert role"), "03:40"),
            ("03", "Persona", tr("பேசும் பாணி", "Speaking style"), "05:27"),
            ("04", "XML", tr("tag கட்டமைப்பு", "tag structure"), "07:59")]),
        ("INTERMEDIATE", "Modules 05–10", [
            ("05", "JSON", "structured output", "10:29"),
            ("06", "Few-Shot", tr("உதாரணங்கள்", "Examples"), "14:25"),
            ("07", "ReAct", tr("சிந்தனை + tool", "reasoning + tools"), "16:23"),
            ("08", "Tree of Thoughts", tr("பல வழிகள்", "Several paths"), "19:39"),
            ("09", "Skeleton of Thoughts", tr("outline + விரிவு", "outline + expansion"), "22:12"),
            ("10", "Prompt Chaining", tr("படிநிலை இணைப்பு", "Staged chaining"), "24:55")]),
        ("ADVANCED", "Modules 11–14", [
            ("11", "Dynamic Template", tr("மாறி (variables)", "Values as variables"), "27:38"),
            ("12", "Concepts", tr("சிறந்த நடைமுறை", "Best practice"), "28:50"),
            ("13", "Combining", tr("கலந்த அணுகுமுறை", "Mixed approach"), "31:39"),
            ("14", "Auto Prompting", tr("AI எழுதும் prompt", "AI writes the prompt"), "35:59")]),
    ]
    label_w = 1.22
    band_h = (h - 0.26) / 3
    chip_h = min(band_h, 0.80)
    for bi, (title, sub, items) in enumerate(bands):
        by = y + bi * (band_h + 0.13)
        cy = by + (band_h - chip_h) / 2
        tb = textbox(sl, x, by + band_h / 2 - 0.32, label_w - 0.14, 0.66, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.05, space_after=3)
        write(p, title, 9.4, ACCENT_D, bold=True)
        p = add_para(tb.text_frame, line=1.1)
        write(p, sub, 7.6, MUTED)
        ax = x + label_w
        aw = w - label_w
        gap = 0.10
        n = len(items)
        cw = (aw - gap * (n - 1)) / n
        for i, (num, nm, desc, ts) in enumerate(items):
            bx = ax + i * (cw + gap)
            rect(sl, bx, cy, cw, chip_h, fill=WHITE if bi == 2 else PANEL,
                 line=ACCENT if bi == 2 else RULE, lw=1.0 if bi == 2 else 0.8)
            rect(sl, bx, cy, cw, 0.05, fill=ACCENT)
            tb = textbox(sl, bx + 0.10, cy + 0.11, cw - 0.18, chip_h - 0.14)
            p = add_para(tb.text_frame, first=True, line=1.0, space_after=1)
            write(p, [(num + "  ", dict(size=8.0, color=ACCENT, bold=True, font=MONO)),
                      (nm, dict(size=9.0, color=INK, bold=True))], 9.0)
            p = add_para(tb.text_frame, line=1.12, space_after=1)
            write(p, desc, 7.8, MUTED)
            p = add_para(tb.text_frame, line=1.0)
            write(p, ts, 7.2, MUTED, font=MONO)


def chain(sl, x, y, w, h):
    """4-stage prompt chain: each stage shows its job and the artifact it hands over."""
    stages = [
        ("Stage 1", "Data Analysis", "compute numbers only", "analysis table"),
        ("Stage 2", "Insight Generation", "5 insights, each citing a number", "5 insights"),
        ("Stage 3", "Recommendations", "exactly 3 actions + impact", "3 actions"),
        ("Stage 4", "Final Report", "1-page report, formal tone", "report.md"),
    ]
    n = len(stages)
    gap = 0.30
    bw = (w - gap * (n - 1)) / n
    cap_h = 0.34
    avail = h - cap_h - 0.06
    bh = min(1.55, avail - 0.55)
    block = bh + 0.44
    top = y + 0.06 + max(0.0, (avail - block) / 2.0)
    for i, (k, t, focus, art) in enumerate(stages):
        bx = x + i * (bw + gap)
        rect(sl, bx, top, bw, bh, fill=WHITE, line=ACCENT, lw=1.0)
        rect(sl, bx, top, bw, 0.045, fill=ACCENT)
        tb = textbox(sl, bx + 0.14, top + 0.10, bw - 0.26, bh - 0.16, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.0, space_after=5)
        write(p, k, 8.0, ACCENT, bold=True, font=MONO)
        p = add_para(tb.text_frame, line=1.12, space_after=5)
        write(p, t, 11.0, INK, bold=True)
        p = add_para(tb.text_frame, line=1.18)
        write(p, focus, 8.6, BODY)
        ac = rect(sl, bx, top + bh + 0.14, bw, 0.28, fill=PANEL, line=RULE, lw=0.7)
        shape_text(ac, [(art, dict(size=7.8, color=BODY, font=MONO))])
        if i < n - 1:
            ay = top + bh / 2
            arrow(sl, bx + bw + 0.05, ay, bx + bw + gap - 0.05, ay, ACCENT, 1.2)
    tb = textbox(sl, x, y + h - cap_h + 0.06, w, cap_h)
    p = add_para(tb.text_frame, first=True)
    write(p, "The small chip is the output that stage hands to the next one. That is chaining.",
          8.8, MUTED, italic=True)


def arch_assistant(sl, x, y, w, h):
    """Snake layout: 4 steps left-to-right, then wrap down to a second row."""
    row1 = [("1", "User Request", tr("IT ticket / கேள்வி", "IT ticket / question")),
            ("2", "Role + Persona", "XML blocks"),
            ("3", "Few-Shot", "3 labeled examples"),
            ("4", "JSON Output", "category, priority, draft")]
    row2 = [("5", "Validate", "schema check"),
            ("6", "Ticket System", "DB / ITSM log"),
            ("7", "Dynamic Template", "tone + variables"),
            ("8", "Reply to User", tr("Tamil + English", "English reply"))]
    gap = 0.24
    bh = 1.02
    bw = (w - gap * 3) / 4
    y1 = y + 0.10 + max(0.0, (h - (2 * bh + 0.60)) / 2.0)
    y2 = y1 + bh + 0.58
    for i, (num, t, sub) in enumerate(row1 + row2):
        if i < 4:
            bx = x + i * (bw + gap)
            by, fill = y1, WHITE
        else:
            bx = x + (i - 4) * (bw + gap)
            by, fill = y2, PANEL
        rect(sl, bx, by, bw, bh, fill=fill, line=RULE, lw=0.9)
        rect(sl, bx, by, bw, 0.045, fill=ACCENT)
        tb = textbox(sl, bx + 0.13, by + 0.12, bw - 0.24, bh - 0.18, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.0, space_after=3)
        write(p, num, 8.0, ACCENT, bold=True, font=MONO)
        p = add_para(tb.text_frame, line=1.12, space_after=3)
        write(p, t, 10.4, INK, bold=True)
        p = add_para(tb.text_frame, line=1.16)
        write(p, sub, 8.0, MUTED)
        if i in (0, 1, 2, 4, 5, 6):
            arrow(sl, bx + bw + 0.04, by + bh / 2, bx + bw + gap - 0.04, by + bh / 2, MUTED, 1.0)
    # wrap connector: end of row 1 -> start of row 2
    x_from = x + 3 * (bw + gap) + bw / 2
    x_to = x + bw / 2
    mid = y1 + bh + 0.29
    c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x_from), Inches(y1 + bh),
                                Inches(x_from), Inches(mid))
    c.line.color.rgb = MUTED
    c.line.width = Pt(1)
    c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x_to), Inches(mid),
                                Inches(x_from), Inches(mid))
    c.line.color.rgb = MUTED
    c.line.width = Pt(1)
    arrow(sl, x_to, mid, x_to, y2 - 0.02, MUTED, 1.0)


def model_compare(sl, x, y, w, h):
    """Zero / one / few-shot comparison as three stacked output strips."""
    cols = ["Zero-Shot", "One-Shot", "Few-Shot"]
    rows = [
        (tr("Prompt-ல் examples", "Examples in prompt"), "0", "1", "3–5"),
        (tr("Output நம்பகத்தன்மை", "Output reliability"), tr("குறைவு", "Low"), tr("நடுத்தரம்", "Medium"), tr("அதிகம்", "High")),
        (tr("Format பின்பற்றுதல்", "Format compliance"), tr("குறைவு", "Low"), tr("நடுத்தரம்", "Medium"), tr("அதிகம்", "High")),
        (tr("Token செலவு", "Token cost"), tr("குறைவு", "Low"), tr("சிறிது", "Some"), tr("அதிகம்", "High")),
    ]
    from pptx.util import Emu
    tbl_shape = sl.shapes.add_table(len(rows) + 1, 4, Inches(x), Inches(y), Inches(w), Inches(h))
    tbl = tbl_shape.table
    tbl.first_row = False
    tbl.horz_banding = False
    widths = [0.40, 0.20, 0.20, 0.20]
    for i, fr in enumerate(widths):
        tbl.columns[i].width = Emu(int(Inches(w) * fr))
    hdr = ["", "Zero-Shot", "One-Shot", "Few-Shot"]
    for r in range(len(rows) + 1):
        tbl.rows[r].height = Inches(h / (len(rows) + 1))
        vals = hdr if r == 0 else [rows[r - 1][0]] + list(rows[r - 1][1:])
        for c in range(4):
            cell = tbl.cell(r, c)
            cell.margin_left = Inches(0.08)
            cell.margin_right = Inches(0.06)
            cell.margin_top = Inches(0.03)
            cell.margin_bottom = Inches(0.03)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            cell.fill.fore_color.rgb = INK if r == 0 else (WHITE if r % 2 else PANEL)
            p = cell.text_frame.paragraphs[0]
            p.line_spacing = 1.06
            write(p, vals[c], 9.4,
                  WHITE if r == 0 else (INK if c == 0 else BODY), bold=(r == 0 or c == 0))
            from .deck_lib import _cell_borders
            _cell_borders(cell, "FFFFFF" if r == 0 else "DCE3EC", 0.75)


def pipeline(sl, x, y, w, h):
    """App → Prompt → LLM → JSON → validate → database."""
    nodes = [("App / UI", "user action"), ("Prompt Template", "variables filled"),
             ("LLM API", "JSON mode"), ("Parse + Validate", "JSON schema"),
             ("Database", "structured data")]
    gap = 0.26
    n = len(nodes)
    bw = (w - gap * (n - 1)) / n
    bh = 1.15
    top = y + 0.18
    for i, (t, s) in enumerate(nodes):
        bx = x + i * (bw + gap)
        rect(sl, bx, top, bw, bh, fill=PANEL if i % 2 == 0 else WHITE, line=RULE, lw=0.9,
             shape_type=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.10)
        tb = textbox(sl, bx + 0.08, top + 0.12, bw - 0.16, bh - 0.2)
        p = add_para(tb.text_frame, first=True, line=1.12, space_after=2)
        write(p, t, 9.4, INK, bold=True)
        p = add_para(tb.text_frame, line=1.1)
        write(p, s, 7.6, MUTED)
        if i < n - 1:
            ay = top + bh / 2
            arrow(sl, bx + bw + 0.03, ay, bx + bw + gap - 0.03, ay, MUTED, 1.0)
    tb = textbox(sl, x, y + h - 0.32, w, 0.32)
    p = add_para(tb.text_frame, first=True)
    write(p, tr("JSON output இருந்தால் மட்டுமே application அதை நம்பகமாக பயன்படுத்த முடியும்.",
           "Only when the output is JSON can an application use it reliably."), 8.8, MUTED, italic=True)
