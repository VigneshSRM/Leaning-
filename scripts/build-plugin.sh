#!/usr/bin/env bash
# Build the Infeara ChatGPT/Codex plugin package.
#
#   ./scripts/build-plugin.sh                # sync skills from skills/ and build dist/infeara-plugin-<version>.zip
#   ./scripts/build-plugin.sh --marketplace  # also write .agents/plugins/marketplace.json for local testing
#   ./scripts/build-plugin.sh --no-zip       # sync skills only
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
    -h|--help) sed -n '2,6p' "$0"; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

VERSION="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["version"])' "$PLUGIN/plugin.json")"

echo "==> Syncing skills/ -> plugins/infeara/skills/"
rm -rf "$PLUGIN/skills"/infeara-*
for d in "$SRC"/infeara-*/; do
  name="$(basename "$d")"
  mkdir -p "$PLUGIN/skills/$name"
  cp "$d/SKILL.md" "$PLUGIN/skills/$name/SKILL.md"
done
count=$(find "$PLUGIN/skills" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
echo "    $count skill folders (22 experts + onboarding)"

if [[ $ZIP -eq 1 ]]; then
  mkdir -p "$DIST"
  zip_path="$DIST/infeara-plugin-$VERSION.zip"
  rm -f "$zip_path"
  echo "==> Building $zip_path"
  ( cd "$PLUGIN" && zip -qr -X "$zip_path" \
      plugin.json README.md assets skills .claude-plugin \
      -x '*.DS_Store' '*__MACOSX*' )
  echo "    $(unzip -l "$zip_path" | tail -n 1 | awk '{print $2}') entries, $(du -h "$zip_path" | cut -f1)"
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
