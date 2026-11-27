# Using the Infeara Skills Like an Expert

The skills are not a menu of answers. They are a **staff**. Your job as the operator is to brief them
like you would brief a senior team: give context, name the deliverable, define what "good" means, and
demand the reasoning — not just the output.

Most people get junior work out of these skills for one reason: they ask like a customer.
Experts get expert work because they ask like a client with a budget and a deadline.

---

## 1. The mental model

```
NOVICE       "Hey CFO, how do I price this?"          → generic advice
COMPETENT    "Use infeara-cfo on this pricing model"  → structured but contextless
EXPERT       Role + real context + constraint + format + success test + explicit ask
             → a decision they can defend in a board meeting
```

Every skill contains: Role · When to Use · Core Expertise · Operating Principles · Playbooks ·
Deliverables · Quality Checklist · Working With · Guardrails. **You can invoke any of those
sections directly** — that is the single biggest upgrade available. See §4.

---

## 2. The six-part brief

Copy this every time. It works for any of the 51 skills.

```
ROLE:      Use the Infeara <role> skill.
SITUATION: <3–5 lines of real context: company, stage, numbers, constraint, history>
TASK:      <the one decision or artefact you need>
CONSTRAINT: <budget, deadline, headcount, legal, brand, non-negotiables>
FORMAT:    <length, structure, table vs memo, what sections you want>
SUCCESS:   <how you will judge it — "I can take this to the board", "20 minutes of reading">
```

### Weak vs expert prompt — the same request

**Weak**
> Use the CFO skill to help with our pricing.

**Expert**
> Use the Infeara CFO skill.
> SITUATION: B2B managed-services company, 14 staff, $1.2M ARR, 62% gross margin, 4-month runway of
> new business. Selling SOC monitoring to mid-market banks in the UAE. Two competitors price per
> endpoint ($18–24), we price per incident.
> TASK: Recommend a pricing model I can defend to the board on 12 December.
> CONSTRAINT: Cannot move below 55% gross margin. Sales team of two, no pricing analyst.
> FORMAT: One page. Table of three options with margin, cash impact, and win-rate effect. Then a
> recommendation with the reversible step.
> SUCCESS: I can present it without being asked a question I cannot answer.

Same skill, same model — completely different output. **Context is the product.**

---

## 3. The four modes of engagement

| Mode | When | How to ask |
|---|---|---|
| **Consult** | One question, one answer | "Use `<skill>` to answer X. Keep it under 300 words." |
| **Decide** | A commitment with a trade-off | "Use `<skill>` to give me a decision memo: options, recommendation, risks, kill criteria." |
| **Project** | Multiple deliverables, several functions | "Give this to the Infeara CEO. It needs marketing, finance and delivery." |
| **Standing engagement** | Ongoing work over weeks | "Act as the Infeara Team Lead for this engagement. Start with the plan, then hold cadence." |

Mode 3 is where the CEO routing lives. Mode 4 is underused and the most valuable: a skill can hold a
role across an entire engagement if you tell it to keep the thread.

---

## 4. Invoke the sections, not just the skill

This is expert-level usage. Every skill has named sections — call them by name.

| Ask for | What you get |
|---|---|
| "Use its **Operating Principles** to challenge my plan" | The skill turns on your thinking instead of producing a document |
| "Run its **Quality Checklist** against my draft and list failures" | A free, specific critique of your own work |
| "Apply its **Guardrails** — tell me what I am about to do wrong" | Risk catch before you commit |
| "Give me the **Playbook** for X, step by step" | Process, not prose |
| "Use the **Deliverables & Templates** section — fill the template with my data" | A finished artefact |
| "Read its **Working With** section and tell me who else I need" | Correct chaining |

> **Example:** *"Use `infeara-revenue-proposal-manager`, apply its Quality Checklist to this RFP
> response, and list every item that fails with the fix."* — that one prompt replaces an hour of review.

---

## 5. Force the reasoning out

By default a skill will give you a clean answer. Experts demand to see the working, because that is
where the value is.

Add one of these to any prompt:

- *"Show your assumptions separately, marked `[VERIFY]`, and tell me which one would change your answer most."*
- *"Give me the strongest argument against your own recommendation."*
- *"What would have to be true for the opposite decision to be right?"*
- *"State the kill criteria — the evidence that would make you reverse this."*
- *"Name what you are NOT recommending, and why."*
- *"Rate your confidence 1–5 per claim, and say what would raise it."*

The `[VERIFY]` habit matters: these skills are instructed never to invent financials, client facts or
legal advice. Push them into marking unknowns instead of smoothing over them.

---

## 6. Chain skills deliberately

A single skill is a specialist. Two or three, correctly ordered, is a company.

| Task | Chain |
|---|---|
| Enter a new market | `ceo` → `revenue-gtm-strategist` → `cfo` → `legal-expert` → `revenue-campaign-manager` |
| Win a big bid | `revenue-account-executive` → `revenue-solutions-consultant` → `cfo` → `revenue-proposal-manager` → `document-writer` |
| Ship a client project | `team-lead` → `team-engagement-manager` → `team-solution-architect` → `team-project-manager` → `team-qa-engineer` |
| Survive an audit | `lead-auditor` → `compliance-manager` → `ciso-auditor` → `document-writer` |
| Fix a churn problem | `client-success-manager` → `team-account-manager` → `coo` → `cfo` |

**Rule:** one skill per step, and make each step *produce an artefact* the next step consumes. Do not
ask four skills to "comment on" the same thing — that produces four opinions, not a chain.

When you do not know the chain, do not guess: *"Give this to the Infeara CEO — decompose it, pick the
internal roles, and return one plan."* That is exactly what the delegation protocol is for.

---

## 7. The quality ladder — check the output like an expert

After any substantial output, run this three-question audit:

1. **Is it specific to my situation?** If you could paste the answer into any company's deck, it failed.
   Re-ask with more context.
2. **Does it contain a decision, an owner and a date?** Advice without those is commentary.
3. **Which claim would embarrass me in the room?** Ask the skill to defend or retract that one.

Then run the skill's own **Quality Checklist** against its output. That is the closest thing to a free
second opinion in this library.

---

## 8. Anti-patterns that keep people at beginner level

| Anti-pattern | Why it fails | Do instead |
|---|---|---|
| "Make it good / make it professional" | No target to hit | Name the reader and what they must decide |
| Letting it decide everything ("you choose") | Shifts judgement you own | "Recommend, but flag the 3 calls I must make" |
| Accepting the first draft | First drafts are smooth and generic | Ask for the counter-argument, then the revision |
| Omitting numbers | Skills are told not to invent them, so they go vague | Give the real figures, or ask for a modelled range |
| Blending five skills into one reply | Contradictory voices, no owner | Chain them, or route through the CEO |
| Asking a skill to do strategy *and* write the doc | Two jobs, both mediocre | `ceo` decides → `document-writer` formats |
| Dumping 40 pages of context | Signal drowned | Give the 5 lines that matter + attach the rest |

---

## 9. Copy-paste starter prompts

**A. Board-ready decision**
```
Use the Infeara CEO skill. SITUATION: <5 lines>. TASK: decide <X> by <date>.
Give me the decision memo from its Playbooks section: options including doing nothing,
recommendation, risks with owners, kill criteria, and what we are NOT doing.
One page. Mark any assumption [VERIFY].
```

**B. Full growth plan from one target**
```
Give this to the Infeara CEO. We need <revenue target> by <date>.
Decompose it into workstreams, assign one internal role per workstream, sequence the
handoffs, and return the consolidated answer: decision, why with the funnel maths,
who did what, plan with owners and dates, top 3 risks, and the one decision you need from me.
```

**C. Audit my own work**
```
Use the Infeara <role> skill. Here is my <artefact>. Run its Quality Checklist against it,
list every failed item with a specific fix, then rewrite only the weakest section.
Do not rewrite what already passes.
```

**D. Stress-test a plan before committing**
```
Use the Infeara <role> skill. Here is the plan: <plan>. Apply its Operating Principles and
Guardrails. Tell me the three ways this fails, what would have to be true for it to work,
and the smallest reversible step to test it this week.
```

**E. A team engagement, run properly**
```
Act as the Infeara Team Lead for this engagement and hold the role for the whole conversation.
Client: <name>. Outcome: <what they must have>. Constraints: <budget, date, stack>.
Start with the assembly brief, name the 10 roles and their deliverables, then hold the
G1–G10 gates as we work. Tell me when a gate is at risk.
```

**F. Teach me the domain while we work**
```
Use the Infeara <role> skill as a mentor, not a ghostwriter. Before each recommendation,
give me the 2–3 questions an expert would ask here, and what a beginner gets wrong.
Then give the answer.
```

---

## 10. Where to run them

| Surface | How |
|---|---|
| **Claude Code (this repo)** | Already wired — just ask. Skills auto-load from `.claude/skills/` |
| **Claude Code, as a plugin** | `/plugin install infeara --marketplace VigneshSRM/Leaning-` |
| **Claude.ai** | Settings → Capabilities → Skills → upload a skill folder as a zip containing `SKILL.md` |
| **ChatGPT / Codex** | Build the plugin zip, upload at `platform.openai.com/plugins` |
| **Anywhere else** | `./scripts/install-skills.sh` — copies all 51 into `~/.claude/skills/` |

Tip: in Claude Code, name the skill in the first sentence (`"Use infeara-cfo"`). It removes ambiguity
about which of the 51 should answer, and it is faster than hoping auto-selection picks right.

---

## 11. The one-line summary

> **Brief like a client, name the skill, give the numbers, demand the reasoning, and audit the output
> against the skill's own checklist.** Do that and you are using a 38-year veteran. Skip it and you get
> a well-formatted intern.
