---
name: langfuse-session-analysis
description: This skill should be used when the user asks to "analyze sessions", "debug multi-turn conversation", "find session issues", "list user sessions", "compare sessions", or needs to understand conversation flows and session-level metrics.
---

# Langfuse Session Analysis

Analyze multi-trace user sessions, debug conversation flows, and understand session-level metrics.

## When to Use

- Listing recent sessions with summary statistics
- Getting detailed session breakdowns with all traces
- Analyzing session quality metrics (turn count, duration, scores)
- Finding problematic sessions with errors or low scores
- Debugging multi-turn conversation flows

## Concepts

**Sessions** in Langfuse are implicit groupings of traces that share a `session_id`. They represent multi-turn conversations or user journeys.

**Session metrics** are aggregated from constituent traces:
- Turn count = number of traces
- Duration = time from first to last trace
- Tokens/Cost = sum across all traces
- Scores = averaged across traces

## Operations

### List Sessions

List recent sessions with summary statistics:

```bash
# List recent sessions
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  list --limit 20

# Filter by user
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  list --user-id "user-456" --limit 10
```

### Get Session Details

Get full session details with all traces:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  get --session-id "session-123"
```

### Analyze Session

Deep analysis of session quality:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  analyze --session-id "session-123"
```

Returns:
- Turn count and duration
- Token usage and cost
- Score aggregations
- Error detection
- Timeline of events

### Find Problematic Sessions

Find sessions with issues:

```bash
# Sessions with errors
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  find-issues --days 7 --has-errors

# Sessions with low scores
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  find-issues --days 7 --min-score 0.5 --score-name "quality"

# Long sessions (many turns)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  find-issues --days 7 --min-turns 10
```

### Session Timeline

Get a formatted timeline of events in a session:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  timeline --session-id "session-123"
```

## Examples

### Example 1: Debug a User Complaint

```bash
# Find user's recent sessions
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  list --user-id "user-456" --limit 5

# Analyze the session in question
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  analyze --session-id "session-abc"

# View the conversation timeline
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  timeline --session-id "session-abc"
```

### Example 2: Find Quality Issues

```bash
# Find sessions with low quality scores
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  find-issues --days 3 --score-name "quality" --min-score 0.6

# Find sessions with errors
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  find-issues --days 7 --has-errors
```

### Example 3: Usage Patterns

```bash
# Find unusually long sessions
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  find-issues --days 7 --min-turns 15

# Review session details
python3 ${CLAUDE_PLUGIN_ROOT}/skills/session-analysis/helpers/session_analyzer.py \
  get --session-id "long-session-id"
```

## Required Environment Variables

```bash
LANGFUSE_PUBLIC_KEY=pk-...    # Required
LANGFUSE_SECRET_KEY=sk-...    # Required
LANGFUSE_HOST=https://cloud.langfuse.com  # Optional
```

## Troubleshooting

**No sessions found:**
- Verify traces have `session_id` set when created
- Check the time range covers when sessions occurred
- Confirm environment variables are correct

**Session appears incomplete:**
- Traces may still be processing
- Some traces might have failed to log
- Check trace-level details for errors

**Metrics seem off:**
- Token/cost data requires instrumentation
- Scores are averaged across all traces in session
- Duration only counts time between first and last trace
