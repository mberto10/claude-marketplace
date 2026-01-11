---
name: langfuse-trace-analysis
description: Use when the user says "analyze trace", "debug workflow", "why did this fail", "output is wrong", "missing data", "slow run", or needs root-cause analysis that ties Langfuse traces to code and fixes.
---

# Langfuse Trace Analysis

Perform structured root-cause analysis by combining trace evidence with codebase investigation.

## Workflow

1. Retrieve the trace using the data-retrieval skill.
2. Classify the symptom (data gap, output error, execution error, latency, quality issue, cost).
3. Inspect observations and compare inputs vs outputs at the failing step.
4. Trace the relevant code or prompt responsible for the step.
5. Produce a concise report with evidence and fixes.

## Trace Retrieval (Use Data Retrieval Skill)

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --trace-id <trace-id> --mode io
```

For latency issues:

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --trace-id <trace-id> --mode flow
```

For prompt quality issues:

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --trace-id <trace-id> --mode prompts
```

## Report Generator

Use the report generator for consistent output:

```bash
python3 ~/.codex/skills/langfuse-trace-analysis/scripts/report_generator.py \
  --symptom "output missing expected data" \
  --category data_gap \
  --trace-id <trace-id> \
  --root-cause "Upstream tool not called" \
  --evidence "Observation X shows no API call" \
  --fix "Ensure tool call is wired in pipeline"
```

## Reference

- `references/common-patterns.md` for symptom patterns and investigation heuristics.
