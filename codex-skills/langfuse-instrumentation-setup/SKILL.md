---
name: langfuse-instrumentation-setup
description: Use when the user needs to instrument code with Langfuse tracing, set up observability, add scoring, or debug Langfuse SDK configuration in a Python pipeline.
---

# Langfuse Instrumentation Setup

Guide users through correct Langfuse tracing and scoring patterns.

## Workflow

1. Validate environment (SDK + keys).
2. Locate the pipeline entry point and LLM/tool calls.
3. Read the tracing model and anti-patterns references.
4. Classify the pipeline type (simple, RAG, agentic, multi-model).
5. Adapt the closest template from assets.
6. Add scoring only if requested.
7. Test with a trace run.

## Step 1: Validate Environment

```bash
python3 ~/.codex/skills/langfuse-instrumentation-setup/scripts/setup_validator.py check
```

If missing:
- Install SDK: `pip install langfuse`
- Set `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, optional `LANGFUSE_HOST`

## Step 2: Explore the Pipeline

Ask for the entry file or function, then inspect:
- LLM calls and clients
- Tool/API calls
- Multi-step flow and conditional logic
- Existing Langfuse code

Use `rg` and `ls` to locate the code before recommending changes.

## Step 3: Read References

- `references/tracing-model.md`
- `references/anti-patterns.md`

If needed:
- `references/llm-instrumentation.md`
- `references/tool-instrumentation.md`
- `references/agent-instrumentation.md`
- `references/decorator-vs-manual.md`

## Step 4: Choose Template

Use the closest template and adapt it:
- `assets/basic-pipeline.py`
- `assets/rag-pipeline.py`
- `assets/agentic-pipeline.py`
- `assets/multi-model-pipeline.py`

For scoring examples:
- `assets/scoring-module.py`

## Step 5: Verify

```bash
python3 ~/.codex/skills/langfuse-instrumentation-setup/scripts/setup_validator.py test-trace
```

## Key Rules

- One trace per logical request.
- Use `generation` for LLM calls, `tool` for tool calls, `span` for local work.
- Always call `langfuse.flush()` in short-lived processes.
