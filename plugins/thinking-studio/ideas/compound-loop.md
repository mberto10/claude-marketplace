---
idea: The Compound Loop
sources: ["Every.io - Dan Shipper", "Kieran Klaassen compound engineering"]
connects_to: ["skills-as-modules", "value-at-boundaries", "execution-vaporization", "anti-complexity-engineering", "compound-engineering-parallels"]
categories: ["ai-strategy", "systems-thinking", "engineering-practice"]
---

# The Compound Loop

## My Understanding

A four-step feedback loop where each cycle improves the next: **Plan → Work → Review → Compound**.

The magic is in the fourth step - "compound" - where lessons, patterns, and decisions get captured and fed back into the system. Every bug becomes a permanent lesson. Every successful pattern becomes reusable. The system accumulates capability, not just code.

This is different from "learning from experience" in a vague sense. It's a **designed architecture** for institutional memory. Each cycle explicitly asks: "What did we learn? How do we encode it so future cycles benefit?"

## Why This Resonates

I've thought about skills-as-modules and knowledge packaging, but this adds the **loop structure** that makes it compound. It's not just "capture knowledge" - it's "capture knowledge *as part of every work cycle*, feeding it back automatically."

The 80/20 split is what made it click: 80% planning/review, 20% work. That's not just "planning is important" - it's a fundamental inversion of where effort goes. The work step becomes almost incidental. The planning and review steps - the *boundaries* - dominate.

This matches my intuition that execution is vaporizing, but gives it a concrete operational shape.

## Examples That Stuck

**The four steps in practice:**

```
PLAN (40%)
├── Agents research codebase, commit history
├── Agents study best practices online
├── Multiple agents in parallel, human synthesizes
└── Output: Detailed implementation plan

WORK (20%)
├── Agents write code per plan
└── Agents create tests

REVIEW (40%)
├── Engineer evaluates output quality
├── Engineer extracts lessons learned
└── Human judgment applied

COMPOUND (ongoing)
├── Lessons → CLAUDE.md or docs/*.md
├── Patterns → specialized reviewers
├── Decisions → codified rules
└── Future cycles inherit all of this
```

**The CLAUDE.md as accumulator:**
Every decision gets written down. "Why we prefer guard clauses over nested ifs." "How we handle rate limiting." This file grows with each cycle, and every future agent reads it. Your taste becomes executable.

**The specialized reviewer pattern:**
After discovering a production bug from missing rate-limit handling, you add it to a reviewer checklist. Every future PR gets checked. The bug becomes impossible to repeat.

## How I Use It

I reach for this when:
- Designing any AI-assisted workflow (not just coding)
- Thinking about how to make processes improve over time
- Evaluating whether a system is truly learning or just executing
- Building institutional memory into teams/tools

My trigger questions:
- "Where does learning get captured in this loop?"
- "Does each cycle make the next one better, or just different?"
- "What's the compound step here?"

## My Explanatory Moves

I usually start with the contrast:

"Most work is a loop: plan, do, review, repeat. But there's a hidden step most people skip - compounding. What did you learn? How do you encode it so you never have to learn it again?"

Then I make it concrete:

"Imagine every bug you fix also updates a checklist that prevents that bug forever. Imagine every architectural decision gets written down so you never have to re-debate it. That's the compound step. Each cycle deposits something that future cycles inherit."

The visual that works: "It's not a circle (plan-do-review-repeat). It's a spiral going upward. Each loop is higher than the last because it stands on everything the previous loops deposited."

## Tensions & Edges

**Not all lessons are easily codifiable.** Tacit judgment, contextual decisions, "it depends" situations resist clean encoding. The loop works best for things that *can* be written down.

**Compounding requires discipline.** It's easy to skip the compound step when you're rushing. "We'll document it later." Later never comes. The loop only works if the compound step is non-negotiable.

**Over-codification can calcify.** If you encode too many rules, the system becomes rigid. Rules that made sense in context become constraints that prevent adaptation. Need a way to prune/update the accumulated knowledge, not just add to it.

**The loop assumes a stable domain.** If the problem space changes radically, accumulated lessons might become irrelevant or misleading. Works best in domains with continuity.

**Who maintains the accumulated knowledge?** As the knowledge base grows, someone has to curate it. Otherwise it becomes a junk drawer of stale rules.

## Source Passages

> "Each bug, failed test, or a-ha problem-solving insight gets documented and used by future agents."

> "Compounding engineering: building self-improving development systems where each iteration makes the next one faster, safer, and better."

> "AI engineering makes you faster today. Compounding engineering makes you faster tomorrow, and each day after."

> "Every time you make a decision, capture it and codify it to stop the AI from making the same mistake again."
