# Langfuse Tracing Model

This is the authoritative reference for understanding how Langfuse structures observability data.

## Core Principle

**One trace per logical request or pipeline execution.**

A trace represents a single user request, API call, or pipeline run from start to finish. Everything that happens during that request (LLM calls, tool calls, preprocessing) are observations nested within that trace.

## Hierarchy

```
TRACE (root container)
+-- OBSERVATION (span, generation, event, tool, etc.)
|   +-- OBSERVATION (nested child)
+-- OBSERVATION
+-- OBSERVATION
```

## Data Types

### Trace

The root container for a single request/execution.

**Key Fields:**
- `name` - Identifier for the trace type (e.g., "chat-request", "agent-run")
- `input` - The initial input to the pipeline
- `output` - The final output from the pipeline
- `user_id` - Who made the request
- `session_id` - Groups multiple traces into a conversation
- `metadata` - Arbitrary key-value data
- `tags` - Categorization labels
- `release` - Version/release identifier

**Create with:**
```python
with langfuse.start_as_current_observation(
    name="my-pipeline",
    user_id="user-123",
    session_id="session-456",
    input=user_input
) as trace:
    # Your pipeline code
    trace.update(output=final_output)
```

### Observation Types

All observations can nest within traces or other observations.

#### Generation

**Use for:** LLM calls (OpenAI, Anthropic, etc.)

**Key Fields:**
- `name` - Identifier for this LLM call
- `model` - Model used (e.g., "gpt-4o", "claude-sonnet-4-20250514")
- `input` - Messages/prompt sent to the model
- `output` - Response from the model
- `usage_details` - Token counts (`input`, `output`, `total`)
- `model_parameters` - Temperature, max_tokens, etc.

```python
with langfuse.start_as_current_observation(
    as_type="generation",
    name="main-llm-call",
    model="gpt-4o"
) as gen:
    # Make LLM call
    gen.update(output=response, usage_details={...})
```

#### Span

**Use for:** Non-LLM work (preprocessing, retrieval, postprocessing)

**Key Fields:**
- `name` - Identifier for this step
- `input` - Input to this step
- `output` - Output from this step

```python
with langfuse.start_as_current_observation(
    as_type="span",
    name="preprocessing"
) as span:
    # Do preprocessing
    span.update(output=processed_data)
```

#### Tool

**Use for:** Tool/API calls made by an agent

**Key Fields:**
- `name` - Tool name (e.g., "search-api", "calculator")
- `input` - Tool arguments
- `output` - Tool result

```python
with langfuse.start_as_current_observation(
    as_type="tool",
    name="weather-api",
    input={"location": "Paris"}
) as tool:
    result = weather_service.get(...)
    tool.update(output=result)
```

#### Event

**Use for:** Point-in-time occurrences (no duration)

```python
langfuse.event(name="user-clicked-button", metadata={...})
```

#### Other Types

- `agent` - Agent execution context
- `retriever` - RAG retrieval operations
- `embedding` - Embedding generation
- `evaluator` - Evaluation runs
- `guardrail` - Safety checks

## Visual Mental Model

```
+------------------------------------------------------------------+
| TRACE: chat-request                                              |
|   user_id: "user-123"                                            |
|   session_id: "session-456"                                      |
|   input: "What's the weather in Paris?"                          |
+------------------------------------------------------------------+
|                                                                  |
|  +------------------------------------------------------------+  |
|  | SPAN: input-validation                                     |  |
|  |   input: "What's the weather in Paris?"                    |  |
|  |   output: {valid: true, intent: "weather_query"}           |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|  +------------------------------------------------------------+  |
|  | GENERATION: intent-classification                          |  |
|  |   model: "gpt-4o-mini"                                     |  |
|  |   input: [{role: "user", content: "..."}]                  |  |
|  |   output: "weather_query"                                  |  |
|  |   usage: {input: 45, output: 3}                            |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|  +------------------------------------------------------------+  |
|  | TOOL: weather-api                                          |  |
|  |   input: {location: "Paris", units: "metric"}              |  |
|  |   output: {temp: 18, conditions: "cloudy"}                 |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|  +------------------------------------------------------------+  |
|  | GENERATION: response-generation                            |  |
|  |   model: "gpt-4o"                                          |  |
|  |   input: [{role: "system", ...}, {role: "user", ...}]      |  |
|  |   output: "It's currently 18 deg C and cloudy in Paris."       |  |
|  |   usage: {input: 120, output: 15}                          |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|   output: "It's currently 18 deg C and cloudy in Paris."            |
+------------------------------------------------------------------+
```

## Nesting Rules

1. **Traces are the root** - All observations belong to a trace
2. **Observations can nest** - A span can contain generations, tools can contain nested calls
3. **Context propagation** - Using `start_as_current_observation()` automatically nests children
4. **Explicit parent** - Use `parent_observation_id` if manual nesting is needed

## Session Grouping

Use `session_id` to group related traces (e.g., a multi-turn conversation):

```python
# First turn
with langfuse.start_as_current_observation(
    name="chat", session_id="conv-123", ...
) as trace1:
    ...

# Second turn (same session_id)
with langfuse.start_as_current_observation(
    name="chat", session_id="conv-123", ...
) as trace2:
    ...
```

## Key Takeaways

1. **One trace = one request** - Don't create multiple traces for steps within a single request
2. **Use correct types** - `generation` for LLMs, `span` for logic, `tool` for tools
3. **Capture input/output** - Always set these for debugging
4. **Use context managers** - They handle nesting and lifecycle automatically
5. **Set user_id and session_id** - Essential for analytics
