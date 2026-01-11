---
name: evaluation-design
description: Use this skill when the user needs to define evaluation metrics, select datasets, or design grading/annotation strategies for agent optimization. Provides a structured, decision-driven workflow and reusable templates.
---

# Evaluation Design

A systematic skill for designing **metrics, datasets, and grading/annotation strategies** before running an optimization loop. This skill ensures evaluations are representative, measurable, and stable across iterations.

## When to Use

Use this skill when the user asks:
- “Which metrics should we track?”
- “What dataset should we use?”
- “How do we grade or annotate outputs?”
- “How should we set up evaluators or LLM judges?”
- “Design the evaluation plan for this agent.”

---

## Outcomes

By the end, you will have:
- A **metrics matrix** (primary, constraints, secondary)
- A **dataset strategy** with sourcing, size, and coverage rules
- A **grading and annotation plan** (human, LLM-judge, or hybrid)
- A **ready-to-run evaluation spec** to insert into the optimization journal

---

## Workflow

### Step 1: Define the Target Task

Confirm the agent’s intended behavior:
- Primary user intent(s)
- Expected output format
- Tools or external data sources used
- Critical failure modes (safety, hallucinations, compliance, etc.)

### Step 2: Build the Metrics Matrix

Use the template:

```yaml
metrics:
  primary:
    - name: <metric>
      definition: <what counts as success?>
      scale: <e.g., binary | 1-5 | percentage>
  constraints:
    - name: <metric>
      limit: <threshold>
      reason: <why this must not regress>
  secondary:
    - name: <metric>
      definition: <supporting metric>
```

Guidelines:
- **Primary**: one metric that represents “overall success.”
- **Constraints**: latency, cost, safety, policy compliance.
- **Secondary**: helpful but not required (helpfulness, readability, etc.).

Reference: `${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/metric-framework.md`

### Step 3: Select the Dataset Strategy

Choose between:
- **Production traces** (high realism)
- **Curated failures** (high signal for improvement)
- **Synthetic cases** (edge coverage)
- **Public benchmarks** (comparability)

Use the dataset template:

```yaml
dataset:
  sources:
    - type: production | curated | synthetic | benchmark
      description: <where it comes from>
      count: <n>
  coverage:
    - category: <failure pattern or intent>
      target_count: <n>
  size_target: <total items>
  refresh_policy: <when to add or retire items>
```

Reference: `${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/dataset-strategy.md`

### Step 4: Design Grading & Annotation

Pick a grading strategy:
- **Rule-based** (deterministic checks)
- **LLM-as-judge** (rubric-driven)
- **Hybrid** (rules for structure + LLM for quality)

Use the grading template:

```yaml
grading:
  type: rule | llm | hybrid
  rubric:
    - criterion: <name>
      description: <what good looks like>
      scale: <binary | 1-5>
  judges:
    - model: <judge model>
      prompt: <prompt name or path>
      bias_mitigations:
        - randomize_order
        - pairwise_comparison
  calibration:
    human_review_rate: <percentage>
    agreement_target: <e.g., 0.8>
```

Reference: `${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/grading-annotation.md`

### Step 5: Produce the Evaluation Spec

Create a compact spec that can be inserted into the optimization journal:

```yaml
evaluation_spec:
  metrics: <from Step 2>
  dataset: <from Step 3>
  grading: <from Step 4>
  baseline_run: "baseline"
```

---

## Example: Support Triage Agent

Reference example:
`${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/example-support-triage.md`

Summary:
- **Primary**: resolution accuracy
- **Constraints**: latency p95 < 4s, cost avg < $0.03, safety violations = 0
- **Dataset**: 60 production cases, 20 curated failures, 20 synthetic edge cases
- **Grading**: hybrid (rules for routing correctness + LLM judge for tone)

---

## Integration with Optimization Loop

Suggested integration points:
- **Initialize**: run this skill before establishing the baseline
- **Hypothesize**: ensure new metrics align with current hypothesis

Once complete, write the evaluation spec into the journal under `meta` and `baseline` sections.

---

## Checklist

Use this checklist before starting the optimization loop:

- [ ] Primary metric clearly defined and measurable
- [ ] Constraint metrics set with explicit thresholds
- [ ] Dataset sources chosen with coverage goals
- [ ] Grading strategy defined with calibration plan
- [ ] Evaluation spec ready for baseline run

---

## References

- `${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/metric-framework.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/dataset-strategy.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/grading-annotation.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/evaluation-design/references/example-support-triage.md`
