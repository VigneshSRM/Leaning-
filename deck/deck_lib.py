# -*- coding: utf-8 -*-
"""Design system + layout engine for the Tamil Prompt Engineering deck.

White background, flat, minimal academic style. One accent colour + neutrals.
All text uses "Noto Sans Tamil" (Latin + Tamil coverage); code uses "Roboto Mono".
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml
from lxml import etree

# ---------------------------------------------------------------- palette
INK      = RGBColor(0x11, 0x18, 0x27)
BODY     = RGBColor(0x33, 0x3D, 0x4D)
MUTED    = RGBColor(0x5B, 0x66, 0x77)
ACCENT   = RGBColor(0x1D, 0x4E, 0xD8)
ACCENT_D = RGBColor(0x15, 0x3F, 0xA8)
RULE     = RGBColor(0xD8, 0xDF, 0xE8)
PANEL    = RGBColor(0xF6, 0xF8, 0xFB)
CODEBG   = RGBColor(0xF5, 0xF7, 0xFA)
CODEBAR  = RGBColor(0xEC, 0xF0, 0xF6)
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
GOODBG   = RGBColor(0xEE, 0xF4, 0xFF)
BADBG    = RGBColor(0xF7, 0xF7, 0xF8)

FONT = "Noto Sans Tamil"
MONO = "Roboto Mono"

SW, SH = 13.333, 7.5          # slide size, inches
M      = 0.7                  # page margin
CW     = SW - 2 * M           # content width  = 11.933

# vertical rhythm
Y_KICK   = 0.40
Y_TITLE  = 0.62
Y_RULE   = 1.40
Y_SUM    = 1.58
Y_BODY   = 2.62
Y_BOT    = 6.38               # body content must end by here
Y_OUT    = 6.55
Y_FOOT   = 7.12


# ---------------------------------------------------------------- low level
def _rgb(hex_or_color):
    return hex_or_color if isinstance(hex_or_color, RGBColor) else RGBColor.from_string(hex_or_color)


def new_deck():
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)
    return prs


def blank(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg = s.background.fill
    bg.solid()
    bg.fore_color.rgb = WHITE
    return s


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    return tb


def _style_run(run, size, color=INK, bold=False, italic=False, font=FONT):
    f = run.font
    f.name = font
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.color.rgb = color


def add_para(tf, first=False, space_before=0, space_after=0, line=1.22, align=PP_ALIGN.LEFT):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.line_spacing = line
    p.space_before = Pt(space_before)
    p.space_after = Pt(space_after)
    return p


def hang(p, indent_in, first_out=0.0):
    """Set a hanging indent so wrapped lines align under the text, not the marker."""
    pPr = p._pPr if p._pPr is not None else p.get_or_add_pPr()
    pPr.set("marL", str(int(Inches(indent_in))))
    pPr.set("indent", str(int(Inches(first_out))))


def write(p, chunks, size, color=INK, bold=False, font=FONT, italic=False):
    """chunks: str or list of (text, dict(size=,color=,bold=,italic=,font=))"""
    if isinstance(chunks, str):
        chunks = [(chunks, {})]
    for text, kw in chunks:
        r = p.add_run()
        r.text = text
        _style_run(r, kw.get("size", size), kw.get("color", color), kw.get("bold", bold),
                   kw.get("italic", italic), kw.get("font", font))
    return p


def rect(slide, x, y, w, h, fill=None, line=None, lw=1.0, shape_type=MSO_SHAPE.RECTANGLE,
         radius=None, dash=None):
    sh = slide.shapes.add_shape(shape_type, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.shadow.inherit = False
    if radius is not None and shape_type == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            sh.adjustments[0] = radius
        except Exception:
            pass
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = _rgb(fill)
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = _rgb(line)
        sh.line.width = Pt(lw)
        if dash:
            sh.line.dash_style = dash
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return sh


def shape_text(sh, lines, pad=0.06):
    """lines: list of (text, dict(size,bold,color,italic,space_after,line,font))"""
    tf = sh.text_frame
    for i, (txt, kw) in enumerate(lines):
        p = add_para(tf, first=(i == 0), space_after=kw.get("space_after", 0),
                     line=kw.get("line", 1.1))
        write(p, txt, kw.get("size", 11), kw.get("color", INK), kw.get("bold", False),
              kw.get("font", FONT), kw.get("italic", False))
    return sh


def hline(slide, x, y, w, color=RULE, weight=0.75):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x), Inches(y),
                                   Inches(x + w), Inches(y))
    c.line.color.rgb = _rgb(color)
    c.line.width = Pt(weight)
    return c


def arrow(slide, x1, y1, x2, y2, color=MUTED, weight=1.0, dash=None):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1),
                                   Inches(x2), Inches(y2))
    c.line.color.rgb = _rgb(color)
    c.line.width = Pt(weight)
    if dash:
        c.line.dash_style = dash
    ln = c._element.spPr.get_or_add_ln()
    tail = etree.SubElement(ln, qn("a:tailEnd"))
    tail.set("type", "triangle")
    tail.set("w", "sm")
    tail.set("len", "sm")
    return c


# ---------------------------------------------------------------- text metrics
def est_lines(text, width_in, size_pt, cpi=0.55):
    cpl = max(6, int(width_in * 72.0 / (cpi * size_pt)))
    n = 0
    for seg in str(text).split("\n"):
        words = seg.split(" ")
        cur = 0
        n += 1
        for wd in words:
            add = len(wd) + (1 if cur else 0)
            if cur + add > cpl and cur:
                n += 1
                cur = len(wd)
            else:
                cur += add
    return n


def choose_size(items, width_in, height_in, sizes, line=1.25, space_after=6, cpi=0.55):
    """items: list of plain strings. Pick the largest size whose wrapped block fits."""
    for sz in sizes:
        total = 0.0
        for t in items:
            total += est_lines(t, width_in, sz, cpi) * sz * line / 72.0 + space_after / 72.0
        if total <= height_in:
            return sz
    return sizes[-1]


# ---------------------------------------------------------------- page chrome
try:                      # optional: real glyph metrics for headline fitting
    from PIL import ImageFont
except Exception:         # pragma: no cover
    ImageFont = None

_MEAS_FONT = "/home/user/fonts/NotoSansTamil.ttf"
_meas_cache = {}


def text_width_in(text, size):
    """Rendered width in inches; falls back to the character-count model."""
    key = (text, size)
    if key in _meas_cache:
        return _meas_cache[key]
    if ImageFont is None:
        w = est_lines_width_fallback(text, size)
    else:
        try:
            f = ImageFont.truetype(_MEAS_FONT, int(round(size * 4)))
            w = f.getlength(text) / 4.0 / 72.0
        except Exception:
            w = est_lines_width_fallback(text, size)
    _meas_cache[key] = w
    return w


def est_lines_width_fallback(text, size):
    return len(str(text)) * 0.55 * size / 72.0


def fit_title(text, sizes=(30, 27, 24, 22, 20), width=None):
    """Largest headline size that keeps the title on a single line.

    Tamil headlines draw ~15% wider in Google Slides than the regular face
    measures (real bold weights, different shaping), so they get a bigger
    safety factor than Latin-only titles.
    """
    width = CW if width is None else width
    tamil = any(ord(ch) > 0x0B00 for ch in text)
    safety = 1.14 if tamil else 1.06
    for sz in sizes:
        if text_width_in(text, sz) * safety <= width:
            return sz
    return sizes[-1]


def header(slide, kicker, title, title_size=None):
    if kicker:
        tb = textbox(slide, M, Y_KICK, CW, 0.24)
        p = add_para(tb.text_frame, first=True)
        write(p, kicker.upper(), 10, ACCENT, bold=True)
    size = title_size or fit_title(title)
    tb = textbox(slide, M, Y_TITLE, CW, 0.78, anchor=MSO_ANCHOR.TOP)
    p = add_para(tb.text_frame, first=True, line=1.05)
    write(p, title, size, INK, bold=True)
    rect(slide, M, Y_RULE, 1.05, 0.05, fill=ACCENT)


def summary(slide, lines, y=Y_SUM, h=0.82, size=14.5):
    rect(slide, M, y + 0.03, 0.035, h - 0.10, fill=ACCENT)
    tb = textbox(slide, M + 0.24, y, CW - 0.24, h)
    for i, ln in enumerate(lines):
        p = add_para(tb.text_frame, first=(i == 0), line=1.22, space_after=3)
        write(p, ln, size, BODY)


def footer(slide, num, label="Prompt Engineering · Beginner to Advanced"):
    hline(slide, M, 7.02, CW, RULE, 0.6)
    tb = textbox(slide, M, Y_FOOT, 8.0, 0.22)
    p = add_para(tb.text_frame, first=True)
    write(p, label, 8.5, MUTED)
    tb = textbox(slide, SW - M - 1.2, Y_FOOT, 1.2, 0.22)
    p = add_para(tb.text_frame, first=True, align=PP_ALIGN.RIGHT)
    write(p, str(num), 9, MUTED, bold=True)


def outcome_strip(slide, text, y=Y_OUT):
    hline(slide, M, y - 0.10, CW, RULE, 0.75)
    tb = textbox(slide, M, y, CW, 0.5)
    p = add_para(tb.text_frame, first=True, line=1.15)
    write(p, [("இந்த Topic-க்குப் பிறகு:  ", dict(size=11, color=ACCENT, bold=True)),
              (text, dict(size=11, color=INK))], 11)


# ---------------------------------------------------------------- bullets
def bullets(slide, items, x, y, w, h, size=None, gap=9, rule_color=None):
    flat = []
    for it in items:
        flat.append(it if isinstance(it, str) else it[0] + " " + it[1])
    size = size or choose_size(flat, w - 0.32, h, [15.5, 15, 14.5, 14, 13, 12.5, 12, 11.5], space_after=gap)
    tb = textbox(slide, x, y, w, h)
    for i, it in enumerate(items):
        p = add_para(tb.text_frame, first=(i == 0), space_after=gap, line=1.24)
        hang(p, 0.26, -0.26)
        # accent dash marker
        write(p, "—  ", size, ACCENT, bold=True)
        if isinstance(it, str):
            write(p, it, size, BODY)
        else:
            head, detail = it
            write(p, head, size, INK, bold=True)
            if detail:
                write(p, "  " + detail, size, BODY)
    return size


def numbered(slide, items, x, y, w, h, size=None, gap=8):
    flat = [t if isinstance(t, str) else t[0] for t in items]
    size = size or choose_size(flat, w - 0.5, h, [15, 14.5, 14, 13.5, 13, 12.5, 12], space_after=gap)
    tb = textbox(slide, x, y, w, h)
    for i, it in enumerate(items):
        p = add_para(tb.text_frame, first=(i == 0), space_after=gap, line=1.24)
        hang(p, 0.40, -0.40)
        write(p, [("%02d  " % (i + 1), dict(size=size, color=ACCENT, bold=True, font=MONO)),
                  (it, dict(size=size, color=BODY))], size)
    return size


# ---------------------------------------------------------------- visuals
def render(slide, spec, x, y, w, h):
    t = spec["type"]
    fn = {
        "code": v_code, "table": v_table, "flow": v_flow, "vflow": v_vflow,
        "tree": v_tree, "compare": v_compare, "cards": v_cards, "stack": v_stack,
        "nested": v_nested, "kv": v_kv, "image": v_image, "grid": v_grid,
        "callout": v_callout, "custom": lambda s, sp, X, Y, W, H: sp["fn"](s, X, Y, W, H),
    }[t]
    return fn(slide, spec, x, y, w, h)


def code_metrics(lines, w, h):
    """Pick a monospace size that fits the box, then return (size, content_height)."""
    maxlen = max([len(l) for l in lines] or [1])
    size = min(12.5, (w - 0.34) * 72.0 / (0.62 * max(20, maxlen)))
    size = max(7.6, size)
    while size > 7.4 and len(lines) * size * 1.30 / 72.0 > h - 0.46:
        size -= 0.25
    return size, len(lines) * size * 1.30 / 72.0 + 0.22


def v_code(slide, spec, x, y, w, h):
    lines = [l.replace("\u2192", "->").replace("\u2026", "...") for l in spec["lines"]]
    label = spec.get("label")
    bar = 0.30 if label else 0.0
    size, need = code_metrics(lines, w, h)
    hh = min(h, need + bar)
    rect(slide, x, y, w, hh, fill=spec.get("bg", CODEBG))
    if label:
        rect(slide, x, y, w, bar, fill=CODEBAR)
        tb = textbox(slide, x + 0.14, y + 0.055, w - 0.28, 0.2)
        p = add_para(tb.text_frame, first=True)
        write(p, label, 8.5, MUTED, bold=True)
    tb = textbox(slide, x + 0.15, y + bar + 0.09, w - 0.28, hh - bar - 0.12)
    for i, ln in enumerate(lines):
        p = add_para(tb.text_frame, first=(i == 0), line=1.30, space_after=0)
        hl = spec.get("highlight")
        col = INK if (hl is None or i in hl or hl == "all") else MUTED
        is_comment = ln.lstrip().startswith("#")
        if is_comment:
            col = ACCENT
        write(p, ln if ln else " ", size, col, font=MONO,
              bold=is_comment or (hl is not None and (i in hl if hl != "all" else False)))
    return hh


def v_table(slide, spec, x, y, w, h):
    data = spec["rows"]
    rows, cols = len(data), len(data[0])
    fracs = spec.get("widths") or [1.0 / cols] * cols
    size = spec.get("size", 10)
    tbl_shape = slide.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(h))
    tbl = tbl_shape.table
    tbl.first_row = False
    tbl.horz_banding = False
    for i, f in enumerate(fracs):
        tbl.columns[i].width = Emu(int(Inches(w) * f))
    head_h = min(0.46, h / rows)
    body_h = (h - head_h) / max(1, rows - 1)
    for r in range(rows):
        tbl.rows[r].height = Inches(head_h if r == 0 else body_h)
        for c in range(cols):
            cell = tbl.cell(r, c)
            cell.margin_left = Inches(0.09)
            cell.margin_right = Inches(0.07)
            cell.margin_top = Inches(0.035)
            cell.margin_bottom = Inches(0.035)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if r == 0:
                cell.fill.fore_color.rgb = INK
            else:
                cell.fill.fore_color.rgb = WHITE if r % 2 else PANEL
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.line_spacing = 1.08
            txt = str(data[r][c])
            bold = (r == 0) or (c == 0 and spec.get("bold_first_col", True))
            write(p, txt, size if r else size - 0.2,
                  WHITE if r == 0 else (INK if bold else BODY), bold=bold)
            _cell_borders(cell, "FFFFFF" if r == 0 else "DCE3EC", 0.75)
    return tbl


def _cell_borders(cell, color, weight):
    tcPr = cell._tc.get_or_add_tcPr()
    for i, tag in enumerate(["a:lnL", "a:lnR", "a:lnT", "a:lnB"]):
        for e in tcPr.findall(qn(tag)):
            tcPr.remove(e)
        ln = etree.Element(qn(tag))
        ln.set("w", str(int(weight * 12700)))
        ln.set("cap", "flat")
        ln.set("cmpd", "sng")
        ln.set("algn", "ctr")
        fill = etree.SubElement(ln, qn("a:solidFill"))
        clr = etree.SubElement(fill, qn("a:srgbClr"))
        clr.set("val", color)
        dash = etree.SubElement(ln, qn("a:prstDash"))
        dash.set("val", "solid")
        tcPr.insert(i, ln)


def v_flow(slide, spec, x, y, w, h, vertical=False):
    nodes = spec["nodes"]
    n = len(nodes)
    cap = spec.get("caption")
    cap_h = 0.34 if cap else 0
    gap = 0.30
    nw = (w - gap * (n - 1)) / n
    # hug the text: two short lines need ~0.9in, not the full band
    need = 0.0
    for nd in nodes:
        if isinstance(nd, str):
            nd = {"t": nd}
        t_lines = max(1, int(text_width_in(nd["t"], nd.get("size", 10.5)) / (nw - 0.26)) +
                      (1 if text_width_in(nd["t"], nd.get("size", 10.5)) % (nw - 0.26) else 0))
        sub = 1 if nd.get("s") else 0
        need = max(need, 0.34 + t_lines * 0.21 + sub * 0.19)
    nh = min(1.46, max(1.15, need))
    title_h = 0.30 if spec.get("title") else 0
    group = title_h + nh + (0.16 + cap_h if cap else 0)
    top = y + max(0.0, (h - group) / 2) + title_h
    if spec.get("title"):
        tb = textbox(slide, x, y + max(0.0, (h - group) / 2), w, 0.26)
        p = add_para(tb.text_frame, first=True)
        write(p, spec["title"], 9.5, MUTED, bold=True)
    for i, nd in enumerate(nodes):
        nx = x + i * (nw + gap)
        if isinstance(nd, str):
            nd = {"t": nd}
        fill = PANEL if not nd.get("strong") else GOODBG
        line = ACCENT if nd.get("strong") else RULE
        box = rect(slide, nx, top, nw, nh, fill=fill, line=line, lw=0.9,
                   shape_type=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.10)
        boost = max(0.0, nh - 1.10)
        lines = [(nd["t"], dict(size=nd.get("size", 10.5 + boost * 3.2), bold=True, color=INK, line=1.16))]
        if nd.get("s"):
            lines.append((nd["s"], dict(size=nd.get("ssize", 8.6 + boost * 2.0), color=MUTED,
                                        space_after=0, line=1.18)))
        shape_text(box, lines)
        if i < n - 1:
            ay = top + nh / 2
            arrow(slide, nx + nw + 0.045, ay, nx + nw + gap - 0.045, ay, MUTED, 1.0)
    if cap:
        tb = textbox(slide, x, top + nh + 0.14, w, 0.34)
        p = add_para(tb.text_frame, first=True, line=1.15)
        write(p, cap, 8.8, MUTED, italic=True)


def v_vflow(slide, spec, x, y, w, h):
    steps = spec["steps"]
    cap = spec.get("caption")
    cap_h = 0.34 if cap else 0
    n = len(steps)
    gap = spec.get("gap", 0.13)
    rh = (h - cap_h - gap * (n - 1)) / n
    for i, st in enumerate(steps):
        sy = y + i * (rh + gap)
        if isinstance(st, str):
            st = {"t": st}
        rect(slide, x, sy, w, rh, fill=PANEL if i % 2 == 0 else WHITE, line=RULE, lw=0.75)
        chip = 0.27
        rect(slide, x + 0.11, sy + (rh - chip) / 2, chip, chip, fill=ACCENT, line=None,
             shape_type=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.18)
        tb = textbox(slide, x + 0.11, sy + (rh - chip) / 2 + 0.045, chip, 0.2)
        p = add_para(tb.text_frame, first=True, align=PP_ALIGN.CENTER)
        write(p, str(i + 1), 8.5, WHITE, bold=True, font=MONO)
        tb = textbox(slide, x + 0.52, sy + 0.04, w - 0.66, rh - 0.08, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.15)
        write(p, st["t"], st.get("size", 10.5), INK, bold=True)
        if st.get("s"):
            p2 = add_para(tb.text_frame, line=1.15)
            write(p2, st["s"], st.get("ssize", 8.8), MUTED)
    if cap:
        tb = textbox(slide, x, y + h - 0.30, w, 0.30)
        p = add_para(tb.text_frame, first=True)
        write(p, cap, 8.6, MUTED, italic=True)


def v_tree(slide, spec, x, y, w, h):
    root = spec["root"]
    kids = spec["children"]
    n = len(kids)
    root_w = min(w * 0.5, 3.3)
    root_h = 0.52
    rx = x + (w - root_w) / 2
    box = rect(slide, rx, y, root_w, root_h, fill=INK, line=None,
               shape_type=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.14)
    shape_text(box, [(root, dict(size=10.5, bold=True, color=WHITE))])
    kid_gap = 0.14
    kw = (w - kid_gap * (n - 1)) / n
    kh = min(h - root_h - 0.55, 1.15)
    ky = y + root_h + 0.50
    bus_y = y + root_h + 0.24
    hline(slide, rx + root_w / 2, y + root_h, 0, RULE)
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(rx + root_w / 2), Inches(y + root_h),
                                   Inches(rx + root_w / 2), Inches(bus_y))
    c.line.color.rgb = RULE
    c.line.width = Pt(1)
    left = x + kw / 2
    right = x + w - kw / 2
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(left), Inches(bus_y),
                                   Inches(right), Inches(bus_y))
    c.line.color.rgb = RULE
    c.line.width = Pt(1)
    for i, kd in enumerate(kids):
        kx = x + i * (kw + kid_gap)
        if isinstance(kd, str):
            kd = {"t": kd}
        c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(kx + kw / 2), Inches(bus_y),
                                       Inches(kx + kw / 2), Inches(ky))
        c.line.color.rgb = RULE
        c.line.width = Pt(1)
        box = rect(slide, kx, ky, kw, kh, fill=WHITE, line=RULE, lw=0.9,
                   shape_type=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.10)
        lines = [(kd["t"], dict(size=kd.get("size", 10), bold=True, color=INK, line=1.15))]
        if kd.get("s"):
            lines.append((kd["s"], dict(size=kd.get("ssize", 8.4), color=MUTED, line=1.16)))
        shape_text(box, lines)


def text_metrics(items, w, h, sizes=None, gap=4):
    sizes = sizes or [12, 11.5, 11, 10.5, 10, 9.5, 9]
    size = choose_size(items, w, h, sizes, space_after=gap)
    total = sum(est_lines(t, w, size) * size * 1.22 / 72.0 + gap / 72.0 for t in items)
    return size, total


def v_compare(slide, spec, x, y, w, h):
    """Two or three labelled panels; height adapts to content and centres vertically."""
    panels = spec["panels"]
    n = len(panels)
    gap = 0.22
    pw = (w - gap * (n - 1)) / n
    # --- measure
    heights = []
    metas = []
    for pn in panels:
        head = 0.50 + (0.26 if pn.get("tag") else 0) + 0.20
        if pn.get("mono"):
            sz, need = code_metrics(pn["lines"], pw - 0.28, h - head - 0.2)
            metas.append(("code", sz, need))
            heights.append(head + need)
        else:
            sz, need = text_metrics(pn["lines"], pw - 0.34, h - head, gap=4)
            metas.append(("text", sz, need))
            heights.append(head + need)
    ph = min(h, max(heights))
    py = y + (h - ph) / 2
    for i, pn in enumerate(panels):
        px = x + i * (pw + gap)
        kind = pn.get("kind")
        good = kind == "good"
        neutral = kind == "neutral"
        rect(slide, px, py, pw, ph,
             fill=PANEL if neutral else (GOODBG if good else BADBG),
             line=RULE if neutral else (ACCENT if good else RULE),
             lw=0.9 if neutral else (1.1 if good else 0.9))
        # marker + label
        rect(slide, px + 0.16, py + 0.20, 0.11, 0.11,
             fill=ACCENT if good else (INK if neutral else MUTED), shape_type=MSO_SHAPE.RECTANGLE)
        tb = textbox(slide, px + 0.36, py + 0.13, pw - 0.52, 0.28)
        p = add_para(tb.text_frame, first=True)
        write(p, pn["label"], 10.5, INK, bold=True)
        yy = py + 0.50
        if pn.get("tag"):
            tb = textbox(slide, px + 0.18, yy, pw - 0.34, 0.22)
            p = add_para(tb.text_frame, first=True)
            write(p, pn["tag"], 8.4, MUTED, bold=True)
            yy += 0.26
        kind, sz, need = metas[i]
        if kind == "code":
            v_code(slide, {"lines": pn["lines"], "label": pn.get("code_label"),
                           "bg": PANEL if neutral else (GOODBG if good else BADBG)},
                   px + 0.12, yy + 0.02, pw - 0.24, ph - (yy - py) - 0.14)
        else:
            tb = textbox(slide, px + 0.18, yy + 0.02, pw - 0.34, ph - (yy - py) - 0.12)
            for j, ln in enumerate(pn["lines"]):
                p = add_para(tb.text_frame, first=(j == 0), space_after=4, line=1.24)
                if isinstance(ln, tuple):
                    write(p, [(ln[0], dict(bold=True, color=INK)), (ln[1], dict(color=BODY))], sz)
                else:
                    write(p, ln, sz, BODY if not good else INK)


def v_cards(slide, spec, x, y, w, h):
    cards = spec["cards"]
    cols = spec.get("cols", len(cards))
    gap = spec.get("gap", 0.18)
    cw = (w - gap * (cols - 1)) / cols
    rows = (len(cards) + cols - 1) // cols
    ch = (h - gap * (rows - 1)) / rows
    cap_h = spec.get("max_h")
    if cap_h:
        ch = min(ch, cap_h)
    oy = y + (h - (rows * ch + gap * (rows - 1))) / 2
    for i, cd in enumerate(cards):
        r, c = divmod(i, cols)
        cx, cy = x + c * (cw + gap), oy + r * (ch + gap)
        rect(slide, cx, cy, cw, ch, fill=WHITE, line=RULE, lw=0.9)
        rect(slide, cx, cy, 0.045, ch, fill=ACCENT)
        tb = textbox(slide, cx + 0.20, cy + 0.12, cw - 0.34, ch - 0.22, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.15, space_after=4)
        write(p, cd.get("k", ""), 8.6, ACCENT, bold=True)
        p = add_para(tb.text_frame, line=1.14, space_after=4)
        write(p, cd["t"], cd.get("size", 12.2), INK, bold=True)
        if cd.get("s"):
            p = add_para(tb.text_frame, line=1.22)
            write(p, cd["s"], cd.get("ssize", 9.4), BODY)


def v_stack(slide, spec, x, y, w, h):
    """Layered bars: each layer has a short label chip + description."""
    layers = spec["layers"]
    n = len(layers)
    gap = spec.get("gap", 0.09)
    rh = (h - gap * (n - 1)) / n
    for i, ly in enumerate(layers):
        sy = y + i * (rh + gap)
        rect(slide, x, sy, w, rh, fill=PANEL, line=RULE, lw=0.75)
        lw_chip = spec.get("chip", 1.55)
        rect(slide, x, sy, lw_chip, rh, fill=ACCENT if ly.get("accent", True) else INK, line=None)
        tb = textbox(slide, x + 0.10, sy + 0.04, lw_chip - 0.18, rh - 0.08, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.1)
        write(p, ly["k"], ly.get("ksize", 9.6), WHITE, bold=True, font=ly.get("font", FONT))
        tb = textbox(slide, x + lw_chip + 0.16, sy + 0.04, w - lw_chip - 0.28, rh - 0.08,
                     anchor=MSO_ANCHOR.MIDDLE)
        for j, d in enumerate(ly["v"] if isinstance(ly["v"], list) else [ly["v"]]):
            p = add_para(tb.text_frame, first=(j == 0), line=1.16)
            write(p, d, ly.get("vsize", 10.2), BODY)


def v_nested(slide, spec, x, y, w, h):
    """Concentric labelled rectangles (AI > ML > DL > GenAI)."""
    layers = spec["layers"]        # outermost first
    n = len(layers)
    pad_x = spec.get("pad_x", 0.38)
    pad_y = spec.get("pad_y", 0.42)
    fills = [PANEL, WHITE, PANEL, WHITE]
    for i, lb in enumerate(layers):
        ix, iy = x + i * pad_x, y + i * pad_y
        iw, ih = w - 2 * i * pad_x, h - 2 * i * pad_y
        rect(slide, ix, iy, iw, ih, fill=fills[i % 2], line=RULE, lw=0.9)
        tb = textbox(slide, ix + 0.14, iy + 0.07, iw - 0.26, 0.34)
        p = add_para(tb.text_frame, first=True, line=1.16)
        write(p, [(lb["t"], dict(size=lb.get("size", 10.2), bold=True, color=INK))], 10.2)
        if lb.get("s"):
            write(p, [("  " + lb["s"], dict(size=9.0, color=MUTED))], 9.0)


def v_kv(slide, spec, x, y, w, h):
    rows = spec["rows"]
    n = len(rows)
    gap = spec.get("gap", 0.10)
    rh = (h - gap * (n - 1)) / n
    lab_w = spec.get("label_w", w * 0.30)
    for i, (k, v) in enumerate(rows):
        ry = y + i * (rh + gap)
        rect(slide, x, ry, w, rh, fill=WHITE, line=RULE, lw=0.75)
        tb = textbox(slide, x + 0.12, ry, lab_w - 0.2, rh, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.12)
        write(p, k, spec.get("ksize", 9.8), ACCENT_D, bold=True)
        tb = textbox(slide, x + lab_w + 0.05, ry, w - lab_w - 0.20, rh, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.14)
        write(p, v, spec.get("vsize", 10.2), BODY)


def v_image(slide, spec, x, y, w, h):
    cap = spec.get("caption")
    cap_h = 0.34 if cap else 0
    ih = h - cap_h
    pic = slide.shapes.add_picture(spec["path"], Inches(x), Inches(y), Inches(w), Inches(ih))
    # preserve aspect ratio: centre inside the box
    ar = pic.width / pic.height
    box_ar = w / ih
    if ar > box_ar:
        pic.height = Emu(int(Inches(w) / ar))
        pic.top = Inches(y + (ih - pic.height / 914400) / 2)
    else:
        pic.width = Emu(int(Inches(ih) * ar))
        pic.left = Inches(x + (w - pic.width / 914400) / 2)
    if cap:
        tb = textbox(slide, x, y + h - 0.32, w, 0.32)
        p = add_para(tb.text_frame, first=True, line=1.15)
        write(p, cap, 8.6, MUTED, italic=True)


def v_grid(slide, spec, x, y, w, h):
    """Dense numbered grid of small cells (used for the 14-technique summary)."""
    cells = spec["cells"]
    cols = spec.get("cols", 5)
    gap = spec.get("gap", 0.14)
    rows = (len(cells) + cols - 1) // cols
    cw = (w - gap * (cols - 1)) / cols
    ch = min((h - gap * (rows - 1)) / rows, spec.get("max_h", 1.06))
    total = rows * ch + gap * (rows - 1)
    y0 = y + max(0.0, (h - total) / 2.0)
    for i, cd in enumerate(cells):
        r, c = divmod(i, cols)
        in_row = min(cols, len(cells) - r * cols)
        off = (cols - in_row) * (cw + gap) / 2.0
        cx, cy = x + off + c * (cw + gap), y0 + r * (ch + gap)
        rect(slide, cx, cy, cw, ch, fill=WHITE, line=RULE, lw=0.8)
        rect(slide, cx, cy, cw, 0.045, fill=ACCENT)
        tb = textbox(slide, cx + 0.13, cy + 0.13, cw - 0.24, ch - 0.20, anchor=MSO_ANCHOR.MIDDLE)
        p = add_para(tb.text_frame, first=True, line=1.1, space_after=3)
        write(p, cd.get("n", ""), 8.6, ACCENT, bold=True, font=MONO)
        p = add_para(tb.text_frame, line=1.14, space_after=3)
        write(p, cd["t"], cd.get("size", 10.6), INK, bold=True)
        if cd.get("s"):
            p = add_para(tb.text_frame, line=1.18)
            write(p, cd["s"], cd.get("ssize", 8.6), MUTED)


def v_callout(slide, spec, x, y, w, h):
    rect(slide, x, y, w, h, fill=PANEL, line=RULE, lw=0.75)
    rect(slide, x, y, 0.05, h, fill=ACCENT)
    tb = textbox(slide, x + 0.24, y + 0.14, w - 0.42, h - 0.24)
    if spec.get("k"):
        p = add_para(tb.text_frame, first=True, line=1.15, space_after=4)
        write(p, spec["k"], 9, ACCENT, bold=True)
        first = False
    else:
        first = True
    for ln in spec["lines"]:
        if isinstance(ln, tuple):
            p = add_para(tb.text_frame, first=first, line=1.26, space_after=5)
            write(p, [(ln[0], dict(bold=True, color=INK)), (ln[1], dict(color=BODY))], spec.get("size", 11))
        else:
            p = add_para(tb.text_frame, first=first, line=1.26, space_after=5)
            write(p, ln, spec.get("size", 11), BODY)
        first = False


# ---------------------------------------------------------------- slide kinds
def slide_concept(prs, s, num):
    sl = blank(prs)
    header(sl, s.get("kicker"), s["title"])
    summary(sl, s["summary"])
    lw = s.get("left_w", 5.85)
    bullets(sl, s["bullets"], M, Y_BODY, lw, Y_BOT - Y_BODY, size=s.get("size"), gap=s.get("gap", 10))
    vx = M + lw + 0.42
    vw = CW - lw - 0.42
    if s.get("visual"):
        render(sl, s["visual"], vx, Y_BODY, vw, Y_BOT - Y_BODY)
    if s.get("outcome"):
        outcome_strip(sl, s["outcome"])
    footer(sl, num)
    _notes(sl, s)
    return sl


def slide_wide(prs, s, num):
    sl = blank(prs)
    header(sl, s.get("kicker"), s["title"])
    summary(sl, s["summary"])
    y = Y_BODY
    if s.get("bullets"):
        bh = s.get("bullets_h", 1.05)
        bullets(sl, s["bullets"], M, y, CW, bh, size=s.get("size", 13), gap=4)
        y += bh + 0.16
    if s.get("visual"):
        render(sl, s["visual"], M, y, CW, (Y_BOT - (0.58 if s.get("outcome") else 0)) - y)
    if s.get("outcome"):
        outcome_strip(sl, s["outcome"])
    footer(sl, num)
    _notes(sl, s)
    return sl


def slide_split(prs, s, num):
    """Left bullets / right visual with custom widths."""
    sl = blank(prs)
    header(sl, s.get("kicker"), s["title"])
    summary(sl, s["summary"], size=s.get("summary_size", 14.5))
    lw = s.get("left_w", 4.9)
    vw = CW - lw - 0.38
    if s.get("bullets"):
        bullets(sl, s["bullets"], M, Y_BODY, lw, Y_BOT - Y_BODY, size=s.get("size"), gap=s.get("gap", 8))
    if s.get("visual"):
        render(sl, s["visual"], M + lw + 0.38, Y_BODY, vw, Y_BOT - Y_BODY)
    if s.get("outcome"):
        outcome_strip(sl, s["outcome"])
    footer(sl, num)
    _notes(sl, s)
    return sl


def slide_stack_visual(prs, s, num):
    """Visual across the top, supporting text below (2 columns)."""
    sl = blank(prs)
    header(sl, s.get("kicker"), s["title"])
    summary(sl, s["summary"])
    vh = s.get("visual_h", 2.5)
    render(sl, s["visual"], M, Y_BODY, CW, vh)
    y = Y_BODY + vh + 0.28
    if s.get("bullets"):
        bullets(sl, s["bullets"], M, y, CW, Y_BOT - y, size=s.get("size", 12.5), gap=4)
    if s.get("outcome"):
        outcome_strip(sl, s["outcome"])
    footer(sl, num)
    _notes(sl, s)
    return sl


def _vis_h(spec, w, h):
    if spec and spec.get("type") == "code":
        sz, need = code_metrics(spec["lines"], w, h)
        return min(h, need + (0.30 if spec.get("label") else 0))
    return h


def slide_demo(prs, s, num):
    sl = blank(prs)
    header(sl, s.get("kicker"), s["title"])
    summary(sl, s["summary"], size=13.5)
    lw = s.get("left_w", 5.0)
    vw = CW - lw - 0.4
    body_h = Y_BOT - Y_BODY
    h1 = _vis_h(s["left"], lw, body_h)
    h2 = _vis_h(s.get("right"), vw, body_h) if s.get("right") else 0
    top = Y_BODY + max(0.0, (body_h - max(h1, h2)) / 2.0)
    render(sl, s["left"], M, top, lw, body_h)
    if s.get("right"):
        render(sl, s["right"], M + lw + 0.4, top, vw, body_h)
    if s.get("outcome"):
        outcome_strip(sl, s["outcome"])
    footer(sl, num)
    _notes(sl, s)
    return sl


def slide_outcome(prs, s, num):
    sl = blank(prs)
    header(sl, s.get("kicker"), s["title"])
    summary(sl, s["summary"], size=15)
    items = s["items"]
    half = (len(items) + 1) // 2
    body_h = Y_BOT - Y_BODY - 0.15
    col_w = CW / 2 - 0.28
    flat = ["\u2022  " + (it if isinstance(it, str) else it[0] + "  " + it[1]) for it in items]
    col1 = flat[:half]
    tw = col_w - 0.26
    sizes = [19, 18, 17, 16, 15, 14.5, 14, 13.5, 13]
    size = sizes[-1]
    for cand in sizes:
        budget = body_h - (half - 1) * 30.0 / 72.0
        if max(sum(est_lines(t, tw, cand) * cand * 1.24 / 72.0 + 8 / 72.0 for t in col)
               for col in (flat[:half], flat[half:])) <= budget:
            size = cand
            break
    total = max(sum(est_lines(t, tw, size) * size * 1.24 / 72.0 + 8 / 72.0 for t in col)
                for col in (flat[:half], flat[half:]))
    gap = max(6, min(30, (body_h - total) * 72.0 / max(1, half - 1)))
    for col, chunk in enumerate([items[:half], items[half:]]):
        x = M + col * (CW / 2 + 0.32)
        tb = textbox(sl, x, Y_BODY, col_w, body_h, anchor=MSO_ANCHOR.MIDDLE)
        for i, it in enumerate(chunk):
            p = add_para(tb.text_frame, first=(i == 0), space_after=gap, line=1.24)
            hang(p, 0.24, -0.24)
            write(p, [("\u2022  ", dict(size=size, bold=True, color=ACCENT))], size)
            if isinstance(it, tuple):
                write(p, [(it[0], dict(size=size, bold=True, color=INK)),
                          ("  " + it[1], dict(size=size, color=BODY))], size)
            else:
                write(p, it, size, BODY)
    if s.get("outcome"):
        outcome_strip(sl, s["outcome"])
    footer(sl, num)
    _notes(sl, s)
    return sl


def slide_cover(prs, s, num):
    sl = blank(prs)
    rect(sl, 0, 0, 0.28, SH, fill=ACCENT)
    tb = textbox(sl, 1.05, 1.30, 7.6, 0.3)
    p = add_para(tb.text_frame, first=True)
    write(p, s["kicker"], 11.5, ACCENT, bold=True)
    tb = textbox(sl, 1.05, 1.66, 8.2, 2.0)
    p = add_para(tb.text_frame, first=True, line=1.0, space_after=6)
    write(p, s["title"], 46, INK, bold=True)
    p = add_para(tb.text_frame, line=1.1)
    write(p, s["subtitle"], 27, ACCENT_D, bold=True)
    hline(sl, 1.05, 3.36, 3.2, ACCENT, 2.4)
    tb = textbox(sl, 1.05, 3.62, 7.3, 1.2)
    for i, ln in enumerate(s["lines"]):
        p = add_para(tb.text_frame, first=(i == 0), line=1.28, space_after=4)
        write(p, ln, 13.5, BODY)
    tb = textbox(sl, 1.05, 6.18, 8.0, 0.6)
    p = add_para(tb.text_frame, first=True, line=1.2)
    write(p, s["meta"], 10.5, MUTED, bold=True)
    if s.get("image"):
        sl.shapes.add_picture(s["image"], Inches(8.60), Inches(1.42), Inches(3.9), Inches(3.9))
    _notes(sl, s)
    return sl


def slide_statement(prs, s, num):
    sl = blank(prs)
    rect(sl, 0, 0, SW, 0.10, fill=ACCENT)
    tb = textbox(sl, M + 0.6, 2.25, CW - 1.2, 0.3)
    p = add_para(tb.text_frame, first=True)
    write(p, s.get("kicker", ""), 11, ACCENT, bold=True)
    tb = textbox(sl, M + 0.6, 2.62, CW - 1.4, 2.6)
    for i, (txt, kw) in enumerate(s["paras"]):
        p = add_para(tb.text_frame, first=(i == 0), line=1.32, space_after=kw.get("space_after", 10))
        write(p, txt, kw.get("size", 22), kw.get("color", INK), bold=kw.get("bold", False))
    if s.get("who"):
        tb = textbox(sl, M + 0.6, 5.9, CW - 1.2, 0.5)
        p = add_para(tb.text_frame, first=True)
        write(p, s["who"], 12, MUTED, bold=True)
    footer(sl, num)
    _notes(sl, s)
    return sl


def _notes(slide, s):
    txt = s.get("notes")
    if txt:
        slide.notes_slide.notes_text_frame.text = txt


KINDS = {
    "concept": slide_concept, "wide": slide_wide, "split": slide_split,
    "stackvis": slide_stack_visual, "demo": slide_demo, "outcome": slide_outcome,
    "cover": slide_cover, "statement": slide_statement,
}


GOOGLE_LINE_BASE = 1.20   # Google Slides: 100% line spacing = 1.20 x font size
LEAD_SCALE = 1.28         # split the difference between Google (1.20) and PPT (1.36)


def tune_leading(prs, floor=0.94):
    """Rescale paragraph line spacing so every renderer lands near the design.

    The deck's layout maths assume line spacing of `ratio x size`. PowerPoint
    measures a percentage against the font's own line height (1.36x for Noto
    Sans Tamil) and Google Slides against 1.20x, so the same percentage draws
    ~36% looser in PowerPoint than the layout intends - which is why text
    could spill into the outcome band after the pptx was imported. Dividing
    every percentage by 1.28 puts Google ~6% under the design and PowerPoint
    ~6% over, so nothing overflows in either.
    """
    for slide in prs.slides:
        for sh in slide.shapes:
            tfs = []
            if sh.has_text_frame:
                tfs.append(sh.text_frame)
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    for cell in row.cells:
                        tfs.append(cell.text_frame)
            for tf in tfs:
                for para in tf.paragraphs:
                    pPr = para._pPr
                    if pPr is None:
                        continue
                    ln = pPr.find(qn("a:lnSpc"))
                    if ln is None:
                        continue
                    pct = ln.find(qn("a:spcPct"))
                    if pct is None:
                        continue
                    try:
                        ratio = int(pct.get("val")) / 100000.0
                    except (TypeError, ValueError):
                        continue
                    scaled = max(ratio / LEAD_SCALE, floor)
                    pct.set("val", str(int(round(scaled * 100000))))


def build(slides, path):
    prs = new_deck()
    for i, s in enumerate(slides, start=1):
        KINDS[s["kind"]](prs, s, i)
    tune_leading(prs)
    prs.save(path)
    print("saved", path, "slides:", len(prs.slides))
    return prs
