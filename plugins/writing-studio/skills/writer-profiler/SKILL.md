---
name: Writer Profiler
description: This skill should be used when the user asks to "analyze my writing", "create a writer profile", "extract my writing style", "profile my voice", "analyze these samples", "build a style profile", "create my writing DNA", "analyze my author voice", or needs comprehensive analysis of writing samples to create a detailed writer profile that can power personalized writing assistants.
version: 1.0.0
---

# Writer Profiler

Comprehensive writing sample analysis to extract detailed writer profiles. This skill performs deep linguistic and stylistic analysis to create profiles that enable truly personalized writing assistants.

## Purpose

Create exhaustive writer profiles by analyzing writing samples across multiple dimensions. The output is a structured profile that captures everything needed to replicate or assist the writer's unique voice.

## When to Use

- Analyzing writing samples to create personalized assistants
- Building comprehensive style profiles for writers
- Extracting "writing DNA" from existing work
- Creating reusable writer configurations
- Profiling an author's voice for ghostwriting or editing

## Analysis Framework

### Input Requirements

**Minimum**: 1 writing sample (500+ words)
**Recommended**: 3-5 samples across different contexts (2,000+ words total)
**Ideal**: 10+ samples covering various topics and formats (5,000+ words)

More samples = more accurate profile. Diverse samples reveal consistent patterns vs. context-dependent variations.

### Analysis Dimensions

The profiler analyzes **12 core dimensions**:

1. **Voice Architecture**
2. **Tonal Signature**
3. **Structural Patterns**
4. **Vocabulary Fingerprint**
5. **Rhythm & Cadence**
6. **Rhetorical Devices**
7. **Cognitive Patterns**
8. **Emotional Register**
9. **Authority Stance**
10. **Reader Relationship**
11. **Topic Treatment**
12. **Distinctive Markers**

## Analysis Process

### Phase 1: Sample Ingestion

For each writing sample:
1. Record source, context, and purpose
2. Note word count and format type
3. Identify intended audience
4. Flag any atypical constraints (client brief, format requirements)

### Phase 2: First-Pass Analysis

Read all samples holistically to identify:
- Immediate voice impression
- Obvious patterns and habits
- Standout characteristics
- Initial personality signals

### Phase 3: Dimensional Deep Dive

Analyze each dimension systematically. See `references/analysis-dimensions.md` for detailed methodology.

**Voice Architecture Analysis:**
- Pronoun preferences and patterns
- Perspective consistency
- Narrative distance
- Speaker persona

**Tonal Signature Analysis:**
- Baseline tone identification
- Tonal range and flexibility
- Humor patterns (type, frequency, placement)
- Seriousness calibration

**Structural Patterns Analysis:**
- Opening strategies
- Section organization
- Paragraph construction
- Closing techniques
- Transition patterns

**Vocabulary Fingerprint Analysis:**
- Lexical sophistication level
- Domain-specific terminology usage
- Signature phrases and expressions
- Word frequency patterns
- Avoided words and constructions

**Rhythm & Cadence Analysis:**
- Sentence length distribution
- Clause complexity patterns
- Punctuation rhythm
- Pacing variations

**Rhetorical Devices Analysis:**
- Metaphor and simile usage
- Analogy patterns
- Repetition techniques
- Question usage
- Emphasis methods

**Cognitive Patterns Analysis:**
- Argument structure preferences
- Evidence presentation style
- Abstraction vs. concrete balance
- Causality expression
- Complexity handling

**Emotional Register Analysis:**
- Emotional vocabulary range
- Sentiment expression style
- Vulnerability level
- Enthusiasm patterns
- Restraint indicators

**Authority Stance Analysis:**
- Confidence expression
- Hedging patterns
- Certainty language
- Source attribution style
- Opinion presentation

**Reader Relationship Analysis:**
- Direct address patterns
- Assumed knowledge level
- Inclusion/exclusion signals
- Pedagogical approach
- Rapport building techniques

**Topic Treatment Analysis:**
- Depth vs. breadth preference
- Example usage patterns
- Abstraction levels
- Context provision
- Tangent handling

**Distinctive Markers Analysis:**
- Unique expressions
- Idiosyncratic patterns
- Signature moves
- Quirks and habits
- Distinguishing features

### Phase 4: Cross-Sample Validation

Compare patterns across all samples:
- Identify consistent patterns (core style)
- Note context-dependent variations
- Flag anomalies for investigation
- Calculate confidence scores

### Phase 5: Profile Synthesis

Compile findings into structured Writer Profile format.

## Output: Writer Profile

### Profile Structure

```yaml
---
profile_version: "1.0"
generated_from:
  sample_count: [N]
  total_words: [N]
  sample_types: ["type1", "type2"]
confidence_score: [0-100]
---

# Writer Profile: [Name/Identifier]

## Executive Summary
[2-3 sentence encapsulation of the writer's voice]

## Voice Architecture
pronoun_default: [I/we/you/one/they]
perspective: [first/second/third]
narrative_distance: [intimate/conversational/professional/distant]
persona_type: [guide/peer/expert/storyteller/analyst]

## Tonal Signature
baseline_tone: [description]
tonal_range: [narrow/moderate/wide]
humor:
  type: [dry/playful/sardonic/absent]
  frequency: [rare/occasional/frequent]
  placement: [openings/asides/throughout]
formality_spectrum: [1-10 scale with description]

## Structural Patterns
opening_strategies:
  primary: [type]
  secondary: [type]
  examples: ["...", "..."]
paragraph_style:
  typical_length: [sentences]
  density: [sparse/moderate/dense]
  structure: [topic-support/narrative/varied]
section_organization: [description]
transition_style: [explicit/implicit/mixed]
closing_patterns:
  primary: [type]
  examples: ["...", "..."]

## Vocabulary Fingerprint
lexical_level: [accessible/moderate/sophisticated/technical]
signature_phrases:
  - "[phrase]"
  - "[phrase]"
power_words:
  - "[word]"
  - "[word]"
avoided_constructions:
  - "[pattern]"
  - "[pattern]"
jargon_comfort: [avoids/minimal/moderate/embraces]
word_invention: [never/rare/occasional]

## Rhythm & Cadence
sentence_length:
  short_percentage: [%]
  medium_percentage: [%]
  long_percentage: [%]
  variation_pattern: [description]
clause_complexity: [simple/moderate/complex/varied]
punctuation_habits:
  em_dashes: [frequency and usage]
  semicolons: [frequency and usage]
  parentheticals: [frequency and usage]
  ellipses: [frequency and usage]
pacing: [description]

## Rhetorical Devices
metaphor_usage:
  frequency: [rare/moderate/frequent]
  types: [concrete/abstract/mixed]
  examples: ["...", "..."]
analogy_patterns: [description]
repetition_techniques: [description]
question_usage:
  rhetorical: [frequency]
  genuine: [frequency]
  placement: [description]

## Cognitive Patterns
argument_structure: [deductive/inductive/narrative/mixed]
evidence_style: [anecdotal/statistical/authoritative/experiential]
abstraction_preference: [concrete-first/abstract-first/balanced]
complexity_handling: [simplifies/embraces/layers]
causality_expression: [explicit/implicit/mixed]

## Emotional Register
emotional_vocabulary: [restrained/moderate/expressive]
vulnerability_level: [guarded/selective/open]
enthusiasm_expression: [subtle/moderate/effusive]
sentiment_balance: [analytical/balanced/emotive]

## Authority Stance
confidence_level: [tentative/balanced/assertive/authoritative]
hedging_patterns:
  frequency: [rare/moderate/frequent]
  types: ["...", "..."]
opinion_framing: [direct/qualified/embedded]
source_attribution: [heavy/moderate/light/implicit]

## Reader Relationship
direct_address: [frequent/occasional/rare]
assumed_knowledge: [none/basic/intermediate/expert]
inclusion_signals: ["...", "..."]
pedagogical_style: [didactic/collaborative/socratic/exploratory]
rapport_techniques: ["...", "..."]

## Topic Treatment
depth_preference: [surface/moderate/deep]
example_frequency: [every point/key points/sparingly]
context_provision: [extensive/moderate/minimal]
tangent_tolerance: [strict focus/occasional asides/exploratory]

## Distinctive Markers
signature_moves:
  - name: "[move name]"
    description: "[what it is]"
    example: "[example]"
unique_expressions:
  - "[expression]"
  - "[expression]"
identifying_quirks:
  - "[quirk]"
  - "[quirk]"
style_tells:
  - "[tell]"
  - "[tell]"

## Writing Assistant Configuration

### Replication Instructions
To write AS this author:
1. [Specific instruction]
2. [Specific instruction]
3. [Specific instruction]

### Editing Instructions
To edit FOR this author:
1. [Specific instruction]
2. [Specific instruction]
3. [Specific instruction]

### Voice Calibration Checklist
Before finalizing any output:
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

### Anti-Patterns
Never do these when writing for this author:
- [Anti-pattern 1]
- [Anti-pattern 2]
- [Anti-pattern 3]
```

## Confidence Scoring

Assign confidence scores based on:

| Factor | Impact |
|--------|--------|
| Sample count | +10 per sample (max 30) |
| Word volume | +1 per 500 words (max 20) |
| Sample diversity | +5 per distinct type (max 20) |
| Pattern consistency | +0-30 based on cross-sample validation |

**Score Interpretation:**
- 90-100: High confidence, profile highly reliable
- 70-89: Good confidence, profile reliable for most purposes
- 50-69: Moderate confidence, profile useful but verify edge cases
- Below 50: Low confidence, gather more samples

## Checkpoints

Present checkpoints during analysis:

**After Sample Review:**
```
═══════════════════════════════════════════
📍 CHECKPOINT: Sample Assessment
═══════════════════════════════════════════

I've reviewed your [N] samples ([X] total words).

**Sample Quality:**
- Diversity: [assessment]
- Volume: [sufficient/could use more]
- Representativeness: [assessment]

**Initial Impressions:**
- [Key observation 1]
- [Key observation 2]
- [Key observation 3]

**Options:**
1. **Proceed** - Analyze these samples
2. **Add samples** - Provide more writing for better accuracy
3. **Clarify context** - Tell me more about specific samples

Ready to proceed? (1/2/3)
═══════════════════════════════════════════
```

**After Analysis:**
```
═══════════════════════════════════════════
📍 CHECKPOINT: Profile Review
═══════════════════════════════════════════

Analysis complete. Confidence score: [X]/100

**Key Profile Elements:**
- Voice: [summary]
- Tone: [summary]
- Distinctive features: [summary]

**Options:**
1. **Generate full profile** - Create comprehensive writer profile
2. **Deep dive** - Explore specific dimensions in more detail
3. **Validate findings** - Confirm key observations with you

How should we proceed? (1/2/3)
═══════════════════════════════════════════
```

## Usage Notes

- Always explain what each profile element means
- Provide examples from the actual samples when possible
- Note areas of uncertainty or insufficient data
- Suggest additional samples for weak areas
- Offer to regenerate sections if writer disagrees

## Additional Resources

### Reference Files
- **`references/analysis-dimensions.md`** - Detailed methodology for each dimension
- **`references/profile-interpretation.md`** - How to use profiles effectively

### Example Files
- **`examples/complete-writer-profile.md`** - Full example profile with annotations
