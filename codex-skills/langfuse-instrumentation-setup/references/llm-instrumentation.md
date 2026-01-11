# LLM Call Instrumentation

How to correctly trace LLM calls in Langfuse.

## Core Rule

**Always use `as_type="generation"` for LLM calls.**

This enables LLM-specific features:
- Model tracking and comparison
- Token usage and cost calculation
- Latency analysis per model
- Prompt/response storage

## Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| `name` | Identifier for this call | `"main-llm"`, `"summarizer"` |
| `model` | Model name | `"gpt-4o"`, `"claude-sonnet-4-20250514"` |
| `input` | Prompt/messages sent | Messages array or string |
| `output` | Response received | Completion text |

## Recommended Fields

| Field | Description | Example |
|-------|-------------|---------|
| `usage_details` | Token counts | `{"input": 100, "output": 50}` |
| `model_parameters` | Model config | `{"temperature": 0.7}` |
| `metadata` | Custom data | `{"prompt_version": "v2"}` |

## Pattern 1: Context Manager (Recommended)

Use when you need control over the observation lifecycle:

```python
from langfuse import Langfuse
from openai import OpenAI

langfuse = Langfuse()
client = OpenAI()

def call_llm(messages: list, model: str = "gpt-4o"):
    with langfuse.start_as_current_observation(
        as_type="generation",
        name="llm-call",
        model=model,
        input=messages,
        model_parameters={"temperature": 0.7}
    ) as generation:

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )

        output = response.choices[0].message.content

        generation.update(
            output=output,
            usage_details={
                "input": response.usage.prompt_tokens,
                "output": response.usage.completion_tokens
            }
        )

        return output
```

## Pattern 2: Decorator

Use for simple functions where automatic capture is sufficient:

```python
from langfuse.decorators import observe

@observe(as_type="generation")
def call_llm(messages: list, model: str = "gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content
```

**Note:** The decorator captures function arguments as input and return value as output automatically.

## Pattern 3: OpenAI Integration

Langfuse provides drop-in OpenAI wrapper:

```python
from langfuse.openai import OpenAI  # Drop-in replacement

client = OpenAI()

# Automatically traced as generation
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Pattern 4: Anthropic

```python
from langfuse import Langfuse
import anthropic

langfuse = Langfuse()
client = anthropic.Anthropic()

with langfuse.start_as_current_observation(
    as_type="generation",
    name="claude-call",
    model="claude-sonnet-4-20250514",
    input=messages
) as generation:

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=messages
    )

    output = response.content[0].text

    generation.update(
        output=output,
        usage_details={
            "input": response.usage.input_tokens,
            "output": response.usage.output_tokens
        }
    )
```

## Streaming Responses

For streaming, update the generation as chunks arrive:

```python
with langfuse.start_as_current_observation(
    as_type="generation",
    name="streaming-llm",
    model="gpt-4o",
    input=messages
) as generation:

    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        stream=True
    )

    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            yield chunk.choices[0].delta.content

    # Update with final response when done
    generation.update(output=full_response)
```

## Multi-Turn Conversations

For chat applications, pass the full message history:

```python
def chat(user_message: str, history: list):
    messages = history + [{"role": "user", "content": user_message}]

    with langfuse.start_as_current_observation(
        as_type="generation",
        name="chat-turn",
        model="gpt-4o",
        input=messages  # Full history for context
    ) as generation:

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        assistant_message = response.choices[0].message.content
        generation.update(output=assistant_message)

        return assistant_message
```

## System Prompts

Include system prompts in the input:

```python
with langfuse.start_as_current_observation(
    as_type="generation",
    name="with-system-prompt",
    model="gpt-4o",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
) as generation:
    ...
```

## Using Langfuse Prompts

Fetch prompts from Langfuse for version control:

```python
# Get prompt from Langfuse
prompt = langfuse.get_prompt("my-prompt", label="production")

with langfuse.start_as_current_observation(
    as_type="generation",
    name="prompted-llm",
    model=prompt.config.get("model", "gpt-4o"),
    input=[
        {"role": "system", "content": prompt.prompt},
        {"role": "user", "content": user_input}
    ],
    metadata={"prompt_name": "my-prompt", "prompt_version": prompt.version}
) as generation:
    ...
```

## Error Handling

Capture errors in the generation:

```python
with langfuse.start_as_current_observation(
    as_type="generation",
    name="llm-call",
    model="gpt-4o",
    input=messages
) as generation:
    try:
        response = client.chat.completions.create(...)
        generation.update(output=response.choices[0].message.content)
    except Exception as e:
        generation.update(
            level="ERROR",
            status_message=str(e)
        )
        raise
```

## Key Takeaways

1. **Always use `as_type="generation"`** - Not span, not event
2. **Set the model** - Essential for cost tracking and comparison
3. **Capture usage** - Token counts enable cost analysis
4. **Input includes full context** - System prompts, history, everything sent to the model
5. **Context managers for control** - Decorators for simplicity
