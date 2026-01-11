---
name: langfuse-prompt-management
description: Use when the user wants to list, fetch, create, update, compare, or promote Langfuse prompts, including versioning and deployment labels.
---

# Langfuse Prompt Management

Manage prompt versions and labels in Langfuse.

## Quick Start

```bash
python3 ~/.codex/skills/langfuse-prompt-management/scripts/prompt_manager.py list
```

## Common Tasks

### Get Prompt

```bash
python3 ~/.codex/skills/langfuse-prompt-management/scripts/prompt_manager.py \
  get --name "my-prompt" --label production
```

### Create Prompt

```bash
python3 ~/.codex/skills/langfuse-prompt-management/scripts/prompt_manager.py \
  create --name "summarizer" --type text --prompt "Summarize: {{content}}"
```

### Update Prompt

```bash
python3 ~/.codex/skills/langfuse-prompt-management/scripts/prompt_manager.py \
  update --name "summarizer" --prompt "Provide a concise summary: {{content}}"
```

### Promote Version

```bash
python3 ~/.codex/skills/langfuse-prompt-management/scripts/prompt_manager.py \
  promote --name "summarizer" --version 3 --label production
```

### Compare Versions

```bash
python3 ~/.codex/skills/langfuse-prompt-management/scripts/prompt_manager.py \
  compare --name "summarizer" --v1 2 --v2 3
```

## Environment

```bash
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```
