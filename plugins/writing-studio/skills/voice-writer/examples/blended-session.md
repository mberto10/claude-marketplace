# Blended Profile Session Example

Complete example of a voice-writer session blending multiple profiles.

---

## Session Start

**User:** "I want to write about focus and distraction. Blend Blake Crouch's philosophical depth with Hemingway's sentence rhythm."

---

## Profile Loading

```
═══════════════════════════════════════════
📚 VOICE REPERTOIRE
═══════════════════════════════════════════

Loaded 2 writer profiles:

**Blake Crouch (Recursion)**
> Writes like a neuroscientist who became a poet.
Key: Science-to-wonder arc, sensory anchoring, reality dissolution

**Hemingway (Sparse)** [hypothetical profile]
> Stripped prose, declarative power, iceberg theory.
Key: Short sentences, active verbs, emotional restraint

═══════════════════════════════════════════

Creating blend:
- Blake Crouch: cognitive_patterns, rhetorical_devices (philosophy)
- Hemingway: rhythm_cadence, sentence_length (rhythm)

Potential conflict: Crouch uses long builds; Hemingway uses short
punches. Resolution: Use Crouch's ideas in Hemingway's rhythm.

═══════════════════════════════════════════
```

---

## First Draft

```
═══════════════════════════════════════════
📝 DRAFT: Opening
═══════════════════════════════════════════
Voice: Blake Crouch (philosophy) + Hemingway (rhythm)

---

Focus is a lie. Your brain tells you it's a spotlight. It isn't.
It's a dam. A dam holding back a flood. Every second, millions
of signals compete for your attention. Colors. Sounds. Thoughts.
Memories. The itch on your arm. The weight of your body in the
chair. Focus doesn't illuminate. It excludes. It says no to
almost everything so you can say yes to one thing.

---

**Blend applied:**
From Blake Crouch:
- Reality dissolution (focus isn't what you think)
- Science-to-wonder arc (mechanism → implication)
- Metaphor usage (dam, flood, spotlight)

From Hemingway:
- Short declarative sentences
- Active verbs (tells, isn't, compete, excludes)
- Minimal clause nesting

Word count: 82

How's the blend? Adjust balance?
═══════════════════════════════════════════
```

---

## User Feedback

**User:** "Good start. But push the philosophy harder. The ideas feel a bit shallow."

---

## Revision (Shift Balance)

```
═══════════════════════════════════════════
📝 REVISED: Opening
═══════════════════════════════════════════
Voice: Blake Crouch (philosophy ↑) + Hemingway (rhythm)
Adjustment: Increased philosophical depth, maintained short rhythm

---

Focus is a lie you tell yourself. You think it's a spotlight.
A beam of attention illuminating what matters. But attention
doesn't work like light. Light reveals what's there. Attention
creates what's there. When you focus on this sentence, you're
not seeing the words more clearly. You're making the rest of
the world disappear. Focus is subtraction. It's the art of
strategic blindness. And everything you've ever accomplished
required you to ignore almost everything else.

---

**Blend adjusted:**
From Blake Crouch (increased):
- Deeper implication (attention creates reality)
- Extended metaphor (light vs. attention)
- Philosophical pivot (spotlight → strategic blindness)
- Broader claim (everything you've accomplished)

From Hemingway (maintained):
- Short sentences (avg 9 words)
- Declarative structure
- Minimal subordinate clauses

Word count: 97

Better depth? Continue?
═══════════════════════════════════════════
```

---

## User Continues

**User:** "Yes, that's it. Now write a paragraph about distraction."

---

## Continuation

```
═══════════════════════════════════════════
📝 DRAFT: Distraction Paragraph
═══════════════════════════════════════════
Voice: Blake Crouch (philosophy) + Hemingway (rhythm)
(blend locked from previous approval)

---

Distraction is the dam breaking. The flood rushing in. But here's
what nobody tells you: the flood is reality. The unfiltered
signal of existence. Every color in your peripheral vision.
Every half-heard voice. Every memory triggered by a smell you
didn't notice noticing. Distraction isn't a failure of focus.
It's focus failing to hold back what's actually there. When you
get distracted, you're not broken. You're just meeting the
universe without your filters on.

---

**Applied elements:**
- Continued dam/flood metaphor from opening
- Reality dissolution (distraction = unfiltered reality)
- Philosophical reframe (distraction isn't failure)
- Maintained Hemingway rhythm (short, punchy)

Word count: 88

Continue? Adjust?
═══════════════════════════════════════════
```

---

## User Wants Section Switch

**User:** "For the closing, drop the Hemingway. I want full Blake Crouch density."

---

## Section Switch

```
═══════════════════════════════════════════
📝 DRAFT: Closing Paragraph
═══════════════════════════════════════════
Voice: Blake Crouch (Recursion) - Full profile
(Hemingway influence removed for this section)

---

So here you are, reading these words, your attention a narrow
beam cutting through the chaos of raw sensory experience—and
somewhere in your peripheral consciousness, the world you're
ignoring continues without you. The coffee cooling on your desk.
The tension in your shoulders you haven't noticed in hours. The
person in the next room whose presence registers only as a vague
sense that you're not alone. All of it real. All of it happening.
All of it invisible to you because you've chosen, in this moment,
to build a tiny room of focus and lock yourself inside. We call
it concentration, as if gathering something together. But it's
the opposite. It's a forgetting so complete you don't remember
you've forgotten. The question isn't whether to focus or
distract. It's what parts of reality are you willing to pretend
don't exist?

---

**Section-specific voice:**
Full Blake Crouch restoration:
- Long, clause-rich sentences ✓
- Sensory anchoring (coffee, shoulders, room) ✓
- Science-to-wonder arc ✓
- Closing philosophical question ✓
- Reality dissolution ✓

Word count: 163
═══════════════════════════════════════════
```

---

## Final Draft

```
═══════════════════════════════════════════
📝 COMPLETE DRAFT
═══════════════════════════════════════════

---
voice_blend:
  sections:
    - name: opening
      primary: blake-crouch-recursion
      elements: [cognitive_patterns, rhetorical_devices]
      secondary: hemingway-sparse
      elements: [rhythm_cadence, sentence_length]
    - name: middle
      primary: blake-crouch-recursion
      elements: [cognitive_patterns, rhetorical_devices]
      secondary: hemingway-sparse
      elements: [rhythm_cadence, sentence_length]
    - name: closing
      primary: blake-crouch-recursion
      elements: [all]
      secondary: none
  custom_adjustments:
    - "increased philosophical depth in opening per feedback"
    - "full Crouch density for closing per request"
---

Focus is a lie you tell yourself. You think it's a spotlight.
A beam of attention illuminating what matters. But attention
doesn't work like light. Light reveals what's there. Attention
creates what's there. When you focus on this sentence, you're
not seeing the words more clearly. You're making the rest of
the world disappear. Focus is subtraction. It's the art of
strategic blindness. And everything you've ever accomplished
required you to ignore almost everything else.

Distraction is the dam breaking. The flood rushing in. But here's
what nobody tells you: the flood is reality. The unfiltered
signal of existence. Every color in your peripheral vision.
Every half-heard voice. Every memory triggered by a smell you
didn't notice noticing. Distraction isn't a failure of focus.
It's focus failing to hold back what's actually there. When you
get distracted, you're not broken. You're just meeting the
universe without your filters on.

So here you are, reading these words, your attention a narrow
beam cutting through the chaos of raw sensory experience—and
somewhere in your peripheral consciousness, the world you're
ignoring continues without you. The coffee cooling on your desk.
The tension in your shoulders you haven't noticed in hours. The
person in the next room whose presence registers only as a vague
sense that you're not alone. All of it real. All of it happening.
All of it invisible to you because you've chosen, in this moment,
to build a tiny room of focus and lock yourself inside. We call
it concentration, as if gathering something together. But it's
the opposite. It's a forgetting so complete you don't remember
you've forgotten. The question isn't whether to focus or
distract. It's what parts of reality are you willing to pretend
don't exist?

---

**Voice notes:** This piece demonstrates section-based blending—using
Hemingway's rhythm to deliver Crouch's ideas in the opening and middle,
then transitioning to full Crouch density for the philosophical landing.
The blend creates a "ease-in" effect: accessible entry, immersive exit.

Word count: 348
═══════════════════════════════════════════
```
