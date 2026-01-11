# Annotation Workflows

Quick-reference playbook for common human annotation patterns.

---

## Workflow 1: Daily Review Queue

Process traces that need human review on a regular basis.

### Setup

Create a score configuration in Langfuse UI:
- **Name:** `human_review`
- **Type:** NUMERIC
- **Range:** 0-10

### Daily Workflow

```bash
# 1. Find traces needing review (last 24 hours)
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  pending --score-name "human_review" --days 1 --limit 20

# 2. For each trace, view details using trace-analysis skill
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --trace-id "<trace-id>" --mode io

# 3. Add score based on review
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-id>" \
  --name "human_review" \
  --value 8.5 \
  --comment "Good response, addressed user query well"
```

### Scoring Guidelines

| Score | Description |
|-------|-------------|
| 9-10 | Excellent: Perfect response, no improvements needed |
| 7-8 | Good: Solid response with minor issues |
| 5-6 | Acceptable: Adequate but could be improved |
| 3-4 | Poor: Significant issues, needs attention |
| 0-2 | Unacceptable: Major problems, investigate |

---

## Workflow 2: Issue Classification

Categorize traces by issue type for analysis.

### Categories

Define categories for your use case:
- `no_issue` - Response was correct
- `factual_error` - Incorrect information
- `hallucination` - Made up information
- `incomplete` - Missing important details
- `off_topic` - Didn't address the question
- `safety_concern` - Potentially harmful content

### Workflow

```bash
# 1. Find traces to classify
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  pending --score-name "issue_type" --days 7 --limit 30

# 2. Review and classify each trace
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-id>" \
  --name "issue_type" \
  --string-value "factual_error" \
  --data-type CATEGORICAL \
  --comment "Stated incorrect date for the event"

# 3. Export for analysis
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  export --score-name "issue_type" --days 30 --format csv --output issues.csv
```

---

## Workflow 3: QA Pass/Fail

Binary quality check for production traces.

### Workflow

```bash
# 1. Find traces needing QA
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  pending --score-name "qa_passed" --days 3 --trace-name "production-chat"

# 2. Mark as passed
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-id>" \
  --name "qa_passed" \
  --value 1 \
  --data-type BOOLEAN

# 3. Mark as failed with reason
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-id>" \
  --name "qa_passed" \
  --value 0 \
  --data-type BOOLEAN \
  --comment "Response contained incorrect pricing information"

# 4. Track pass rate with score-analytics
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  summary --score-name "qa_passed" --days 7
```

---

## Workflow 4: Multi-Dimension Evaluation

Rate traces on multiple quality dimensions.

### Dimensions

| Dimension | Description | Scale |
|-----------|-------------|-------|
| accuracy | Factual correctness | 0-10 |
| helpfulness | How useful the response was | 0-10 |
| safety | Appropriate and safe content | 0-10 |
| tone | Professional and appropriate tone | 0-10 |

### Workflow

```bash
# For each trace, add multiple scores

# Accuracy
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score --trace-id "<trace-id>" --name "accuracy" --value 9.0

# Helpfulness
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score --trace-id "<trace-id>" --name "helpfulness" --value 8.5

# Safety
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score --trace-id "<trace-id>" --name "safety" --value 10.0

# Tone
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score --trace-id "<trace-id>" --name "tone" --value 8.0

# Compare dimensions over time
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  summary --score-name "accuracy" --days 14

python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  summary --score-name "helpfulness" --days 14
```

---

## Workflow 5: Comparative Labeling

Compare responses and pick the better one (for preference tuning).

### Workflow

```bash
# 1. Create comparison scores
# response_a better
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-a-id>" \
  --name "comparison_winner" \
  --string-value "a" \
  --data-type CATEGORICAL

# response_b better
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-b-id>" \
  --name "comparison_winner" \
  --string-value "b" \
  --data-type CATEGORICAL

# tie
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-id>" \
  --name "comparison_winner" \
  --string-value "tie" \
  --data-type CATEGORICAL \
  --comment "Both responses equally good"
```

---

## Workflow 6: Session-Level Annotation

Annotate entire sessions rather than individual traces.

### Workflow

```bash
# 1. Find sessions to review
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  find-issues --days 3 --min-turns 5

# 2. Analyze session quality
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  analyze --session-id "<session-id>"

# 3. View timeline for context
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  timeline --session-id "<session-id>"

# 4. Annotate key traces in the session
# Mark the final response quality
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<final-trace-id>" \
  --name "session_outcome" \
  --string-value "resolved" \
  --data-type CATEGORICAL \
  --comment "User's question was fully answered"
```

### Session Outcome Categories

- `resolved` - User goal achieved
- `unresolved` - User goal not met
- `escalated` - Required human intervention
- `abandoned` - User left before resolution

---

## Workflow 7: Error Investigation

Deep-dive into traces with low scores or errors.

### Workflow

```bash
# 1. Find low-scoring traces
python3 ~/.codex/skills/langfuse-score-analytics/scripts/score_analyzer.py \
  distribution --score-name "quality" --days 7 --bins 10

# 2. Find sessions with errors
python3 ~/.codex/skills/langfuse-session-analysis/scripts/session_analyzer.py \
  find-issues --days 7 --has-errors

# 3. Investigate specific trace
python3 ~/.codex/skills/langfuse-data-retrieval/scripts/trace_retriever.py \
  --trace-id "<low-score-trace-id>" --mode io

# 4. Add root cause annotation
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  create-score \
  --trace-id "<trace-id>" \
  --name "root_cause" \
  --string-value "context_window_exceeded" \
  --data-type CATEGORICAL \
  --comment "Response truncated due to context length"
```

### Common Root Causes

- `context_window_exceeded`
- `rate_limit_hit`
- `invalid_input`
- `model_error`
- `prompt_issue`
- `tool_failure`

---

## Best Practices

### 1. Consistent Scoring

- Define clear scoring guidelines before starting
- Use the same scale across similar tasks
- Document edge cases and decisions

### 2. Regular Calibration

- Review sample annotations periodically
- Check inter-annotator agreement if multiple reviewers
- Update guidelines based on learnings

### 3. Efficient Workflows

- Batch similar traces together
- Use trace-analysis for context before scoring
- Export and analyze patterns regularly

### 4. Comments Are Valuable

- Always add comments for edge cases
- Explain low scores to enable debugging
- Note patterns you observe

### 5. Integrate with Analytics

- Run regression detection after annotation batches
- Compare scores by release/environment
- Track improvement over time

---

## Automation Tips

### Combine with Experiments

Use experiment-runner to auto-evaluate, then human-review edge cases:

```bash
# Run automated evaluation
python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  run --dataset "test-set" --run-name "auto-eval" \
  --task-script ./task.py --evaluator-script ./evaluators.py

# Find items that need human review (low auto scores)
python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  analyze --dataset "test-set" --run-name "auto-eval" \
  --score-name accuracy --score-threshold 0.7

# Human annotate the edge cases
# ...
```

### Export for Training

Regular exports for model improvement:

```bash
# Weekly export of all annotations
python3 ~/.codex/skills/langfuse-annotation-manager/scripts/annotation_manager.py \
  export --score-name "human_review" --days 7 --format json --output week-$(date +%Y%m%d).json
```
