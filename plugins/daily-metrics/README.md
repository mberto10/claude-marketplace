# daily-metrics

Personal tracking and goal management plugin for Claude Code, integrated with Supabase.

## Features

- **Daily Logging**: Parse freeform notes into structured metric entries with preview
- **Progress Visualization**: ASCII charts with flexible timeframes and period comparison
- **Metric Management**: Create, update, and organize trackable metrics
- **Goal Tracking**: Set targets, track streaks, monitor completion rates
- **Periodic Reviews**: Weekly/monthly summaries with trend analysis and adjustment suggestions

## Prerequisites

- Supabase MCP server connected to project `ezwdpxbbqmsqqmafqxpw`
- Database schema with:
  - `tracking_categories`
  - `metric_definitions`
  - `daily_entries`
  - `metric_versions`

## Installation

### Option 1: Plugin directory flag
```bash
claude --plugin-dir /path/to/daily-metrics
```

### Option 2: Copy to plugins folder
```bash
cp -r daily-metrics ~/.claude/plugins/
```

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/log` | Log daily entries from freeform text | `/log meditated, slept 7h, weight 74.8kg` |
| `/progress` | Visualize progress with ASCII charts | `/progress weight last 30 days` |
| `/metrics` | Manage metric definitions | `/metrics create`, `/metrics list` |
| `/goals` | Set and track goals | `/goals set meditation`, `/goals streaks` |
| `/review` | Run periodic reviews | `/review week`, `/review month` |

## Usage Examples

### Logging Daily Entries
```
/log Did my morning meditation, read for 45 minutes, skipped exercise.
     Slept about 7.5 hours. Weight at 74.8kg, feeling good - mood 8/10.
```

The plugin will:
1. Parse your freeform text
2. Show a preview table of extracted metrics
3. Ask for confirmation before saving

### Viewing Progress
```
/progress              # Overview dashboard
/progress weight       # Weight trend
/progress sleep last 14 days
/progress this week vs last
```

### Setting Goals
```
/goals set meditation   # Set a goal for meditation (streaks, completion rate)
/goals view            # See all goal progress
/goals streaks         # View current and best streaks
```

### Weekly Reviews
```
/review week           # Analyze last 7 days with insights
/review month          # Monthly summary with trends
```

## Components

### Commands (5)
- `log.md` - Parse and save daily entries
- `progress.md` - Generate ASCII visualizations
- `metrics.md` - CRUD for metric definitions
- `goals.md` - Goal setting and tracking
- `review.md` - Periodic review analysis

### Agent (1)
- `entry-parser` - Parses natural language into structured metrics

### Skills (2)
- `goal-methodology` - SMART goals, habit formation, adjustment strategies
- `ascii-charts` - Patterns for terminal-based data visualization

## Database Schema

The plugin works with this Supabase schema:

```
tracking_categories     # Habits, Health, Sleep, Nutrition, Exercise, Mood
       ↓
metric_definitions      # What you track (name, data_type, unit, goals)
       ↓
daily_entries          # Your actual data (date + value)
       ↓
metric_versions        # Audit trail of definition changes
```

## Author

Maximilian Bruhn
