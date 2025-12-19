# Tool Call Instrumentation

How to correctly trace tool and API calls in Langfuse.

## Core Rule

**Use `as_type="tool"` for tool/function calls made by agents.**

This enables:
- Tool usage tracking
- Success/failure analysis
- Latency per tool
- Input/output inspection

## When to Use Tool Type

Use `as_type="tool"` for:
- Function calls decided by an LLM
- External API calls
- Database queries
- File operations
- Any discrete operation with input/output

Use `as_type="span"` for:
- Internal preprocessing/postprocessing
- Logic that isn't a discrete "tool"

## Basic Pattern

```python
from langfuse import Langfuse

langfuse = Langfuse()

def call_tool(tool_name: str, args: dict):
    with langfuse.start_as_current_observation(
        as_type="tool",
        name=tool_name,
        input=args
    ) as tool:

        result = execute_tool(tool_name, args)

        tool.update(output=result)

        return result
```

## Common Tool Patterns

### Search/Retrieval

```python
def search_documents(query: str, limit: int = 10):
    with langfuse.start_as_current_observation(
        as_type="tool",
        name="document-search",
        input={"query": query, "limit": limit}
    ) as tool:

        results = vector_db.search(query, limit=limit)

        tool.update(
            output={"count": len(results), "results": results},
            metadata={"index": "main", "model": "text-embedding-3-small"}
        )

        return results
```

### External API

```python
def get_weather(location: str):
    with langfuse.start_as_current_observation(
        as_type="tool",
        name="weather-api",
        input={"location": location}
    ) as tool:

        try:
            response = requests.get(
                f"https://api.weather.com/v1/current",
                params={"location": location}
            )
            response.raise_for_status()
            data = response.json()

            tool.update(output=data)
            return data

        except Exception as e:
            tool.update(
                level="ERROR",
                status_message=str(e),
                output={"error": str(e)}
            )
            raise
```

### Database Query

```python
def query_database(sql: str, params: dict = None):
    with langfuse.start_as_current_observation(
        as_type="tool",
        name="database-query",
        input={"sql": sql, "params": params}
    ) as tool:

        start = time.time()
        results = db.execute(sql, params)
        duration_ms = (time.time() - start) * 1000

        tool.update(
            output={"rows": len(results), "data": results[:10]},  # Truncate for storage
            metadata={"duration_ms": duration_ms}
        )

        return results
```

### Calculator/Code Execution

```python
def calculate(expression: str):
    with langfuse.start_as_current_observation(
        as_type="tool",
        name="calculator",
        input={"expression": expression}
    ) as tool:

        try:
            result = eval(expression)  # In production, use safe eval
            tool.update(output={"result": result})
            return result
        except Exception as e:
            tool.update(
                level="ERROR",
                output={"error": str(e)}
            )
            raise
```

## Nested Tools

Tools can contain nested operations:

```python
def complex_search(query: str):
    with langfuse.start_as_current_observation(
        as_type="tool",
        name="complex-search",
        input={"query": query}
    ) as tool:

        # Nested embedding generation
        with langfuse.start_as_current_observation(
            as_type="generation",
            name="embedding",
            model="text-embedding-3-small",
            input=query
        ) as embedding:
            vector = embed_model.encode(query)
            embedding.update(output={"dimensions": len(vector)})

        # Nested vector search
        with langfuse.start_as_current_observation(
            as_type="tool",
            name="vector-search",
            input={"vector": "...", "limit": 10}
        ) as search:
            results = vector_db.search(vector)
            search.update(output=results)

        tool.update(output={"count": len(results), "results": results})
        return results
```

## Tool Registry Pattern

For agents with multiple tools:

```python
class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name: str, func):
        self.tools[name] = func

    def call(self, name: str, args: dict):
        """Call a tool with automatic tracing."""
        if name not in self.tools:
            raise ValueError(f"Unknown tool: {name}")

        with langfuse.start_as_current_observation(
            as_type="tool",
            name=name,
            input=args
        ) as tool:
            try:
                result = self.tools[name](**args)
                tool.update(output=result)
                return result
            except Exception as e:
                tool.update(level="ERROR", status_message=str(e))
                raise

# Usage
registry = ToolRegistry()
registry.register("search", search_documents)
registry.register("weather", get_weather)
registry.register("calculate", calculate)

# In agent loop
result = registry.call(tool_name, tool_args)
```

## Error Handling

Always capture tool failures:

```python
with langfuse.start_as_current_observation(
    as_type="tool",
    name="risky-tool",
    input=args
) as tool:
    try:
        result = execute_risky_operation(args)
        tool.update(output=result)
        return result
    except TimeoutError:
        tool.update(level="ERROR", status_message="Timeout")
        return {"error": "timeout"}
    except RateLimitError:
        tool.update(level="WARNING", status_message="Rate limited")
        return {"error": "rate_limit"}
    except Exception as e:
        tool.update(level="ERROR", status_message=str(e))
        raise
```

## Metadata Best Practices

Add useful metadata for debugging:

```python
with langfuse.start_as_current_observation(
    as_type="tool",
    name="api-call",
    input=args,
    metadata={
        "service": "external-api",
        "version": "v2",
        "retry_count": retry_count,
        "timeout_ms": 5000
    }
) as tool:
    ...
```

## Key Takeaways

1. **Use `as_type="tool"`** - Not span or generation
2. **Capture input and output** - Essential for debugging
3. **Handle errors explicitly** - Set level and status_message
4. **Add metadata** - Service version, timing, retry info
5. **Tools can nest** - Embeddings inside search, etc.
