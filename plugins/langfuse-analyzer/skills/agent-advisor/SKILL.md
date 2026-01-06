---
name: langfuse-agent-advisor
description: This skill should be used when the user wants to brainstorm about agent development strategy, asks "how should I evaluate", "what dataset do I need", "how to improve my agent", "best approach for", or needs strategic guidance on building, testing, and iterating on AI agents. A knowledgeable partner for thinking through agent engineering challenges.
---

# AI Agent Engineering Advisor

A brainstorming partner for thinking through agent development strategy. Helps you figure out the right approach for evaluation, dataset curation, and improvement cycles based on your specific project and constraints.

## How to Use This Skill

When the user describes their project (e.g., "web research agent", "customer support bot", "code generation agent"), help them think through:

1. **Evaluation strategy** - What to measure and how
2. **Dataset approach** - What test cases to build
3. **Improvement cycle** - How to iterate effectively

Ask clarifying questions. Understand their constraints. Then provide strategic guidance.

---

## Evaluation Strategy Framework

### The Three Pillars (Google)

Help users think through evaluation across three dimensions:

**Pillar 1: Output Quality**
- Does the final result solve the user's problem?
- Is it accurate, relevant, coherent?
- Task completion rate

**Pillar 2: Process/Trajectory Quality**
- Did the agent take sensible steps to get there?
- Tool selection accuracy
- Reasoning quality
- Efficiency (no wasted steps)

**Pillar 3: Trust & Safety**
- Does it handle edge cases gracefully?
- Error recovery
- Prompt injection resistance
- Appropriate behavior under adversarial input

### Key Question to Ask Users

> "If your agent produces a correct answer through flawed reasoning, is that a pass or fail?"

This reveals whether they need trajectory evaluation (Pillar 2) or just output evaluation (Pillar 1).

### Evaluation Methods

| Method | Best For | Scalability |
|--------|----------|-------------|
| **Human evaluation** | Establishing ground truth, subjective quality | Low - expensive, slow |
| **LLM-as-judge** | Approximating human judgment at scale | High - fast, cheap |
| **Programmatic** | Objective correctness, format validation | High - regression testing |
| **Adversarial** | Finding failure modes | Medium - creative test cases |

**Starting point:** Most projects should use LLM-as-judge for quality + programmatic checks for format/correctness.

---

## Dataset Curation Strategy

### The Golden Dataset Concept

A curated set of test cases with known expected outcomes. This is the foundation for:
- Measuring baseline performance
- Detecting regressions
- Comparing iterations

### Three Ways to Build a Dataset

**1. Synthesize with "Dueling LLMs"**
- Use a second LLM to roleplay as users
- Generates diverse multi-turn conversations at scale
- Good for: Initial dataset when you have no production data

**2. Curate from Production**
- Pull real traces from Langfuse
- Anonymize and annotate with expected outcomes
- Good for: Realistic edge cases you didn't anticipate

**3. Human-in-the-Loop Curation**
- Experts create test cases for critical scenarios
- Include adversarial/edge cases
- Good for: High-stakes domains, safety-critical behavior

### What to Include in Your Dataset

| Category | Purpose | Example |
|----------|---------|---------|
| **Happy path** | Common successful cases | Typical user queries |
| **Edge cases** | Unusual but valid inputs | Long queries, ambiguous requests |
| **Adversarial** | Inputs designed to break it | Prompt injection, contradictory info |
| **Failure modes** | Known weaknesses | Cases you've seen fail in production |

### Starting Without a Golden Dataset

You don't need a perfect dataset to start. Use this progression:

```
Week 1: Human evaluation on 20-30 cases
        ↓ Define what "good" means
Week 2: Convert to LLM-as-judge prompts
        ↓ Scale up evaluation
Week 3: Add production failures as they occur
        ↓ Dataset grows organically
Ongoing: Continuous curation from traces
```

---

## Improvement Cycle Methodology

### Anthropic's Evaluation-First Approach

From Claude Code best practices:

1. **Document specific failures** - What exactly is going wrong?
2. **Create evaluations** - Build 3+ test cases that capture the failure
3. **Establish baseline** - Measure current performance
4. **Make minimal changes** - Address gaps with targeted fixes
5. **Iterate** - Run evals, adjust, repeat

**Key insight:** Create evaluations BEFORE writing fixes. This prevents solving imaginary problems.

### Manus's Iteration Methodology

From building Manus AI:

- **"Stochastic Graduate Descent"** - Manual architecture search + prompt experimentation
- Rebuilt their agent framework 4 times based on empirical results
- Ship improvements in hours, not weeks (via prompt changes vs fine-tuning)

### The Virtuous Feedback Loop

```
Production → Monitor → Review → Identify failures
     ↑                              ↓
     └──────── Curate ←───── Annotate with expected outcome
               (add to dataset)
```

**Continuous cycle:**
1. Monitor production traces in Langfuse
2. Identify interesting failures or novel requests
3. Annotate with expected outcome
4. Add to evaluation dataset
5. Use in next iteration cycle

---

## Metrics That Matter

### Output Layer (Pillar 1)

- **Task completion rate** - Did it finish the job?
- **Answer accuracy** - Is the output correct?
- **Groundedness** - Is it based on real information?
- **Relevance** - Does it address the actual question?

### Reasoning Layer (Pillar 2)

- **Plan quality** - Is the approach logical and efficient?
- **Plan adherence** - Did it follow its own plan?
- **Tool selection accuracy** - Did it pick the right tools?
- **Step efficiency** - No unnecessary actions?

### Operational (Production)

- **Latency** - How long does it take?
- **Cost** - Token usage per task
- **Error rate** - How often does it fail completely?
- **User feedback** - Thumbs up/down signals

---

## Project-Specific Guidance

When helping users, tailor advice to their project type:

### Web Research Agent
- **Key challenge:** Grounding - is information from reliable sources?
- **Evaluation focus:** Factual accuracy, source quality, completeness
- **Dataset approach:** Queries with verifiable answers, include current events
- **Metrics:** Groundedness, citation accuracy, information completeness

### Customer Support Bot
- **Key challenge:** Handling edge cases without escalation
- **Evaluation focus:** Resolution rate, appropriate escalation
- **Dataset approach:** Real tickets, include escalation scenarios
- **Metrics:** Resolution rate, customer satisfaction proxy, escalation accuracy

### Code Generation Agent
- **Key challenge:** Code that actually works
- **Evaluation focus:** Test pass rate, code quality
- **Dataset approach:** Problems with test suites, include edge cases
- **Metrics:** Test pass rate, lint score, human review score

### RAG/Q&A System
- **Key challenge:** Retrieval quality affects everything
- **Evaluation focus:** Retrieval relevance + generation quality
- **Dataset approach:** Questions with known answers in corpus
- **Metrics:** Retrieval precision, answer accuracy, hallucination rate

---

## Using Langfuse Skills for This

Help users leverage the other skills for their improvement cycle:

**Building dataset from production:**
```bash
# Find interesting traces
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 50 --mode minimal

# Find failures to learn from
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 30 --max-score 5.0 --mode io

# Add to dataset
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dataset-management/helpers/dataset_manager.py \
  add-trace --dataset "my-evals" --trace-id <id>
```

**Setting up LLM judges:**
```bash
# Create judge prompt in Langfuse
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  create --name "judge-accuracy" --type text --prompt "..."
```

**Running evaluations:**
```bash
# Run with Langfuse judges
python3 ${CLAUDE_PLUGIN_ROOT}/skills/experiment-runner/helpers/experiment_runner.py \
  run --dataset "my-evals" --run-name "v2-test" \
  --task-script ./task.py --use-langfuse-judges
```

**Analyzing results:**
```bash
# Compare iterations
python3 ${CLAUDE_PLUGIN_ROOT}/skills/experiment-runner/helpers/experiment_runner.py \
  compare --dataset "my-evals" --runs "v1" "v2"

# Find what's still failing
python3 ${CLAUDE_PLUGIN_ROOT}/skills/experiment-runner/helpers/experiment_runner.py \
  analyze --dataset "my-evals" --run-name "v2-test" --show-failures
```

---

## Questions to Ask Users

When brainstorming, understand their situation:

1. **What does your agent do?** (task type)
2. **What's going wrong?** (specific failures vs general quality)
3. **Do you have production data?** (dataset starting point)
4. **What does "good" look like?** (success criteria)
5. **What are your constraints?** (time, cost, latency requirements)
6. **How will you know if you've improved?** (metrics)

Then help them design an approach tailored to their answers.

---

## Sources

This skill draws from:
- [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Manus: Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Google Cloud: A Methodical Approach to Agent Evaluation](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation)
- [DeepEval: AI Agent Evaluation Guide](https://deepeval.com/guides/guides-ai-agent-evaluation)
- [Datadog: Building an LLM Evaluation Framework](https://www.datadoghq.com/blog/llm-evaluation-framework-best-practices/)
