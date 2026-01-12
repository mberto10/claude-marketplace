---
name: langfuse-agent-advisor
description: Use when the user asks for strategic guidance on evaluating or improving an AI agent, choosing metrics, building datasets, or setting up an iteration loop with Langfuse.
---

# Langfuse Agent Advisor

Provide strategic guidance for agent evaluation and iteration. Ask clarifying questions, then propose an evaluation plan.

## Clarify First

- What does the agent do and who is the user?
- Is output quality enough, or do they care about trajectory quality?
- What failures are most costly?
- Do they have production traces or only synthetic data?

## Evaluation Framework

Cover three layers:
- Output quality (accuracy, relevance, completeness)
- Trajectory/process quality (tool choice, efficiency)
- Safety and trust (guardrails, adversarial cases)

Ask: "If the answer is correct but the reasoning is flawed, is that a pass or fail?"

## Prerequisites

Before proposing the evaluation plan, confirm:

- **Tracing is active:** agent generates Langfuse traces with key steps instrumented.
- **Dataset exists (or can be created):** an initial eval set (from production traces, curated cases, or synthetic data).
- **Target metric is defined:** primary metric, target value, and guardrail constraints.

## Dataset Strategy

Recommend a mix of:
- Golden set (high-quality baseline)
- Edge cases (rare but valid)
- Known failures (production regressions)
- Adversarial inputs (prompt injection, contradictions)

Explicitly call out **compounding**: turn failures into new test cases and link them into the persistent optimization loop so the dataset grows every iteration.

If no production data exists, propose synthetic data generation and then add real traces over time.

## Improvement Loop

1. Document failure patterns.
2. Build or expand eval cases that cover them.
3. Measure baseline with Langfuse experiments.
4. Apply minimal fixes.
5. Re-run and compare.

## Output

Deliver a concise plan with:
- Proposed dimensions and thresholds
- Dataset source and size
- A step to update the dataset after each iteration (capture failures → new eval cases)
- Suggested Langfuse skills to run next
