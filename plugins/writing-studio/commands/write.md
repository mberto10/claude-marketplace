---
description: Start a complete writing session with guided workflow
argument-hint: <topic or goal>
allowed-tools: Read, Write, Edit, Glob, Grep, Task, AskUserQuestion
---

Start a comprehensive writing session for: $ARGUMENTS

## Setup

First, check for the user's style configuration:
1. Look for `.claude/writing-studio.local.md` in the project
2. If found, load and internalize the style preferences
3. If not found, ask if the user wants to set up their style guide first with `/setup-style`

## Workflow

Guide the user through the complete writing workflow with structured checkpoints:

### Stage 1: Brainstorming
Use the brainstormer agent via Task tool to:
- Clarify the topic and intended audience
- Generate diverse angles and approaches
- Ask probing questions to uncover hidden aspects
- Present checkpoint with direction options

### Stage 2: Planning
After direction is chosen, use the planner agent via Task tool to:
- Define the main thesis or central argument
- Identify key sections and their purposes
- Create detailed outline
- Present checkpoint for structure approval

### Stage 3: Drafting
After outline is approved, use the drafter agent via Task tool to:
- Write content following the approved outline
- Maintain the user's style throughout
- Create checkpoints after each major section
- Allow for mid-draft adjustments

### Stage 4: Editing
After draft is complete, use the editor agent via Task tool to:
- Review for style consistency
- Check against prohibited words and preferences
- Improve clarity and flow
- Present final checkpoint with changes summary

## Checkpoint Format

At each stage, use structured checkpoints:
```
═══════════════════════════════════════════
📍 CHECKPOINT: [Stage Name]
═══════════════════════════════════════════

[Summary of current state]

**Options:**
1. [Option A] - [Description]
2. [Option B] - [Description]
3. [Option C] - [Description]

Which direction? (1/2/3) Or describe your preference.
═══════════════════════════════════════════
```

## Key Principles

- Be highly interactive - check in frequently
- Follow the user's style guide strictly
- Present meaningful options at decision points
- Allow the user to skip stages if desired
- Adapt workflow based on user feedback
