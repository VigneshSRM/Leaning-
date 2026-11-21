# -*- coding: utf-8 -*-
"""English edition of the deck.

Same slide specs as the Tamil build; every string is swapped through
``deck/en_map.json`` (Tamil string -> English string).  Nothing else changes,
so the layout, code samples and visuals stay identical.

    python3 -m deck.deck_en out.pptx
"""
import json
import os
import re
import sys

from pptx import Presentation

from . import build as deckbuild
from .deck_lib import build as build_pptx
from .i18n import set_lang

TAMIL = re.compile(r"[\u0B80-\u0BFF]")
MAP_PATH = os.path.join(os.path.dirname(__file__), "en_map.json")

with open(MAP_PATH, encoding="utf-8") as fh:
    EN_MAP = json.load(fh)


# Strings that are already ASCII in the Tamil deck but are edition-specific
# (they talk about Tamil itself, so the translation map never sees them).
OVERRIDES = {
    "Tamil explanations  |  English technical terms  |  ChatGPT · Gemini · Copilot":
        "Clear explanations  |  Real examples  |  ChatGPT · Gemini · Copilot",
    "Tamil + English: ": "Technical terms: ",
    "\"Use simple Tamil; keep technical terms in English.\"":
        "\"Use simple English; keep technical terms exact.\"",
    "Max 100 words, simple Tamil.": "Max 100 words, simple English.",
    "CONSTRAINTS: simple Tamil, technical": "CONSTRAINTS: simple English, technical",
    "   English + Tamil?": "   one language or both?",
    "#  1 leads  2 English + Tamil": "#  1 leads  2 English only",
}


class MissingTranslation(KeyError):
    pass


def translate(value):
    """Deep-copy a slide spec, swapping every Tamil string for its English line."""
    if isinstance(value, str):
        if value in OVERRIDES:
            return OVERRIDES[value]
        if not TAMIL.search(value):
            return value
        try:
            return EN_MAP[value]
        except KeyError:
            raise MissingTranslation(value)
    if isinstance(value, dict):
        return {translate(k): translate(v) for k, v in value.items()}
    if isinstance(value, list):
        return [translate(v) for v in value]
    if isinstance(value, tuple):
        return tuple(translate(v) for v in value)
    return value


def _count_tamil(value):
    if isinstance(value, str):
        return len(TAMIL.findall(value))
    if isinstance(value, (list, tuple)):
        return sum(_count_tamil(v) for v in value)
    if isinstance(value, dict):
        return sum(_count_tamil(k) + _count_tamil(v) for k, v in value.items())
    return 0


def en_slides():
    set_lang("en")
    return [translate(spec) for spec in deckbuild.all_slides()]


def audit(path):
    """Count Tamil code points left in the built file (body, tables, notes)."""
    prs = Presentation(path)
    hits = 0
    for idx, slide in enumerate(prs.slides, start=1):
        texts = []
        for sh in slide.shapes:
            if sh.has_text_frame:
                texts.append(sh.text_frame.text)
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    for cell in row.cells:
                        texts.append(cell.text_frame.text)
        if slide.has_notes_slide:
            texts.append(slide.notes_slide.notes_text_frame.text)
        for txt in texts:
            n = len(TAMIL.findall(txt))
            if n:
                hits += n
                print("slide %3d  tamil chars %d | %s" % (idx, n, txt[:70].replace("\n", " / ")))
    print("---- residual Tamil code points:", hits)
    return hits


def main(argv):
    out = argv[1] if len(argv) > 1 else "Prompt-Engineering-English.pptx"
    slides = en_slides()
    print("english slides:", len(slides))
    print("spec residual:", sum(_count_tamil(s) for s in slides))
    build_pptx(slides, out)
    deckbuild.check(out)
    audit(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
