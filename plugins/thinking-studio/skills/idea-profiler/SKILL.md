---
name: Idea Profiler
description: This skill should be used when the user asks to "profile an idea", "capture my thinking on", "extract my take on", "add to my thinking studio", "what resonates about this", or provides passages/quotes/concepts they want to internalize into their personal thinking library.
version: 1.0.0
---

# Idea Profiler

Extract the user's personal relationship to ideas from source material. This is NOT about creating canonical definitions - it's about capturing how THIS person thinks about and uses an idea.

## Purpose

Transform source passages, quotes, or concepts into personal idea profiles that capture:
- The user's internalized understanding (not textbook definitions)
- Why this specific idea resonates with them
- Examples that clicked for them personally
- How they actually use the idea in their thinking
- Their explanatory moves when sharing this idea

## When to Use

- User provides passages/quotes that resonate with them
- User wants to add a concept to their thinking library
- User wants to articulate their understanding of an idea
- User asks "help me capture my thinking on X"

## Core Principle

**Personal, not canonical.** Every field in the idea profile should reflect the USER's relationship to the idea, not the authoritative definition.

Wrong: "Inversion is a problem-solving technique where you consider the opposite..."
Right: "For me, inversion is about asking 'what would make this fail?' before asking how to succeed..."

## Profiling Process

### Phase 1: Source Ingestion

Gather the raw material:
1. What passages/quotes did the user provide?
2. What idea or concept is this about?
3. Why did they select THIS material? (The curation itself reveals something)

### Phase 2: Resonance Extraction

Understand the personal connection:
- What specifically clicked for them?
- What problem does this idea solve in THEIR thinking?
- What were they thinking about before this idea helped?

Ask probing questions:
- "What made you save this particular passage?"
- "When do you find yourself reaching for this idea?"
- "How would you explain this to a friend?"

### Phase 3: Personal Articulation

Capture their version:
- Their language, not source language
- Their examples, not canonical examples
- Their use cases, not general applications

### Phase 4: Connection Mapping

Link to existing ideas:
- What other ideas in their library does this connect to?
- Are there tensions with other ideas they hold?
- What category/cluster does this belong to?

## Output: Idea Profile

Generate a markdown file following this structure:

```markdown
---
idea: [Idea Name]
sources: ["source 1", "source 2"]
connects_to: ["other-idea-1", "other-idea-2"]
categories: ["category-1", "category-2"]
---

# [Idea Name]

## My Understanding
[Their internalized version - how they'd explain it to themselves]
[NOT the textbook definition]

## Why This Resonates
[What about this clicked for them specifically]
[What gap in their thinking does it fill]

## Examples That Stuck
[Specific instances that crystallized this idea for them]
[Personal examples, not canonical ones]

## How I Use It
[When they reach for this idea]
[What situations trigger this mental model]
[Practical application in their life/work]

## My Explanatory Moves
[How THEY explain this to others]
[Their go-to analogies for this idea]
[The teaching version they've developed]

## Tensions & Edges
[Where does this idea break down?]
[What doesn't it handle well?]
[Honest limits in their understanding]

## Source Passages
[The actual quotes/passages that shaped their take]
[Preserved for reference]
```

## Checkpoints

### After Source Review
```
════════════════════════════════════════════
CHECKPOINT: Source Material
════════════════════════════════════════════

I see you've shared material about [idea].

Before I profile this, help me understand YOUR relationship to it:

1. What made you save/notice this particular passage?
2. When do you find yourself thinking about this?
3. How would you explain this in your own words?

(This helps me capture YOUR take, not a textbook definition)
════════════════════════════════════════════
```

### After Draft Profile
```
════════════════════════════════════════════
CHECKPOINT: Profile Review
════════════════════════════════════════════

Here's a draft of your idea profile for [idea].

Does this capture YOUR thinking?

- Is "My Understanding" how YOU actually think about it?
- Are there better examples from YOUR experience?
- What connections to other ideas am I missing?

1. Looks good - save it
2. Adjust sections - [tell me what's off]
3. Add more - I have more to share about this
════════════════════════════════════════════
```

## File Management

- Save idea profiles to: `${CLAUDE_PLUGIN_ROOT}/../ideas/[idea-name].md`
- Use kebab-case for filenames: `second-order-effects.md`
- Update `references/connections.md` with new links
- Update `references/categories.md` if new category

## Key Questions to Ask

These prompts help extract personal resonance:

- "What were you struggling with when this idea helped?"
- "Can you give me an example from your own experience?"
- "How would you explain this at a dinner party?"
- "What's the 'aha' moment this idea creates?"
- "What's the opposite of this idea - what does it argue against?"
- "What other ideas in your library feel related?"

## Anti-Patterns

Never do these:

- **Don't be encyclopedic** - This isn't Wikipedia
- **Don't use source language verbatim** - Translate to their voice
- **Don't assume completeness** - Partial understanding is valid
- **Don't add canonical examples** - Only use THEIR examples
- **Don't over-structure** - Some sections can be sparse

## Reference Files

- `references/idea-template.md` - Blank template structure
- `examples/complete-idea-profile.md` - Annotated example
