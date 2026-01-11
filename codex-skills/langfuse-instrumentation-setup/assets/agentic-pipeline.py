"""
Agentic Pipeline Template

Pattern: User input -> [Think -> Act -> Observe]* -> Final response
Use case: Tool-using agents, multi-step reasoning, autonomous task completion

This template shows:
- Single trace for entire agent execution
- Each reasoning step as a generation
- Each tool call as a tool observation
- Proper loop structure with iteration tracking
"""

import json
from langfuse import Langfuse
from openai import OpenAI

# Initialize clients
langfuse = Langfuse()
openai_client = OpenAI()

# Define available tools
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform a mathematical calculation",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression"}
                },
                "required": ["expression"]
            }
        }
    }
]


def run_agent(
    user_input: str,
    user_id: str = None,
    session_id: str = None,
    max_iterations: int = 10
):
    """
    Agentic pipeline with tool use.

    Args:
        user_input: The user's request
        user_id: Optional user identifier
        session_id: Optional session ID
        max_iterations: Maximum number of think-act cycles

    Returns:
        The agent's final response
    """

    # One trace for the entire agent execution
    with langfuse.start_as_current_observation(
        name="agent-execution",
        user_id=user_id,
        session_id=session_id,
        input=user_input,
        metadata={
            "max_iterations": max_iterations,
            "available_tools": [t["function"]["name"] for t in TOOLS]
        }
    ) as trace:

        messages = [
            {
                "role": "system",
                "content": """You are a helpful assistant with access to tools.
Use tools when needed to answer the user's question.
Think step by step and use the most appropriate tool for each task."""
            },
            {"role": "user", "content": user_input}
        ]

        for iteration in range(max_iterations):
            # Think: LLM decides what to do next
            with langfuse.start_as_current_observation(
                as_type="generation",
                name=f"think-{iteration}",
                model="gpt-4o",
                input=messages,
                metadata={"iteration": iteration}
            ) as think:

                response = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    tools=TOOLS,
                    tool_choice="auto"
                )

                message = response.choices[0].message

                think.update(
                    output={
                        "content": message.content,
                        "tool_calls": [
                            {"name": tc.function.name, "args": tc.function.arguments}
                            for tc in (message.tool_calls or [])
                        ]
                    },
                    usage_details={
                        "input": response.usage.prompt_tokens,
                        "output": response.usage.completion_tokens
                    },
                    metadata={
                        "finish_reason": response.choices[0].finish_reason,
                        "has_tool_calls": message.tool_calls is not None
                    }
                )

            messages.append(message)

            # Check if agent is done (no tool calls, has response)
            if not message.tool_calls:
                if message.content:
                    trace.update(
                        output=message.content,
                        metadata={
                            "iterations": iteration + 1,
                            "completed": True
                        }
                    )
                    return message.content
                else:
                    # No content and no tool calls - unusual state
                    continue

            # Act: Execute each tool call
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                with langfuse.start_as_current_observation(
                    as_type="tool",
                    name=tool_name,
                    input=tool_args,
                    metadata={"tool_call_id": tool_call.id}
                ) as tool_obs:

                    try:
                        result = execute_tool(tool_name, tool_args)
                        tool_obs.update(output=result)
                    except Exception as e:
                        result = {"error": str(e)}
                        tool_obs.update(
                            output=result,
                            level="ERROR",
                            status_message=str(e)
                        )

                # Add tool result to messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })

        # Max iterations reached
        final_output = "I wasn't able to complete the task within the allowed steps."
        trace.update(
            output=final_output,
            metadata={
                "iterations": max_iterations,
                "completed": False,
                "reason": "max_iterations_reached"
            }
        )
        return final_output


def execute_tool(name: str, args: dict) -> dict:
    """Execute a tool by name. Replace with actual implementations."""

    if name == "search_web":
        # Placeholder - replace with actual search
        return {
            "results": [
                {"title": "Example result", "snippet": "..."}
            ]
        }

    elif name == "get_weather":
        # Placeholder - replace with actual weather API
        return {
            "location": args["location"],
            "temperature": 22,
            "conditions": "sunny"
        }

    elif name == "calculate":
        # Simple calculator
        try:
            result = eval(args["expression"])  # Use safe eval in production!
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}

    else:
        return {"error": f"Unknown tool: {name}"}


# Example usage
if __name__ == "__main__":
    result = run_agent(
        user_input="What's the weather in Paris and what's 25 * 4?",
        user_id="user-123"
    )
    print(result)

    # IMPORTANT: Flush in scripts/serverless
    langfuse.flush()
