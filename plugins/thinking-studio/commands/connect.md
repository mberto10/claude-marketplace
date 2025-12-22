---
name: connect
description: Explore connections between your profiled ideas
arguments:
  - name: ideas
    description: Which ideas to connect (comma-separated, or "all")
    required: false
---

# Connect Ideas

Explore and map connections between your profiled ideas.

## Your Task

Help the user discover and articulate connections between ideas in their thinking library. These connections are PERSONAL - bridges that make sense to THEM, not canonical relationships.

## Process

1. **Select Ideas to Connect**
   - If `$ARGUMENTS.ideas` provided, parse the comma-separated list
   - If "all", load all profiles from `${CLAUDE_PLUGIN_ROOT}/ideas/`
   - If none specified, show their idea library and ask which to explore

2. **Load Profiles**
   - Read each idea profile
   - Note existing `connects_to` fields
   - Check `${CLAUDE_PLUGIN_ROOT}/references/connections.md` for existing mappings

3. **Explore Connections**
   For each pair, consider:
   - Do they address similar problems differently?
   - Does one extend or refine the other?
   - Are they "the same thing" at a deeper level?
   - Do they create productive tension?
   - When would you use one vs. the other?

4. **Articulate in Their Voice**
   Connections should reflect their thinking:
   - "These feel related because..."
   - "I reach for X when... but Y when..."
   - "For me, X and Y are almost the same thing"

5. **Update References**
   - Offer to update idea profiles with new `connects_to` links
   - Offer to add bridges to `${CLAUDE_PLUGIN_ROOT}/references/connections.md`

## Key Questions to Explore

- "Do these ideas feel like siblings or opposites?"
- "When would you reach for one vs. the other?"
- "Is there a meta-idea that contains both?"
- "Do these create a useful tension?"

## Output Format

```
Connecting: [idea-1] ↔ [idea-2]

Relationship: [type - siblings/tension/extension/same-thing/complements]

My link: [articulated in their voice]

When to use [idea-1]: [situations]
When to use [idea-2]: [situations]

Update profiles with this connection? (y/n)
```

## Discovering New Clusters

If patterns emerge across multiple ideas:

```
Possible cluster emerging: [cluster name]

Ideas: [idea-1], [idea-2], [idea-3]

What they share for you: [articulation]

Add this cluster to your categories? (y/n)
```
