---
name: langfuse-dataset-management
description: Use when the user asks to create Langfuse datasets, add traces to datasets, curate regression or golden sets, list datasets, or inspect dataset items.
---

# Langfuse Dataset Management

Create and manage datasets that power experiments and regression tests.

## Quick Start

```bash
python3 ~/.codex/skills/langfuse-dataset-management/scripts/dataset_manager.py list
```

## Common Tasks

### Create Dataset

```bash
python3 ~/.codex/skills/langfuse-dataset-management/scripts/dataset_manager.py \
  create --name "checkout_regressions" --description "Failing traces for checkout"
```

### Add Single Trace

```bash
python3 ~/.codex/skills/langfuse-dataset-management/scripts/dataset_manager.py \
  add-trace --dataset "checkout_regressions" --trace-id <trace-id> --expected-score 9.0
```

### Add Batch

```bash
echo "trace_id_1\ntrace_id_2" > failing_traces.txt
python3 ~/.codex/skills/langfuse-dataset-management/scripts/dataset_manager.py \
  add-batch --dataset "checkout_regressions" --trace-file failing_traces.txt --expected-score 9.0
```

### Get Dataset Items

```bash
python3 ~/.codex/skills/langfuse-dataset-management/scripts/dataset_manager.py \
  get --name "checkout_regressions"
```

## Naming Guidance

Use `{project}_{purpose}` or `{workflow}_{purpose}` (e.g., `api_v2_golden_set`).

## Environment

```bash
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```
