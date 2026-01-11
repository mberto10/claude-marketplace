"""
RAG Pipeline Template

Pattern: User input -> Retrieve -> Augment -> Generate
Use case: Document Q&A, knowledge base search, context-aware responses

This template shows:
- Trace containing the full RAG flow
- Embedding generation traced separately
- Retrieval as a tool observation
- Final generation with augmented context
"""

from langfuse import Langfuse
from openai import OpenAI

# Initialize clients
langfuse = Langfuse()
openai_client = OpenAI()


def run_rag_pipeline(
    user_query: str,
    user_id: str = None,
    session_id: str = None,
    top_k: int = 5
):
    """
    RAG pipeline: retrieves relevant documents and generates a response.

    Args:
        user_query: The user's question
        user_id: Optional user identifier
        session_id: Optional session ID
        top_k: Number of documents to retrieve

    Returns:
        The generated response based on retrieved context
    """

    # One trace for the entire RAG pipeline
    with langfuse.start_as_current_observation(
        name="rag-pipeline",
        user_id=user_id,
        session_id=session_id,
        input=user_query,
        metadata={"top_k": top_k}
    ) as trace:

        # Step 1: Generate embedding for the query
        with langfuse.start_as_current_observation(
            as_type="generation",
            name="query-embedding",
            model="text-embedding-3-small",
            input=user_query
        ) as embedding_gen:

            embedding_response = openai_client.embeddings.create(
                model="text-embedding-3-small",
                input=user_query
            )
            query_embedding = embedding_response.data[0].embedding

            embedding_gen.update(
                output={"dimensions": len(query_embedding)},
                usage_details={
                    "input": embedding_response.usage.prompt_tokens,
                    "output": 0
                }
            )

        # Step 2: Retrieve relevant documents
        with langfuse.start_as_current_observation(
            as_type="tool",
            name="vector-search",
            input={
                "query": user_query,
                "top_k": top_k,
                "embedding_dimensions": len(query_embedding)
            }
        ) as retrieval:

            # Replace with your actual vector store
            documents = search_vector_store(query_embedding, top_k)

            retrieval.update(
                output={
                    "document_count": len(documents),
                    "documents": [
                        {"id": doc["id"], "score": doc["score"]}
                        for doc in documents
                    ]
                }
            )

        # Step 3: Generate response with context
        context = "\n\n".join([doc["content"] for doc in documents])

        messages = [
            {
                "role": "system",
                "content": f"""You are a helpful assistant. Answer the user's question based on the following context.
If the context doesn't contain relevant information, say so.

Context:
{context}"""
            },
            {"role": "user", "content": user_query}
        ]

        with langfuse.start_as_current_observation(
            as_type="generation",
            name="rag-generation",
            model="gpt-4o",
            input=messages,
            metadata={
                "context_length": len(context),
                "num_documents": len(documents)
            }
        ) as generation:

            response = openai_client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.3  # Lower temperature for factual responses
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
        trace.update(
            output=output,
            metadata={
                "total_documents_retrieved": len(documents),
                "context_used": len(context) > 0
            }
        )

        return output


def search_vector_store(embedding: list, top_k: int) -> list:
    """
    Placeholder for your vector store search.
    Replace with actual implementation (Pinecone, Weaviate, pgvector, etc.)
    """
    # Example return format
    return [
        {
            "id": "doc-1",
            "content": "Example document content...",
            "score": 0.92
        },
        {
            "id": "doc-2",
            "content": "Another relevant document...",
            "score": 0.87
        }
    ]


# Example usage
if __name__ == "__main__":
    result = run_rag_pipeline(
        user_query="How do I reset my password?",
        user_id="user-123",
        top_k=3
    )
    print(result)

    # IMPORTANT: Flush in scripts/serverless
    langfuse.flush()
