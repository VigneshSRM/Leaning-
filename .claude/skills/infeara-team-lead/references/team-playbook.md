# Infeara 10-Person Delivery Team — Operating Playbook

Use with `infeara-team-lead` and `infeara-sprint-orchestrator`. Everything here is designed to be copied into a project folder on day one.

## 1. The team

| # | Role | Primary artefact | Decides |
|---|---|---|---|
| 1 | Engagement Manager | Scope statement | What is in/out of scope |
| 2 | Solution Architect | Design doc + ADRs | Solution shape and trade-offs |
| 3 | Technical Lead | Task breakdown + standards | Technical quality and reviews |
| 4 | Implementation Engineer | Working code + tests | How to implement within design |
| 5 | QA Engineer | Test plan + acceptance record | Whether quality is sufficient |
| 6 | Deployment Engineer | Release + rollback plan | Whether it is safe to release |
| 7 | Documentation Analyst | Runbook + handover pack | What "documented" means |
| 8 | Security Analyst | Threat model + findings | Security sign-off |
| 9 | Project Manager | Plan + risk register | Schedule and trade-off options |
| 10 | Account Manager | Health scorecard + renewal plan | Relationship and commercial health |

Orchestration: **Team Lead** (gates, escalation, one narrative) and **Sprint Orchestrator** (ceremonies, backlog, flow).

## 2. Engagement lifecycle and handoffs

```
QUALIFY      Account Manager ──▶ go/no-go memo ──▶ Team Lead
DISCOVER     Engagement Manager ──▶ Scope statement + assumptions ──▶ Architect, PM
DESIGN       Solution Architect ──▶ Design doc + ADRs ──▶ Tech Lead, Security Analyst
                                  ──▶ Security Analyst threat model ──▶ Architect (loop)
PLAN         Project Manager ──▶ Plan + RACI + risk register ──▶ Team Lead (baseline)
BUILD        Tech Lead ──▶ Task breakdown ──▶ Implementation Engineer
                                  ──▶ code + tests ──▶ Tech Lead review
VERIFY       QA Engineer ──▶ Test plan, acceptance record ──▶ Team Lead
             Security Analyst ──▶ findings + sign-off ──▶ Team Lead
RELEASE      Deployment Engineer ──▶ Release + rollback plan ──▶ Team Lead (gate)
DOCUMENT     Documentation Analyst ──▶ Runbook + handover pack ──▶ Engagement Manager
HANDOVER     Engagement Manager ──▶ client sign-off ──▶ Account Manager
CLOSE & GROW Account Manager + PM ──▶ retrospective + expansion plan
```

**Every arrow is a handoff.** Record it with artefact, owner, acceptance criterion, and date.

## 3. Gate checklist (Team Lead signs)

| Gate | Evidence required | Who attests |
|---|---|---|
| G1 Scope baselined | Signed scope statement, explicit out-of-scope | Engagement Manager |
| G2 Design approved | Design doc, ADRs, NFR sheet | Architect + Security Analyst |
| G3 Plan baselined | Plan, RACI, risk register, critical path | Project Manager |
| G4 Build complete | Code reviewed, unit tests green, debt logged | Tech Lead |
| G5 Quality verified | Acceptance record, no open S1/S2 | QA Engineer |
| G6 Security cleared | Threat model, no open critical/high | Security Analyst |
| G7 Release ready | Release plan, tested rollback, monitoring window | Deployment Engineer |
| G8 Documented | Runbook, handover pack, owner + review date | Documentation Analyst |
| G9 Accepted | Written client acceptance | Engagement Manager |
| G10 Closed | Retrospective, expansion plan, lessons logged | Account Manager + PM |

## 4. Weekly rhythm

| Day | Ceremony | Owner | Output |
|---|---|---|---|
| Mon | Stand-up + week plan | Sprint Orchestrator | Week commitments per role |
| Tue–Thu | Stand-up (15 min) | Sprint Orchestrator | Blockers owned |
| Wed | Risk review (top 3) | Project Manager | Updated risk register |
| Thu | Client status | Account Manager + PM | One-page status, one voice |
| Fri | Demo + retro (sprint end) | Sprint Orchestrator | Acceptance + one experiment |

## 5. Conflict resolution

| Conflict | First resolver | Then |
|---|---|---|
| Scope ambiguity | Engagement Manager | Team Lead |
| Design disagreement | Solution Architect (ADR) | Team Lead |
| Code quality dispute | Technical Lead | Team Lead |
| Test vs schedule | QA Engineer holds; PM offers four options | Team Lead → COO/CEO |
| Security blocks release | Security Analyst holds | Team Lead → CISO Auditor |
| Client escalation | Account Manager | Team Lead + CEO |

**Non-negotiable:** no role signs off its own work; no gate is skipped for a date; no verbal scope change.

## 6. Team assembly brief (copy this)

```
Engagement: <client> — <outcome in one sentence>
Team Lead: <name/role>            Sprint Orchestrator: <name/role>
Account Manager: <>               Project Manager: <>
Engagement Manager: <>            Solution Architect: <>
Technical Lead: <>                Implementation Engineer: <>
QA Engineer: <>                   Deployment Engineer: <>
Documentation Analyst: <>         Security Analyst: <>
Milestones: M1 <date> | M2 <date> | M3 <date>
Gates: G1–G10 per checklist, dates below each milestone
Cadence: weekly stand-up, Thu client status, sprint demo Friday
Escalation: role → team lead → COO/CEO (see table)
Risks (top 3): <risk — owner — trigger date>
Decisions needed now: <decision — owner — date>
```

## 7. What good looks like

- Every deliverable has one owner and a written acceptance criterion.
- Every gate has evidence, and the Team Lead can show it in under a minute.
- The client hears one status, from one voice, that matches the risk register.
- QA and Security have said no at least once and been supported for it.
- Handover happens with the client's own staff able to run the thing.
- The retrospective produces one experiment, not a list of regrets.
