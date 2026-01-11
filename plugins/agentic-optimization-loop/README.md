# Agentic Optimization Loop

A Claude Code plugin for systematic, iterative improvement of AI agents through hypothesis-driven experimentation.

## Overview

This plugin implements the **Build → Evaluate → Analyze → Improve → Compound** loop for AI agent development. It maintains persistent state across sessions, allowing you to pause and resume optimization work.

## Key Features

- **Journal-driven state**: All progress persists in `.claude/optimization-loops/<agent>/`
- **Phase-aware**: Automatically detects where you are in the loop and continues
- **Hypothesis-driven**: Forces clear, testable hypotheses before changes
- **Compounding**: Captures learnings and grows your evaluation dataset over time

## Commands

### `/optimize [agent]`

Main entry point. Starts or continues an optimization loop.

```
/optimize my-agent
```

The command will:
1. Check for existing journal
2. Determine current phase
3. Guide you through the next steps

### `/optimize-status [agent]`

Quick status check without making changes.

```
/optimize-status my-agent
```

Shows current phase, metrics trajectory, and next action needed.

## The Optimization Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│         ┌───────────▶  HYPOTHESIZE                              │
│         │            What specific change will improve metrics? │
│         │                       │                               │
│         │                       ▼                               │
│         │              EXPERIMENT                               │
│         │            Implement change, run evaluation           │
│         │                       │                               │
│         │                       ▼                               │
│         │               ANALYZE                                 │
│         │            Did it work? Why/why not?                  │
│         │                       │                               │
│         │                       ▼                               │
│         │               COMPOUND                                │
│         └────────────  Capture learnings, grow dataset          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Prerequisites

1. **Langfuse tracing**: Your agent must have Langfuse instrumentation
2. **Dataset**: Either an existing evaluation dataset or production traces to build from
3. **Clear target**: Know what metric you're optimizing and the goal

## Quick Start

1. Ensure your agent has Langfuse tracing
2. Run `/optimize my-agent`
3. Follow the prompts to establish baseline
4. The plugin guides you through iterations

## Journal Structure

State persists in `.claude/optimization-loops/<agent>/`:

```
.claude/optimization-loops/my-agent/
├── journal.yaml           # Central state file
└── iterations/            # Detailed iteration records
    ├── 001-reasoning-step.md
    └── 002-tool-guidance.md
```

## Integration

Works with:
- **Langfuse**: For traces, datasets, prompts, and experiments
- **Your codebase**: For prompt and code changes
- **Any AI agent**: Framework-agnostic approach

## Philosophy

This plugin embodies principles from:
- Anthropic's evaluation-first development
- The scientific method (hypothesis → experiment → analysis)
- Compound improvement (each cycle makes the system better)

The goal is not just to improve your agent, but to build a **self-improving evaluation system** where failures become test cases and learnings accumulate.
