---
name: langfuse-score-analytics
description: Use when the user asks to analyze score trends, regressions, distributions, or compare quality metrics across releases, environments, or trace names in Langfuse.
---

# Langfuse Score Analytics

Summarize and compare score metrics over time.

## Quick Start

```bash
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  summary --score-name "quality" --days 7
```

## Common Tasks

### Trend

```bash
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  trend --score-name "accuracy" --days 14 --granularity day
```

### Regression

```bash
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  regression --score-name "quality" --baseline-days 14 --current-days 7
```

### Compare by Dimension

```bash
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  compare --score-name "accuracy" --dimension release --days 30
```

### Distribution

```bash
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  distribution --score-name "helpfulness" --days 30 --bins 10
```

### List Scores

```bash
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  list-scores --days 30
```

## Environment

```bash
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```
