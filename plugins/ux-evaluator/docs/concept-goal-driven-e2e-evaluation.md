# Goal-Driven End-to-End Evaluation Framework

> **Status:** Concept / Brainstorming
> **Date:** 2026-01-15

## Core Insight

Users don't "use products" - they **accomplish goals**. Every goal touches multiple system layers. Problems can originate at any layer but manifest elsewhere.

**Current evaluation approaches:**
- UX evaluation → finds friction in UI layer only
- Code debugging → finds bugs in code layer only
- Infrastructure audit → finds gaps in backend only

**What's missing:**
- Tracing a goal through ALL layers
- Identifying WHERE problems originate vs. where they manifest
- Optimizing the complete path, not just individual layers

---

## The Framework

### Concept: Goal → Layers → Outcome → Optimization

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   USER GOAL                                                         │
│   "I want to [specific outcome]"                                    │
│                                                                     │
│         │                                                           │
│         ▼                                                           │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                    SYSTEM LAYERS                            │   │
│   │                                                             │   │
│   │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐    │   │
│   │   │   UX    │ → │  CODE   │ → │   AI    │ → │  INFRA  │    │   │
│   │   │  Layer  │   │  Layer  │   │  Layer  │   │  Layer  │    │   │
│   │   └─────────┘   └─────────┘   └─────────┘   └─────────┘    │   │
│   │                                                             │   │
│   │   User        Config         LLM calls      Database        │   │
│   │   interactions transforms    Tool usage     Persistence     │   │
│   │   Choices     Mappings       Prompts        APIs            │   │
│   │   Friction    Logic          Quality        State           │   │
│   │                                                             │   │
│   └─────────────────────────────────────────────────────────────┘   │
│         │                                                           │
│         ▼                                                           │
│   OUTCOME                                                           │
│   Did the user achieve their goal?                                  │
│   How well? What friction? What failed?                             │
│                                                                     │
│         │                                                           │
│         ▼                                                           │
│   OPTIMIZATION                                                      │
│   For each problem: Which layer is the ROOT CAUSE?                  │
│   What's the fix? What's the priority?                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Connecting to User Lifecycle Framework

The existing User Lifecycle Framework defines 8 phases, each with characteristic user goals:

| Phase | User Question | Example Goals |
|-------|---------------|---------------|
| **DISCOVER** | "Why should I care?" | Understand value prop, see examples |
| **SIGN UP** | "Let me in" | Create account, verify identity |
| **ONBOARD** | "Help me get started" | Initial setup, first configuration |
| **ACTIVATE** | "Aha! This is useful" | First value moment, see it work |
| **ADOPT** | "This is how I use it" | Establish core workflow |
| **ENGAGE** | "I check this regularly" | Repeated use, habit formation |
| **RETAIN** | "I can't work without this" | Ongoing value, handle edge cases |
| **EXPAND** | "I want more" | Advanced features, upgrade, refer |

**Key insight:** Each phase contains goals that touch different layers with different weights.

### Layer Involvement by Phase

```
              UX    CODE    AI    INFRA
              ───   ────    ──    ─────
DISCOVER      ███   ░░░     ░░░   ░░░      (mostly UX)
SIGN UP       ██░   █░░     ░░░   ██░      (UX + infra)
ONBOARD       ███   ██░     ░░░   █░░      (UX + code)
ACTIVATE      ██░   ██░     ███   ██░      (all layers)
ADOPT         █░░   ██░     ███   ██░      (code + AI heavy)
ENGAGE        █░░   █░░     ███   ██░      (AI + infra heavy)
RETAIN        █░░   ██░     ██░   ███      (infra + code)
EXPAND        ██░   ██░     █░░   ██░      (balanced)

███ = Primary    ██░ = Secondary    █░░ = Minor    ░░░ = Minimal
```

---

## Goal Types & Evaluation Strategies

### Type 1: Navigation Goals
**Pattern:** User wants to find/reach something

```
Example: "Find where I configure email delivery"

Layers touched:
- UX: Information architecture, navigation patterns
- Code: Routing, feature flags
- AI: N/A
- Infra: N/A

Success criteria: User finds it without confusion
Evaluation: UX-focused with code verification
```

### Type 2: Configuration Goals
**Pattern:** User wants to set something up

```
Example: "Configure my newsletter's brand colors"

Layers touched:
- UX: Form design, options presented
- Code: Validation, storage logic
- AI: N/A (unless AI-assisted config)
- Infra: Persistence, retrieval

Success criteria: Config saved correctly, retrievable, applied
Evaluation: UX journey + infrastructure verification
```

### Type 3: Generation Goals
**Pattern:** User wants to create output via AI

```
Example: "Generate an article matching this reference"

Layers touched:
- UX: Configuration interface
- Code: Config transformation, workflow orchestration
- AI: Research, writing, editing quality
- Infra: Job execution, output storage

Success criteria: Output matches intent, quality sufficient
Evaluation: Full stack - all layers
```

### Type 4: Operational Goals
**Pattern:** User wants to monitor/manage ongoing operations

```
Example: "Check why my scheduled newsletter didn't send"

Layers touched:
- UX: Status visibility, error presentation
- Code: Logging, error handling
- AI: N/A (unless AI-assisted diagnosis)
- Infra: Job history, delivery logs

Success criteria: User can diagnose and resolve issue
Evaluation: UX + code + infrastructure
```

### Type 5: Recovery Goals
**Pattern:** User wants to fix something that went wrong

```
Example: "My article has wrong data, I need to fix and resend"

Layers touched:
- UX: Edit flows, retry mechanisms
- Code: Update logic, state management
- AI: Re-generation capability
- Infra: State persistence, delivery retry

Success criteria: User can correct and recover
Evaluation: Full stack with focus on state management
```

---

## Generalized Evaluation Process

### Phase 1: Goal Definition

```
INPUTS:
- Goal statement: "I want to [specific outcome]"
- Context:
  - Lifecycle phase (optional, can be inferred)
  - Persona (optional, affects expectations)
  - Success criteria (what does "done" look like?)
  - Reference artifacts (if applicable - example output, etc.)
```

### Phase 2: Expectation Setting

Before touching the product:
- What should the user journey look like?
- What layers will be involved?
- What could go wrong at each layer?
- What's the expected outcome?

### Phase 3: Goal Pursuit

Claude attempts to achieve the goal via UI:
- Documents each step
- Notes friction and confusion
- Makes choices and records rationale
- Continues until goal achieved or blocked

### Phase 4: Layer-Specific Analysis

Based on goal type, analyze relevant layers:

| Layer | Analysis Focus | Agent |
|-------|----------------|-------|
| UX | Friction, confusion, missing guidance | Journey Agent |
| Code | Logic errors, missing handlers, mapping issues | Code Debugger |
| AI | Quality, prompt effectiveness, tool usage | Trace Analyst |
| Infra | Persistence, APIs, external services | Infra Auditor |

### Phase 5: Outcome Evaluation

- Did the user achieve their goal?
- How well? (against success criteria)
- What friction occurred?
- What failed?

### Phase 6: Root Cause Synthesis

For each problem:
```
SYMPTOM: [What the user experienced]
    ↓
LAYER TRACE: [UX → Code → AI → Infra]
    ↓
ROOT CAUSE: [Which layer + specific location]
    ↓
FIX: [What to change]
```

---

## Example: Mapping Specific Goals

### ACTIVATE Phase Goal: "See my first generated newsletter"

```yaml
goal: "Generate and preview my first newsletter issue"
phase: ACTIVATE
persona: Newsletter Creator (non-technical)

success_criteria:
  - Newsletter generates without errors
  - Output appears in preview
  - Content is relevant to configured topic
  - Styling matches brand configuration

layer_expectations:
  ux:
    - Clear "generate" action
    - Progress indication during generation
    - Preview appears when done
  code:
    - Configuration passed to workflow correctly
    - Job created and tracked
    - Output routed to preview
  ai:
    - Research finds relevant sources
    - Writing matches configured tone
    - Quality passes editorial checks
  infra:
    - Job persists and completes
    - Output stored and retrievable
    - No external service failures
```

### RETAIN Phase Goal: "Figure out why my newsletter didn't send"

```yaml
goal: "Diagnose and fix a failed newsletter delivery"
phase: RETAIN
persona: Content Operations Lead

success_criteria:
  - User can find the failed run
  - Error reason is clear
  - User can take corrective action
  - User can retry successfully

layer_expectations:
  ux:
    - Failed runs visible in dashboard
    - Error messages human-readable
    - Retry action available
  code:
    - Error captured and categorized
    - Retry logic exists
    - State allows recovery
  ai:
    - N/A (unless AI-assisted diagnosis)
  infra:
    - Failure logged with details
    - External service errors captured
    - State consistent after failure
```

---

## Framework Components

### 1. Goal Library

Pre-defined goals mapped to lifecycle phases:

```yaml
# goals/activate.yaml
phase: ACTIVATE
goals:
  - id: first_generation
    statement: "Generate and preview my first content"
    success_criteria: [...]
    layer_weights: {ux: 0.3, code: 0.3, ai: 0.3, infra: 0.1}

  - id: first_delivery
    statement: "Send my first newsletter to myself"
    success_criteria: [...]
    layer_weights: {ux: 0.2, code: 0.2, ai: 0.2, infra: 0.4}
```

### 2. Layer Analyzers

Specialized agents for each layer:

| Layer | Agent | Focus |
|-------|-------|-------|
| UX | Journey Agent | Friction, confusion, flow |
| Code | Code Debugger | Logic, mappings, handlers |
| AI | Trace Analyst | Prompts, tools, quality |
| Infra | Infra Auditor | Persistence, APIs, state |

### 3. Synthesis Engine

Cross-layer correlation:
- Match symptoms to root causes
- Trace problems through layers
- Prioritize by goal impact

### 4. Optimization Report

Unified output:
- Goal achievement status
- Issues by origin layer
- Root cause chains
- Prioritized fixes

---

## Command Interface

### Option A: Phase-Based Entry

```
/goal-eval --phase ACTIVATE

> Which ACTIVATE goal do you want to evaluate?
> ○ First generation - "Generate and preview my first content"
> ○ First delivery - "Send my first newsletter"
> ○ Custom goal - Define your own
```

### Option B: Goal-Based Entry

```
/goal-eval "I want to create a weekly newsletter about AI news"

> Detected: ONBOARD/ACTIVATE phase goal
> Type: Generation goal
> Layers: All (UX, Code, AI, Infra)
>
> Proceed with full-stack evaluation?
```

### Option C: Reference-Based Entry (for generation goals)

```
/goal-eval --reference article.txt "Replicate this article style"

> Detected: Generation goal with reference artifact
> Will compare output to reference for quality assessment
> Layers: All (UX, Code, AI, Infra)
```

---

## Relationship to Existing Commands

```
CURRENT                          PROPOSED
───────                          ────────

/ux-eval
  └─ UX layer only          →    /goal-eval (UX layer)
                                   with goal context

/dogfood
  └─ UX + Code + Infra      →    /goal-eval (multi-layer)
                                   with goal context

/mcp-eval
  └─ Intent-driven UI       →    /goal-eval --type mcp
                                   specialized for MCP apps

[NEW]                            /goal-eval
                                   └─ Unified entry point
                                   └─ Goal-driven
                                   └─ Phase-aware
                                   └─ Layer-traced
                                   └─ Reference-comparable
```

---

## The Insight Crystallized

**Old mental model:**
> "Evaluate the product's UX/code/infrastructure"

**New mental model:**
> "Can a user achieve goal X? If not, which layer is blocking them? If yes but with friction, where does the friction originate?"

This reframes evaluation from **"find problems in layer Y"** to **"trace goal achievement across all layers."**

---

## Open Questions

1. **Goal library scope**
   - Pre-define common goals per phase?
   - Allow fully custom goals?
   - Both?

2. **Layer weight customization**
   - Fixed weights per goal type?
   - User-adjustable?
   - Auto-inferred from goal?

3. **Partial evaluations**
   - What if user only cares about UX layer?
   - Still trace other layers but lighter touch?
   - Explicit layer selection?

4. **Comparison mode**
   - Before/after evaluations?
   - A/B configuration comparison?
   - Historical trending?

5. **Automation**
   - Can this run as CI/CD check?
   - Scheduled goal evaluations?
   - Alert on regressions?

---

## Next Steps

1. [ ] Validate mental model - does this framing resonate?
2. [ ] Define goal library structure
3. [ ] Map existing agents to layer analyzers
4. [ ] Design synthesis logic
5. [ ] Prototype with one goal type (generation)
6. [ ] Extend to other goal types
7. [ ] Unify command interface
