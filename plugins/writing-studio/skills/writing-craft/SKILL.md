---
name: Writing Craft
description: This skill should be used when the user asks to "write something", "help me write", "draft content", "edit my writing", "brainstorm ideas", "create an outline", "setup my style", "analyze my writing style", or needs guidance on maintaining consistent voice and style across writing tasks. Provides comprehensive writing workflow and style management guidance.
version: 1.0.0
---

# Writing Craft

Core knowledge for the Writing Studio plugin, providing guidance on style management, writing workflows, and interactive checkpoint communication.

## Style Guide System

### Loading User Style

Before any writing task, load the user's style configuration:

1. Check for `.claude/writing-studio.local.md` in the project root
2. Parse YAML frontmatter for structured preferences
3. Read markdown body for examples and contextual notes
4. If no style file exists, suggest running `/setup-style`

### Style File Structure

```yaml
---
tone: [conversational, formal, technical, casual, authoritative]
voice: [first-person singular, first-person plural, second-person, third-person]
formality: [low, medium, high]
sentence_length: [short, varied, long]
paragraph_style: [dense, spacious, mixed]
prohibited_words:
  - word1
  - word2
vocabulary_preferences:
  - "prefer X over Y"
writing_types:
  technical:
    tone_override: technical
    notes: "specific notes for technical writing"
  creative:
    tone_override: conversational
    notes: "specific notes for creative writing"
---

## Example Excerpts

[User's writing samples with annotations]

## Style Notes

[Detailed preferences and context]
```

### Applying Style Consistently

When drafting or editing:
- Match sentence rhythm patterns from examples
- Use vocabulary from the approved list
- Avoid prohibited words and phrases
- Maintain consistent voice throughout
- Adapt tone based on writing type if specified

## Checkpoint Communication Pattern

All writing agents use structured checkpoints for interactive collaboration.

### Checkpoint Format

```
═══════════════════════════════════════════
📍 CHECKPOINT: [Checkpoint Name]
═══════════════════════════════════════════

[Context or summary of current state]

**Options:**
1. [Option A] - [Brief description]
2. [Option B] - [Brief description]
3. [Option C] - [Brief description]

Which direction? (1/2/3) Or describe your preference.
═══════════════════════════════════════════
```

### When to Create Checkpoints

- After generating multiple viable directions
- Before committing to a structural decision
- When user preferences could significantly alter approach
- At transition points between workflow stages
- When encountering ambiguity in requirements

### Checkpoint Best Practices

- Limit to 3-4 options to avoid decision paralysis
- Make options meaningfully different
- Include brief rationale for each option
- Allow free-form response as alternative
- Keep checkpoint titles descriptive but concise

## Writing Workflow Stages

### Stage 1: Brainstorming

**Purpose**: Generate and explore ideas without judgment

**Process**:
1. Clarify the topic and intended audience
2. Generate diverse angles and approaches
3. Ask probing questions to uncover hidden aspects
4. Present ideas with checkpoint for direction selection

**Key Questions**:
- What is the core message or purpose?
- Who is the intended audience?
- What makes this unique or interesting?
- What angles haven't been explored?

### Stage 2: Planning

**Purpose**: Create structured outline from selected direction

**Process**:
1. Define the main thesis or central argument
2. Identify key sections and their purposes
3. Determine logical flow and transitions
4. Create detailed outline with checkpoint for structure approval

**Outline Format**:
```
# [Title]

## Opening Hook
- [Hook approach]
- [Bridge to main content]

## Section 1: [Name]
- Key point A
- Key point B
- Transition to next section

## Section 2: [Name]
...

## Conclusion
- [Summary approach]
- [Call to action or final thought]
```

### Stage 3: Drafting

**Purpose**: Write content following style guide and approved outline

**Process**:
1. Load and internalize user's style preferences
2. Follow outline structure precisely
3. Maintain consistent voice and tone
4. Create checkpoint after completing each major section

**Drafting Principles**:
- Lead with the strongest content
- Use concrete examples over abstractions
- Vary sentence structure for rhythm
- Connect sections with smooth transitions

### Stage 4: Editing

**Purpose**: Refine and polish draft to match style exactly

**Process**:
1. Check consistency with style guide
2. Identify and fix prohibited words
3. Improve clarity and flow
4. Present changes with checkpoint for approval

**Editing Checklist**:
- [ ] Voice consistency throughout
- [ ] No prohibited words or phrases
- [ ] Sentence variety matches preference
- [ ] Tone appropriate for writing type
- [ ] Transitions smooth between sections
- [ ] Opening hook effective
- [ ] Conclusion satisfying

## Style Analysis (User-Guided)

When analyzing user's sample documents:

### Initial Questions

Before deep analysis, ask:
- What aspects of this sample do you most want to preserve?
- Are there elements in this sample you want to change?
- What makes this sample representative of your style?

### Analysis Categories

Based on user guidance, analyze:

**Structural Patterns**:
- Paragraph length and density
- Section organization
- Opening/closing patterns
- Use of lists, headers, quotes

**Voice Markers**:
- Pronoun usage (I, we, you, one)
- Level of formality
- Attitude and personality
- Directness vs. hedge language

**Vocabulary Patterns**:
- Common phrases and expressions
- Technical vs. accessible language
- Preferred synonyms
- Sentence starters

**Rhythm and Flow**:
- Sentence length variation
- Punctuation patterns
- Transition words
- Paragraph transitions

### Presenting Analysis

After user-guided analysis:
1. Summarize key findings
2. Ask user to confirm or adjust observations
3. Create checkpoint for which elements to codify in style guide

## Writing Type Adaptations

### Technical Writing

- Prioritize clarity over creativity
- Use precise, unambiguous language
- Include code examples where relevant
- Maintain consistent terminology
- Structure with clear headers and sections

### Creative Writing

- Allow more voice and personality
- Use vivid, sensory language
- Vary rhythm more dramatically
- Include hooks and narrative elements
- Balance showing vs. telling

### Business/Professional

- Lead with key information
- Keep paragraphs focused
- Use action-oriented language
- Maintain professional tone
- Include clear next steps or asks

## Additional Resources

### Reference Files

For detailed guidance, consult:
- **`references/checkpoint-examples.md`** - Complete checkpoint examples for each workflow stage
- **`references/style-analysis-guide.md`** - Detailed style analysis methodology

### Example Files

Working examples in `examples/`:
- **`example-style-guide.md`** - Complete style guide template with annotations
