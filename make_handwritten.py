#!/usr/bin/env python3
"""
Rebuild ``OOAD_Assignment_2_Vignesh_M.pdf`` so that it reads as a genuinely
hand-written document.

Nothing in the output is typeset with a system font.  Every glyph comes from a
real handwriting typeface (Caveat / Kalam, both SIL Open Font License) and the
page is composed the way a person writes on ruled sheets:

  * baselines sit exactly on the ruled lines,
  * every line gets a tiny random tilt, baseline drift and word wobble,
  * bullet dots and the deployment diagram are drawn as freehand vector strokes.

Usage
-----
    python make_handwritten.py                      # Caveat on ruled paper
    python make_handwritten.py --font kalam
    python make_handwritten.py --plain              # same fonts, blank paper
    python make_handwritten.py --out output/foo.pdf
"""

from __future__ import annotations

import argparse
import math
import os
import random
import zlib

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from scanify import scan_pdf

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "assets", "fonts")

# --------------------------------------------------------------------------
# page geometry (points, 1 pt = 1/72 inch)
# --------------------------------------------------------------------------
W, H = A4

PAPER = HexColor("#FEFDF7")      # warm off-white sheet
INK = HexColor("#1C2C50")        # blue-black ballpoint
INK_SOFT = HexColor("#2B3D66")
RULE = HexColor("#C7D5E6")       # pale blue ruling
MARGIN_LINE = HexColor("#E0A6A6")  # red margin rule
GHOST = HexColor("#93A0B4")

LEFT = 98.0
RIGHT = 546.0
TOP = 788.0
BOTTOM = 60.0
LEAD_BASE = 22.0
TEXT_W = RIGHT - LEFT

# every typeface has a different x-height, so all sizes are expressed relative
# to the Caveat baseline and multiplied by this factor
SCALE = 1.0


def S(size: float) -> float:
    """Apply the active typeface scale to a point size."""
    return size * SCALE

# ink density varies a little from stroke to stroke, like a real pen
INKS = (INK, INK, INK_SOFT, HexColor("#22335C"))


# --------------------------------------------------------------------------
# fonts
# --------------------------------------------------------------------------
def register_fonts(family: str) -> tuple[str, str, str]:
    """Register the handwriting family and return (regular, semibold, bold)."""
    if family == "kalam":
        spec = {
            "Hand-Regular": "Kalam-Regular.ttf",
            "Hand-SemiBold": "Kalam-Regular.ttf",
            "Hand-Bold": "Kalam-Bold.ttf",
        }
    elif family == "indie":
        # Indie Flower is a single-weight face
        spec = {
            "Hand-Regular": "IndieFlower-Regular.ttf",
            "Hand-SemiBold": "IndieFlower-Regular.ttf",
            "Hand-Bold": "IndieFlower-Regular.ttf",
        }
    else:
        spec = {
            "Hand-Regular": "Caveat-Regular.ttf",
            "Hand-SemiBold": "Caveat-SemiBold.ttf",
            "Hand-Bold": "Caveat-Bold.ttf",
        }
    for name, filename in spec.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, filename)))
    return "Hand-Regular", "Hand-SemiBold", "Hand-Bold"


BODY = BOLD = SEMI = None  # filled in by main()


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
def sw(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def tokenize(runs):
    """runs = [(text, font, size)] -> flat list of word atoms."""
    atoms = []
    for text, font, size in runs:
        for chunk in text.replace("\n", " ").split(" "):
            if chunk == "":
                continue
            atoms.append({"w": chunk, "f": font, "s": size})
    return atoms


def wrap(atoms, max_w):
    """Greedy line breaker that understands mixed font runs."""
    if not atoms:
        return []
    lines, cur, cur_w = [], [], 0.0
    for a in atoms:
        word_w = sw(a["w"], a["f"], a["s"])
        space_w = sw(" ", a["f"], a["s"])
        extra = word_w + (space_w if cur else 0.0)
        if cur and cur_w + word_w > max_w:
            lines.append(cur)
            cur, cur_w = [a], word_w
        else:
            cur.append(a)
            cur_w += extra
    if cur:
        lines.append(cur)
    return lines


def line_width(atoms) -> float:
    total = 0.0
    for i, a in enumerate(atoms):
        total += sw(a["w"], a["f"], a["s"])
        if i < len(atoms) - 1:
            total += sw(" ", a["f"], a["s"])
    return total


# --------------------------------------------------------------------------
# freehand vector primitives
# --------------------------------------------------------------------------
def sketch_poly(c, pts, rng, wob=0.9, segs=6, close=True):
    """Draw a closed polygon with hand tremor along every edge."""
    path = c.beginPath()
    first = True
    n = len(pts)
    edges = n if close else n - 1
    for i in range(edges):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy) or 1.0
        px, py = -dy / length, dx / length
        for k in range(segs):
            t = k / segs
            off = rng.uniform(-wob, wob) * (0.35 if k == 0 else 1.0)
            X = x1 + dx * t + px * off
            Y = y1 + dy * t + py * off
            if first:
                path.moveTo(X, Y)
                first = False
            else:
                path.lineTo(X, Y)
    if close:
        path.close()
    c.drawPath(path, stroke=1, fill=0)


def sketch_line(c, x1, y1, x2, y2, rng, wob=0.9, segs=7):
    path = c.beginPath()
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy) or 1.0
    px, py = -dy / length, dx / length
    for k in range(segs + 1):
        t = k / segs
        off = rng.uniform(-wob, wob)
        X, Y = x1 + dx * t + px * off, y1 + dy * t + py * off
        if k == 0:
            path.moveTo(X, Y)
        else:
            path.lineTo(X, Y)
    c.drawPath(path, stroke=1, fill=0)


def sketch_dot(c, x, y, rng, r=2.1):
    """A hand-pressed bullet: a slightly lumpy filled blob."""
    path = c.beginPath()
    steps = 9
    for k in range(steps + 1):
        ang = 2 * math.pi * k / steps
        rr = r * rng.uniform(0.82, 1.18)
        X, Y = x + rr * math.cos(ang) * 1.05, y + rr * math.sin(ang) * 0.92
        if k == 0:
            path.moveTo(X, Y)
        else:
            path.lineTo(X, Y)
    path.close()
    c.drawPath(path, stroke=0, fill=1)


def sketch_arrow(c, x1, y1, x2, y2, rng):
    """Vertical connector with a freehand arrowhead at the lower end."""
    sketch_line(c, x1, y1, x2, y2 + 7, rng, wob=0.7)
    head = 7.0
    for side in (-1, 1):
        sketch_line(
            c,
            x2 + side * head * 0.62,
            y2 + head * 1.15,
            x2,
            y2,
            rng,
            wob=0.45,
            segs=3,
        )


# --------------------------------------------------------------------------
# the writer
# --------------------------------------------------------------------------
class HandWriter:
    def __init__(self, path, body, bold, semi, ruled=True, seed=11):
        self.path = path
        self.body, self.bold, self.semi = body, bold, semi
        self.ruled = ruled
        self.rng = random.Random(seed)
        self.lead = LEAD_BASE * SCALE
        self.maxrow = int((TOP - BOTTOM) / self.lead)
        self.c = canvas.Canvas(
            path,
            pagesize=A4,
            initialFontName=body,          # never fall back to a system font
            initialFontSize=S(12),
        )
        self.c.setTitle("OOAD Assignment 2 - Vignesh M")
        self.c.setAuthor("Vignesh M")
        self.c.setSubject("Object Oriented Analysis and Design - Assignment 2")
        self.page = 0
        self.row = 0
        self.line_no = 0
        self.cover_page = True

    # -- paper ------------------------------------------------------------
    def _paint_sheet(self):
        c = self.c
        c.setFillColor(PAPER)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        if not self.ruled:
            return
        c.setStrokeColor(RULE)
        c.setLineWidth(0.55)
        for k in range(self.maxrow + 1):
            y = TOP - k * self.lead
            c.line(LEFT - 26, y, RIGHT + 14, y)
        # red margin rule
        c.setStrokeColor(MARGIN_LINE)
        c.setLineWidth(1.0)
        c.line(LEFT - 18, BOTTOM - 14, LEFT - 18, TOP + 20)

    def new_page(self, plain=False):
        if self.page:
            self._footer()
            self.c.showPage()
        self.page += 1
        self.cover_page = plain
        if plain:
            self.c.setFillColor(PAPER)
            self.c.rect(0, 0, W, H, stroke=0, fill=1)
        else:
            self._paint_sheet()
        self.row = 0

    def _footer(self):
        if self.cover_page:
            return
        c = self.c
        c.saveState()
        c.setFillColor(GHOST)
        c.setFont(self.body, S(10))
        c.drawCentredString(W / 2.0, 30, str(self.page))
        c.restoreState()

    # -- row bookkeeping --------------------------------------------------
    def _need(self, rows=1):
        if self.row + rows - 1 > self.maxrow:
            self.new_page()

    def reserve(self, rows):
        """Start a new page unless ``rows`` more ruled lines fit here."""
        self._need(rows)

    def _y(self):
        return TOP - self.row * self.lead

    def _advance(self, rows=1):
        self.row += rows

    # -- text -------------------------------------------------------------
    def _draw_line(self, atoms, x, y, align="left", rng=None, ink=None, cx=None):
        rng = rng or self.rng
        c = self.c
        total = line_width(atoms)
        if align == "center":
            x = (cx if cx is not None else (LEFT + RIGHT) / 2.0) - total / 2.0
        elif align == "right":
            x = RIGHT - total

        angle = rng.uniform(-0.22, 0.22)
        drift_x = rng.uniform(-0.7, 0.7)
        drift_y = rng.uniform(-0.9, 0.9)
        color = ink or rng.choice(INKS)

        # merge consecutive words that share a face, so the line stays one text
        # object and the PDF remains selectable / searchable
        groups = []
        for a in atoms:
            if groups and groups[-1][0] == a["f"] and groups[-1][2] == a["s"]:
                groups[-1][1].append(a["w"])
            else:
                groups.append([a["f"], [a["w"]], a["s"]])

        c.saveState()
        c.translate(x + drift_x, y + drift_y)
        c.rotate(angle)
        c.setFillColor(color)
        pen = 0.0
        for font, words, size in groups:
            text = " ".join(words)
            word_space = rng.uniform(-0.45, 0.45)
            t = c.beginText(pen + rng.uniform(-0.3, 0.3), rng.uniform(-0.4, 0.4))
            t.setFont(font, size)
            t.setWordSpace(word_space)
            t.textOut(text)
            c.drawText(t)
            pen += sw(text, font, size) + word_space * (len(words) - 1) + sw(" ", font, size)
        c.restoreState()

    def para(self, runs, first_indent=20.0, left_indent=0.0, align="left",
             before=0, bullet=False, keep_rows=1, after_keep=0):
        """Flow a paragraph; returns the baseline y of its first line.

        ``after_keep`` is the number of rows that must still be available below
        the block, so a heading is never stranded at the foot of a page.
        """
        max_w = TEXT_W - left_indent - (first_indent if not bullet else 0.0)
        atoms = tokenize(runs)
        lines = wrap(atoms, max_w)

        if after_keep:
            self._need(before + len(lines) + after_keep)
        else:
            self._need(before + keep_rows)
        self._advance(before)

        first_y = None
        for i, line in enumerate(lines):
            if self.row > self.maxrow:
                self.new_page()
            y = self._y()
            if first_y is None:
                first_y = y
            indent = left_indent + (first_indent if i == 0 else 0.0)
            if bullet and i == 0:
                self.c.setFillColor(self.rng.choice(INKS))
                sketch_dot(self.c, LEFT + left_indent - S(13.0), y + S(5.0), self.rng, r=S(2.1))
                indent = left_indent
            elif bullet:
                indent = left_indent
            self._draw_line(line, LEFT + indent, y, align=align)
            self.line_no += 1
            self._advance(1)
        return first_y

    # -- semantic blocks --------------------------------------------------
    def question(self, text):
        self.para([(text, self.bold, S(16))], first_indent=0, before=2,
                  after_keep=6)

    def section(self, text):
        self.para([(text, self.bold, S(16))], first_indent=0, before=1,
                  after_keep=4)

    def sub(self, text):
        self.para([(text, self.semi, S(16))], first_indent=0, before=1,
                  after_keep=4)

    def body_para(self, text):
        self.para([(text, self.body, S(14))], first_indent=S(22))

    def bullets(self, items):
        for lead, rest in items:
            runs = [(lead, self.bold, S(14))]
            if rest:
                runs.append((rest, self.body, S(14)))
            self.para(runs, left_indent=S(26), bullet=True)

    # -- diagram ----------------------------------------------------------
    def diagram(self, nodes, links):
        box_h, gap = S(50.0), S(32.0)
        total = len(nodes) * box_h + (len(nodes) - 1) * gap
        rows = int(math.ceil((total + 8) / self.lead))
        self._need(rows)

        c = self.c
        rng = random.Random(4242)
        cx = (LEFT + RIGHT) / 2.0
        top = min(self._y() + 14, TOP)

        c.saveState()
        c.setStrokeColor(INK)
        c.setLineWidth(1.15)
        c.setLineJoin(1)
        c.setLineCap(1)

        for idx, (title, inner) in enumerate(nodes):
            by = top - idx * (box_h + gap) - box_h
            bx = cx - S(106.0)
            bw = S(212.0)

            # outer node
            sketch_poly(c, [(bx, by), (bx + bw, by), (bx + bw, by + box_h), (bx, by + box_h)],
                        rng, wob=1.0)
            c.setFillColor(INK)
            c.setFont(self.bold, S(13))
            c.drawCentredString(cx, by + box_h - S(17.0), title)

            # nested artifact box
            iw, ih = S(150.0), S(19.0)
            ix, iy = cx - iw / 2.0, by + S(5.0)
            sketch_poly(c, [(ix, iy), (ix + iw, iy), (ix + iw, iy + ih), (ix, iy + ih)],
                        rng, wob=0.8)
            c.setFillColor(INK_SOFT)
            c.setFont(self.body, S(12))
            c.drawCentredString(cx, iy + S(6.0), inner)

            # connector to the next node
            if idx < len(links):
                label = links[idx]
                y_from = by
                y_to = by - gap
                sketch_arrow(c, cx, y_from, cx, y_to, rng)
                c.setFillColor(INK_SOFT)
                c.setFont(self.body, S(11))
                c.drawString(cx + S(11.0), y_from - gap / 2.0 - S(5.0), label)

        c.restoreState()
        self._advance(rows)

    # -- cover ------------------------------------------------------------
    def cover(self, lines):
        """Plain title page - no border, no ruling, just centred writing."""
        self.new_page(plain=True)
        limit = W - 2 * 72.0
        for text, size, bold, y in lines:
            font = self.bold if bold else self.body
            size = S(size)
            while size > 9 and sw(text, font, size) > limit:
                size -= 0.5
            self._draw_line(tokenize([(text, font, size)]), LEFT, y,
                            align="center", cx=W / 2.0,
                            rng=random.Random(zlib.crc32(text.encode())))

    def save(self):
        self._footer()
        self.c.showPage()
        self.c.save()


# --------------------------------------------------------------------------
# document content (verbatim from the original PDF)
# --------------------------------------------------------------------------
Q1 = "1. Explain the Different Behavioral Diagrams Used in UML"
Q2 = "2. Describe Deployment Diagram with Neat Diagram"
Q3 = "3. What is a Use Case Diagram and How Does It Represent Actors?"
Q4 = "4. Dynamic Architectural Modelling"
Q5 = "5. Static Architectural Modelling"


def build(path, plain=False, family="indie"):
    global BODY, BOLD, SEMI, SCALE
    # the requested 16 pt / 14 pt sizes are absolute, so every family uses them as-is
    SCALE = 1.0
    BODY, SEMI, BOLD = register_fonts(family)
    w = HandWriter(path, BODY, BOLD, SEMI, ruled=not plain)

    w.cover([
        ("ASSIGNMENT \u2013 2", 24, True, 660),
        ("OBJECT ORIENTED ANALYSIS AND DESIGN (OOAD)", 16, True, 596),
        ("Name: VIGNESH M", 14, False, 430),
        ("Register Number: DC2431006010004", 14, False, 396),
        ("Subject: OBJECT ORIENTED ANALYSIS AND DESIGN (OOAD)", 14, False, 362),
        ("Assignment: 2", 14, False, 328),
        ("Professor: Dr.A Shareen", 14, False, 294),
        ("SRM INSTITUTE OF SCIENCE AND TECHNOLOGY", 16, True, 150),
        ("Kattankulathur \u2013 603 203", 14, False, 118),
    ])

    w.new_page()

    # ---------------- question 1 ----------------
    w.question(Q1)
    w.section("Introduction")
    w.body_para(
        "Unified Modeling Language (UML) is a standard visual language used to design, "
        "describe and document software systems. UML diagrams are mainly classified into "
        "structural diagrams and behavioral diagrams. Behavioral diagrams explain how a "
        "system works, how objects interact and how activities change over time."
    )
    w.section("Types of Behavioral Diagrams")

    for head, para, example in [
        ("1. Use Case Diagram",
         "A Use Case Diagram represents the interaction between users (actors) and the "
         "functions provided by a system. It helps identify the requirements of a system "
         "from the user's point of view.",
         "In an online shopping system, a customer can log in, search products, add items "
         "to the cart and place an order."),
        ("2. Activity Diagram",
         "An Activity Diagram represents the workflow of activities in a system. It shows "
         "the sequence of actions, decisions and parallel activities involved in completing "
         "a process.",
         "An online payment process includes selecting a product, entering payment details, "
         "verifying payment and displaying the result."),
        ("3. State Machine Diagram",
         "A State Machine Diagram describes the different states of an object and the "
         "transitions between those states based on events.",
         "An order may move through the states New, Confirmed, Shipped, Delivered or "
         "Cancelled."),
        ("4. Sequence Diagram",
         "A Sequence Diagram shows how objects communicate with each other through messages "
         "in a particular time sequence. It is useful for understanding the order of "
         "interactions in a system.",
         "In a login process, the user sends login details to the application, the "
         "application checks the database and returns the login result."),
        ("5. Communication Diagram",
         "A Communication Diagram represents interactions between objects by focusing on "
         "their relationships and the messages exchanged. Numbered messages indicate the "
         "order of communication.",
         None),
        ("6. Interaction Overview Diagram",
         "An Interaction Overview Diagram provides a high-level view of the flow between "
         "different interactions. It combines activity-flow concepts with references to "
         "interaction diagrams.",
         None),
        ("7. Timing Diagram",
         "A Timing Diagram shows changes in the state or value of objects over a specific "
         "period. It is mainly used in real-time and embedded systems where timing is "
         "important.",
         None),
    ]:
        w.sub(head)
        w.body_para(para)
        if example:
            w.body_para("Example: " + example)

    w.body_para(
        "Behavioral diagrams help developers understand the dynamic behavior of a software "
        "system. They explain user interactions, workflows, object communication and state "
        "changes, making software design easier to understand and maintain."
    )

    # ---------------- question 2 ----------------
    w.question(Q2)
    w.section("Introduction")
    w.body_para(
        "A Deployment Diagram is a UML structural diagram that represents the physical "
        "arrangement of hardware devices, software components and their communication "
        "connections in a system. It explains where software applications are installed and "
        "how different devices communicate with each other."
    )
    w.section("Main Elements of a Deployment Diagram")
    w.bullets([
        ("Node:", " Represents a physical or virtual computing resource, such as a server, "
                  "computer or mobile device."),
        ("Device:", " A hardware resource that executes software, such as a desktop computer "
                    "or server."),
        ("Execution Environment:", " A software environment in which applications run, such "
                                   "as a web server or application server."),
        ("Artifact:", " Represents a deployable software file, such as an application "
                      "package, executable or database script."),
        ("Communication Path:", " Represents the network connection between nodes."),
    ])

    w.section("Example: Online Shopping System Deployment Diagram")
    w.body_para(
        "The following diagram shows a simple deployment structure for an online shopping "
        "application. The customer accesses the application through a browser. The web "
        "server communicates with the application server, which accesses the database server."
    )
    w.diagram(
        [
            ("Customer Device", "Web Browser"),
            ("Web Server", "Web Application"),
            ("Application Server", "Business Logic"),
            ("Database Server", "Customer / Order DB"),
        ],
        ["HTTPS / Internet", "Internal Network", "SQL Connection"],
    )

    w.section("Working of the Diagram")
    w.bullets([
        ("", "The customer uses a web browser to access the shopping application."),
        ("", "The web server receives the request through the internet using HTTPS."),
        ("", "The application server processes business operations such as login, product "
             "search and order placement."),
        ("", "The application server communicates with the database server to store or "
             "retrieve information."),
        ("", "The result is sent back to the customer through the web server."),
    ])

    w.section("Advantages of Deployment Diagrams")
    w.bullets([
        ("", "Shows the physical architecture of a software system."),
        ("", "Helps understand hardware and software requirements."),
        ("", "Makes network communication and server relationships clear."),
        ("", "Supports installation, configuration and maintenance planning."),
        ("", "Helps identify deployment dependencies."),
    ])
    w.body_para(
        "Deployment Diagrams are useful for understanding how software is distributed across "
        "hardware and software environments. They help developers and system administrators "
        "plan infrastructure, installation and communication between system components."
    )

    # ---------------- question 3 ----------------
    w.question(Q3)
    w.section("Introduction")
    w.body_para(
        "A Use Case Diagram is a UML behavioral diagram that describes the functional "
        "requirements of a system. It shows how external users or systems interact with the "
        "services provided by the application. It gives a simple overview of what a system "
        "does from the user's point of view."
    )
    w.section("Main Components of a Use Case Diagram")

    for head, para in [
        ("1. Actor",
         "An actor represents a person, organization or external system that interacts with "
         "the application. Actors are shown using a stick-figure symbol and are placed "
         "outside the system boundary."),
        ("2. Use Case",
         "A use case represents a specific function or service provided by the system. It is "
         "generally represented using an oval shape. Examples include Login, Register, "
         "Search Product and Make Payment."),
        ("3. System Boundary",
         "The system boundary is represented by a rectangle. It defines the scope of the "
         "application and contains all the use cases provided by the system."),
        ("4. Relationship",
         "Relationships show how actors and use cases are connected. Common relationships "
         "include association, include, extend and generalization."),
    ]:
        w.sub(head)
        w.body_para(para)

    w.section("How Actors Are Represented")
    w.bullets([
        ("", "Actors are represented by stick figures outside the system boundary."),
        ("", "A line connects an actor to the use case with which it interacts."),
        ("", "A primary actor initiates an activity to achieve a goal."),
        ("", "A secondary actor supports the system by providing an external service."),
        ("", "An external software system can also be represented as an actor."),
    ])

    w.section("Example")
    w.body_para(
        "In an online shopping application, the Customer is an actor who can register, log "
        "in, search products, add products to the cart and make payments. The Payment "
        "Gateway is another actor that supports payment processing."
    )

    w.section("Advantages")
    w.bullets([
        ("", "Clearly identifies system users and their requirements."),
        ("", "Helps understand the scope and functions of an application."),
        ("", "Improves communication between developers and clients."),
        ("", "Supports requirement analysis and system design."),
    ])
    w.body_para(
        "A Use Case Diagram is an important UML tool for representing system functionality "
        "and user interaction. Actors identify who or what interacts with the system, while "
        "use cases describe the services provided."
    )

    # ---------------- question 4 ----------------
    w.question(Q4)
    w.section("Introduction")
    w.body_para(
        "Dynamic Architectural Modelling describes how the components of a software system "
        "interact and behave during execution. It focuses on the runtime activities of a "
        "system, including communication, message exchange, process flow and changes in "
        "system states."
    )
    w.section("Main Concepts")
    w.bullets([
        ("Component Interaction:", " Explains how different software components communicate "
                                   "with one another during execution."),
        ("Message Flow:", " Describes the exchange of information between objects, services "
                          "or components."),
        ("Control Flow:", " Represents the order in which operations and activities are "
                          "performed."),
        ("State Changes:", " Shows how an object or component changes its state when an "
                           "event occurs."),
        ("Concurrency:", " Explains how multiple tasks or processes execute at the same "
                         "time."),
    ])

    w.section("UML Diagrams Used in Dynamic Modelling")
    w.bullets([
        ("Sequence Diagram:", " Shows messages exchanged between objects in time order."),
        ("Activity Diagram:", " Represents workflows and the flow of control."),
        ("State Machine Diagram:", " Shows object states and transitions."),
        ("Communication Diagram:", " Shows object relationships and message exchanges."),
    ])

    w.section("Example")
    w.body_para(
        "In an online banking application, a customer requests a fund transfer. The "
        "application verifies the user's login, checks the account balance, processes the "
        "transaction and updates the account records. These activities and interactions "
        "represent the dynamic behavior of the system."
    )

    w.section("Importance of Dynamic Architectural Modelling")
    w.bullets([
        ("", "Helps understand system behavior during execution."),
        ("", "Identifies communication between software components."),
        ("", "Helps detect design and workflow problems."),
        ("", "Supports performance and concurrency analysis."),
        ("", "Makes complex system interactions easier to understand."),
    ])
    w.body_para(
        "Dynamic Architectural Modelling explains how a software system behaves while "
        "running. It is useful for designing interactive applications, understanding "
        "component communication and ensuring that system operations work in the correct "
        "sequence."
    )

    # ---------------- question 5 ----------------
    w.question(Q5)
    w.section("Introduction")
    w.body_para(
        "Static Architectural Modelling describes the structure and organization of a "
        "software system without focusing on its runtime behavior. It explains the major "
        "components, classes, modules, relationships and dependencies that form the system."
    )
    w.section("Main Concepts")
    w.bullets([
        ("Components:", " Represents the major functional parts of a software application."),
        ("Classes and Objects:", " Describe the data, attributes and operations used in the "
                                 "system."),
        ("Relationships:", " Explain how different classes or components are connected."),
        ("Dependencies:", " Show when one component depends on another component."),
        ("Interfaces:", " Define how components expose services and communicate with other "
                        "parts of the system."),
    ])

    w.section("UML Diagrams Used in Static Modelling")
    w.bullets([
        ("Class Diagram:", " Represents classes, attributes, methods and relationships."),
        ("Object Diagram:", " Shows instances of classes and their relationships at a "
                            "particular moment."),
        ("Component Diagram:", " Shows the organization and dependencies of software "
                               "components."),
        ("Package Diagram:", " Groups related classes and components into packages."),
        ("Deployment Diagram:", " Shows the physical arrangement of software artifacts and "
                                "deployment nodes."),
    ])

    w.section("Example")
    w.body_para(
        "In a library management system, static modelling identifies classes such as "
        "Student, Book, Librarian and IssueRecord. It defines their attributes and "
        "relationships. For example, a Student can borrow books, and an IssueRecord stores "
        "the details of each borrowing transaction."
    )

    w.section("Importance of Static Architectural Modelling")
    w.bullets([
        ("", "Provides a clear view of system structure."),
        ("", "Helps organize software into manageable components."),
        ("", "Identifies relationships and dependencies."),
        ("", "Supports software maintenance and future development."),
        ("", "Improves communication among developers and designers."),
    ])

    w.save()
    return w.page


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--font", choices=["indie", "caveat", "kalam"], default="indie")
    ap.add_argument("--plain", action="store_true", help="no ruled paper")
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-scan", action="store_true",
                    help="keep the clean vector output instead of the phone-scan look")
    ap.add_argument("--dpi", type=int, default=160, help="raster resolution of the scan")
    ap.add_argument("--quality", type=int, default=82, help="JPEG quality of the scan")
    ap.add_argument("--scan-strength", type=float, default=1.0,
                    help="0 = clean, 1 = normal phone scan, >1 = heavier")
    args = ap.parse_args()

    out = args.out or os.path.join(
        HERE, "output",
        "OOAD_Assignment_2_Vignesh_M_handwritten%s%s.pdf"
        % ("" if args.font == "indie" else "_" + args.font, "_plain" if args.plain else ""),
    )
    os.makedirs(os.path.dirname(out), exist_ok=True)

    if args.no_scan:
        pages = build(out, plain=args.plain, family=args.font)
        print(f"wrote {out}  ({pages} pages, vector)")
        return

    # build the clean vector master, then photograph it
    vector = out[:-4] + ".vector.pdf"
    pages = build(vector, plain=args.plain, family=args.font)
    scan_pdf(vector, out, dpi=args.dpi, quality=args.quality,
             strength=args.scan_strength)
    os.remove(vector)
    print(f"wrote {out}  ({pages} pages, scanned at {args.dpi} dpi)")


if __name__ == "__main__":
    main()
