# Agent Instrumentation

How to correctly trace agentic workflows in Langfuse.

## Agent Structure

An agent typically follows this pattern:
1. Receive input
2. **Loop:** Think -> Decide -> Act -> Observe
3. Return final output

The trace should capture this entire flow.

## Visual Model

```
TRACE: agent-execution
|
+-- GENERATION: initial-planning
|   "I need to search for weather data, then format the response"
|
+-- TOOL: weather-api
|   input: {location: "Paris"}
|   output: {temp: 18, conditions: "cloudy"}
|
+-- GENERATION: reasoning
|   "The weather data shows 18 deg C and cloudy. Let me format this."
|
+-- GENERATION: final-response
|   "It's currently 18 deg C and cloudy in Paris."
|
output: "It's currently 18 deg C and cloudy in Paris."
```

## Basic Agent Pattern

```python
from langfuse import Langfuse
from openai import OpenAI

langfuse = Langfuse()
client = OpenAI()

def run_agent(user_input: str, user_id: str = None, session_id: str = None):
    # One trace for the entire agent execution
    with langfuse.start_as_current_observation(
        name="agent-execution",
        user_id=user_id,
        session_id=session_id,
        input=user_input
    ) as trace:

        messages = [
            {"role": "system", "content": AGENT_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]

        max_iterations = 10
        for i in range(max_iterations):
            # LLM decides next action
            with langfuse.start_as_current_observation(
                as_type="generation",
                name=f"think-step-{i}",
                model="gpt-4o",
                input=messages
            ) as gen:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    tools=TOOL_DEFINITIONS
                )
                gen.update(
                    output=response.choices[0].message,
                    usage_details={
                        "input": response.usage.prompt_tokens,
                        "output": response.usage.completion_tokens
                    }
                )

            message = response.choices[0].message
            messages.append(message)

            # Check if done
            if message.content and not message.tool_calls:
                trace.update(output=message.content)
                return message.content

            # Execute tool calls
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)

                    with langfuse.start_as_current_observation(
                        as_type="tool",
                        name=tool_name,
                        input=tool_args
                    ) as tool:
                        result = execute_tool(tool_name, tool_args)
                        tool.update(output=result)

                    # Add tool result to messages
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(result)
                    })

        # Max iterations reached
        trace.update(output="Max iterations reached")
        return "Max iterations reached"
```

## ReAct Pattern

For Reason-Act-Observe loops:

```python
def react_agent(user_input: str):
    with langfuse.start_as_current_observation(
        name="react-agent",
        input=user_input
    ) as trace:

        thought_history = []

        for step in range(max_steps):
            # Reason
            with langfuse.start_as_current_observation(
                as_type="generation",
                name=f"reason-{step}",
                model="gpt-4o",
                input={"history": thought_history, "query": user_input}
            ) as reason:
                thought = llm.generate_thought(thought_history, user_input)
                reason.update(output=thought)

            thought_history.append({"thought": thought})

            # Check if final answer
            if thought.get("final_answer"):
                trace.update(output=thought["final_answer"])
                return thought["final_answer"]

            # Act
            action = thought.get("action")
            if action:
                with langfuse.start_as_current_observation(
                    as_type="tool",
                    name=action["tool"],
                    input=action["args"]
                ) as tool:
                    observation = execute_tool(action["tool"], action["args"])
                    tool.update(output=observation)

                thought_history.append({"observation": observation})
```

## Multi-Agent Pattern

For systems with multiple specialized agents:

```python
def orchestrator(user_input: str):
    with langfuse.start_as_current_observation(
        name="multi-agent-orchestrator",
        input=user_input
    ) as trace:

        # Router decides which agent
        with langfuse.start_as_current_observation(
            as_type="generation",
            name="router",
            model="gpt-4o-mini"
        ) as router:
            route = llm.route(user_input)
            router.update(output=route)

        # Execute specialized agent
        with langfuse.start_as_current_observation(
            as_type="span",  # Use span to group agent work
            name=f"agent-{route['agent']}"
        ) as agent_span:

            if route["agent"] == "research":
                result = research_agent(user_input)
            elif route["agent"] == "coding":
                result = coding_agent(user_input)
            else:
                result = general_agent(user_input)

            agent_span.update(output=result)

        trace.update(output=result)
        return result
```

## Parallel Tool Execution

When tools can run in parallel:

```python
import asyncio

async def run_parallel_tools(tool_calls: list):
    with langfuse.start_as_current_observation(
        as_type="span",
        name="parallel-tools"
    ) as parallel_span:

        async def run_one(tool_call):
            with langfuse.start_as_current_observation(
                as_type="tool",
                name=tool_call["name"],
                input=tool_call["args"]
            ) as tool:
                result = await execute_tool_async(tool_call["name"], tool_call["args"])
                tool.update(output=result)
                return result

        results = await asyncio.gather(*[run_one(tc) for tc in tool_calls])
        parallel_span.update(output={"results": results})
        return results
```

## Agent with Memory

For agents that maintain state:

```python
def stateful_agent(user_input: str, session_id: str):
    with langfuse.start_as_current_observation(
        name="stateful-agent",
        session_id=session_id,  # Groups traces by session
        input=user_input
    ) as trace:

        # Load memory
        with langfuse.start_as_current_observation(
            as_type="span",
            name="load-memory"
        ) as mem_span:
            memory = memory_store.get(session_id)
            mem_span.update(output={"memory_items": len(memory)})

        # Agent execution with memory context
        result = agent_loop(user_input, memory)

        # Save memory
        with langfuse.start_as_current_observation(
            as_type="span",
            name="save-memory"
        ) as save_span:
            memory_store.save(session_id, memory)
            save_span.update(output={"saved": True})

        trace.update(output=result)
        return result
```

## Tracing Agent Decisions

Capture why the agent made decisions:

```python
with langfuse.start_as_current_observation(
    as_type="generation",
    name="decide-next-action",
    model="gpt-4o",
    input=messages,
    metadata={
        "step": step_number,
        "available_tools": [t["name"] for t in tools],
        "context_length": len(str(messages))
    }
) as decision:
    response = llm.generate(messages, tools)

    decision.update(
        output=response,
        metadata={
            "chose_tool": response.tool_calls[0].name if response.tool_calls else None,
            "is_final": response.content is not None and not response.tool_calls
        }
    )
```

## Key Takeaways

1. **One trace per agent invocation** - Not per step
2. **Each LLM call is a generation** - Even reasoning steps
3. **Each tool call is a tool observation** - With input/output
4. **Use spans to group** - Multi-agent, parallel execution
5. **Session ID for continuity** - Groups related agent runs
6. **Capture decisions** - Why the agent chose each action
