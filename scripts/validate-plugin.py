#!/usr/bin/env python3
"""Validate the Infeara ChatGPT/Codex plugin package.

Checks the Agent Plugins identity fields, every public listing limit, the icon
files, the onboarding skill path, and each bundled skill's frontmatter.
Exits non-zero on any failure.
"""
from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent / "plugins" / "infeara"
ALLOWED_CATEGORIES = {
    "Productivity", "Developer Tools", "Creativity", "Communication",
    "Education", "Finance", "Health", "Lifestyle", "News", "Travel",
    "Food", "Shopping", "Entertainment", "Other",
}
EXPECTED_SKILLS = 24
errors: list[str] = []
warnings: list[str] = []
checks = 0


def ok(condition: bool, message: str) -> bool:
    global checks
    checks += 1
    if not condition:
        errors.append(message)
    return condition


def png_size(path: Path) -> tuple[int, int] | None:
    """Read PNG dimensions from the IHDR chunk without external libraries."""
    try:
        data = path.read_bytes()[:33]
    except OSError:
        return None
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def svg_size(path: Path) -> tuple[float, float] | None:
    head = path.read_text(errors="replace")[:2000]
    vb = re.search(r'viewBox="([\d.\s-]+)"', head)
    if vb:
        parts = [float(p) for p in vb.group(1).split()]
        if len(parts) == 4:
            return parts[2], parts[3]
    w = re.search(r'\bwidth="([\d.]+)', head)
    h = re.search(r'\bheight="([\d.]+)', head)
    if w and h:
        return float(w.group(1)), float(h.group(1))
    return None


def check_image(label: str, rel: str) -> None:
    if not ok(isinstance(rel, str) and rel.startswith("./"), f"{label}: path must start with './' (got {rel!r})"):
        return
    path = PLUGIN / rel[2:]
    if not ok(path.is_file(), f"{label}: file missing: {rel}"):
        return
    if not ok(path.stat().st_size <= 5 * 1024 * 1024, f"{label}: larger than 5 MiB"):
        return
    suffix = path.suffix.lower()
    if not ok(suffix in {".png", ".jpg", ".jpeg", ".webp", ".svg"}, f"{label}: unsupported format {suffix}"):
        return
    dims = svg_size(path) if suffix == ".svg" else png_size(path)
    if not ok(dims is not None, f"{label}: could not read dimensions (corrupt file?)"):
        return
    w, h = dims
    ok(w == h, f"{label}: must be square (got {w}×{h})")
    ok(w >= 48 and h >= 48, f"{label}: must be at least 48×48 (got {w}×{h})")
    ok(w <= 4096 and h <= 4096, f"{label}: raster max is 4096 px (got {w}×{h})")
    if label == "logo":
        ok(w >= 512, f"{label}: primary listing icon should be at least 512 px (got {w})")
    print(f"  {label:14s} {rel:32s} {w}×{h}  {path.stat().st_size / 1024:.0f} KiB")


def main() -> int:
    manifest_path = PLUGIN / "chatgpt-plugin.json"
    if not manifest_path.is_file():
        print(f"FAIL: missing {manifest_path}")
        return 1
    raw = manifest_path.read_text()
    try:
        manifest = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"FAIL: plugin.json is not valid JSON: {exc}")
        return 1
    print(f"Validating {manifest_path.relative_to(PLUGIN.parent.parent)}\n")

    # --- identity -----------------------------------------------------------
    ok(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
       "plugin.json: $schema must be the Agent Plugins 1.0.0 schema")
    name = manifest.get("name", "")
    ok(bool(name), "plugin.json: name is required")
    ok(len(name) <= 64, "plugin.json: name must be <= 64 characters")
    ok(bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name)), "plugin.json: name must be lowercase kebab-case")
    ok(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", ""))), "plugin.json: version must be semver")
    ok(0 < len(manifest.get("description", "")) <= 4000, "plugin.json: description required, <= 4000 chars")
    author = manifest.get("author") or {}
    ok(bool(author.get("name")), "plugin.json: author.name is required")
    for key, limit in (("name", 120), ("email", 320), ("url", 2048)):
        if key in author:
            ok(len(author[key]) <= limit, f"plugin.json: author.{key} exceeds {limit} chars")

    ext = (manifest.get("extensions") or {}).get("com.openai") or {}
    if not ok(bool(ext), "plugin.json: extensions.com.openai is required for the ChatGPT listing"):
        return report()

    # --- listing metadata ---------------------------------------------------
    listing = ext.get("interface") or {}
    if not ok(bool(listing), "extensions.com.openai.interface is required"):
        return report()
    limits = {
        "displayName": 30, "shortDescription": 30, "longDescription": 4000,
        "developerName": 80, "websiteURL": 1024, "supportURL": 1024,
        "privacyPolicyURL": 1024, "termsOfServiceURL": 1024,
    }
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        ok(bool(listing.get(field)), f"interface.{field} is required")
    for field, limit in limits.items():
        if field in listing:
            ok(len(listing[field]) <= limit, f"interface.{field} exceeds {limit} characters")
    ok(listing.get("shortDescription", "") != "", "interface.shortDescription is the subtitle and cannot be blank")
    ok(listing.get("category") in ALLOWED_CATEGORIES,
       f"interface.category must be a directory category (got {listing.get('category')!r})")

    caps = listing.get("capabilities")
    if caps is not None:
        ok(isinstance(caps, list), "interface.capabilities must be an array")
        ok(len(caps) <= 20, "interface.capabilities allows at most 20 entries")
        ok(all(len(c) <= 120 for c in caps), "interface.capabilities entries max 120 chars")
    prompts = listing.get("defaultPrompt")
    if prompts is not None:
        prompts = [prompts] if isinstance(prompts, str) else prompts
        ok(len(prompts) <= 3, "interface.defaultPrompt allows at most 3 prompts")
        ok(all(len(p) <= 128 for p in prompts), "interface.defaultPrompt entries max 128 chars")
        ok(all("@" not in p for p in prompts), "interface.defaultPrompt must not contain @mentions")
    for field in ("brandColor", "brandColorDark"):
        if field in listing:
            ok(bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", listing[field])),
               f"interface.{field} must be #RRGGBB (got {listing[field]!r})")
    for field, limit in limits.items():
        if field in listing and field.endswith("URL"):
            ok(listing[field].startswith("https://"), f"interface.{field} must use HTTPS")

    # --- icons --------------------------------------------------------------
    print("Icons:")
    check_image("logo", listing.get("logo"))
    check_image("composerIcon", listing.get("composerIcon"))
    for optional in ("logoDark", "composerIconDark"):
        if optional in listing:
            check_image(optional, listing[optional])

    # --- onboarding skill ---------------------------------------------------
    onboarding = ext.get("onboardingSkill")
    if onboarding:
        ok(onboarding.startswith("./"), "onboardingSkill must be a ./-prefixed path")
        path = PLUGIN / onboarding[2:]
        ok(path.is_file(), f"onboardingSkill target missing: {onboarding}")

    # --- skills -------------------------------------------------------------
    skills_dir = PLUGIN / "skills"
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
    experts = [p for p in skill_dirs if p.name.startswith("infeara-")]
    ok(len(experts) == EXPECTED_SKILLS, f"expected {EXPECTED_SKILLS} expert skills, found {len(experts)}")
    ok(any(p.name == "get-started" for p in skill_dirs), "skills/get-started (onboarding) is missing")
    print(f"\nSkills: {len(skill_dirs)} folders")
    for d in skill_dirs:
        skill_md = d / "SKILL.md"
        if not ok(skill_md.is_file(), f"{d.name}: SKILL.md missing"):
            continue
        text = skill_md.read_text()
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not ok(match is not None, f"{d.name}: YAML frontmatter missing"):
            continue
        front = match.group(1)
        fm_name = re.search(r"^name:\s*(.+)$", front, re.M)
        fm_desc = re.search(r"^description:\s*(.+)$", front, re.M)
        ok(fm_name is not None, f"{d.name}: frontmatter 'name' missing")
        ok(fm_desc is not None, f"{d.name}: frontmatter 'description' missing")
        if fm_name:
            value = fm_name.group(1).strip().strip('"')
            ok(value == d.name, f"{d.name}: frontmatter name '{value}' must match the folder")
            ok(len(value) <= 64, f"{d.name}: name must be <= 64 chars")
        if fm_desc:
            value = fm_desc.group(1).strip().strip('"')
            ok(len(value) >= 40, f"{d.name}: description is too short to trigger reliably")
            ok(len(value) <= 1024, f"{d.name}: description exceeds 1024 chars")
        # supporting files referenced from the skill body must ship
        for rel in sorted(set(re.findall(r"(?:assets|references)/[A-Za-z0-9._-]+", text))):
            ok((d / rel).is_file(), f"{d.name}: referenced file missing: {rel}")
    if len(experts) != EXPECTED_SKILLS:
        warnings.append(f"{len(experts)} expert skills bundled; run ./scripts/build-plugin.sh to resync skills/")

    # --- plugin.json uniqueness across the repo -------------------------------
    # A Claude plugin ZIP must contain exactly one file named plugin.json.
    # The repo root (.claude-plugin/plugin.json) is that file; everything else is renamed.
    root = PLUGIN.parent.parent
    stray = [
        p for p in root.rglob("plugin.json")
        if ".git" not in p.parts and "dist" not in p.parts
        and p != root / ".claude-plugin" / "plugin.json"
    ]
    ok(not stray, "extra files named plugin.json (rename them): "
       + ", ".join(str(s.relative_to(root)) for s in stray))
    ok((root / ".claude-plugin" / "plugin.json").is_file(),
       "repo root manifest missing: .claude-plugin/plugin.json")

    return report()


def report() -> int:
    print(f"\n{checks} checks")
    for warning in warnings:
        print(f"WARN  {warning}")
    if errors:
        print(f"\n{len(errors)} FAILURE(S):")
        for error in errors:
            print(f"  FAIL  {error}")
        return 1
    print("PASS  plugin package is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
