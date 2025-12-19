---
name: Langfuse Instrumentation Setup
description: Use this skill when users want to add Langfuse tracing to their code, set up observability, instrument LLM calls, or add scoring to their pipelines. Helps users correctly structure traces, spans, and generations.
version: 1.0.0
---

# Langfuse Instrumentation Setup

This skill helps you correctly instrument Python code with Langfuse tracing. It addresses common misunderstandings about the tracing model and provides best-practice patterns.

## When to Use This Skill

Activate this skill when users ask to:
- "Set up Langfuse tracing"
- "Instrument my code with Langfuse"
- "Add observability to my pipeline"
- "Trace my LLM calls"
- "Add scoring to my traces"
- "Debug my Langfuse setup"

## Interactive Workflow

Follow these steps in order. **Do not skip the exploration phase** - understanding the user's actual code is critical.

---

### Step 1: Validate Environment

First, check if the user's environment is properly configured.

**Run the setup validator:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/helpers/setup_validator.py check
```

**If setup is incomplete:**
1. Langfuse SDK not installed → Suggest: `pip install langfuse`
2. Missing API keys → Ask user for their Langfuse project keys
3. Wrong host → Check if they're using self-hosted Langfuse

**Once environment is ready, proceed to Step 2.**

---

### Step 2: Explore the User's Pipeline

**This is the most important step.** You must understand the user's code structure before recommending instrumentation.

**Ask the user:**
> "Where is your main pipeline or agent code? Point me to the entry file or function."

**Then read the relevant files and identify:**

1. **Entry point**: Where does a request come in?
2. **LLM calls**: What client are they using? (OpenAI, Anthropic, etc.)
3. **Tool/API calls**: Any external services, databases, or tools?
4. **Multi-step logic**: Loops, chains, conditional flows?
5. **Existing instrumentation**: Any Langfuse code already present?

**Document what you find before proceeding.**

---

### Step 3: Read Core References

**Always read the tracing model reference first:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/references/tracing-model.md
```

**Then read the anti-patterns reference:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/references/anti-patterns.md
```

These establish the foundation for correct instrumentation.

---

### Step 4: Classify Pipeline Type

Based on your exploration, classify the pipeline:

| Type | Characteristics | Template |
|------|-----------------|----------|
| **Simple** | Single LLM call, minimal preprocessing | `basic-pipeline.py` |
| **RAG** | Embedding + retrieval + generation | `rag-pipeline.py` |
| **Agentic** | LLM with tool loop, autonomous decisions | `agentic-pipeline.py` |
| **Multi-model** | Chain of LLM calls (summarize→translate) | `multi-model-pipeline.py` |
| **Hybrid** | Combination of patterns | Combine templates |

---

### Step 5: Read Relevant References

Based on the pipeline type, read additional references:

**For pipelines with LLM calls (all types):**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/references/llm-instrumentation.md
```

**For pipelines with tool calls:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/references/tool-instrumentation.md
```

**For agent workflows:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/references/agent-instrumentation.md
```

**If user asks about decorators vs context managers:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/references/decorator-vs-manual.md
```

---

### Step 6: Select and Adapt Template

Read the most appropriate template:

**Simple pipeline:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/templates/basic-pipeline.py
```

**RAG pipeline:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/templates/rag-pipeline.py
```

**Agentic pipeline:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/templates/agentic-pipeline.py
```

**Multi-model pipeline:**
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/templates/multi-model-pipeline.py
```

---

### Step 7: Generate Custom Instrumentation

Now adapt the template to the user's specific code:

1. **Map their functions to observation types:**
   - LLM call functions → `generation`
   - Tool/API functions → `tool`
   - Preprocessing/postprocessing → `span`
   - Important events → `event`

2. **Show exactly where to add instrumentation:**
   - Point to specific lines in their code
   - Provide before/after examples
   - Highlight what should be captured (input, output, metadata)

3. **Remind them of anti-patterns to avoid:**
   - One trace per logical request (not per function)
   - Always use `as_type="generation"` for LLM calls
   - Don't forget to flush in short-lived processes

---

### Step 8: Optional - Add Scoring

**Only if the user requests automated scoring**, read the scoring module:
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/templates/scoring-module.py
```

**Scoring options:**
- **Automatic metrics**: Latency, token count, cost
- **LLM-as-judge**: Quality, safety, relevance evaluation
- **Categorical scores**: Intent classification
- **Boolean scores**: PII detection, other checks

---

### Step 9: Verify Setup

After instrumentation is added, suggest testing:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/helpers/setup_validator.py test-trace
```

Or have them run their instrumented code and check the Langfuse dashboard.

---

## Key Principles

### One Trace Per Request

The most common mistake is creating multiple traces when there should be one. A trace represents **one logical unit of work**:
- One user request
- One pipeline execution
- One agent task

Everything else goes **inside** the trace as observations.

### Observation Type Selection

| Type | Use For | Example |
|------|---------|---------|
| `generation` | LLM API calls | OpenAI completion, Anthropic message |
| `span` | Non-LLM work | Preprocessing, validation |
| `tool` | Tool executions | API calls, database queries |
| `event` | Point-in-time | Errors, important state changes |

### Context Propagation

When using context managers, observations automatically nest correctly:

```python
with langfuse.start_as_current_observation(name="pipeline") as trace:
    with langfuse.start_as_current_observation(as_type="generation") as gen:
        # gen is automatically a child of trace
        pass
```

### Required Data for Generations

Always capture for LLM calls:
- `model`: Which model was used
- `input`: The messages/prompt sent
- `output`: The response received
- `usage_details`: Token counts (input/output)

---

## Quick Reference Commands

**Check environment:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/helpers/setup_validator.py check
```

**Test connection:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/instrumentation-setup/helpers/setup_validator.py test-trace
```

---

## Template Summary

| Template | Pattern | Best For |
|----------|---------|----------|
| `basic-pipeline.py` | Input → LLM → Output | Simple chatbots, Q&A |
| `rag-pipeline.py` | Query → Retrieve → Generate | Document Q&A, search |
| `agentic-pipeline.py` | Think → Act → Observe loop | Tool-using agents |
| `multi-model-pipeline.py` | LLM1 → LLM2 → ... | Translation, refinement |
| `scoring-module.py` | Add scores to traces | Quality monitoring |

---

## Reference Summary

| Reference | Content |
|-----------|---------|
| `tracing-model.md` | Core concepts: trace vs span vs generation |
| `llm-instrumentation.md` | How to trace LLM calls correctly |
| `tool-instrumentation.md` | How to trace tool/API calls |
| `agent-instrumentation.md` | Multi-step agent patterns |
| `decorator-vs-manual.md` | When to use each approach |
| `anti-patterns.md` | Common mistakes and how to avoid |
