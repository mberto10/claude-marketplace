---
name: Goal-Driven E2E Evaluation
description: This skill should be used when the user asks to "evaluate a goal", "trace a user goal", "goal-driven evaluation", "test if users can achieve X", "evaluate end-to-end", "trace through layers", or wants to understand why a user goal succeeds or fails across UX, code, and infrastructure layers. Provides systematic methodology for tracing user goals through all system layers to identify root causes.
version: 0.1.0
---

# Goal-Driven End-to-End Evaluation

Systematic methodology for evaluating whether users can achieve specific goals, tracing problems across system layers to identify root causes.

**Core principle:** Users accomplish goals, not "use products". Problems can originate at one layer but manifest at another.

## The Framework

```
USER GOAL
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│                    SYSTEM LAYERS                        │
│                                                         │
│   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐               │
│   │ UX  │ → │CODE │ → │ AI  │ → │INFRA│               │
│   └─────┘   └─────┘   └─────┘   └─────┘               │
│                                                         │
│   User        Config      LLM calls    Database        │
│   interactions transforms Tool usage   Persistence     │
│   Feedback    Logic       Prompts      APIs            │
│   Friction    Handlers    Quality      State           │
└─────────────────────────────────────────────────────────┘
    │
    ▼
OUTCOME: Did the user achieve their goal?
    │
    ▼
ROOT CAUSE: Which layer is the origin of each problem?
```

## Goal Types

| Type | Description | Primary Layers |
|------|-------------|----------------|
| **Navigation** | User wants to find/reach something | UX |
| **Configuration** | User wants to set something up | UX, Code, Infra |
| **Generation** | User wants AI-generated output | All layers |
| **Operational** | User wants to monitor/manage | UX, Code, Infra |
| **Recovery** | User wants to fix something | UX, Code |

## Evaluation Workflow

### Step 1: Goal Definition

Establish what you're evaluating. Two approaches:

**From Goal Library:**
```
Read goals/{product}/{phase}.yaml
Select goal by ID
Load: statement, type, success_criteria, layer_weights
```

**Custom Goal:**
```
User provides: "I want to [specific outcome]"
Infer: goal type, relevant layers, success criteria
```

### Step 2: Gather Inputs

Ask user for:
1. **Product area** - Which part of the product? (e.g., design-studio)
2. **Goal** - Library goal ID or custom statement
3. **URL** - Starting point (e.g., localhost:3001/design-studio)
4. **Scope** - Full evaluation or specific layers only

### Step 3: Set Expectations

Before touching the product, document:

```markdown
## Evaluation Plan

**Goal:** [statement]
**Type:** [navigation/configuration/generation/operational/recovery]
**Phase:** [lifecycle phase]

### Expected User Journey
1. [Step 1]
2. [Step 2]
...

### Layer Analysis Plan
| Layer | Weight | Will Evaluate | Focus |
|-------|--------|---------------|-------|
| UX | [0.X] | [Yes/No] | [specific focus] |
| Code | [0.X] | [Yes/No] | [specific focus] |
| AI | [0.X] | [Yes/No] | [specific focus] |
| Infra | [0.X] | [Yes/No] | [specific focus] |

### Success Criteria
- [ ] [criterion 1]
- [ ] [criterion 2]
...
```

### Step 4: Execute Layer Analysis

Spawn appropriate agents based on goal type.

**For Configuration Goals (most common for Design Studio):**

1. **UX Layer** - Spawn `ux-evaluator` agent
   - Walk the user journey via browser
   - Document friction and clarity issues
   - Capture at checkpoints

2. **Code Layer** - Spawn `technical-debugger` agent
   - Trace data transforms
   - Check handlers and logic
   - Identify code gaps

3. **Infrastructure Layer** - Spawn `infrastructure-auditor` agent
   - Test API endpoints
   - Verify persistence
   - Check external services

4. **Fidelity Testing** (optional) - Spawn `config-fidelity-tester` agent
   - Test round-trip data integrity
   - Measure transform accuracy
   - Identify data loss points

### Step 5: Synthesize Findings

Correlate findings across layers:

For each issue:
```markdown
### Issue: [title]

**Symptom:** [What was observed]

**Layer Trace:**
- UX: [finding or N/A]
- Code: [finding or N/A]
- Infra: [finding or N/A]

**Root Cause:**
- Layer: [where problem originates]
- Location: [file:line or endpoint]
- Issue: [specific problem]

**Fix:** [recommendation]
**Priority:** [Critical/High/Medium/Low]
```

### Step 6: Generate Report

Produce unified evaluation report:

```markdown
# Goal Evaluation: [goal_id]

## Summary
| Metric | Value |
|--------|-------|
| Goal | [statement] |
| Achieved | [Yes/Partial/No] |
| Critical Issues | [count] |

## Success Criteria Status
- [x] [achieved]
- [ ] [failed] → Issue #X

## Issues by Origin Layer

### UX Layer
[issues originating in UX]

### Code Layer
[issues originating in code]

### Infrastructure Layer
[issues originating in infra]

## Prioritized Recommendations
1. [Critical] [fix]
2. [High] [fix]
...
```

### Step 7: Create Linear Issues (Optional)

If requested and Linear MCP available:
1. Create Project: "Goal Eval: [product] - [goal]"
2. Create Issues for each finding
3. Set priorities and relationships

## Using the Goal Library

### Design Studio Goals

Available goal files:
- `goals/design-studio/onboard.yaml` - First-time setup goals
- `goals/design-studio/activate.yaml` - First value goals
- `goals/design-studio/adopt.yaml` - Regular usage goals

### Loading a Goal

```
Read goals/design-studio/onboard.yaml
Find goal: first_design_creation
```

Returns:
```yaml
id: first_design_creation
statement: "Create my first design from scratch"
type: configuration
success_criteria:
  - User can find and click "New Design" action
  - Brand colors are configurable
  - Design saves successfully
  - Design persists after refresh
layer_weights:
  ux: 0.6
  code: 0.2
  ai: 0.0
  infra: 0.2
```

### Available Goals

| Phase | Goal ID | Type |
|-------|---------|------|
| ONBOARD | `first_design_creation` | configuration |
| ONBOARD | `template_start` | configuration |
| ONBOARD | `interface_orientation` | navigation |
| ONBOARD | `configure_brand_colors` | configuration |
| ACTIVATE | `preview_with_content` | configuration |
| ACTIVATE | `add_section` | configuration |
| ACTIVATE | `real_time_preview` | configuration |
| ACTIVATE | `understand_sections` | navigation |
| ADOPT | `edit_existing_design` | configuration |
| ADOPT | `recover_from_mistakes` | recovery |
| ADOPT | `manage_multiple_designs` | operational |
| ADOPT | `rapid_iteration` | configuration |
| ADOPT | `connect_to_composition` | configuration |

## Reference Files

- **`references/goal-types.md`** - Detailed evaluation strategies per goal type
- **`references/layer-analysis.md`** - Layer-specific analysis patterns
- **`references/synthesis-templates.md`** - Report and issue templates

## Integration Points

- **Goal Library** - `goals/` directory with YAML goal definitions
- **UX Evaluator** - Browser-based journey evaluation
- **Technical Debugger** - Code-level analysis
- **Infrastructure Auditor** - Backend verification
- **Config Fidelity Tester** - Round-trip data testing
- **Linear MCP** - Issue/project creation
