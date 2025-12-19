---
name: langfuse-score-analytics
description: This skill should be used when the user asks to "analyze scores", "show score trends", "detect score regressions", "compare scores across releases", "get score statistics", or needs to understand score distributions and quality metrics over time.
---

# Langfuse Score Analytics

Analyze score trends, detect regressions, and understand score distributions across your Langfuse project.

## When to Use

- Analyzing score statistics (mean, min, max, percentiles)
- Tracking score trends over time
- Comparing scores across releases, environments, or trace names
- Detecting quality regressions between time periods
- Understanding score value distributions

## Operations

### Score Summary

Get aggregate statistics for a score:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  summary --score-name "accuracy" --days 30
```

Returns: count, mean, min, max, p50, p95

### Score Trend

Show score values over time with configurable granularity:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  trend --score-name "accuracy" --days 14 --granularity day
```

Granularity options: `hour`, `day`, `week`, `month`

### Compare by Dimension

Compare scores across different dimensions:

```bash
# Compare across releases
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  compare --score-name "accuracy" --dimension release --days 7

# Compare across environments
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  compare --score-name "accuracy" --dimension environment --days 7

# Compare across trace names
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  compare --score-name "accuracy" --dimension name --days 7
```

### Regression Detection

Compare scores between two time periods to detect regressions:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  regression \
  --score-name "accuracy" \
  --baseline-days 14 \
  --current-days 7
```

Compares the last N days (current) against the previous N days (baseline).

### Score Distribution

Show the distribution of score values:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  distribution --score-name "accuracy" --days 30 --bins 10
```

### List Available Scores

See all score names in your project:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  list-scores --days 30
```

## Examples

### Example 1: Weekly Quality Report

```bash
# Get summary of key scores
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  summary --score-name "quality" --days 7

# Check for regressions
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  regression --score-name "quality" --baseline-days 14 --current-days 7
```

### Example 2: Release Comparison

```bash
# Compare accuracy across releases
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  compare --score-name "accuracy" --dimension release --days 30
```

### Example 3: Trend Analysis

```bash
# Daily trend for the past 2 weeks
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  trend --score-name "helpfulness" --days 14 --granularity day

# Hourly trend for the past day
python3 ${CLAUDE_PLUGIN_ROOT}/skills/score-analytics/helpers/score_analyzer.py \
  trend --score-name "latency" --days 1 --granularity hour
```

## Required Environment Variables

```bash
LANGFUSE_PUBLIC_KEY=pk-...    # Required
LANGFUSE_SECRET_KEY=sk-...    # Required
LANGFUSE_HOST=https://cloud.langfuse.com  # Optional
```

## Troubleshooting

**No data returned:**
- Verify scores exist with the given name using `list-scores`
- Check that the time range contains data
- Confirm environment variables are set correctly

**Unexpected values:**
- Scores are aggregated server-side; outliers can affect means
- Use distribution to understand value spread
- Consider filtering by dimension for more specific analysis

**Regression not detected:**
- Ensure baseline and current periods don't overlap
- Check that both periods have sufficient data
- Consider statistical significance of the change
