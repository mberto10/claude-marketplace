# Writing Studio: Critique Loop Workflow

A new autonomous writing workflow inspired by the Ralph Wiggum self-referential loop pattern, adapted for voice-matched content creation.

## Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         WRITING STUDIO QUALITY LOOP                         │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ DISCOVER │ → │  LEARN   │ → │  IDEATE  │ → │   PLAN   │ → │  WRITE   │
  │          │   │          │   │          │   │          │   │          │
  │ Context  │   │  Voice   │   │  Angle   │   │ Outline  │   │  Draft   │
  │ Audience │   │  Profile │   │  Hook    │   │ Structure│   │  Content │
  │ Goals    │   │  Tone    │   │  Thesis  │   │ Flow     │   │  Voice   │
  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └────┬─────┘
                                                                    │
                                                                    ▼
  ┌──────────┐   ┌──────────┐   ┌──────────┐                  ┌──────────┐
  │ PUBLISH  │ ← │  POLISH  │ ← │ ITERATE  │ ← ── [NO] ── ← │ CRITIQUE │
  │          │   │          │   │          │                  │          │
  │ Final    │   │  Edit    │   │ Address  │                  │ Score    │
  │ Output   │   │  Refine  │   │ Weakness │                  │ Test     │
  │ Export   │   │  Perfect │   │ Re-draft │                  │ Judge    │
  └──────────┘   └──────────┘   └──────────┘                  └────┬─────┘
       ▲                                                           │
       │                                                           │
       └─────────────────────── [PASS] ────────────────────────────┘
```

## Core Philosophy

### The Quality Question

Every piece must answer: **"Would the author actually publish this?"**

This isn't about perfection—it's about authenticity. A piece passes when:
1. It sounds like the author wrote it (voice match)
2. The author would be proud to put their name on it (publish test)
3. No glaring weaknesses remain (weakness count = 0 critical)

### Self-Referential Improvement

Each iteration sees its previous work:
- Draft N+1 reads Draft N and Critique N
- Specific weaknesses become specific improvements
- Progress is tracked and visible
- The loop converges toward quality

---

## Phase Breakdown

### Phase 1: DISCOVER (Deep Understanding)
**Purpose:** Deeply understand the idea before writing anything

This phase is **heavily interrogative**. Complex ideas require thorough exploration before any writing begins. The goal is to understand not just WHAT the user wants to write, but WHY, for WHOM, and what makes this idea THEIRS.

**Philosophy:** Better to ask 10 questions upfront than iterate 5 times on the wrong piece.

#### Step 1.1: Initial Idea Capture

When user provides input (topic, idea, assignment), immediately probe for depth:

```
═══════════════════════════════════════════════════════════════════════════════
📍 UNDERSTANDING YOUR IDEA
═══════════════════════════════════════════════════════════════════════════════

You want to write about: "[user's input]"

Before we begin, I want to make sure I truly understand what you're going for.
═══════════════════════════════════════════════════════════════════════════════
```

**AskUserQuestion - Idea Type:**
```yaml
question: "What kind of piece is this?"
header: "Format"
options:
  - label: "Article/Essay"
    description: "Long-form exploration of an idea (800-3000 words)"
  - label: "Blog Post"
    description: "Conversational, web-friendly (500-1500 words)"
  - label: "Newsletter"
    description: "Direct to subscribers, personal voice"
  - label: "LinkedIn/Social"
    description: "Professional platform, shorter format"
```

#### Step 1.2: Core Idea Extraction

For complex ideas, use progressive questioning to unpack:

**AskUserQuestion - The Core:**
```yaml
question: "What's the ONE thing you want readers to walk away with?"
header: "Core Message"
options:
  - label: "A new perspective"
    description: "Readers will see something familiar differently"
  - label: "Actionable insight"
    description: "Readers will know what to DO"
  - label: "Emotional resonance"
    description: "Readers will FEEL something"
  - label: "Knowledge transfer"
    description: "Readers will understand something new"
```

**AskUserQuestion - Your Unique Take:**
```yaml
question: "What makes YOUR take on this different?"
header: "Unique Angle"
options:
  - label: "Personal experience"
    description: "I've lived this / done this / seen this"
  - label: "Contrarian view"
    description: "I disagree with the common wisdom"
  - label: "New connection"
    description: "I see a pattern others don't"
  - label: "Not sure yet"
    description: "Help me find my angle"
```

#### Step 1.3: Audience Deep Dive

**AskUserQuestion - Who's Reading:**
```yaml
question: "Who is this for?"
header: "Audience"
multiSelect: false
options:
  - label: "My existing audience"
    description: "People who already follow my work"
  - label: "New audience"
    description: "People discovering me through this piece"
  - label: "Specific group"
    description: "A particular professional/interest group"
  - label: "General public"
    description: "Anyone interested in this topic"
```

**Follow-up if "Specific group":**
```yaml
question: "What does this audience already know?"
header: "Knowledge"
options:
  - label: "Beginners"
    description: "Need basics explained"
  - label: "Intermediate"
    description: "Know fundamentals, want depth"
  - label: "Advanced"
    description: "Experts who want nuance"
  - label: "Mixed"
    description: "Need to serve multiple levels"
```

**AskUserQuestion - Audience Pain:**
```yaml
question: "What problem or question does your audience have that this addresses?"
header: "Pain Point"
options:
  - label: "They're stuck"
    description: "They can't figure something out"
  - label: "They're wrong"
    description: "They believe something that isn't true"
  - label: "They're missing out"
    description: "They don't know what they don't know"
  - label: "They need validation"
    description: "They suspect something but need confirmation"
```

#### Step 1.4: Context & Constraints

**AskUserQuestion - Stakes:**
```yaml
question: "How important is this piece?"
header: "Stakes"
options:
  - label: "High stakes"
    description: "Career-defining, public launch, major publication"
  - label: "Medium stakes"
    description: "Important but not critical"
  - label: "Low stakes"
    description: "Experimental, practice, internal"
  - label: "Fun/creative"
    description: "No pressure, just want to create"
```

**AskUserQuestion - Length:**
```yaml
question: "How long should this be?"
header: "Length"
options:
  - label: "Short (500-800 words)"
    description: "Punchy, focused, one idea"
  - label: "Medium (800-1500 words)"
    description: "Standard blog/article length"
  - label: "Long (1500-3000 words)"
    description: "Deep dive, thorough exploration"
  - label: "Whatever it takes"
    description: "Let the idea determine length"
```

#### Step 1.5: Confirm Understanding

**Critical checkpoint before proceeding.** Synthesize everything learned and confirm:

```
═══════════════════════════════════════════════════════════════════════════════
📍 CONFIRM: Do I understand your piece?
═══════════════════════════════════════════════════════════════════════════════

Here's what I understand you want to create:

**THE PIECE**
Format: [type] | Length: [target]
Stakes: [level]

**THE IDEA**
Core message: "[synthesized from answers]"
Your unique angle: "[what makes this yours]"

**THE AUDIENCE**
Who: [audience description]
Their current state: [what they know/believe]
What they need: [the transformation]

**THE GOAL**
After reading, they will: [outcome]

═══════════════════════════════════════════════════════════════════════════════
```

**AskUserQuestion - Confirmation:**
```yaml
question: "Does this capture what you want to create?"
header: "Confirm"
options:
  - label: "Yes, exactly"
    description: "You've got it, let's proceed"
  - label: "Mostly, but..."
    description: "Close, need to adjust something"
  - label: "Not quite"
    description: "Let me clarify further"
  - label: "Actually, let me rethink"
    description: "This helped me realize I want something different"
```

**If "Mostly, but..." or "Not quite":** Loop back with targeted questions on what's off.

**If "Actually, let me rethink":** Start fresh with new framing.

**Only proceed to LEARN phase when user confirms "Yes, exactly"**

#### Step 1.6: Discovery Brief Output

Once confirmed, generate the brief:

```yaml
discovery_brief:
  confirmed: true
  timestamp: "..."

  piece:
    format: "..."
    target_length: "..."
    stakes: "..."

  idea:
    raw_input: "[original user input]"
    core_message: "[distilled]"
    unique_angle: "[what makes it theirs]"
    type: "[perspective/insight/emotion/knowledge]"

  audience:
    who: "..."
    knowledge_level: "..."
    current_state: "..."
    pain_point: "..."
    desired_transformation: "..."

  success_criteria:
    - "[specific measurable outcome 1]"
    - "[specific measurable outcome 2]"

  questions_asked: [N]
  clarifications_made: [list]
```

**Key Principle:** The DISCOVER phase should feel like a thoughtful conversation with a skilled interviewer, not a form to fill out.

---

#### Handling Complex Ideas

When user input is abstract, multi-faceted, or unclear, trigger **Deep Idea Exploration** before the standard questions.

**Complexity Signals:**
- Input is a concept rather than a topic ("I want to write about how constraints breed creativity")
- Input contains multiple connected ideas
- Input references personal insight or experience
- Input is a question rather than a statement
- Input contains hedging ("I think maybe...")

**Deep Idea Exploration Process:**

**Step 1: Reflect back what you heard**
```
═══════════════════════════════════════════════════════════════════════════════
📍 LET ME MAKE SURE I UNDERSTAND
═══════════════════════════════════════════════════════════════════════════════

You said: "[exact user input]"

Here's what I'm hearing: [your interpretation in different words]

Is that right, or am I missing something?
═══════════════════════════════════════════════════════════════════════════════
```

**Step 2: Unpack the layers**

**AskUserQuestion - Origin:**
```yaml
question: "Where did this idea come from?"
header: "Origin"
options:
  - label: "Personal experience"
    description: "Something happened that made me see this"
  - label: "Pattern I noticed"
    description: "I keep seeing this show up"
  - label: "Something I read/heard"
    description: "Another idea sparked this"
  - label: "A question I can't shake"
    description: "I keep wondering about this"
```

**AskUserQuestion - The Tension:**
```yaml
question: "What's the tension or conflict in this idea?"
header: "Tension"
options:
  - label: "Common belief vs. reality"
    description: "People think X but actually Y"
  - label: "Two good things in conflict"
    description: "You can't have both A and B"
  - label: "Surface vs. depth"
    description: "It looks like X but underneath it's Y"
  - label: "Past vs. future"
    description: "What worked before doesn't work now"
```

**Step 3: Find the story**

**AskUserQuestion - Concrete Example:**
```yaml
question: "Can you give me ONE specific example that illustrates this idea?"
header: "Example"
options:
  - label: "Yes, from my life"
    description: "I have a personal story"
  - label: "Yes, something I observed"
    description: "I saw this happen"
  - label: "Yes, a known case"
    description: "There's a famous example"
  - label: "Not yet"
    description: "I know it's true but can't point to one example"
```

**If "Not yet":** This is a signal—help them find an example before proceeding:
```yaml
question: "Let's find an example together. Where have you seen hints of this?"
header: "Find Example"
options:
  - label: "In my work"
    description: "Something from my professional life"
  - label: "In relationships"
    description: "How people interact"
  - label: "In culture/society"
    description: "Broader patterns"
  - label: "In myself"
    description: "My own behavior or thinking"
```

**Step 4: Test the idea's edges**

**AskUserQuestion - Strongest Form:**
```yaml
question: "If this idea is TRUE, what follows from it?"
header: "Implications"
options:
  - label: "People should change behavior"
    description: "Stop doing X, start doing Y"
  - label: "We should see things differently"
    description: "Reframe how we understand something"
  - label: "Something is at stake"
    description: "There are consequences to ignoring this"
  - label: "I'm still figuring that out"
    description: "I know it matters but not sure how"
```

**AskUserQuestion - Steel Man Opposition:**
```yaml
question: "What's the strongest argument AGAINST your idea?"
header: "Opposition"
options:
  - label: "It's not actually new"
    description: "Everyone already knows this"
  - label: "It doesn't scale"
    description: "Works in some cases, not all"
  - label: "The evidence is weak"
    description: "Hard to prove"
  - label: "I haven't thought about opposition yet"
    description: "Help me find the counter-argument"
```

**Step 5: Synthesize the refined idea**

After deep exploration, present the **distilled idea**:

```
═══════════════════════════════════════════════════════════════════════════════
📍 YOUR IDEA, CRYSTALLIZED
═══════════════════════════════════════════════════════════════════════════════

**The Core Insight:**
[One sentence capturing the essential idea]

**The Tension:**
[What makes this interesting/non-obvious]

**The Evidence:**
[The example(s) that prove it]

**The Stakes:**
[Why this matters / what follows]

**The Counter:**
[The opposition you'll need to address]

═══════════════════════════════════════════════════════════════════════════════

Does this capture what you're trying to say?
```

**Only after idea is crystallized:** Proceed to standard DISCOVER questions (format, audience, length, etc.)

---

#### Adaptive Question Depth

Not every piece needs full interrogation. Adapt based on:

| Input Type | Question Depth | Example |
|------------|----------------|---------|
| Simple topic | Light (3-4 questions) | "Write about morning routines" |
| Assigned brief | Medium (5-7 questions) | "Newsletter about our product launch" |
| Personal insight | Deep (10+ questions) | "I realized that my failures taught me more than my successes" |
| Abstract concept | Very deep (15+ questions) | "The relationship between boredom and creativity" |

**Detect and adapt.** Start light, go deeper if answers reveal complexity.

---

### Phase 2: LEARN
**Purpose:** Load and internalize the voice profile

**Inputs:**
- Writer profile name OR samples to profile
- Discovery brief

**Actions:**
1. Load specified profile from `profiles/`
2. Extract key voice elements:
   - Pronoun patterns
   - Tonal signature
   - Rhythm preferences
   - Signature moves
   - Anti-patterns to avoid
3. Adapt voice considerations to topic

**Output:** Voice Configuration
```yaml
profile_loaded: "steven-pinker"
key_elements:
  voice: "first-person plural, conversational authority"
  tone: "intellectually curious, occasionally playful"
  rhythm: "varied sentences, builds to punchy conclusions"
  signatures:
    - "The [unexpected] is [reframe]"
    - "Consider: ..."
  avoid:
    - "utilize"
    - "facilitate"
    - "in order to"
calibration_notes:
  - "For this topic, lean into the explanatory mode"
  - "Match the 'curious guide' persona"
```

**Checkpoint:** "Voice profile loaded. Any adjustments for this piece?"

---

### Phase 3: IDEATE
**Purpose:** Find the angle nobody else is taking

**Inputs:**
- Discovery brief
- Voice configuration

**Actions:**
1. Generate 5-7 distinct angles on the topic
2. Evaluate each for:
   - Uniqueness (not the obvious take)
   - Voice fit (does this suit the author?)
   - Audience resonance (will they care?)
3. Develop hook concepts for top angles
4. Identify the thesis statement

**Output:** Angle Selection
```yaml
selected_angle:
  thesis: "..."
  hook_concept: "..."
  unique_value: "Why this angle stands out"
rejected_angles:
  - angle: "..."
    reason: "Too common / doesn't fit voice / etc."
```

**Checkpoint:** "Here are 3 strong angles. Which direction resonates?"

---

### Phase 4: PLAN
**Purpose:** Create the structural blueprint

**Inputs:**
- Selected angle and thesis
- Voice configuration
- Constraints

**Actions:**
1. Design opening hook strategy
2. Map the argument/narrative arc
3. Identify key sections and their purposes
4. Plan transitions between sections
5. Design the closing (callback, CTA, thought)

**Output:** Structural Outline
```markdown
# [Working Title]

## Opening Hook
- Strategy: [anecdote/question/provocation/statistic]
- Bridge to thesis: [how we get there]

## Section 1: [Name]
- Purpose: [what this section accomplishes]
- Key points:
  - Point A
  - Point B
- Transition to next: [connection]

## Section 2: [Name]
...

## Closing
- Strategy: [callback/CTA/thought-provoker/synthesis]
- Final image/sentence: [how we leave them]

---
Estimated length: X words
Voice notes: [specific considerations for this structure]
```

**Checkpoint:** "Does this structure serve your thesis?"

---

### Phase 5: WRITE
**Purpose:** Execute the first draft with full voice commitment

**Inputs:**
- Structural outline
- Voice configuration
- All previous phase outputs

**Actions:**
1. Write section by section
2. Apply voice profile to every sentence
3. Check for prohibited patterns
4. Maintain rhythm consistency
5. Include signature moves naturally

**Output:** Draft N (saved to `drafts/draft-N.md`)
```markdown
---
draft_version: 1
voice_profile: "steven-pinker"
word_count: 1247
timestamp: "2024-01-15T10:30:00Z"
---

# [Title]

[Full draft content...]
```

**No checkpoint here—flows directly to CRITIQUE**

---

### Phase 6: CRITIQUE
**Purpose:** Honest evaluation against quality standards

**This is the core innovation.** The critique phase applies rigorous self-evaluation.

**Inputs:**
- Current draft
- Voice profile (as rubric)
- Previous critiques (if iterating)

**Critique Dimensions:**

| Dimension | Question | Score |
|-----------|----------|-------|
| Voice Match | "Does this sound like [author]?" | 1-10 |
| Hook Strength | "Would a reader keep reading after paragraph 1?" | 1-10 |
| Thesis Clarity | "Is the main point unmistakable?" | 1-10 |
| Evidence Quality | "Are claims supported compellingly?" | 1-10 |
| Flow & Rhythm | "Does it read smoothly in the author's cadence?" | 1-10 |
| Conclusion Impact | "Does the ending land?" | 1-10 |

**The Publish Test:**
> "If [author name] woke up tomorrow and saw this published under their name, would they be embarrassed, neutral, or proud?"
> - **Embarrassed** → Critical issues, must iterate
> - **Neutral** → Acceptable but not their best, should iterate
> - **Proud** → Ready to publish

**Weakness Identification:**
Each weakness must be:
1. **Specific** - Exact location and issue
2. **Categorized** - Hook/Voice/Structure/Evidence/Rhythm/Conclusion
3. **Actionable** - Clear fix instruction
4. **Prioritized** - Critical/Major/Minor

**Output:** Critique Report
```yaml
critique_version: 1
draft_evaluated: "draft-1.md"

scores:
  voice_match: 7
  hook_strength: 6
  thesis_clarity: 8
  evidence_quality: 7
  flow_rhythm: 7
  conclusion_impact: 5
  overall: 6.7

publish_test: "NEUTRAL"
publish_reasoning: "Voice is 70% there but missing the sharpest edges. Hook doesn't grab hard enough. Conclusion fizzles."

weaknesses:
  - id: W1
    category: hook
    severity: major
    location: "Paragraph 1"
    issue: "Opening is informative but not provocative"
    fix: "Lead with the counterintuitive insight, not the setup"

  - id: W2
    category: voice
    severity: major
    location: "Throughout"
    issue: "Missing signature 'Consider:' moves"
    fix: "Add 2-3 'Consider:' pivots at key argument shifts"

  - id: W3
    category: conclusion
    severity: critical
    location: "Final paragraph"
    issue: "Ends with summary, not punch"
    fix: "Callback to opening hook or provocative final thought"

  - id: W4
    category: evidence
    severity: minor
    location: "Section 2"
    issue: "Abstract claim without concrete example"
    fix: "Add specific anecdote or data point"

iteration_decision: "ITERATE"
next_draft_focus:
  - "Rewrite hook with counterintuitive lead"
  - "Inject 3 signature moves"
  - "Complete conclusion rewrite"
  - "Add one concrete example to Section 2"
```

**Quality Gates:**
```yaml
pass_criteria:
  voice_match: ">= 8"
  publish_test: "PROUD"
  critical_weaknesses: "0"
  overall_score: ">= 7.5"
```

---

### Phase 7: ITERATE (if needed)
**Purpose:** Systematically address identified weaknesses

**Inputs:**
- Previous draft
- Critique report
- Original voice profile

**Actions:**
1. Read previous draft and critique together
2. Address weaknesses in priority order (critical → major → minor)
3. Re-apply voice calibration
4. Write improved draft
5. Note what changed

**Output:** Draft N+1 with changelog
```markdown
---
draft_version: 2
voice_profile: "steven-pinker"
word_count: 1312
timestamp: "2024-01-15T11:15:00Z"
previous_draft: "draft-1.md"
changes_from_previous:
  - "Rewrote hook: now leads with counterintuitive insight"
  - "Added 3 'Consider:' signature moves"
  - "Complete conclusion rewrite with callback"
  - "Added concrete example in Section 2"
weaknesses_addressed: ["W1", "W2", "W3", "W4"]
---

# [Title]

[Improved draft content...]
```

**Then returns to CRITIQUE phase.**

---

### Phase 8: POLISH (after passing critique)
**Purpose:** Final refinement for publication-ready output

**Inputs:**
- Passing draft
- Style guide
- Format requirements

**Actions:**
1. Line-level editing pass
2. Prohibited word scan
3. Rhythm fine-tuning
4. Format compliance
5. Final voice calibration check

**Output:** Polished final draft

---

### Phase 9: PUBLISH
**Purpose:** Deliver the final piece with full documentation

**Outputs:**
1. **Final piece** - Publication-ready content
2. **Voice metadata** - Profile used, scores achieved
3. **Iteration history** - Journey from draft 1 to final
4. **Learnings** - What worked, what to remember for next time

```yaml
final_output:
  file: "final/my-article.md"
  word_count: 1298

voice_metadata:
  profile: "steven-pinker"
  final_voice_score: 9
  publish_test: "PROUD"

iteration_history:
  total_drafts: 3
  iterations_to_pass: 2
  key_improvements:
    - "Hook strength: 6 → 9"
    - "Conclusion impact: 5 → 8"

learnings:
  - "This topic benefits from concrete examples early"
  - "Signature moves work best at argument pivots"
```

---

## Workflow Modes

### Mode 1: Interactive (Human in Loop)
Traditional checkpoint-based collaboration with critique visibility.

```
Human: /write "Topic"
→ DISCOVER (checkpoint) → Human approves
→ LEARN (checkpoint) → Human confirms profile
→ IDEATE (checkpoint) → Human selects angle
→ PLAN (checkpoint) → Human approves structure
→ WRITE → CRITIQUE (checkpoint) → Human decides: iterate or pass
→ [iterate as needed with human oversight]
→ POLISH → PUBLISH
```

### Mode 2: Semi-Autonomous (Critique Loop)
Human sets parameters, loop runs until quality gate or max iterations.

```
Human: /write-loop "Topic" --voice pinker --max-iterations 5 --threshold 8
→ DISCOVER (checkpoint) → Human approves brief
→ LEARN (auto) → IDEATE (checkpoint) → Human selects angle
→ PLAN (checkpoint) → Human approves structure
→ [WRITE → CRITIQUE → ITERATE] × N (autonomous loop)
→ POLISH (checkpoint) → Human final review
→ PUBLISH
```

### Mode 3: Fully Autonomous (Ralph-Style)
Define everything upfront, let it run.

```
Human: /write-auto "Topic" --voice pinker --angle "counterintuitive" --max-iterations 10
→ All phases run autonomously
→ Persists all state to files
→ Exits when pass criteria met or max iterations
→ Human reviews final output
```

---

## File Structure

```
.claude/writing-loop/
├── sessions/
│   └── {session-id}/
│       ├── config.yaml          # Session configuration
│       ├── discovery-brief.yaml # Phase 1 output
│       ├── voice-config.yaml    # Phase 2 output
│       ├── angle-selection.yaml # Phase 3 output
│       ├── outline.md           # Phase 4 output
│       ├── drafts/
│       │   ├── draft-1.md
│       │   ├── draft-2.md
│       │   └── ...
│       ├── critiques/
│       │   ├── critique-1.yaml
│       │   ├── critique-2.yaml
│       │   └── ...
│       ├── final/
│       │   └── final-piece.md
│       └── progress.md          # Human-readable log
│
└── analytics/
    └── session-summaries.yaml   # Learning across sessions
```

---

## Implementation Components

### New Agents

1. **discoverer.md** - Brief creation and context gathering
2. **ideator.md** - Angle generation and selection
3. **critic.md** - Self-critique and scoring
4. **iterator.md** - Weakness-addressing rewrites

### New Commands

1. **/write-loop** - Semi-autonomous with critique loop
2. **/write-auto** - Fully autonomous mode
3. **/critique** - Run critique on any draft
4. **/iterate** - Address specific weaknesses

### New Hooks

1. **write-loop-stop.md** - Ralph-style stop hook for autonomous mode

### New Skills

1. **writing-critique/** - Critique methodology and rubrics
2. **writing-iteration/** - Systematic improvement patterns

---

## Quality Rubric Details

### Voice Match Scoring (1-10)

| Score | Description |
|-------|-------------|
| 1-3 | Doesn't sound like author at all |
| 4-5 | Some elements present but inconsistent |
| 6-7 | Recognizable but missing key signatures |
| 8 | Strong match, minor calibration needed |
| 9 | Excellent match, author would approve |
| 10 | Indistinguishable from author's best work |

### Weakness Categories

| Category | What It Covers |
|----------|----------------|
| **Hook** | Opening strength, reader grab, curiosity gap |
| **Voice** | Profile match, signatures, anti-patterns |
| **Structure** | Flow, transitions, section purposes |
| **Evidence** | Support quality, examples, data |
| **Rhythm** | Sentence variety, pacing, cadence |
| **Conclusion** | Landing, callback, final impact |
| **Clarity** | Thesis, argument, comprehension |

### Severity Levels

| Level | Definition | Action |
|-------|------------|--------|
| **Critical** | Piece cannot publish with this issue | Must fix before pass |
| **Major** | Significantly weakens the piece | Should fix |
| **Minor** | Polish-level improvement | Fix if iterating anyway |

---

## Example Session

### Input
```
/write-loop "Why most productivity advice fails" --voice steven-pinker --max-iterations 5 --threshold 8
```

### Iteration 1
- Draft 1: 1,200 words
- Critique: Voice 6/10, Hook 5/10, Overall 6.2
- Publish test: NEUTRAL
- Weaknesses: 4 (1 critical, 2 major, 1 minor)
- Decision: ITERATE

### Iteration 2
- Draft 2: 1,280 words
- Critique: Voice 8/10, Hook 7/10, Overall 7.5
- Publish test: NEUTRAL (borderline PROUD)
- Weaknesses: 2 (0 critical, 1 major, 1 minor)
- Decision: ITERATE

### Iteration 3
- Draft 3: 1,310 words
- Critique: Voice 9/10, Hook 9/10, Overall 8.4
- Publish test: PROUD
- Weaknesses: 1 (0 critical, 0 major, 1 minor)
- Decision: PASS

### Output
Final piece at voice match 9/10, polished and exported.

---

## Cost Considerations

| Mode | Typical Iterations | Est. Tokens | Est. Cost (Opus) |
|------|-------------------|-------------|------------------|
| Interactive | 1-2 | 50-100k | $1-3 |
| Semi-Auto | 2-4 | 100-200k | $3-8 |
| Full Auto | 3-7 | 150-400k | $5-15 |

**Mitigation strategies:**
- Use Sonnet for critique phase (faster, cheaper)
- Cache voice profiles
- Set conservative max-iterations
- Exit early on diminishing returns

---

## Success Metrics

### Per-Session
- Iterations to pass
- Voice score improvement curve
- Weakness resolution rate

### Across Sessions
- Average iterations needed
- Most common weakness categories
- Profile-specific patterns

This data feeds back into improving prompts and critique calibration.
