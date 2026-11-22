#!/usr/bin/env python3
"""Give the three Caveat static instances unique font names.

Google Fonts ships Caveat only as a variable font.  Instantiating it with
fontTools leaves every instance reporting the *same* PostScript name
(``Caveat-Regular``), so a PDF producer that keys embedded subsets by that
name collapses bold and regular into one face.  This script rewrites the
name table of each instance so they stay distinguishable.

Run once after (re)generating assets/fonts/Caveat-*.ttf:

    python tools/fix_caveat_names.py
"""

import os

from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(HERE, "assets", "fonts")

INSTANCES = {
    "Caveat-Regular.ttf": ("Caveat", "Regular", "Caveat-Regular", "Caveat"),
    "Caveat-SemiBold.ttf": ("Caveat", "SemiBold", "Caveat-SemiBold", "Caveat SemiBold"),
    "Caveat-Bold.ttf": ("Caveat", "Bold", "Caveat-Bold", "Caveat Bold"),
}

# nameIDs that carry family / style / PostScript information
TARGETS = {1: 0, 2: 1, 4: 3, 6: 2, 16: 0, 17: 1}


def main() -> None:
    for filename, values in INSTANCES.items():
        path = os.path.join(FONT_DIR, filename)
        if not os.path.exists(path):
            print("skip (missing):", filename)
            continue
        font = TTFont(path)
        name = font["name"]
        for name_id, pick in TARGETS.items():
            value = values[pick]
            name.setName(value, name_id, 3, 1, 0x409)   # Windows / Unicode
            name.setName(value, name_id, 1, 0, 0)       # Mac / Roman
        font.save(path)
        print(f"{filename}: {values[2]}")


if __name__ == "__main__":
    main()
