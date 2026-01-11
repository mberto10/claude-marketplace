---
name: compound-consolidation-craft
description: This skill should be used when the user invokes "/compound:consolidate", asks to "process learnings", "implement compound improvements", "review pending reflections", or wants to turn captured learnings into actual changes. Provides methodology for reviewing, approving, and implementing learning artifacts.
---

# Consolidation Craft

## Purpose

Process pending compound-reflect learnings and implement approved changes into skills or plugins. Consolidation is the second half of the compound loop where captured learnings become permanent improvements.

## Foundation

Load `references/compounding-methodology.md` for the underlying philosophy, heuristics format, and anti-patterns to avoid.

## Compound Consolidate Workflow

### 1. Gather Pending Learnings

If Linear is available:
- Team: MB90
- Project: Compound
- Labels: compound-learning
- Status: Not done

If Linear is not available, check local:
```
./compound-learnings/*.md
```

If the user provided filter text, apply it to narrow results (plugin names, learning types, keywords, file paths).

### 2. Present Each Learning for Review

For each learning, present:

```markdown
## Learning #1 [source-date]

Type: rule | feature | fix
Plugin: affected-plugin-name
Learning: The one-line learning statement

Proposed Change:
- File: path/to/file
- Action: update | create | delete
- Description: What specifically to change

Recommendation: Approve | Defer | Reject
Reasoning: Why this change is or is not worth implementing
```

Group by plugin for easier review when multiple learnings exist.

### 3. Evolvability and Cross-Pollination Check

Before asking for approval, evaluate each proposed change:

Evolvability check:
- [ ] Modular: Can this skill or command workflow change independently?
- [ ] Loosely coupled: No hidden dependencies on other skills?
- [ ] Adaptable: Does this make future changes easier or harder?

Cross-pollination check:
- [ ] Could this learning apply to other plugins or domains?
- [ ] Should this be a shared pattern instead?
- [ ] Is there a more general capability hiding in this specific learning?

If a change reduces evolvability, flag it. Sometimes worth it, but should be conscious.

### 4. Get Approval

For each learning, the user can:
- Approve: implement the change
- Defer: keep for later (do not close issue)
- Reject: close without implementing (with reason)
- Modify: adjust the proposed change before implementing

Wait for explicit approval before making changes. Never auto-implement.

### 5. Propose Edits With Reasoning

Before making any change, show the specific edit:

```markdown
## Proposed Edit

File: path/to/file

Current:
```
[existing content]
```

Proposed:
```
[new content]
```

Reasoning:
Why this change implements the learning

Approve this change? [y/n/modify]
```

Only edit after explicit confirmation.

### 6. Implement Approved Changes

Implement based on type:

Rule -> Skill update
- Add to relevant SKILL.md or CLAUDE.md
- Use imperative form and include source reference

Feature -> New capability
- For this Codex port, create a new skill or extend an existing SKILL.md with a command-style workflow
- If the capability is broad, create a new skill directory

Fix -> Edit existing
- Update skill description triggers
- Correct workflow behavior
- Fix inaccurate documentation

Architecture -> Structure change
- Update plugin or skill structure
- Add or remove directories
- Adjust metadata if needed

### 7. Close the Loop

If Linear:
- Close the issue with a comment referencing the changes

If local files:
- Move processed file to `./compound-learnings/archived/` or delete if not needed

### 8. Verify Implementation

After changes:
- Confirm files were updated correctly
- Note if testing is needed
- Suggest follow-up if changes need validation

### 9. Summary Report

After processing all learnings:

```
Consolidation complete
Processed: X learnings
- Approved and implemented: Y
- Deferred: Z
- Rejected: W

Files modified:
- [file1]: [brief change]
- [file2]: [brief change]

Suggested commit message:
compound: implement learnings from [date range]

- [skill]: [change summary]
- [skill]: [change summary]

Closes: [issue IDs or local learning files]
```

## Change Implementation Patterns

Updating skill descriptions:
```yaml
# Before
description: This skill handles X.

# After
description: This skill should be used when the user asks to "do X", "perform X", "X workflow", or mentions X-related tasks.
```

Adding rules to skills:
```markdown
## Operational Rules

- When processing >100 items, use pagination [src:2025-12-25]
- Always validate inputs before API calls [src:2025-12-20]
```

Extending existing skills:
- Add to the appropriate section in SKILL.md
- Or create a new reference file if substantial
- Update SKILL.md to reference the new file

## User Filter Integration

When the user provides filter text:

```
/compound:consolidate only langfuse improvements
-> Filter to learnings tagged with langfuse or affecting langfuse skills

/compound:consolidate skill descriptions only
-> Filter to learnings of type "fix" targeting skill descriptions
```

Match against:
- Plugin or skill names
- Learning types (rule, feature, fix)
- Keywords in learning text
- File paths in proposed changes

## Output Expectations

After consolidation:
1. Summary of processed learnings
2. Changes made (files modified)
3. Commit suggestion if multiple changes
4. Follow-up items needing testing or review

## Important Notes

- Never auto-implement; always show changes and get confirmation
- Provide reasoning for each recommendation
- Group by plugin or skill when multiple learnings exist
- Respect user filter text
- Quality over speed
