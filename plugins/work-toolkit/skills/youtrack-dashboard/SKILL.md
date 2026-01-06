---
name: YouTrack Dashboard
description: This skill should be used when the user asks to "write a youtrack comment", "create youtrack ticket", "update youtrack issue", "get youtrack comments", "compile weekly update from youtrack", "check epic status", "update youtrack epic", "review epic health", mentions "KW" (Kalenderwoche) updates, or references YouTrack issue IDs like "AI-74", "AI-76". Provides guidance for interacting with the YouTrack REST API at fazit.youtrack.cloud.
version: 0.3.0
---

# YouTrack Dashboard

Interact with YouTrack (fazit.youtrack.cloud) via REST API for ticket management, comments, and weekly status compilation.

## Important: No Linear References

**Never reference Linear or Linear issue IDs in YouTrack documentation.** Linear is a personal planning system. YouTrack is the official record for stakeholders and Lenkungsausschuss reporting.

When writing to YouTrack:
- Reference YouTrack Aufgaben (e.g., `AI-305`) not Linear issues
- Use YouTrack as the source of truth for project status
- Keep all official documentation in YouTrack only

## Slash Commands

### `/add-kw-update <project> <section> <content>`
Quickly add an entry to the current week's KW update:
- **section**: `update`, `blocker`, or `next`
- Automatically creates or updates the KW comment
- See `youtrack-documentation-guide.md` for format

Example: `/add-kw-update "Customer Support Chatbot" update "System prompt v2 deployed"`

### `/update-youtrack-epic <project_name>`
Generate a full KW update from project activity and post to YouTrack epic.

Option: `--dry-run` for preview without posting

### `/prepare-jf-team <team_member>`
Prepare JF agenda for all projects where a team member is Bearbeiter:
- Fetches all active epics for the person
- Shows milestones, current status, blockers
- Flags items needing attention

Example: `/prepare-jf-team "Maximilian"`

### `/review-epics [team_member]`
Review health of active epics:
- Missing descriptions/Projektziel
- Missing milestone tables
- No Bearbeiter assigned
- Stale updates (>2 weeks)

Example: `/review-epics` or `/review-epics "Maximilian"`

### `/weekly-email`
Compile weekly Lenkungsausschuss update from all YouTrack KW comments.

### `/sync-to-youtrack <project_name>`
Sync Linear project issues to YouTrack Aufgaben:
- Creates Aufgaben under matching epic
- Maps status: Backlog/Todo → Backlog, In Progress → Aufgaben, Done → Geschlossen
- Tracks mapping in Linear (YouTrack stays clean)

Example: `/sync-to-youtrack "Web Research Agents"`

## Recommended: Use helper_tools CLI

The `helper_tools/` directory contains ready-to-use Python scripts for all common YouTrack operations. **Prefer these over raw API calls.**

```bash
# Get ticket details
python helper_tools/youtrack/yt.py get AI-123

# Search tickets (defaults to AI project)
python helper_tools/youtrack/yt.py search "State: Open"
python helper_tools/youtrack/yt.py search "assignee: me"

# Find epic by project name
python helper_tools/youtrack/yt.py find-epic "Customer Support Chatbot"

# List team member's active epics
python helper_tools/youtrack/yt.py team-epics "Maximilian"

# Check epic health (descriptions, milestones, updates)
python helper_tools/youtrack/yt.py health-check "Maximilian"

# Create ticket in AI project
python helper_tools/youtrack/yt.py create "Bug: Login fails" "Users cannot log in"

# Add comment
python helper_tools/youtrack/yt.py comment AI-123 "Fixed in latest commit"

# Update existing comment
python helper_tools/youtrack/yt.py update-comment AI-123 4-443828 "Updated text..."

# Get comments (use --full for complete text)
python helper_tools/youtrack/yt.py comments AI-123 --full

# Get weekly KW updates from all epic tickets
python helper_tools/youtrack/get_kw_updates.py --kw=39

# Sync helpers (for Linear → YouTrack sync)
python helper_tools/youtrack/sync_linear.py create AI-62 "Task title" "Description"
python helper_tools/youtrack/sync_linear.py update-state AI-401 "Aufgaben"
python helper_tools/youtrack/sync_linear.py map-state "In Progress"  # → Aufgaben
```

See `helper_tools/README.md` for complete documentation.

## Configuration

**Base URL:** `https://fazit.youtrack.cloud`
**Authentication:** Bearer token via `YOUTRACK_API_TOKEN` environment variable
**Default Project:** AI (project ID: `0-331`)

### Request Headers

```
Authorization: Bearer $YOUTRACK_API_TOKEN
Accept: application/json
Content-Type: application/json
```

## Core Operations

### Get Issue Details

Retrieve a single issue by readable ID (e.g., `AI-74`):

```bash
curl -s "https://fazit.youtrack.cloud/api/issues/AI-74?fields=idReadable,summary,description,created,updated,reporter(name),assignee(name),customFields(name,value(name))" \
  -H "Authorization: Bearer $YOUTRACK_API_TOKEN" \
  -H "Accept: application/json"
```

### Search Issues

Query issues using YouTrack query syntax:

```bash
curl -s "https://fazit.youtrack.cloud/api/issues?query=project:AI%20State:Open&fields=idReadable,summary,description&\$top=50" \
  -H "Authorization: Bearer $YOUTRACK_API_TOKEN" \
  -H "Accept: application/json"
```

**Common query patterns:**
| Query | Purpose |
|-------|---------|
| `project: AI` | All issues in AI project |
| `project: AI Type: Story` | Epic/Story tickets only |
| `project: AI State: Projektticket` | Active project tickets |
| `project: AI assignee: me` | Issues assigned to current user |
| `project: AI updated: {Last week}` | Recently updated issues |

### Get Comments

Retrieve all comments for an issue:

```bash
curl -s "https://fazit.youtrack.cloud/api/issues/AI-74/comments?fields=id,text,created,author(name,login)&\$top=100" \
  -H "Authorization: Bearer $YOUTRACK_API_TOKEN" \
  -H "Accept: application/json"
```

### Add Comment

Post a new comment to an issue:

```bash
curl -s -X POST "https://fazit.youtrack.cloud/api/issues/AI-74/comments?fields=id,text,created,author(name)" \
  -H "Authorization: Bearer $YOUTRACK_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"text": "Comment text in **Markdown** format", "usesMarkdown": true}'
```

### Create Issue

Create a new issue in the AI project:

```bash
curl -s -X POST "https://fazit.youtrack.cloud/api/issues?fields=idReadable,summary" \
  -H "Authorization: Bearer $YOUTRACK_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "project": {"id": "0-331"},
    "summary": "Issue title",
    "description": "Detailed description"
  }'
```

## Weekly Update Workflow (KW Format)

Compile weekly status updates from YouTrack comments using German Kalenderwoche (KW) format.

### Recommended: Use helper_tools

```bash
# Get all KW updates for a specific week
python helper_tools/youtrack/get_kw_updates.py --kw=39

# Get project updates with structured output
python helper_tools/youtrack/get_weekly_project_updates.py --weeks-back=1 --format=markdown
```

## Project-Specific Configuration

### AI Project Custom Fields

| Field | Values |
|-------|--------|
| Type | Story, Task, Bug, Feature |
| State | Open, In Progress, Done, Projektticket |
| Priority | Critical, Major, Normal, Minor |
| Epic | (Dynamic - links to parent Story) |

## Tips

- **Markdown in comments:** Set `usesMarkdown: true` when posting comments for rich formatting
- **Field expansion:** Use the `fields` parameter to specify exactly which fields to return
- **Pagination:** Use `$top` and `$skip` parameters for large result sets
- **Date filtering:** YouTrack supports natural language dates like `{Last week}`, `{Today}`, `{This month}`

## Reference Files

- **`references/youtrack-documentation-guide.md`** - How we document in YouTrack (KW format, epic structure, best practices)
- **`references/api-reference.md`** - YouTrack REST API field reference
- **`examples/kw-comment-template.md`** - KW comment template with examples
