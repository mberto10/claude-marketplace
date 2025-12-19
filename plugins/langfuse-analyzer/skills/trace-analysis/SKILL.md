---
name: langfuse-trace-analysis
description: This skill should be used when the user says "analyze trace", "debug workflow", "why did this fail", "investigate issue", "trace shows wrong output", "output quality is bad", "missing data in output", "slow execution", or describes any problem with a workflow run. Combines Langfuse trace data with codebase investigation to find root causes and suggest fixes.
---

# Langfuse Trace Analysis

Agent-driven diagnostic analysis that bridges trace observations with codebase investigation. Produces structured reports with actionable fixes.

## Analysis Workflow

### Step 1: Retrieve the Trace

Use the data-retrieval skill to get trace data:

```bash
# Get trace with inputs/outputs (recommended for most analyses)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode io

# For performance issues, use flow mode
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode flow

# For LLM prompt quality issues, use prompts mode
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode prompts

# For full investigation with all metrics
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode full
```

### Step 2: Classify the Symptom

Map the user's description to an investigation strategy:

| Symptom Pattern | Category | Primary Investigation |
|-----------------|----------|----------------------|
| "missing data", "incomplete", "didn't include X" | `data_gap` | Data flow between steps |
| "wrong output", "incorrect result", "not expected" | `output_error` | Step logic and transformations |
| "failed", "error", "exception", "crashed" | `execution_error` | Error observations, stack traces |
| "slow", "took too long", "timeout" | `latency` | Step timing, external calls |
| "quality is bad", "not accurate", "poor results" | `quality_issue` | LLM prompts, input quality |
| "cost too high", "expensive", "too many tokens" | `cost` | Token usage, model selection |

### Step 3: Investigation Strategies

#### For `data_gap` (Missing Data)

**Trace Investigation:**
1. Find all step/span observations in order
2. Check: What data was passed as input to each step?
3. Check: What data was produced as output?
4. Identify where expected data disappears or never appears

**Key Questions:**
- Was the data source called? (API, database, tool)
- Did the source return data or empty/error?
- Was the data passed correctly between steps?
- Is there a transformation that dropped the data?

**Common Root Causes:**
- External API not called or returned empty
- Data filtering logic too restrictive
- State/context not passed between steps
- Missing input in LLM prompt template
- Upstream step silently failed

#### For `output_error` (Wrong Output)

**Trace Investigation:**
1. Find the step that produced incorrect output
2. Compare input vs output for that step
3. Check preceding steps for bad input data
4. Look for logic/prompt issues in the step

**Key Questions:**
- What input did the step receive?
- What was the expected output?
- What was the actual output?
- Is the logic/prompt correct for this input?

**Common Root Causes:**
- LLM prompt not specific enough
- Wrong step executed (conditional logic issue)
- Input data was already incorrect
- Model hallucination
- Missing context or examples

#### For `execution_error` (Failures/Crashes)

**Trace Investigation:**
1. Find observations with level: ERROR or status: ERROR
2. Check status_message and error fields
3. Find the last successful observation before failure
4. Look for stack traces in outputs

**Key Questions:**
- What was the error message?
- Which step failed?
- What input caused the failure?
- Is this a repeatable or intermittent issue?

**Common Root Causes:**
- API key missing or invalid
- Rate limiting / quota exceeded
- Malformed input data
- Network timeout
- Unhandled edge case in code
- External service unavailable

#### For `latency` (Performance Issues)

**Trace Investigation:**
1. Retrieve trace with `--mode flow` for timing data
2. Identify steps with longest duration
3. Check for sequential vs parallel execution
4. Look for retry patterns or multiple API calls

**Key Questions:**
- Which step(s) are slowest?
- Are external calls the bottleneck?
- Could steps run in parallel?
- Are there unnecessary retries?

**Common Root Causes:**
- Slow external API response
- Sequential execution of independent steps
- Large payload processing
- Excessive retries
- No caching of repeated calls
- Wrong model choice (larger than needed)

#### For `quality_issue` (Poor LLM Output)

**Trace Investigation:**
1. Retrieve trace with `--mode prompts` for LLM interactions
2. Examine the system prompt and user prompt
3. Check what context/examples were provided
4. Look at any scoring or validation observations

**Key Questions:**
- Is the prompt clear and specific?
- Was relevant context included?
- Were examples provided?
- Is the model appropriate for this task?

**Common Root Causes:**
- Vague or ambiguous prompt
- Missing context or examples
- Wrong model for the task
- Token limit truncating input
- Conflicting instructions in prompt

#### For `cost` (High Token Usage)

**Trace Investigation:**
1. Retrieve trace with `--mode full` for token metrics
2. Find steps with highest token usage
3. Check for redundant LLM calls
4. Look for large inputs that could be trimmed

**Key Questions:**
- Which steps use the most tokens?
- Are there unnecessary LLM calls?
- Could a smaller model be used?
- Is input being duplicated or repeated?

**Common Root Causes:**
- Overly large context windows
- Redundant LLM calls
- Using powerful model for simple tasks
- Verbose prompts that could be shortened
- No caching of repeated queries

### Step 4: Generate Report

Use the report generator:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/trace-analysis/helpers/report_generator.py \
  --symptom "user's original description" \
  --category <classified_category> \
  --trace-id <id> \
  --root-cause "identified root cause" \
  --evidence "Evidence from trace: ..." \
  --fix "Recommended fix with details"
```

Or format the report manually:

```markdown
# Trace Analysis Report

## Symptom
> [User's original description]

**Trace ID:** `<id>`
**Category:** `<classified_category>`

---

## Root Cause

[Clear explanation of what went wrong and why]

---

## Evidence

### From Trace

[Relevant excerpts from trace observations]

### From Code

[Relevant code snippets that contributed to the issue]

---

## Recommended Fixes

### Fix 1: [Title]

**File:** `path/to/file.py`

```diff
 def process_data(input):
-    result = transform(input)
+    result = transform(input, validate=True)
     return result
```

**Rationale:** [Why this fix addresses the root cause]

---

## Verification

After applying fixes:
1. Re-run the workflow with the same inputs
2. Retrieve new trace to verify fix
3. Confirm the issue is resolved
```

---

## Common Debugging Patterns

### Pattern: Compare Good vs Bad Traces

When you have working and broken cases:

```bash
# Get the failing trace
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <bad_id> --mode io

# Get a working trace for comparison
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <good_id> --mode io
```

Focus on differences:
- Input data variations
- Step execution order
- Conditional branches taken
- External call results

### Pattern: Find Similar Failures

Look for patterns across multiple traces:

```bash
# Get recent failing traces
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 10 --max-score 5.0 --mode minimal

# Investigate each to find common patterns
```

### Pattern: Trace Data Flow

For data_gap issues, trace data through each step:

1. Start at final output - what's missing?
2. Go back one step - was it in the input?
3. Continue backwards until you find where data disappears
4. Investigate that step's logic

### Pattern: Performance Profiling

For latency issues:

```bash
# Get timing breakdown
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode flow
```

Identify:
- Steps taking >50% of total time
- Steps that could run in parallel
- External calls that could be cached

---

## Codebase Investigation Tips

When trace analysis points to code issues:

1. **Locate the relevant code** - Use trace step names to find implementation files
2. **Check error handling** - Look for try/except blocks, error responses
3. **Trace data transformations** - Follow how input becomes output
4. **Check configuration** - Look for env vars, config files affecting behavior
5. **Review recent changes** - Git blame/log for recently modified code

---

## Tips for Effective Analysis

1. **Start with the trace** - Always retrieve trace data first before looking at code
2. **Follow the data flow** - Track data from input through each step to output
3. **Check both presence and content** - A step running doesn't mean it produced correct data
4. **Compare expected vs actual** - Know what should happen to identify divergence
5. **Look for the gap** - Find where expected behavior diverged from actual
6. **Consider timing** - Some issues only appear under load or with specific timing
