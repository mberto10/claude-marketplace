---
name: optimize-status
description: Quick view of optimization loop status for an agent. Shows current phase, metrics trajectory, and next actions without making changes.
arguments:
  - name: agent
    description: Agent name to check status for. If omitted, lists all active optimizations.
    required: false
---

# Optimization Status Command

Provide a quick, read-only view of optimization progress.

## If No Agent Specified

List all active optimization loops:

```bash
# Find all journals
ls .claude/optimization-loops/*/journal.yaml
```

Show summary for each:
```
## Active Optimization Loops

| Agent | Phase | Iteration | Progress | Last Activity |
|-------|-------|-----------|----------|---------------|
| my-agent | analyze | 3 | 72% → 81% / 90% | 2 days ago |
| other-agent | hypothesize | 1 | baseline | today |
```

## If Agent Specified

Read the journal:
```
.claude/optimization-loops/<agent>/journal.yaml
```

### Status Report Format

```
## Optimization Status: <agent>

**Phase:** <current_phase> (iteration <N>)
**Started:** <date>
**Target:** <target_statement>

---

### Metrics Trajectory

| Metric | Baseline | Current | Target | Gap | Trend |
|--------|----------|---------|--------|-----|-------|
| accuracy | 72% | 81% | 90% | -9% | ↑ |
| latency_p95 | 2.1s | 2.4s | <3s | ✓ | → |
| cost_avg | $0.015 | $0.018 | <$0.02 | ✓ | ↑ |

---

### Iteration History

| # | Hypothesis | Result | Delta |
|---|------------|--------|-------|
| 1 | Add reasoning step | ✓ Validated | +6% accuracy |
| 2 | Tool guidance | ✓ Validated | +3% accuracy |
| 3 | Context chunking | ⏳ In progress | - |

---

### Current Iteration (#3)

**Hypothesis:** If we chunk long inputs before processing, accuracy on long queries will improve by ~5%

**Status:** ANALYZE phase
- ✓ Hypothesis documented
- ✓ Change implemented
- ✓ Experiment run (v3-context-chunking)
- ⏳ Analysis pending
- ○ Compounding pending

**Last results:**
- accuracy: 84% (+3%)
- latency_p95: 2.2s (-0.2s)

---

### Accumulated Learnings

**What works:**
- Explicit tool guidance improves tool selection
- Step-by-step reasoning helps complex queries

**What fails:**
- Generic "be thorough" instructions hurt latency
- Too many examples confuse the model

**Dataset growth:** 50 → 62 items (+24%)

---

### Next Action

To continue, run `/optimize <agent>` to complete the ANALYZE phase.

Needed:
- Review experiment results
- Investigate 4 new failures
- Document findings
```

## If No Journal Exists

```
## Optimization Status: <agent>

No optimization loop found for "<agent>".

To start optimization:
1. Ensure agent has Langfuse tracing
2. Run `/optimize <agent>`

Available agents with journals:
- other-agent (iteration 2, COMPOUND phase)
```

## Quick Stats Mode

If user asks for "quick" or "brief" status:

```
<agent>: iteration 3, ANALYZE phase, 81% accuracy (target: 90%)
Next: Complete failure analysis
```
