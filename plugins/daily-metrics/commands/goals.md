---
description: Set and track goals, view streaks
argument-hint: [set|view|streaks] [metric-name]
allowed-tools: mcp__supabase__execute_sql, mcp__supabase__apply_migration, AskUserQuestion
---

Set targets for metrics and track goal progress.

## Input
Action: $1 (set, view, streaks)
Metric: $2

## Goal Storage
Goals are stored in metric_definitions.validation_rules as JSONB:
```json
{
  "goal": {
    "type": "minimum|maximum|target|streak",
    "value": 7,
    "unit": "hours",
    "period": "daily|weekly|monthly"
  },
  "min": 0,
  "max": 24
}
```

## Actions

### SET
Create or update a goal for a metric:

1. Query metric to get current settings
2. Ask goal type:
   - **Minimum**: At least X per period (e.g., 7h sleep minimum)
   - **Maximum**: No more than X (e.g., max 2000 calories)
   - **Target**: Aim for exactly X (e.g., 75kg weight target)
   - **Streak**: Complete X days in a row (e.g., 30-day meditation streak)
   - **Completion rate**: X% of days in period

3. Ask for target value
4. Ask for period (daily, weekly, monthly)
5. Update validation_rules with goal

```sql
UPDATE metric_definitions
SET validation_rules = jsonb_set(
  COALESCE(validation_rules, '{}'),
  '{goal}',
  $goal_json
)
WHERE id = $metric_id;
```

### VIEW
Display goal progress for one or all metrics:

```
Goal Progress
══════════════════════════════════════

HABITS
────────────────────────────────────────
Morning meditation
  Goal: 30-day streak
  Progress: ████████████░░░░░░░░  12/30 days
  Status: 🔥 On track (40%)

Reading
  Goal: 90% completion rate (monthly)
  Progress: █████████████████░░░  85%
  Status: ⚠️ Slightly behind

HEALTH
────────────────────────────────────────
Weight
  Goal: Reach 74.0 kg
  Current: 74.8 kg
  Progress: █████████████████░░░  ↓0.8 to go
  Status: ✓ On track

Sleep Duration
  Goal: Minimum 7h daily
  This week: 7.2h avg
  Met goal: 5/7 days (71%)
  Status: ✓ Meeting goal
```

### STREAKS
Show current and best streaks for all habits:

Query streak data:
```sql
WITH streak_data AS (
  SELECT
    m.id, m.name,
    de.date,
    de.boolean_value,
    de.date - (ROW_NUMBER() OVER (PARTITION BY m.id ORDER BY de.date))::int AS streak_group
  FROM daily_entries de
  JOIN metric_definitions m ON de.metric_id = m.id
  WHERE m.data_type = 'boolean' AND de.boolean_value = true
)
SELECT name, COUNT(*) as streak_length, MIN(date) as streak_start
FROM streak_data
GROUP BY id, name, streak_group
ORDER BY streak_length DESC
```

Display format:
```
Streak Tracker 🔥
══════════════════════════════════════

CURRENT STREAKS
────────────────────────────────────────
🔥 Reading               12 days  Dec 6 - today
🔥 Morning meditation    5 days   Dec 19 - today
   Exercise              0 days   (last: Dec 20)
   Journaling            0 days   (never started)

BEST STREAKS (ALL TIME)
────────────────────────────────────────
📈 Reading               21 days  Nov 1-21, 2024
📈 Morning meditation    14 days  Nov 15-28, 2024
📈 Exercise              7 days   Oct 1-7, 2024

STREAK GOALS
────────────────────────────────────────
Morning meditation: 12/30 days to goal ████░░░░░░
Reading: 12/21 days (beat best!) ██████████░
```

## Goal Suggestions
When setting goals, suggest based on:
- Current performance (aim 10-20% improvement)
- Scientific recommendations (7-9h sleep, etc.)
- User's historical best performance
