---
idea: Anti-Complexity Engineering
sources: ["Every.io compound engineering", "systems thinking"]
connects_to: ["compound-loop", "skills-as-modules", "my-thinking-patterns"]
categories: ["engineering-philosophy", "systems-thinking", "design-principles"]
---

# Anti-Complexity Engineering

## My Understanding

Traditional engineering accepts growing complexity as inevitable: each feature you add makes it harder to add the next. This is treated as a law of nature - entropy for codebases.

Anti-complexity engineering inverts this assumption: **each feature should make subsequent features easier to build, not harder.** Complexity accumulation isn't inevitable - it's a design failure.

The mechanism: instead of features adding only code (which compounds complexity), features also add knowledge (which compounds capability). The knowledge accumulation outpaces the complexity accumulation. Net effect: easier, not harder.

## Why This Resonates

I've felt this tension in every system I've built or observed. The first features are easy; the twentieth feature fights against nineteen others. I accepted this as "just how it is."

Anti-complexity engineering names the alternative I didn't know was possible. It's not "manage complexity better" - it's "design so complexity doesn't accumulate in the first place."

This connects to my scarcity-migration thinking: if you're spending effort fighting complexity, that's a cost. If you can make complexity not accumulate, that effort goes elsewhere. The constraint dissolves rather than migrates.

## Examples That Stuck

**The compounding framing:**

Traditional: Feature 1 → Feature 2 harder → Feature 3 even harder → ... → Feature N nearly impossible

Anti-complexity: Feature 1 → Feature 2 easier (learned from 1) → Feature 3 easier still → ... → Feature N trivial

The curve bends the opposite direction.

**CLAUDE.md as anti-complexity device:**
Every decision documented prevents that decision from being re-debated or re-made incorrectly. The cognitive load of "how do we do X?" disappears because the answer is already recorded. Complexity that would exist (in arguments, in inconsistency, in bugs) never materializes.

**Specialized reviewers as guardrails:**
After encountering a bug type once, you add it to a reviewer checklist. Future code can't have that bug - the reviewer catches it automatically. The complexity of "remembering to check for this" disappears.

**The documentation-as-investment reframe:**
Traditional view: documentation is overhead (adds work without adding features).
Anti-complexity view: documentation is investment (reduces future work by encoding knowledge).

One hour documenting a pattern saves ten hours of future debugging. The complexity cost is paid once; the benefit compounds forever.

## How I Use It

I reach for this when:
- Designing systems (software or otherwise)
- Evaluating whether a process is sustainable
- Pushing back on "that's just how it is" complexity fatalism
- Deciding where to invest effort (execution vs. knowledge capture)

My trigger questions:
- "Does adding this make the next thing easier or harder?"
- "Where does complexity accumulate in this system?"
- "What would it take to bend the curve the other direction?"
- "Am I just managing complexity or actually preventing it?"

## My Explanatory Moves

I usually start with the assumption people don't know they're making:

"You probably assume that systems get harder to change over time. More features, more code, more complexity, more friction. That's true for most systems. But it's not a law of physics - it's a design choice."

Then I introduce the alternative:

"What if each feature you added also deposited knowledge that made future features easier? The code still grows, but the capability to work with it grows faster. You end up with a system that gets *easier* to change over time, not harder."

The key reframe:

"Traditional engineering trades today's effort for features. Anti-complexity engineering trades today's effort for features PLUS future capability. The features are the same; the side effect is different."

## Tensions & Edges

**It's an ideal, not always achievable.** Some complexity is inherent to the problem domain. You can't always make things easier. The goal is to push toward anti-complexity, not to achieve it perfectly.

**Upfront cost for long-term benefit.** Anti-complexity requires investment (documentation, design, knowledge capture) that doesn't pay off immediately. In short-term thinking environments, this gets cut first.

**Knowledge accumulation has limits.** At some point, the knowledge base itself becomes complex. "Too many rules" is its own complexity. Need meta-strategies for pruning and organizing accumulated knowledge.

**Doesn't work for one-off work.** If you're building something once and never touching it again, anti-complexity engineering has no payoff. The benefits come from iteration and continuity.

**Requires cultural buy-in.** One person can't do anti-complexity engineering in a team that rewards shipping fast and ignoring knowledge capture. It's a system property, not an individual practice.

## Generalizing Beyond Engineering

This isn't just about code. Any system that accumulates work can either accumulate complexity or capability:

- **Organizations:** Each process added makes future processes harder (bureaucracy) OR captures patterns that make future processes easier (institutional learning)
- **Personal knowledge:** Each thing learned adds cognitive load (information overload) OR adds frameworks that make future learning easier (compounding understanding)
- **Products:** Each feature adds surface area to maintain (feature bloat) OR adds capabilities that make future features natural extensions (platform effects)

The anti-complexity principle is general: design for capability accumulation, not just output accumulation.

## Source Passages

> "In normal engineering, every feature you add, it makes it harder to add the next feature. In compounding engineering, your goal is to make the next feature easier to build from the feature that you just added."

> "Each bug, failed test, or a-ha problem-solving insight gets documented and used by future agents."

> "Compounding engineering: building self-improving development systems where each iteration makes the next one faster, safer, and better."
