# Linear GraphQL Queries

Use these queries when you need direct GraphQL access (fallback or debugging).

## My Assigned Issues

```graphql
query MyIssues {
  viewer {
    assignedIssues(
      filter: { state: { type: { nin: ["completed", "canceled"] } } }
      first: 50
      orderBy: updatedAt
    ) {
      nodes {
        id
        identifier
        title
        priority
        dueDate
        state { name type }
        project { name }
        labels { nodes { name } }
      }
    }
  }
}
```

## Project Activity (Recent)

```graphql
query ProjectIssues($filter: IssueFilter) {
  issues(filter: $filter, first: 100, orderBy: updatedAt) {
    nodes {
      identifier
      title
      updatedAt
      state { name type }
    }
  }
}
```

Variables example:
```json
{
  "filter": {
    "project": { "name": { "eq": "Project Name" } },
    "updatedAt": { "gte": "2026-01-01T00:00:00Z" }
  }
}
```

## Create Issue

```graphql
mutation CreateIssue($input: IssueCreateInput!) {
  issueCreate(input: $input) {
    success
    issue { id identifier title url }
  }
}
```

## Update Issue State

```graphql
mutation UpdateIssue($id: String!, $input: IssueUpdateInput!) {
  issueUpdate(id: $id, input: $input) {
    success
    issue { identifier state { name } }
  }
}
```
