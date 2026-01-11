"""
Multi-Model Pipeline Template

Pattern: Input -> LLM1 -> LLM2 -> ... -> Output
Use case: Chained processing, summarize-then-translate, review-then-refine

This template shows:
- Single trace for the chain
- Each LLM call as a separate generation
- Passing output from one step as input to the next
- Different models for different purposes
"""

from langfuse import Langfuse
from openai import OpenAI

# Initialize clients
langfuse = Langfuse()
openai_client = OpenAI()


def run_summarize_and_translate(
    document: str,
    target_language: str = "Spanish",
    user_id: str = None,
    session_id: str = None
):
    """
    Multi-step pipeline: summarize document, then translate summary.

    Args:
        document: The document to process
        target_language: Target language for translation
        user_id: Optional user identifier
        session_id: Optional session ID

    Returns:
        Translated summary
    """

    # One trace for the entire chain
    with langfuse.start_as_current_observation(
        name="summarize-and-translate",
        user_id=user_id,
        session_id=session_id,
        input={"document_length": len(document), "target_language": target_language},
        metadata={
            "pipeline_type": "chain",
            "steps": ["summarize", "translate"]
        }
    ) as trace:

        # Step 1: Summarize (fast model for summarization)
        with langfuse.start_as_current_observation(
            as_type="generation",
            name="summarize",
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": "You are a summarization expert. Create a concise summary of the document."
                },
                {"role": "user", "content": f"Summarize this document:\n\n{document}"}
            ]
        ) as summarize:

            summary_response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a summarization expert. Create a concise summary of the document."
                    },
                    {"role": "user", "content": f"Summarize this document:\n\n{document}"}
                ],
                temperature=0.3
            )

            summary = summary_response.choices[0].message.content

            summarize.update(
                output=summary,
                usage_details={
                    "input": summary_response.usage.prompt_tokens,
                    "output": summary_response.usage.completion_tokens
                },
                metadata={"summary_length": len(summary)}
            )

        # Step 2: Translate (quality model for translation)
        with langfuse.start_as_current_observation(
            as_type="generation",
            name="translate",
            model="gpt-4o",
            input=[
                {
                    "role": "system",
                    "content": f"You are a professional translator. Translate the text to {target_language}. Preserve the meaning and tone."
                },
                {"role": "user", "content": summary}
            ],
            metadata={"source_language": "English", "target_language": target_language}
        ) as translate:

            translation_response = openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a professional translator. Translate the text to {target_language}. Preserve the meaning and tone."
                    },
                    {"role": "user", "content": summary}
                ],
                temperature=0.3
            )

            translation = translation_response.choices[0].message.content

            translate.update(
                output=translation,
                usage_details={
                    "input": translation_response.usage.prompt_tokens,
                    "output": translation_response.usage.completion_tokens
                }
            )

        # Update trace with final output
        trace.update(
            output=translation,
            metadata={
                "summary_length": len(summary),
                "translation_length": len(translation)
            }
        )

        return translation


def run_generate_and_review(
    prompt: str,
    user_id: str = None,
    max_revisions: int = 2
):
    """
    Generate content, then review and refine it.

    Args:
        prompt: What to generate
        user_id: Optional user identifier
        max_revisions: Maximum revision iterations

    Returns:
        Final refined content
    """

    with langfuse.start_as_current_observation(
        name="generate-and-review",
        user_id=user_id,
        input=prompt,
        metadata={"max_revisions": max_revisions}
    ) as trace:

        # Step 1: Initial generation
        with langfuse.start_as_current_observation(
            as_type="generation",
            name="initial-generation",
            model="gpt-4o",
            input=[{"role": "user", "content": prompt}]
        ) as gen:

            response = openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            content = response.choices[0].message.content

            gen.update(
                output=content,
                usage_details={
                    "input": response.usage.prompt_tokens,
                    "output": response.usage.completion_tokens
                }
            )

        # Step 2: Review and revise loop
        for revision in range(max_revisions):
            # Review
            with langfuse.start_as_current_observation(
                as_type="generation",
                name=f"review-{revision}",
                model="gpt-4o",
                input=[
                    {
                        "role": "system",
                        "content": """Review this content for:
1. Clarity and coherence
2. Accuracy and completeness
3. Grammar and style

If improvements are needed, explain what should be changed.
If the content is good, respond with "APPROVED"."""
                    },
                    {"role": "user", "content": content}
                ]
            ) as review:

                review_response = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": """Review this content for:
1. Clarity and coherence
2. Accuracy and completeness
3. Grammar and style

If improvements are needed, explain what should be changed.
If the content is good, respond with "APPROVED"."""
                        },
                        {"role": "user", "content": content}
                    ],
                    temperature=0.2
                )

                feedback = review_response.choices[0].message.content

                review.update(
                    output=feedback,
                    usage_details={
                        "input": review_response.usage.prompt_tokens,
                        "output": review_response.usage.completion_tokens
                    }
                )

            # Check if approved
            if "APPROVED" in feedback.upper():
                trace.update(
                    output=content,
                    metadata={"revisions": revision, "approved": True}
                )
                return content

            # Revise based on feedback
            with langfuse.start_as_current_observation(
                as_type="generation",
                name=f"revise-{revision}",
                model="gpt-4o",
                input=[
                    {"role": "user", "content": f"Original request: {prompt}"},
                    {"role": "assistant", "content": content},
                    {"role": "user", "content": f"Please revise based on this feedback:\n{feedback}"}
                ]
            ) as revise:

                revise_response = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "user", "content": f"Original request: {prompt}"},
                        {"role": "assistant", "content": content},
                        {"role": "user", "content": f"Please revise based on this feedback:\n{feedback}"}
                    ]
                )

                content = revise_response.choices[0].message.content

                revise.update(
                    output=content,
                    usage_details={
                        "input": revise_response.usage.prompt_tokens,
                        "output": revise_response.usage.completion_tokens
                    }
                )

        # Max revisions reached
        trace.update(
            output=content,
            metadata={"revisions": max_revisions, "approved": False}
        )
        return content


# Example usage
if __name__ == "__main__":
    # Example 1: Summarize and translate
    document = """
    Artificial intelligence has made remarkable progress in recent years.
    Machine learning models can now understand and generate human language,
    recognize images, and even create art. These advances are transforming
    industries from healthcare to transportation.
    """

    result = run_summarize_and_translate(
        document=document,
        target_language="French",
        user_id="user-123"
    )
    print("Translated summary:", result)

    # Example 2: Generate and review
    result = run_generate_and_review(
        prompt="Write a short introduction to machine learning for beginners.",
        user_id="user-123",
        max_revisions=2
    )
    print("Final content:", result)

    # IMPORTANT: Flush in scripts/serverless
    langfuse.flush()
