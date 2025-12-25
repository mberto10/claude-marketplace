---
description: Run weekly or monthly review with insights
argument-hint: [week|month]
allowed-tools: mcp__supabase__execute_sql, AskUserQuestion
---

Generate a comprehensive periodic review with trends, insights, and goal adjustment suggestions.

## Input
Period: $1 (week, month) - defaults to week

## Process

1. **Determine date range**:
   - week: last 7 days
   - month: last 30 days

2. **Query comprehensive data**:
```sql
WITH period_data AS (
  SELECT
    m.id, m.name, m.data_type, m.unit, m.validation_rules,
    c.name as category,
    de.date, de.boolean_value, de.numeric_value
  FROM daily_entries de
  JOIN metric_definitions m ON de.metric_id = m.id
  JOIN tracking_categories c ON m.category_id = c.id
  WHERE de.date >= CURRENT_DATE - INTERVAL '$period days'
    AND m.is_active = true
),
previous_period AS (
  SELECT
    m.id, m.name,
    de.date, de.boolean_value, de.numeric_value
  FROM daily_entries de
  JOIN metric_definitions m ON de.metric_id = m.id
  WHERE de.date >= CURRENT_DATE - INTERVAL '$period * 2 days'
    AND de.date < CURRENT_DATE - INTERVAL '$period days'
    AND m.is_active = true
)
SELECT * FROM period_data, previous_period;
```

## Review Report Format

```
══════════════════════════════════════════════════════════
  WEEKLY REVIEW: Dec 18-24, 2024
══════════════════════════════════════════════════════════

📊 OVERVIEW
────────────────────────────────────────────────────────────
Total entries logged:     42
Active metrics:           8
Days with entries:        7/7 (100%)
Overall goal completion:  78%

🏆 WINS THIS WEEK
────────────────────────────────────────────────────────────
✓ Reading streak hit 12 days (new personal best approaching!)
✓ Sleep average improved: 7.2h → 7.5h (+0.3h)
✓ Weight trending down: 75.2kg → 74.8kg (-0.4kg)
✓ Meditation consistency at 86% (6/7 days)

⚠️ AREAS FOR ATTENTION
────────────────────────────────────────────────────────────
• Exercise only 3/7 days (43%) - below 70% target
• Missed journaling entirely this week
• Sleep quality dipped on Thu/Fri (work stress?)

📈 TRENDS VS LAST WEEK
────────────────────────────────────────────────────────────
                    This Week   Last Week   Change
Sleep duration      7.5h avg    7.2h avg    ↑ +0.3h
Sleep quality       7.8/10      7.2/10      ↑ +0.6
Weight              74.8 kg     75.2 kg     ↓ -0.4kg
Exercise days       3/7         4/7         ↓ -1 day
Meditation rate     86%         71%         ↑ +15%

🎯 GOAL PROGRESS
────────────────────────────────────────────────────────────
Morning meditation (30-day streak goal)
  ████████████░░░░░░░░░░░░░░░░░░  12/30 (40%)
  Pace: On track to complete Jan 6

Weight (reach 74.0 kg)
  ██████████████████░░░░░░░░░░░░  0.8 kg to go
  Pace: ~2 weeks at current rate

Reading (beat 21-day best streak)
  ████████████████████░░░░░░░░░░  12/21 (57%)
  Pace: Will beat record on Dec 27!

💡 INSIGHTS & SUGGESTIONS
────────────────────────────────────────────────────────────
1. Your meditation habit is solidifying - consider increasing
   to 15 minutes (currently tracking completion only)

2. Exercise pattern: You skip most on Wed/Thu. Consider:
   - Scheduling lighter workouts mid-week
   - Setting a "minimum viable workout" (10 min walk)

3. Sleep quality correlates with exercise (+0.8 on workout days)
   Another reason to prioritize exercise consistency.

4. Reading streak is strong! You're 9 days from your all-time
   best. Keep it up!

🔄 SUGGESTED GOAL ADJUSTMENTS
────────────────────────────────────────────────────────────
```

3. **Ask about adjustments** using AskUserQuestion:
   - "Based on this review, would you like to adjust any goals?"
   - Options: "Adjust exercise goal", "Add new metric", "Keep current goals", "Show more details"

4. **If adjustments requested**, use `/goals set` to update targets.

## Analysis Guidelines

- **Celebrate wins first** - positive reinforcement
- **Identify patterns** - day-of-week effects, correlations
- **Be specific** - include numbers, not just "improved"
- **Suggest actionable changes** - not just "do better"
- **Consider context** - note potential external factors
- **Compare to goals** - show progress toward targets
