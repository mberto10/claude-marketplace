---
name: Behavior Mapping
description: This skill should be used when the user asks to "set up tracking", "what should I track", "map behaviors to goals", "identify leading indicators", "which habits matter", "connect actions to outcomes", or needs to identify which daily behaviors produce their defined targets.
version: 1.0.0
---

# Behavior Mapping

Map optimization targets to the daily behaviors that produce them.

## Purpose

Targets are lagging indicators — they change slowly. This skill identifies the leading indicators (behaviors) that actually move the targets. Track behaviors daily, outcomes weekly/monthly.

## Core Concept: Leading vs. Lagging

| Type | Definition | Track Frequency |
|------|------------|-----------------|
| **Leading** | Behaviors (inputs you control) | Daily |
| **Lagging** | Outcomes (results of behaviors) | Weekly/Monthly |

**Key insight:** You cannot directly control lagging indicators. Control leading indicators and trust the algorithm.

## The Process

### 1. Identify the Algorithm

For each target, determine: What behaviors actually produce this outcome?

| Domain | Target | Known Algorithm (Behaviors) |
|--------|--------|----------------------------|
| Productivity | Deep work hours | Time blocking + environment design + energy management |
| Learning | Skill acquisition | Deliberate practice + spaced repetition + application |
| Finance | Savings rate | Automated transfers + spending awareness |
| Writing | Published output | Daily writing habit + editing process + shipping |
| Health | Body composition | Nutrition + resistance training + sleep |
| Coding | Features shipped | Focused blocks + reduced meetings + clear priorities |

Research evidence-based approaches. Do not guess.

### 2. Extract Trackable Behaviors

For each algorithm component, identify the **minimum trackable unit**:

| Target | Algorithm Component | Trackable Behavior |
|--------|--------------------|--------------------|
| Deep work capacity | Time blocking | Deep work hours logged |
| Deep work capacity | Environment design | Distraction-free session? (Y/N) |
| Skill acquisition | Deliberate practice | Practice sessions completed |
| Skill acquisition | Spaced repetition | Anki reviews done? (Y/N) |
| Savings rate | Automated transfers | (Automated — no tracking needed) |

### 3. Apply Minimum Viable Tracking

Choose the **simplest tracking that provides useful signal**:

| Level | Type | Example | When to Use |
|-------|------|---------|-------------|
| 1 | **Automated** | Syncs from device/app | When possible |
| 2 | **Boolean** | Did I do it? Y/N | Default choice |
| 3 | **Simple count** | How many? | When quantity matters |
| 4 | **Duration** | How long? | When time matters |
| 5 | **Detailed log** | Full description | Only if truly necessary |

**Start with boolean.** Add detail only if needed for feedback.

### 4. Verify the Connection

For each behavior → target mapping, check:
- Is there evidence this behavior produces this outcome?
- How long until results expected? (Set expectations)
- What could interfere? (Confounding factors)

### 5. Output: Tracking Schema

```yaml
domain: [domain]
target: [target name]

behaviors:
  - name: [behavior name]
    type: [boolean|count|duration|rating]
    unit: [unit if applicable]
    frequency: daily
    target_connection: [direct|indirect]
    expected_lag: [time to see results]

outcomes:
  - name: [outcome name]
    type: [aggregation|measurement]
    source: [how calculated]
    frequency: [weekly|monthly]
```

## Database Schema

```sql
-- Behaviors table
CREATE TABLE behaviors (
  id UUID PRIMARY KEY,
  domain TEXT,
  name TEXT,
  type TEXT, -- boolean, count, duration, rating
  frequency TEXT, -- daily, weekly
  target_id UUID REFERENCES targets(id),
  created_at TIMESTAMPTZ
);

-- Daily logs table
CREATE TABLE daily_logs (
  id UUID PRIMARY KEY,
  date DATE,
  behavior_id UUID REFERENCES behaviors(id),
  value JSONB, -- {completed: true} or {minutes: 90}
  notes TEXT,
  created_at TIMESTAMPTZ
);
```

## Anti-Patterns

**Do not track:**
- Behaviors with no clear connection to targets
- Things that can be automated instead of logged
- Detailed data that will never be analyzed
- More than 5-7 daily inputs (friction kills compliance)

**Do track:**
- Minimum behaviors that produce targets
- At simplest level providing feedback
- Only what will actually be reviewed
