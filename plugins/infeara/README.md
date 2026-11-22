# Infeara — ChatGPT & Codex Plugin

One plugin that packages all 22 Infeara expert skills, with the Infeara mark as the plugin icon.

```
infeara/
├── plugin.json                 # Agent Plugins manifest + OpenAI listing metadata
├── assets/
│   ├── logo.png                # 1024×1024 primary listing icon
│   └── composer-icon.png       # 512×512 composer icon
├── skills/
│   ├── get-started/SKILL.md     # onboarding + routing skill
│   └── infeara-*/SKILL.md       # 22 expert skills
└── .claude-plugin/plugin.json   # same package installable in Claude Code
```

Skills are copied from the repo's canonical `skills/` folder by `scripts/build-plugin.sh` — edit them there, never here.

## Install

### ChatGPT / Codex (plugin directory)

1. `./scripts/build-plugin.sh` → produces `dist/infeara-plugin-1.0.0.zip` with `plugin.json` at the archive root.
2. Go to [platform.openai.com/plugins](https://platform.openai.com/plugins) → **Upload new or existing plugin**.
3. Choose your verified developer identity, upload the ZIP, resolve any automated findings, then submit for review.

### ChatGPT desktop (local testing, no upload)

1. Copy `plugins/infeara` into `$REPO_ROOT/plugins/` of the repo you test from (it is already there).
2. Add `.agents/plugins/marketplace.json` (see `scripts/build-plugin.sh --marketplace`).
3. Restart the ChatGPT desktop app, open the Plugins Directory, pick the local marketplace, install **Infeara**, and start a new chat.

### Claude Code

```bash
/plugin install infeara --marketplace VigneshSRM/Leaning-   # from the repo marketplace
claude --plugin-dir plugins/infeara                          # or load this package for one session
./scripts/install-skills.sh                                  # or install the 22 skills globally
```

### Claude.ai

Upload the 22 folders in `skills/` one at a time as skill zips (Settings → Capabilities → Skills), or use the Claude Code plugin above.

## What ships in the manifest

| Field | Value |
|---|---|
| `name` / `version` | `infeara` / `1.0.0` |
| Display name | Infeara |
| Subtitle | 22 expert business skills |
| Category | Productivity |
| Brand colour | `#055998` (light) · `#F16935` (dark) |
| Icons | `assets/logo.png` 1024² · `assets/composer-icon.png` 512² |
| Onboarding skill | `skills/get-started/SKILL.md` |
| MCP server | none — skills-only plugin |

## Before you submit

These listing URLs require real, publicly reachable pages owned by the publisher. They are deliberately **not** in `plugin.json` so the package ships no invented links:

- [ ] `websiteURL` — Infeara product page (HTTPS)
- [ ] `supportURL` — support / contact page (HTTPS)
- [ ] `privacyPolicyURL` — published privacy policy (HTTPS)
- [ ] `termsOfServiceURL` — published terms (HTTPS)
- [ ] Developer identity verified in OpenAI Platform → Settings → Organization → General
- [ ] `brandColor`/`brandColorDark` re-checked if the palette changes (≥2:1 contrast on white / #212121)

Add them under `extensions.com.openai.interface` once the pages exist. Skills-only packages pass metadata validation without all four URLs, but a published privacy policy is still required by the plugin guidelines.

## Verify the package

```bash
python3 scripts/validate-plugin.py          # schema, limits, icons, skills
./scripts/build-plugin.sh                   # copy skills + rebuild the ZIP
```

The validator checks the Agent Plugins identity fields, every listing limit, icon format and dimensions, the onboarding path, and each skill's frontmatter (`name` must equal the folder, `description` required).
