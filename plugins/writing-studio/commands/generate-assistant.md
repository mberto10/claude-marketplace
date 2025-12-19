---
description: Transform a writer profile into professional writing assistant instructions
argument-hint: [profile-path]
allowed-tools: Read, Write, AskUserQuestion
---

Transform a writer profile into actionable, professional writing assistant instructions.

## Input

If argument provided ($ARGUMENTS):
- Read the writer profile from that path

If no argument:
1. Check for `.claude/writer-profile.md`
2. Check for `.claude/writing-studio.local.md`
3. If neither exists, ask user to provide path or run `/profile-writer` first

## Output Format Selection

Ask user what type of assistant instructions to generate:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Assistant Type
═══════════════════════════════════════════

What type of writing assistant instructions do you need?

**Options:**
1. **Full System Prompt** - Complete instructions for an AI writing assistant
2. **Voice Replication Guide** - Instructions for writing AS this author
3. **Editing Guide** - Instructions for editing TO MATCH this author's style
4. **Quick Reference Card** - Condensed essential rules (1 page)

Which format? (1/2/3/4)
═══════════════════════════════════════════
```

## Output Formats

### 1. Full System Prompt

Generate a complete system prompt for a writing assistant:

```markdown
# Writing Assistant: [Writer Name]

## Your Role
You are a professional writing assistant specialized in [Writer Name]'s voice and style. Your purpose is to help create, edit, and refine content that authentically matches their established writing patterns.

## Voice Identity

### Core Voice
[Extracted from profile: pronoun usage, perspective, narrative distance, persona type]

### Tonal Framework
[Extracted: baseline tone, formality level, humor patterns]

## Writing Rules

### Always Do
- [Specific instruction from profile]
- [Specific instruction from profile]
- [Specific instruction from profile]

### Never Do
- [Anti-pattern from profile]
- [Anti-pattern from profile]
- [Anti-pattern from profile]

### Vocabulary
**Use these patterns:**
- [Signature phrases]
- [Power words]
- [Preferred constructions]

**Avoid:**
- [Prohibited words]
- [Avoided constructions]

## Structural Guidelines

### Openings
[Opening strategy instructions]

### Paragraphs
[Paragraph style instructions]

### Rhythm
[Sentence length and rhythm instructions]

### Closings
[Closing pattern instructions]

## Quality Checklist

Before delivering any writing:
- [ ] Voice consistent throughout (pronouns, tone)
- [ ] No prohibited words or constructions
- [ ] Rhythm matches expected patterns
- [ ] Signature elements present but not forced
- [ ] Would the writer recognize this as their voice?

## Examples

### This sounds like [Writer]:
> "[Example from profile]"

### This does NOT sound like [Writer]:
> "[Counter-example showing what to avoid]"
```

### 2. Voice Replication Guide

Generate focused instructions for writing AS this author:

```markdown
# Voice Replication Guide: [Writer Name]

## The Voice in One Sentence
[Executive summary distilled to essence]

## Before You Write

1. **Adopt the persona**: [Persona type and stance]
2. **Set the tone**: [Tonal baseline]
3. **Choose your pronouns**: [Pronoun defaults and when to shift]

## While Writing

### Sentence by Sentence
- Default length: [Pattern]
- Vary rhythm: [Specific pattern]
- Punctuation habits: [Em-dash, semicolon, parenthetical usage]

### Paragraph by Paragraph
- Length: [Typical sentences per paragraph]
- Structure: [Topic sentence pattern]
- Transitions: [Explicit vs implicit ratio]

### Section by Section
- Open with: [Opening strategy]
- Build through: [Section pattern]
- Close with: [Closing approach]

## Signature Moves to Include

1. **[Move name]**: [How to execute]
2. **[Move name]**: [How to execute]
3. **[Move name]**: [How to execute]

## Phrases to Use Naturally
- "[Phrase]" - [When to use]
- "[Phrase]" - [When to use]
- "[Phrase]" - [When to use]

## Red Lines (Never Cross)
- Never: [Anti-pattern]
- Never: [Anti-pattern]
- Never: [Anti-pattern]

## Final Check
Read your draft aloud. Does it sound like [Writer] talking? If not, identify where the voice breaks and fix those spots.
```

### 3. Editing Guide

Generate instructions for editing content to match this style:

```markdown
# Editing Guide: Match [Writer Name]'s Style

## Editing Philosophy
Edit to reveal the writer's voice, not impose external standards. The goal is consistency with [Writer]'s established patterns, not generic "good writing."

## Pass 1: Voice Alignment

### Check Pronouns
- Expected: [Distribution]
- Fix: Convert [X] to [Y] where appropriate
- Exception: [When to keep different pronouns]

### Check Tone
- Target: [Baseline tone]
- Too formal? [How to adjust]
- Too casual? [How to adjust]

## Pass 2: Vocabulary Sweep

### Find and Replace
| Find | Replace With | Reason |
|------|--------------|--------|
| [word] | [preferred] | [from profile] |
| [word] | [preferred] | [from profile] |

### Flag for Removal
- [Prohibited word/phrase]
- [Prohibited word/phrase]

### Consider Adding
- [Signature phrase] - if natural opportunity
- [Power word] - for emphasis points

## Pass 3: Rhythm Adjustment

### Sentence Length Check
- Too many long sentences in a row? Break one up.
- Too many short sentences? Combine or add a longer one.
- Target distribution: [From profile]

### Punctuation Review
- Em-dashes: [Usage pattern]
- Semicolons: [Usage pattern]
- Parentheticals: [Usage pattern]

## Pass 4: Structure Review

### Opening
- Does it match [Writer]'s typical opening strategy?
- Options: [Opening types they use]

### Transitions
- Are they [explicit/implicit] enough?
- Check for transition words: [Their patterns]

### Closing
- Does it match [Writer]'s typical closing?
- Options: [Closing types they use]

## Pass 5: Signature Elements

### Should Be Present (somewhere)
- [ ] [Signature move or element]
- [ ] [Signature move or element]
- [ ] [Distinctive marker]

### Should NOT Be Present
- [ ] No [anti-pattern]
- [ ] No [anti-pattern]

## Final Validation
Ask: "Would [Writer] publish this under their name without changes?" If hesitant, identify what feels off.
```

### 4. Quick Reference Card

Generate a condensed one-page reference:

```markdown
# [Writer Name] - Quick Style Reference

## Voice
**Pronouns**: [Default] | **Tone**: [Baseline] | **Formality**: [Level]

## Do ✓
- [Key instruction]
- [Key instruction]
- [Key instruction]
- [Key instruction]
- [Key instruction]

## Don't ✗
- [Anti-pattern]
- [Anti-pattern]
- [Anti-pattern]
- [Anti-pattern]
- [Anti-pattern]

## Signature Phrases
- "[Phrase]"
- "[Phrase]"
- "[Phrase]"

## Rhythm
**Sentences**: [Pattern] | **Paragraphs**: [Length] | **Punctuation**: [Key habit]

## Structure
**Open**: [Type] | **Build**: [Pattern] | **Close**: [Type]

## Quick Check
□ Voice consistent? □ No prohibited words? □ Rhythm right? □ Sounds like them?
```

## Save Options

After generating, ask:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Save Instructions
═══════════════════════════════════════════

**Options:**
1. **Save to file** - Write to `.claude/[writer]-assistant.md`
2. **Copy to clipboard** - Just display for copying
3. **Regenerate** - Try a different format
4. **Refine** - Adjust specific sections

How would you like to proceed? (1/2/3/4)
═══════════════════════════════════════════
```

## Key Principles

- Instructions must be actionable, not descriptive
- Use imperative mood ("Use X" not "The writer uses X")
- Include specific examples from the profile
- Prioritize the most distinctive elements
- Make instructions usable without the original profile
