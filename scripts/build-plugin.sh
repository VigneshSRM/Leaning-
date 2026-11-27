#!/usr/bin/env bash
# Build the Infeara plugin artifacts.
#
#   ./scripts/build-plugin.sh                # sync skills, build ChatGPT zip + repo zip
#   ./scripts/build-plugin.sh --no-zip       # sync skills only
#   ./scripts/build-plugin.sh --marketplace  # also write .agents/plugins/marketplace.json
#
# IMPORTANT — plugin.json naming rule:
#   A Claude plugin ZIP must contain EXACTLY ONE file named plugin.json.
#   This repo is itself the Claude plugin, so the only plugin.json is at
#   .claude-plugin/plugin.json (repo root). Everything else is renamed:
#     plugins/infeara/chatgpt-plugin.json          -> ChatGPT/Codex manifest
#     plugins/infeara/.claude-plugin/claude-plugin.json -> repo-plugin view of the package
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/skills"
PLUGIN="$REPO_ROOT/plugins/infeara"
DIST="$REPO_ROOT/dist"

ZIP=1
MARKETPLACE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-zip) ZIP=0; shift ;;
    --marketplace) MARKETPLACE=1; shift ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

VERSION="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["version"])' "$PLUGIN/chatgpt-plugin.json")"

echo "==> Syncing skills/ -> plugins/infeara/skills/"
rm -rf "$PLUGIN/skills"/infeara-*
for d in "$SRC"/infeara-*/; do
  name="$(basename "$d")"
  mkdir -p "$PLUGIN/skills/$name"
  # copy SKILL.md plus any bundled references/, assets/, scripts/
  cp -R "$d". "$PLUGIN/skills/$name/"
  rm -rf "$PLUGIN/skills/$name/.DS_Store"
done
count=$(find "$PLUGIN/skills" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
echo "    $count skill folders (24 experts + 12 team roles + onboarding)"

if [[ $ZIP -eq 1 ]]; then
  mkdir -p "$DIST"

  # --- ChatGPT/Codex package: its manifest must be named plugin.json INSIDE this zip ---
  chatgpt_zip="$DIST/infeara-chatgpt-$VERSION.zip"
  rm -f "$chatgpt_zip"
  echo "==> Building $chatgpt_zip"
  staging="$(mktemp -d)"
  cp -R "$PLUGIN"/. "$staging"/
  cp "$staging/chatgpt-plugin.json" "$staging/plugin.json"   # rename for the ChatGPT upload
  rm -f "$staging/chatgpt-plugin.json" "$staging/README.md"
  rm -rf "$staging/.claude-plugin"
  ( cd "$staging" && zip -qr -X "$chatgpt_zip" plugin.json assets skills \
      -x '*.DS_Store' '*__MACOSX*' )
  rm -rf "$staging"
  echo "    $(unzip -l "$chatgpt_zip" | tail -n 1 | awk '{print $2}') entries, $(du -h "$chatgpt_zip" | cut -f1)"

  # --- repo package: the repository IS the Claude plugin, so exactly one plugin.json ---
  repo_zip="$DIST/Leaning--arena-plugin-$VERSION.zip"
  rm -f "$repo_zip"
  echo "==> Building $repo_zip"
  ( cd "$REPO_ROOT" && zip -qr -X "$repo_zip" . \
      -x '.git/*' -x 'dist/*' -x '*.DS_Store' -x '__MACOSX/*' -x 'node_modules/*' )
  # exact basename match only — chatgpt-plugin.json / claude-plugin.json must not count
  manifests=$(unzip -l "$repo_zip" | awk '{n=$4} n ~ /(^|\/)plugin\.json$/ {c++} END {print c+0}')
  echo "    $(du -h "$repo_zip" | cut -f1), plugin.json files inside: $manifests"
  if [[ "$manifests" != "1" ]]; then
    echo "    ERROR: a Claude plugin zip must contain exactly one plugin.json" >&2
    exit 1
  fi
fi

if [[ $MARKETPLACE -eq 1 ]]; then
  mkdir -p "$REPO_ROOT/.agents/plugins"
  cat > "$REPO_ROOT/.agents/plugins/marketplace.json" <<'JSON'
{
  "name": "infeara-local",
  "plugins": [
    {
      "name": "infeara",
      "source": { "source": "local", "path": "./plugins/infeara" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Productivity",
      "interface": { "displayName": "Infeara" }
    }
  ]
}
JSON
  echo "==> Wrote .agents/plugins/marketplace.json (restart the ChatGPT desktop app to pick it up)"
fi

echo "==> Validating"
python3 "$REPO_ROOT/scripts/validate-plugin.py"
