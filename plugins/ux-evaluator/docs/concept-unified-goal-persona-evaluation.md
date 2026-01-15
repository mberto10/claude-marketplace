# Unified Goal-Persona Evaluation Framework

> **Status:** Concept - Validated Direction
> **Date:** 2026-01-15

## Vision

**Direct product optimization based on user goals.**

Before real users touch the product, simulate goal pursuit across multiple personas, trace through all system layers, and synthesize findings into prioritized optimizations.

This is not a replacement for user testing - it's a **pre-filter** that catches obvious issues before real users encounter them, and a **systematic optimization tool** that identifies root causes across the full stack.

---

## The Formula

```
GOAL × PERSONA × LAYERS = Evaluation Instance

Multiple Instances → Synthesis → Prioritized Optimization
```

### Dimensions

| Dimension | What It Represents |
|-----------|-------------------|
| **Goal** | What the user is trying to achieve |
| **Persona** | Who is trying to achieve it (expectations, mental model, tolerance) |
| **Layers** | Where in the system things can go wrong (UX, Code, AI, Infra) |

### The Power of Combination

Same goal, different personas:
- Newsletter Creator trying to "generate first article" → expects visual, guided flow
- Technical Integrator trying to "generate first article" → expects API, config files

Same persona, different goals:
- Newsletter Creator doing "initial setup" → tolerates complexity, one-time
- Newsletter Creator doing "weekly check" → expects speed, zero friction

**By varying goals and personas systematically, we surface issues that single-perspective evaluation misses.**

---

## Framework Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                         EVALUATION MATRIX                                   │
│                                                                             │
│                    Persona A    Persona B    Persona C                      │
│                    ─────────    ─────────    ─────────                      │
│   Goal 1          [eval]       [eval]       [eval]       → Synthesis       │
│   Goal 2          [eval]       [eval]       [eval]       → Synthesis       │
│   Goal 3          [eval]       [eval]       [eval]       → Synthesis       │
│                      │            │            │                            │
│                      ▼            ▼            ▼                            │
│                  Synthesis    Synthesis    Synthesis                        │
│                  by persona   by persona   by persona                       │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                    ┌─────────────────────┐                                  │
│                    │  MASTER SYNTHESIS   │                                  │
│                    │                     │                                  │
│                    │  • Universal issues │                                  │
│                    │  • Persona-specific │                                  │
│                    │  • Goal-specific    │                                  │
│                    │  • Layer root cause │                                  │
│                    │  • Priority ranking │                                  │
│                    └─────────────────────┘                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Components

### 1. Goal Library

Goals organized by User Lifecycle phase:

```yaml
phases:
  ACTIVATE:
    goals:
      - id: first_generation
        statement: "Generate my first piece of content"
        success_criteria:
          - Content generates without errors
          - Output appears in UI
          - Quality is acceptable
        reference_artifact: optional  # for comparison

      - id: first_delivery
        statement: "Send content to myself as a test"
        success_criteria:
          - Delivery completes
          - Email/output received
          - Content renders correctly

  ADOPT:
    goals:
      - id: weekly_workflow
        statement: "Run my regular weekly content generation"
        success_criteria:
          - Can trigger in <30 seconds
          - Status visible during run
          - Output meets quality bar

      - id: customize_output
        statement: "Adjust the output to match my brand better"
        success_criteria:
          - Can find customization options
          - Changes reflected in output
          - Settings persist
```

### 2. Persona Library

Personas defined with evaluation-relevant attributes:

```yaml
personas:
  - id: newsletter_creator
    name: "Newsletter Creator"
    description: "Content creator building a weekly newsletter"

    attributes:
      technical_level: low
      patience_for_complexity: low
      expected_ux_pattern: "visual, guided, Substack-like"

    goals_focus:  # which goals matter most to this persona
      - first_generation
      - customize_output
      - weekly_workflow

    friction_tolerance:
      configuration: low      # expects it to "just work"
      errors: very_low        # will abandon on first error
      learning_curve: medium  # willing to learn if guided

  - id: content_ops
    name: "Content Operations Lead"
    description: "Manages multiple publications and writers"

    attributes:
      technical_level: medium
      patience_for_complexity: medium
      expected_ux_pattern: "dashboard, metrics, status-oriented"

    goals_focus:
      - monitor_runs
      - diagnose_failures
      - manage_multiple

    friction_tolerance:
      configuration: medium
      errors: medium          # expects errors, wants clarity
      learning_curve: high    # will invest time to learn

  - id: technical_integrator
    name: "Technical Integrator"
    description: "Developer setting up integrations"

    attributes:
      technical_level: high
      patience_for_complexity: high
      expected_ux_pattern: "API-first, docs, config files"

    goals_focus:
      - api_integration
      - custom_configuration
      - debugging

    friction_tolerance:
      configuration: high     # expects complexity
      errors: high            # wants detailed error messages
      learning_curve: high    # will read docs
```

### 3. Layer Analyzers

Specialized agents for each system layer:

| Layer | Agent | Analyzes |
|-------|-------|----------|
| **UX** | Journey Agent | Navigation, friction, confusion, missing guidance |
| **Code** | Code Debugger | Logic errors, missing handlers, mapping bugs |
| **AI** | Trace Analyst | Prompt effectiveness, tool usage, output quality |
| **Infra** | Infra Auditor | Persistence, APIs, external services, state |

### 4. Evaluation Engine

Runs goal × persona combinations:

```
FOR each goal in selected_goals:
  FOR each persona in selected_personas:

    1. Load persona context (expectations, tolerance)
    2. Set success criteria for goal
    3. Pursue goal via UI as persona
    4. Document journey (friction, confusion, blockers)
    5. Evaluate outcome against criteria
    6. Analyze relevant layers
    7. Store evaluation instance

  END
END

Synthesize all instances → Master report
```

### 5. Synthesis Engine

Correlates findings across instances:

**Cross-Persona Analysis:**
- Which issues affect ALL personas? → Universal problems (highest priority)
- Which issues affect SPECIFIC personas? → Targeted fixes
- Which personas are blocked entirely? → Critical gaps

**Cross-Goal Analysis:**
- Which issues appear across MULTIPLE goals? → Systemic problems
- Which issues are GOAL-specific? → Targeted fixes

**Cross-Layer Attribution:**
- For each issue: which layer is the ROOT CAUSE?
- Trace symptom → origin

---

## Evaluation Instance Structure

Each goal × persona combination produces:

```markdown
# Evaluation Instance

## Context
- **Goal:** [goal statement]
- **Persona:** [persona name]
- **Date:** [timestamp]

## Pre-Evaluation Expectations
Based on persona attributes:
- Expected journey: [what this persona would expect]
- Friction tolerance: [what level of friction is acceptable]
- Success bar: [what "good enough" looks like for this persona]

## Journey Narrative
[Step-by-step account as this persona pursuing this goal]

## Outcome
- **Goal achieved:** Yes / Partial / No
- **Quality:** [if applicable, vs. success criteria]
- **Time to completion:** [if achieved]
- **Blocker:** [if not achieved, what stopped progress]

## Findings

### Friction Points
[Issues that slowed progress but didn't block]

### Confusion Points
[Places where persona didn't know what to do]

### Blockers
[Issues that prevented goal completion]

### Positive Observations
[Things that worked well for this persona]

## Layer Analysis

### UX Layer
- Issues found: [list]
- Severity for this persona: [rating]

### Code Layer
- Issues found: [list]
- Severity for this persona: [rating]

### AI Layer (if applicable)
- Issues found: [list]
- Severity for this persona: [rating]

### Infra Layer
- Issues found: [list]
- Severity for this persona: [rating]

## Persona-Specific Assessment
How well does the product serve THIS persona for THIS goal?
[Rating + explanation]
```

---

## Synthesis Report Structure

After running multiple evaluations:

```markdown
# Goal-Persona Evaluation Synthesis

## Evaluation Coverage
- Goals evaluated: [N]
- Personas evaluated: [M]
- Total instances: [N × M]
- Date range: [timestamps]

---

## Executive Summary

### Overall Product Readiness
[High-level assessment]

### Critical Findings
[Top 3-5 issues that must be addressed]

### Persona Readiness
| Persona | Ready? | Blocking Issues |
|---------|--------|-----------------|
| Newsletter Creator | No | [issues] |
| Content Ops | Partial | [issues] |
| Technical Integrator | Yes | - |

---

## Issue Classification

### Universal Issues (affect all personas)
These are highest priority - everyone hits them.

| Issue | Severity | Origin Layer | Affected Goals |
|-------|----------|--------------|----------------|
| [issue] | Critical | Code | Goal 1, 2, 3 |
| [issue] | High | UX | Goal 1, 2 |

### Persona-Specific Issues
These matter for specific user types.

#### Newsletter Creator
| Issue | Severity | Origin Layer | Root Cause |
|-------|----------|--------------|------------|
| [issue] | Critical | UX | [cause] |

#### Content Ops
| Issue | Severity | Origin Layer | Root Cause |
|-------|----------|--------------|------------|
| [issue] | Medium | Infra | [cause] |

### Goal-Specific Issues
These appear only for specific goals.

| Goal | Issue | Severity | Origin Layer |
|------|-------|----------|--------------|
| First generation | [issue] | High | AI |

---

## Layer Summary

### UX Layer
- Total issues: [N]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N]
- Key patterns: [common UX problems]

### Code Layer
- Total issues: [N]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N]
- Key patterns: [common code problems]

### AI Layer
- Total issues: [N]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N]
- Key patterns: [common AI problems]

### Infra Layer
- Total issues: [N]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N]
- Key patterns: [common infra problems]

---

## Root Cause Chains

### Chain 1: [Issue Title]
```
SYMPTOM: [What users experience]
PERSONAS AFFECTED: [which ones]
GOALS AFFECTED: [which ones]

TRACE:
User action → UX response → Code path → [AI/Infra] → Outcome
     ✓            ✓            ✗              -          ✗

ROOT CAUSE: [Layer] - [specific location/issue]
FIX: [recommended action]
EFFORT: [estimate]
IMPACT: [what improves when fixed]
```

### Chain 2: [Issue Title]
[...]

---

## Prioritized Recommendations

### P0 - Blocking (fix before any user touches product)
1. [Fix] - [Layer] - [Effort]
   - Blocks: [personas] for [goals]

### P1 - Critical (fix before target persona uses product)
1. [Fix] - [Layer] - [Effort]
   - Affects: [personas] for [goals]

### P2 - High (fix soon, significant friction)
1. [Fix] - [Layer] - [Effort]

### P3 - Medium (improve when possible)
1. [Fix] - [Layer] - [Effort]

---

## Appendix

### Evaluation Instance Summaries
[Links to individual evaluation reports]

### Methodology Notes
[Any deviations or special considerations]
```

---

## Command Interface

### Full Matrix Evaluation

```
/goal-eval --matrix

> Select goals to evaluate:
> [x] ACTIVATE: First generation
> [x] ACTIVATE: First delivery
> [ ] ADOPT: Weekly workflow
> [x] ADOPT: Customize output
>
> Select personas to evaluate:
> [x] Newsletter Creator
> [x] Content Ops Lead
> [ ] Technical Integrator
>
> This will run 6 evaluation instances. Proceed?
```

### Single Instance (Quick)

```
/goal-eval --goal "first_generation" --persona "newsletter_creator"

> Running single evaluation instance...
```

### Goal-Focused (All Personas)

```
/goal-eval --goal "first_generation" --all-personas

> Running goal across all personas (3 instances)...
```

### Persona-Focused (All Goals)

```
/goal-eval --persona "newsletter_creator" --phase ACTIVATE

> Running all ACTIVATE goals for Newsletter Creator (2 instances)...
```

---

## Value Proposition

### For Product Teams

**Before real user testing:**
- Catch obvious issues before users hit them
- Understand which personas are blocked vs. served
- Prioritize fixes by persona importance

**Systematic optimization:**
- Not random "find bugs" - targeted goal achievement
- Root cause attribution across layers
- Clear fix priorities

### For Engineering Teams

**Actionable output:**
- Issues traced to specific layers and code locations
- Not "the UX is confusing" but "mapping in file.py:234 is wrong"
- Priority based on goal/persona impact

**Regression potential:**
- Goal × Persona evaluations become test cases
- Re-run after changes to verify fixes
- Track improvement over time

### Complements Real User Testing

```
BEFORE USERS                          WITH USERS
────────────                          ──────────
Goal-Persona Evaluation               Real user testing
    │                                     │
    ▼                                     ▼
Catch systematic issues               Discover unknown unknowns
Optimize known paths                  Find unexpected behaviors
Fix blocking problems                 Validate assumptions
Prioritize by persona                 Learn real patterns
    │                                     │
    └─────────────┬───────────────────────┘
                  │
                  ▼
            Better Product
```

---

## Implementation Path

### Phase 1: Foundation
- [ ] Define goal library structure
- [ ] Define persona library structure
- [ ] Adapt Journey Agent for persona context
- [ ] Create single-instance evaluation flow

### Phase 2: Multi-Instance
- [ ] Build evaluation matrix runner
- [ ] Create instance storage/retrieval
- [ ] Build cross-instance correlation logic

### Phase 3: Synthesis
- [ ] Implement persona-level synthesis
- [ ] Implement goal-level synthesis
- [ ] Implement layer attribution
- [ ] Build master synthesis report

### Phase 4: Integration
- [ ] Unify command interface
- [ ] Linear integration for issue creation
- [ ] Regression test mode
- [ ] Historical comparison

---

## Open Questions

1. **Goal library curation**
   - Who defines goals? Product team? Auto-derived from features?
   - How granular? "First generation" vs. "Generate newsletter about tech"?

2. **Persona accuracy**
   - How do we validate personas match real users?
   - Feedback loop from real user testing?

3. **Evaluation parallelism**
   - Run instances sequentially or in parallel?
   - State isolation between instances?

4. **AI layer evaluation**
   - Always include trace analysis?
   - Only for generation goals?

5. **Comparison baselines**
   - Compare to previous evaluation runs?
   - Compare to competitor products?

---

## The One-Liner

> **Simulate diverse users pursuing real goals, trace through all system layers, synthesize into prioritized optimizations.**

This is systematic product optimization driven by user goals, not feature checklists.
