# Agent Evaluator Plugin Proposal

> A plugin for systematic AI agent evaluation using the three-layer dogfooding methodology.

## Overview

The `agent-evaluator` plugin applies the universal three-layer dogfooding structure to AI agents, leveraging Langfuse for tracing, datasets, experiments, and scoring.

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT-EVALUATOR PLUGIN                       │
│                                                                 │
│   /agent-dogfood "article-writer" --dataset articles_v1         │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │ Layer 1: OUTPUT QUALITY                                 │   │
│   │ → Run experiment on dataset                             │   │
│   │ → Score with judges                                     │   │
│   │ → Identify failures                                     │   │
│   └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │ Layer 2: BEHAVIOR ANALYSIS                              │   │
│   │ → Retrieve traces for failures                          │   │
│   │ → Investigate root causes                               │   │
│   │ → Compare good vs bad                                   │   │
│   └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │ Layer 3: COMPONENT VERIFICATION                         │   │
│   │ → Test tools in isolation                               │   │
│   │ → Verify retrieval quality                              │   │
│   │ → Audit prompts                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                          ↓                                      │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │ COMPOUND                                                │   │
│   │ → Add failures to dataset                               │   │
│   │ → Update judges if needed                               │   │
│   │ → Document patterns                                     │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Relationship to Existing Plugins

```
┌─────────────────────────────────────────────────────────────────┐
│                    PLUGIN ECOSYSTEM                             │
│                                                                 │
│  ┌─────────────────┐     ┌─────────────────┐                   │
│  │                 │     │                 │                   │
│  │  ux-evaluator   │     │ agent-evaluator │  ← NEW            │
│  │                 │     │                 │                   │
│  │  UI/Frontend    │     │  AI Agents      │                   │
│  │  Products       │     │                 │                   │
│  │                 │     │                 │                   │
│  └────────┬────────┘     └────────┬────────┘                   │
│           │                       │                             │
│           │   Same 3-layer        │                             │
│           │   structure           │                             │
│           │                       │                             │
│           ▼                       ▼                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              dogfooding-methodology.md                   │   │
│  │              (shared reference)                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────┐                                           │
│  │                 │                                           │
│  │langfuse-analyzer│ ← agent-evaluator USES these capabilities │
│  │                 │                                           │
│  │ • Traces        │                                           │
│  │ • Datasets      │                                           │
│  │ • Experiments   │                                           │
│  │ • Scores        │                                           │
│  │ • Prompts       │                                           │
│  │                 │                                           │
│  └─────────────────┘                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key insight:** `agent-evaluator` orchestrates the three-layer flow, while `langfuse-analyzer` provides the underlying capabilities.

---

## Plugin Structure

```
agent-evaluator/
├── .claude-plugin/
│   └── plugin.json
├── README.md
│
├── commands/
│   ├── agent-dogfood.md          # Full 3-layer evaluation
│   ├── agent-experiment.md       # Quick Layer 1 only
│   └── agent-setup.md            # Set up evaluation for new agent
│
├── agents/
│   ├── output-evaluator.md       # Layer 1: Run experiments, score
│   ├── failure-analyst.md        # Layer 2: Trace investigation
│   ├── component-auditor.md      # Layer 3: Component testing
│   └── eval-compounder.md        # Compound step
│
├── skills/
│   └── agent-eval-framework/
│       ├── SKILL.md
│       └── references/
│           ├── evaluation-dimensions.md
│           ├── judge-templates.md
│           ├── trace-patterns.md
│           └── component-tests.md
│
└── templates/
    ├── agent-config.yaml         # Config file template
    ├── judge-accuracy.md         # Judge prompt template
    ├── judge-completeness.md
    ├── judge-safety.md
    └── experiment-report.md      # Report template
```

---

## Commands

### `/agent-dogfood` — Full Three-Layer Evaluation

The main command that orchestrates all three layers.

```markdown
---
name: agent-dogfood
description: Run full three-layer dogfooding evaluation on an AI agent
allowed_tools:
  - Read
  - Glob
  - Grep
  - Write
  - AskUserQuestion
  - Task
  - Bash
arguments:
  - name: agent
    description: Name or path of the agent to evaluate
    required: true
  - name: dataset
    description: Langfuse dataset name to use
    required: false
  - name: depth
    description: Evaluation depth (quick/standard/full)
    required: false
---

# Agent Dogfood

Systematic evaluation of an AI agent using the three-layer methodology.

## Gather Context

1. **Agent identification**
   - Where is the agent code?
   - What is the entry point?
   - How do we invoke it?

2. **Evaluation setup**
   - Which dataset? (existing or create new)
   - Which judges? (existing or configure)
   - What thresholds? (pass criteria)

3. **Depth selection**
   - Quick: Layer 1 only (experiment + scores)
   - Standard: Layers 1 + 2 (+ failure analysis)
   - Full: All three layers (+ component audit)

## Execution

### Layer 1: Output Quality Evaluation

Launch `output-evaluator` agent:
- Run agent on each dataset item
- Score outputs with configured judges
- Calculate pass rates and distributions
- Identify failures (below threshold)

**Output:** Experiment results, failure list

### Layer 2: Behavior Analysis (if standard or full)

Launch `failure-analyst` agent with failure list:
- Retrieve Langfuse traces for each failure
- Investigate root causes
- Compare successful vs failed traces
- Classify failure patterns

**Output:** Root cause analysis, recommendations

### Layer 3: Component Verification (if full)

Launch `component-auditor` agent with problem areas:
- Test tools in isolation
- Verify retrieval quality
- Audit prompt effectiveness
- Check state management

**Output:** Component audit report

### Compound (optional)

Ask user: "Run compound step to encode learnings?"

If yes, launch `eval-compounder` agent:
- Add failures to regression dataset
- Calibrate/update judges if needed
- Document failure patterns
- Track improvement metrics

## Output

Generate comprehensive report:
- Executive summary
- Score distributions
- Failure analysis
- Recommendations (prioritized)
- Component issues (if full)
- Next steps
```

### `/agent-experiment` — Quick Layer 1

Fast evaluation without deep analysis.

```markdown
---
name: agent-experiment
description: Quick experiment run - Layer 1 only
allowed_tools:
  - Read
  - Glob
  - Grep
  - Write
  - AskUserQuestion
  - Task
  - Bash
arguments:
  - name: agent
    description: Agent to evaluate
    required: true
  - name: dataset
    description: Dataset to use
    required: true
---

# Quick Experiment

Run agent on dataset and score outputs. No deep analysis.

## Process

1. Load agent configuration
2. Load or verify dataset exists
3. Run experiment (agent on each item, k trials)
4. Score with judges
5. Report results

## Output

- Pass rates (pass@k, pass^k)
- Score distributions per dimension
- Failure list (for manual review or later analysis)
- Comparison to previous run (if exists)
```

### `/agent-setup` — Initialize Evaluation

Set up evaluation infrastructure for a new agent.

```markdown
---
name: agent-setup
description: Set up evaluation for a new AI agent
allowed_tools:
  - Read
  - Glob
  - Grep
  - Write
  - AskUserQuestion
  - Task
  - Bash
---

# Agent Evaluation Setup

Interactive wizard to configure evaluation for a new agent.

## Steps

### 1. Agent Discovery
- Where is the agent code?
- What does it do? (purpose, inputs, outputs)
- How is it invoked?

### 2. Quality Dimensions
- What makes a good output?
- Define 3-5 measurable dimensions
- Set thresholds for each

### 3. Create Judges
For each dimension:
- Code-based (programmatic check) or model-based (LLM judge)?
- If model-based, create judge prompt in Langfuse
- Define scoring scale and rubric

### 4. Create Dataset
- Start with 20-50 items
- Include: happy path, edge cases, adversarial
- Balance: should-succeed AND should-fail cases

### 5. Generate Config
Create `.claude/agent-eval.yaml`:
```yaml
agent:
  name: article-writer
  entry: src/agents/article_writer.py
  invoke: "python -m agents.article_writer"

evaluation:
  dataset: article_writer_v1
  trials_per_item: 3

  dimensions:
    - name: accuracy
      type: llm
      judge: langfuse://prompts/judge-accuracy
      threshold: 7.0
      weight: 0.3

    - name: completeness
      type: programmatic
      check: "all_sections_present"
      threshold: 1.0
      weight: 0.2

    - name: style
      type: llm
      judge: langfuse://prompts/judge-style
      threshold: 7.0
      weight: 0.3

    - name: safety
      type: llm
      judge: langfuse://prompts/judge-safety
      threshold: 9.0
      weight: 0.2

  pass_criteria:
    overall: 7.5
    all_dimensions_above: 6.0
    safety_minimum: 9.0
```

### 6. Verify Setup
- Run single item test
- Confirm judges work
- Confirm tracing enabled
```

---

## Agents

### `output-evaluator` — Layer 1

```markdown
---
name: output-evaluator
description: Run experiments and score agent outputs. Layer 1 of agent dogfooding.
color: green
tools:
  - Read
  - Glob
  - Grep
  - Write
  - Bash
model: sonnet
---

# Output Evaluator

You evaluate AI agent outputs by running experiments and applying judges.

## Input

- Agent configuration (how to invoke)
- Dataset name in Langfuse
- Judge configurations
- Number of trials (k)

## Process

### 1. Load Dataset
Fetch items from Langfuse dataset.

### 2. Run Agent
For each item, run agent k times:
```python
for item in dataset:
    outputs = []
    for trial in range(k):
        output = run_agent(item.input)
        trace_id = capture_trace()
        outputs.append((output, trace_id))
```

### 3. Apply Judges
For each output, apply all judges:
```python
for output, trace_id in outputs:
    scores = {}
    for judge in judges:
        if judge.type == "programmatic":
            scores[judge.name] = run_programmatic(judge, output)
        elif judge.type == "llm":
            scores[judge.name] = run_llm_judge(judge, item, output)
    record_scores(trace_id, scores)
```

### 4. Calculate Metrics
- Pass rate per dimension
- Overall pass rate (weighted)
- pass@k: P(at least one success)
- pass^k: P(all trials succeed)
- Score distributions (mean, p50, p95)

### 5. Identify Failures
Items where:
- Any dimension below threshold
- Overall score below pass criteria
- Safety below minimum

## Output

```markdown
# Experiment Results: [agent] on [dataset]

## Summary
- Items: N
- Trials per item: k
- Total runs: N × k

## Scores by Dimension
| Dimension | Mean | P50 | P95 | Pass Rate |
|-----------|------|-----|-----|-----------|
| accuracy | X.X | X.X | X.X | XX% |
| ... | ... | ... | ... | ... |

## Pass Metrics
- pass@k: XX%
- pass^k: XX%
- Overall pass rate: XX%

## Failures (N items)
| Item | Scores | Primary Issue |
|------|--------|---------------|
| item_001 | acc=3, comp=8 | Low accuracy |
| ... | ... | ... |

## vs Previous Run
| Dimension | Previous | Current | Delta |
|-----------|----------|---------|-------|
| accuracy | X.X | X.X | +X.X |
| ... | ... | ... | ... |
```
```

### `failure-analyst` — Layer 2

```markdown
---
name: failure-analyst
description: Analyze failed agent runs by investigating traces. Layer 2 of agent dogfooding.
color: yellow
tools:
  - Read
  - Glob
  - Grep
  - Write
  - Bash
model: opus
---

# Failure Analyst

You investigate why AI agents fail by analyzing execution traces.

## Input

- Failure list from Layer 1 (items, scores, trace IDs)
- Agent codebase location
- Access to Langfuse traces

## Process

### 1. Retrieve Traces
For each failure, fetch full trace from Langfuse:
- All LLM calls (prompts, responses)
- Tool invocations (inputs, outputs)
- Timing information
- Any logged metadata

### 2. Classify Symptom
Categorize the failure:
- **Output error**: Wrong content produced
- **Data gap**: Missing information in output
- **Quality issue**: Correct but poor quality
- **Execution error**: Crashed or incomplete
- **Safety issue**: Inappropriate content

### 3. Investigate Root Cause

**For output errors:**
1. Find step that produced wrong output
2. Check input to that step
3. Check prompt/instructions
4. Check model response

**For data gaps:**
1. Trace backward from output
2. Find where data should have come from
3. Check retrieval/tool calls
4. Check filtering logic

**For quality issues:**
1. Compare to high-scoring output
2. Identify differences in reasoning
3. Check prompt emphasis
4. Check revision steps

### 4. Compare Good vs Bad
Find successful run on similar input:
- Diff the traces
- Identify divergence point
- Understand what worked vs failed

### 5. Identify Patterns
Group failures by root cause:
- Same component failing?
- Same prompt issue?
- Same tool problem?

## Output

```markdown
# Failure Analysis: [agent]

## Failure Summary
- Total failures: N
- Unique patterns: M

## Pattern 1: [Name]

**Affected items:** X/N (Y%)
**Symptom:** [Description]

**Trace Pattern:**
```
Input → Step A (OK)
     → Step B (OK)
     → Step C ← FAILURE POINT
     → Output (degraded)
```

**Root Cause:**
[Specific explanation with evidence from traces]

**Evidence:**
- Trace item_023: [specific observation]
- Trace item_041: [specific observation]

**Recommended Fix:**
[Actionable recommendation]

**Complexity:** [Low/Medium/High]

---

## Pattern 2: [Name]
...

---

## Recommendations (Prioritized)

1. **[Fix]** — Addresses patterns 1, 3 — [Complexity]
2. **[Fix]** — Addresses pattern 2 — [Complexity]
...

## Components to Audit
Based on failure patterns, recommend Layer 3 audit for:
- [ ] [Component]: [Why]
- [ ] [Component]: [Why]
```
```

### `component-auditor` — Layer 3

```markdown
---
name: component-auditor
description: Verify agent components work correctly in isolation. Layer 3 of agent dogfooding.
color: red
tools:
  - Read
  - Glob
  - Grep
  - Write
  - Bash
model: sonnet
---

# Component Auditor

You verify that individual agent components work correctly.

## Input

- Components to audit (from Layer 2 recommendations)
- Component code locations
- Test cases to run

## Components to Verify

### Tools
External capabilities the agent invokes.

**Tests:**
- Known input → expected output
- Error handling (bad input, timeout, etc.)
- Edge cases
- Performance bounds

### Retrieval
Context/knowledge retrieval systems.

**Tests:**
- Relevance: Does it find relevant content?
- Recall: Does it find ALL relevant content?
- Precision: Is noise filtered?
- Chunk quality: Right granularity?

### Prompts
Instructions that guide LLM behavior.

**Tests:**
- Clarity: Are instructions unambiguous?
- Completeness: Are edge cases covered?
- Examples: Do they demonstrate expected behavior?
- Output format: Is it specified clearly?

### State Management
Context passing between steps.

**Tests:**
- State preserved between steps
- No data loss in serialization
- Context window not exceeded
- Memory correctly maintained

## Output

```markdown
# Component Audit: [agent]

## Tool: [name]

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Basic query | X | X | ✓ PASS |
| Error handling | graceful | throws | ✗ FAIL |
| ... | ... | ... | ... |

**Issues:**
- [Issue description]

**Recommendation:**
- [Fix]

---

## Retrieval: [name]

| Test | Expected | Actual | Status |
|------|----------|--------|--------|
| Relevance | >0.8 | 0.72 | ⚠ WARN |
| ... | ... | ... | ... |

---

## Prompt: [name]

**Clarity check:** [Assessment]
**Missing cases:** [List]
**Recommendation:** [Fix]

---

## Summary

| Component | Status | Priority |
|-----------|--------|----------|
| tool_research | ✗ FAIL | High |
| retrieval_docs | ⚠ WARN | Medium |
| prompt_draft | ✓ PASS | - |

## Implementation Checklist

1. [ ] [Fix] — [Component] — [Priority]
2. [ ] [Fix] — [Component] — [Priority]
```
```

### `eval-compounder` — Compound Step

```markdown
---
name: eval-compounder
description: Encode learnings from evaluation cycle. Compound step of agent dogfooding.
color: magenta
tools:
  - Read
  - Glob
  - Grep
  - Write
  - Bash
  - AskUserQuestion
model: sonnet
---

# Evaluation Compounder

You extract and encode learnings from agent evaluation cycles.

## Input

- Experiment results (Layer 1)
- Failure analysis (Layer 2)
- Component audit (Layer 3, if run)
- Current agent configuration

## Process

### 1. Identify Compoundable Learnings

For each finding, evaluate:

**Value filter:**
```
value = recurrence × impact × half-life - encoding_cost
```

| Factor | Score 1-5 | Question |
|--------|-----------|----------|
| Recurrence | | Will this come up again? |
| Impact | | How much does it matter? |
| Half-life | | How long will this be relevant? |
| Encoding cost | | How hard to encode? |

If value > threshold → encode

### 2. Classify Destination

| Learning Type | Destination |
|--------------|-------------|
| Test case | Langfuse dataset |
| Judge improvement | Langfuse prompt update |
| Agent prompt fix | Langfuse prompt update |
| Component fix | Code change recommendation |
| Failure pattern | Documentation |

### 3. Execute Encoding

**Add failures to dataset:**
- Select failures worth preserving as regression tests
- Add to Langfuse dataset with metadata
- Mark expected output (what it should have produced)

**Update judges (if needed):**
- If judge missed issues → refine rubric
- If judge was too strict → adjust threshold
- Create new version in Langfuse

**Document patterns:**
- Add to trace-patterns.md reference
- Include: symptom, cause, fix

### 4. Track Progress

Record in evaluation history:
- Date, agent version, dataset version
- Scores (for trend tracking)
- Changes made
- Learnings encoded

## Output

```markdown
# Compound Report: [agent] evaluation [date]

## Learnings Encoded

### 1. [Learning]
- **Type:** Test case
- **Destination:** Dataset [name]
- **Value:** recurrence(4) × impact(5) × half-life(5) / cost(2) = 50
- **Action:** Added item_023, item_041 failures as regression tests

### 2. [Learning]
- **Type:** Judge improvement
- **Destination:** Langfuse prompt judge-accuracy
- **Value:** recurrence(5) × impact(4) × half-life(5) / cost(3) = 33
- **Action:** Added rubric for technical accuracy verification

### 3. [Learning]
- **Type:** Pattern documentation
- **Destination:** trace-patterns.md
- **Value:** recurrence(3) × impact(4) × half-life(4) / cost(1) = 48
- **Action:** Documented "research query too narrow" pattern

## Not Encoded (kept as observations)
- [Finding]: value = X (below threshold)

## Progress Tracking

| Metric | Previous | Current | Trend |
|--------|----------|---------|-------|
| Dataset size | 50 | 52 | +2 |
| Pass rate | 78% | 85% | +7% |
| Failure patterns documented | 5 | 7 | +2 |

## Recommendations for Next Cycle
1. [Recommendation]
2. [Recommendation]
```
```

---

## Integration with langfuse-analyzer

The `agent-evaluator` plugin uses `langfuse-analyzer` capabilities:

| agent-evaluator needs | langfuse-analyzer provides |
|-----------------------|---------------------------|
| Run experiments | experiment-runner skill |
| Retrieve traces | data-retrieval skill |
| Analyze traces | trace-analysis skill |
| Manage datasets | dataset-management skill |
| Track scores | score-analytics skill |
| Version prompts | prompt-management skill |

**Implementation approach:**

The agents in `agent-evaluator` invoke `langfuse-analyzer` skills via the Task tool:

```markdown
# In output-evaluator agent

To run the experiment, invoke the langfuse experiment runner:

Use Task tool with subagent_type="langfuse-analyzer" and prompt:
"Run experiment on dataset [X] with task script [Y] and evaluators [Z]"
```

Or, the commands can directly use `langfuse-analyzer` skills in their allowed_tools:

```yaml
allowed_tools:
  - Read
  - Write
  - Skill  # To invoke langfuse-analyzer skills
```

---

## Configuration

### Agent Evaluation Config (`.claude/agent-eval.yaml`)

```yaml
# Agent definition
agent:
  name: article-writer
  description: "Writes articles on given topics"
  entry_point: src/agents/article_writer.py
  invoke_command: "python -m agents.article_writer --input '{input}'"

# Langfuse connection
langfuse:
  project: my-project
  # Keys from environment: LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY

# Evaluation configuration
evaluation:
  # Dataset to use
  dataset: article_writer_v1

  # Trials per item (for non-determinism)
  trials: 3

  # Quality dimensions
  dimensions:
    - name: accuracy
      description: "Factual correctness"
      type: llm
      judge_prompt: langfuse://prompts/judge-accuracy@production
      threshold: 7.0
      scale: [0, 10]
      weight: 0.3

    - name: completeness
      description: "All sections present"
      type: programmatic
      check: |
        def check(output, expected):
            required = expected.get('sections', [])
            return all(s in output for s in required)
      threshold: 1.0
      weight: 0.2

    - name: style
      description: "Matches style guide"
      type: llm
      judge_prompt: langfuse://prompts/judge-style@production
      threshold: 7.0
      scale: [0, 10]
      weight: 0.3

    - name: safety
      description: "No harmful content"
      type: llm
      judge_prompt: langfuse://prompts/judge-safety@production
      threshold: 9.0
      scale: [0, 10]
      weight: 0.2
      critical: true  # Failure here fails entire item

  # Pass criteria
  pass_criteria:
    overall_minimum: 7.0
    all_dimensions_minimum: 5.0
    critical_dimensions_minimum: 9.0

  # Metrics to track
  metrics:
    - pass_at_k
    - pass_power_k
    - score_mean
    - score_p50
    - score_p95

# Compounding configuration
compound:
  # Where to add regression tests
  regression_dataset: article_writer_regression

  # Pattern documentation
  patterns_file: docs/failure-patterns.md

  # Value threshold for encoding
  value_threshold: 20
```

---

## Workflow Example

```
User: /agent-dogfood article-writer --dataset articles_v1 --depth full

Claude: I'll run a full three-layer evaluation on the article-writer agent.

## Layer 1: Output Quality

Running experiment on articles_v1 dataset (50 items, 3 trials each)...

[Launches output-evaluator agent]

Results:
- Overall pass rate: 78%
- pass@3: 92%
- pass^3: 58%

| Dimension | Mean | Pass Rate |
|-----------|------|-----------|
| accuracy | 7.2 | 78% |
| completeness | 8.5 | 92% |
| style | 6.8 | 70% |
| safety | 9.9 | 100% |

11 items failed. Proceeding to Layer 2...

## Layer 2: Behavior Analysis

Analyzing failures...

[Launches failure-analyst agent]

Found 3 failure patterns:

1. **Research Too Narrow** (6 items)
   - Root cause: Single query misses relevant sources
   - Fix: Add query expansion step

2. **Style Drift in Long Articles** (4 items)
   - Root cause: No style enforcement after initial draft
   - Fix: Add style revision pass

3. **Missing Section** (1 item)
   - Root cause: Context window truncated outline
   - Fix: Chunk long outlines

Proceeding to Layer 3...

## Layer 3: Component Verification

Auditing flagged components...

[Launches component-auditor agent]

| Component | Status | Issue |
|-----------|--------|-------|
| research_tool | ⚠ WARN | Single query, no expansion |
| style_guide_retrieval | ✓ PASS | - |
| section_writer | ✗ FAIL | Truncates at 1000 words |

## Recommendations

1. **Add query expansion** — High priority, addresses 6 failures
2. **Add style revision pass** — Medium priority, addresses 4 failures
3. **Fix section writer truncation** — Medium priority, addresses 1 failure

## Compound Step

Would you like to encode learnings from this cycle?
- Add 11 failures to regression dataset
- Document 3 failure patterns
- Update evaluation config

User: yes

[Launches eval-compounder agent]

Encoded:
- Added 11 items to article_writer_regression dataset
- Documented patterns in failure-patterns.md
- Updated judge-accuracy prompt to check source diversity

Next cycle ready. Run /agent-experiment to test after fixes.
```

---

## Summary

The `agent-evaluator` plugin provides:

1. **Structured evaluation** — Three-layer methodology for AI agents
2. **Langfuse integration** — Uses existing tracing/dataset/experiment infrastructure
3. **Systematic debugging** — Trace-based failure analysis
4. **Component testing** — Verify building blocks work
5. **Compounding** — Learnings encoded for future cycles

The plugin orchestrates the flow while leveraging `langfuse-analyzer` for underlying capabilities. This avoids duplication and maintains a clean separation of concerns.
