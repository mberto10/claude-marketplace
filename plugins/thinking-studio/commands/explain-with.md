---
name: explain-with
description: Explain something using your profiled ideas and analogies
arguments:
  - name: topic
    description: What to explain
    required: true
  - name: idea
    description: Which idea(s) to use for explanation
    required: false
---

# Explain With

Explain a topic using your personal thinking patterns and analogies.

## Your Task

Help the user explain something using THEIR mental models, THEIR analogies, THEIR examples. The explanation should sound like them, not like a textbook.

## Process

1. **Understand What to Explain**
   - Topic from `$ARGUMENTS.topic`
   - Clarify audience/context if helpful

2. **Select Ideas to Use**
   - If `$ARGUMENTS.idea` specified, load that profile
   - Otherwise, scan `${CLAUDE_PLUGIN_ROOT}/ideas/` for relevant ideas
   - Check `${CLAUDE_PLUGIN_ROOT}/references/connections.md` for related concepts

3. **Build Explanation Using Their Patterns**
   From their idea profiles, draw on:
   - "My Explanatory Moves" - how they teach this idea
   - "Examples That Stuck" - their go-to illustrations
   - "My Understanding" - their framing
   - Their analogies and language

4. **Craft the Explanation**
   - Use their voice and framing
   - Reference their examples
   - Connect to their other ideas if relevant

## Key Principles

- **Their analogies, not generic ones**
- **Their examples, not textbook examples**
- **Their level of understanding** - don't exceed what's in profiles
- **Their teaching style** - match how they explain things

## Output Format

Present the explanation, then note which ideas you drew from:

```
[Explanation in their voice/style]

---
Drew from:
- [idea-1]: Used your analogy of [X]
- [idea-2]: Applied your framing of [Y]
```

## Example

If they have an "inversion" profile with the example "instead of asking 'how do I make this succeed?' I ask 'what would guarantee failure?'"

And they ask to explain project planning:

"Think about your project the way you'd think about inversion - don't start with 'how do we succeed?' Start with 'what would guarantee this fails?' Identify those failure modes first, then design around them..."
