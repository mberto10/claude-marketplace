---
name: compound-discovery-craft
description: This skill should be used when the user invokes "/compound:discover", asks to "find patterns", "extract workflows", "what could be a skill", "what could be a command", "what could be an agent", "modularize this", "discover repeatable procedures", or wants to identify work patterns that could become new plugin components. Provides methodology for pattern extraction and component type selection.
---

# Discovery Craft

## Purpose

Analyze work sessions to discover modularizable patterns and determine the right component type: skill, command workflow, agent, or hook. This is pattern extraction with architectural guidance.

## When to Use

- User invokes /compound:discover
- User asks to find repeatable patterns or modularize workflows
- User wants a specification for a new capability

## Foundation

Load `references/compounding-methodology.md` for the underlying philosophy and decision gates.

## This is Different From /compound:reflect

| /compound:reflect | /compound:discover |
|------------------|--------------------|
| Improve existing plugins | Create new components |
| Fix friction | Extract patterns |
| Output: change proposal | Output: component specification |

## The Skills-as-Modules Lens

Every repeatable procedure with clear inputs and outputs can become a loadable module. Ask:

"What procedure lives in people's heads that could be a plugin component?"

## Component Type Selection

### Skills

Use when the pattern provides specialized knowledge or methodology that Codex should apply when relevant.

Characteristics:
- Knowledge-based, not action-based
- Activates automatically based on context
- Provides guidance, workflows, domain expertise
- User does not have to invoke directly

Examples:
- How to analyze Langfuse traces effectively
- Best practices for German business emails
- The compound loop methodology

### Commands (Workflow in a Skill)

Use when the pattern is a user-initiated action with clear steps.

Characteristics:
- User explicitly invokes with /command-name
- Has defined inputs and outputs
- Executes a specific workflow
- May use skills for guidance during execution

Examples:
- /reflect - capture learnings
- /draft - write content
- /analyze-traces - trace analysis

### Agents

Use when the pattern requires autonomous, multi-step work that benefits from specialization.

Characteristics:
- Launched via Task tool, runs independently
- Has specific expertise and tool access
- Returns results to the parent conversation
- Good for parallelizable or complex subtasks

### Hooks

Use when the pattern should happen automatically in response to system events.

Characteristics:
- Event-driven (PreToolUse, PostToolUse, Stop, etc.)
- No user invocation
- For validation, logging, guardrails, automation
- Can block actions or modify behavior

## Decision Matrix

| Pattern Characteristic | Component |
|------------------------|-----------|
| Knowledge Codex should apply | Skill |
| Action user explicitly requests | Command workflow (in a skill) |
| Autonomous specialized subtask | Agent |
| Should happen on every event | Hook |
| Combines knowledge and action | Command workflow plus skill |
| Complex workflow with subspecialties | Command workflow plus agents |

## Compound Discover Workflow

### 1. Load Methodology

- Read `references/compounding-methodology.md`.
- Apply skills-as-modules, component selection, modularizability criteria.

### 2. Session Analysis

Examine what happened:
- What multi-step procedures were performed?
- What was done more than once?
- What domain knowledge was applied?
- What should have happened automatically but did not?
- What could have been delegated to a specialist?

If the user provided focus text, prioritize that area.

### 3. Parallel Exploration (Optional)

For complex pattern spaces, launch parallel agents if supported:

```
Launch Task with subagent_type="Explore":
"Find patterns similar to [X] in other parts of the codebase"

Launch Task with subagent_type="Explore":
"How do other plugins/tools solve [problem Y]?"
```

Go wide before deep. Synthesize findings before extraction.

### 4. Pattern Extraction

For each potential pattern, document:

```
PATTERN: [Name]
Trigger: When would this be needed?
Inputs: What does it start with?
Process: [3-7 steps]
Outputs: What does it produce?
Knowledge: What expertise is embedded?
```

### 5. Component Type Selection

Apply the decision matrix for each pattern:

```
COMPONENT ANALYSIS: [Pattern Name]
- Knowledge Codex should apply contextually? -> Skill
- Action user explicitly requests? -> Command workflow
- Autonomous work for a specialist? -> Agent
- Should happen automatically on events? -> Hook

Selected: [Component Type]
Reasoning: [Why this type fits]

If combination needed:
- Primary: [type] - [purpose]
- Supporting: [type] - [purpose]
```

### 6. Documentation Verification

Before generating specifications, verify current component patterns.

If a documentation agent is available, ask for:
- Current frontmatter requirements
- Available hook events (if proposing a hook)
- Best practices for the component type
- Recent changes to component structure

### 7. Modularizability Assessment

```
Modularizability Score
Recurrence likelihood:    [High/Med/Low]
Clear boundaries:         [Yes/Partial/No]
Teachable as instructions:[Yes/Partial/No]
Should be consistent:     [Yes/Partial/No]
Packaging value:          [High/Med/Low]

Verdict: [Worth modularizing | Maybe later | Not a good candidate]
```

### 8. Generate Specification

Based on the component type, generate the full spec.

Skill specification:
```markdown
## Proposed Skill: [name]

Location: plugins/[plugin-name]/skills/[skill-name]/

### Trigger Description
This skill should be used when the user asks to "[trigger 1]",
"[trigger 2]", "[trigger 3]", or [context].

### What It Provides
- [Knowledge area 1]
- [Workflow guidance]

### SKILL.md Structure
1. Purpose
2. Core Concepts
3. Workflow
4. Examples
5. References (if needed)

### Estimated Size
- SKILL.md: ~[X] words
- References: [yes/no]
- Scripts: [yes/no]
```

Command workflow specification:
```markdown
## Proposed Command: /[command-name]

Location: codex-skills/[skill-name]/SKILL.md

### Purpose
[What the user accomplishes]

### Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Inputs/Outputs
- Input: $ARGUMENTS = [what]
- Output: [what it produces]

### Skills Used
- [skill name] - [why]

### Agents Launched
- [agent name] - [for what]
```

Agent specification:
```markdown
## Proposed Agent: [agent-name]

Location: plugins/[plugin-name]/agents/[agent-name].md

### Frontmatter
```yaml
description: [agent expertise]
model: [sonnet/opus/haiku]
tools: [tool list]
```

### When to Use
<example>
Context: [situation]
user: "[message]"
assistant: "[how Codex invokes]"
<commentary>Why appropriate</commentary>
</example>

### System Prompt Summary
- Role: [what it is]
- Expertise: [specialty]
- Task: [what to accomplish]
- Output: [what it returns]

### Tools Required
- [Tool]: [why]
```

Hook specification:
```markdown
## Proposed Hook: [hook-name]

Location: plugins/[plugin-name]/hooks/hooks.json

### Event Type
PreToolUse | PostToolUse | Stop | SubagentStop | SessionStart | SessionEnd | UserPromptSubmit | PreCompact | Notification

### Matcher
[Tool pattern if applicable]

### Hook Type
command | prompt

### Purpose
[What it enforces/validates/logs]

### Configuration
```json
{
  "[Event]": [{
    "matcher": "[pattern]",
    "hooks": [{
      "type": "[type]",
      "command": "[path]" // or "prompt": "[instruction]"
    }]
  }]
}
```

### Behavior
- Triggers: [when]
- Action: [what]
- Blocks: [yes/no]
```

### 9. Create Discovery Artifact

If Linear is available:
- Team: MB90
- Project: Compound
- Labels: compound-discovery
- Title: `[compound-discover] YYYY-MM-DD: [component type]: [name]`

If Linear is not available, write to:
- `./compound-discoveries/YYYY-MM-DD-HHMMSS-[name].md`

### 10. Summary

Provide:
- Patterns analyzed count
- Components proposed (skills, commands, agents, hooks)
- Top candidate with location
- Artifact created link or file path
- Next steps (review, implement, test)

## Outputs

- A discovery artifact (Linear issue or `./compound-discoveries/YYYY-MM-DD-HHMMSS-[name].md`).
- A prioritized component specification ready for implementation.

## Prompting for Depth

If session context is thin, ask:
- What workflow did you just complete?
- What would you want to do the same way next time?
- What took multiple steps that should be simpler?
- What should have happened automatically?
- What subtask could a specialist have handled?

## Important Notes

- Consider all four component types
- Verify documentation before finalizing specs
- Quality over quantity: one good spec beats five vague ideas
- Pick the right component type
- Output should be implementation-ready
