---
description: Visualize progress with ASCII charts
argument-hint: [metric-name] [timeframe: "last 7 days" | "March 2025" | "this week vs last"]
allowed-tools: mcp__supabase__execute_sql
---

Generate ASCII visualizations for tracking progress.

## Input
- Metric (optional): $1
- Timeframe: $2 or remaining arguments

## Process

1. **Parse timeframe** from user input:
   - "last 7 days" / "last week" → past 7 days
   - "last 30 days" / "last month" → past 30 days
   - "March 2025" / "2025-03" → specific month
   - "this week vs last" → comparison mode
   - "this month vs last" → month comparison
   - Default: last 7 days

2. **If no metric specified**, show overview of all active metrics

3. **Query data**:
   ```sql
   SELECT
     m.name, m.data_type, m.unit, c.name as category,
     de.date, de.boolean_value, de.numeric_value
   FROM daily_entries de
   JOIN metric_definitions m ON de.metric_id = m.id
   JOIN tracking_categories c ON m.category_id = c.id
   WHERE de.date BETWEEN [start] AND [end]
     AND m.is_active = true
   ORDER BY de.date
   ```

## Visualization Formats

### Boolean Metrics (Habits)
```
Morning meditation (last 7 days)
══════════════════════════════════════
Mon Tue Wed Thu Fri Sat Sun
 ✓   ✓   ✗   ✓   ✓   ✓   ✓     6/7 (86%)
```

### Numeric Metrics (Sparkline)
```
Weight (last 30 days)
══════════════════════════════════════
75.5 ─┐
      │    ╭─╮
75.0 ─┤ ╭──╯ ╰──╮
      │╭╯       ╰╮
74.5 ─┴──────────╰─
      Dec 1       Dec 30

Current: 74.8 kg | Trend: ↓ 0.7 kg | Avg: 75.1 kg
```

### Streak Display
```
Reading (streak)
══════════════════════════════════════
🔥 Current streak: 12 days
📈 Best streak: 21 days (Nov 2024)
✓ Completion rate: 78% (last 30 days)
```

### Comparison Mode
```
Sleep Duration: This Week vs Last Week
══════════════════════════════════════
         This Week    Last Week
Mon      7.5h ████    6.5h ███
Tue      8.0h █████   7.0h ████
Wed      6.0h ███     7.5h ████
Thu      7.0h ████    8.0h █████
Fri      7.5h ████    7.0h ████
─────────────────────────────────────
Avg      7.2h         7.2h      (=)
```

### Overview Dashboard
```
Daily Metrics Overview (Dec 18-24)
══════════════════════════════════════

HABITS                          Streak  Rate
────────────────────────────────────────────
✓ Morning meditation            5 days  86%
✓ Reading                       12 days 100%
✗ Exercise                      0 days  43%

HEALTH                          Current  Trend
────────────────────────────────────────────
Weight                          74.8 kg  ↓0.7
Blood pressure                  120/80   →

SLEEP                           Avg      Range
────────────────────────────────────────────
Duration                        7.2h     6-8h
Quality                         7.5/10   6-9
```

## Chart Characters
- Progress bars: █ ▓ ▒ ░
- Sparklines: ─ │ ╭ ╮ ╰ ╯
- Status: ✓ ✗ ● ○
- Trends: ↑ ↓ →
- Fire: 🔥 (streaks)
