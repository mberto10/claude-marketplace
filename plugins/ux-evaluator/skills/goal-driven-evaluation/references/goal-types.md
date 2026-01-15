# Goal Type Evaluation Strategies

Detailed evaluation patterns for each goal type.

## Navigation Goals

**Pattern:** User wants to find or reach something

### Characteristics
- Primarily UX-focused
- Success = user finds target
- Minimal backend involvement
- Information architecture is key

### Evaluation Strategy

```
1. Start at entry point (homepage, dashboard, etc.)
2. Attempt to find target using only UI cues
3. Document each decision point:
   - What options are visible?
   - Which would user choose?
   - Is the path obvious?
4. Measure clicks/steps to target
5. Note confusion points
```

### Success Metrics
- **Findability**: Did user find target?
- **Efficiency**: How many steps?
- **Clarity**: Any confusion?
- **Recovery**: Could user backtrack?

### Layer Analysis
| Layer | Focus | Weight |
|-------|-------|--------|
| UX | Navigation, labels, hierarchy | 0.9 |
| Code | Routing, conditionals | 0.1 |
| AI | N/A | 0.0 |
| Infra | N/A | 0.0 |

### Common Issues
- Hidden or buried navigation
- Unclear labels
- Too many clicks required
- Dead ends with no backtrack
- Inconsistent navigation patterns

---

## Configuration Goals

**Pattern:** User wants to set something up

### Characteristics
- Full layer involvement
- Data flows through entire stack
- Fidelity is critical
- Round-trip must preserve intent

### Evaluation Strategy

```
1. UX Phase: Walk configuration flow
   - Can user find settings?
   - Are options clear?
   - Is feedback provided?

2. Code Phase: Trace data transform
   - UI value → React state
   - React state → API payload
   - Are transforms correct?

3. Infra Phase: Verify persistence
   - Does API accept payload?
   - Does database store correctly?
   - Does retrieval match storage?

4. Fidelity Test: Round-trip
   - Save configuration
   - Reload page
   - Compare before/after
```

### Success Metrics
- **Completability**: Can user configure?
- **Transform Accuracy**: Does data transform correctly?
- **Persistence**: Does data save?
- **Fidelity**: Does round-trip preserve values?

### Layer Analysis
| Layer | Focus | Weight |
|-------|-------|--------|
| UX | Forms, feedback, validation | 0.4-0.6 |
| Code | Transforms, state management | 0.2-0.3 |
| AI | N/A (usually) | 0.0 |
| Infra | Persistence, retrieval | 0.2-0.3 |

### Common Issues
- Type coercion errors
- Missing validation
- Silent failures
- Default value injection
- Nested object flattening

---

## Generation Goals

**Pattern:** User wants AI-generated output

### Characteristics
- All layers involved
- AI quality is central
- Long execution times
- Output comparison needed

### Evaluation Strategy

```
1. UX Phase: Trigger generation
   - Can user configure generation?
   - Is progress visible?
   - Is output accessible?

2. Code Phase: Verify orchestration
   - Are inputs passed correctly?
   - Is workflow triggered?
   - Is output routed correctly?

3. AI Phase: Assess quality
   - Does output match intent?
   - Are prompts effective?
   - Is quality consistent?

4. Infra Phase: Verify delivery
   - Is output stored?
   - Can output be retrieved?
   - Are external services working?
```

### Success Metrics
- **Triggerable**: Can user start generation?
- **Visibility**: Can user see progress?
- **Quality**: Is output acceptable?
- **Delivery**: Is output accessible?

### Layer Analysis
| Layer | Focus | Weight |
|-------|-------|--------|
| UX | Trigger, progress, output | 0.2-0.3 |
| Code | Orchestration, routing | 0.2-0.3 |
| AI | Quality, prompts, tools | 0.3-0.4 |
| Infra | Execution, storage | 0.1-0.2 |

### Common Issues
- Generation never completes
- Progress invisible
- Output quality poor
- Output inaccessible
- External service failures

---

## Operational Goals

**Pattern:** User wants to monitor or manage operations

### Characteristics
- Status visibility is key
- Actions must be effective
- State consistency matters
- Recovery paths needed

### Evaluation Strategy

```
1. UX Phase: Assess visibility
   - Can user see status?
   - Is state clear?
   - Are actions available?

2. Code Phase: Verify actions
   - Do actions trigger correctly?
   - Is state updated?
   - Are side effects handled?

3. Infra Phase: Verify consistency
   - Is displayed state accurate?
   - Are logs available?
   - Is state recoverable?
```

### Success Metrics
- **Visibility**: Is status clear?
- **Accuracy**: Is status accurate?
- **Actionability**: Can user take action?
- **Effectiveness**: Do actions work?

### Layer Analysis
| Layer | Focus | Weight |
|-------|-------|--------|
| UX | Status display, actions | 0.4 |
| Code | Action handlers, state sync | 0.3 |
| AI | N/A (unless AI-assisted) | 0.0 |
| Infra | State, logs, recovery | 0.3 |

### Common Issues
- Stale status display
- Actions don't work
- State inconsistency
- Missing error details
- No recovery path

---

## Recovery Goals

**Pattern:** User wants to fix something that went wrong

### Characteristics
- Error handling is central
- Undo/revert needed
- Clear guidance required
- State must be recoverable

### Evaluation Strategy

```
1. UX Phase: Assess error handling
   - Are errors visible?
   - Are messages clear?
   - Is recovery path obvious?
   - Can user undo?

2. Code Phase: Verify recovery logic
   - Is state recoverable?
   - Are undo handlers implemented?
   - Is error state clearable?
```

### Success Metrics
- **Visibility**: Is error shown?
- **Clarity**: Is cause explained?
- **Recoverability**: Can user fix it?
- **Prevention**: Can user avoid repeat?

### Layer Analysis
| Layer | Focus | Weight |
|-------|-------|--------|
| UX | Error messages, undo UI | 0.5-0.6 |
| Code | Error handling, state recovery | 0.3-0.4 |
| AI | N/A | 0.0 |
| Infra | State consistency | 0.0-0.1 |

### Common Issues
- Silent failures
- Cryptic error messages
- No undo capability
- Unrecoverable state
- Lost user data

---

## Goal Type Selection Guide

When analyzing a user statement, classify using these patterns:

| User Says | Goal Type |
|-----------|-----------|
| "find", "where is", "navigate to" | Navigation |
| "set up", "configure", "change settings" | Configuration |
| "generate", "create content", "produce" | Generation |
| "check status", "monitor", "manage" | Operational |
| "fix", "undo", "recover", "revert" | Recovery |

When unclear, default to **Configuration** as it covers the most layers and provides comprehensive analysis.
