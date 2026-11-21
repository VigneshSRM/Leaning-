# -*- coding: utf-8 -*-
"""Build the deck and report likely text overflow (no renderer available here)."""
import sys
from pptx import Presentation
from pptx.util import Emu

from .deck_lib import build, est_lines
from . import content_a

mods = []
for name in ("content_b", "content_c", "content_d", "content_e"):
    try:
        mods.append(__import__("deck." + name, fromlist=["slides"]))
    except ModuleNotFoundError:
        pass


def all_slides():
    slides = []
    slides += content_a.build_front()
    slides += content_a.build_m1()
    slides += content_a.build_m2()
    for mod in mods:
        slides += mod.slides()
    return slides


def check(path):
    prs = Presentation(path)
    problems = 0
    for i, slide in enumerate(prs.slides, start=1):
        for sh in slide.shapes:
            if not sh.has_text_frame:
                continue
            tf = sh.text_frame
            if not tf.text.strip():
                continue
            w_in = sh.width / 914400.0
            h_in = sh.height / 914400.0
            total = 0.0
            for p in tf.paragraphs:
                txt = "".join(r.text for r in p.runs)
                if not txt:
                    total += 0.1
                    continue
                size = max([(r.font.size.pt if r.font.size else 12) for r in p.runs] or [12])
                marL = 0.0
                try:
                    if p._pPr is not None and p._pPr.get("marL"):
                        marL = int(p._pPr.get("marL")) / 914400.0
                except Exception:
                    marL = 0.0
                if isinstance(p.line_spacing, float):
                    line = 1.20 * p.line_spacing
                elif p.line_spacing is not None:
                    line = p.line_spacing.pt / float(size or 12)
                else:
                    line = 1.2
                sb = p.space_after.pt if p.space_after is not None else 0
                mono = any(r.font.name == "Roboto Mono" for r in p.runs)
                total += est_lines(txt, w_in - marL, size, 0.62 if mono else 0.55) * size * line / 72.0 + sb / 72.0
            if total > h_in * 1.06 + 0.02:
                problems += 1
                print("slide %3d  needs %.2f\" has %.2f\"  | %s" %
                      (i, total, h_in, tf.text[:60].replace("\n", " / ")))
    print("---- overflow candidates:", problems)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "out.pptx"
    build(all_slides(), out)
    check(out)
