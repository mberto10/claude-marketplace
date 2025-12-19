---
description: Create or update your personal writing style guide interactively
argument-hint: [sample-file-path]
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion
---

Create or update the user's personal writing style guide.

## Process

### Step 1: Check Existing Configuration

Look for `.claude/writing-studio.local.md`:
- If exists, read current configuration and ask if user wants to update or start fresh
- If not exists, proceed with initial setup

### Step 2: Style Source Selection

Ask the user how they want to define their style:

```
═══════════════════════════════════════════
📍 CHECKPOINT: Style Definition Method
═══════════════════════════════════════════

How would you like to define your writing style?

**Options:**
1. **Answer Questions** - I'll guide you through style preferences interactively
2. **Analyze Sample** - Provide a writing sample and I'll extract your style
3. **Both** - Answer questions AND analyze a sample for comprehensive profile

Which approach? (1/2/3)
═══════════════════════════════════════════
```

### Step 3A: Interactive Questions (if chosen)

Ask about each style dimension using AskUserQuestion:

**Tone:**
- Formal vs. casual
- Serious vs. playful
- Authoritative vs. collaborative

**Voice:**
- First-person (I/we) vs. second-person (you) vs. third-person
- Active vs. passive preference
- Direct vs. nuanced

**Structure:**
- Sentence length preference (short, varied, long)
- Paragraph density (spacious, medium, dense)
- Use of lists, headers, formatting

**Vocabulary:**
- Technical vs. accessible language
- Words or phrases to avoid
- Preferred alternatives

### Step 3B: Sample Analysis (if chosen or if file argument provided)

If sample file path provided as argument ($ARGUMENTS), analyze that file.
Otherwise, ask user to provide a sample file path.

Before deep analysis, ask user-guided focus questions:
- "What aspects of this sample do you most want to preserve?"
- "Are there elements you want to change or avoid?"
- "Is this representative of your 'true voice'?"

Analyze based on user guidance, focusing on:
- Voice markers and personality signals
- Structural patterns
- Vocabulary preferences
- Rhythm and flow

Present findings with checkpoint for confirmation.

### Step 4: Generate Style Guide

Create `.claude/writing-studio.local.md` with:

```markdown
---
# Core Style Elements
tone: [derived preference]
voice: [derived preference]
formality: [low/medium/high]

# Structural Preferences
sentence_length: [derived preference]
paragraph_style: [derived preference]

# Vocabulary Rules
prohibited_words:
  - [word1]
  - [word2]

vocabulary_preferences:
  - "[preference 1]"
  - "[preference 2]"

# Type-Specific Overrides (optional)
writing_types:
  technical:
    notes: "[specific notes]"
  creative:
    notes: "[specific notes]"
---

## Example Excerpts

[Include user's sample excerpts with annotations]

## Style Notes

[Additional preferences and context]
```

### Step 5: Confirmation

Present the generated style guide and ask for approval:
- Show summary of key preferences
- Explain how it will be used
- Offer to adjust any elements
- Save when user confirms

## If No Arguments

If `/setup-style` is called without arguments and user chooses sample analysis:
1. Ask for file path to analyze
2. Use Glob to help find files if user is unsure
3. Read and analyze the specified file

## Output

After completion:
- Confirm the style guide was saved
- Explain how to use it: "Your style guide is now active. Use `/write` to start writing with your style applied."
- Mention they can run `/setup-style` again to update preferences
