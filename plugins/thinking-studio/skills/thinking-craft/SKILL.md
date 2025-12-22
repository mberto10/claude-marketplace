---
name: Thinking Craft
description: This skill should be used when the user asks to "think through", "help me reason about", "apply my ideas to", "analyze using my thinking", "brainstorm with my models", or wants to work through a problem using their profiled thinking patterns.
version: 1.0.0
---

# Thinking Craft

Apply the user's profiled thinking patterns to problems, decisions, and situations.

## Purpose

Use the user's personal idea library as the lens for thinking. Every analysis, brainstorm, or explanation should be grounded in THEIR mental models, not generic frameworks.

## When to Use

- User wants to think through a problem
- User wants to apply their ideas to a situation
- User wants to brainstorm using their mental models
- User asks "how would I think about this?"
- User wants explanations in their conceptual language

## Core Principle

**Their thinking, not generic thinking.** The value is in using THEIR profiled ideas, THEIR examples, THEIR framings - not textbook mental models.

## Loading the Thinking Library

Before any thinking task:

1. Read available idea profiles from `${CLAUDE_PLUGIN_ROOT}/ideas/`
2. Load connections from `${CLAUDE_PLUGIN_ROOT}/references/connections.md`
3. Review categories from `${CLAUDE_PLUGIN_ROOT}/references/categories.md`

If the library is empty, note this and offer to help build it.

## Applying Ideas

When using an idea profile:

### Use Their Understanding
- Reference "My Understanding" not textbook definitions
- Frame things the way THEY frame them

### Use Their Examples
- Draw analogies from "Examples That Stuck"
- Don't introduce examples they haven't profiled

### Use Their Trigger Questions
- From "How I Use It" - when do they reach for this?
- Apply the same triggers to the current situation

### Use Their Explanatory Moves
- From "My Explanatory Moves" - how do they teach this?
- Mirror their teaching style

### Respect Their Tensions
- Note ideas from "Tensions & Edges"
- Don't oversell an idea beyond their stated confidence

## Thinking Modes

### Analysis Mode
"How do my ideas explain this?"
- Map the situation to relevant idea profiles
- Show which ideas apply and how
- Note gaps where no profiled ideas fit

### Decision Mode
"Which of my ideas helps me decide?"
- Identify decision-relevant ideas
- Apply their framing to the options
- Note when ideas conflict

### Brainstorm Mode
"What do my ideas suggest I try?"
- Generate possibilities through their lenses
- Ground each idea in their existing thinking
- Flag which profiles informed each suggestion

### Explanation Mode
"How would I explain this?"
- Build explanation using their mental models
- Use their examples and analogies
- Match their teaching style

## Showing Your Work

Always make explicit which ideas you're using:

```
Using your thinking on [idea-name]:
- Your framing: [from their profile]
- Applied here: [how it maps]
- Implication: [insight]
```

## Handling Gaps

When their library doesn't cover something:

"Your thinking library doesn't have an idea that directly addresses [X]. Options:
1. Continue with adjacent ideas: [list relevant-ish profiles]
2. Profile a new idea: Do you have source material about [X]?
3. Note the gap: This might be worth adding to your library"

Don't silently introduce foreign mental models.

## Integration with Writing Studio

If the user has writing profiles:
- Thinking Studio provides the WHAT (ideas, analysis)
- Writing Studio provides the HOW (voice, style)
- Can combine: "Explain [topic] using [idea] in [voice]"

## Reference Files

- `references/application-patterns.md` - Common ways to apply ideas
