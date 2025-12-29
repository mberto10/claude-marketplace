# Essential Code Patterns for GenAI Engineers

A practical guide to classical software engineering patterns, prioritized for engineers with strong GenAI/LLM knowledge who want to level up their foundational code architecture skills.

---

## Learning Philosophy

**Pattern-first learning works when you apply immediately.** For each pattern:

1. Understand the concept (10 min)
2. Find examples in real codebases (30 min)
3. Apply it to something you're building
4. Have AI implement it, then critique the result

---

## Tier 1: Foundational (Learn First)

### 1. Dependency Injection

**What**: Pass dependencies in rather than creating them inside a class.

**Why**: Makes code testable, flexible, and explicit about its dependencies. Every senior engineer expects this.

**Before (tight coupling)**:
```python
class Agent:
    def __init__(self):
        self.llm = OpenAI()  # Locked in, can't test
        self.db = PostgresDB()  # Hidden dependency
```

**After (dependency injection)**:
```python
class Agent:
    def __init__(self, llm: LLM, db: Database):
        self.llm = llm
        self.db = db

# Now testable:
agent = Agent(llm=MockLLM(), db=InMemoryDB())
```

**GenAI connection**: You already do this when passing `model="gpt-4"` as config—DI is the formalized version.

**Use when**: Always. This is the default way to structure classes.

---

### 2. Strategy Pattern

**What**: Define a family of interchangeable algorithms behind a common interface.

**Why**: Eliminates `if/elif` chains. Each strategy is isolated, testable, and swappable at runtime.

```python
from typing import Protocol

class Embedder(Protocol):
    def embed(self, text: str) -> list[float]: ...

class OpenAIEmbedder:
    def embed(self, text: str) -> list[float]:
        return openai.embed(text)

class LocalEmbedder:
    def embed(self, text: str) -> list[float]:
        return local_model.embed(text)

# Swap without changing calling code
retriever = Retriever(embedder=OpenAIEmbedder())
retriever = Retriever(embedder=LocalEmbedder())
```

**GenAI connection**: Your model routers and provider selection are strategies.

**Use when**: You have multiple ways to do the same thing (embedding, LLM calls, parsing, validation).

---

### 3. Repository Pattern

**What**: Abstract data access behind a clean interface.

**Why**: Domain logic never knows about SQL, Redis, or file systems. Swap storage freely. Test without databases.

```python
from typing import Protocol

class ConversationRepository(Protocol):
    def save(self, conv: Conversation) -> None: ...
    def get(self, id: str) -> Conversation | None: ...
    def list_by_user(self, user_id: str) -> list[Conversation]: ...

class PostgresConversationRepo:
    def __init__(self, connection):
        self.conn = connection

    def save(self, conv: Conversation) -> None:
        self.conn.execute("INSERT INTO conversations ...")

    def get(self, id: str) -> Conversation | None:
        row = self.conn.fetchone("SELECT * FROM conversations WHERE id = %s", id)
        return Conversation.from_row(row) if row else None

class InMemoryConversationRepo:
    """For testing - no database needed."""
    def __init__(self):
        self._store: dict[str, Conversation] = {}

    def save(self, conv: Conversation) -> None:
        self._store[conv.id] = conv

    def get(self, id: str) -> Conversation | None:
        return self._store.get(id)
```

**Use when**: Any time you persist data. Separates "what data" from "how stored."

---

### 4. Decorator Pattern

**What**: Wrap behavior around existing functions/classes without modifying them.

**Why**: Cross-cutting concerns (logging, retry, caching, tracing) stay separate from business logic.

```python
import functools
import time

def retry(max_attempts: int = 3, backoff: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(backoff * (2 ** attempt))
        return wrapper
    return decorator

def cache(ttl: int = 3600):
    def decorator(func):
        _cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args in _cache:
                value, timestamp = _cache[args]
                if time.time() - timestamp < ttl:
                    return value
            result = func(*args)
            _cache[args] = (result, time.time())
            return result
        return wrapper
    return decorator

# Usage: stack decorators for composed behavior
@retry(max_attempts=3)
@cache(ttl=3600)
def call_llm(prompt: str) -> str:
    return client.complete(prompt)
```

**GenAI connection**: Your observability/tracing wrappers (Langfuse, etc.) are decorators.

**Use when**: Logging, caching, retry, auth, timing, tracing—anything that wraps behavior.

---

## Tier 2: Structural (Learn Next)

### 5. Adapter Pattern

**What**: Translate between your interface and an external/incompatible interface.

**Why**: Isolates third-party dependencies. When an API changes, you change one adapter file.

```python
from typing import Protocol

# Your interface (you control this)
class VectorStore(Protocol):
    def search(self, embedding: list[float], k: int) -> list[Document]: ...
    def upsert(self, id: str, embedding: list[float], metadata: dict) -> None: ...

# Adapter for Pinecone
class PineconeAdapter(VectorStore):
    def __init__(self, client, index_name: str):
        self.index = client.Index(index_name)

    def search(self, embedding: list[float], k: int) -> list[Document]:
        results = self.index.query(vector=embedding, top_k=k, include_metadata=True)
        return [Document(id=m.id, content=m.metadata["text"]) for m in results.matches]

    def upsert(self, id: str, embedding: list[float], metadata: dict) -> None:
        self.index.upsert(vectors=[{"id": id, "values": embedding, "metadata": metadata}])

# Adapter for Weaviate (same interface, different implementation)
class WeaviateAdapter(VectorStore):
    def __init__(self, client, class_name: str):
        self.client = client
        self.class_name = class_name

    def search(self, embedding: list[float], k: int) -> list[Document]:
        result = self.client.query.get(self.class_name, ["text"]).with_near_vector({"vector": embedding}).with_limit(k).do()
        return [Document(id=item["_id"], content=item["text"]) for item in result["data"]["Get"][self.class_name]]
```

**Use when**: Integrating any third-party library or API. Your code depends on YOUR interface.

---

### 6. Factory Pattern

**What**: Centralize complex object creation logic.

**Why**: Object creation often has conditional logic, defaults, and wiring. Factories contain this complexity.

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class AgentConfig:
    model: str = "gpt-4"
    tools: list[str] = None
    memory_type: Literal["buffer", "summary", "vector"] = "buffer"
    temperature: float = 0.7

def create_agent(config: AgentConfig) -> Agent:
    """Factory function - all creation logic in one place."""

    # Create LLM based on model string
    if config.model.startswith("gpt"):
        llm = OpenAILLM(model=config.model, temperature=config.temperature)
    elif config.model.startswith("claude"):
        llm = AnthropicLLM(model=config.model, temperature=config.temperature)
    else:
        llm = LocalLLM(model=config.model)

    # Create tools
    tools = [create_tool(name) for name in (config.tools or [])]

    # Create memory
    memory = {
        "buffer": BufferMemory,
        "summary": SummaryMemory,
        "vector": VectorMemory,
    }[config.memory_type]()

    return Agent(llm=llm, tools=tools, memory=memory)

# Usage is simple
agent = create_agent(AgentConfig(model="claude-3-opus", tools=["search", "calculator"]))
```

**Use when**: Object creation is complex, involves conditionals, or needs to be consistent across the codebase.

---

### 7. Facade Pattern

**What**: Provide a simple interface over a complex subsystem.

**Why**: Users of your system don't need to understand internals. Reduces cognitive load.

```python
class RAGSystem:
    """Facade: simple interface hiding complex internals."""

    def __init__(
        self,
        embedder: Embedder,
        vector_store: VectorStore,
        reranker: Reranker,
        llm: LLM,
        chunker: Chunker,
    ):
        self._embedder = embedder
        self._vector_store = vector_store
        self._reranker = reranker
        self._llm = llm
        self._chunker = chunker

    def index(self, document: str, doc_id: str) -> None:
        """Simple method hides chunking, embedding, upserting."""
        chunks = self._chunker.chunk(document)
        for i, chunk in enumerate(chunks):
            embedding = self._embedder.embed(chunk)
            self._vector_store.upsert(f"{doc_id}_{i}", embedding, {"text": chunk})

    def query(self, question: str, k: int = 5) -> str:
        """Simple method hides retrieval, reranking, generation."""
        embedding = self._embedder.embed(question)
        candidates = self._vector_store.search(embedding, k=k * 3)
        reranked = self._reranker.rerank(question, candidates, k=k)
        context = "\n\n".join(doc.content for doc in reranked)
        return self._llm.generate(f"Context:\n{context}\n\nQuestion: {question}")

# User only sees simple API
rag = RAGSystem(...)
rag.index("Long document text...", "doc_123")
answer = rag.query("What is the main argument?")
```

**Use when**: You have a complex subsystem that others will use. Good API design.

---

## Tier 3: Behavioral (Learn When Needed)

### 8. Observer / Event Bus

**What**: Decouple event producers from consumers.

**Why**: Modules don't need to know about each other. Add new behaviors without modifying existing code.

```python
from collections import defaultdict
from typing import Callable, Any

class EventBus:
    def __init__(self):
        self._handlers: dict[str, list[Callable]] = defaultdict(list)

    def on(self, event: str, handler: Callable) -> None:
        """Subscribe to an event."""
        self._handlers[event].append(handler)

    def emit(self, event: str, data: Any = None) -> None:
        """Publish an event to all subscribers."""
        for handler in self._handlers[event]:
            handler(data)

# Setup
event_bus = EventBus()

# Different modules subscribe independently
def send_welcome_email(user):
    print(f"Sending welcome email to {user['email']}")

def create_default_workspace(user):
    print(f"Creating workspace for {user['id']}")

def track_signup(user):
    print(f"Analytics: user {user['id']} signed up")

event_bus.on("user.created", send_welcome_email)
event_bus.on("user.created", create_default_workspace)
event_bus.on("user.created", track_signup)

# Producer doesn't know who's listening
event_bus.emit("user.created", {"id": "123", "email": "user@example.com"})
```

**Use when**: Multiple reactions to the same event, loose coupling between modules.

---

### 9. Builder Pattern

**What**: Construct complex objects step by step with a fluent interface.

**Why**: Better than constructors with 15 parameters. Self-documenting. Can enforce required fields.

```python
from dataclasses import dataclass, field

@dataclass
class Prompt:
    system: str = ""
    messages: list[dict] = field(default_factory=list)
    examples: list[dict] = field(default_factory=list)
    output_schema: dict = None

class PromptBuilder:
    def __init__(self):
        self._system = ""
        self._messages = []
        self._examples = []
        self._output_schema = None

    def system(self, content: str) -> "PromptBuilder":
        self._system = content
        return self

    def user(self, content: str) -> "PromptBuilder":
        self._messages.append({"role": "user", "content": content})
        return self

    def assistant(self, content: str) -> "PromptBuilder":
        self._messages.append({"role": "assistant", "content": content})
        return self

    def example(self, input: str, output: str) -> "PromptBuilder":
        self._examples.append({"input": input, "output": output})
        return self

    def output_schema(self, schema: dict) -> "PromptBuilder":
        self._output_schema = schema
        return self

    def build(self) -> Prompt:
        return Prompt(
            system=self._system,
            messages=self._messages,
            examples=self._examples,
            output_schema=self._output_schema,
        )

# Fluent, readable construction
prompt = (
    PromptBuilder()
    .system("You are a helpful assistant.")
    .example("What is 2+2?", "4")
    .example("What is the capital of France?", "Paris")
    .user("What is the largest planet?")
    .output_schema({"type": "object", "properties": {"answer": {"type": "string"}}})
    .build()
)
```

**Use when**: Complex object construction, optional parameters, fluent APIs.

---

### 10. State Machine

**What**: Model explicit states and valid transitions between them.

**Why**: Replaces tangled boolean flags and conditionals. Makes valid states explicit and enforced.

```python
from enum import Enum

class DocumentState(Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    INDEXED = "indexed"
    FAILED = "failed"

# Define valid transitions explicitly
VALID_TRANSITIONS: dict[DocumentState, set[DocumentState]] = {
    DocumentState.UPLOADED: {DocumentState.PROCESSING},
    DocumentState.PROCESSING: {DocumentState.INDEXED, DocumentState.FAILED},
    DocumentState.FAILED: {DocumentState.PROCESSING},  # Allow retry
    DocumentState.INDEXED: set(),  # Terminal state
}

class InvalidTransition(Exception):
    pass

class Document:
    def __init__(self, id: str):
        self.id = id
        self.state = DocumentState.UPLOADED

    def transition_to(self, new_state: DocumentState) -> None:
        if new_state not in VALID_TRANSITIONS[self.state]:
            raise InvalidTransition(
                f"Cannot transition from {self.state.value} to {new_state.value}"
            )
        self.state = new_state

    def start_processing(self) -> None:
        self.transition_to(DocumentState.PROCESSING)

    def mark_indexed(self) -> None:
        self.transition_to(DocumentState.INDEXED)

    def mark_failed(self) -> None:
        self.transition_to(DocumentState.FAILED)

    def retry(self) -> None:
        self.transition_to(DocumentState.PROCESSING)

# Usage
doc = Document("doc_123")
doc.start_processing()  # OK: UPLOADED -> PROCESSING
doc.mark_indexed()       # OK: PROCESSING -> INDEXED
doc.retry()              # Raises InvalidTransition: INDEXED has no valid transitions
```

**Use when**: Workflows, lifecycles, anything with distinct states (orders, documents, tasks).

---

## Bonus: Registry Pattern

**What**: Central lookup for implementations registered by name.

**Why**: Extensible plugin architecture. New implementations register without modifying core code.

```python
class HandlerRegistry:
    _handlers: dict[str, type] = {}

    @classmethod
    def register(cls, name: str):
        def decorator(handler_class):
            cls._handlers[name] = handler_class
            return handler_class
        return decorator

    @classmethod
    def get(cls, name: str):
        if name not in cls._handlers:
            raise KeyError(f"No handler registered for '{name}'")
        return cls._handlers[name]()

# Handlers register themselves
@HandlerRegistry.register("json")
class JsonHandler:
    def process(self, data): ...

@HandlerRegistry.register("xml")
class XmlHandler:
    def process(self, data): ...

# Usage
handler = HandlerRegistry.get("json")
handler.process(data)
```

**Use when**: Plugin systems, format handlers, extensible architectures.

---

## Quick Reference

| Pattern | One-liner | Use When |
|---------|-----------|----------|
| **Dependency Injection** | Pass dependencies in | Always (default approach) |
| **Strategy** | Swappable algorithms | Multiple ways to do same thing |
| **Repository** | Abstract data access | Any persistence |
| **Decorator** | Wrap behavior | Cross-cutting concerns |
| **Adapter** | Translate interfaces | Third-party integrations |
| **Factory** | Centralize creation | Complex object construction |
| **Facade** | Simplify complex systems | API design |
| **Observer** | Event-driven decoupling | Multiple reactions to events |
| **Builder** | Step-by-step construction | Many optional parameters |
| **State Machine** | Explicit states/transitions | Workflows, lifecycles |

---

## The Meta-Principle

All these patterns share one insight: **separate what changes from what stays the same.**

When you identify the axis of change in your code, the right pattern usually becomes obvious.

---

## Anti-Pattern: Over-Engineering

Every pattern has a cost:
- More files and indirection
- More cognitive load for readers
- More abstraction to maintain

**The goal is not "use all patterns"—it's "use the right pattern, or none."**

Three similar lines of code is often better than a premature abstraction.

---

## Learning Schedule

| Week | Focus | Patterns |
|------|-------|----------|
| 1-2 | Foundational | DI, Strategy, Repository |
| 3-4 | Structural | Decorator, Adapter, Factory |
| 5+ | Behavioral | Facade, Observer, Builder, State Machine |

For each pattern: read → find examples → apply → critique AI implementations.
