"""
Basic Pipeline Template

Pattern: User input -> LLM -> Response
Use case: Simple chatbot, Q&A system, single-turn interactions

This template shows the fundamental tracing pattern:
- One trace for the entire request
- One generation for the LLM call
- Proper input/output capture
"""

from langfuse import Langfuse
from openai import OpenAI

# Initialize clients
langfuse = Langfuse()
openai_client = OpenAI()


def run_pipeline(
    user_input: str,
    user_id: str = None,
    session_id: str = None,
    system_prompt: str = "You are a helpful assistant."
):
    """
    Simple pipeline: takes user input, calls LLM, returns response.

    Args:
        user_input: The user's message
        user_id: Optional user identifier for analytics
        session_id: Optional session ID to group related traces
        system_prompt: System prompt for the LLM

    Returns:
        The LLM's response text
    """

    # Create ONE trace for the entire pipeline
    with langfuse.start_as_current_observation(
        name="basic-pipeline",
        user_id=user_id,
        session_id=session_id,
        input=user_input,
        metadata={
            "pipeline_version": "1.0",
            "system_prompt_length": len(system_prompt)
        }
    ) as trace:

        # Prepare messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        # LLM call traced as generation
        with langfuse.start_as_current_observation(
            as_type="generation",
            name="main-llm",
            model="gpt-4o",
            input=messages,
            model_parameters={"temperature": 0.7}
        ) as generation:

            response = openai_client.chat.completions.create(
                model="gpt-4o",
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

        # Update trace with final output
        trace.update(output=output)

        return output


# Example usage
if __name__ == "__main__":
    result = run_pipeline(
        user_input="What is the capital of France?",
        user_id="user-123",
        session_id="session-456"
    )
    print(result)

    # IMPORTANT: Flush in scripts/serverless
    langfuse.flush()
