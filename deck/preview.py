# -*- coding: utf-8 -*-
"""Rough PIL renderer for QA: draws shapes/text from the pptx so layout can be eyeballed.

Not pixel-perfect (no Tamil shaping guarantee, approximate bold), but reliable enough
to catch overflow, collisions and bad spacing.
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.enum.text import MSO_ANCHOR

S = 150.0                      # px per inch
FONT_PATH = "/home/user/fonts/NotoSansTamil.ttf"
MONO_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
EMU = 914400.0

_cache = {}


def font(path, px, bold=False):
    key = (path, int(px))
    if key not in _cache:
        try:
            _cache[key] = ImageFont.truetype(path, int(px))
        except Exception:
            _cache[key] = ImageFont.load_default()
    return _cache[key]


def measure(draw, txt, f):
    if not txt:
        return 0
    return draw.textlength(txt.replace("\n", " "), font=f)


def rgb(color, default=None):
    from pptx.dml.color import RGBColor
    if isinstance(color, RGBColor):
        return tuple(color)
    try:
        if color is None or color.type is None:
            return default
        return tuple(color.rgb)
    except Exception:
        return default


def render(pptx_path, outdir, only=None, size_scale=1.0):
    prs = Presentation(pptx_path)
    os.makedirs(outdir, exist_ok=True)
    order = []
    for idx, slide in enumerate(prs.slides, start=1):
        if only and idx not in only:
            continue
        W = int(prs.slide_width / EMU * S * size_scale)
        H = int(prs.slide_height / EMU * S * size_scale)
        img = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(img)
        for sh in slide.shapes:
            _shape(d, img, sh, size_scale)
        path = os.path.join(outdir, "slide-%03d.png" % idx)
        img.save(path)
        order.append(path)
    print("rendered", len(order), "->", outdir)


def _xy(sh, s):
    return (sh.left / EMU * S * s, sh.top / EMU * S * s,
            sh.width / EMU * S * s, sh.height / EMU * S * s)


def _shape(d, img, sh, s):
    x, y, w, h = _xy(sh, s)
    kind = sh.shape_type
    if sh.shape_type is not None and str(sh.shape_type).startswith("LINE") or sh.__class__.__name__ == "Connector":
        try:
            col = rgb(sh.line.color, (120, 120, 120)) or (120, 120, 120)
            d.line([(x, y), (x + w, y + h)], fill=col, width=max(1, int(0.9 * s)))
            # crude arrowhead at the end
            try:
                if sh._element.spPr.find('{http://schemas.openxmlformats.org/drawingml/2006/main}ln') is not None:
                    from pptx.oxml.ns import qn
                    ln = sh._element.spPr.find(qn('a:ln'))
                    if ln is not None and ln.find(qn('a:tailEnd')) is not None:
                        import math
                        ang = math.atan2(y + h - y, x + w - x)
                        L = 5 * s
                        for sg in (0.5, -0.5):
                            d.line([(x + w, y + h),
                                    (x + w - L * math.cos(ang + sg), y + h - L * math.sin(ang + sg))],
                                   fill=col, width=max(1, int(0.9 * s)))
            except Exception:
                pass
        except Exception:
            pass
        return

    # picture
    if sh.__class__.__name__ == "Picture":
        try:
            im = Image.open(sh.image.blob and __import__("io").BytesIO(sh.image.blob))
            im = im.convert("RGB").resize((int(w), int(h)))
            img.paste(im, (int(x), int(y)))
        except Exception:
            d.rectangle([x, y, x + w, y + h], outline=(200, 200, 200))
        return

    # table
    if sh.has_table:
        tbl = sh.table
        cx = x
        for c in tbl.columns:
            cx += c.width / EMU * S * s
        cy = y
        rows_h = [r.height / EMU * S * s for r in tbl.rows]
        for r_i, rh in enumerate(rows_h):
            cx = x
            for c_i, col in enumerate(tbl.columns):
                cw = col.width / EMU * S * s
                cell = tbl.cell(r_i, c_i)
                fill = rgb(cell.fill.fore_color, (255, 255, 255))
                d.rectangle([cx, cy, cx + cw, cy + rh], fill=fill, outline=(225, 230, 236))
                txt = cell.text_frame.text
                if txt.strip():
                    f = font(FONT_PATH, 9.2 * S / 72 * s)
                    d.text((cx + 6, cy + 4), txt.split("\n")[0][:60], font=f,
                           fill=(255, 255, 255) if r_i == 0 else (30, 30, 40))
                cx += cw
            cy += rh
        return

    # autoshape / textbox: fill + outline
    try:
        fill = rgb(sh.fill.fore_color, None) if sh.fill.type is not None else None
    except Exception:
        fill = None
    try:
        line = rgb(sh.line.color, None)
    except Exception:
        line = None
    if fill is not None or line is not None:
        r = 4 * s
        if str(sh.shape_type) == "ROUNDED_RECTANGLE":
            d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=line,
                                width=1 if line else 0)
        else:
            if fill is not None:
                d.rectangle([x, y, x + w, y + h], fill=fill)
            if line is not None:
                d.rectangle([x, y, x + w, y + h], outline=line, width=1)

    if not sh.has_text_frame or not sh.text_frame.text.strip():
        return
    _text(d, sh, x, y, w, h, s)


def _text(d, sh, x, y, w, h, s):
    tf = sh.text_frame
    ml = tf.margin_left / EMU * S * s if tf.margin_left is not None else 0
    mr = tf.margin_right / EMU * S * s if tf.margin_right is not None else 0
    mt = tf.margin_top / EMU * S * s if tf.margin_top is not None else 0
    tw = w - ml - mr
    lines = []      # (text, font, color, xoff)
    total_h = 0.0
    for p in tf.paragraphs:
        runs = [(r.text, r.font) for r in p.runs]
        if not runs:
            total_h += 6
            continue
        sz = max([(f.size.pt if f.size else 12) for _, f in runs] or [12])
        if isinstance(p.line_spacing, float):
            ls = 1.20 * p.line_spacing
        elif p.line_spacing is not None:
            ls = p.line_spacing.pt / float(sz or 12)
        else:
            ls = 1.2
        lh = sz * ls * S / 72 * s
        # word-level wrap
        marL = 0
        ind = 0
        try:
            if p._pPr is not None and p._pPr.get("marL"):
                marL = int(p._pPr.get("marL")) / EMU * S * s
            if p._pPr is not None and p._pPr.get("indent"):
                ind = int(p._pPr.get("indent")) / EMU * S * s
        except Exception:
            marL, ind = 0, 0
        first_line = True
        words = []
        for txt, f in runs:
            name = f.name or ""
            path = MONO_PATH if "Mono" in name or "Courier" in name else FONT_PATH
            for wtxt in txt.split(" "):
                words.append((wtxt, font(path, (f.size.pt if f.size else 12) * S / 72 * s),
                              rgb(getattr(f.color, "rgb", None), (34, 34, 45)) or (34, 34, 45),
                              bool(f.bold)))
        cur, curw = [], 0.0
        align = p.alignment
        for wtxt, fnt, col, bd in words:
            wpx = measure(d, wtxt + " ", fnt)
            lime = tw - marL - (ind if first_line else 0)
            if curw + wpx > lime and cur:
                lines.append((cur, lh, align, marL + (ind if first_line else 0)))
                total_h += lh
                first_line = False
                cur, curw = [(wtxt, fnt, col, bd)], wpx
            else:
                cur.append((wtxt, fnt, col, bd))
                curw += wpx
        if cur:
            lines.append((cur, lh, align, marL + (ind if first_line else 0)))
            total_h += lh
        total_h += (p.space_after.pt * S / 72 * s) if p.space_after is not None else 0

    if tf.vertical_anchor == MSO_ANCHOR.MIDDLE:
        cy = y + mt + max(0, (h - mt - total_h) / 2)
    elif tf.vertical_anchor == MSO_ANCHOR.BOTTOM:
        cy = y + h - total_h - mt
    else:
        cy = y + mt
    for cur, lh, align, lmar in lines:
        lw = sum(measure(d, t + " ", fn) for t, fn, _, _ in cur)
        cx = x + ml + lmar
        if str(align) in ("CENTER (2)", "CENTER"):
            cx = x + ml + lmar + max(0, (tw - lmar - lw) / 2)
        for wtxt, fnt, col, bd in cur:
            d.text((cx, cy), wtxt.replace("\n", " "), font=fnt, fill=col,
                   stroke_width=(1 if bd else 0), stroke_fill=col)
            cx += measure(d, wtxt + " ", fnt)
        cy += lh
    if cy > y + h + 2 * s:
        d.line([(x, y + h), (x + w, y + h)], fill=(255, 0, 0), width=2)


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2],
           only=[int(v) for v in sys.argv[3].split(",")] if len(sys.argv) > 3 else None)
