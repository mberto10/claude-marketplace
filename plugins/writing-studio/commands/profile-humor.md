---
name: profile-humor
description: Analyze comedy material to create a comprehensive humor profile for content generation
arguments:
  - name: samples
    description: Path to comedy samples, transcripts, or comedian name to search
    required: false
---

# Profile Humor Command

Analyze comedy material to create a detailed humor profile for generating speeches, roasts, or entertainment content.

## Usage

```
/profile-humor                    # Start interactive
/profile-humor @transcript.txt    # Analyze file
/profile-humor "comedian name"    # Search online
```

## Process

1. Ingests comedy samples
2. Analyzes 12 comedy-specific dimensions
3. Extracts comedic DNA
4. Produces structured profile with generation instructions

## Dimensions Analyzed

- Comedy Persona & Worldview
- Humor Mechanics (setup/punchline)
- Comedy Types & Modes
- Target Selection
- Delivery Style
- Timing Patterns
- Callback & Layering
- Audience Relationship
- Taboo Navigation
- Sincerity Balance
- Vocabulary & Language
- Signature Bits

## Output

Profile saved to `profiles/[name]-humor.md` with:
- Complete dimensional analysis
- Joke construction templates
- Replication instructions
- Anti-patterns to avoid
- Context adaptation notes

## See Also

- `/profile-writer` - For prose/writing style profiles
- `/draft` - Generate content using a profile
