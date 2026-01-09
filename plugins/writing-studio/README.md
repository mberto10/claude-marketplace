# Writing Studio

A comprehensive writing assistant plugin for Claude Code with quality loop workflow: deep discovery, voice profiles, iterative self-critique, and publication-ready output.

## Features

- **Quality Loop Workflow**: Iterative write → critique → iterate cycle until publication-ready
- **Deep Discovery**: Extensive questioning to understand complex ideas before writing
- **Writer Profiling**: 12-dimension analysis to create comprehensive voice profiles
- **Self-Critique**: Rigorous evaluation against voice profiles with scoring and weakness identification
- **Interactive Checkpoints**: Structured decision points with AskUserQuestion throughout
- **Voice Matching**: Score drafts against profiles (1-10) with publish test
- **Full Workflow Support**: Discover → Learn → Ideate → Plan → Write → Critique → Polish → Publish

## Commands

| Command | Description |
|---------|-------------|
| `/write-loop <topic>` | **NEW**: Start quality loop workflow with iterative critique |
| `/write <topic>` | Start a complete writing session with guided workflow |
| `/setup-style [file]` | Create or update your style guide interactively |
| `/profile-writer <samples>` | Create comprehensive writer profile from samples |
| `/generate-assistant [profile]` | Transform profile into assistant instructions |
| `/brainstorm <topic>` | Generate and explore ideas |
| `/plan <topic>` | Create structured outlines |
| `/draft <outline>` | Write content following your style |
| `/edit <content>` | Refine and polish writing |

## Quality Loop Workflow

```
DISCOVER → LEARN → IDEATE → PLAN → WRITE → CRITIQUE ←→ ITERATE → POLISH → PUBLISH
                                              ↑              │
                                              └──── NO ──────┘
```

### The Loop

1. **DISCOVER**: Deep understanding of your idea through extensive questioning
2. **LEARN**: Load voice profile as the quality rubric
3. **IDEATE**: Generate unique angles, select the best direction
4. **PLAN**: Create structural outline
5. **WRITE**: Draft with full voice commitment
6. **CRITIQUE**: Score against profile, identify weaknesses, decide pass/iterate
7. **ITERATE**: Address weaknesses systematically (loops back to CRITIQUE)
8. **POLISH**: Final editing pass
9. **PUBLISH**: Export with metadata and iteration history

### Quality Gates

A draft passes when:
- Voice match score ≥ 8/10
- Publish test = PROUD ("Would the author actually publish this?")
- Critical weaknesses = 0
- Overall score ≥ 7.5

### Usage

```bash
# Start quality loop with a topic
/write-loop "Why most productivity advice fails"

# Specify voice profile
/write-loop "The future of remote work" --voice steven-pinker

# Set iteration limits
/write-loop "My leadership philosophy" --max-iterations 5 --threshold 8
```

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
