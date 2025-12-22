---
name: brainstorm
description: Generate ideas using your thinking patterns
arguments:
  - name: topic
    description: What to brainstorm about
    required: true
  - name: mode
    description: "Mode: applications, extensions, inversions, wild"
    required: false
---

# Brainstorm

Generate ideas by filtering through your personal thinking patterns.

## Your Task

Help the user brainstorm using THEIR mental models as lenses. Every idea should be grounded in or filtered through their profiled thinking.

## Modes

### Applications (default)
"How could my ideas apply to [topic]?"
- Take their profiled ideas and find applications to the topic
- Use their examples as analogy anchors

### Extensions
"How could [topic] extend my ideas?"
- What new dimensions does this topic add to their thinking?
- What would a new idea profile look like here?

### Inversions
"What's the opposite? What am I missing?"
- Apply inversion thinking to the topic
- What would their ideas argue AGAINST?
- What blind spots might their thinking have?

### Wild
"Unexpected connections"
- Cross-pollinate ideas that don't obviously connect
- Look for surprising bridges
- "What if [idea-1] and [idea-2] had a child?"

## Process

1. **Load Their Thinking Library**
   - Read all profiles from `${CLAUDE_PLUGIN_ROOT}/ideas/`
   - Load connections from `${CLAUDE_PLUGIN_ROOT}/references/connections.md`
   - Understand their mental model landscape

2. **Apply Mode to Topic**
   - Generate ideas through the lens of their profiles
   - Reference their specific framings, examples, analogies
   - Show how each brainstorm connects to their thinking

3. **Present Ideas**
   - Ground each idea in their existing thinking
   - Note which profiles informed it
   - Flag ideas that might become new profiles

## Output Format

```
Brainstorming: [topic]
Mode: [mode]
Using: [relevant ideas from their library]

---

1. [Idea]
   Via your thinking on [idea-name]: [how it connects]

2. [Idea]
   Combining [idea-1] + [idea-2]: [synthesis]

3. [Idea]
   Extending your [example from profile]: [extension]

---

New profile candidates:
- [Idea that might deserve its own profile]
```

## Key Principles

- **Every idea should trace back to their thinking**
- **Use their language and examples**
- **Don't introduce foreign mental models** without flagging them
- **Note gaps** - "Your library doesn't address X, might be worth profiling"

## If Library Empty

"Your thinking library is empty - I don't have your mental models to brainstorm with yet. Want to profile some ideas first? Share passages or concepts that resonate with you."
