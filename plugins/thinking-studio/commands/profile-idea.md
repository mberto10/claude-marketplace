---
name: profile-idea
description: Capture your personal relationship to an idea from source material
arguments:
  - name: idea
    description: Name of the idea/concept to profile
    required: false
---

# Profile Idea

Create a personal idea profile from source material.

## Your Task

Help the user capture their personal relationship to an idea. This is NOT about creating a canonical definition - it's about extracting how THEY think about and use this concept.

## Process

1. **Gather Source Material**
   - Ask what passages, quotes, or concepts they want to profile
   - If they've provided material, acknowledge it
   - If `$ARGUMENTS.idea` is provided, ask for their source material on that idea

2. **Extract Personal Resonance**
   Use the idea-profiler skill to understand:
   - Why did they save/notice this particular material?
   - When do they find themselves thinking about this?
   - How would they explain it in their own words?

3. **Draft the Profile**
   Create a profile following the structure in `${CLAUDE_PLUGIN_ROOT}/skills/idea-profiler/references/idea-template.md`

   Key sections:
   - My Understanding (THEIR version, not textbook)
   - Why This Resonates (personal connection)
   - Examples That Stuck (THEIR examples)
   - How I Use It (practical application)
   - My Explanatory Moves (how they teach it)
   - Tensions & Edges (honest limits)
   - Source Passages (original material)

4. **Review & Save**
   - Present the draft for review
   - Ask if it captures their thinking accurately
   - Save to `${CLAUDE_PLUGIN_ROOT}/ideas/[idea-name].md`
   - Update `${CLAUDE_PLUGIN_ROOT}/references/connections.md` if there are links to other ideas

## Key Principles

- **Their language, not source language**
- **Their examples, not canonical examples**
- **Partial understanding is valid** - capture where they are
- **Ask probing questions** - don't assume you know their take

## Starting Prompt

If no material provided:
"What idea do you want to profile? Share the passages, quotes, or concepts that resonate with you, and I'll help capture your personal take on it."

If material provided:
"I see you've shared material about [X]. Before I profile this, help me understand YOUR relationship to it - what made this click for you?"
