#!/usr/bin/env bash
# Install Infeara Agent Skills for Claude.
#
# Usage:
#   ./scripts/install-skills.sh                          # install all to ~/.claude/skills
#   ./scripts/install-skills.sh --project <dir>          # install all to <dir>/.claude/skills
#   ./scripts/install-skills.sh --skill infeara-cfo      # install one skill to ~/.claude/skills
#   ./scripts/install-skills.sh --skill infeara-cfo --project <dir>
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC="$REPO_ROOT/skills"

DEST="$HOME/.claude/skills"
SKILL=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project) DEST="$2/.claude/skills"; shift 2 ;;
    --skill)   SKILL="$2"; shift 2 ;;
    -h|--help)
      sed -n '2,8p' "$0"; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

if [[ ! -d "$SRC" ]]; then
  echo "Skills source not found: $SRC" >&2; exit 1
fi

mkdir -p "$DEST"

if [[ -n "$SKILL" ]]; then
  if [[ ! -f "$SRC/$SKILL/SKILL.md" ]]; then
    echo "Skill not found: $SKILL (available: $(ls "$SRC" | grep '^infeara-' | tr '\n' ' '))" >&2
    exit 1
  fi
  cp -r "$SRC/$SKILL" "$DEST/"
  echo "Installed $SKILL -> $DEST/$SKILL"
else
  for d in "$SRC"/infeara-*/; do
    name="$(basename "$d")"
    cp -r "$d" "$DEST/"
    echo "Installed $name -> $DEST/$name"
  done
  echo "Done. Restart Claude Code / Claude to pick up the skills."
fi
