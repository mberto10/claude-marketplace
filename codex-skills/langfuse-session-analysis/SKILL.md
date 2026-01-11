---
name: langfuse-session-analysis
description: Use when the user needs session-level analysis in Langfuse, wants to list or inspect sessions, debug multi-turn conversations, or identify sessions with errors or low scores.
---

# Langfuse Session Analysis

Analyze multi-trace sessions grouped by `session_id`.

## Quick Start

```bash
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py list --limit 20
```

## Common Tasks

### Get Session Details

```bash
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  get --session-id <session-id>
```

### Analyze Session Quality

```bash
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  analyze --session-id <session-id>
```

### Find Problem Sessions

```bash
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  find-issues --days 7 --has-errors

python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  find-issues --days 7 --score-name quality --min-score 0.6
```

### Timeline View

```bash
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  timeline --session-id <session-id>
```

## Environment

```bash
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```
