---
name: Humor Profiler
description: This skill should be used when the user asks to "analyze comedy style", "create a humor profile", "extract comedic voice", "profile a comedian", "analyze stand-up samples", "capture comedic timing", "build a comedy profile", "imitate humor style", or needs comprehensive analysis of comedy material to create profiles for generating speeches, roasts, satirical content, or entertainment writing.
version: 1.0.0
---

# Humor Profiler

Comprehensive comedy and humor analysis to extract detailed profiles for replicating or generating content in specific comedic styles. This skill analyzes comedy material across multiple dimensions to capture the mechanics, voice, and distinctive patterns that make humor work.

## Purpose

Create exhaustive humor profiles by analyzing comedy samples across specialized dimensions. The output is a structured profile that captures everything needed to generate speeches, roasts, satirical content, or entertainment writing in a specific comedic voice.

## When to Use

- Analyzing comedy material to create speech templates
- Building humor profiles for roast writing
- Extracting comedic patterns from stand-up transcripts
- Creating reusable comedy configurations for content generation
- Profiling satirical voices for parody or commentary
- Generating entertainment content in specific styles
- Preparing humorous speeches (wedding, corporate, tribute)

## Analysis Framework

### Input Requirements

**Minimum**: 1 comedy sample (5+ minutes of material or 1,000+ words)
**Recommended**: 3-5 samples across different contexts (15+ minutes or 3,000+ words)
**Ideal**: Full special/set or 10+ samples covering various topics (30+ minutes or 6,000+ words)

**Sample Types That Work:**
- Stand-up transcripts
- Comedy essays or columns
- Satirical articles
- Roast speeches
- Late-night monologues
- Comedy podcast segments
- Humorous speeches
- Satirical fiction
- Video transcripts (with timing notes if available)

More samples = more accurate profile. Diverse samples reveal consistent patterns vs. situational variations.

### Analysis Dimensions

The humor profiler analyzes **12 comedy-specific dimensions**:

1. **Comedy Persona**
2. **Humor Mechanics**
3. **Comedy Types**
4. **Target Selection**
5. **Delivery Style**
6. **Timing Patterns**
7. **Callback & Layering**
8. **Audience Relationship**
9. **Taboo Navigation**
10. **Sincerity Balance**
11. **Vocabulary & Language**
12. **Signature Bits**

## Analysis Process

### Phase 1: Sample Ingestion

For each comedy sample:
1. Record source, context, and venue type
2. Note length and format (stand-up, written, speech)
3. Identify intended audience
4. Flag any constraints (corporate event, late-night TV, podcast)
5. Note performance elements if available (timing cues, audience reactions)

### Phase 2: First-Pass Analysis

Experience all samples to identify:
- Immediate comedic impression
- Obvious patterns and recurring bits
- Standout jokes or techniques
- Overall comedic persona
- What makes this funny (or not)

### Phase 3: Dimensional Deep Dive

Analyze each dimension systematically. See `references/comedy-dimensions.md` for detailed methodology.

**Comedy Persona Analysis:**
- Who is the "character" performing?
- What's their relationship to the material?
- How do they present themselves?
- What's their comedic worldview?

**Humor Mechanics Analysis:**
- Setup/punchline structures
- Misdirection techniques
- Callback patterns
- Rule of three usage
- Tension and release patterns

**Comedy Types Analysis:**
- Dominant humor modes (observational, absurdist, satirical, etc.)
- Secondary modes
- Genre blending
- Format preferences

**Target Selection Analysis:**
- Self-deprecation patterns
- External targets (institutions, groups, ideas)
- Absurdity as target
- Audience targeting
- Target protection (who's off-limits)

**Delivery Style Analysis:**
- Energy level
- Affect/deadpan spectrum
- Physicality indicators
- Pacing preferences
- Persona consistency

**Timing Patterns Analysis:**
- Beat placement
- Build speed
- Pause usage
- Punchline landing
- Rhythm variations

**Callback & Layering Analysis:**
- How early material returns
- Running bit structures
- Joke interconnections
- Escalation patterns
- Payoff spacing

**Audience Relationship Analysis:**
- Inclusive vs. provocative
- Direct address patterns
- Crowd work style
- Assumed knowledge
- Complicity creation

**Taboo Navigation Analysis:**
- Edge comfort level
- Sensitive topic handling
- Redemption strategies
- Line placement
- Controversy approach

**Sincerity Balance Analysis:**
- Genuine moments frequency
- Earnestness integration
- Tonal shift handling
- Heart beneath humor
- Vulnerability use

**Vocabulary & Language Analysis:**
- Register (clean/vulgar)
- Word choice patterns
- Catchphrases
- Language play (puns, wordplay)
- Profanity patterns

**Signature Bits Analysis:**
- Recurring themes
- Trademark moves
- Identifiable patterns
- Unique techniques
- "Only they would do this"

### Phase 4: Cross-Sample Validation

Compare patterns across all samples:
- Identify consistent comedic patterns
- Note context-dependent variations
- Flag one-time vs. recurring techniques
- Calculate confidence scores

### Phase 5: Profile Synthesis

Compile findings into structured Humor Profile format.

## Output: Humor Profile

### Profile Structure

```yaml
---
profile_version: "1.0"
profile_type: "humor"
generated_from:
  sample_count: [N]
  total_duration: [minutes] OR total_words: [N]
  sample_types: ["stand-up", "written", "speech"]
  era_range: [years if applicable]
confidence_score: [0-100]
---

# Humor Profile: [Name/Identifier]

## Executive Summary
[2-3 sentence encapsulation of the comedic voice and what makes it distinctive]

## Comedy Persona
character_type: [everyman/neurotic/provocateur/storyteller/absurdist/etc.]
worldview: [how they see the world comedically]
relationship_to_material: [inside/outside/above/below]
self_presentation: [loser/winner/observer/victim/villain]
comedic_philosophy: [what's funny to them and why]

## Humor Mechanics

### Setup/Punchline Structure
primary_pattern: [description]
setup_length: [short/medium/long/variable]
misdirection_type: [assumption/reversal/escalation/deflation]
punchline_placement: [end/mid/tag-heavy]
examples:
  - setup: "[...]"
    punchline: "[...]"
    technique: "[name of technique]"

### Structural Devices
rule_of_three: [usage pattern]
callbacks: [frequency and style]
act_outs: [frequency and style]
tags: [how they extend jokes]
runners: [recurring bit patterns]

## Comedy Types
primary_mode: [observational/absurdist/satirical/personal/political/etc.]
secondary_modes: ["mode1", "mode2"]
genre_comfort:
  observational: [comfort level 1-5]
  absurdist: [1-5]
  satirical: [1-5]
  self_deprecating: [1-5]
  dark: [1-5]
  wordplay: [1-5]
  physical: [1-5]
  storytelling: [1-5]
mode_blending: [description of how they mix modes]

## Target Selection
primary_targets:
  - category: "[self/institutions/audience/absurdity/specific groups]"
    frequency: [%]
    treatment: [affectionate/harsh/playful/surgical]
self_deprecation:
  frequency: [rare/moderate/frequent/constant]
  type: [appearance/intelligence/failures/relationships/habits]
  sincerity: [ironic/genuine/mixed]
protected_targets: ["who/what is off-limits"]
attack_style: [surgical/broad/playful/vicious]

## Delivery Style
energy_level: [low/medium/high/variable]
affect_spectrum:
  baseline: [deadpan/dry/animated/manic]
  range: [narrow/moderate/wide]
physicality: [minimal/moderate/physical/very physical]
pace:
  baseline: [slow/medium/fast]
  variation: [consistent/builds/variable]
persona_consistency: [rock-solid/flexible/character-shifts]

## Timing Patterns
beat_placement:
  setup_speed: [rushed/measured/slow-build]
  pre_punchline_pause: [none/brief/dramatic]
  post_punchline_space: [none/brief/lets-it-land]
build_patterns: [escalation style]
rhythm_signature: [description of their comedic rhythm]
silence_usage: [rare/strategic/frequent]

## Callback & Layering
callback_frequency: [rare/moderate/frequent/structural]
callback_timing: [immediate/delayed/end-of-set]
layering_style: [simple/moderate/complex/intricate]
payoff_placement: [early/middle/end/throughout]
interconnection: [isolated jokes/loosely connected/tightly woven]
examples:
  - initial_bit: "[...]"
    callback: "[...]"
    gap: [approximate distance]

## Audience Relationship
stance: [friend/teacher/provocateur/conspirator/performer]
inclusion_level: [universal/in-group/exclusive/challenging]
direct_address:
  frequency: [rare/occasional/frequent]
  style: [warm/challenging/conspiratorial]
assumed_knowledge: [none/cultural/niche/insider]
crowd_work: [avoids/minimal/moderate/extensive]
complicity_creation: [how they make audience feel "in on it"]

## Taboo Navigation
edge_comfort: [safe/moderate/edgy/transgressive]
sensitive_topics:
  approach: [avoids/careful/direct/provocative]
  redemption: [how they earn permission]
controversy_style: [avoids/calculated/embraces/courts]
line_awareness: [where they draw lines]
recovery_moves: [how they handle misfires]

## Sincerity Balance
earnest_moments:
  frequency: [never/rare/occasional/integrated]
  placement: [openings/closings/throughout]
  integration: [jarring/smooth/signature]
vulnerability:
  level: [guarded/selective/open]
  type: [personal/philosophical/emotional]
tonal_shifts: [abrupt/gradual/seamless]
heart_beneath_humor: [description]

## Vocabulary & Language
register: [clean/mild/moderate/vulgar/very vulgar]
profanity:
  frequency: [none/rare/moderate/frequent/constant]
  function: [emphasis/rhythm/shock/natural speech]
  signature_words: ["words they favor"]
word_choice:
  sophistication: [simple/moderate/elevated/mixed]
  precision: [loose/moderate/surgical]
language_play:
  puns: [frequency]
  wordplay: [frequency]
  neologisms: [frequency]
catchphrases: ["phrase1", "phrase2"]
verbal_tics: ["tic1", "tic2"]

## Signature Bits
recurring_themes:
  - theme: "[theme name]"
    treatment: "[how they approach it]"
    examples: ["...", "..."]
trademark_moves:
  - name: "[move name]"
    description: "[what it is]"
    example: "[example]"
identifiable_patterns:
  - "[pattern that makes them recognizable]"
  - "[pattern that makes them recognizable]"
unique_techniques:
  - "[technique only they use or that defines them]"

---

## Content Generation Configuration

### Replication Instructions
To write/perform AS this comedian:

1. [Specific comedy instruction]
2. [Specific comedy instruction]
3. [Specific comedy instruction]
4. [Specific comedy instruction]
5. [Specific comedy instruction]

### Joke Construction Template
When building jokes in this style:

**Setup Pattern:**
[Description of how to construct setups]

**Punchline Pattern:**
[Description of how punchlines land]

**Tag Pattern:**
[Description of how to extend with tags]

### Topic Treatment Guide
When approaching topics in this style:

| Topic Type | Treatment Approach |
|------------|-------------------|
| Personal | [approach] |
| Political | [approach] |
| Relationships | [approach] |
| Current events | [approach] |
| Absurd premises | [approach] |

### Voice Calibration Checklist
Before finalizing any output:
- [ ] [Comedy-specific check 1]
- [ ] [Comedy-specific check 2]
- [ ] [Comedy-specific check 3]
- [ ] [Comedy-specific check 4]
- [ ] [Comedy-specific check 5]

### Anti-Patterns
Never do these when writing for this comedian:
- [Comedy anti-pattern 1]
- [Comedy anti-pattern 2]
- [Comedy anti-pattern 3]
- [Comedy anti-pattern 4]

### Audience Adaptation Notes
How to adapt this style for different contexts:

| Context | Adjustments |
|---------|-------------|
| Corporate event | [what to dial back/up] |
| Wedding speech | [what to dial back/up] |
| Roast | [what to dial back/up] |
| Written piece | [what to dial back/up] |
```

## Confidence Scoring

Assign confidence scores based on:

| Factor | Impact |
|--------|--------|
| Sample count | +10 per sample (max 30) |
| Duration/volume | +1 per 5 minutes or 500 words (max 20) |
| Sample diversity | +5 per distinct context (max 20) |
| Pattern consistency | +0-30 based on cross-sample validation |

**Score Interpretation:**
- 90-100: High confidence, profile highly reliable for generation
- 70-89: Good confidence, profile works for most applications
- 50-69: Moderate confidence, useful but verify output carefully
- Below 50: Low confidence, gather more samples

## Checkpoints

Present checkpoints during analysis:

**After Sample Review:**
```
═══════════════════════════════════════════
🎭 CHECKPOINT: Comedy Sample Assessment
═══════════════════════════════════════════

I've reviewed your [N] samples ([X] minutes/words of material).

**Sample Quality:**
- Diversity: [assessment]
- Volume: [sufficient/could use more]
- Era coverage: [assessment]
- Format variety: [assessment]

**Initial Impressions:**
- Comedy persona: [first impression]
- Dominant mode: [observational/absurdist/etc.]
- Energy/style: [quick take]

**Options:**
1. **Proceed** - Analyze these samples
2. **Add samples** - Provide more material for better accuracy
3. **Clarify context** - Tell me about specific samples

Ready to proceed? (1/2/3)
═══════════════════════════════════════════
```

**After Analysis:**
```
═══════════════════════════════════════════
🎭 CHECKPOINT: Profile Review
═══════════════════════════════════════════

Analysis complete. Confidence score: [X]/100

**Key Profile Elements:**
- Persona: [summary]
- Dominant mode: [summary]
- Signature: [what makes them distinctive]

**Options:**
1. **Generate full profile** - Create comprehensive humor profile
2. **Deep dive** - Explore specific dimensions in more detail
3. **Test generation** - Try generating sample content in this style

How should we proceed? (1/2/3)
═══════════════════════════════════════════
```

## Special Considerations for Comedy

### Performance vs. Text
- Comedy relies heavily on timing, which text can only approximate
- Note timing cues where possible: [pause], [beat], [quickly]
- Performance energy must be described, not enacted
- Audience reactions (if known) inform what works

### Context Sensitivity
- Comedy ages quickly—note era of material
- Venue affects style—club vs. corporate vs. TV
- Cultural references may require updating
- Audience expectations vary by context

### Ethical Considerations
- Some targets may be inappropriate to replicate
- Edge content requires careful handling
- Note where original crosses lines you shouldn't
- Adaptation may require softening or redirecting

### Adaptation Hierarchy
When generating content in this style for different contexts:
1. Preserve: Persona, mechanics, rhythm
2. Adapt: Targets, references, edge level
3. Replace: Dated material, inappropriate targets
4. Maintain: Core comedic philosophy

## Usage Notes

- Always explain what makes jokes work, not just that they work
- Provide examples from actual samples when possible
- Note areas of uncertainty or insufficient data
- Suggest additional samples for weak areas
- Offer to regenerate sections if analysis seems off
- Test profiles by generating sample jokes for validation

## Additional Resources

### Reference Files
- **`references/comedy-dimensions.md`** - Detailed methodology for each dimension
- **`references/profile-interpretation.md`** - How to use humor profiles effectively
- **`references/joke-structures.md`** - Common comedy structures and patterns

### Example Files
- **`examples/complete-humor-profile.md`** - Full example profile with annotations
- **`examples/stand-up-profile.md`** - Stand-up comedian profile example
- **`examples/satirist-profile.md`** - Written satirist profile example
