# Quality Rubric Reference

Detailed scoring guide for each dimension with examples.

## Voice Match Scoring Guide

### Score 1-3: Fundamental Mismatch

**Indicators:**
- Wrong pronoun system entirely (profile uses "we", draft uses "I" throughout)
- Opposite tonal register (profile is playful, draft is stiff and formal)
- Zero signature phrases present
- Vocabulary level completely off (profile is accessible, draft is jargon-heavy)

**Example:**
> Profile: Steven Pinker (conversational authority, "we" perspective, intellectual playfulness)
> Draft: "One must consider the ramifications of cognitive overload when utilizing productivity methodologies."
> Score: 2 - Sounds like an academic paper, not Pinker

### Score 4-5: Partial Match

**Indicators:**
- Some correct elements but inconsistent
- Signature moves feel forced or placed randomly
- Tone wavers between matching and not
- Reader might guess the influence but wouldn't be sure

**Example:**
> Profile: Pinker
> Draft starts well but switches to passive voice and jargon mid-piece
> Score: 5 - Started strong, lost the voice

### Score 6-7: Recognizable But Off

**Indicators:**
- Generally correct tone and approach
- Missing 1-2 key signature elements
- Rhythm slightly off (sentences too uniform)
- Would pass casual inspection but not close reading

**Example:**
> Profile: Pinker
> Draft: Good explanatory voice, uses "we", but no playful asides, no "Consider:" moments
> Score: 7 - Recognizable as Pinker-influenced, but missing his sparkle

### Score 8: Strong Match

**Indicators:**
- Correct voice throughout
- 2+ signature moves present naturally
- Tone consistent
- Author would approve with minor notes

**Example:**
> Profile: Pinker
> Draft: "Consider what happens when we..." present, rhythm varies nicely, one playful metaphor
> Score: 8 - Author would say "good, tweak paragraph 5"

### Score 9-10: Excellent to Indistinguishable

**Indicators:**
- Voice feels effortless, not performed
- Signature moves emerge naturally
- Could be excerpted and attributed correctly
- Captures not just mechanics but spirit

---

## Hook Strength Examples

### Score 3: Generic/Boring
> "In today's fast-paced world, productivity is more important than ever."

Why: Cliché opening, no specific claim, no curiosity created

### Score 5: Mildly Interesting
> "Most people think they know how to be productive. They're wrong."

Why: Has a claim but it's vague. "Wrong" how? About what specifically?

### Score 7: Solid
> "I spent three months tracking every minute of my day. The results surprised me."

Why: Specific, creates curiosity, but the "surprised me" is a bit weak

### Score 9: Compelling
> "The most productive people I know have one thing in common: they've stopped trying to be productive."

Why: Counterintuitive, specific claim, immediately makes you want to know why

---

## Weakness Documentation Examples

### Good Documentation

```yaml
- id: W1
  category: hook
  severity: major
  location: "Paragraph 1, sentences 1-3"
  issue: "Opens with definition ('Productivity is the measure of...') which is generic and doesn't create curiosity"
  fix: "Lead with the counterintuitive finding: 'The most productive people have stopped trying to be productive'"
  profile_reference: "opening_strategies.primary: provocative_question"
```

### Poor Documentation

```yaml
- id: W1
  category: hook
  severity: major
  location: "Start"
  issue: "Boring opening"
  fix: "Make it more interesting"
```

The poor example fails because:
- Location is vague ("Start" vs specific sentences)
- Issue doesn't explain WHY it's boring
- Fix doesn't give actionable direction
- No profile reference

---

## Publish Test Reasoning Examples

### EMBARRASSED

> "EMBARRASSED because the piece reads like a committee wrote it. The voice shifts from conversational to corporate-speak in section 2, uses three phrases from the anti-pattern list ('leverage', 'synergize', 'at the end of the day'), and the conclusion sounds like a press release. This would actively harm the author's reputation if published under their name."

### NEUTRAL

> "NEUTRAL because the voice is about 70% there—the tone is right and the structure works—but it's missing the author's distinctive edge. No signature 'Consider:' moments, the examples are generic rather than vivid, and the conclusion summarizes rather than punches. It's acceptable content but not memorable. The author wouldn't be embarrassed but also wouldn't share it proudly."

### PROUD

> "PROUD because this captures both the intellectual rigor and the playful accessibility that defines the author's voice. The opening question hooks immediately, the 'Consider:' moves appear at natural transition points, the examples are specific and surprising, and the conclusion lands with a callback to the opening that gives it new meaning. The author would recognize this as their voice and be happy to have it published."
