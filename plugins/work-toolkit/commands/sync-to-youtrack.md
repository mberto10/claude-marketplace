---
name: sync-to-youtrack
description: Sync Linear project issues to YouTrack Aufgaben under the matching epic
allowed-tools:
  - Bash
  - Read
  - mcp__linear-server__list_issues
  - mcp__linear-server__get_issue
  - mcp__linear-server__list_projects
  - mcp__linear-server__update_issue
argument-hint: "<project_name>"
---

# Sync to YouTrack Command

One-way sync from Linear project issues to YouTrack Aufgaben under an **existing epic**.

**Prerequisites:** The YouTrack epic must already exist with matching project name.

## Arguments

- `<project_name>`: Name of the project (must match in both Linear and YouTrack)
  - Linear: Project name
  - YouTrack: Epic summary (Type: Story, State: Projektticket)

## Status Mapping

```
Linear Status              →    YouTrack State
───────────────────────────────────────────────
Backlog, Todo, Unstarted   →    Backlog
In Progress, Started       →    Aufgaben
Done, Completed            →    Geschlossen
Canceled                   →    (skip)
```

## Workflow

### 1. Find YouTrack Epic

```bash
python ${CLAUDE_PLUGIN_ROOT}/helper_tools/youtrack/yt.py find-epic "<project_name>"
```

### 2. Get Linear Project Issues

Use Linear MCP to get all issues for the project:
- `mcp__linear-server__list_issues` with project filter
- Get issue title, state, description

### 3. Check Existing Sync

For each Linear issue, check if already synced by looking for `[YT:AI-XXX]` in Linear issue description.

### 4. Sync Logic

For each Linear issue:

**If NOT synced (no YouTrack ID in Linear):**
```bash
# Create YouTrack Aufgabe
python ${CLAUDE_PLUGIN_ROOT}/helper_tools/youtrack/yt.py create "<title>" "<description>"

# Then update Linear issue description to add [YT:AI-XXX] tag
```

**If already synced:**
```bash
# Update YouTrack Aufgabe status if changed
python ${CLAUDE_PLUGIN_ROOT}/helper_tools/youtrack/sync_status.py <youtrack_id> <new_state>
```

### 5. Set Parent Epic

After creating Aufgabe, link it to the epic as parent.

## Output Format

```markdown
# Sync: <project_name>

**Linear Project:** <project_id>
**YouTrack Epic:** AI-XXX

## Created (X)

| Linear | YouTrack | Title |
|--------|----------|-------|
| MB90-XXX | AI-XXX | Task title |

## Updated (X)

| YouTrack | Status Change |
|----------|---------------|
| AI-XXX | Aufgaben → Geschlossen |

## Unchanged (X)

Already in sync.

## Skipped (X)

Canceled issues not synced.
```

## Example

```bash
/sync-to-youtrack "Web Research Agents"
```

## Important Notes

- **Epic must exist**: Only creates Aufgaben under existing epic, never creates new epics
- **YouTrack stays clean**: No Linear IDs appear in YouTrack
- **Linear tracks mapping**: `[YT:AI-XXX]` added to Linear issue description
- **Titles as-is**: Keep titles from Linear (German or English)
- **Idempotent**: Safe to run multiple times

## Re-sync Behavior

- New Linear issues → Create YouTrack Aufgabe
- Status changed in Linear → Update YouTrack status
- Title changed → Update YouTrack title
- Linear issue deleted → YouTrack Aufgabe unchanged (manual cleanup)
