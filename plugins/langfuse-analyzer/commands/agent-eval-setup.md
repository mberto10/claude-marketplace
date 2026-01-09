---
name: agent-eval-setup
description: Set up AI agent evaluation - explore codebase, infer quality dimensions, configure dataset and judges
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
    description: Agent name or path to explore
    required: false
---

# Agent Evaluation Setup

Set up evaluation infrastructure for an AI agent through codebase exploration.

---

## Phase 1: Deep Codebase Exploration

### 1.1 Discover Agent

Find and understand the agent:

```
Search for:
- Agent entry points, main files
- Class/function definitions with "agent" in name
- LangGraph/LangChain agent patterns
- Claude Code agent definitions
```

**Document:**
- Entry point location
- How to invoke
- Framework used (if any)

### 1.2 Map Agent Flow

Trace the execution flow:

```
From entry point, follow:
- What LLM calls are made? (prompts, models)
- What tools/functions are available?
- What retrieval/context is used?
- What is the decision/routing logic?
```

**Document:**
- Flow diagram (conceptual)
- Each step and its purpose
- Decision points

### 1.3 Analyze Prompts

Find and analyze all prompts:

```
Search for:
- Prompt templates (strings, files, Langfuse)
- System messages
- Few-shot examples
- Output format instructions
```

**Document:**
- Each prompt's purpose
- Variables/context used
- Quality expectations embedded in prompts

### 1.4 Understand Inputs/Outputs

From code and prompts, determine:

```
Inputs:
- What does the agent receive?
- What format?
- What variations?

Outputs:
- What does it produce?
- What format?
- What makes output "good" (from prompt instructions)?
```

### 1.5 Identify Quality Dimensions

**Infer from prompts and code** what quality dimensions matter:

```
Look for:
- Accuracy/correctness instructions
- Completeness requirements
- Style/tone guidance
- Safety/filtering logic
- Format requirements
- Speed/efficiency concerns
```

Most agents have quality expectations baked into their prompts. Extract these.

### 1.6 Find Existing Evaluation

Check for existing eval infrastructure:

```
Search for:
- Test files
- Eval scripts
- Langfuse datasets
- Judge prompts
- Benchmark data
```

---

## Phase 2: Present Findings

After exploration, present what was discovered:

```markdown
## Agent Analysis: [name]

### Overview
[Brief description of what agent does]

### Entry Point
- Location: [path]
- Invocation: [how to run]

### Flow
[Conceptual flow of agent execution]

### Components
| Component | Location | Purpose |
|-----------|----------|---------|
| [prompt] | [path] | [purpose] |
| [tool] | [path] | [purpose] |

### Inferred Quality Dimensions
Based on prompt instructions and code:

| Dimension | Source | Inferred Criteria |
|-----------|--------|-------------------|
| [accuracy] | [prompt X] | "[exact instruction from prompt]" |
| [completeness] | [prompt Y] | "[exact instruction from prompt]" |

### Existing Evaluation
[What was found, or "None found"]
```

---

## Phase 3: Targeted Questions

Only ask what **cannot be inferred** from codebase:

### 3.1 Confirm or Adjust Dimensions

```
Based on the codebase, I identified these quality dimensions:
1. [dimension]: [inferred criteria]
2. [dimension]: [inferred criteria]

Questions:
- Are these the right dimensions to evaluate?
- Any dimensions to add or remove?
- What are the priority weights? (or equal weight)
```

### 3.2 Thresholds

```
For each dimension, what score threshold means "pass"?
(Scale 0-10, or specify different scale)

- [dimension 1]: [suggest based on criticality]
- [dimension 2]: [suggest based on criticality]

Are any dimensions critical (must always pass regardless of overall score)?
```

### 3.3 Dataset Source

```
For the evaluation dataset, I can:
1. Pull from existing Langfuse traces (if available)
2. Use existing test cases (if found: [location])
3. Generate synthetic test cases
4. You provide test cases

Which approach? Or combination?
```

### 3.4 Known Problem Areas (optional)

```
Are there specific scenarios or inputs you know are problematic?
(These should be included in the dataset)
```

That's it. No other questions needed.

---

## Phase 4: Configure Components

### 4.1 Create Dataset

Based on answers, invoke appropriate skill:

**If pulling from Langfuse traces:**
- Use `langfuse-data-retrieval` to find relevant traces
- Use `langfuse-dataset-management` to create dataset from traces

**If using existing test cases:**
- Read test files
- Convert to Langfuse dataset format
- Upload via `langfuse-dataset-management`

**If generating synthetic:**
- Based on input patterns discovered
- Generate diverse test cases
- Include edge cases based on known problem areas

**Target:** 20-50 items covering:
- Typical inputs
- Edge cases
- Known problem areas (if provided)

### 4.2 Create Judges

For each confirmed dimension:

**Generate judge prompt based on inferred criteria:**

```markdown
## Judge: [Dimension]

Evaluate the [dimension] of this agent output.

### Criteria
[Use the exact criteria extracted from agent prompts]

### Input
**User Input:** {{input}}
**Agent Output:** {{output}}

### Scoring (0-10)
- 10: [specific criteria for excellent]
- 7-9: [good]
- 4-6: [acceptable]
- 1-3: [poor]
- 0: [complete failure]

Provide score and brief reasoning.
```

Use `langfuse-prompt-management` to create judge prompts in Langfuse.

### 4.3 Generate Config

Create `.claude/agent-eval/{agent}.yaml`:

```yaml
agent:
  name: "[name]"
  path: "[discovered path]"
  entry_point: "[discovered invocation]"

  components:
    prompts: [list from exploration]
    tools: [list from exploration]

evaluation:
  dataset: "[created dataset name]"

  dimensions:
    - name: "[dimension]"
      judge: "langfuse://prompts/judge-[dimension]"
      threshold: [from user]
      weight: [from user]
      critical: [true/false]

  pass_criteria:
    overall: [calculated from weights/thresholds]

output:
  linear_project: "[if available]"
  local_path: ".claude/agent-eval/[agent]/reports/"
```

---

## Phase 5: Validate

### Smoke Test

Run single item through pipeline:
1. Invoke agent
2. Verify trace captured
3. Apply judges
4. Verify scores recorded

If passes → setup complete.

---

## Output

```markdown
# Setup Complete: [agent]

## Configuration
- Config: .claude/agent-eval/[agent].yaml
- Dataset: [name] ([N] items)
- Judges: [list]

## Quality Dimensions
| Dimension | Threshold | Weight | Critical |
|-----------|-----------|--------|----------|
| [name] | [X] | [X] | [yes/no] |

## Ready
Run `/agent-eval [agent]` to start evaluation.
```
