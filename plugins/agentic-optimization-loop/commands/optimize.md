---
name: optimize
description: Start or continue an optimization loop for an AI agent. Guides through hypothesis -> experiment -> analyze -> compound cycles with persistent state.
arguments:
  - name: agent
    description: Name of the agent to optimize (used for journal path)
    required: false
  - name: phase
    description: Force entry at a specific phase (init, hypothesize, experiment, analyze, compound)
    required: false
---

# Optimization Loop Command

You are orchestrating an iterative optimization loop for an AI agent. This command manages state across sessions and guides the user through systematic improvement.

## Step 1: Determine Agent

If `agent` argument provided, use it. Otherwise:

```
Which agent would you like to optimize?

If this is a new optimization, I'll need:
- Agent name (for the journal)
- Path to agent code
- How to run it
- Target metric and goal
```

Use AskUserQuestion if needed.

## Step 2: Load State

Check for existing optimization journal:

```
.claude/optimization-loops/<agent>/journal.yaml
```

Read the journal if it exists. Parse the YAML to understand current state.

## Step 3: Determine Phase

Based on journal (or absence), determine current phase:

| Journal State | Current Phase |
|---------------|---------------|
| No journal exists | INITIALIZE |
| `current_phase: init` | INITIALIZE (continue) |
| `current_phase: hypothesize` | HYPOTHESIZE |
| `current_phase: experiment` | EXPERIMENT |
| `current_phase: analyze` | ANALYZE |
| `current_phase: compound` | COMPOUND |
| `current_phase: graduated` | COMPLETE (celebrate!) |

If `phase` argument provided, override (but warn if skipping steps).

## Step 4: Load Skill and Reference

Load the optimization-craft skill:
```
Read: ${CLAUDE_PLUGIN_ROOT}/skills/optimization-craft/SKILL.md
```

Then load the phase-specific reference:
- INITIALIZE: `references/journal-schema.md`
- HYPOTHESIZE: `references/hypothesis-patterns.md`
- EXPERIMENT: `references/experiment-design.md`
- ANALYZE: `references/analysis-framework.md`
- COMPOUND: `references/compounding-strategies.md`

## Step 5: Execute Phase

Follow the skill instructions for the current phase. Key behaviors:

### INITIALIZE Phase
1. Gather agent information (path, entry point, prompts, tools)
2. Confirm target metric and goal with user
3. Establish baseline by running initial evaluation
4. Create journal with baseline metrics
5. Transition to HYPOTHESIZE

### HYPOTHESIZE Phase
1. Review current state vs target
2. Analyze failures from previous iteration (if any)
3. Identify highest-impact improvement opportunity
4. Formulate specific, testable hypothesis
5. Design the change (what, where, how)
6. Update journal with hypothesis
7. Confirm with user before transitioning to EXPERIMENT

### EXPERIMENT Phase
1. Guide user through implementing the change
2. Verify change is active (smoke test)
3. Run evaluation experiment
4. Collect results
5. Update journal with results
6. Transition to ANALYZE

### ANALYZE Phase
1. Compare results to baseline and previous iteration
2. Determine if hypothesis was validated
3. Investigate failures (use optimization-analyst agent for deep dives)
4. Extract patterns and findings
5. Update journal with analysis
6. Transition to COMPOUND

### COMPOUND Phase
1. Add failure cases to dataset
2. Check judge calibration
3. Capture learnings in journal
4. Decide: continue, pivot, or graduate
5. If continuing, formulate next hypothesis direction
6. Transition to HYPOTHESIZE or GRADUATED

## Step 6: Update Journal

After each phase completion:
1. Update `current_phase` in journal
2. Update iteration record with phase data
3. Write journal back to file

## Step 7: Report and Prompt

After executing phase:
1. Summarize what was accomplished
2. Show current metrics vs target
3. Explain what's needed for next phase
4. Ask if user wants to continue or pause

## Interruption Handling

The user can pause at any time. State is preserved in journal. When they return:
- Journal tells us exactly where we left off
- Continue from that point seamlessly

## Output Format

Always provide clear status:

```
## Optimization Loop: <agent>

**Phase:** <current> → <next>
**Iteration:** <N>

### Progress
| Metric   | Baseline | Current | Target | Gap |
|----------|----------|---------|--------|-----|
| accuracy | 72%      | 81%     | 90%    | 9%  |

### This Phase
<Summary of what was done>

### Next Steps
<What's needed to proceed>

Ready to continue? [Yes / Pause for now]
```

## Error Handling

- If Langfuse unavailable: Inform user, suggest checking credentials
- If experiment fails: Record failure, allow retry or skip
- If journal corrupted: Offer to backup and restart
- If agent not found: Help user set up tracing first
