# Synthesis and Report Templates

Templates for cross-layer synthesis and final reports.

## Root Cause Analysis Template

For each issue discovered:

```markdown
### Issue: [Brief descriptive title]

**ID:** [issue-001, issue-002, etc.]
**Severity:** [Critical | High | Medium | Low]

---

#### Symptom
[What was observed - user-facing description]

#### Layer Trace

| Layer | Finding | Contributes? |
|-------|---------|--------------|
| UX | [observation or "No issues found"] | [Yes/No] |
| Code | [observation or "No issues found"] | [Yes/No] |
| AI | [observation or "N/A"] | [Yes/No] |
| Infra | [observation or "No issues found"] | [Yes/No] |

#### Root Cause

**Origin Layer:** [UX | Code | AI | Infra]

**Location:** [file:line or API endpoint or UI element]

**Specific Issue:**
[Detailed technical description of what's wrong]

#### Contributing Factors

[Other layers that made the problem worse or masked it]

1. [Contributing factor 1 - layer and description]
2. [Contributing factor 2 - layer and description]

#### Fix

**Primary Fix:** (addresses root cause)
```
[Code change, configuration, migration, etc.]
```

**Secondary Fixes:** (addresses contributing factors)
1. [Fix for contributing factor 1]
2. [Fix for contributing factor 2]

#### Impact on Goal

[How this issue affects user's ability to achieve the goal]

- [ ] Blocks goal completely
- [ ] Partially blocks goal
- [ ] Adds friction but goal achievable
- [ ] Minor inconvenience
```

---

## Goal Evaluation Report Template

```markdown
# Goal Evaluation Report

**Date:** [YYYY-MM-DD]
**Evaluator:** Claude (Goal-Driven E2E Framework)

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Goal** | [goal statement] |
| **Product** | [product area] |
| **Phase** | [lifecycle phase] |
| **Goal Type** | [navigation/configuration/generation/operational/recovery] |
| **Achievement** | [Achieved / Partially Achieved / Not Achieved] |
| **Critical Issues** | [count] |
| **High Issues** | [count] |
| **Medium Issues** | [count] |
| **Low Issues** | [count] |
| **Total Issues** | [count] |

### One-Line Summary
[Single sentence describing overall finding]

---

## Goal Definition

**Statement:** [full goal statement]

**Success Criteria:**
| # | Criterion | Status |
|---|-----------|--------|
| 1 | [criterion] | [✅ Passed / ❌ Failed / ⚠️ Partial] |
| 2 | [criterion] | [status] |
| ... | ... | ... |

**Layer Weights:**
| Layer | Weight | Analyzed |
|-------|--------|----------|
| UX | [0.X] | [Yes/No] |
| Code | [0.X] | [Yes/No] |
| AI | [0.X] | [Yes/No] |
| Infra | [0.X] | [Yes/No] |

---

## Issues Summary

### By Origin Layer

```
UX Layer:     [████░░░░░░] [X] issues
Code Layer:   [██████░░░░] [Y] issues
AI Layer:     [░░░░░░░░░░] [0] issues
Infra Layer:  [████████░░] [Z] issues
```

### Critical Issues

| ID | Title | Origin Layer | Blocks Goal |
|----|-------|--------------|-------------|
| [id] | [title] | [layer] | [Yes/No] |

### High Priority Issues

| ID | Title | Origin Layer |
|----|-------|--------------|
| [id] | [title] | [layer] |

---

## Detailed Findings

### UX Layer Findings

[Include all issues where root cause is UX]

### Code Layer Findings

[Include all issues where root cause is Code]

### Infrastructure Layer Findings

[Include all issues where root cause is Infra]

---

## Cross-Layer Analysis

### Root Cause Chains

[For issues where symptom appears in different layer than cause]

```
Issue: [title]

[UX Layer]          [Code Layer]         [Infra Layer]
     │                    │                    │
     │                    │              ┌─────┴─────┐
     │                    │              │ ROOT CAUSE│
     │              ┌─────┴─────┐        │ [detail]  │
     │              │ PROPAGATES│        └───────────┘
     │              │ [detail]  │              │
┌────┴────┐        └───────────┘              │
│ SYMPTOM │              ▲                    │
│ [detail]│◄─────────────┴────────────────────┘
└─────────┘
```

---

## Recommendations

### Critical (Must Fix)

1. **[Issue ID]:** [recommendation]
   - Layer: [origin layer]
   - Effort: [Low/Medium/High]
   - Impact: [description]

### High Priority

2. **[Issue ID]:** [recommendation]
   ...

### Medium Priority

3. **[Issue ID]:** [recommendation]
   ...

### Low Priority (Nice to Have)

4. **[Issue ID]:** [recommendation]
   ...

---

## Fix Implementation Order

Recommended order based on dependencies and impact:

1. **[Fix 1]** - [reason this should be first]
2. **[Fix 2]** - [reason, any dependencies on #1]
3. **[Fix 3]** - [reason, any dependencies]
...

---

## Appendix

### A: User Journey Walkthrough

[Step-by-step documentation of the journey attempted]

### B: API Test Results

```bash
# Commands executed and results
```

### C: Code References

| Issue | File | Line |
|-------|------|------|
| [id] | [path] | [line] |

### D: Agent Reports

[Links or summaries of individual agent reports]

- UX Evaluation: [summary]
- Technical Analysis: [summary]
- Infrastructure Audit: [summary]
- Fidelity Test: [summary] (if applicable)
```

---

## Linear Issue Template

When creating Linear issues from findings:

```markdown
## Description

**From Goal Evaluation:** [goal_id]
**Origin Layer:** [UX/Code/Infra]

### Symptom
[User-facing description of the problem]

### Root Cause
[Technical description of the underlying issue]

### Location
- File: `[path]`
- Line: [number]
- Function/Component: [name]

## Acceptance Criteria

- [ ] [Specific fix criterion 1]
- [ ] [Specific fix criterion 2]
- [ ] Goal "[goal statement]" can be completed without this issue

## Technical Notes

[Any relevant technical context]

## Related Issues

- Blocks: [issue IDs if any]
- Blocked by: [issue IDs if any]
- Related to: [issue IDs if any]
```

---

## Quick Reference: Severity Criteria

| Severity | Goal Impact | User Experience | Fix Urgency |
|----------|-------------|-----------------|-------------|
| **Critical** | Blocks goal completely | Cannot proceed | Immediate |
| **High** | Major friction, workaround needed | Frustrating | This sprint |
| **Medium** | Noticeable friction | Annoying | Next sprint |
| **Low** | Minor issue | Barely noticeable | Backlog |
