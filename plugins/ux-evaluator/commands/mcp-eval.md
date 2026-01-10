---
description: Evaluate MCP app frontend through conversational intent lens
argument-hint: [flow-or-intent]
allowed-tools: Read, Glob, Grep, AskUserQuestion, Task, mcp__playwright__*, mcp__linear-server__*
---

# MCP Eval Command

Evaluate MCP-powered application frontends by walking the UI through the lens of conversational intent. Identifies where the tool→widget chain fails to serve user goals.

## What This Evaluates

For MCP apps, users arrive at screens via LLM conversations. This evaluation:
- Derives the target persona from the product concept
- Defines how they would naturally express their intent
- Walks UI screens as that persona
- Evaluates whether each screen's tool→widget chain serves the intent
- Detects MCP-specific failure patterns
- Categorizes improvements by layer (tool schema, tool output, widget, flow)

## Step 1: Gather Inputs

Use AskUserQuestion to collect:

**Question 1:** "Where is the product concept stored?"
- Linear document (specify document ID or name)
- Local file (path to product_concept.md or similar)

**Question 2:** "What intent or flow do you want to evaluate?"
Options:
- Core workflow (main value delivery)
- Search/browse flow
- Action/transaction flow
- Specific intent (specify in natural language)

**Question 3:** "What is the starting URL?"
Default: http://localhost:3000

**Question 4:** "What evaluation mode?"
- Hypothetical tracing (Recommended) - Infer tool calls from UI and codebase
- Actual tool calling - Call MCP tools directly via HTTP endpoint

**If actual tool calling selected:**

**Question 5:** "What is the MCP tool endpoint?"
Example: http://localhost:8000/api/mcp/call

## Step 2: Load Product Concept

Based on source selected:

**If Linear document:**
- Use `mcp__linear-server__get_document` to fetch
- Extract: product name, value proposition, target user, core workflow

**If local file:**
- Read the specified file
- Parse product concept content

Display understanding and confirm before proceeding.

## Step 3: Launch MCP Evaluator

Use the Task tool to launch the `mcp-evaluator` agent with:

```
Product Concept: [loaded content]
Target Intent/Flow: [selected flow]
Starting URL: [specified URL]
Mode: [Hypothetical | Actual Tool Calling]
Tool Endpoint: [if actual mode]

Your mission: Evaluate this MCP app frontend by walking the UI as the target persona.

1. Derive persona from product concept
2. Define natural conversation arc for this intent
3. Walk each screen, evaluating the tool→widget chain
4. Detect failure patterns at each turn
5. Categorize improvements by layer

Save your evaluation report to: mcp-eval-report-[flow].md
```

Wait for mcp-evaluator to complete and return the report.

## Step 4: Present Results

Show the user:
- Overall assessment
- Failure patterns found (count by type)
- Improvements by layer (count per layer)
- Top priority fixes

## Step 5: Technical Investigation (Optional)

Ask: "Would you like to trace these improvements to specific code locations?"

If yes, launch `technical-debugger` agent with:

```
MCP Evaluation Report: [path to report]

Your mission: For each improvement identified in the MCP evaluation report, trace to specific code locations.

Focus on:
- Tool schema improvements → Find tool definitions
- Tool output improvements → Find response formatting code
- Widget improvements → Find component implementations
- Flow improvements → Find routing/state management

Save your analysis to: technical-analysis-mcp-[flow].md
```

Wait for technical-debugger to complete.

## Step 6: Create Linear Project (Optional)

If Linear MCP is available, ask:
"Would you like to create a Linear project with issues for each improvement?"

If yes:
1. Get teams using `mcp__linear-server__list_teams`
2. Ask which team to use
3. Create project: "MCP Evaluation: [Product] - [Flow]"
4. Create issues organized by layer:
   - **Tool Schema** - label: `mcp`, `tool-schema`
   - **Tool Output** - label: `mcp`, `tool-output`
   - **Widget Design** - label: `frontend`, `widget`
   - **Flow Architecture** - label: `ux`, `flow`

## Step 7: Final Summary

Present combined results:

```
MCP EVALUATION COMPLETE
═══════════════════════

Product: [Name]
Flow Evaluated: [Intent/Flow]
Mode: [Hypothetical | Actual Tool Calling]

FAILURE PATTERNS DETECTED
─────────────────────────
Over-clarifying:     [N]
Under-clarifying:    [N]
Tool ping-pong:      [N]
Widget mismatch:     [N]
Poor edit loop:      [N]
No commit gate:      [N]
Error opacity:       [N]
─────────────────────────
Total:               [N]

IMPROVEMENTS BY LAYER
─────────────────────
Tool Schema:         [N]
Tool Output:         [N]
Widget Design:       [N]
Flow Architecture:   [N]
─────────────────────────
Total:               [N]

TOP PRIORITIES
──────────────
1. [Layer]: [Most critical improvement]
2. [Layer]: [Second priority]
3. [Layer]: [Third priority]

REPORTS GENERATED
─────────────────
• MCP Evaluation:     [path]
• Technical Analysis: [path if generated]

NEXT STEPS
──────────
[Specific recommendations based on findings]
```

## Usage Examples

### Evaluate search workflow with hypothetical tracing
```
/mcp-eval search workflow
```
Select "Hypothetical tracing" mode.

### Evaluate with actual tool calls
```
/mcp-eval "find flights"
```
Select "Actual tool calling" mode and provide endpoint.

### Full evaluation with technical analysis
```
/mcp-eval core workflow
```
Select full evaluation, then opt into technical debugger handoff.

### Interactive mode
```
/mcp-eval
```
Will prompt for all options.
