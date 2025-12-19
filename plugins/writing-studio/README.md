# Writing Studio

A comprehensive, interactive writing assistant plugin for Claude Code that maintains your personal writing style across the full creative workflow.

## Features

- **Style Learning**: Learns your writing style from samples and preferences
- **Writer Profiling**: Deep analysis of writing samples to create comprehensive writer profiles
- **Full Workflow Support**: Brainstorming → Planning → Drafting → Editing
- **Interactive Checkpoints**: Structured decision points throughout the process
- **Flexible Access**: Use the main `/write` command or individual stage commands
- **Personalized Assistants**: Build writing assistants that truly match your voice

## Commands

| Command | Description |
|---------|-------------|
| `/write <topic>` | Start a complete writing session with guided workflow |
| `/setup-style [file]` | Create or update your style guide interactively |
| `/profile-writer <samples>` | Create comprehensive writer profile from samples |
| `/generate-assistant [profile]` | Transform profile into assistant instructions |
| `/brainstorm <topic>` | Generate and explore ideas |
| `/plan <topic>` | Create structured outlines |
| `/draft <outline>` | Write content following your style |
| `/edit <content>` | Refine and polish writing |

## Setup

1. Run `/setup-style` to create your personal style guide
2. Optionally provide sample documents for style analysis
3. Start writing with `/write <your topic>`

## Style Configuration

Your style preferences are stored in `.claude/writing-studio.local.md` with:

- **YAML frontmatter**: tone, voice, formality, vocabulary preferences
- **Markdown body**: examples, detailed notes, contextual preferences

### Example Style File

```markdown
---
tone: conversational yet professional
voice: first-person plural (we)
formality: medium
sentence_length: varied, mix of short punchy and longer explanatory
prohibited_words:
  - synergy
  - leverage (as verb)
  - utilize
vocabulary_preferences:
  - prefer "use" over "utilize"
  - prefer "help" over "facilitate"
---

## Example Excerpts

[Your writing samples here]

## Notes

- Always lead with the key insight
- Use concrete examples over abstract concepts
```

## Workflow

Each agent uses **Structured Checkpoints** - clear decision points with numbered options:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Direction Selection
═══════════════════════════════════════════

Based on our brainstorming, here are the strongest directions:

1. [Option A] - Focus on practical benefits
2. [Option B] - Lead with the problem/solution angle
3. [Option C] - Start with a compelling story

Which direction would you like to pursue? (1/2/3)
```

## Writer Profiling

For writers who want a truly personalized assistant, use `/profile-writer` to create a comprehensive writer profile from your existing work.

### What Gets Analyzed

The profiler examines **12 dimensions** of your writing:

1. **Voice Architecture** - Pronouns, perspective, narrative distance
2. **Tonal Signature** - Baseline tone, humor, formality
3. **Structural Patterns** - Openings, paragraphs, transitions, closings
4. **Vocabulary Fingerprint** - Signature phrases, power words, avoided terms
5. **Rhythm & Cadence** - Sentence length, punctuation patterns, pacing
6. **Rhetorical Devices** - Metaphors, analogies, repetition
7. **Cognitive Patterns** - Argument structure, evidence style, abstraction level
8. **Emotional Register** - Vocabulary range, vulnerability, enthusiasm
9. **Authority Stance** - Confidence level, hedging, opinion framing
10. **Reader Relationship** - Direct address, assumed knowledge, pedagogy
11. **Topic Treatment** - Depth preference, example frequency, tangent handling
12. **Distinctive Markers** - Signature moves, unique expressions, style tells

### Using Your Profile

Once profiled, run `/generate-assistant` to create ready-to-use instructions:

| Output Type | Use Case |
|-------------|----------|
| **Full System Prompt** | Configure an AI assistant with complete instructions |
| **Voice Replication Guide** | Instructions for writing AS you |
| **Editing Guide** | Instructions for editing TO MATCH your style |
| **Quick Reference Card** | Condensed 1-page style rules |

### Sample Requirements

| Samples | Confidence |
|---------|------------|
| 1 (500+ words) | Basic profile |
| 3-5 (2,000+ words) | Good accuracy |
| 10+ (5,000+ words) | High confidence |

More diverse samples (different topics, formats) produce better profiles.

## License

MIT
