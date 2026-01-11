---
name: compound-reflection-craft
description: This skill should be used when the user invokes "/compound:reflect", asks to "reflect on this session", "capture learnings", "what did we learn", "debrief this work", or wants to create a structured learning artifact from recent work. Provides methodology for trace-aware reflection and structured output.
---

# Reflection Craft

## Purpose

Transform a work session into structured, actionable learnings that can compound into improvements. Reflection is trace-aware (grounded in what actually happened) and produces one-line testable rules with source references.

## When to Use

- User invokes /compound:reflect
- User asks to reflect, debrief, or capture learnings from recent work
- User wants a structured learning artifact (Linear issue or local file)

## Foundation

Load `references/compounding-methodology.md` for the full framework on what makes learning worth encoding, the heuristics format, and decision gates.

## Compound Reflect Workflow

### 1. Load Methodology

- Read `references/compounding-methodology.md`.
- Apply the quality gates: recurrence, testability, architecture fit, maintenance cost.

### 2. Gather Session Context

Analyze the current session:
- What plugins, skills, or commands were used
- What decisions were made
- What friction occurred
- What worked well
- What was missing

If the user provided focus text, prioritize that observation.

### 3. Introspect Plugin or Skill Structure

Read the local structure to understand what already exists:
- If the repo includes `plugins/compound-loop/`, review that.
- If the repo includes `codex-skills/`, inspect relevant skills there.
- Use this to target changes accurately.

### 4. Structured Debrief

Document:
- What happened (brief summary)
- What worked (successful patterns)
- Friction points (confusion, missing capability, unexpected behavior)
- Missing capabilities (what would have helped)

### 5. Classify Learnings

For each potential learning, classify:

Frontier position:
- Frontier-shifting (high r): improves underlying capability so both volume and quality improve
- Frontier-sliding (low r): optimizes within current constraints

Selection pressure:
- Real friction (high confidence): emerged from actual pain in this session
- Theoretical (lower confidence): sounds good but was not tested

Prioritize frontier-shifting plus real friction learnings.

### 6. Distill Learnings

Convert observations into one-line testable rules:

```
[Specific, actionable learning statement]
[src:YYYY-MM-DDTHHMMZ__context] [type:rule|feature|fix]
```

Quality filter (only include learnings that are):
- Specific enough to act on
- Testable (can verify compliance)
- Likely to recur
- Worth the encoding cost

Reject vague observations like "be more careful" or "remember to check".

### 7. Categorize by Destination

Map each learning to where it should land:

| Type | Destination | Example |
|------|-------------|---------|
| rule | Skill update or CLAUDE.md | Behavioral guidance |
| feature | New skill section or extension | Missing capability |
| fix | Skill update | Incorrect behavior |
| architecture | Documentation or structure change | Pattern improvement |

### 8. Create Learning Artifact

Try Linear first (preferred):
- Team: MB90
- Project: Compound
- Labels: compound-learning
- Title: `[compound-reflect] YYYY-MM-DD: [brief description]`

If Linear is not available, create a local file:
- `./compound-learnings/YYYY-MM-DD-HHMMSS.md`
- Create the directory if it does not exist

Issue/File body format:

```markdown
## Session Context
- Date: [today's date]
- Plugins used: [list what was used]
- Focus: [user-provided focus or "general reflection"]

## Summary
[2-3 sentences on what was done and outcomes]

## Learnings

### Rules
- [Learning] [src:...]

### Feature Requests
- [Feature] [src:...]

### Fixes
- [Fix] [src:...]

## Proposed Changes

### [Plugin/Skill Name]
- **File:** path/to/file
- **Change type:** update | create | delete
- **Description:** What to change and why
- **Priority:** high | medium | low

## Raw Observations
[Additional context that might be useful later]
```

### 9. Confirm Output

Report to the user:
- Where the artifact was created (Linear issue link or file path)
- Count of learnings captured (X rules, Y features, Z fixes)
- Highest priority item
- Next step: "Run /compound:consolidate to implement these"

## User Focus Integration

When the user provides freeform text with their reflection request:

1. Treat it as the primary lens.
2. Validate against the session.
3. Expand if relevant.
4. Prioritize their focus as the first learning.

Example:
```
User: /compound:reflect the skill description was confusing for langfuse
Primary learning: Update langfuse-analyzer skill description triggers
Secondary: Any other langfuse-related friction discovered
```

## Output Expectations

After reflection, confirm:
1. Issue or file created with link or path
2. Learning count (rules, features, fixes)
3. Top priority item
4. Next step reminder

## Important Notes

- If the user provided focus text, make that the primary learning
- Ground observations in what actually happened
- Be specific; vague learnings have no value
- Quality over quantity: 3 good learnings beat 10 vague ones
- Include source references for traceability
