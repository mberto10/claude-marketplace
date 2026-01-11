# YouTrack API Reference (Minimal)

Base URL: `https://fazit.youtrack.cloud/api`

## Auth Headers

```
Authorization: Bearer $YOUTRACK_API_TOKEN
Accept: application/json
Content-Type: application/json
```

## Common Endpoints

- **Search issues**: `/issues?query=<query>&fields=<fields>&$top=50`
- **Issue details**: `/issues/{id}?fields=<fields>`
- **Comments**: `/issues/{id}/comments?fields=<fields>&$top=100`
- **Add comment**: `POST /issues/{id}/comments`
- **Create issue**: `POST /issues`

## Common Query Patterns

- `project: AI Type: Story State: Projektticket`
- `project: AI assignee: me`
- `project: AI updated: {Last week}`

## Field Snippet

`idReadable,summary,description,created,updated,reporter(name),assignee(name),customFields(name,value(name))`
