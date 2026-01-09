---
name: Writing Critique
description: This skill should be used when evaluating writing drafts against voice profiles, scoring quality dimensions, identifying weaknesses, or deciding whether a piece is ready for publication. Provides the critique methodology and rubrics for the writing loop.
version: 1.0.0
---

# Writing Critique

Core knowledge for evaluating writing against voice profiles. This skill defines the quality rubrics, scoring methodology, and critique patterns used in the writing loop workflow.

## Purpose

Provide rigorous, consistent critique of writing drafts by:
- Scoring against specific voice profile dimensions
- Identifying actionable weaknesses
- Making pass/iterate decisions
- Tracking improvement across iterations

## The Central Question

Every critique answers: **"Would the author actually publish this?"**

This isn't about perfection—it's about authenticity and quality bar.

## Quality Dimensions

### 1. Voice Match (1-10)

**Question:** "Does this sound like [author] wrote it?"

| Score | Description | Indicators |
|-------|-------------|------------|
| 1-3 | Doesn't sound like author | Wrong pronouns, opposite tone, no signatures |
| 4-5 | Some elements present | Inconsistent voice, forced signatures |
| 6-7 | Recognizable but off | Missing key signatures, rhythm slightly off |
| 8 | Strong match | Minor calibration needed, author would approve |
| 9 | Excellent match | Captures voice authentically |
| 10 | Indistinguishable | Could be author's own work |

**Checklist:**
- [ ] Pronoun usage matches profile (I/we/you)
- [ ] Tonal signature maintained throughout
- [ ] At least 2 signature phrases/moves present
- [ ] No anti-pattern violations
- [ ] Sentence rhythm matches profile patterns
- [ ] Vocabulary level appropriate

### 2. Hook Strength (1-10)

**Question:** "Would a reader keep reading after paragraph 1?"

| Score | Description |
|-------|-------------|
| 1-3 | Generic, boring, gives no reason to continue |
| 4-5 | Mildly interesting but forgettable |
| 6-7 | Solid but not distinctive |
| 8 | Engaging, creates curiosity |
| 9 | Compelling, hard to stop reading |
| 10 | Irresistible, shares itself |

**Evaluation criteria:**
- Creates curiosity or stakes
- Distinctive (not generic opening)
- Fits author's opening style
- Bridges naturally to thesis
- Appropriate energy for piece type

### 3. Thesis Clarity (1-10)

**Question:** "Is the main point unmistakable?"

| Score | Description |
|-------|-------------|
| 1-3 | No clear thesis, reader confused about point |
| 4-5 | Vague thesis, multiple competing ideas |
| 6-7 | Thesis present but buried or unclear |
| 8 | Clear thesis, well-articulated |
| 9 | Crystal clear, memorable |
| 10 | Thesis is the piece's organizing force |

**Evaluation criteria:**
- Can state thesis in one sentence
- Every section serves the thesis
- Argument structure is sound
- No tangents that derail
- Thesis delivered at right moment

### 4. Evidence Quality (1-10)

**Question:** "Are claims supported compellingly?"

| Score | Description |
|-------|-------------|
| 1-3 | Unsupported assertions, no evidence |
| 4-5 | Weak or irrelevant evidence |
| 6-7 | Adequate evidence, could be stronger |
| 8 | Strong, relevant evidence |
| 9 | Compelling, varied evidence |
| 10 | Evidence is itself memorable and shareable |

**Evaluation criteria:**
- Abstract claims grounded in examples
- Evidence matches author's style (anecdotal/statistical/authoritative)
- Enough support without over-explaining
- Examples are specific, not generic
- Evidence advances argument, not just decorates

### 5. Flow & Rhythm (1-10)

**Question:** "Does it read smoothly in the author's cadence?"

| Score | Description |
|-------|-------------|
| 1-3 | Choppy, awkward, hard to read |
| 4-5 | Uneven, some smooth sections |
| 6-7 | Generally smooth with rough patches |
| 8 | Flows well, matches profile rhythm |
| 9 | Excellent flow, pleasure to read |
| 10 | Rhythm is part of the meaning |

**Evaluation criteria:**
- Sentence length variation matches profile
- Transitions smooth (not abrupt or over-signposted)
- Pacing appropriate for content
- Paragraph breaks at right moments
- No jarring shifts in register

### 6. Conclusion Impact (1-10)

**Question:** "Does the ending land?"

| Score | Description |
|-------|-------------|
| 1-3 | Just stops, no conclusion |
| 4-5 | Weak summary, fizzles out |
| 6-7 | Adequate conclusion, forgettable |
| 8 | Satisfying conclusion, ties things together |
| 9 | Strong landing, memorable |
| 10 | Ending elevates the entire piece |

**Evaluation criteria:**
- Satisfies (doesn't just stop)
- Callback to opening or introduces new thought
- Matches author's closing style
- Leaves reader with clear takeaway or emotion
- Appropriate energy (punch vs. reflection)

## The Publish Test

After scoring dimensions, apply the ultimate test:

> "If [author name] woke up tomorrow and saw this published under their name, would they be:"

| Result | Meaning | Action |
|--------|---------|--------|
| **EMBARRASSED** | Critical issues, cannot publish | Must iterate, major work needed |
| **NEUTRAL** | Acceptable but not their best | Should iterate, specific fixes needed |
| **PROUD** | This represents them well | Can proceed to polish |

**Always provide reasoning:**
- "NEUTRAL because the voice is 70% there but the conclusion fizzles"
- "EMBARRASSED because it sounds like a committee wrote it"
- "PROUD because it captures both the intellectual rigor and playfulness"

## Weakness Taxonomy

### Categories

| Category | What It Covers |
|----------|----------------|
| **hook** | Opening strength, reader grab, curiosity gap |
| **voice** | Profile match, signatures, anti-patterns, tone |
| **structure** | Flow, transitions, section organization, pacing |
| **evidence** | Support quality, examples, data, specificity |
| **rhythm** | Sentence variety, cadence, punctuation |
| **conclusion** | Landing, callback, final impact |
| **clarity** | Thesis, argument, comprehension, logic |

### Severity Levels

| Level | Definition | Action Required |
|-------|------------|-----------------|
| **Critical** | Piece cannot publish with this | Must fix before pass |
| **Major** | Significantly weakens the piece | Should fix |
| **Minor** | Polish-level improvement | Fix if iterating anyway |

### Weakness Documentation Format

Every weakness must be:

```yaml
- id: W[N]
  category: "[category]"
  severity: "[critical|major|minor]"
  location: "[Exact: paragraph, section, line]"
  issue: "[What's wrong - specific]"
  fix: "[How to fix - actionable]"
  profile_reference: "[Which profile element violated]"
```

**Good weakness:**
```yaml
- id: W1
  category: hook
  severity: major
  location: "Paragraph 1, sentences 1-3"
  issue: "Opens with definition ('Productivity is...') instead of engaging reader"
  fix: "Lead with the counterintuitive insight about why productivity advice fails"
  profile_reference: "opening_strategies.primary: provocative question"
```

**Bad weakness:**
```yaml
- id: W1
  category: hook
  severity: major
  location: "Beginning"
  issue: "Hook needs work"
  fix: "Make it better"
```

## Pass/Fail Criteria

### PASS Requirements (ALL must be true)

- Voice match score >= 8
- Publish test = PROUD
- Critical weaknesses = 0
- Overall score >= 7.5

### ITERATE Triggers (ANY triggers iterate)

- Voice match < 8
- Publish test = EMBARRASSED or NEUTRAL
- Critical weaknesses > 0
- Overall score < 7.5

## Critique Calibration

### Avoid These Errors

1. **Grade inflation**
   - Don't give 8s for mediocre work to be nice
   - An 8 means "author would approve"
   - Most first drafts are 5-7

2. **Vague feedback**
   - "Needs work" is useless
   - "Paragraph 3 lacks concrete example for the claim about cognitive load" is useful

3. **Ignoring the profile**
   - Your opinion doesn't matter
   - The profile defines what "good" means for this voice
   - Evaluate against THEIR style, not general style

4. **Moving goalposts**
   - Use consistent standards across iterations
   - Don't suddenly care about new things in draft 3

5. **Nitpicking on first pass**
   - Draft 1: Focus on critical/major
   - Draft 2+: Can address minor issues
   - Don't overwhelm with 20 minor issues

### Score Conflicts

**High voice match + NEUTRAL publish test:**
- Mechanics right but something intangible missing
- Look for: missing "soul," too safe, lacks distinctive edge
- The piece is correct but not compelling

**High individual scores + wrong overall feel:**
- Trust holistic read
- Document what's missing that scores don't capture
- May need new weakness category

## Progress Tracking

### First Draft Critique
- Be comprehensive, identify all weaknesses
- Set baseline scores
- Don't expect perfection

### Iteration N Critique
- Primary focus: Were previous weaknesses addressed?
- Secondary: Any new issues introduced?
- Track score progression
- Note improvement velocity

### Progress Documentation

```yaml
progress_from_previous:
  voice_delta: +2  # 6 → 8
  hook_delta: +3   # 5 → 8
  weaknesses_addressed: ["W1", "W2", "W3"]
  weaknesses_remaining: ["W4"]  # Wasn't fixed
  weaknesses_new: ["W5"]  # Introduced in this draft
  iteration_assessment: "Good progress, one more pass should get us there"
```

## Additional Resources

### Reference Files
- **`references/scoring-examples.md`** - Example scores with reasoning
- **`references/weakness-patterns.md`** - Common weaknesses by category

### Integration
- Used by: critic agent, write-loop command
- Inputs from: writer-profiler (creates the rubric)
- Outputs to: iterator agent (weakness fixes)
