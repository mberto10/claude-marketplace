---
description: Log daily entries from freeform text with preview
argument-hint: [freeform notes about your day]
allowed-tools: mcp__supabase__execute_sql, mcp__supabase__apply_migration, AskUserQuestion
---

Parse the user's freeform daily notes and extract trackable metrics.

## Input
User's notes: $ARGUMENTS

## Process

1. **Query available metrics** from the database:
   ```sql
   SELECT m.id, m.name, m.data_type, m.unit, c.name as category
   FROM metric_definitions m
   JOIN tracking_categories c ON m.category_id = c.id
   WHERE m.is_active = true
   ORDER BY c.sort_order, m.sort_order
   ```

2. **Parse the freeform text** to identify:
   - Boolean completions (habits done/not done)
   - Numeric values with units (weight, hours slept, calories)
   - Mood/ratings on scales
   - Any other trackable data

3. **Show preview table** in this format:
   ```
   ┌─────────────────────────────────────────────────────┐
   │ Daily Entry Preview - [DATE]                        │
   ├──────────────────┬──────────────┬──────────────────┤
   │ Metric           │ Value        │ Category         │
   ├──────────────────┼──────────────┼──────────────────┤
   │ Morning meditation│ ✓ Done      │ Habits           │
   │ Weight           │ 75.5 kg      │ Health           │
   │ Sleep duration   │ 7.5 hours    │ Sleep            │
   └──────────────────┴──────────────┴──────────────────┘
   ```

4. **Ask for confirmation** using AskUserQuestion:
   - "Does this look correct? Save these entries?"
   - Options: "Save all", "Edit first", "Cancel"

5. **If confirmed**, insert entries:
   ```sql
   INSERT INTO daily_entries (metric_id, date, boolean_value, numeric_value, text_value, json_value, notes)
   VALUES (...)
   ON CONFLICT (metric_id, date) DO UPDATE SET ...
   ```

6. **Report success** with count of entries saved.

## Notes Parsing Guidelines

- "meditated" / "meditation done" / "✓ meditation" → boolean_value: true
- "skipped workout" / "no exercise" / "didn't run" → boolean_value: false
- "75.5 kg" / "weight 75.5" → numeric_value: 75.5 (Health/Weight)
- "slept 7 hours" / "7h sleep" → numeric_value: 7 (Sleep/duration)
- "2100 calories" / "ate 2100 kcal" → numeric_value: 2100 (Nutrition/Calories)
- "mood 8/10" / "feeling 8" → numeric_value: 8 (Mood rating)

If a metric mentioned doesn't exist yet, note it and ask if user wants to create it.
