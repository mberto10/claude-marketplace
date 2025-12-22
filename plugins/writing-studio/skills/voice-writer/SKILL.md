---
name: Voice Writer
description: This skill should be used when the user asks to "write something", "draft content", "write in X style", "use my profiles", "write like [author]", "blend styles", "mix voices", "combine writing styles", or wants to create content using their repertoire of writer profiles. Loads all available profiles and responds to conversational direction.
version: 1.0.0
---

# Voice Writer

A flexible writing skill that loads the user's repertoire of writer profiles and responds to conversational direction. No rigid arguments—natural language direction drives the writing.

## Purpose

Write content using any combination of stored writer profiles. The skill understands natural direction:
- "Write this in the Blake Crouch style"
- "More philosophical, less technical"
- "Keep the rhythm but soften the authority"
- "Blend the wonder of profile A with the brevity of profile B"

## On Activation

### Step 1: Load Profile Repertoire

Scan `plugins/writing-studio/profiles/` for all `.md` files.

For each profile found:
1. Read the file
2. Extract executive summary
3. Note key dimensions (voice, tone, rhythm, signature moves)
4. Build internal reference map

### Step 2: Present Available Voices

```
═══════════════════════════════════════════
📚 VOICE REPERTOIRE
═══════════════════════════════════════════

Loaded [N] writer profiles:

**[Profile 1 Name]**
> [Executive summary - 1-2 sentences]
Key: [2-3 distinctive features]

**[Profile 2 Name]**
> [Executive summary - 1-2 sentences]
Key: [2-3 distinctive features]

═══════════════════════════════════════════

Options:
- Name a profile to use
- Describe the desired voice
- Request blending of specific elements
- Describe content and receive voice suggestions

═══════════════════════════════════════════
```

## Understanding Direction

Parse user input for these patterns:

| Input Type | Example | Action |
|------------|---------|--------|
| Explicit profile | "Use Blake Crouch style" | Load as primary |
| Dimension targeting | "More philosophical" | Adjust specific dimension |
| Blending request | "A's ideas with B's brevity" | Combine elements |
| Mood description | "Something contemplative" | Match to fitting profiles |

See `references/direction-parsing.md` for detailed parsing logic.

## Writing Process

### Single Profile

1. Load core elements from profile (voice, tone, structure, rhythm)
2. Load distinctive markers (signature moves, anti-patterns)
3. Apply calibration checklist before each section
4. Write content
5. Present draft with applied elements noted

### Blended Profiles

1. Identify which dimensions to pull from each profile
2. Resolve conflicts (ask user if unclear)
3. Default to primary profile for unspecified dimensions
4. Note the blend in output metadata

See `references/blending-guide.md` for dimension compatibility.

## Feedback Loop

After each draft, remain responsive to direction:

```
═══════════════════════════════════════════
📍 DRAFT CHECK
═══════════════════════════════════════════

[Preview of content]

**Current voice blend:**
- [Primary influence]: [elements used]
- [Secondary influence]: [elements used]

Adjustment options:
- "More X, less Y"
- "Continue" (voice is correct)
- "Switch to [profile]"
- "Add [element] from [profile]"

═══════════════════════════════════════════
```

### Feedback Types

| Feedback | Action |
|----------|--------|
| Additive ("Add more wonder") | Increase target dimension |
| Subtractive ("Less dense") | Reduce target dimension |
| Shifting ("Warmer tone") | Adjust emotional register |
| Profile switch ("Switch to X") | Load new profile |

## Output Format

Each output includes voice metadata:

```markdown
---
voice_blend:
  primary: [profile name]
  elements: [dimensions used]
  secondary: [profile name, if any]
  custom_adjustments: [user-directed tweaks]
---

[Written content]

---
**Voice notes:** [What makes this voice work]
```

## Profile Not Found

When user references a non-existent profile:

```
═══════════════════════════════════════════
📚 PROFILE NOT FOUND
═══════════════════════════════════════════

No profile for "[requested name]" exists.

Options:
1. **Create it** - Provide samples to build profile
2. **Approximate** - Write in general style without formal profile
3. **Suggest alternative** - Show similar existing profiles

═══════════════════════════════════════════
```

## Adding Profiles Mid-Session

Users can add profiles during a session:

"Profile this passage and add it to my repertoire"

→ Use writer-profiler skill to analyze
→ Save to `profiles/` directory
→ Add to active repertoire

## Storage

Profiles location: `plugins/writing-studio/profiles/`

Each profile follows the Writer Profile structure from the writer-profiler skill.

## Additional Resources

### Reference Files

For detailed guidance, consult:
- **`references/direction-parsing.md`** - How to parse user direction
- **`references/blending-guide.md`** - Dimension compatibility and conflict resolution
- **`references/feedback-patterns.md`** - Common feedback patterns and responses

### Example Files

Working examples in `examples/`:
- **`examples/single-profile-session.md`** - Complete single-profile writing session
- **`examples/blended-session.md`** - Multi-profile blending interaction
