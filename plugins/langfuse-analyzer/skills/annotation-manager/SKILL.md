---
name: langfuse-annotation-manager
description: This skill should be used when the user asks to "add score to trace", "annotate trace", "create human label", "review traces for annotation", "export annotations", "find traces needing review", or needs to manage human scoring and labeling workflows.
---

# Langfuse Annotation Manager

Manage human annotations and scores on traces. Create, update, and export manual quality labels.

## When to Use

- Adding human scores/labels to traces
- Managing annotation workflows
- Finding traces that need human review
- Exporting annotations for analysis
- Configuring score types

## Score Types

Langfuse supports three score data types:

| Type | Description | Example |
|------|-------------|---------|
| NUMERIC | Float values | 0.0 to 1.0, or 1-10 ratings |
| CATEGORICAL | String values | "good", "bad", "neutral" |
| BOOLEAN | True/false | pass/fail checks |

## Operations

### Create Score

Add a score to a trace:

```bash
# Numeric score (default)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  create-score \
  --trace-id "abc123" \
  --name "quality" \
  --value 8.5 \
  --comment "Good response, minor formatting issues"

# Categorical score
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  create-score \
  --trace-id "abc123" \
  --name "category" \
  --string-value "helpful" \
  --data-type CATEGORICAL

# Boolean score
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  create-score \
  --trace-id "abc123" \
  --name "approved" \
  --value 1 \
  --data-type BOOLEAN
```

### Update Score

Update an existing score:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  update-score \
  --score-id "score-456" \
  --value 9.0 \
  --comment "Updated after additional review"
```

### Delete Score

Remove a score:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  delete-score --score-id "score-456"
```

### List Scores

View scores for a trace or by name:

```bash
# Scores for a specific trace
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  list-scores --trace-id "abc123"

# All scores with a specific name
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  list-scores --name "quality" --limit 50
```

### Find Pending Traces

Find traces that need annotation:

```bash
# Traces missing a specific score
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  pending \
  --score-name "human_review" \
  --days 7 \
  --limit 20

# Filter by trace name
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  pending \
  --score-name "quality" \
  --trace-name "chat-completion" \
  --days 3
```

### Export Annotations

Export scores to JSON or CSV:

```bash
# Export to JSON
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  export \
  --score-name "quality" \
  --days 30 \
  --format json

# Export to CSV
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  export \
  --score-name "quality" \
  --days 30 \
  --format csv \
  --output annotations.csv
```

### List Score Configs

View available score configurations:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  configs
```

## Examples

### Example 1: Human Review Workflow

```bash
# Find traces needing review
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  pending --score-name "human_review" --days 7 --limit 10

# Review a trace (use trace-analysis skill to see details)
# Then add annotation
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  create-score \
  --trace-id "trace-to-review" \
  --name "human_review" \
  --value 8.0 \
  --comment "Response was accurate and helpful"
```

### Example 2: Categorical Labeling

```bash
# Label traces with categories
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  create-score \
  --trace-id "abc123" \
  --name "response_type" \
  --string-value "clarification_needed" \
  --data-type CATEGORICAL

# Export categorical labels
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  export --score-name "response_type" --days 30 --format csv
```

### Example 3: Pass/Fail Annotation

```bash
# Mark as passed
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  create-score \
  --trace-id "abc123" \
  --name "qa_check" \
  --value 1 \
  --data-type BOOLEAN

# Mark as failed with reason
python3 ${CLAUDE_PLUGIN_ROOT}/skills/annotation-manager/helpers/annotation_manager.py \
  create-score \
  --trace-id "def456" \
  --name "qa_check" \
  --value 0 \
  --data-type BOOLEAN \
  --comment "Failed: incorrect date format in response"
```

## Annotation Best Practices

1. **Consistent naming** - Use standardized score names across your project
2. **Clear guidelines** - Document what each score level means
3. **Include comments** - Explain reasoning for edge cases
4. **Regular exports** - Back up annotations periodically
5. **Score configs** - Define score ranges and categories in Langfuse UI

## Required Environment Variables

```bash
LANGFUSE_PUBLIC_KEY=pk-...    # Required
LANGFUSE_SECRET_KEY=sk-...    # Required
LANGFUSE_HOST=https://cloud.langfuse.com  # Optional
```

## Troubleshooting

**Score not created:**
- Verify trace ID exists
- Check that score name is valid
- Ensure value type matches data type

**Can't find pending traces:**
- Confirm traces exist in the time range
- Check that score name is spelled correctly
- Some traces may already have the score

**Export missing data:**
- Scores may not have comments
- Check date range covers the annotation period
- Verify score name matches exactly
