---
name: Target Definition
description: This skill should be used when the user asks to "define goals", "set up tracking", "what should I optimize", "clarify my targets", "start tracking something new", "what does success mean", or wants to establish clear optimization targets in any domain (health, productivity, learning, finance, habits, creative output).
version: 1.0.0
---

# Target Definition

Define clear, measurable optimization targets before tracking anything.

## Purpose

The optimization stack principle: clarify the target first. Tracking without a clear target is wasted friction. This skill guides target definition for any domain.

## When to Use

- Starting to track something new
- Feeling unclear about what success means
- Tracking many things but unsure which matter
- Reviewing whether current targets still apply

## The Process

### 1. Identify the Domain

Common domains for personal tracking:

| Domain | Example Targets |
|--------|-----------------|
| Health | Body composition, energy, sleep, longevity |
| Productivity | Deep work hours, output volume, completion rate |
| Learning | Skill acquisition, knowledge retention, practice hours |
| Finance | Savings rate, investment growth, spending patterns |
| Creative | Writing output, code shipped, projects completed |
| Relationships | Quality time, communication frequency |
| Habits | Behavior consistency, streak maintenance |

### 2. Surface the True Target

Ask: What does success actually mean here?

Dig beneath surface statements:
- "I want to be more productive" → What does productive mean? Output volume? Quality? Both?
- "I want to learn X" → What level? Functional? Expert? Specific capability?
- "I want to save more" → What rate? For what purpose? By when?

**The target should answer:** If I achieve this, I'll know I succeeded.

### 3. Operationalize the Target

For each target, define:

| Field | Description |
|-------|-------------|
| **Outcome metric** | How to measure success |
| **Current baseline** | Where are you now? |
| **Target state** | Where do you want to be? |
| **Timeframe** | When to evaluate |
| **Constraints** | What must not be sacrificed |

### 4. Identify Proxy Risks

Every metric is a proxy for something deeper. Check:
- Is this the real target or a proxy?
- What could go wrong if optimizing only this number?
- What does the proxy hide?

| Domain | Common Proxy | What It Hides |
|--------|--------------|---------------|
| Productivity | Hours worked | Output quality, sustainability |
| Learning | Time spent | Actual retention, application |
| Finance | Income | Savings rate, net worth |
| Writing | Word count | Quality, coherence, value |
| Health | Weight | Body composition, markers |

### 5. Handle Multi-Objective Reality

Most real goals involve multiple targets:
- **Aligned** — Optimizing one helps the other
- **Orthogonal** — Independent, can optimize separately
- **Conflicting** — Trade-offs required

For conflicting targets:
- Acknowledge the trade-off explicitly
- Define hierarchy: "If X and Y conflict, I prioritize X because..."
- Or define constraints: "Maximize X subject to Y ≥ threshold"

### 6. Commit to 3-5 Targets Maximum

More targets = more tracking = more friction = less execution.

## Output Format

```yaml
domain: [domain name]
targets:
  - name: [target name]
    metric: [how to measure]
    baseline: [current value]
    goal: [target value]
    unit: [unit of measurement]
    timeframe: [evaluation period]
    priority: [1-5]
    constraints:
      - [constraint 1]
      - [constraint 2]
```

## Database Integration

Store target definitions in Supabase `targets` table:
- `id`, `domain`, `name`, `metric`, `baseline`, `goal`, `timeframe`, `priority`, `created_at`

Query existing targets before defining new ones to check for overlap or conflicts.

## Anti-Patterns

- Defining too many targets (>5 active)
- Vague targets without measurable outcomes
- Conflicting targets without explicit priority
- Changing targets frequently (prevents accumulation)
- Optimizing proxies while neglecting real goals
