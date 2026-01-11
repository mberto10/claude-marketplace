---
name: langfuse-annotation-manager
description: Use when the user wants to add or update human scores on traces, manage annotation workflows, list scores, find traces pending review, or export annotations from Langfuse.
---

# Langfuse Annotation Manager

Create and manage human annotations and manual scores on traces.

## Quick Start

```bash
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  pending --score-name "human_review" --days 7 --limit 10
```

## Common Tasks

### Create Score

```bash
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score --trace-id <trace-id> --name "quality" --value 8.5 \
  --comment "Good response, minor issues"
```

### Update Score

```bash
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  update-score --score-id <score-id> --value 9.0
```

### Export Scores

```bash
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  export --score-name "quality" --days 30 --format csv --output annotations.csv
```

### List Score Configs

```bash
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py configs
```

## Reference

- `references/annotation-workflows.md` for review workflows and patterns.

## Environment

```bash
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```
