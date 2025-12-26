---
name: Metrics Review
description: This skill should be used when the user asks to "review my week", "analyze my data", "what's working", "check progress", "weekly review", "monthly review", "look at my metrics", "show my trends", or wants to extract signal from tracked data and close the feedback loop.
version: 1.0.0
---

# Metrics Review

Extract signal from noise and close the feedback loop between behaviors and outcomes.

## Purpose

Tracking without review is wasted friction. This skill structures the review process to tighten feedback and enable data-driven iteration.

## Review Cadence

| Review Type | Frequency | Duration | Focus |
|-------------|-----------|----------|-------|
| **Daily glance** | Daily | 30 sec | Did I execute today? |
| **Weekly review** | Weekly | 10-15 min | Compliance + trends + adjustments |
| **Monthly review** | Monthly | 30-60 min | Target progress + system evaluation |

## Daily Glance (30 seconds)

Quick check on today's execution:
- Completed key behaviors?
- Notes to capture?
- Tomorrow's intention set?

**No analysis.** Just logging and awareness.

## Weekly Review Process

### 1. Behavior Compliance Check

For each tracked behavior, calculate:

```
Compliance = (days executed / days intended) × 100%
```

| Behavior | Target Days | Actual | Compliance | Status |
|----------|-------------|--------|------------|--------|
| [name] | [N] | [n] | [%] | [OK/Review] |

**Threshold:** Flag anything below 80% for friction audit.

**Low compliance is usually friction, not willpower.**

### 2. Outcome Trends (Lagging Indicators)

Compare trends not snapshots:

```
This week vs. Last week vs. 4-week average
```

| Outcome | This Week | Last Week | 4-Week Avg | Trend |
|---------|-----------|-----------|------------|-------|
| [metric] | [value] | [value] | [value] | [arrow] |

**Ignore single-point fluctuations.** Look for directional trends.

### 3. Leading → Lagging Analysis

Ask: Are behavior changes producing outcome changes?

| Behavior Change | Expected Outcome | Actual | Conclusion |
|-----------------|------------------|--------|------------|
| [change] | [expected] | [actual] | [working/investigate] |

**Attribution is hard.** Look for patterns over 4+ weeks.

### 4. Insights and Adjustments

Based on the data:
- **Continue:** High compliance + producing results
- **Investigate:** Low compliance (friction) or no results (algorithm)
- **Stop:** Tracking that provides no useful signal

### 5. Weekly Output

```yaml
weekly_review:
  week_of: [date]
  domain: [domain]

  compliance:
    [behavior]: [%]

  trends:
    [outcome]: "[direction and value]"

  insights:
    - "[observation]"

  next_week:
    - "[focus area]"
```

## Monthly Review Process

### 1. Target Progress

For each defined target:

| Target | Baseline | Current | Goal | Progress | On Track? |
|--------|----------|---------|------|----------|-----------|
| [name] | [start] | [now] | [goal] | [%] | [Y/N] |

### 2. System Evaluation

Questions to answer:
- Are the right behaviors being tracked?
- Is tracking friction acceptable?
- Are targets still the right targets?
- What's working that should be preserved?
- What's not working that needs intervention?

### 3. Optimization Stack Check

Which layer needs attention?

| Symptom | Layer | Action |
|---------|-------|--------|
| Unclear success definition | Target | Re-run target-definition |
| Doing behaviors, no results | Algorithm | Research better approaches |
| Know what to do, not doing it | Friction | Run friction-audit |
| Not reviewing data | Feedback | Simplify review process |

## Supabase Queries

### Weekly Compliance

```sql
SELECT
  behavior_id,
  COUNT(*) FILTER (WHERE value->>'completed' = 'true') as completed,
  COUNT(*) as total,
  ROUND(100.0 * COUNT(*) FILTER (WHERE value->>'completed' = 'true') / COUNT(*), 1) as compliance
FROM daily_logs
WHERE date >= CURRENT_DATE - 7
GROUP BY behavior_id;
```

### Trend Comparison

```sql
SELECT
  DATE_TRUNC('week', date) as week,
  SUM((value->>'minutes')::int) as total_minutes
FROM daily_logs
WHERE behavior_id = '[behavior_id]'
GROUP BY week
ORDER BY week DESC
LIMIT 4;
```

### Outcome Averages

```sql
SELECT
  AVG((value->>'rating')::numeric) as avg_rating
FROM daily_logs
WHERE behavior_id = '[outcome_id]'
  AND date >= CURRENT_DATE - 7;
```

## Presentation Guidelines

When presenting review results:
1. Lead with wins (positive reinforcement)
2. Show trends, not just numbers
3. Suggest specific, actionable changes
4. Acknowledge external factors
5. Offer options, not mandates
