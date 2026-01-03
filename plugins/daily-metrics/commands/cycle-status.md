---
description: View current cycle goals status, streaks, and requirements
argument-hint: [date: defaults to today]
allowed-tools: mcp__supabase__execute_sql
---

Show comprehensive status of current cycle goals including progress, streaks, and what's needed to achieve each goal.

## Input
- Date: $1 (optional, defaults to CURRENT_DATE)

## Process

1. **Get current cycle goals with progress**:
```sql
WITH cycle_info AS (
  SELECT
    cg.id as goal_id,
    cg.goal_text,
    cg.cycle_start_date,
    cg.cycle_end_date,
    cg.status,
    tc.name as category_name,
    tc.icon as category_icon,
    (cg.cycle_end_date - cg.cycle_start_date + 1) as total_days,
    (CURRENT_DATE - cg.cycle_start_date + 1) as days_elapsed,
    (cg.cycle_end_date - CURRENT_DATE) as days_remaining
  FROM cycle_goals cg
  JOIN tracking_categories tc ON cg.category_id = tc.id
  WHERE CURRENT_DATE BETWEEN cg.cycle_start_date AND cg.cycle_end_date
    AND cg.status = 'active'
)
SELECT * FROM cycle_info ORDER BY category_name;
```

2. **Get daily entries for current cycle** (for metrics that can be tracked):
```sql
SELECT
  md.name as metric_name,
  md.data_type,
  tc.name as category_name,
  de.date,
  de.boolean_value,
  de.numeric_value
FROM daily_entries de
JOIN metric_definitions md ON de.metric_id = md.id
JOIN tracking_categories tc ON md.category_id = tc.id
WHERE de.date >= (SELECT MIN(cycle_start_date) FROM cycle_goals WHERE status = 'active' AND CURRENT_DATE BETWEEN cycle_start_date AND cycle_end_date)
  AND de.date <= CURRENT_DATE
ORDER BY tc.name, md.name, de.date;
```

3. **Calculate streaks** for boolean metrics:
```sql
WITH ordered_entries AS (
  SELECT
    md.name,
    de.date,
    de.boolean_value,
    ROW_NUMBER() OVER (PARTITION BY md.id ORDER BY de.date DESC) as rn
  FROM daily_entries de
  JOIN metric_definitions md ON de.metric_id = md.id
  WHERE md.data_type = 'boolean'
    AND de.date <= CURRENT_DATE
),
streak_calc AS (
  SELECT
    name,
    date,
    boolean_value,
    SUM(CASE WHEN boolean_value = false OR boolean_value IS NULL THEN 1 ELSE 0 END)
      OVER (PARTITION BY name ORDER BY date DESC) as break_group
  FROM ordered_entries
)
SELECT
  name,
  COUNT(*) FILTER (WHERE break_group = 0 AND boolean_value = true) as current_streak
FROM streak_calc
GROUP BY name;
```

## Output Format

```
Cycle Status: [cycle_start_date] → [cycle_end_date]
══════════════════════════════════════════════════════════
Day [days_elapsed] of [total_days] | [days_remaining] days remaining
Progress: [████████░░░░░░░░░░░░] XX%

CATEGORY: [category_name] [category_icon]
────────────────────────────────────────────────────────
Goal: [goal_text]
  Progress: X/Y completed
  Streak: 🔥 X days (or ❌ broken)

  Status Table:
  | Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... |
  |-----|---|---|---|---|---|---|---|-----|
  |     | ✅| ✅| ✅| - | - | - | - | ... |

  To achieve goal: Need X more in Y days (Z% rate required)
  Margin: [X days buffer] or [No room for error!]

[Repeat for each category/goal]

══════════════════════════════════════════════════════════
SUMMARY
────────────────────────────────────────────────────────
🟢 On track: [list goals with buffer]
🟡 Tight: [list goals with no margin]
🔴 At risk: [list goals that are mathematically difficult/impossible]
```

## Goal-Metric Mapping

Parse goal_text to extract target numbers:
- "X/Y [metric]" → target is X out of Y
- "X [metric] sessions/days" → target is X total
- "X% [metric]" → target is X percent completion

Common patterns:
- "21/21 phone boundaries (100%)" → 21 completions needed
- "15 meditation sessions" → 15 completions needed
- "18 clean eating days" → 18 completions needed
- "15 early bedtimes" → 15 completions needed
- "15 exercise sessions" → 15 completions needed

## Status Indicators

- 🟢 **On track**: Can miss ≥3 more days and still achieve goal
- 🟡 **Tight**: Can miss 1-2 more days
- 🔴 **Critical**: No room for error OR already impossible
- ✅ Completed day
- ❌ Missed day
- ⬜ Future/unlogged day
- 🔥 Active streak

## Example Output

```
Cycle Status: Jan 1 → Jan 21, 2026
══════════════════════════════════════════════════════════
Day 3 of 21 | 18 days remaining
Progress: [███░░░░░░░░░░░░░░░░░] 14%

HABITS ✓
────────────────────────────────────────────────────────
📌 21/21 phone boundaries (100%)
   Done: 3/21 | Streak: 🔥 3 days

   |  1 |  2 |  3 |  4 |  5 |  6 |  7 | ... | 21 |
   | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ | ... | ⬜ |

   → Need: 18 more in 18 days (100% required)
   → Status: 🔴 No room for error

📌 15 meditation sessions
   Done: 0/15 | Streak: ❌ (0 days)

   |  1 |  2 |  3 |  4 |  5 |  6 |  7 | ... | 21 |
   | ❌ | ❌ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ... | ⬜ |

   → Need: 15 more in 18 days (83% required)
   → Status: 🟢 3 days buffer

[... continue for all goals ...]

══════════════════════════════════════════════════════════
SUMMARY
────────────────────────────────────────────────────────
🟢 On track (3+ day buffer):
   • Exercise (5 days buffer)
   • Meditation (3 days buffer)
   • Early Bedtime (3 days buffer)

🔴 Critical (no margin):
   • Phone Boundaries - must be perfect
   • Clean Eating - must be perfect
```
