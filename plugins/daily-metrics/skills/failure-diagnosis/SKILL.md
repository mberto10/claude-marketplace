---
name: Failure Diagnosis
description: This skill should be used when the user asks "why isn't this working", "I'm stuck", "not making progress", "can't stick to habits", "what's wrong", "I keep failing at", "this isn't working", "why can't I", or when behaviors aren't happening or outcomes aren't improving despite effort.
version: 1.0.0
---

# Failure Diagnosis

When the system isn't working, diagnose which layer is failing.

## Purpose

The optimization stack has three layers: Target, Algorithm, Friction. Intervening at the wrong layer wastes effort. This skill diagnoses the actual problem.

## The Separation Principle

**Check in order:**
1. Is the target right? (Rare problem)
2. Is the algorithm right? (Sometimes the problem)
3. Is friction too high? (Usually the problem)

**Most failures are friction failures.** But check systematically.

## Diagnostic Flowchart

```
START: Something isn't working
              |
              v
+--------------------------------------+
| Are you executing the behaviors?     |
| (Check compliance: >80%?)            |
+--------------------------------------+
              |
       +------+------+
       |             |
      YES            NO
       |             |
       v             v
+------------+   +-----------------------------+
| Check      |   | FRICTION FAILURE            |
| Algorithm  |   | Know what to do but not     |
| & Target   |   | doing it.                   |
|            |   | -> Run friction-audit       |
+------------+   +-----------------------------+
       |
       v
+--------------------------------------+
| Are outcomes moving in the right     |
| direction? (Check trends)            |
+--------------------------------------+
              |
       +------+------+
       |             |
      YES            NO
       |             |
       v             v
+------------+   +-----------------------------+
| WORKING    |   | Possible ALGORITHM FAILURE  |
| Keep going |   | Behaviors not producing     |
|            |   | outcomes.                   |
+------------+   +-----------------------------+
                          |
                          v
              +-----------------------+
              | Has enough time       |
              | elapsed?              |
              +-----------------------+
                          |
                   +------+------+
                   |             |
                  YES            NO
                   |             |
                   v             v
              +---------+   +---------+
              | WRONG   |   | WAIT    |
              | ALGO or |   | Lagging |
              | TARGET  |   | indica- |
              |         |   | tors    |
              | Review  |   | are     |
              | both    |   | slow    |
              +---------+   +---------+
```

## Layer-Specific Diagnosis

### Friction Layer (Most Common — Check First)

**Symptoms:**
- Low behavior compliance (<80%)
- "I know what to do but don't do it"
- Starting but not finishing
- Skipping logging/tracking
- Feeling of "too hard" or "too much"
- Procrastination, avoidance

**Diagnostic questions:**
- What specifically stops execution?
- Is getting started the problem? (Activation friction)
- Is continuing the problem? (Execution friction)
- Is tracking itself the friction?

**Intervention:** Run friction-audit skill

### Algorithm Layer (Sometimes)

**Symptoms:**
- High behavior compliance (>80%)
- Outcomes not changing after sufficient time
- Effort without progress
- "I'm doing everything right but..."

**Diagnostic questions:**
- Are these behaviors actually connected to the outcome?
- Is the behavior being done correctly? (Quality not just quantity)
- Is there a better known approach for this target?
- Is something else interfering? (Confounding factors)
- Has enough time elapsed? (See timing table)

**Intervention:**
- Research evidence-based approaches
- Consult domain experts
- Re-run behavior-mapping with better algorithms

### Target Layer (Rare but Critical)

**Symptoms:**
- Achieving metrics but not satisfied
- Proxy drift — number improves, actual goal doesn't
- Constant goal-changing, pivoting
- Targets conflict and paralysis results
- Success feels empty

**Diagnostic questions:**
- Is this metric measuring what you actually care about?
- If you hit this number, would you feel successful?
- Have priorities changed since setting this target?
- Are you optimizing a proxy while neglecting the real goal?

**Intervention:** Re-run target-definition skill

## Expected Time to Results

**Lagging indicators are slow.** Before diagnosing algorithm failure, confirm enough time has passed:

| Domain | Target Type | Minimum Time |
|--------|-------------|--------------|
| Productivity | Output quality | 2-4 weeks |
| Learning | Skill improvement | 4-8 weeks |
| Health | Body composition | 4-8 weeks |
| Finance | Savings growth | 1-3 months |
| Habits | Automaticity | 4-8 weeks |
| Writing | Quality improvement | 4-8 weeks |

**If compliance is high but less than minimum time elapsed:** Keep executing.

## The Willpower Trap

When diagnosing friction failures, beware these responses:
- "I just need to try harder" — Rarely works
- "I need more discipline" — Willpower depletes
- "I'm being lazy" — Usually system problem, not character

**Friction is structural. Willpower is a resource.**

The answer is almost always: reduce friction, don't increase effort.

## Output Format

```yaml
diagnosis:
  date: [date]
  presenting_problem: "[user's description]"

  compliance_check:
    [behavior]: [%]  # Flag if <80%

  time_elapsed: [duration]
  expected_time_for_results: [duration]

  diagnosis: "[FRICTION|ALGORITHM|TARGET] FAILURE"
  layer: [friction|algorithm|target]

  reasoning: |
    [explanation of diagnosis]

  specific_issues:
    - "[issue 1]"
    - "[issue 2]"

  recommended_intervention: "[skill to run]"

  suggested_experiments:
    - "[experiment 1]"
    - "[experiment 2]"
```

## Quick Reference

| Compliance | Outcome Trend | Time | Diagnosis | Action |
|------------|---------------|------|-----------|--------|
| Low (<80%) | Any | Any | Friction | friction-audit |
| High (>80%) | Improving | Any | Working | Continue |
| High (>80%) | Flat | Short | Patience | Wait longer |
| High (>80%) | Flat | Long | Algorithm | Research alternatives |
| High (>80%) | Wrong direction | Any | Algorithm/Target | Deep review |
| Any | Success feels empty | Any | Target | target-definition |
