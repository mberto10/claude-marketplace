# Style Analysis Guide

Detailed methodology for analyzing user writing samples with user-guided focus.

## Analysis Philosophy

Style analysis serves the user, not the analyst. Avoid imposing external style rules—instead, discover and codify what makes the user's writing distinctly theirs.

### Principles

1. **User-guided focus**: Ask what matters before diving deep
2. **Descriptive, not prescriptive**: Document what IS, not what SHOULD BE
3. **Actionable output**: Every observation should inform future writing
4. **Confirmation before codification**: Verify observations with the user

## Pre-Analysis Questions

Before reading samples, establish context:

### Essential Questions

```
Before I analyze your sample(s), help me focus:

1. What aspects of this writing do you most want to preserve in future work?
2. Are there elements in this sample you actually want to change or avoid?
3. Is this sample representative of your "true voice" or a specific context?
4. What type of writing is this (technical, creative, business, personal)?
```

### Follow-up Questions

Based on initial answers:

- "You mentioned [X]—can you give me an example of what you mean?"
- "When you say you want to preserve [Y], what specifically about it matters?"
- "Is this sample your best work, typical work, or aspirational work?"

## Analysis Categories

### 1. Voice Markers

**What to look for:**
- Pronoun usage (I, we, you, one, they)
- Level of formality (contracted vs. formal language)
- Personality signals (humor, warmth, authority, skepticism)
- Directness vs. hedging patterns

**How to document:**

```yaml
voice:
  pronoun_preference: first-person plural
  formality_level: medium
  personality_markers:
    - dry humor in parentheticals
    - occasional self-deprecation
    - confident assertions
  directness: high (minimal hedging)
```

### 2. Structural Patterns

**What to look for:**
- Paragraph length and variation
- Section organization patterns
- Opening and closing tendencies
- Use of headers, lists, quotes
- Transition patterns

**How to document:**

```yaml
structure:
  paragraph_length:
    opening: short (2-3 sentences)
    body: medium (4-6 sentences)
    closing: short (1-2 sentences)
  section_pattern: "problem → insight → application"
  list_usage: sparingly, for emphasis
  transition_style: implicit connections, minimal explicit bridges
```

### 3. Vocabulary Patterns

**What to look for:**
- Preferred words and phrases
- Words consistently avoided
- Technical vs. accessible language balance
- Sentence starters and connectors
- Signature expressions

**How to document:**

```yaml
vocabulary:
  preferred_words:
    - use (not utilize)
    - help (not facilitate)
    - actually (for emphasis)
  prohibited_words:
    - synergy
    - leverage (as verb)
    - stakeholder
  technical_balance: accessible first, technical when necessary
  signature_phrases:
    - "Here's the thing"
    - "The real question is"
```

### 4. Rhythm and Flow

**What to look for:**
- Sentence length variation
- Punctuation patterns (em-dashes, semicolons, parentheticals)
- Paragraph transitions
- Pacing (fast/slow sections)
- Reading rhythm

**How to document:**

```yaml
rhythm:
  sentence_length: varied (mix short punchy with longer explanatory)
  punctuation_preferences:
    - em-dashes for asides
    - avoids semicolons
    - parentheticals for humor
  pacing: fast openings, slower middles, quick conclusions
```

### 5. Content Patterns

**What to look for:**
- How arguments are structured
- Use of examples and evidence
- Balance of abstract/concrete
- Handling of counterarguments
- Source of authority (personal experience, research, logic)

**How to document:**

```yaml
content:
  argument_structure: claim → evidence → implication
  example_frequency: high (every major point illustrated)
  abstract_concrete_ratio: concrete-heavy
  counterarguments: acknowledged briefly, not dwelt upon
  authority_source: personal experience primary, research secondary
```

## Analysis Process

### Step 1: First Read (Holistic)

Read the sample once without taking notes. Get the feel of the voice.

**After first read, note:**
- Overall impression of personality
- General sense of formality
- Immediate standout features

### Step 2: User-Guided Focus

Present initial impressions and ask user to guide deeper analysis:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Analysis Focus
═══════════════════════════════════════════

My initial impression of your sample:
- [Voice observation]
- [Structure observation]
- [Vocabulary observation]

What aspects should I analyze more deeply?

1. Voice & Personality
2. Structure & Flow
3. Vocabulary & Phrasing
4. All of the above
═══════════════════════════════════════════
```

### Step 3: Focused Analysis

Based on user guidance, analyze specific categories in depth.

**For each focus area:**
1. Identify patterns (what repeats?)
2. Note exceptions (what breaks the pattern?)
3. Extract specific examples
4. Form actionable observations

### Step 4: Pattern Extraction

Convert observations into style guide entries:

**From observation:**
> "The writer uses short opening paragraphs (2-3 sentences) that hook with a question or surprising statement, then expands in subsequent paragraphs."

**To style guide entry:**
```yaml
paragraph_style:
  opening: short hook (2-3 sentences), question or surprise
  body: expand and develop (4-6 sentences)
```

### Step 5: Confirmation Checkpoint

Present findings and ask for confirmation:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Analysis Confirmation
═══════════════════════════════════════════

Here's what I observed about your [focus area]:

**Voice Markers:**
- [Observation 1]
- [Observation 2]

**Specific Examples:**
> "[Quote from sample]"
> "[Quote from sample]"

**Options:**
1. Accurate - Save to style guide
2. Partially correct - Tell me what's off
3. Redo - Analyze again with different focus
═══════════════════════════════════════════
```

## Handling Multiple Samples

When user provides multiple samples:

### Same Type

If all samples are similar writing types:
- Look for consistent patterns across samples
- Note any evolution or variation
- Identify the "core voice" that persists

### Different Types

If samples represent different writing contexts:
- Analyze each separately first
- Identify what stays constant (core voice)
- Document context-specific adaptations

```yaml
writing_types:
  technical:
    formality_override: high
    structure_override: header-heavy
    notes: "More precise language, less personality"

  creative:
    formality_override: low
    structure_override: flowing paragraphs
    notes: "Full personality, more experimental"

  core_voice:
    - first-person plural when possible
    - direct statements
    - concrete examples
```

## Common Pitfalls

### Over-Analysis

**Problem:** Documenting every tiny detail, creating unusable style guide
**Solution:** Focus on patterns that repeat and matter to the user

### Prescription Creep

**Problem:** Suggesting "improvements" instead of documenting actual style
**Solution:** Only document what IS, not what COULD BE

### Ignoring Context

**Problem:** Treating a business email sample as representative of all writing
**Solution:** Always ask about sample representativeness

### Rigid Categorization

**Problem:** Forcing observations into predetermined categories
**Solution:** Let patterns emerge, then categorize

## Output Format

Final style analysis should produce entries for the style guide:

```yaml
---
# Core Style Elements
tone: [derived from analysis]
voice: [derived from analysis]
formality: [derived from analysis]

# Specific Patterns
sentence_length: [derived from analysis]
paragraph_style: [derived from analysis]

# Vocabulary
prohibited_words: [derived from analysis]
vocabulary_preferences: [derived from analysis]

# Type-Specific Overrides
writing_types:
  [type]:
    [overrides]
---

## Example Excerpts

### Opening Hooks
> "[Example from analysis]"

### Transitions
> "[Example from analysis]"

### Conclusions
> "[Example from analysis]"

## Style Notes

[User-confirmed observations that don't fit elsewhere]
[Contextual preferences]
[Evolution notes if relevant]
```

## Iteration

Style guides should evolve:

1. **Initial creation**: Based on first analysis
2. **Refinement**: Updated after using in real writing
3. **Expansion**: Add new writing types as needed
4. **Pruning**: Remove rules that don't help

After each writing session, ask:
- "Did the style guide help capture your voice?"
- "What was missing or wrong?"
- "Should we update any preferences?"
