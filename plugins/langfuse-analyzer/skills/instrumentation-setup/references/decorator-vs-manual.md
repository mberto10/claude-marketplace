# Decorator vs Manual Tracing

When to use each approach for Langfuse instrumentation.

## Overview

Langfuse provides three ways to create observations:

| Approach | Syntax | Best For |
|----------|--------|----------|
| **@observe decorator** | `@observe()` | Simple functions, automatic capture |
| **Context manager** | `with langfuse.start_as_current_observation()` | Fine-grained control, streaming |
| **Manual** | `langfuse.start_observation()` | Parallel work, custom lifecycle |

## @observe Decorator

### When to Use

- Simple function-based code
- When automatic input/output capture is sufficient
- Clean function call hierarchies
- Quick instrumentation with minimal code changes

### Syntax

```python
from langfuse.decorators import observe, langfuse_context

@observe()
def my_function(arg1, arg2):
    return result

@observe(as_type="generation")
def call_llm(messages):
    return llm.generate(messages)

@observe(as_type="tool", name="custom-name")
def call_api(params):
    return api.call(params)
```

### Automatic Capture

The decorator automatically captures:
- Function arguments → `input`
- Return value → `output`
- Execution time
- Exceptions

### Updating Within Decorated Function

Use `langfuse_context` to update the current observation:

```python
from langfuse.decorators import observe, langfuse_context

@observe(as_type="generation")
def call_llm(messages):
    response = client.chat.completions.create(...)

    # Update the current observation
    langfuse_context.update_current_observation(
        model="gpt-4o",
        usage_details={
            "input": response.usage.prompt_tokens,
            "output": response.usage.completion_tokens
        }
    )

    return response.choices[0].message.content
```

### Nesting

Decorated functions automatically nest:

```python
@observe()
def main():
    step1()  # Child of main
    step2()  # Child of main

@observe()
def step1():
    substep()  # Child of step1

@observe()
def substep():
    pass

@observe()
def step2():
    pass
```

### Limitations

- Less control over observation lifecycle
- Can't easily capture partial updates during streaming
- Return value capture happens after function completes

## Context Manager

### When to Use

- Need to update observation during execution
- Streaming responses
- Complex branching logic
- When you need to set fields before the operation completes

### Syntax

```python
with langfuse.start_as_current_observation(
    name="operation",
    as_type="generation",  # Optional: generation, span, tool, event
    input=input_data,
    metadata={"key": "value"}
) as observation:
    # Do work
    result = some_operation()

    # Update during execution
    observation.update(output=result)
```

### Streaming Example

```python
with langfuse.start_as_current_observation(
    as_type="generation",
    name="streaming-llm",
    model="gpt-4o",
    input=messages
) as generation:

    full_output = ""
    stream = client.chat.completions.create(..., stream=True)

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            full_output += content
            yield content  # Stream to user

    # Update when complete
    generation.update(output=full_output)
```

### Nesting

Context managers automatically nest when used together:

```python
with langfuse.start_as_current_observation(name="parent") as parent:
    # Work in parent

    with langfuse.start_as_current_observation(name="child") as child:
        # Child is automatically nested under parent
        pass
```

## Manual Observations

### When to Use

- Parallel/concurrent operations
- Background tasks
- When observation lifecycle doesn't match code scope
- Non-nested or cross-cutting observations

### Syntax

```python
observation = langfuse.start_observation(
    name="background-task",
    as_type="span"
)

# Later...
observation.update(output=result)
observation.end()  # Must call explicitly!
```

### Parallel Operations

```python
# Start all observations
obs1 = langfuse.start_observation(name="parallel-1", as_type="tool")
obs2 = langfuse.start_observation(name="parallel-2", as_type="tool")
obs3 = langfuse.start_observation(name="parallel-3", as_type="tool")

# Run in parallel
import asyncio
results = await asyncio.gather(
    task1(),
    task2(),
    task3()
)

# End observations
obs1.update(output=results[0])
obs1.end()
obs2.update(output=results[1])
obs2.end()
obs3.update(output=results[2])
obs3.end()
```

### Important: Call `.end()`

Manual observations must be explicitly ended:

```python
observation = langfuse.start_observation(name="task")
try:
    result = do_work()
    observation.update(output=result)
finally:
    observation.end()  # Always end!
```

## Comparison Table

| Feature | Decorator | Context Manager | Manual |
|---------|-----------|-----------------|--------|
| Automatic input capture | Yes | No | No |
| Automatic output capture | Yes | No | No |
| Update during execution | Via langfuse_context | Via observation.update() | Via observation.update() |
| Streaming support | Limited | Yes | Yes |
| Automatic nesting | Yes | Yes | No |
| Parallel operations | No | Limited | Yes |
| Code changes required | Minimal | Moderate | More |
| Lifecycle management | Automatic | Automatic | Manual |

## Mixed Usage

You can mix approaches:

```python
@observe()
def main_pipeline(input):
    # Decorator for overall function

    with langfuse.start_as_current_observation(
        as_type="generation",
        name="llm-call"
    ) as gen:
        # Context manager for fine-grained control
        response = stream_llm()
        gen.update(output=response)

    return response
```

## Best Practice Recommendations

1. **Start with decorators** - Quickest to implement
2. **Use context managers for LLM calls** - Better control over model/usage capture
3. **Use manual for parallel work** - When lifecycle doesn't match scope
4. **Don't over-complicate** - Simple code usually needs simple tracing
