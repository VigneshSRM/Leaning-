#!/usr/bin/env python3
"""Make a clean vector PDF look like a page photographed by a phone.

The vector pages are rasterised and then put through the optical chain a phone
camera actually imposes on a sheet of paper:

* warm, slightly grey paper instead of pure white
* uneven lighting — a few low-frequency lobes plus a directional falloff
* lens vignette darkening the corners
* low-frequency mottling (paper fibre, uneven absorption)
* fine sensor grain
* a warm colour cast, then a touch of optical softness

The result is written as a JPEG-per-page PDF, which is what a scanner app
produces anyway.
"""

from __future__ import annotations

import io
import math
import random

import numpy as np
import pypdfium2 as pdfium
from PIL import Image, ImageFilter
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

PAPER = np.array([0.970, 0.963, 0.944], dtype=np.float32)   # warm off-white
CAST = np.array([1.006, 1.000, 0.984], dtype=np.float32)    # warm sensor cast


def _norm(a: np.ndarray) -> np.ndarray:
    lo, hi = float(a.min()), float(a.max())
    return (a - lo) / (hi - lo) if hi > lo else np.zeros_like(a)


def scanify(img: Image.Image, rng: np.random.Generator, strength: float = 1.0) -> Image.Image:
    """Apply the phone-camera optical chain to one rendered page."""
    src = np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0
    h, w, _ = src.shape

    yy, xx = np.mgrid[0:h, 0:w]
    nx = (xx / max(w - 1, 1)).astype(np.float32)
    ny = (yy / max(h - 1, 1)).astype(np.float32)

    # ---- uneven lighting -------------------------------------------------
    light = np.ones((h, w), dtype=np.float32)
    for _ in range(3):
        ang = float(rng.uniform(0.0, 2.0 * math.pi))
        freq = float(rng.uniform(0.8, 2.0))
        phase = float(rng.uniform(0.0, 2.0 * math.pi))
        amp = float(rng.uniform(0.012, 0.030)) * strength
        u = nx * math.cos(ang) + ny * math.sin(ang)
        light += amp * np.sin(u * freq * 2.0 * math.pi + phase)

    light *= (
        1.0
        + float(rng.uniform(-0.050, 0.050)) * strength * (nx - 0.5)
        + float(rng.uniform(-0.040, 0.040)) * strength * (ny - 0.5)
    )

    # ---- lens vignette ---------------------------------------------------
    r2 = (nx - 0.5) ** 2 + (ny - 0.5) ** 2
    light *= 1.0 - 0.22 * strength * (r2 / 0.5) ** 1.15

    # ---- paper mottling --------------------------------------------------
    small = rng.normal(0.0, 1.0, (max(h // 24, 2), max(w // 24, 2))).astype(np.float32)
    mottle = np.asarray(
        Image.fromarray((_norm(small) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC),
        dtype=np.float32,
    ) / 255.0
    light *= 1.0 + (mottle - 0.5) * 0.030 * strength

    # ---- composite: paper colour multiplied by the ink layer --------------
    out = src * (PAPER * light[..., None])

    # ---- sensor grain ----------------------------------------------------
    out += rng.normal(0.0, 0.011 * strength, (h, w, 1)).astype(np.float32)

    # ---- colour cast -----------------------------------------------------
    out *= CAST

    im = Image.fromarray(np.clip(out * 255.0, 0, 255).astype(np.uint8))
    im = im.filter(ImageFilter.GaussianBlur(radius=0.55 * strength))
    return im


def scan_pdf(src: str, dst: str, dpi: int = 170, quality: int = 84,
             seed: int = 7, strength: float = 1.0) -> int:
    """Rasterise ``src`` and write a phone-scanned looking copy to ``dst``."""
    doc = pdfium.PdfDocument(src)
    c = canvas.Canvas(dst, pagesize=A4)
    c.setTitle("OOAD Assignment 2 - Vignesh M")
    c.setAuthor("Vignesh M")
    c.setSubject("Object Oriented Analysis and Design - Assignment 2")

    for i in range(len(doc)):
        page = doc[i]
        pil = page.render(scale=dpi / 72.0).to_pil().convert("RGB")
        pil = scanify(pil, np.random.default_rng(seed * 1009 + i), strength=strength)

        buf = io.BytesIO()
        pil.save(buf, format="JPEG", quality=quality, optimize=True, subsampling=0)
        buf.seek(0)

        c.drawImage(ImageReader(buf), 0, 0, width=A4[0], height=A4[1])
        c.showPage()

    c.save()
    return len(doc)
