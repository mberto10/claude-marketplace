---
name: work-toolkit-linear
description: Daily planning and Linear task management. Use when the user asks to check Linear tasks, plan their day/week, create or update Linear issues, mark tasks done or in progress, search issues, or summarize project activity for weekly updates.
---

# Work Toolkit: Linear

Enable daily planning and task execution using Linear as the source of truth.

## Quick Start

1. Ask for scope: today, week, or a specific project.
2. Fetch Linear data (MCP first, script fallback).
3. Summarize priorities and confirm next actions.

## Core Workflows

### Daily Planning

1. List assigned tasks (open only).
2. Identify top 1-3 priorities.
3. Propose a time-blocked plan.
4. Confirm the plan and update issue states if requested.

### Task Operations

- List tasks
- List tasks due today
- Create new issue
- Move issue to in progress
- Mark issue done
- Search issues by title

### Project Activity Summary

Generate a 7-day activity summary for a project to support weekly updates.

## Tooling

### Prefer Linear MCP

Use MCP if available:
- `mcp__linear__list_issues`
- `mcp__linear__create_issue`
- `mcp__linear__update_issue`
- `mcp__linear__list_projects`

### Script Fallback

Use the bundled script if MCP is unavailable:

```bash
python ~/.codex/skills/work-toolkit-linear/scripts/linear.py tasks
python ~/.codex/skills/work-toolkit-linear/scripts/linear.py today
python ~/.codex/skills/work-toolkit-linear/scripts/linear.py create "Issue title"
python ~/.codex/skills/work-toolkit-linear/scripts/linear.py progress ABC-123
python ~/.codex/skills/work-toolkit-linear/scripts/linear.py done ABC-123
python ~/.codex/skills/work-toolkit-linear/scripts/linear.py search "query"
python ~/.codex/skills/work-toolkit-linear/scripts/linear.py project-activity "Project Name" --days=7
```

### Configuration

- Requires `LINEAR_API_KEY` in the environment.

## Output Standards

- Keep summaries short and actionable.
- For daily plans, show 1-3 priorities with time blocks.
- If listing tasks, group by state (In Progress, Todo).

## References

- `references/graphql-queries.md`
