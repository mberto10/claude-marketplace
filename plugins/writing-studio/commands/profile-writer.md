---
description: Analyze writing samples to create a comprehensive writer profile
argument-hint: <file-path or folder-path>
allowed-tools: Read, Write, Glob, Grep, AskUserQuestion
---

Create a comprehensive writer profile by analyzing the provided writing samples.

## Input Handling

If argument is provided ($ARGUMENTS):
1. Check if it's a file path → analyze that single file
2. Check if it's a folder path → find all .md, .txt files in that folder
3. If glob pattern (e.g., "*.md") → find matching files

If no argument provided:
1. Ask user to provide file paths or folder
2. Use Glob to help locate writing samples

## Analysis Process

Follow the Writer Profiler skill methodology:

### Phase 1: Sample Ingestion
- Read all provided samples
- Calculate total word count
- Identify sample types and contexts
- Present sample assessment checkpoint

### Phase 2: Analysis Focus
Ask the user:
```
═══════════════════════════════════════════
📍 CHECKPOINT: Analysis Scope
═══════════════════════════════════════════

I found [N] samples totaling [X] words.

**Sample breakdown:**
- [List sample types found]

**Analysis options:**
1. **Full Profile** - Comprehensive 12-dimension analysis (recommended for 3+ samples)
2. **Quick Profile** - Core dimensions only (voice, tone, vocabulary, rhythm)
3. **Focused Analysis** - Choose specific dimensions to analyze

Which approach? (1/2/3)
═══════════════════════════════════════════
```

### Phase 3: Dimensional Analysis

Analyze each relevant dimension following the methodology in the writer-profiler skill.

For each dimension:
- Extract patterns from samples
- Note specific examples
- Calculate confidence based on consistency
- Document variations

### Phase 4: Profile Synthesis

Generate the complete writer profile in the standard format:
- YAML frontmatter with metadata
- All analyzed dimensions
- Writing Assistant Configuration section
- Specific examples from the samples

### Phase 5: Profile Delivery

Present the profile and ask:
```
═══════════════════════════════════════════
📍 CHECKPOINT: Profile Complete
═══════════════════════════════════════════

Analysis complete. Confidence score: [X]/100

**Key findings:**
- Voice: [summary]
- Tone: [summary]
- Distinctive features: [list]

**Options:**
1. **Save profile** - Write to `.claude/writer-profile.md`
2. **Review findings** - Walk through each dimension
3. **Refine analysis** - Focus on specific areas
4. **Convert to style guide** - Create writing-studio compatible style guide

How would you like to proceed? (1/2/3/4)
═══════════════════════════════════════════
```

## Output Options

### Save Profile
Write complete profile to `.claude/writer-profile.md`

### Convert to Style Guide
Transform profile into `.claude/writing-studio.local.md` format for use with other writing-studio commands.

## Key Principles

- Show examples from actual samples for every observation
- Be specific and actionable, not vague
- Note confidence levels for each dimension
- Distinguish consistent patterns from variations
- Create profiles that enable genuine voice replication
