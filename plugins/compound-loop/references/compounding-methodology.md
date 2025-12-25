# Compounding Methodology

> Reference document for compound-loop plugin. Loaded by reflection-craft, discovery-craft, and consolidation-craft skills.

## Core Philosophy

The compound loop is a four-step feedback cycle where each iteration improves the next: **Plan → Work → Review → Compound**.

The critical insight: most workflows skip the fourth step. They plan, work, review, repeat—but the learnings stay in people's heads. The compound step makes learning *architectural*: explicitly capturing and encoding lessons so future cycles inherit them.

> "AI engineering makes you faster today. Compounding engineering makes you faster tomorrow, and each day after."

## The Compound Loop

```
PLAN (40%)
├── Research codebase, patterns, context
├── Study best practices
└── Output: Clear implementation approach

WORK (20%)
├── Execute per plan
└── Create artifacts

REVIEW (40%)
├── Evaluate output quality
├── Extract lessons learned
└── Apply human judgment

COMPOUND (ongoing)
├── Lessons → skills, CLAUDE.md, docs
├── Patterns → reusable components
├── Decisions → codified rules
└── Future cycles inherit all of this
```

The 80/20 split is intentional: 80% planning/review, 20% execution. Execution is increasingly commoditized; the boundaries—planning and review—are where human judgment creates value.

## What Makes Learning Worth Encoding

Not all observations should become permanent rules. Apply these decision gates:

### Recurrence Likelihood
- Will this situation come up again?
- Is this a one-off edge case or a pattern?

### Maintenance Cost
- Is the rule simple enough to maintain?
- Will encoding this add value or clutter?

### Architecture Fit
- Does this align with existing patterns?
- Will this help or confuse future sessions?

### Testability
- Can compliance be verified?
- Is this specific enough to act on?

## The Heuristics Format

Learnings should be **1-line, testable rules**, not essays:

**Good:**
```
When fetching >100 traces from Langfuse, always use pagination to avoid timeouts.
[src:2025-12-25T1430Z__langfuse-analysis]
```

**Bad:**
```
I learned that when you're doing Langfuse analysis, it's really important
to think about how many traces you're looking at because if there are too
many the analysis gets unfocused...
```

The good format:
- Is actionable (you know exactly what to do)
- Is testable (did I paginate? is batch size reasonable?)
- Has traceability (source reference tells you where this came from)

## Where Learnings Land

Different types of learnings have different homes:

| Learning Type | Destination |
|--------------|-------------|
| Plugin behavior improvement | Skill update, new command |
| Workflow pattern | CLAUDE.md or skill reference |
| Bug prevention | Specialized reviewer or hook |
| Missing capability | New skill or command |
| Architecture decision | Documentation or CLAUDE.md |

## Anti-Patterns

### Over-Codification
Too many rules calcify the system. Rules that made sense in context become constraints that prevent adaptation. Prune stale rules, don't just add.

### Essay Learnings
Vague, long-form observations get ignored. If it can't be a 1-line testable rule, it might not be encodable.

### Skipping the Compound Step
"We'll document it later." Later never comes. The loop only works if compounding is non-negotiable.

### Encoding Opinions as Rules
Prefer measurable guardrails (performance, reliability, correctness) over style opinions. "Always use guard clauses" is opinion; "Validate API inputs before processing" is testable.

## Connected Ideas

This methodology connects to:

**Skills as Modular Knowledge**: Learnings become packaged, loadable modules. The sophistication of your skills library compounds over time.

**Agent-Leverageable Architecture**: Build abstractions that agents can introspect and extend. Registry patterns, self-describing components, clear extension points—all enable agents to participate in the compound loop.

## The Spiral, Not the Circle

> "It's not a circle (plan-do-review-repeat). It's a spiral going upward. Each loop is higher than the last because it stands on everything the previous loops deposited."

Every cycle should ask:
- What did we learn?
- How do we encode it so we never have to learn it again?
- Where does this learning belong?
