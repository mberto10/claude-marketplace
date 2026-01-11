---
name: langfuse-data-retrieval
description: Use when the user asks to fetch Langfuse traces, list recent runs, inspect a trace ID, debug workflow inputs or outputs, filter by tags or metadata, or needs compact trace summaries for analysis.
---

# Langfuse Data Retrieval

Fetch Langfuse traces with focused output modes so the analysis stays readable.

## Quick Start

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py --last 1
```

## Common Tasks

### Retrieve a Specific Trace

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --trace-id <trace-id> --mode io
```

### List Recent Traces

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py --last 5 --mode minimal
```

### Filter by Metadata or Tags

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --last 10 --filter-field project_id --filter-value myproject --mode io

python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --last 10 --tags production api-v2 --mode minimal
```

### Filter by Score (Client-side)

```bash
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --last 20 --max-score 7.0 --score-name quality_score --mode minimal
```

## Output Modes

- `io` (default): node inputs/outputs and tool calls
- `minimal`: trace ID, name, timestamp, status
- `prompts`: LLM prompts and responses only
- `flow`: node order and timing
- `full`: all fields, costs, tokens, metadata

## Environment

```bash
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```

## Notes

- Use `io` for most debugging tasks.
- Use `flow` for latency investigations.
- Use `prompts` for prompt quality checks.
