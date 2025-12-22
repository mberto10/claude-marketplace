---
name: apply
description: Apply your profiled ideas to analyze a problem or situation
arguments:
  - name: idea
    description: Which idea(s) to apply (or "all" to let me choose)
    required: false
  - name: problem
    description: The problem or situation to analyze
    required: false
---

# Apply Ideas

Use your profiled thinking patterns to analyze a problem or situation.

## Your Task

Help the user apply their personal mental models to a concrete problem. Draw from their idea profiles to think through things the way THEY would think through them.

## Process

1. **Understand the Problem**
   - If `$ARGUMENTS.problem` provided, clarify if needed
   - Otherwise, ask what they want to think through

2. **Select Relevant Ideas**
   - If `$ARGUMENTS.idea` specified, load that profile from `${CLAUDE_PLUGIN_ROOT}/ideas/`
   - If "all" or unspecified, scan their idea library and suggest relevant ones
   - Read the connections in `${CLAUDE_PLUGIN_ROOT}/references/connections.md` for related ideas

3. **Apply Their Thinking Patterns**
   For each relevant idea profile, use:
   - Their "How I Use It" section for application triggers
   - Their "My Explanatory Moves" for framing
   - Their "Examples That Stuck" for analogies
   - Their understanding, not generic understanding

4. **Synthesize**
   - If multiple ideas apply, show how they interact
   - Note any tensions between ideas
   - Present analysis in THEIR thinking style

## Key Principles

- **Use their framing** - Reference their examples and analogies
- **Stay grounded in their profiles** - Don't add generic mental models
- **Show your work** - "Using your thinking on [idea]..."
- **Note gaps** - "Your library doesn't have an idea for this aspect..."

## Output Format

```
Applying: [idea-name]

[Analysis using THEIR framing from the profile]

Using your example of [their example]: [application]

Your thinking on [idea] suggests: [insight]
```

## If No Ideas Profiled Yet

"Your thinking library is empty. Would you like to profile some ideas first? Share passages or concepts that resonate with you, and I'll help capture your take on them."
