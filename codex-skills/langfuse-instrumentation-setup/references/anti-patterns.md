# Anti-Patterns to Avoid

Common mistakes when instrumenting with Langfuse and how to fix them.

---

## 1. Creating Multiple Traces for One Request

### The Problem

```python
# WRONG: Creates 3 separate traces
def process_request(input):
    trace1 = langfuse.trace(name="step1")
    preprocess(input)
    trace1.end()

    trace2 = langfuse.trace(name="step2")
    result = call_llm(input)
    trace2.end()

    trace3 = langfuse.trace(name="step3")
    postprocess(result)
    trace3.end()
```

### The Fix

```python
# CORRECT: One trace with nested observations
def process_request(input):
    with langfuse.start_as_current_observation(name="process-request", input=input) as trace:

        with langfuse.start_as_current_observation(name="preprocess", as_type="span"):
            preprocess(input)

        with langfuse.start_as_current_observation(name="llm-call", as_type="generation"):
            result = call_llm(input)

        with langfuse.start_as_current_observation(name="postprocess", as_type="span"):
            postprocess(result)

        trace.update(output=result)
```

**Rule:** One trace = one user request/pipeline execution.

---

## 2. Not Using as_type="generation" for LLM Calls

### The Problem

```python
# WRONG: LLM call traced as generic span
with langfuse.start_as_current_observation(name="llm-call") as span:
    response = openai.chat.completions.create(...)
    span.update(output=response)
```

### The Fix

```python
# CORRECT: LLM call traced as generation with model info
with langfuse.start_as_current_observation(
    as_type="generation",
    name="llm-call",
    model="gpt-4o",
    input=messages
) as generation:
    response = openai.chat.completions.create(...)
    generation.update(
        output=response.choices[0].message.content,
        usage_details={
            "input": response.usage.prompt_tokens,
            "output": response.usage.completion_tokens
        }
    )
```

**Rule:** Always use `as_type="generation"` for LLM calls to enable model tracking and cost analysis.

---

## 3. Forgetting to Flush in Short-Lived Processes

### The Problem

```python
# WRONG: Script ends before data is sent
def lambda_handler(event, context):
    with langfuse.start_as_current_observation(name="handler") as trace:
        result = process(event)
        trace.update(output=result)

    return result  # Data might be lost!
```

### The Fix

```python
# CORRECT: Flush before exiting
def lambda_handler(event, context):
    with langfuse.start_as_current_observation(name="handler") as trace:
        result = process(event)
        trace.update(output=result)

    langfuse.flush()  # Ensure data is sent
    return result
```

**Rule:** Always call `langfuse.flush()` in scripts, serverless functions, or any short-lived process.

---

## 4. Incorrect Nesting (Sibling LLM Calls Appear Nested)

### The Problem

```python
# WRONG: Second LLM call appears nested under first
def process():
    gen1 = langfuse.start_observation(as_type="generation", name="llm-1")
    result1 = call_llm_1()
    # Forgot to end gen1!

    gen2 = langfuse.start_observation(as_type="generation", name="llm-2")
    result2 = call_llm_2()
    gen2.end()

    gen1.end()  # Too late - gen2 is already nested under gen1
```

### The Fix

```python
# CORRECT: Use context managers for proper lifecycle
def process():
    with langfuse.start_as_current_observation(as_type="generation", name="llm-1"):
        result1 = call_llm_1()

    with langfuse.start_as_current_observation(as_type="generation", name="llm-2"):
        result2 = call_llm_2()
```

**Rule:** Use context managers for automatic lifecycle management, or be careful to end observations in the correct order.

---

## 5. Missing Input/Output on Observations

### The Problem

```python
# WRONG: No input or output captured
with langfuse.start_as_current_observation(name="process-data"):
    result = process(data)
```

### The Fix

```python
# CORRECT: Capture input and output
with langfuse.start_as_current_observation(
    name="process-data",
    input=data
) as span:
    result = process(data)
    span.update(output=result)
```

**Rule:** Always capture input and output for debugging and analysis.

---

## 6. Not Propagating Context in Async Code

### The Problem

```python
# WRONG: Context lost in async/thread
async def main():
    with langfuse.start_as_current_observation(name="main"):
        await asyncio.gather(
            task1(),  # Context might be lost
            task2()   # Context might be lost
        )

async def task1():
    # This might create a new trace instead of nesting
    with langfuse.start_as_current_observation(name="task1"):
        ...
```

### The Fix

```python
# CORRECT: Context is preserved with proper async handling
# The Langfuse SDK handles this in most cases with contextvars,
# but be careful with ThreadPoolExecutor and ProcessPoolExecutor

async def main():
    with langfuse.start_as_current_observation(name="main"):
        # asyncio.gather preserves context
        await asyncio.gather(
            task1(),
            task2()
        )
```

For thread pools, pass the observation explicitly:

```python
def run_in_thread(parent_observation_id):
    with langfuse.start_as_current_observation(
        name="thread-task",
        parent_observation_id=parent_observation_id  # Explicit parent
    ):
        ...
```

**Rule:** Be aware of context propagation in concurrent code. Use explicit parent IDs when needed.

---

## 7. Hardcoding Trace IDs

### The Problem

```python
# WRONG: Hardcoded trace ID
langfuse.trace(id="my-trace-id", name="handler")
# Later, another request uses the same ID
langfuse.trace(id="my-trace-id", name="handler")  # Conflict!
```

### The Fix

```python
# CORRECT: Let Langfuse generate IDs, or use unique IDs
langfuse.trace(name="handler")  # Auto-generated ID

# Or use request-specific ID
langfuse.trace(id=f"request-{request_id}", name="handler")
```

**Rule:** Let Langfuse auto-generate trace IDs, or ensure IDs are unique per request.

---

## 8. Tracing Too Much Detail

### The Problem

```python
# WRONG: Every tiny operation gets a span
def process(data):
    with langfuse.start_as_current_observation(name="check-null"):
        if data is None:
            return None

    with langfuse.start_as_current_observation(name="convert-type"):
        data = str(data)

    with langfuse.start_as_current_observation(name="strip-whitespace"):
        data = data.strip()

    # ... 20 more spans for trivial operations
```

### The Fix

```python
# CORRECT: Trace meaningful operations only
def process(data):
    with langfuse.start_as_current_observation(name="preprocess", input=data) as span:
        if data is None:
            span.update(output=None)
            return None
        result = str(data).strip()
        span.update(output=result)
        return result
```

**Rule:** Trace business-meaningful operations, not every line of code.

---

## 9. Not Setting User and Session IDs

### The Problem

```python
# WRONG: No user or session context
with langfuse.start_as_current_observation(name="chat"):
    response = chat(message)
```

### The Fix

```python
# CORRECT: Include user and session for analytics
with langfuse.start_as_current_observation(
    name="chat",
    user_id=user_id,
    session_id=conversation_id,
    input=message
) as trace:
    response = chat(message)
    trace.update(output=response)
```

**Rule:** Always set `user_id` and `session_id` when available for user-level analytics.

---

## 10. Swallowing Errors

### The Problem

```python
# WRONG: Error not recorded in trace
with langfuse.start_as_current_observation(name="risky-op"):
    try:
        result = risky_operation()
    except Exception:
        result = None  # Error silently ignored
```

### The Fix

```python
# CORRECT: Record errors in the trace
with langfuse.start_as_current_observation(name="risky-op") as span:
    try:
        result = risky_operation()
        span.update(output=result)
    except Exception as e:
        span.update(
            level="ERROR",
            status_message=str(e)
        )
        raise  # Or handle appropriately
```

**Rule:** Always record errors in traces for debugging.

---

## Quick Reference

| Anti-Pattern | Fix |
|--------------|-----|
| Multiple traces per request | One trace with nested observations |
| Missing as_type="generation" | Always use for LLM calls |
| Forgot to flush | Call `langfuse.flush()` in short-lived processes |
| Incorrect nesting | Use context managers |
| Missing input/output | Always capture both |
| Lost async context | Use explicit parent IDs when needed |
| Hardcoded trace IDs | Let Langfuse auto-generate |
| Over-tracing | Focus on meaningful operations |
| Missing user/session | Always set when available |
| Swallowing errors | Record errors in traces |
