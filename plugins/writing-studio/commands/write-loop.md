---
description: Start writing with quality loop workflow
argument-hint: <topic>
allowed-tools: Read, Write, Edit, Glob, Task, AskUserQuestion, Bash
---

Start a writing session using the Quality Loop workflow for: $ARGUMENTS

## Workflow Overview

```
DISCOVER → VOICE → IDEATE → PLAN → DRAFT → CRITIQUE ←→ ITERATE → POLISH → PUBLISH
```

## Phase 1: Discovery (Orchestrator-Led)

**You are the discoverer.** Do NOT delegate to a sub-agent. Ask the user directly using AskUserQuestion.

### Step 1.1: Assess Complexity

Read the user's input carefully. Determine complexity:
- **Simple**: Clear topic with obvious scope (e.g., "write about my vacation")
- **Complex**: Abstract concept, multiple layers, or requires clarification (e.g., "write about how constraints breed creativity")

### Step 1.2: Reflect Back (Complex Ideas)

For complex ideas, first show understanding:

```
═══════════════════════════════════════════════════════════════════════════════
📍 LET ME MAKE SURE I UNDERSTAND
═══════════════════════════════════════════════════════════════════════════════

You said: "[exact user input]"

Here's what I'm hearing: [your interpretation]

Is that right, or am I missing something?
═══════════════════════════════════════════════════════════════════════════════
```

### Step 1.3: Deep Exploration Questions (Complex Ideas)

Use AskUserQuestion to explore the idea. Ask these in sequence, not all at once:

**Origin:**
```yaml
questions:
  - question: "Where did this idea come from?"
    header: "Origin"
    multiSelect: false
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

**Tension:**
```yaml
questions:
  - question: "What's the tension or conflict in this idea?"
    header: "Tension"
    multiSelect: false
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

**Evidence:**
```yaml
questions:
  - question: "Can you give me ONE specific example that illustrates this?"
    header: "Example"
    multiSelect: false
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

**Stakes:**
```yaml
questions:
  - question: "If this idea is TRUE, what follows from it?"
    header: "Stakes"
    multiSelect: false
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

### Step 1.4: Standard Questions

After deep exploration (or immediately for simple topics):

**Format:**
```yaml
questions:
  - question: "What kind of piece is this?"
    header: "Format"
    multiSelect: false
    options:
      - label: "Article/Essay"
        description: "Long-form exploration (800-3000 words)"
      - label: "Blog Post"
        description: "Conversational, web-friendly (500-1500 words)"
      - label: "Newsletter"
        description: "Direct to subscribers, personal voice"
      - label: "LinkedIn/Social"
        description: "Professional platform, shorter format"
```

**Audience:**
```yaml
questions:
  - question: "Who is this for?"
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

**Length:**
```yaml
questions:
  - question: "How long should this be?"
    header: "Length"
    multiSelect: false
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

### Step 1.5: Confirm Understanding

Synthesize everything and confirm with the user:

```
═══════════════════════════════════════════════════════════════════════════════
📍 CONFIRM: Do I understand your piece?
═══════════════════════════════════════════════════════════════════════════════

**THE PIECE**
Format: [type] | Length: [target]

**THE IDEA**
Core message: "[synthesized]"
Your unique angle: "[what makes this yours]"

**THE AUDIENCE**
Who: [audience]
What they need: [the transformation]

**THE GOAL**
After reading, they will: [outcome]
═══════════════════════════════════════════════════════════════════════════════
```

```yaml
questions:
  - question: "Does this capture what you want to create?"
    header: "Confirm"
    multiSelect: false
    options:
      - label: "Yes, exactly"
        description: "You've got it, let's proceed"
      - label: "Mostly, but..."
        description: "Close, need to adjust something"
      - label: "Not quite"
        description: "Let me clarify further"
```

**Only proceed when user confirms "Yes, exactly"**

### Step 1.6: Save Discovery Brief

Create session directory and save brief:

```bash
mkdir -p .claude/writing-loop/sessions/$(date +%Y%m%d-%H%M%S)/drafts
mkdir -p .claude/writing-loop/sessions/$(date +%Y%m%d-%H%M%S)/critiques
```

Save to `.claude/writing-loop/sessions/[session-id]/discovery-brief.yaml`

## Phase 2: Voice Profile Selection

Ask the user which voice to use:

```yaml
questions:
  - question: "Which voice should we use?"
    header: "Voice"
    multiSelect: false
    options:
      - label: "Select from profiles"
        description: "Use an existing writer profile"
      - label: "Use my style guide"
        description: "Use your personal style"
      - label: "No specific voice"
        description: "Write in general professional voice"
```

If "Select from profiles": List available profiles from `plugins/writing-studio/profiles/` and let user choose.

Load the selected voice profile for subsequent phases.

## Phase 3: Ideation (Agent)

Use the **ideator agent** to generate unique angles based on the discovery brief.

The ideator will:
1. Generate 3-5 distinct angles for the piece
2. Present options with pros/cons
3. Let user select or combine

## Phase 4: Planning (Agent)

Use the **planner agent** to create a structural outline based on:
- Discovery brief
- Selected angle
- Voice profile

## Phase 5: Drafting (Agent)

Use the **drafter agent** to write the first draft with:
- Discovery brief context
- Selected angle
- Structural outline
- Voice profile applied

Save draft to `sessions/[session-id]/drafts/draft-01.md`

## Phase 6: Critique Loop (Agent)

Use the **critic agent** to evaluate the draft:
- Score all quality dimensions (1-10)
- Run publish test: EMBARRASSED / NEUTRAL / PROUD
- Identify specific weaknesses
- Verdict: ITERATE or PASS

### If ITERATE:
1. Use **iterator agent** to address weaknesses
2. Save new draft to `drafts/draft-0N.md`
3. Save critique to `critiques/critique-0N.md`
4. Return to critic agent
5. Repeat until PASS

### If PASS:
Proceed to polish phase.

## Phase 7: Polish (Agent)

Use the **editor agent** for final refinement:
- Tighten prose
- Ensure voice consistency
- Polish opening and closing
- Final quality check

## Phase 8: Publish

Output the final piece with:
- Voice match score
- Iteration history (how many drafts)
- Final word count
- All drafts preserved in session folder

```
═══════════════════════════════════════════════════════════════════════════════
✓ WRITING COMPLETE
═══════════════════════════════════════════════════════════════════════════════

Final piece: [word count] words
Voice match: [score]/10
Iterations: [N] drafts
Publish test: [PROUD/NEUTRAL]

All drafts saved to: .claude/writing-loop/sessions/[session-id]/
═══════════════════════════════════════════════════════════════════════════════
```

## Quality Gates

Pass criteria for publishing:
- Voice match >= 8/10
- Publish test = PROUD
- Critical weaknesses = 0
