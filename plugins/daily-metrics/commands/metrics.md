---
description: Manage metric definitions (create, update, list, deactivate)
argument-hint: [create|update|list|deactivate] [metric-name]
allowed-tools: mcp__supabase__execute_sql, mcp__supabase__apply_migration, AskUserQuestion
---

Manage metric definitions in the tracking system.

## Input
Action: $1 (create, update, list, deactivate)
Metric name: $2

## Actions

### LIST (default if no action specified)
Query and display all metrics organized by category:

```sql
SELECT
  c.name as category, c.icon,
  m.name, m.description, m.data_type, m.unit, m.is_active,
  (SELECT COUNT(*) FROM daily_entries WHERE metric_id = m.id) as entry_count
FROM metric_definitions m
JOIN tracking_categories c ON m.category_id = c.id
ORDER BY c.sort_order, m.sort_order
```

Display format:
```
Tracking Metrics
══════════════════════════════════════

✓ HABITS (4 metrics)
────────────────────────────────────────
  ● Morning meditation     boolean     52 entries
  ● Evening reading        boolean     48 entries
  ● Exercise               boolean     31 entries
  ○ Journaling            boolean     0 entries (inactive)

❤️ HEALTH (2 metrics)
────────────────────────────────────────
  ● Weight                 number (kg) 45 entries
  ● Blood pressure         json        12 entries

😴 SLEEP (2 metrics)
────────────────────────────────────────
  ● Sleep duration         number (h)  52 entries
  ● Sleep quality          number (1-10) 52 entries
```

### CREATE
Guide through creating a new metric:

1. Ask for category (show available options from tracking_categories)
2. Ask for metric name
3. Ask for data type:
   - boolean: habits (done/not done)
   - number: measurements with unit
   - duration: time-based (hours, minutes)
   - text: freeform notes
   - json: complex structured data
4. If number/duration, ask for unit
5. Optional: validation rules (min, max)
6. Optional: description

Insert:
```sql
INSERT INTO metric_definitions (category_id, name, description, data_type, unit, validation_rules, sort_order)
VALUES (
  (SELECT id FROM tracking_categories WHERE name = $category),
  $name,
  $description,
  $data_type,
  $unit,
  $validation_rules,
  (SELECT COALESCE(MAX(sort_order), 0) + 1 FROM metric_definitions WHERE category_id = $category_id)
)
RETURNING id, name;
```

The auto-versioning trigger will log this creation.

### UPDATE
Update an existing metric definition:

1. Query current metric state
2. Ask what to update:
   - Name
   - Description
   - Unit
   - Validation rules
   - Sort order
3. Show preview of changes
4. Confirm before updating

```sql
UPDATE metric_definitions
SET name = $new_name, description = $new_desc, ...
WHERE id = $metric_id;
```

The auto-versioning trigger will log this update.

### DEACTIVATE
Soft-delete a metric (preserves historical data):

1. Query metric and show entry count
2. Warn: "This metric has X entries. Deactivating will hide it but preserve data."
3. Confirm with AskUserQuestion
4. Set is_active = false

```sql
UPDATE metric_definitions
SET is_active = false
WHERE id = $metric_id;
```

To reactivate, use: `/metrics update [name]` and set is_active = true

## Categories Reference
Available categories for new metrics:
- Habits (boolean tracking)
- Health (measurements)
- Sleep (duration/quality)
- Nutrition (food/hydration)
- Exercise (workouts)
- Mood (emotional state)

To add new categories, use direct SQL via Supabase.
