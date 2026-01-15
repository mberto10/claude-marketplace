# Full-Stack Generation Dogfooding

> **Status:** Concept / Brainstorming
> **Date:** 2026-01-15

## Overview

A new dogfooding approach that evaluates the **complete generation pipeline** from UI interaction through AI execution to output quality. Instead of generic product exploration, Claude performs a **specific, measurable task** and traces the entire system path.

**Core insight:** Real users don't "explore products" - they try to accomplish specific goals. Dogfooding should mirror this.

---

## The Scenario

```
USER TASK: "Here's an article from [Newsletter X]. I want to automate
           creating similar articles weekly. Set this up for me."

INPUT: Reference article text
GOAL: Configure the system to replicate this style/format
SUCCESS: Generated output matches reference quality and style
```

Claude acts as a user with a concrete goal, navigates the UI to configure the system, triggers generation, and evaluates whether it worked.

---

## Why This Matters

### Current Dogfooding Limitations

| Current Approach | Limitation |
|------------------|------------|
| Generic exploration | No objective success criteria |
| "Find friction" | Doesn't test if the product actually works |
| UX-only focus | Misses AI quality and infrastructure issues |
| Single-layer analysis | Can't trace problems to their source |

### Full-Stack Dogfooding Advantages

| Advantage | Description |
|-----------|-------------|
| Objective success | Compare output to reference - did it work? |
| End-to-end coverage | UI → Config → AI → Output → Quality |
| Root cause tracing | Every problem traced to its origin layer |
| Regression potential | Reference articles become reusable test cases |

---

## Architecture

### Stage Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                         INPUTS                                      │
│  • Reference article (text)                                         │
│  • Task description ("replicate this style weekly")                 │
│  • Dev server URL                                                   │
│  • Langfuse access (for trace analysis)                             │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 1: E2E JOURNEY AGENT                                         │
│  ─────────────────────────────                                      │
│                                                                     │
│  Claude as user with specific task:                                 │
│  1. Navigate to creation flow                                       │
│  2. Analyze reference article → infer needed configuration          │
│  3. Make configuration choices in UI                                │
│  4. Document friction, confusion, missing guidance                  │
│  5. Trigger generation run                                          │
│  6. Wait for completion                                             │
│  7. Capture generated output                                        │
│                                                                     │
│  OUTPUT: journey-report.md                                          │
│  • UX friction findings                                             │
│  • Configuration choices made (and why)                             │
│  • Questions that arose during configuration                        │
│  • Job ID / trace ID for downstream analysis                        │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┬───────────────────┐
          │                   │                   │                   │
          ▼                   ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  STAGE 2A       │ │  STAGE 2B       │ │  STAGE 2C       │ │  STAGE 2D       │
│  OUTPUT         │ │  TRACE          │ │  CODE           │ │  INFRA          │
│  EVALUATOR      │ │  ANALYST        │ │  DEBUGGER       │ │  AUDITOR        │
├─────────────────┤ ├─────────────────┤ ├─────────────────┤ ├─────────────────┤
│ Compare output  │ │ Read Langfuse   │ │ Investigate     │ │ Verify data     │
│ to reference    │ │ traces          │ │ code paths      │ │ persistence     │
│                 │ │                 │ │                 │ │                 │
│ • Style match   │ │ • Research      │ │ • Missing       │ │ • Config saved? │
│ • Tone match    │ │   quality       │ │   handlers      │ │ • Run persisted?│
│ • Structure     │ │ • Tool usage    │ │ • Broken paths  │ │ • Output stored?│
│ • Quality       │ │ • Edit cycles   │ │ • Guard issues  │ │ • APIs called?  │
│                 │ │ • Token costs   │ │                 │ │                 │
│ OUTPUT:         │ │ OUTPUT:         │ │ OUTPUT:         │ │ OUTPUT:         │
│ output-eval.md  │ │ trace-analysis  │ │ technical-      │ │ infra-audit.md  │
│                 │ │ .md             │ │ analysis.md     │ │                 │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │                   │
         └───────────────────┴─────────┬─────────┴───────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 3: OPTIMIZATION SYNTHESIZER                                  │
│  ─────────────────────────────────────                              │
│                                                                     │
│  Cross-layer root cause analysis:                                   │
│  • Correlate UX choices → config saved → AI behavior → output      │
│  • Identify which layer caused each problem                         │
│  • Prioritize by impact on task success                             │
│                                                                     │
│  OUTPUT: optimization-report.md                                     │
│  • Issues by origin layer                                           │
│  • Root cause chains                                                │
│  • Prioritized fix recommendations                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Agent Specifications

### Stage 1: E2E Journey Agent

**Role:** User with a specific task to accomplish

**Mindset:** "I have this article. I want to automate creating similar ones. Let me figure out how to set this up."

**Process:**

1. **Analyze reference article** before touching UI
   - What's the format? (newsletter, brief, analysis)
   - What's the tone? (formal, conversational, technical)
   - What's the structure? (sections, length, style)
   - What research would be needed? (news, data, sources)

2. **Form expectations**
   - "I expect to be able to configure tone as conversational"
   - "I expect to specify word count around 800 words"
   - "I expect to choose research sources"

3. **Navigate creation flow**
   - Document each step
   - Note when expectations aren't met
   - Note when guidance is unclear
   - Make best-effort configuration choices

4. **Trigger generation**
   - Start the workflow run
   - Capture job ID for trace analysis

5. **Wait and capture output**
   - Poll for completion
   - Save generated output for evaluation

**Output Schema:**

```markdown
# E2E Journey Report

## Reference Article Analysis
- Format: [identified format]
- Tone: [identified tone]
- Structure: [identified structure]
- Estimated word count: [X words]
- Research needs: [what sources would be needed]

## Pre-Journey Expectations
- [ ] Expectation 1
- [ ] Expectation 2
- ...

## Journey Narrative
[Step-by-step account of navigation]

## Configuration Choices Made
| Setting | Value Chosen | Why | Confidence |
|---------|--------------|-----|------------|
| Format | Newsletter | Matched reference | High |
| Tone | Conversational | Couldn't find exact option | Medium |
| ... | ... | ... | ... |

## Friction Points
[Finding cards for UX issues]

## Unanswered Questions
- "What does 'research depth' mean?"
- "Should I use Perplexity or Exa for news?"
- ...

## Run Information
- Job ID: [job_id]
- Trace ID: [trace_id]
- Started: [timestamp]
- Completed: [timestamp]
```

---

### Stage 2A: Output Evaluator Agent

**Role:** Quality assessor comparing generated output to reference

**Evaluation Dimensions:**

#### Style Match (0-100)
- Sentence structure patterns
- Vocabulary sophistication level
- Rhetorical devices used
- Formatting conventions

#### Tone Match (0-100)
- Formality level (formal ↔ casual)
- Voice (authoritative, conversational, analytical)
- Perspective handling (first person, third person)
- Emotional register

#### Structure Match (0-100)
- Opening/hook pattern
- Section organization
- Transition style
- Conclusion approach
- Length alignment

#### Content Quality (0-100)
- Information density
- Source quality (if visible)
- Accuracy (if verifiable)
- Completeness

**Output Schema:**

```markdown
# Output Evaluation Report

## Overall Match Score: [X]/100

## Dimension Scores

### Style Match: [X]/100
[Analysis with examples]

### Tone Match: [X]/100
[Analysis with examples]

### Structure Match: [X]/100
[Analysis with examples]

### Content Quality: [X]/100
[Analysis]

## Side-by-Side Comparison

| Aspect | Reference | Generated | Delta |
|--------|-----------|-----------|-------|
| Word count | 850 | 720 | -15% |
| Sections | 4 | 3 | -1 |
| Tone | Conversational | Formal | Mismatch |
| ... | ... | ... | ... |

## Key Differences
1. [Most significant difference]
2. [Second most significant]
...

## Quality Verdict
[ ] Output matches reference quality
[ ] Output is close but has notable gaps
[ ] Output significantly differs from reference
[ ] Output fails to replicate reference style
```

---

### Stage 2B: Trace Analyst Agent

**Role:** AI system investigator reading execution traces

**Data Sources:**
- Langfuse traces for the job
- Node execution logs
- Tool call records
- LLM input/output pairs

**Investigation Questions:**

#### Research Phase
- What tools were called?
- What queries were used?
- How much context was gathered?
- Any tool failures or timeouts?
- Was research sufficient for reference-quality output?

#### Write Phase
- What prompt was sent to the writer?
- Was tone/style configuration passed correctly?
- What was the raw output before editing?
- Token usage vs. output length ratio

#### Edit Phase
- What checks ran?
- What scores were achieved?
- How many edit iterations?
- What specific edits were made?
- Final quality gate results

#### Cost & Efficiency
- Total tokens used
- Cost breakdown by phase
- Time per phase
- Retry counts

**Output Schema:**

```markdown
# Trace Analysis Report

## Execution Summary
- Total duration: [X seconds]
- Total tokens: [X]
- Total cost: $[X.XX]
- Edit iterations: [X]

## Research Phase Analysis

### Tools Called
| Tool | Query/Input | Results | Quality |
|------|-------------|---------|---------|
| perplexity | "..." | 5 sources | Good |
| ... | ... | ... | ... |

### Research Sufficiency
- Reference article info density: [high/medium/low]
- Research gathered: [assessment]
- Gap: [what was missed]

## Write Phase Analysis

### Configuration Received
- Tone setting: [what writer node received]
- Style guidance: [what was passed]
- Word count target: [X]

### Output Assessment
- Raw output length: [X words]
- Tone in output: [detected tone]
- Match to config: [yes/no + explanation]

## Edit Phase Analysis

### Checks Executed
| Check | Score | Threshold | Pass |
|-------|-------|-----------|------|
| tone_consistency | 7.2 | 8.0 | No |
| ... | ... | ... | ... |

### Edit Iterations
- Iteration 1: [what changed]
- Iteration 2: [what changed]
- Final score: [X]

## Anomalies Detected
1. [Unexpected behavior]
2. [Missing expected call]
...

## AI System Issues
[Issues originating in AI layer, not UX or code]
```

---

### Stage 2C: Code Debugger Agent

*Existing technical-debugger agent, extended with trace context*

Additional focus:
- Why did trace show X when config showed Y?
- Where is the code path that handles this configuration?
- What's missing in the mapping/transformation?

---

### Stage 2D: Infrastructure Auditor Agent

*Existing infrastructure-auditor agent*

Additional focus:
- Was the configuration actually persisted?
- Did the job record get created correctly?
- Is the output stored and retrievable?

---

### Stage 3: Optimization Synthesizer

**Role:** Cross-layer correlation and root cause identification

**Process:**

1. **Ingest all stage 2 reports**
2. **Build issue inventory** across all layers
3. **Correlate issues** - trace each problem through layers
4. **Identify root causes** - which layer is the origin?
5. **Prioritize by task impact** - what blocked success?

**Root Cause Chain Format:**

```markdown
## Issue: Output tone was too formal (user wanted conversational)

### Symptom Chain

```
USER SELECTED: "Conversational" tone in UI
         ↓
CONFIG SAVED: tone="conversational" ✓ (verified in DB)
         ↓
TRACE SHOWS: writer_node received tone="professional" ✗
         ↓
OUTPUT: Formal tone detected
```

### Layer Analysis

| Layer | Status | Evidence |
|-------|--------|----------|
| UX | ✓ OK | User selected correctly |
| Infrastructure | ✓ OK | Config persisted correctly |
| Code | ✗ ISSUE | Tone mapping missing "conversational" |
| AI | — | Behaved correctly given input |

### Root Cause
**Code layer:** `composition.py:234` - TONE_MAP doesn't include "conversational", falls back to "professional"

### Fix
Add mapping: `"conversational": "casual, friendly, approachable"`
```

**Output Schema:**

```markdown
# Optimization Report

## Task Outcome
- Goal: Replicate [reference article] style
- Result: [Success / Partial / Failed]
- Overall match score: [X]/100

## Issue Summary by Layer

| Layer | Critical | High | Medium | Low |
|-------|----------|------|--------|-----|
| UX | 1 | 2 | 3 | 1 |
| AI | 0 | 1 | 2 | 0 |
| Code | 2 | 1 | 0 | 0 |
| Infra | 0 | 0 | 1 | 0 |

## Root Cause Chains

### Chain 1: [Issue title]
[Full chain analysis]

### Chain 2: [Issue title]
[Full chain analysis]

...

## Prioritized Fixes

### P0 - Blocked Task Success
1. [Fix with layer, location, effort estimate]

### P1 - Degraded Output Quality
1. [Fix]
2. [Fix]

### P2 - UX Friction (task completable)
1. [Fix]
2. [Fix]

## Regression Test Case
This evaluation can be reused as a regression test:
- Input: [reference article hash/location]
- Expected: Match score > 80, no P0 issues
- Config: [snapshot of choices made]
```

---

## Command Interface

```
/dogfood-generation

DESCRIPTION:
  Full-stack dogfooding with a specific generation task.
  Claude configures the system via UI, triggers generation,
  and evaluates the complete pipeline from UX to output quality.

INPUTS:
  1. Reference article
     - Paste text directly, OR
     - Provide file path, OR
     - Provide URL to fetch

  2. Task description
     - What should the automation do?
     - e.g., "Create similar articles weekly about tech stocks"

  3. Dev server URL
     - Default: http://localhost:5173

  4. Langfuse access (optional)
     - Project ID for trace analysis
     - If not provided, skip trace analysis stage

  5. Evaluation depth
     - quick: Stage 1 + 2A only (UX + output quality)
     - standard: All stages except infra audit
     - thorough: All stages including infrastructure

OUTPUTS:
  - journey-report-{flow}.md
  - output-evaluation-{flow}.md
  - trace-analysis-{flow}.md (if Langfuse access)
  - technical-analysis-{flow}.md
  - infrastructure-audit-{flow}.md (if thorough)
  - optimization-report-{flow}.md (synthesized)
```

---

## Example Walkthrough

### Input

```
Reference Article: [800-word conversational tech newsletter about AI developments]
Task: "I want to create a weekly newsletter like this about AI news"
URL: http://localhost:5173
```

### Stage 1: Journey

Claude navigates:
1. Opens Command Center
2. Clicks "New Publication"
3. Selects "Newsletter" format
4. Looks for tone setting - finds "Writing Style" dropdown
5. Options are: Professional, Casual, Technical - no "Conversational"
6. Selects "Casual" as closest match (notes friction)
7. Configures word count: 800
8. Selects research tools: Perplexity for news
9. Triggers test run
10. Waits for completion

Friction found:
- "Conversational" tone not available
- Unclear what "research depth" levels mean
- No preview of what output will look like

### Stage 2A: Output Evaluation

- Style match: 72/100 (similar structure, different voice)
- Tone match: 58/100 (output more formal than reference)
- Structure match: 85/100 (good section organization)
- Quality: 78/100 (solid content, less engaging)

Key gap: Tone mismatch is primary issue

### Stage 2B: Trace Analysis

- Research phase: Good tool selection, sufficient sources
- Write phase: Received tone="casual" but output reads formal
- Edit phase: No tone check configured, passed quality gate

Issue: Writer LLM not responding to "casual" tone instruction effectively

### Stage 2C: Code Analysis

- Tone mapping exists but "casual" maps to generic instruction
- Writer prompt template doesn't emphasize tone strongly
- No tone-specific examples in prompt

### Stage 3: Synthesis

```
ROOT CAUSE CHAIN:

UX: User selected "Casual" (closest to conversational) ✓
Code: "Casual" maps to weak tone instruction ✗
AI: Writer doesn't get strong enough guidance ✗
Output: Formal tone despite casual setting

FIXES:
1. [UX] Add "Conversational" as explicit tone option
2. [Code] Strengthen tone mapping with specific instructions
3. [AI] Add tone examples to writer prompt template
```

---

## Open Questions

1. **Langfuse integration** - How to programmatically access traces?
   - API access?
   - Direct DB queries?
   - Export format?

2. **Reference article analysis** - How sophisticated should this be?
   - Simple heuristics (word count, sentence length)?
   - LLM-based style analysis?
   - Quantitative metrics only?

3. **Output comparison** - What's the right comparison approach?
   - Side-by-side LLM evaluation?
   - Quantitative metrics?
   - Human-calibrated rubric?

4. **Scope boundaries** - Where does this end?
   - Single generation run?
   - Multiple runs with variations?
   - A/B comparison of configurations?

5. **Failure modes** - What if generation fails completely?
   - Still valuable (identifies blocking issues)
   - Different report format needed?

---

## Related Concepts

### Persona-Based Dogfooding
- This approach could combine with persona-based evaluation
- Different personas would approach the same reference article differently
- A "newsletter creator" vs "content ops" person would make different config choices

### Regression Testing
- Successful runs become regression test cases
- Reference article + expected match score = test assertion
- Can run periodically to catch regressions

### A/B Configuration Testing
- Run same reference article with different configurations
- Compare which settings produce better match
- Optimize default configurations based on data

---

## Implementation Considerations

### New Components Needed
1. **E2E Journey Agent** - Extended dogfooding-evaluator with task focus
2. **Output Evaluator Agent** - New agent for quality comparison
3. **Trace Analyst Agent** - New agent for Langfuse trace reading
4. **Optimization Synthesizer** - New agent for cross-layer correlation

### Existing Components to Extend
1. **Technical Debugger** - Add trace context awareness
2. **Infrastructure Auditor** - Add generation-specific checks

### Integration Points
1. Langfuse API for trace retrieval
2. Job API for run status polling
3. Output retrieval (where is generated content stored?)

---

## Next Steps

1. [ ] Validate concept with real walkthrough
2. [ ] Design Langfuse integration approach
3. [ ] Define output comparison rubric
4. [ ] Draft agent specifications in detail
5. [ ] Implement Stage 1 agent (E2E Journey)
6. [ ] Implement Stage 2A agent (Output Evaluator)
7. [ ] Implement Stage 2B agent (Trace Analyst)
8. [ ] Implement Stage 3 synthesizer
9. [ ] Create command interface
10. [ ] Test with real reference articles
