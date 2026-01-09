# Dogfooding Methodology

> A systematic approach to product optimization using agentic coding agents.

## Core Premise

Traditional dogfooding means "eat your own dog food" — use your own product to find problems. With agentic coding agents, we can systematize this into a repeatable loop that not only finds problems but traces them to root causes and verifies fixes.

**The insight:** Agents can adopt user personas authentically, experience products without developer bias, trace issues through code, and verify infrastructure — all in a single coordinated flow.

## The Dogfooding Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE DOGFOODING LOOP                         │
│                                                                 │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│    │          │     │          │     │          │              │
│    │  BUILD   │────▶│ DOGFOOD  │────▶│   FIX    │              │
│    │          │     │          │     │          │              │
│    └──────────┘     └──────────┘     └──────────┘              │
│          ▲                                  │                   │
│          │                                  │                   │
│          │          ┌──────────┐            │                   │
│          │          │          │            │                   │
│          └──────────│ COMPOUND │◀───────────┘                   │
│                     │          │                                │
│                     └──────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Phase | What Happens | Output |
|-------|--------------|--------|
| **BUILD** | Implement features, make changes | Working code |
| **DOGFOOD** | Experience product as real user, trace issues | Reports + Issues |
| **FIX** | Address root causes identified | Improved product |
| **COMPOUND** | Encode learnings for future cycles | Better evaluator |

The loop is continuous. Each cycle should leave both the **product** and the **evaluation process** better than before.

## Why Agents Excel at Dogfooding

### The Bias Problem

Human developers can't truly dogfood their own products because:
- They know what the button is supposed to do
- They remember the workaround for that edge case
- They unconsciously avoid the broken flow
- They make excuses: "users will figure it out"

### The Agent Advantage

Agents can:
- **Adopt personas completely** — become the target user without developer knowledge
- **Stay naive by design** — don't read code during experience evaluation
- **React authentically** — no excuses, just document what happened
- **Maintain separation** — different agents for experience vs. debugging
- **Scale evaluation** — run multiple user journeys, multiple personas

### The Constraint That Enables Authenticity

The key constraint: **The experience evaluator must never read code.**

This forces authentic user perspective. The agent documents WHAT happened, not WHY. A separate agent traces the WHY by reading code. This clean separation prevents bias contamination.

---

## The Three-Layer Model

The dogfooding evaluation uses three distinct layers, each with a different perspective and purpose.

```
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 1: CONSUMER EXPERIENCE                                    │
│                                                                 │
│ Perspective: The actual user/consumer                           │
│ Constraint:  Never reads implementation code                    │
│ Question:    "What is my experience using this?"                │
│                                                                 │
│ Documents:                                                      │
│   • Confusion and friction                                      │
│   • Broken functionality                                        │
│   • Missing capabilities                                        │
│   • Unmet expectations                                          │
│   • Value assessment                                            │
│                                                                 │
│ Output: Experience Report (symptoms, not causes)                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    Experience Report
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 2: IMPLEMENTATION VERIFICATION                            │
│                                                                 │
│ Perspective: Developer/engineer                                 │
│ Input:       Experience report from Layer 1                     │
│ Question:    "Why does the system behave this way?"             │
│                                                                 │
│ Investigates:                                                   │
│   • Traces symptoms to code locations                           │
│   • Maps data flow through system                               │
│   • Identifies root causes                                      │
│   • Proposes specific fixes                                     │
│                                                                 │
│ Output: Technical Analysis (file:line, root causes, fixes)      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    Technical Analysis
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 3: FOUNDATION VERIFICATION                                │
│                                                                 │
│ Perspective: Infrastructure/operations                          │
│ Question:    "Is the underlying system real and reliable?"      │
│                                                                 │
│ Verifies:                                                       │
│   • Backend services actually implemented                       │
│   • Data actually persists                                      │
│   • External integrations actually connected                    │
│   • Operational concerns addressed                              │
│                                                                 │
│ Output: Infrastructure Audit (reality vs. facade)               │
└─────────────────────────────────────────────────────────────────┘
```

### Why Three Layers?

Each layer catches different failure modes:

| Layer | Catches | Misses |
|-------|---------|--------|
| Layer 1 only | UX problems | Root causes, infrastructure gaps |
| Layer 1+2 | UX + code issues | Facade implementations, ops gaps |
| All three | Complete picture | — |

A product can pass Layer 1 (feels okay) but fail Layer 3 (nothing actually persists). The three layers together prevent "demo-ware" — products that look good but don't work.

### The Information Flow

```
Layer 1 produces symptoms  → "Form submission feels broken"
Layer 2 explains causes    → "Handler doesn't await async call (api.ts:47)"
Layer 3 verifies reality   → "Database table exists but no data persists"
```

Each layer informs the next. Layer 2 can't investigate without Layer 1's findings. Layer 3 validates Layer 2's assumptions about infrastructure.

---

## Universal Structure, Domain-Specific Methods

The three-layer structure applies to any product type. What changes is the **method** of evaluation, not the **structure**.

### The Universal Pattern

```
Layer 1: [Consumer Type] Experience
         → Adopt consumer persona
         → Use the product as they would
         → Document friction without reading implementation

Layer 2: [Domain] Implementation Debug
         → Take Layer 1 findings as input
         → Trace to specific code/logic
         → Identify root causes and fixes

Layer 3: [Domain] Foundation Audit
         → Verify underlying systems work
         → Check operational readiness
         → Identify gaps between facade and reality
```

### Domain Instantiations

#### UI/Frontend Products

| Layer | Consumer | Method | Tools |
|-------|----------|--------|-------|
| Layer 1 | Human user | Browser automation, click through flows | Playwright |
| Layer 2 | Developer | Trace components, handlers, state | Code search |
| Layer 3 | Ops | Verify DB, auth, APIs work | Direct queries |

**Layer 1 persona:** "I am a [target user] trying to [accomplish goal]."

**Key constraint:** Experience evaluator uses only browser, never reads code.

---

#### Backend APIs

| Layer | Consumer | Method | Tools |
|-------|----------|--------|-------|
| Layer 1 | Developer integrating | Write actual client code | HTTP client, SDK |
| Layer 2 | Backend developer | Trace handlers, validation | Code search |
| Layer 3 | Ops | Verify DB, auth, rate limits, monitoring | Direct access |

**Layer 1 persona:** "I am a developer trying to integrate this API into my application."

**Layer 1 documents:**
- Documentation gaps or inaccuracies
- Unexpected response formats
- Missing endpoints for common operations
- Unhelpful error messages
- Authentication friction
- Rate limiting surprises
- SDK ergonomics issues

**Key constraint:** Only use public docs and API responses, not server code.

---

#### Data Pipelines

| Layer | Consumer | Method | Tools |
|-------|----------|--------|-------|
| Layer 1 | Analyst/scientist | Query output, attempt real analysis | SQL, notebooks |
| Layer 2 | Data engineer | Trace transformations, joins | Pipeline code |
| Layer 3 | Ops | Verify scheduling, recovery, scaling | Orchestrator |

**Layer 1 persona:** "I am an analyst trying to use this data for [specific analysis]."

**Layer 1 documents:**
- Missing or unexpected fields
- Data quality issues (nulls, duplicates, outliers)
- Stale or delayed data
- Schema doesn't match documentation
- Joins that should work but don't
- Performance issues at query time

**Key constraint:** Only query output tables, don't read transformation code.

---

#### CLI Tools

| Layer | Consumer | Method | Tools |
|-------|----------|--------|-------|
| Layer 1 | Terminal user | Run actual commands | Shell |
| Layer 2 | Developer | Trace argument parsing, execution | Code search |
| Layer 3 | Ops | Cross-platform, dependencies, permissions | Multi-env test |

**Layer 1 persona:** "I am a [user type] trying to [accomplish task] via command line."

**Layer 1 documents:**
- Confusing command structure
- Unhelpful error messages
- Missing or unclear help text
- Unexpected behavior
- Silent failures
- Output format issues

**Key constraint:** Only use --help and documentation, not source code.

---

#### Libraries/SDKs

| Layer | Consumer | Method | Tools |
|-------|----------|--------|-------|
| Layer 1 | Developer using library | Import and use in real code | IDE, REPL |
| Layer 2 | Library maintainer | Trace implementation | Code search |
| Layer 3 | Ops | Distribution, versioning, compatibility | Package managers |

**Layer 1 persona:** "I am a developer adding this library to my project."

**Layer 1 documents:**
- Installation friction
- Import/setup complexity
- API doesn't match docs
- Unexpected exceptions
- Type issues (if typed)
- Missing common use cases

**Key constraint:** Only use published docs and package, not library source.

---

## The Experience Report

Layer 1 produces an Experience Report. This is the foundation for all subsequent analysis.

### Report Structure

```markdown
# Experience Report: [Flow/Feature Name]

## Context
- **Date:** [timestamp]
- **Persona:** [who you adopted]
- **Goal:** [what you tried to accomplish]
- **Starting point:** [where you began]

## Journey Narrative

[First-person account of the experience, step by step]

### Step 1: [Action taken]
- **Expected:** [what you thought would happen]
- **Actual:** [what actually happened]
- **Feeling:** [confusion/frustration/delight/etc.]

### Step 2: ...

## Findings

### Critical (Blocked goal)
1. [Finding with specific observation]

### High (Significant friction)
1. [Finding with specific observation]

### Medium (Noticeable issues)
1. [Finding with specific observation]

### Low (Polish)
1. [Finding with specific observation]

## Value Assessment

1. Did I understand what this product does? [yes/no, why]
2. Could I accomplish my goal? [yes/no, why]
3. Would I use this again? [yes/no, why]
4. Would I recommend this? [yes/no, why]

## Raw Observations

[Anything else noticed that doesn't fit above]
```

### Severity Classification

| Severity | Definition | Example |
|----------|------------|---------|
| **Critical** | Cannot accomplish goal | Form submission fails silently |
| **High** | Significant degradation | Error message doesn't explain fix |
| **Medium** | Noticeable friction | Extra clicks to reach key action |
| **Low** | Polish issues | Inconsistent button styling |

---

## The Technical Analysis

Layer 2 takes the Experience Report and produces technical root causes.

### Analysis Structure

```markdown
# Technical Analysis: [Flow/Feature Name]

## Input
Experience Report from [date]

## Issue Investigation

### Issue 1: [Title from Experience Report]

**Symptom:** [What the user experienced]

**Investigation:**
1. [Step taken to locate code]
2. [What was found]
3. [Data flow traced]

**Root Cause:**
[Specific explanation with file:line references]

**Data Flow:**
```
User Action → Component (file:line)
           → Handler (file:line)
           → Service (file:line)
           → [Break point identified]
```

**Recommended Fix:**
```
[Specific code change or approach]
```

**Complexity:** [Low/Medium/High]

### Issue 2: ...

## Issue Categories

| Category | Count | Issues |
|----------|-------|--------|
| Technical Bug | N | #1, #3 |
| Integration Gap | N | #2 |
| Implementation Gap | N | #4, #5 |
| UX Gap | N | #6 |

## Fix Priority

1. [Issue] - [Complexity] - [Impact]
2. ...
```

---

## The Infrastructure Audit

Layer 3 verifies that the foundation is real, not facade.

### Audit Structure

```markdown
# Infrastructure Audit: [Flow/Feature Name]

## Verification Checklist

### Database Reality
- [ ] Tables exist for required data
- [ ] Data actually persists after operations
- [ ] Queries return expected results
- [ ] No hardcoded/stub data

### Authentication Reality
- [ ] User records exist in database
- [ ] Sessions actually persist
- [ ] Token refresh works
- [ ] Logout actually invalidates

### API Reality
- [ ] Endpoints exist and respond
- [ ] Not returning mock data
- [ ] Error handling implemented
- [ ] Rate limiting enforced (if claimed)

### Integration Reality
- [ ] External services actually called
- [ ] Credentials configured
- [ ] Fallback behavior works
- [ ] Webhooks actually fire

### Operational Reality
- [ ] Logging captures key events
- [ ] Errors tracked/reported
- [ ] Monitoring in place
- [ ] Backup/recovery possible

## Findings

### Verified Working
- [Component]: [Evidence]

### Facade/Stub Detected
- [Component]: [What's missing]

### Not Implemented
- [Component]: [What's needed]

## Implementation Checklist

Priority items to make this production-real:
1. [ ] [Specific task]
2. [ ] [Specific task]
```

---

## Running the Loop

### Prerequisites

1. **Product concept defined** — What is this? Who is it for? What value does it deliver?
2. **Target flow identified** — Which user journey to evaluate
3. **Access available** — Can reach the product (URL, credentials, etc.)

### Execution Flow

```
1. PREPARE
   │
   ├── Load product context (concept, target user, value prop)
   ├── Identify flow to evaluate
   └── Set up access (dev server, test accounts)
   │
   ▼
2. LAYER 1: EXPERIENCE
   │
   ├── Adopt target user persona completely
   ├── Experience the flow naturally
   ├── Document everything without reading code
   └── Produce Experience Report
   │
   ▼
3. LAYER 2: DEBUG
   │
   ├── Take Experience Report as input
   ├── Investigate each finding
   ├── Trace to specific code locations
   └── Produce Technical Analysis
   │
   ▼
4. LAYER 3: AUDIT
   │
   ├── Verify infrastructure claims
   ├── Check what's real vs. facade
   ├── Identify operational gaps
   └── Produce Infrastructure Audit
   │
   ▼
5. CREATE ISSUES
   │
   ├── Convert findings to trackable issues
   ├── Prioritize by severity and complexity
   └── Assign to appropriate workstreams
   │
   ▼
6. FIX
   │
   ├── Address issues in priority order
   ├── Verify each fix
   └── Mark issues complete
   │
   ▼
7. COMPOUND (optional)
   │
   ├── Extract patterns from this cycle
   ├── Identify learnings worth encoding
   └── Improve evaluation process
   │
   ▼
8. REPEAT
   │
   └── Next flow, or re-evaluate same flow
```

### Evaluation Depth Options

| Depth | Layers | When to Use |
|-------|--------|-------------|
| Quick | Layer 1 only | Rapid feedback, early development |
| Standard | Layers 1 + 2 | Most evaluations |
| Full | All three layers | Pre-launch, critical flows |

---

## The Compound Step

After fixes are implemented, optionally run the compound step to improve future evaluations.

### The Challenge

The dogfooding process itself doesn't change between cycles. The product improves (via fixes), but how does the **evaluator** improve?

### Encoding Learnings

Learnings should be:
- **One level above the incident** — smallest generalization that prevents repeat
- **Testable** — can verify compliance
- **Triggerable** — clear when it applies

### Value Filter

```
value = recurrence × impact × half-life - encoding_cost

If positive → encode
If negative → keep as observation only
```

### Where Learnings Land

| Learning Type | Destination | Example |
|--------------|-------------|---------|
| Product-specific pattern | Product config file | "This product's users expect <2s load" |
| Evaluation heuristic | Evaluation checklist | "Forms must show loading within 100ms" |
| Investigation pattern | Debug methodology | "Pattern: Optimistic UI without rollback" |
| Domain methodology | Domain reference | "API errors must include request ID" |

### Strong vs. Weak Compounding

| Mechanism | Will Execute? | Compounds? |
|-----------|---------------|------------|
| Add to large reference doc | Maybe | Weak |
| Add to mandatory checklist | Yes | Medium |
| Generate automated test | Yes | Strong |
| Add to product context | Yes | Medium |

Prefer mechanisms that **will execute**, not just expand documentation.

---

## Integration with Agentic Coding

This methodology is designed for agentic coding environments like Claude Code.

### Agent Separation

| Agent | Perspective | Constraint |
|-------|-------------|------------|
| Experience Evaluator | User | Never reads code |
| Technical Debugger | Developer | Reads code, traces issues |
| Infrastructure Auditor | Ops | Verifies systems |

The separation prevents bias. An agent that reads code cannot authentically experience as a user.

### Tool Access by Layer

| Layer | Tools Needed |
|-------|--------------|
| Layer 1 | Browser automation (Playwright), product access |
| Layer 2 | Code search (Glob, Grep, Read), codebase access |
| Layer 3 | Database access, API testing, system commands |

### Orchestration

The dogfooding command orchestrates all three layers:

```
/dogfood "signup flow"

→ Gathers product context
→ Launches Layer 1 agent (experience)
→ Waits for Experience Report
→ Launches Layer 2 agent (debug) with report
→ Waits for Technical Analysis
→ Launches Layer 3 agent (audit)
→ Waits for Infrastructure Audit
→ Creates issues from all findings
→ Optionally runs compound step
```

### Model Selection

| Agent | Recommended Model | Rationale |
|-------|-------------------|-----------|
| Experience Evaluator | Opus/Sonnet | Needs nuanced persona adoption |
| Technical Debugger | Sonnet | Code tracing, pattern matching |
| Infrastructure Auditor | Sonnet | Systematic verification |

---

## Success Metrics

### Per-Cycle Metrics

- **Findings discovered** — Issues found per evaluation
- **Fix rate** — Issues fixed within cycle
- **Severity distribution** — Critical/High/Medium/Low ratio
- **Time to resolution** — From finding to fix

### Cross-Cycle Metrics

- **Regression rate** — Do fixed issues recur?
- **New issue rate** — Issues per evaluation over time (should decrease)
- **Coverage growth** — Flows evaluated, personas tested
- **Compound rate** — Learnings encoded per cycle

### Health Indicators

| Indicator | Healthy | Unhealthy |
|-----------|---------|-----------|
| Critical issues | Decreasing | Flat or increasing |
| Fix cycle time | Decreasing | Increasing |
| Layer 3 failures | Rare | Frequent |
| Regression rate | Near zero | Significant |

---

## Anti-Patterns

### Breaking the Constraint

**Problem:** Experience evaluator reads code to "understand" the product.

**Result:** Loses authentic user perspective. Makes excuses. Misses real friction.

**Fix:** Strict separation. Experience agent has no code access.

### Skipping Layers

**Problem:** Only run Layer 1, skip technical debug.

**Result:** Symptoms documented but not traced. Fixes address wrong causes.

**Fix:** Always run at least Layers 1+2 for actionable findings.

### Facade Satisfaction

**Problem:** Product passes Layer 1+2 but Layer 3 never run.

**Result:** Ship demo-ware. Nothing persists. Infrastructure gaps discovered in production.

**Fix:** Run full evaluation before launch.

### Compound Skipping

**Problem:** Run evaluations but never encode learnings.

**Result:** Same issues keep appearing. Evaluator doesn't improve.

**Fix:** Make compound step part of the cycle, even if brief.

---

## Getting Started

### Minimum Viable Dogfooding

1. Define product concept (one paragraph)
2. Identify one critical user flow
3. Run Layer 1 (experience evaluation)
4. Run Layer 2 (technical debug)
5. Fix critical and high issues
6. Repeat

### Scaling Up

1. Add Layer 3 for pre-launch evaluation
2. Cover multiple flows
3. Test multiple personas
4. Add compound step
5. Track metrics across cycles

### Maturity Model

| Level | Characteristics |
|-------|-----------------|
| **1 - Ad hoc** | Occasional manual testing |
| **2 - Structured** | Regular dogfooding with 3-layer model |
| **3 - Systematic** | All critical flows covered, issues tracked |
| **4 - Optimizing** | Compound step active, evaluator improving |
| **5 - Predictive** | Metrics predict issues before users find them |

---

## Summary

The dogfooding methodology provides:

1. **Authentic user perspective** — through persona adoption and code separation
2. **Root cause tracing** — from symptoms to specific code locations
3. **Reality verification** — distinguishing working systems from facades
4. **Continuous improvement** — via the compound step

The three-layer structure is **universal** across product types. What changes is the method of evaluation, not the structure:

- Layer 1 always adopts the consumer perspective
- Layer 2 always traces to implementation
- Layer 3 always verifies the foundation

This creates a systematic loop for product optimization that leverages the unique capabilities of agentic coding agents.
