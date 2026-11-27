# Infeara Agent Skills for Claude & ChatGPT

51 Agent Skills (open Agent Skills standard) covering Infeara's executive, go-to-market, finance, technology, operations, audit, security, legal, and content functions.

Each skill is a folder containing a `SKILL.md` with YAML frontmatter (`name` + `description`) and a focused playbook. Claude and ChatGPT auto-discover skills by matching the `description` against the user's request — no manual invocation needed, though you can also name a skill explicitly (e.g. *"Use the Infeara CFO skill to…"*).

The same 51 skills ship in two packages:

| Package | Location | Install |
|---|---|---|
| **Claude skills** | `skills/` (mirrored to `.claude/skills/`) | `./scripts/install-skills.sh`, or `/plugin install infeara --marketplace VigneshSRM/Leaning-` |
| **ChatGPT/Codex plugin** | `plugins/infeara/` | `./scripts/build-plugin.sh` → upload `dist/infeara-chatgpt-1.0.0.zip` |

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
| 23 | `infeara-document-writer` | Professional Document Writer | 25+ yrs | Cover pages, pagination, letterhead, typography, print PDF |
| 24 | `infeara-guide` | Library Guide | — | Routes requests, documents repo layout and build steps |

### Delivery team — 10 roles that work together

| # | Skill | Team role | Owns |
|---|---|---|---|
| 25 | `infeara-team-lead` | Team Lead | Assigns roles, owns gates and the engagement outcome |
| 26 | `infeara-sprint-orchestrator` | Orchestrator | Sprint rhythm, backlog, ceremonies, flow |
| 27 | `infeara-team-engagement-manager` | Engagement Manager | Discovery, scope, commitments, sign-off |
| 28 | `infeara-team-solution-architect` | Solution Architect | Solution design, NFRs, ADRs |
| 29 | `infeara-team-tech-lead` | Technical Lead | Standards, task breakdown, code review |
| 30 | `infeara-team-implementation-engineer` | Implementation Engineer | Building, unit tests, pull requests |
| 31 | `infeara-team-qa-engineer` | QA Engineer | Test strategy, acceptance, defect triage |
| 32 | `infeara-team-deployment-engineer` | Deployment Engineer | Environments, releases, rollback, monitoring |
| 33 | `infeara-team-documentation-analyst` | Documentation Analyst | Runbooks, handover, user guides |
| 34 | `infeara-team-security-analyst` | Security Analyst | Threat models, hardening, security sign-off |
| 35 | `infeara-team-project-manager` | Project Manager | Plan, schedule, dependencies, risks, status |
| 36 | `infeara-team-account-manager` | Account Manager | Relationship, health, renewal, expansion |

### Revenue team — 15 roles for sales and marketing

| # | Skill | Role | Owns |
|---|---|---|---|
| 37 | `infeara-revenue-lead` | Revenue Team Lead | Target, pipeline coverage, arbitration |
| 38 | `infeara-revenue-pipeline-orchestrator` | Pipeline Orchestrator | Funnel reviews, SLA, forecast truth |
| 39 | `infeara-revenue-gtm-strategist` | GTM Strategist | Segmentation, positioning, launch, pricing input |
| 40 | `infeara-revenue-product-marketing` | Product Marketing | Messaging, proof, enablement, battlecards |
| 41 | `infeara-revenue-brand-manager` | Brand Manager | Voice, visual system, brand audits |
| 42 | `infeara-revenue-content-manager` | Content Manager | Editorial engine, production, repurposing |
| 43 | `infeara-revenue-campaign-manager` | Campaign Manager | Integrated campaigns, launches, webinars, events |
| 44 | `infeara-revenue-seo-specialist` | SEO & Web Specialist | Organic search, technical SEO, landing pages |
| 45 | `infeara-revenue-marketing-ops` | Marketing Operations | Martech, tracking, attribution, lead scoring |
| 46 | `infeara-revenue-sdr` | SDR / Lead Qualifier | Outbound, inbound qualification, meeting booking |
| 47 | `infeara-revenue-account-executive` | Account Executive | Discovery, demo, business case, close |
| 48 | `infeara-revenue-solutions-consultant` | Solutions Consultant | Technical validation, POCs, scoping |
| 49 | `infeara-revenue-sales-ops` | Sales Operations | CRM, stages, forecast mechanics, territories |
| 50 | `infeara-revenue-proposal-manager` | Proposal / Bid Manager | RFPs, proposals, compliance matrices |
| 51 | `infeara-revenue-partnerships-manager` | Partnerships Manager | Channel, reseller, alliance pipeline |

**How the revenue team works:** `infeara-revenue-lead` sets the target and decomposes it into funnel maths; seven marketing roles create demand, six sales roles convert it, and `infeara-revenue-pipeline-orchestrator` runs the weekly review. Both directions carry SLAs, and both teams report one pipeline number. Ask with: *"Build the Infeara revenue team for this target"* or *"Plan sales and marketing for this offer"*.

**How the delivery team works:** `infeara-team-lead` assigns work along the engagement lifecycle (qualify → discover → design → plan → build → verify → release → document → handover → close). Each role hands off a named artefact with acceptance criteria; `infeara-sprint-orchestrator` runs the weekly rhythm. Ask for the team with: *"Assemble the Infeara team for this client"* or *"Who owns this?"*.

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

### ChatGPT / Codex (plugin)

```bash
./scripts/build-plugin.sh            # syncs skills/, validates, builds dist/infeara-chatgpt-1.0.0.zip
python3 scripts/validate-plugin.py   # 471 checks: manifest, limits, icons, skills
```

Upload the ZIP at [platform.openai.com/plugins](https://platform.openai.com/plugins) (verified developer identity required), resolve any automated findings, and submit. The package uses the Infeara mark as its icon and adds a `get-started` onboarding skill that routes requests to the right expert. See [`plugins/infeara/README.md`](plugins/infeara/README.md) for the local-marketplace testing flow and the pre-submission URL checklist.

### Other agents (Cursor, Codex, etc.)

Copy any skill folder into your agent's skills directory — the `SKILL.md` format follows the open Agent Skills standard (`name` + `description` frontmatter).

## Repository layout

```
skills/                      # Canonical skills (edit here)
  infeara-ceo/SKILL.md
  infeara-cfo/SKILL.md
  … (23 skills)
  infeara-document-writer/   # SKILL.md + references/ + assets/ (letterhead & report templates)
.claude/skills/              # Mirror for Claude Code auto-discovery (do not edit separately)
plugins/infeara/             # ChatGPT/Codex plugin package, generated skills, icon assets
scripts/install-skills.sh    # Installer for other projects / personal folder
scripts/build-plugin.sh      # Sync skills → plugin + build dist zip
scripts/validate-plugin.py   # Validate the plugin package
CLAUDE.md                    # Routing guide for Claude in this repo
```

> **Editing rule:** Edit files under `skills/` only, then re-sync:
> ```bash
> cp -r skills/infeara-* .claude/skills/
> ./scripts/build-plugin.sh
> ```

## Skill format

Every `SKILL.md` follows the same structure so Claude can load them efficiently:

- **Frontmatter:** `name` (matches folder) + trigger-rich `description`
- **Role / When to Use / Core Expertise:** who the persona is and when to invoke it
- **Operating Principles + Playbooks:** how the persona works, with templates
- **Deliverables + Quality Checklist:** what to produce and how to verify it
- **Working With Other Infeara Skills + Guardrails:** handoffs and safety limits
