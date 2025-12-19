---
description: Generate and explore ideas for a topic
argument-hint: <topic>
allowed-tools: Read, Task, AskUserQuestion
---

Launch the brainstormer agent to explore ideas for: $ARGUMENTS

## Setup

1. Load user's style from `.claude/writing-studio.local.md` if it exists
2. Launch the brainstormer agent via Task tool with the topic

## Agent Instructions

The brainstormer agent should:
- Clarify the topic and intended audience through questions
- Generate diverse angles and approaches (at least 5-7 initial ideas)
- Ask probing questions to uncover hidden aspects
- Explore unexpected connections and angles
- Group related ideas into themes

## Checkpoints

Present structured checkpoints:
- After initial idea generation: offer to explore specific directions deeper
- After exploring directions: present top 3 strongest angles with rationale
- Final checkpoint: direction selection with clear options

## Output Format

Conclude brainstorming with a direction selection checkpoint:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Direction Selection
═══════════════════════════════════════════

Based on our exploration, here are the strongest directions:

1. **[Direction A]** - [Why this angle is compelling]
2. **[Direction B]** - [Why this angle is compelling]
3. **[Direction C]** - [Why this angle is compelling]

Which direction resonates most? (1/2/3) Or describe a different approach.
═══════════════════════════════════════════
```

## Key Principles

- Be genuinely curious and exploratory
- Ask questions before generating ideas
- Don't judge ideas early - quantity first
- Connect ideas across domains
- Surface the user's underlying goals
