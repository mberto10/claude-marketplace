# Layer-Specific Analysis Patterns

Detailed patterns for analyzing each system layer.

## UX Layer

**Agent:** ux-evaluator
**Focus:** User interface, interactions, feedback, friction

### Analysis Checklist

- [ ] **Discoverability** - Can user find the feature/action?
- [ ] **Clarity** - Are labels and instructions clear?
- [ ] **Feedback** - Does UI respond to user actions?
- [ ] **Efficiency** - How many steps to complete goal?
- [ ] **Error Handling** - Are errors visible and helpful?
- [ ] **Recovery** - Can user undo or backtrack?
- [ ] **Accessibility** - Is UI keyboard/screen-reader accessible?

### Evaluation Pattern

```
1. Navigate to starting point
2. Take accessibility snapshot
3. Identify primary action for goal
4. Execute action via browser
5. Observe response:
   - Did UI update?
   - Was feedback provided?
   - Any errors shown?
6. Continue until goal complete or blocked
7. Document each friction point
```

### Playwright Tools Used

| Tool | Purpose |
|------|---------|
| `browser_snapshot` | Capture semantic structure |
| `browser_click` | Test interactions |
| `browser_type` | Test input handling |
| `browser_fill_form` | Test form flows |
| `browser_wait_for` | Handle async operations |
| `browser_console_messages` | Check for JS errors |

### Output Format

```markdown
### UX Finding: [title]

**Location:** [URL or element path]
**Severity:** [Critical/High/Medium/Low]

**Observation:**
[What was observed during user journey]

**Expected:**
[What should happen for good UX]

**Screenshot:** [if applicable]

**Recommendation:**
[Specific UI/UX fix]
```

---

## Code Layer

**Agent:** technical-debugger
**Focus:** Logic, transforms, handlers, state management

### Analysis Checklist

- [ ] **Handler Exists** - Is there code for this action?
- [ ] **Transform Correct** - Does data transform properly?
- [ ] **State Management** - Is state updated correctly?
- [ ] **Error Handling** - Are errors caught and handled?
- [ ] **Edge Cases** - Are boundary conditions handled?
- [ ] **Type Safety** - Are types correct throughout?

### Evaluation Pattern

```
1. Identify entry point (component, handler)
2. Trace data flow:
   - UI event → handler
   - Handler → state update
   - State → API call
3. Check each transform:
   - Input shape → Output shape
   - Any data loss?
   - Type coercion?
4. Verify error paths:
   - Try/catch present?
   - Error propagated to UI?
5. Document issues with file:line references
```

### Code Search Tools

| Tool | Purpose |
|------|---------|
| `Grep` | Find function/handler definitions |
| `Read` | Examine implementation |
| `Glob` | Find related files |

### Output Format

```markdown
### Code Finding: [title]

**File:** [path:line]
**Severity:** [Critical/High/Medium/Low]

**Code:**
```typescript
// Relevant code snippet
```

**Issue:**
[What's wrong with the code]

**Fix:**
```typescript
// Suggested fix
```

**Impact:**
[How this affects user goal]
```

---

## AI Layer

**Agent:** ai-trace-analyst (when available)
**Focus:** LLM calls, prompts, tool usage, output quality

### Analysis Checklist

- [ ] **Prompt Quality** - Is prompt clear and effective?
- [ ] **Tool Selection** - Are right tools being used?
- [ ] **Output Quality** - Does output meet requirements?
- [ ] **Consistency** - Is quality consistent across runs?
- [ ] **Error Recovery** - How are LLM errors handled?
- [ ] **Cost Efficiency** - Is token usage reasonable?

### Evaluation Pattern

```
1. Identify AI touchpoints in goal flow
2. Capture prompts sent to LLM
3. Analyze tool calls:
   - Were appropriate tools selected?
   - Were tool outputs used correctly?
4. Assess output quality:
   - Does it match user intent?
   - Is it factually accurate?
   - Does it meet quality criteria?
5. Check traces (Langfuse if available)
```

### Output Format

```markdown
### AI Finding: [title]

**Component:** [research/write/edit/etc.]
**Severity:** [Critical/High/Medium/Low]

**Prompt Analysis:**
[Assessment of prompt effectiveness]

**Output Quality:**
[Assessment against criteria]

**Trace Reference:** [Langfuse trace ID if available]

**Recommendation:**
[Prompt improvement, tool adjustment, etc.]
```

---

## Infrastructure Layer

**Agent:** infrastructure-auditor
**Focus:** Database, APIs, external services, persistence

### Analysis Checklist

- [ ] **Endpoint Exists** - Does required API exist?
- [ ] **Endpoint Works** - Does it return correct data?
- [ ] **Persistence** - Is data saved correctly?
- [ ] **Retrieval** - Is data retrieved correctly?
- [ ] **External Services** - Are dependencies healthy?
- [ ] **Error Handling** - Are infra errors handled?

### Evaluation Pattern

```
1. Identify required API endpoints
2. Test each endpoint:
   - Does it exist? (not 404)
   - Does it accept expected payload?
   - Does it return expected response?
3. Verify database state:
   - Was data written?
   - Can data be read back?
   - Is data correct?
4. Check external service health
5. Test error scenarios:
   - What if service is down?
   - What if request fails?
```

### API Testing Commands

```bash
# Test endpoint exists
curl -I http://localhost:8000/api/endpoint

# Test POST
curl -X POST http://localhost:8000/api/endpoint \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'

# Test GET
curl http://localhost:8000/api/endpoint/{id}
```

### Output Format

```markdown
### Infrastructure Finding: [title]

**Endpoint:** [method] [path]
**Severity:** [Critical/High/Medium/Low]

**Test:**
```bash
# Command executed
```

**Expected:**
[Expected response]

**Actual:**
[Actual response]

**Root Cause:**
[Why this failed - missing migration, misconfiguration, etc.]

**Fix:**
[Specific infrastructure fix]
```

---

## Cross-Layer Correlation

When findings exist in multiple layers, determine the root cause:

### Correlation Pattern

```
SYMPTOM in Layer A
    ↓
Trace backward through data flow
    ↓
Find ORIGIN in Layer B
    ↓
Report as: "Symptom in A, Root Cause in B"
```

### Example

```
Symptom (UX): Save button shows success but data lost on reload
    ↓
Trace: UI calls API → API returns 500 → UI ignores error
    ↓
Root Cause Analysis:
  - UX: Error not displayed (contributing factor)
  - Code: Error not propagated (contributing factor)
  - Infra: Database table missing (ROOT CAUSE)
    ↓
Report: "Root cause is Infrastructure (missing migration),
         manifests in UX (no error feedback)"
```

### Priority Assignment

Based on root cause layer:

| Root Cause Layer | Typical Priority | Reasoning |
|------------------|------------------|-----------|
| Infra | Critical | Blocks all functionality |
| Code | High | Incorrect behavior |
| UX | Medium | Friction but functional |
| AI | Varies | Depends on quality impact |
