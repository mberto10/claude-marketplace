---
description: Write content following your style and outline
argument-hint: <outline or topic>
allowed-tools: Read, Write, Edit, Task, AskUserQuestion
---

Launch the drafter agent to write content for: $ARGUMENTS

## Setup

1. Load user's style from `.claude/writing-studio.local.md` - this is REQUIRED
2. If no style file exists, suggest running `/setup-style` first
3. Check if input includes an outline or is a fresh topic
4. Launch the drafter agent via Task tool

## Agent Instructions

The drafter agent MUST:
- Internalize and apply the user's style guide strictly
- Follow the outline structure if provided
- Match the user's tone, voice, and vocabulary preferences
- Avoid all prohibited words
- Create checkpoints after each major section

## Style Application

Before writing each section:
- Review style guide tone and voice
- Check prohibited words list
- Apply vocabulary preferences
- Match sentence length patterns from examples

## Checkpoints

Present checkpoints frequently:
- After each major section: show preview, ask if tone is right
- When making structural decisions: offer options
- If unsure about direction: ask before continuing

## Section Checkpoint Format

```
═══════════════════════════════════════════
📍 CHECKPOINT: [Section Name] Complete
═══════════════════════════════════════════

I've drafted [section description] ([word count] words).

**Preview:**
> "[First 2-3 sentences of the section]..."

**Options:**
1. **Continue** - This captures the right tone, proceed to next section
2. **Adjust tone** - It's too [formal/casual/etc.] (specify)
3. **Revise content** - The message needs adjustment (explain what)

Ready to proceed? (1/2/3)
═══════════════════════════════════════════
```

## Output

When complete:
- Present full draft
- Note total word count
- Highlight any areas of uncertainty
- Suggest moving to `/edit` for refinement

## Key Principles

- Style consistency is paramount
- Check in frequently with user
- Follow outline but allow creative flow
- Flag any deviation from style preferences
- Quality over speed
