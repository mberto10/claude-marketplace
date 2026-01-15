# Goal Library Schema

This document defines the structure for goal definitions used in Goal-Driven E2E Evaluation.

## Goal Definition Structure

```yaml
id: string                    # Unique identifier (snake_case)
statement: string             # User-centric "I want to..." statement
type: enum                    # Goal type classification
phase: enum                   # User lifecycle phase
success_criteria:             # Measurable outcomes (list)
  - string
layer_weights:                # Layer involvement (0.0-1.0)
  ux: number
  code: number
  ai: number
  infra: number
preconditions:                # Required state before starting
  - string
artifacts:                    # Optional reference files
  - path: string
    purpose: string
tags:                         # Optional categorization
  - string
```

## Field Definitions

### id
Unique identifier for the goal within its product/phase context.
- Format: `snake_case`
- Example: `first_design_creation`, `preview_with_content`

### statement
User-centric goal statement expressing what the user wants to accomplish.
- Format: "I want to..." or imperative form
- Should be specific and measurable
- Example: "Create my first design from scratch"

### type
Classification of goal type. Determines evaluation strategy.

| Type | Description | Primary Layers |
|------|-------------|----------------|
| `navigation` | User wants to find/reach something | UX |
| `configuration` | User wants to set something up | UX, Code, Infra |
| `generation` | User wants AI-generated output | All |
| `operational` | User wants to monitor/manage | UX, Code, Infra |
| `recovery` | User wants to fix something | UX, Code |

### phase
User lifecycle phase where this goal typically occurs.

| Phase | User Question | Focus |
|-------|---------------|-------|
| `DISCOVER` | "Why should I care?" | Value communication |
| `SIGN_UP` | "Let me in" | Account creation |
| `ONBOARD` | "Help me get started" | Initial setup |
| `ACTIVATE` | "Aha! This is useful" | First value |
| `ADOPT` | "This is how I use it" | Core workflow |
| `ENGAGE` | "I check this regularly" | Repeated use |
| `RETAIN` | "I can't work without this" | Ongoing value |
| `EXPAND` | "I want more" | Growth |

### success_criteria
List of specific, measurable outcomes that define goal completion.
- Should be testable via UI observation
- Include both functional and quality criteria
- Example:
  ```yaml
  success_criteria:
    - User can start a new blank design
    - Brand colors are configurable
    - Design saves without error
    - Design persists after refresh
  ```

### layer_weights
Relative importance of each system layer for this goal. Values 0.0-1.0.
- Determines which agents to spawn
- Guides analysis depth per layer
- Sum does not need to equal 1.0

| Layer | Analysis Focus |
|-------|----------------|
| `ux` | User interface, interactions, feedback |
| `code` | Logic, transforms, handlers |
| `ai` | LLM calls, prompts, quality |
| `infra` | Database, APIs, persistence |

Example:
```yaml
layer_weights:
  ux: 0.6      # Primary - heavy UI interaction
  code: 0.2    # Secondary - some transform logic
  ai: 0.0      # Not applicable
  infra: 0.2   # Secondary - persistence needed
```

### preconditions
State that must be true before the goal can be pursued.
- Used to validate test setup
- Documents assumptions
- Example:
  ```yaml
  preconditions:
    - User is logged in
    - Design Studio page is accessible
    - At least one design exists (for edit goals)
  ```

### artifacts (optional)
Reference files that help evaluate the goal.
- Example outputs for comparison
- Configuration files
- Screenshots of expected state

```yaml
artifacts:
  - path: examples/design-studio/expected-preview.png
    purpose: Reference for successful preview rendering
```

### tags (optional)
Categorization tags for filtering and organization.
```yaml
tags:
  - critical-path
  - new-user
  - regression-test
```

## Example Complete Goal

```yaml
id: first_design_creation
statement: "Create my first design from scratch"
type: configuration
phase: ONBOARD
success_criteria:
  - User can start a new blank design
  - Brand colors are configurable
  - At least one section can be added
  - Design saves and persists after refresh
layer_weights:
  ux: 0.6
  code: 0.2
  ai: 0.0
  infra: 0.2
preconditions:
  - User is logged in
  - Design Studio is accessible
tags:
  - critical-path
  - new-user
```

## Goal File Organization

Goals are organized by product and phase:

```
goals/
├── schema.md                 # This file
├── index.yaml                # Master index
└── {product}/                # Product-specific goals
    ├── onboard.yaml          # ONBOARD phase goals
    ├── activate.yaml         # ACTIVATE phase goals
    ├── adopt.yaml            # ADOPT phase goals
    └── ...                   # Other phases as needed
```

## Versioning

Goal definitions may evolve. Track changes via:
1. Git history of goal files
2. `version` field in index.yaml
3. Changelog in product goal directory (optional)
