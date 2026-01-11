---
name: work-toolkit-youtrack
description: YouTrack operations and weekly reporting. Use when the user asks to add KW updates, review epic health, prepare JF agendas, create project overviews, compile weekly emails from YouTrack, update YouTrack epics, or sync Linear issues to YouTrack Aufgaben.
---

# Work Toolkit: YouTrack

Operate YouTrack as the official reporting system for project status and weekly updates.

## Hard Rules

- Write in German for stakeholder-facing content.
- Do not mention Linear IDs or Linear links in YouTrack.
- Use YouTrack IDs only (e.g., AI-301).

## Core Workflows

### KW Updates (Add or Update)

1. Find the epic by project name.
2. Determine current KW (calendar week).
3. Create or update the KW comment using the template.

Use `references/kw-comment-template.md`.

### Epic Health Review

1. List active epics.
2. Check: missing description, missing milestones, missing Bearbeiter, stale updates (>2 weeks).
3. Output a health report with action items.

### Project Overview (Prepare Update)

1. Fetch epic description + milestones.
2. Pull recent KW comments.
3. Summarize status, blockers, open Aufgaben, and next steps.

### JF Team Agenda

1. List epics for a specific Bearbeiter.
2. For each epic, summarize milestones, current KW update, blockers.
3. Flag items needing discussion.

### Weekly Email (Lenkungsausschuss)

1. Fetch all KW comments for the selected week.
2. Compile into a single email draft.

### Update YouTrack Epic from Linear

1. Gather Linear project activity (MCP or Linear script).
2. Convert into a KW update using the standard template.
3. Post comment to YouTrack (and optionally update Linear description).

### Sync Linear Issues to YouTrack Aufgaben

1. Find the epic in YouTrack.
2. List Linear issues in the project.
3. Create YouTrack Aufgaben for issues not yet linked.
4. Map status from Linear to YouTrack.

## Tooling

### YouTrack Scripts (Preferred)

```bash
python ~/.codex/skills/work-toolkit-youtrack/scripts/yt.py find-epic "Project Name"
python ~/.codex/skills/work-toolkit-youtrack/scripts/yt.py team-epics "Name"
python ~/.codex/skills/work-toolkit-youtrack/scripts/yt.py health-check "Name"
python ~/.codex/skills/work-toolkit-youtrack/scripts/yt.py comments AI-301 --full
python ~/.codex/skills/work-toolkit-youtrack/scripts/yt.py comment AI-301 "KW update text"
python ~/.codex/skills/work-toolkit-youtrack/scripts/get_kw_updates.py --kw=50
python ~/.codex/skills/work-toolkit-youtrack/scripts/sync_linear.py create AI-301 "Title" "Description"
python ~/.codex/skills/work-toolkit-youtrack/scripts/sync_linear.py update-state AI-401 "Aufgaben"
```

### Linear MCP (For Sync/Update)

Prefer Linear MCP when available:
- `mcp__linear__list_projects`
- `mcp__linear__list_issues`
- `mcp__linear__update_issue`

Fallback: use the Linear script from `work-toolkit-linear` if installed.

### Configuration

- Requires `YOUTRACK_API_TOKEN` in the environment.
- Base URL: `https://fazit.youtrack.cloud`.

## References

- `references/youtrack-documentation-guide.md`
- `references/api-reference.md`
- `references/kw-comment-template.md`
