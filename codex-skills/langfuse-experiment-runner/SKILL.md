---
name: langfuse-experiment-runner
description: Use when the user wants to run Langfuse experiments on datasets, apply LLM-as-judge prompts, compare runs, analyze failures, or evaluate prompt/model changes.
---

# Langfuse Experiment Runner

Run experiments on Langfuse datasets using task scripts and evaluators.

## Quick Start

```bash
python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  run --dataset "my-tests" --run-name "v1" --task-script ./task.py --use-langfuse-judges
```

## Core Operations

### Run with Langfuse Judges

```bash
python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  run --dataset "my-tests" --run-name "v2" --task-script ./task.py --use-langfuse-judges
```

### Run with Local Evaluators

```bash
python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  run --dataset "my-tests" --run-name "v2" --task-script ./task.py \
  --evaluator-script ./evaluators.py --max-concurrency 5
```

### List or Compare Runs

```bash
python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  list-runs --dataset "my-tests"

python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  compare --dataset "my-tests" --runs "v1" "v2"
```

### Analyze Failures

```bash
python3 ~/.codex/skills/langfuse-experiment-runner/scripts/experiment_runner.py \
  analyze --dataset "my-tests" --run-name "v2" --show-failures
```

## Reference

- `references/experiment-workflows.md` for experiment playbooks and evaluator patterns.

## Environment

```bash
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```

## Notes

- `--use-langfuse-judges` auto-discovers prompts named `judge-*` in Langfuse.
- Task scripts must export a `task()` function; evaluator scripts must expose `EVALUATORS`.
