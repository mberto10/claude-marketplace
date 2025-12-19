---
description: Create a structured outline for your content
argument-hint: <topic or brainstorm output>
allowed-tools: Read, Task, AskUserQuestion
---

Launch the planner agent to create a structured outline for: $ARGUMENTS

## Setup

1. Load user's style from `.claude/writing-studio.local.md` if it exists
2. Check if input references brainstorming output or is a fresh topic
3. Launch the planner agent via Task tool

## Agent Instructions

The planner agent should:
- Define the main thesis or central argument
- Identify key sections and their purposes
- Determine logical flow and transitions
- Consider the target audience
- Estimate scope and depth

## Checkpoints

Present structured checkpoints:
- After understanding scope: confirm target length and depth
- After initial structure: present outline for approval
- Before finalizing: offer to adjust section order or content

## Output Format

Create outline in this structure:

```markdown
# [Title]

**Thesis/Core Message:** [One sentence summary]
**Target Audience:** [Who this is for]
**Estimated Length:** [Word count range]

## Opening Hook
- [Approach: question/story/statistic/provocation]
- [Bridge to main content]

## Section 1: [Section Title]
- Key point A
- Key point B
- Supporting evidence/examples
- Transition to next section

## Section 2: [Section Title]
...

## Conclusion
- [Summary approach]
- [Call to action or final thought]
```

## Structure Checkpoint

```
═══════════════════════════════════════════
📍 CHECKPOINT: Structure Review
═══════════════════════════════════════════

Here's the proposed outline:

[Summary of structure]

**Options:**
1. **Approve** - This structure works, proceed
2. **Reorder** - Adjust the flow (specify how)
3. **Modify** - Add or remove sections (specify what)

How should we proceed? (1/2/3)
═══════════════════════════════════════════
```

## Key Principles

- Ask about scope and audience first
- Create clear, logical flow
- Plan transitions between sections
- Consider reader's journey through content
- Keep outline flexible enough to allow drafting creativity
