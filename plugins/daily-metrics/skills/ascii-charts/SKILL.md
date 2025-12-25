---
name: ASCII Charts
description: This skill should be used when generating progress visualizations, charts, graphs, sparklines, progress bars, or dashboards in the terminal. Provides patterns for ASCII-based data visualization in Claude Code responses.
version: 1.0.0
---

# ASCII Chart Patterns for Terminal Visualization

Use these patterns when generating visual representations of tracking data.

## Progress Bars

### Basic Horizontal Bar
```
Progress: ████████████░░░░░░░░ 60%
```

Characters: █ (filled), ░ (empty)
Width: 20 characters standard

### Labeled Bar
```
Sleep (7.5h)  ███████████████░░░░░ 75%
Weight goal   ██████████████████░░ 90%
Exercise      ████████░░░░░░░░░░░░ 40%
```

### Multi-segment Bar
```
Week Overview: ██████░██████░░░░░░░
               M T W T F S S
```

## Sparklines

### Simple Trend Line
```
Last 7 days: ▁▂▄▃▅▆█
```

Characters: ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ (8 levels)

### With Value Labels
```
Weight (kg): 75.5 ─▂▃▄▃▂▁─ 74.8
                   ↓ trending down
```

### Extended Sparkline
```
Sleep hours (30 days):
▄▅▆▃▄▅▆▇▅▄▃▄▅▆▅▄▅▆▇▆▅▄▃▄▅▆▅▄▅▆
```

## Box-Drawing Charts

### Line Chart
```
8h ─┤     ╭─╮
    │  ╭──╯ ╰╮
7h ─┤╭─╯     ╰─╮
    │          ╰─
6h ─┴────────────
    Mon       Sun
```

Characters: ─ │ ╭ ╮ ╰ ╯ ┼ ├ ┤ ┬ ┴

### Bar Chart (Vertical)
```
    █
    █ █   █
  █ █ █ █ █
  █ █ █ █ █ █
──────────────
  M T W T F S S
```

### Comparison Chart
```
         This Week    Last Week
Mon      ████████     ██████
Tue      ██████████   ████████
Wed      ████         ████████
Thu      ████████     ██████████
Fri      ████████     ████████
```

## Tables

### Simple Table
```
┌──────────┬───────┬────────┐
│ Metric   │ Value │ Status │
├──────────┼───────┼────────┤
│ Weight   │ 74.8  │ ↓      │
│ Sleep    │ 7.5h  │ ✓      │
│ Exercise │ 3/7   │ ⚠      │
└──────────┴───────┴────────┘
```

### Wide Table
```
══════════════════════════════════════════════════
  Metric              Value      Trend    Status
══════════════════════════════════════════════════
  Morning meditation  6/7        ↑ +2     ✓ Good
  Weight              74.8 kg    ↓ -0.4   ✓ Good
  Sleep duration      7.2h avg   → 0      ○ Ok
  Exercise            3/7        ↓ -1     ⚠ Watch
══════════════════════════════════════════════════
```

## Status Indicators

### Checkmarks and Crosses
```
✓ Completed    ✗ Missed    ○ Pending    ● Active
```

### Trend Arrows
```
↑ Improving    ↓ Declining    → Stable
```

### Emoji Status
```
🔥 Streak active    💪 Goal met    ⚠️ Attention needed
✨ Personal best    📈 Trending up    📉 Trending down
```

### Progress Indicators
```
● ● ● ● ● ○ ○  (5/7 complete)
[▓▓▓▓▓▓▓▓░░]  (80% progress)
```

## Dashboards

### Daily Summary
```
═══════════════════════════════════════
  TODAY: December 24, 2024
═══════════════════════════════════════

HABITS              Done
───────────────────────────────────────
✓ Morning meditation
✓ Reading (45 min)
✗ Exercise
○ Journaling (pending)

METRICS             Value       vs Avg
───────────────────────────────────────
Sleep               7.5h        +0.3h
Weight              74.8 kg     -0.2kg
Mood                8/10        +1

STREAKS             Current    Best
───────────────────────────────────────
🔥 Reading          12 days    21 days
🔥 Meditation       5 days     14 days
```

### Weekly Overview
```
WEEK OF DEC 18-24
════════════════════════════════════════════════

            Mon Tue Wed Thu Fri Sat Sun  Total
Meditation   ✓   ✓   ✗   ✓   ✓   ✓   ✓   6/7
Reading      ✓   ✓   ✓   ✓   ✓   ✓   ✓   7/7
Exercise     ✓   ✗   ✗   ✓   ✗   ✓   ✗   3/7
────────────────────────────────────────────────
Sleep (h)   7.5 8.0 6.0 7.0 7.5 8.5 7.0  Avg: 7.4

HIGHLIGHTS
• Reading: 7-day perfect week! 🎉
• Sleep avg up 0.3h from last week
• Exercise needs attention (43%)
```

## Calendar Views

### Month Calendar
```
December 2024
───────────────────────────
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 ✓  ✓  ✓  ✓  ✗  ✓  ✓
 8  9 10 11 12 13 14
 ✓  ✓  ✓  ✓  ✓  ✓  ✓
15 16 17 18 19 20 21
 ✗  ✓  ✓  ✓  ✓  ✓  ✓
22 23 24
 ✓  ✓  ○
───────────────────────────
Completion: 19/23 (83%)
```

### Habit Heatmap
```
Meditation Heatmap (Dec)
░ = 0  ▒ = partial  █ = done

Week 1: █ █ █ █ ░ █ █
Week 2: █ █ █ █ █ █ █
Week 3: ░ █ █ █ █ █ █
Week 4: █ █ █ · · · ·
```

## Formatting Guidelines

1. **Consistent widths**: Use fixed-width sections (40 or 60 chars)
2. **Clear headers**: Use ═══ for major sections, ─── for subsections
3. **Alignment**: Right-align numbers, left-align text
4. **Whitespace**: Use blank lines between sections
5. **Status at a glance**: Lead with visual indicators (✓, ✗, 🔥)
6. **Legends**: Include legend if symbols aren't obvious
7. **Context**: Always show timeframe and comparison basis
