# AI Agent Dogfooding Methodology

> A systematic approach to building self-improving AI agents through evaluation-driven development.

## The Core Difference

Traditional product dogfooding evaluates a **single user journey**. AI agent dogfooding evaluates **many outputs** because:

1. **Non-determinism** — Same input produces different outputs
2. **Quality is multi-dimensional** — Accuracy, style, completeness, safety
3. **The "code" is different** — Prompts, architecture, tool selection
4. **Improvement is iterative** — Small prompt changes, not bug fixes

| Aspect | Traditional Product | AI Agent |
|--------|---------------------|----------|
| Evaluation unit | Single journey | Dataset of samples |
| Quality measure | Qualitative experience | Quantitative scores |
| Determinism | Deterministic | Probabilistic |
| What to "fix" | Application code | Prompts, architecture, tools |
| Trace format | Code execution | LLM calls, reasoning steps |
| Success metric | Works/doesn't work | pass@k, score distributions |

## The Universal Three-Layer Structure

The three-layer dogfooding structure applies to AI agents, but with different methods:

```
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 1: OUTPUT QUALITY EVALUATION                              │
│                                                                 │
│ Perspective: Output consumer                                    │
│ Question:    "Does the agent produce good outputs?"             │
│ Method:      Run agent on dataset, score with judges            │
│                                                                 │
│ Measures:                                                       │
│   • Task completion rate                                        │
│   • Quality scores (accuracy, relevance, style)                 │
│   • Safety/appropriateness                                      │
│   • Efficiency (tokens, latency, cost)                          │
│                                                                 │
│ Output: Score distributions, failure cases, pass rates          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    Failure cases identified
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 2: BEHAVIOR ANALYSIS (Trace Investigation)                │
│                                                                 │
│ Perspective: Agent architect                                    │
│ Question:    "Why did the agent fail?"                          │
│ Method:      Analyze execution traces of failures               │
│                                                                 │
│ Investigates:                                                   │
│   • Decision points — Where did reasoning go wrong?             │
│   • Tool usage — Did it use the right tools? Correctly?         │
│   • Context — Did it have the right information?                │
│   • Prompts — Were instructions clear? Followed?                │
│                                                                 │
│ Output: Root causes, prompt issues, architecture gaps           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    Root causes identified
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 3: COMPONENT VERIFICATION                                 │
│                                                                 │
│ Perspective: System reliability                                 │
│ Question:    "Do the building blocks work correctly?"           │
│ Method:      Unit-level evaluation of components                │
│                                                                 │
│ Verifies:                                                       │
│   • Tools return correct results                                │
│   • Retrieval fetches relevant context                          │
│   • External APIs respond correctly                             │
│   • State/context passes correctly between steps                │
│                                                                 │
│ Output: Component-level issues, reliability metrics             │
└─────────────────────────────────────────────────────────────────┘
```

## The Agent Dogfooding Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                  THE AGENT DOGFOODING LOOP                      │
│                                                                 │
│                      ┌──────────────┐                           │
│                      │              │                           │
│         ┌───────────▶│    BUILD     │                           │
│         │            │              │                           │
│         │            └──────┬───────┘                           │
│         │                   │                                   │
│         │                   ▼                                   │
│         │            ┌──────────────┐                           │
│         │            │              │                           │
│         │            │   EVALUATE   │◀──── Datasets             │
│         │            │              │◀──── Judges               │
│         │            └──────┬───────┘                           │
│         │                   │                                   │
│         │                   ▼                                   │
│         │            ┌──────────────┐                           │
│         │            │              │                           │
│         │            │   ANALYZE    │◀──── Traces               │
│         │            │              │                           │
│         │            └──────┬───────┘                           │
│         │                   │                                   │
│         │                   ▼                                   │
│         │            ┌──────────────┐                           │
│         │            │              │                           │
│         │            │   IMPROVE    │                           │
│         │            │              │                           │
│         │            └──────┬───────┘                           │
│         │                   │                                   │
│         │                   ▼                                   │
│         │            ┌──────────────┐                           │
│         │            │              │                           │
│         └────────────│   COMPOUND   │                           │
│                      │              │                           │
│                      └──────────────┘                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Phase | What Happens | Artifacts |
|-------|--------------|-----------|
| **BUILD** | Create/modify prompts, tools, architecture | Agent code, prompts |
| **EVALUATE** | Run agent on dataset, score outputs | Scores, pass rates |
| **ANALYZE** | Trace through failures, find root causes | Diagnostic reports |
| **IMPROVE** | Fix prompts, add tools, change architecture | Updated agent |
| **COMPOUND** | Encode learnings, expand datasets | Better evals |

---

## Alignment with Anthropic's Eval Best Practices

The methodology incorporates key principles from Anthropic's agent evaluation guidance:

### Three Grader Types

| Grader Type | Implementation | Best For |
|-------------|----------------|----------|
| **Code-based** | Programmatic checks (JSON valid, word count, contains X) | Objective, fast, reproducible |
| **Model-based** | LLM-as-judge with rubrics | Subjective quality, nuanced assessment |
| **Human** | Manual annotation and review | Gold standard, calibration |

All three should be used. Code-based for fast iteration, model-based for scale, human for calibration.

### Capability vs Regression Evals

```
┌─────────────────────────────────────────────────────────────────┐
│ CAPABILITY EVALS                                                │
│                                                                 │
│ Purpose: Measure what the agent can learn to do                 │
│ Start:   Low pass rates (agent can't do it yet)                 │
│ Goal:    Push pass rates up through improvement                 │
│ Dataset: Aspirational tasks, stretch goals                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ REGRESSION EVALS                                                │
│                                                                 │
│ Purpose: Ensure nothing breaks with changes                     │
│ Start:   High pass rates (agent already handles these)          │
│ Goal:    Maintain pass rates, catch regressions                 │
│ Dataset: Known working cases, past failures (now fixed)         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Non-Determinism Metrics

Because agents are non-deterministic, single-run pass/fail is insufficient:

| Metric | Formula | Use When |
|--------|---------|----------|
| **pass@k** | P(at least one success in k trials) | "One good answer is enough" |
| **pass^k** | P(all k trials succeed) | "Must be reliable every time" |

For critical applications, track pass^k. For exploratory tasks, pass@k may suffice.

### Read Transcripts

> "Reading transcripts is a critical skill"

When agents fail, the trace reveals:
- Did the judge reject a valid solution? → Fix the eval
- Did the agent genuinely err? → Fix the agent

This distinction is crucial. Bad evals waste improvement effort.

### Eval-Driven Development

```
1. Write evals BEFORE agent can pass them
2. Establish baseline (low pass rate expected)
3. Iterate on agent until passing
4. Add passing cases to regression suite
5. Repeat with new capability evals
```

This inverts traditional development: evals first, then implementation.

---

## The Langfuse Integration

Langfuse provides the infrastructure for the entire loop:

```
┌─────────────────────────────────────────────────────────────────┐
│                     LANGFUSE ECOSYSTEM                          │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │             │  │             │  │             │             │
│  │   TRACES    │  │  DATASETS   │  │   PROMPTS   │             │
│  │             │  │             │  │             │             │
│  │ Execution   │  │ Test cases  │  │ Versioned   │             │
│  │ history     │  │ for evals   │  │ prompts     │             │
│  │             │  │             │  │             │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         │                │                │                     │
│         ▼                ▼                ▼                     │
│  ┌─────────────────────────────────────────────────┐           │
│  │                                                 │           │
│  │               EXPERIMENTS                       │           │
│  │                                                 │           │
│  │   Run agent on dataset, score with judges       │           │
│  │                                                 │           │
│  └─────────────────────────────────────────────────┘           │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │             │  │             │  │             │             │
│  │   SCORES    │  │ ANNOTATIONS │  │  ANALYTICS  │             │
│  │             │  │             │  │             │             │
│  │ Automated   │  │ Human       │  │ Trends,     │             │
│  │ eval scores │  │ labels      │  │ regressions │             │
│  │             │  │             │  │             │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Mapping Loop Phases to Langfuse

| Phase | Langfuse Component | Usage |
|-------|-------------------|-------|
| BUILD | Prompts | Version control agent prompts |
| EVALUATE | Datasets + Experiments | Run agent, apply judges |
| ANALYZE | Traces | Investigate failures |
| IMPROVE | Prompts | Update and version |
| COMPOUND | Datasets + Scores | Add failures, track progress |

---

## Layer 1: Output Quality Evaluation

### Setting Up Evaluation

**Step 1: Define Quality Dimensions**

What makes a good output? Define measurable criteria:

```yaml
dimensions:
  - name: accuracy
    type: numeric
    scale: 0-10
    description: "Factual correctness of claims"

  - name: completeness
    type: numeric
    scale: 0-10
    description: "Covers all required aspects"

  - name: style
    type: categorical
    values: [matches, partially_matches, does_not_match]
    description: "Adherence to style guide"

  - name: safety
    type: boolean
    description: "No harmful or inappropriate content"
```

**Step 2: Create Dataset**

Start with 20-50 realistic cases (Anthropic's recommendation):

```
Sources for initial dataset:
├── Real user failures (production traces with low scores)
├── Manual test cases (designed to test specific capabilities)
├── Edge cases (unusual inputs, boundary conditions)
└── Adversarial cases (inputs designed to cause failure)
```

Balance the dataset:
- Include cases where behavior SHOULD occur
- Include cases where behavior should NOT occur
- Avoid one-sided optimization

**Step 3: Create Judges**

For each dimension, create an evaluator:

```markdown
## Judge: Accuracy

You are evaluating the factual accuracy of an AI-generated response.

**Input:** {{input}}
**Output:** {{output}}
**Expected:** {{expected_output}} (if available)

Evaluate on a scale of 0-10:
- 10: All claims are factually correct and verifiable
- 7-9: Minor inaccuracies that don't affect main points
- 4-6: Some significant inaccuracies
- 1-3: Major factual errors
- 0: Completely incorrect or fabricated

Provide:
1. Score (0-10)
2. Reasoning (specific claims evaluated)
3. Evidence (what was correct/incorrect)
```

**Step 4: Run Experiment**

```python
# Pseudocode for experiment execution
for item in dataset:
    # Run agent k times for non-determinism
    outputs = [agent.run(item.input) for _ in range(k)]

    # Score each output with each judge
    for output in outputs:
        scores = {
            'accuracy': accuracy_judge(item, output),
            'completeness': completeness_judge(item, output),
            'style': style_judge(item, output),
            'safety': safety_judge(item, output),
        }
        record_scores(item, output, scores)

    # Calculate pass@k and pass^k
    calculate_aggregate_metrics(item, outputs)
```

### Evaluation Output

```markdown
# Experiment Results: Article Writer v2.3

## Summary
- Dataset: article_writing_v1 (50 items)
- Trials per item: 3
- Total runs: 150

## Score Distributions

| Dimension | Mean | P50 | P95 | Pass Rate |
|-----------|------|-----|-----|-----------|
| accuracy | 7.2 | 7.5 | 9.0 | 78% |
| completeness | 8.1 | 8.0 | 10.0 | 85% |
| style | 6.5 | 7.0 | 9.0 | 62% |
| safety | 9.8 | 10.0 | 10.0 | 99% |

## Pass Metrics
- pass@3 (at least one good): 92%
- pass^3 (all three good): 58%

## Failure Cases (12 items)
1. item_023: accuracy=3, style=4 — "Technical claims unsourced"
2. item_037: completeness=2 — "Missing required sections"
...

## Regression Check
- vs v2.2: accuracy +0.3, style -0.2, completeness +0.5
- No regressions detected (within threshold)
```

---

## Layer 2: Behavior Analysis

When Layer 1 identifies failures, Layer 2 investigates WHY.

### Trace Investigation Process

```
┌─────────────────────────────────────────────────────────────────┐
│ FAILURE TRIAGE                                                  │
│                                                                 │
│ 1. Retrieve trace for failed output                             │
│ 2. Classify symptom type:                                       │
│    • Output error (wrong content)                               │
│    • Data gap (missing information)                             │
│    • Quality issue (correct but poor)                           │
│    • Execution error (crashed/incomplete)                       │
│    • Latency issue (too slow)                                   │
│    • Cost issue (too expensive)                                 │
│                                                                 │
│ 3. Apply investigation strategy for symptom type                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Investigation Strategies

**Output Error (Wrong Content)**
```
1. Find the step that produced wrong output
2. Check input to that step — was it correct?
3. Check prompt — were instructions clear?
4. Check model response — did it follow instructions?
5. Compare to successful trace — where did they diverge?
```

**Data Gap (Missing Information)**
```
1. Trace backward from output — what data was expected?
2. Find retrieval/tool calls — did they return data?
3. Check filtering logic — was relevant data filtered out?
4. Check context window — was data truncated?
5. Check tool correctness — did external call succeed?
```

**Quality Issue (Correct but Poor)**
```
1. Compare to high-scoring output on same input
2. Identify differences in reasoning steps
3. Check prompt emphasis — is quality criteria clear?
4. Check examples — are there quality exemplars?
5. Check revision steps — did self-critique run?
```

### Good vs Bad Comparison

The most powerful debugging technique: diff successful and failed traces.

```
SUCCESSFUL TRACE (score: 9)          FAILED TRACE (score: 4)
─────────────────────────────────    ─────────────────────────────────
1. Parse input                       1. Parse input
2. Research: query "X"               2. Research: query "X"
   → Found 5 sources                    → Found 5 sources
3. Research: query "Y"               3. [MISSING - no second query]
   → Found 3 sources
4. Synthesize from 8 sources         4. Synthesize from 5 sources
5. Fact-check claims                 5. [MISSING - no fact-check]
6. Apply style guide                 6. Apply style guide
7. Final output                      7. Final output

DIVERGENCE POINT: Step 3             ROOT CAUSE: Research incomplete,
                                                 fact-check skipped
```

### Trace Analysis Output

```markdown
# Trace Analysis: item_023 (accuracy=3)

## Symptom
Article contains unsourced technical claims about quantum computing.

## Trace Summary
```
Input: "Write article about quantum computing breakthroughs"
    ↓
research_tool("quantum computing breakthroughs 2024")
    → 3 results (all news articles, no technical sources)
    ↓
draft_article(sources=3)
    → Generated article with specific technical claims
    ↓
[NO FACT-CHECK STEP]
    ↓
style_revision()
    → Final output
```

## Root Cause Analysis

1. **Research quality**: Query returned news articles, not technical sources
   - News articles don't contain technical details
   - Agent extrapolated/hallucinated technical specifics

2. **Missing fact-check**: The fact-checking step was skipped
   - Condition: `if len(sources) > 5` — only 3 sources found
   - Bug: threshold too high, fact-check should always run

## Recommended Fixes

1. **Improve research prompt**: "Include academic and technical sources"
2. **Fix fact-check condition**: Always run, regardless of source count
3. **Add source quality filter**: Prefer technical over news sources

## Similar Failures

Found 3 other items with same pattern:
- item_028: accuracy=4 (missing technical verification)
- item_041: accuracy=3 (news-only sources)
- item_045: accuracy=5 (skipped fact-check)

→ This is a systematic issue, not one-off failure
```

---

## Layer 3: Component Verification

When Layer 2 points to specific components, Layer 3 verifies them in isolation.

### Component Types

```
┌─────────────────────────────────────────────────────────────────┐
│ TOOLS                                                           │
│                                                                 │
│ External capabilities the agent can invoke                      │
│                                                                 │
│ Verify:                                                         │
│   • Returns correct results for known inputs                    │
│   • Handles errors gracefully                                   │
│   • Performance within acceptable bounds                        │
│   • Edge cases handled                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ RETRIEVAL                                                       │
│                                                                 │
│ Context/knowledge retrieval systems                             │
│                                                                 │
│ Verify:                                                         │
│   • Relevance of retrieved documents                            │
│   • Recall — does it find what exists?                          │
│   • Precision — is noise filtered?                              │
│   • Chunk quality — right granularity?                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PROMPTS                                                         │
│                                                                 │
│ Instructions that guide LLM behavior                            │
│                                                                 │
│ Verify:                                                         │
│   • Instructions are clear and unambiguous                      │
│   • Examples demonstrate expected behavior                      │
│   • Edge cases are addressed                                    │
│   • Output format is specified                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STATE MANAGEMENT                                                │
│                                                                 │
│ Context passing between steps                                   │
│                                                                 │
│ Verify:                                                         │
│   • State correctly passed between steps                        │
│   • No data loss in serialization                               │
│   • Context window not exceeded                                 │
│   • Memory correctly maintained                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Component-Level Evaluation

For each component, create targeted tests:

```python
# Tool verification example
def test_research_tool():
    # Known query with expected results
    results = research_tool("python asyncio tutorial")

    assert len(results) >= 3, "Should return multiple results"
    assert any("asyncio" in r.title.lower() for r in results), \
        "Results should be relevant"
    assert all(r.url.startswith("https://") for r in results), \
        "URLs should be valid"
    assert results[0].snippet is not None, \
        "Should include snippets"

# Retrieval verification example
def test_retrieval_relevance():
    query = "How do I reset my password?"
    docs = retriever.retrieve(query, k=5)

    # At least one doc should be about password reset
    relevant = [d for d in docs if "password" in d.content.lower()]
    assert len(relevant) >= 1, "Should retrieve relevant docs"

    # Relevance score should be high for relevant docs
    assert docs[0].score > 0.7, "Top doc should be highly relevant"
```

### Component Audit Output

```markdown
# Component Audit: Research Tool

## Test Results

| Test Case | Expected | Actual | Status |
|-----------|----------|--------|--------|
| Basic query | 5+ results | 3 results | ⚠️ WARN |
| Technical query | Technical sources | News only | ❌ FAIL |
| Error handling | Graceful fallback | Throws exception | ❌ FAIL |
| Rate limiting | Retry logic | No retry | ❌ FAIL |

## Issues Found

1. **Source quality**: Tool doesn't filter by source type
   - News articles ranked equal to technical docs
   - No preference for authoritative sources

2. **Result quantity**: Sometimes returns fewer results than requested
   - API pagination not implemented

3. **Error handling**: No retry on transient failures
   - Network errors cause complete failure

## Recommendations

1. Add source type filtering parameter
2. Implement pagination for more results
3. Add retry logic with exponential backoff
4. Log and surface partial failures
```

---

## The Compound Step

The unique opportunity with AI agents: **the evaluation system itself can improve**.

### What Compounds?

```
┌─────────────────────────────────────────────────────────────────┐
│ DATASET GROWTH                                                  │
│                                                                 │
│ Every failure becomes a test case:                              │
│   • Failed items → add to regression dataset                    │
│   • Edge cases discovered → add to capability dataset           │
│   • Adversarial inputs found → add to adversarial dataset       │
│                                                                 │
│ The dataset gets more comprehensive with each cycle             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ JUDGE IMPROVEMENT                                               │
│                                                                 │
│ Evaluation quality increases:                                   │
│   • Calibrate judges against human labels                       │
│   • Add dimensions discovered through failures                  │
│   • Refine rubrics based on edge cases                          │
│   • Version judges alongside agent prompts                      │
│                                                                 │
│ Better judges catch more issues                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ AGENT PROMPTS                                                   │
│                                                                 │
│ Prompts evolve through experimentation:                         │
│   • Version control in Langfuse                                 │
│   • A/B test prompt variants                                    │
│   • Promote successful versions to production                   │
│   • Archive learnings about what works                          │
│                                                                 │
│ Prompts become more robust and effective                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FAILURE PATTERNS                                                │
│                                                                 │
│ Knowledge about common failures:                                │
│   • Document patterns (like technical-investigation.md)         │
│   • Create checklists for known issues                          │
│   • Build specific tests for recurring problems                 │
│                                                                 │
│ Debugging gets faster with each cycle                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### The Virtuous Feedback Loop

```
Production
    │
    ▼
Monitor (Langfuse traces + scores)
    │
    ▼
Review (identify low-scoring traces)
    │
    ▼
Identify failures (trace analysis)
    │
    ▼
Curate (add to dataset)
    │
    ▼
Annotate (human labels for calibration)
    │
    ▼
Experiment (run improved agent)
    │
    ▼
Deploy (if better)
    │
    └──────────▶ Production
```

This loop runs continuously. Production failures become test cases, test cases prevent future failures.

### Compound Artifacts

| Artifact | Storage | Purpose |
|----------|---------|---------|
| Test cases | Langfuse datasets | Regression prevention |
| Judge prompts | Langfuse prompts | Consistent evaluation |
| Agent prompts | Langfuse prompts | Version-controlled behavior |
| Score history | Langfuse scores | Track improvement over time |
| Failure patterns | Reference docs | Faster debugging |
| Architecture decisions | Documentation | Institutional knowledge |

---

## Concrete Example: Article Writing Agent

### The Agent

An agent that writes articles with criteria:
- **Fact-driven**: Claims are sourced and verifiable
- **Style-adherent**: Matches defined style guide
- **Complete**: Covers all required sections
- **Engaging**: Readable and interesting

### Layer 1: Output Quality Setup

**Dataset: article_writing_v1**
```yaml
items:
  - id: article_001
    input:
      topic: "Recent advances in quantum computing"
      style: "technical_blog"
      sections: ["intro", "background", "advances", "implications", "conclusion"]
    expected:
      min_sources: 5
      required_sections: all

  - id: article_002
    input:
      topic: "Best practices for remote work"
      style: "business_casual"
      sections: ["intro", "tips", "tools", "conclusion"]
    expected:
      min_sources: 3
      required_sections: all

  # ... 48 more items covering edge cases, different styles, etc.
```

**Judges**
```yaml
judges:
  - name: accuracy
    type: llm
    prompt: langfuse://prompts/judge-accuracy@production
    threshold: 7.0

  - name: completeness
    type: programmatic
    check: "all required sections present"
    threshold: 1.0  # boolean

  - name: style
    type: llm
    prompt: langfuse://prompts/judge-style@production
    threshold: 7.0

  - name: source_count
    type: programmatic
    check: "count citations >= expected.min_sources"
    threshold: 1.0
```

### Layer 2: Failure Investigation

After running experiment, analyze failures:

```markdown
# Failure Analysis: Article Writer v1.0

## Failure Pattern 1: Unsourced Technical Claims

**Affected items:** 8/50 (16%)
**Symptom:** accuracy < 5, technical topics

**Trace Pattern:**
- Research step returns news articles only
- No technical/academic sources retrieved
- Agent extrapolates technical details without sources

**Root Cause:** Research query doesn't specify source type

**Fix:** Update research prompt to request technical sources

---

## Failure Pattern 2: Missing Sections

**Affected items:** 5/50 (10%)
**Symptom:** completeness < 0.8

**Trace Pattern:**
- Outline step generates correct sections
- Writing step skips sections when article gets long
- Context window approaching limit

**Root Cause:** No explicit instruction to complete all sections

**Fix:** Add explicit checklist verification step

---

## Failure Pattern 3: Style Drift

**Affected items:** 12/50 (24%)
**Symptom:** style < 6

**Trace Pattern:**
- Initial paragraphs match style
- Style degrades in later sections
- No style enforcement after initial draft

**Root Cause:** Style guide only referenced in initial prompt

**Fix:** Add style revision pass after complete draft
```

### Layer 3: Component Verification

Test components in isolation:

```markdown
# Component Audit Results

## Research Tool
- Technical query test: FAIL (returns news, not academic)
- Source diversity test: FAIL (single domain dominates)
- Recommendation: Add source type parameter

## Style Guide Retrieval
- Retrieval accuracy: PASS (correct guide retrieved)
- Content coverage: WARN (missing examples for edge cases)
- Recommendation: Expand style guide examples

## Section Writer
- Basic section: PASS
- Long section: FAIL (truncates at ~1000 words)
- Recommendation: Chunk long sections
```

### The Improvement Cycle

```
Cycle 1 (v1.0 → v1.1):
├── Fix: Add source type to research prompt
├── Fix: Add section completion checklist
├── Fix: Add style revision pass
├── Result: accuracy 7.2→8.1, completeness 0.85→0.95
└── Add 8 failure cases to regression dataset

Cycle 2 (v1.1 → v1.2):
├── Fix: Improve research query generation
├── Fix: Handle long sections with chunking
├── Result: accuracy 8.1→8.5, style 6.5→7.8
└── Add 5 failure cases to regression dataset

Cycle 3 (v1.2 → v1.3):
├── Fix: Add fact-checking step
├── Fix: Improve source quality ranking
├── Result: accuracy 8.5→9.1
└── Add 3 edge cases to capability dataset
```

### What Compounded

After 3 cycles:
- **Dataset**: 50 → 66 items (failures became tests)
- **Judges**: Added fact_verification dimension
- **Agent prompts**: v1.0 → v1.3 (4 versions, learnings encoded)
- **Failure patterns**: 3 documented, won't recur
- **Pass rate**: 58% → 89%

---

## The Self-Improving System

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SELF-IMPROVING AGENT SYSTEM                  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                      AGENT                               │   │
│  │                                                         │   │
│  │   Prompts (versioned) ──────────────────────┐           │   │
│  │   Tools                                      │           │   │
│  │   Architecture                               │           │   │
│  │                                              │           │   │
│  └──────────────────────────────────────────────│───────────┘   │
│                         │                       │               │
│                         ▼                       │               │
│  ┌─────────────────────────────────────────────│───────────┐   │
│  │                 EVALUATION                   │           │   │
│  │                                              │           │   │
│  │   Datasets ──────────────────────────────────┤           │   │
│  │   Judges (versioned) ────────────────────────┤           │   │
│  │   Experiments                                │           │   │
│  │   Scores                                     │           │   │
│  │                                              │           │   │
│  └──────────────────────────────────────────────│───────────┘   │
│                         │                       │               │
│                         ▼                       │               │
│  ┌─────────────────────────────────────────────│───────────┐   │
│  │                 ANALYSIS                     │           │   │
│  │                                              │           │   │
│  │   Traces                                     │           │   │
│  │   Failure patterns                           │           │   │
│  │   Root cause identification                  │           │   │
│  │                                              │           │   │
│  └──────────────────────────────────────────────│───────────┘   │
│                         │                       │               │
│                         │      ┌────────────────┘               │
│                         ▼      ▼                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   COMPOUND                               │   │
│  │                                                         │   │
│  │   Update prompts (new version)                          │   │
│  │   Expand datasets (failures → tests)                    │   │
│  │   Improve judges (calibrate, add dimensions)            │   │
│  │   Document patterns (institutional knowledge)           │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Compounding Formula

For AI agents, the compounding formula has multiple components:

```
capability_n = capability_0 × (1 + r_agent)^n × (1 + r_eval)^n
```

Where:
- **r_agent** = improvement rate of agent per cycle
- **r_eval** = improvement rate of evaluation per cycle

Because both compound, the system improves faster than either alone.

### Thresholds and Graduation

Define when agent is "ready":

```yaml
graduation_criteria:
  capability_eval:
    pass_rate: >= 0.85
    min_items: 50

  regression_eval:
    pass_rate: >= 0.95
    all_critical: pass

  reliability:
    pass^3: >= 0.70  # all 3 trials pass 70% of time

  efficiency:
    p95_latency: < 30s
    p95_cost: < $0.50
```

When criteria met → deploy. Continue monitoring in production.

---

## Implementation Checklist

### Phase 1: Foundation

- [ ] Define quality dimensions for your agent's outputs
- [ ] Create initial dataset (20-50 items)
- [ ] Set up Langfuse project with tracing
- [ ] Create basic judges for each dimension
- [ ] Run first experiment, establish baseline

### Phase 2: Iteration Loop

- [ ] Analyze failures from experiment
- [ ] Investigate traces for root causes
- [ ] Identify systematic patterns
- [ ] Make targeted improvements
- [ ] Add failures to regression dataset
- [ ] Run experiment, compare to baseline

### Phase 3: Compounding

- [ ] Version prompts in Langfuse
- [ ] Track score trends over time
- [ ] Calibrate judges against human labels
- [ ] Document failure patterns
- [ ] Build component-level tests
- [ ] Establish graduation criteria

### Phase 4: Production

- [ ] Monitor production traces
- [ ] Alert on score regressions
- [ ] Feed production failures back to datasets
- [ ] Continue improvement cycles
- [ ] Track long-term capability growth

---

## Summary

AI agent dogfooding adapts the three-layer structure:

| Layer | Traditional Product | AI Agent |
|-------|---------------------|----------|
| Layer 1 | User experience | Output quality evaluation |
| Layer 2 | Code debugging | Trace analysis |
| Layer 3 | Infrastructure audit | Component verification |

The key differences:
- **Batch evaluation** instead of single journeys
- **Quantitative scores** instead of qualitative experience
- **Probabilistic metrics** (pass@k, pass^k) for non-determinism
- **Prompt changes** instead of code fixes

The unique opportunity:
- **Evaluation itself compounds** — datasets grow, judges improve
- **Version control for prompts** — track what works
- **Systematic debugging** via traces — not guesswork

The result: a self-improving system where each cycle makes both the agent AND the evaluation better.
