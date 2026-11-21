# -*- coding: utf-8 -*-
"""Tiny language switch for labels that live in the layout code (not in content dicts)."""

LANG = "ta"


def set_lang(code):
    global LANG
    if code not in ("ta", "en"):
        raise ValueError(code)
    LANG = code
    return LANG


def t(ta, en):
    return en if LANG == "en" else ta
