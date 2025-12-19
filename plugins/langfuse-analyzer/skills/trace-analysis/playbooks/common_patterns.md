# Common Trace Analysis Patterns

Quick-reference playbook for common debugging scenarios in Langfuse-traced applications.

---

## Finding Failed Steps

Quickly identify what went wrong in a trace:

```bash
# Get trace with full details
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode io
```

**What to look for:**
- Observations with `level: ERROR` or `status: ERROR`
- `status_message` fields containing error details
- Steps with empty or null outputs
- Stack traces in output fields

**Investigation steps:**
1. Find the first error observation
2. Check the input to that step
3. Look at the preceding step's output
4. Identify whether the error is in input data or step logic

---

## Performance Bottlenecks

Find what's making your workflow slow:

```bash
# Get timing breakdown
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode flow
```

**What to look for:**
- Steps with duration > 50% of total time
- Sequential steps that could run in parallel
- Repeated API calls that could be cached
- Retry patterns indicating instability

**Quick wins:**
- Parallelize independent steps
- Add caching for repeated external calls
- Use smaller models for simple tasks
- Batch API calls where possible

---

## Data Loss Between Steps

Track where data disappears:

```bash
# Get full input/output flow
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode io
```

**Investigation technique:**
1. Start from the final output - what's missing?
2. Work backwards step by step
3. For each step, compare output vs expected
4. Find where the data was lost or never appeared

**Common causes:**
- Step didn't receive data in input
- Data was filtered/transformed incorrectly
- External API returned empty
- State not passed between steps
- LLM prompt template missing placeholder

---

## LLM Quality Issues

Debug poor LLM outputs:

```bash
# Focus on LLM interactions
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode prompts
```

**What to analyze:**
- System prompt clarity and specificity
- User prompt content and structure
- Context/examples provided
- Model used (appropriate for task?)
- Token usage (truncation issues?)

**Improvement checklist:**
- [ ] Is the task clearly stated?
- [ ] Are constraints specific (format, length, style)?
- [ ] Is relevant context included?
- [ ] Are examples provided for complex tasks?
- [ ] Is the model appropriate (not over/underpowered)?

---

## Comparing Good vs Bad Traces

When something worked before but now fails:

```bash
# Get the failing trace
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <failing_id> --mode io

# Get a working trace
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <working_id> --mode io
```

**Comparison points:**
| Aspect | Good Trace | Bad Trace | Difference |
|--------|------------|-----------|------------|
| Input | | | |
| Step order | | | |
| API responses | | | |
| LLM output | | | |
| Final result | | | |

**Focus areas:**
- Different input data
- Missing or extra steps
- Different conditional branches
- Changed external responses
- Model/prompt differences

---

## Finding Traces by Score

Identify systematic quality issues:

```bash
# Find low-scoring traces
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 20 --max-score 5.0 --mode minimal

# Find high-quality examples for comparison
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 10 --min-score 9.0 --mode minimal

# Filter by custom score name
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 10 --min-score 8.0 --score-name accuracy_score
```

**Pattern analysis:**
1. Get a sample of low-scoring traces
2. Identify common characteristics:
   - Same input patterns?
   - Same step failures?
   - Same time of day?
   - Same external API issues?
3. Compare with high-scoring traces
4. Document the pattern for targeted fix

---

## Filtering by Metadata

Find traces for specific contexts:

```bash
# By project/environment
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 10 --filter-field environment --filter-value production

# By user or tenant
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 5 --filter-field user_id --filter-value user_123

# By workflow type
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 10 --filter-field workflow_name --filter-value checkout

# By tags
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 10 --tags production high-priority
```

---

## Building Regression Datasets

Create test sets from problematic traces:

```bash
# Step 1: Find failing traces
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 30 --max-score 6.0 --mode minimal

# Step 2: Create regression dataset
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dataset-management/helpers/dataset_manager.py \
  create \
  --name "workflow_regressions" \
  --description "Failing traces for regression testing"

# Step 3: Add trace IDs to file
echo "trace_id_1
trace_id_2
trace_id_3" > failing_traces.txt

# Step 4: Batch add to dataset
python3 ${CLAUDE_PLUGIN_ROOT}/skills/dataset-management/helpers/dataset_manager.py \
  add-batch \
  --dataset "workflow_regressions" \
  --trace-file failing_traces.txt \
  --expected-score 9.0
```

---

## Quick Diagnostic Commands

### Check latest trace
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 1 --mode io
```

### List recent failures
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --last 10 --max-score 5.0 --mode minimal
```

### Get specific trace with timing
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode flow
```

### Full investigation mode
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/trace_retriever.py \
  --trace-id <id> --mode full
```

### Test Langfuse connection
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/data-retrieval/helpers/langfuse_client.py
```

---

## Report Generation

Generate structured analysis report:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/trace-analysis/helpers/report_generator.py \
  --symptom "User's description of the problem" \
  --category data_gap \
  --trace-id <id> \
  --root-cause "Identified cause" \
  --evidence "Supporting evidence from trace" \
  --fix "Recommended fix"
```

**Categories:**
- `data_gap` - Missing or incomplete data
- `output_error` - Wrong or unexpected output
- `execution_error` - Failures and crashes
- `latency` - Performance issues
- `quality_issue` - Poor LLM output quality
- `cost` - High token/resource usage
