---
name: Friction Audit
description: This skill should be used when the user asks to "reduce friction", "simplify tracking", "make this easier", "audit my system", "why is this so hard", "I keep forgetting to log", "tracking is tedious", "streamline my habits", or when behaviors aren't happening consistently and the system needs friction analysis.
version: 1.0.0
---

# Friction Audit

Systematically identify and reduce friction in any behavioral system.

## Purpose

The friction hypothesis: most failures are friction failures, not knowledge failures. You know what to do. Friction stops you from doing it. This skill audits friction and applies the reduction hierarchy.

## The Friction Reduction Hierarchy

```
1. ELIMINATE  — Remove the step entirely (best)
       |
2. AUTOMATE   — Make it happen without attention
       |
3. REDUCE     — Make it easier but still present
       |
4. TOLERATE   — Push through with willpower (worst)
```

**Most people operate at "tolerate."** Move up the hierarchy.

## Types of Friction

| Type | Definition | Examples |
|------|------------|----------|
| **Activation** | Cost to start | Decision fatigue, setup time, context switching |
| **Execution** | Cost to continue | Effort, complexity, time required |
| **Feedback** | Cost to learn | Delayed results, noisy data, unclear attribution |

Each type needs different interventions.

## The Audit Process

### 1. List All Friction Points

For each tracked behavior, identify friction at each stage:

| Behavior | Activation Friction | Execution Friction | Feedback Friction |
|----------|--------------------|--------------------|-------------------|
| [behavior] | [what stops starting] | [what makes continuing hard] | [what blocks learning] |

### 2. Score Each Friction Point (1-5)

- **1** — Trivial, barely notice
- **2** — Minor inconvenience
- **3** — Noticeable effort
- **4** — Significant barrier
- **5** — Often prevents the behavior

**Focus on 4s and 5s first.** These kill behaviors.

### 3. Apply the Hierarchy

For each high-friction point:

**ELIMINATE — Can we remove this entirely?**
- Do we need to track this at all?
- Can we remove this step from the process?
- Can we eliminate the decision by pre-committing?

**AUTOMATE — Can we make it happen without attention?**
- Can technology do this automatically?
- Can we create triggers that remove thinking?
- Can systems run on their own?

**REDUCE — Can we make it simpler?**
- Can we reduce the number of steps?
- Can we simplify what's tracked? (detailed → boolean)
- Can we batch it? (real-time → end of day)
- Can we template it? (same every day → no logging)

**TOLERATE — Accept consciously**
- Some friction is irreducible
- Accept it explicitly
- Budget willpower for only these items

### 4. The Tracking Paradox

**Tracking itself is friction.**

Every input added is execution friction. The goal is **minimum viable tracking** — enough feedback to iterate, not so much that tracking becomes the obstacle.

**Signs of over-tracking:**
- More than 5-7 daily inputs
- Tracking takes more than 2-3 minutes
- Logging is frequently skipped because tedious
- Data exists that is never reviewed
- Tracking feels like a chore

**Solution:** Eliminate low-value tracking. Keep only what gets reviewed.

### 5. Redesign the System

Document transformations:

| Before | Friction Score | Intervention | After | New Score |
|--------|----------------|--------------|-------|-----------|
| [original] | [4-5] | [eliminate/automate/reduce] | [new version] | [1-2] |

## Output Format

```yaml
friction_audit:
  date: [date]
  domain: [domain]

  high_friction_items:
    - behavior: [name]
      friction_type: [activation|execution|feedback]
      current_score: [4-5]
      intervention: [eliminate|automate|reduce]
      description: [what to change]
      new_expected_score: [1-2]

  eliminated:
    - "[tracking/behavior removed and why]"

  automated:
    - "[what now syncs automatically]"

  reduced:
    - "[what was simplified and how]"
```

## When to Re-Audit

- Behavior compliance drops below 80%
- After 2-4 weeks of stable tracking (optimization opportunity)
- When adding new targets or behaviors
- When life circumstances change significantly

## Common Friction Reductions

| Friction Source | Tolerate | Reduce | Automate | Eliminate |
|----------------|----------|--------|----------|-----------|
| Deciding what to do | Think each time | Weekly planning | Fixed schedule | Same thing daily |
| Data entry | Manual each event | End-of-day batch | Device sync | Don't track it |
| Finding tools | Search each time | Dedicated location | Always ready | Fewer tools |
| Multiple apps | Switch between | Single dashboard | Unified system | One app |
