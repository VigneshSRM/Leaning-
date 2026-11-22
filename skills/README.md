# Infeara Agent Skills for Claude

22 Claude Agent Skills (Agent Skills open standard) covering Infeara's executive, go-to-market, finance, technology, operations, audit, security, legal, and content functions.

Each skill is a folder containing a `SKILL.md` with YAML frontmatter (`name` + `description`) and a focused playbook. Claude auto-discovers skills by matching the `description` against the user's request — no manual invocation needed, though you can also name a skill explicitly (e.g. *"Use the Infeara CFO skill to…"*).

## Skill catalog

| # | Skill (folder) | Persona | Experience | Use for |
|---|----------------|---------|------------|---------|
| 1 | `infeara-ceo` | Chief Executive Officer | 38+ yrs | Strategy, vision, board, M&A, executive decisions |
| 2 | `infeara-marketing-expert` | Marketing Expert | 30+ yrs | Positioning, GTM, campaigns, demand generation |
| 3 | `infeara-sales-expert` | Sales Expert | 30+ yrs | Pipeline, proposals, pricing, negotiation, forecasting |
| 4 | `infeara-cfo` | Chief Financial Officer | 38+ yrs | Budget, P&L, pricing, cash flow, unit economics |
| 5 | `infeara-cto` | Chief Technical Officer | 38+ yrs | Tech strategy, architecture, build-vs-buy |
| 6 | `infeara-coo` | Chief Operating Officer | 38+ yrs | Operations, delivery, SOPs, capacity, quality |
| 7 | `infeara-rd-expert` | Research & Development Expert | 38+ yrs | Research, prototypes, feasibility, innovation |
| 8 | `infeara-client-success-manager` | Client Success Manager | 38+ yrs | Onboarding, retention, renewals, QBRs, health |
| 9 | `infeara-lead-auditor` | Lead Auditor | 38+ yrs | Internal / ISO audits, findings, CAPA |
| 10 | `infeara-ciso-auditor` | CISO Auditor | 38+ yrs | Security audits, ISO 27001, SOC 2, risk assessment |
| 11 | `infeara-cloud-associate` | Cloud Associate | 38+ yrs | AWS / Azure / GCP, migration, FinOps, landing zones |
| 12 | `infeara-devops-expert` | DevOps Expert | 38+ yrs | CI/CD, Kubernetes, IaC, monitoring, SRE |
| 13 | `infeara-compliance-manager` | Compliance Manager | 38+ yrs | Compliance systems, policies, audit readiness |
| 14 | `infeara-server-system-admin` | Server & System Administrator | 38+ yrs | Servers, patching, backup, troubleshooting |
| 15 | `infeara-network-administrator` | Network Administrator | 38+ yrs | Networks, VPN, DNS, firewalls, troubleshooting |
| 16 | `infeara-cyber-security-expert` | Cyber Security Expert | 38+ yrs | Threats, vulnerabilities, IR, hardening |
| 17 | `infeara-legal-expert` | Legal Expert | 38+ yrs | Contracts, NDAs, MSAs, SOWs, redlines |
| 18 | `infeara-business-management-expert` | Business & Management Expert | 38+ yrs | Business plans, org design, KPIs, performance |
| 19 | `infeara-founder` | Founder | 45+ yrs | 0-to-1, vision, fundraising, pivots |
| 20 | `infeara-cofounder` | Co-founder | 45+ yrs | Co-founder roles, equity, partnerships, conflict |
| 21 | `infeara-digital-marketing-expert` | Digital Marketing Expert | 49+ yrs | Google Ads & Meta Ads, PPC, ROAS, paid media |
| 22 | `infeara-content-creator-expert` | Content Creator Expert | 38+ yrs | Blogs, social, video scripts, newsletters |

## How Claude uses these skills

1. **Automatic:** Claude reads each skill's `description` and loads the matching skill when your request fits. Example: *"Build a Google Ads plan for our cloud services"* → loads `infeara-digital-marketing-expert`.
2. **Explicit:** Name the skill: *"Use infeara-cfo to review this pricing model."*
3. **Chained:** Skills cross-reference each other (see "Working With Other Infeara Skills" in each file). Example: CEO strategy → CFO numbers → CTO feasibility → COO delivery plan.

## Install

### Claude Code (this repo — already wired)

Skills are mirrored to `.claude/skills/` so Claude Code in this repo discovers them automatically. Just open Claude Code here and ask.

### Claude Code (any other project)

```bash
# Install all 22 skills to your personal Claude skills folder
./scripts/install-skills.sh

# Or install to a specific project only
./scripts/install-skills.sh --project /path/to/your/project

# Or install a single skill
./scripts/install-skills.sh --skill infeara-cfo
```

### Claude.ai (web)

Upload a skill as a zip: zip one skill folder (it must contain `SKILL.md` at the root of the zip), then upload via Settings → Capabilities → Skills. Repeat per skill, or upload the whole `skills/` set one folder at a time.

### Other agents (Cursor, Codex, etc.)

Copy any skill folder into your agent's skills directory — the `SKILL.md` format follows the open Agent Skills standard (`name` + `description` frontmatter).

## Repository layout

```
skills/                      # Canonical skills (edit here)
  infeara-ceo/SKILL.md
  infeara-cfo/SKILL.md
  … (22 skills)
.claude/skills/              # Mirror for Claude Code auto-discovery (do not edit separately)
  infeara-ceo/SKILL.md
  …
scripts/install-skills.sh    # Installer for other projects / personal folder
CLAUDE.md                    # Routing guide for Claude in this repo
```

> **Editing rule:** Edit files under `skills/` only, then re-mirror:
> `cp -r skills/infeara-* .claude/skills/`

## Skill format

Every `SKILL.md` follows the same structure so Claude can load them efficiently:

- **Frontmatter:** `name` (matches folder) + trigger-rich `description`
- **Role / When to Use / Core Expertise:** who the persona is and when to invoke it
- **Operating Principles + Playbooks:** how the persona works, with templates
- **Deliverables + Quality Checklist:** what to produce and how to verify it
- **Working With Other Infeara Skills + Guardrails:** handoffs and safety limits
