---
description: Refine and polish your writing for style consistency
argument-hint: <draft text or file path>
allowed-tools: Read, Write, Edit, Task, AskUserQuestion
---

Launch the editor agent to refine and polish: $ARGUMENTS

## Setup

1. Load user's style from `.claude/writing-studio.local.md` - this is REQUIRED
2. If no style file exists, suggest running `/setup-style` first
3. Determine input type:
   - If argument looks like a file path (contains `/` or ends in `.md`, `.txt`), read that file
   - Otherwise, treat as inline content to edit
4. Launch the editor agent via Task tool

## Agent Instructions

The editor agent MUST:
- Review content against the style guide systematically
- Check for prohibited words and replace them
- Verify voice consistency throughout
- Improve clarity and flow
- Present all changes for approval before applying

## Editing Checklist

Apply these checks in order:
1. **Voice consistency** - Same tone and perspective throughout
2. **Prohibited words** - Find and flag all violations
3. **Vocabulary preferences** - Apply preferred alternatives
4. **Sentence variety** - Match preferred rhythm patterns
5. **Paragraph structure** - Check density and flow
6. **Transitions** - Ensure smooth connections
7. **Opening/closing** - Verify hook effectiveness and conclusion satisfaction

## Change Presentation

Present changes clearly:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Style Consistency Review
═══════════════════════════════════════════

I've reviewed the draft against your style guide.

**Matches:**
✓ [What's already good]
✓ [What's already good]

**Suggested Changes:**
1. Line 23: "utilize" → "use" (prohibited word)
2. Line 45: Paragraph too long (187 words) → suggest splitting
3. Line 67: Passive voice → convert to active

**Options:**
1. **Apply all** - Make all suggested changes
2. **Review individually** - Show me each change before applying
3. **Keep some** - Tell me which to skip

How should I proceed? (1/2/3)
═══════════════════════════════════════════
```

## Individual Change Review (if requested)

```
═══════════════════════════════════════════
📍 Change 1 of 5
═══════════════════════════════════════════

**Current:**
> "We need to leverage our existing infrastructure..."

**Suggested:**
> "We need to use our existing infrastructure..."

**Reason:** "leverage" is on your prohibited words list

Apply this change? (y/n/skip all similar)
═══════════════════════════════════════════
```

## Final Summary

After all edits:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Final Review
═══════════════════════════════════════════

Editing complete. Summary:

- **Word count:** [X] words ([+/-Y] from original)
- **Changes made:** [N] edits
- **Style compliance:** [X]%

**Options:**
1. **Finalize** - The piece is complete
2. **One more pass** - I want to refine [specific aspect]
3. **Major revision** - This needs more significant changes

Ready to finalize? (1/2/3)
═══════════════════════════════════════════
```

## Key Principles

- Every change must have a reason
- User approves all significant changes
- Preserve the writer's intent
- Improve without over-editing
- Focus on consistency over perfection
