---
name: langfuse-prompt-management
description: This skill should be used when the user asks to "list prompts", "get prompt", "create prompt", "update prompt", "promote prompt to production", "compare prompt versions", or needs to manage Langfuse prompts including versioning and deployment labels.
---

# Langfuse Prompt Management

Full CRUD operations for Langfuse prompts with version control and deployment labels.

## When to Use

- Listing all prompts in a project
- Fetching a specific prompt by name, version, or label
- Creating new prompts (text or chat type)
- Updating prompts (creates new version)
- Promoting prompt versions to production/staging
- Comparing prompt versions to see differences

## Operations

### List All Prompts

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py list
```

Output shows all prompts with their latest version and production status.

### Get Prompt

```bash
# Get production version (default)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  get --name "my-prompt"

# Get specific version
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  get --name "my-prompt" --version 3

# Get by label
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  get --name "my-prompt" --label staging

# Get latest version
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  get --name "my-prompt" --label latest
```

### Create Prompt

**Text Prompt:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  create \
  --name "summarizer" \
  --type text \
  --prompt "Summarize the following content: {{content}}"
```

**Chat Prompt:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  create \
  --name "assistant" \
  --type chat \
  --prompt '[{"role": "system", "content": "You are a helpful assistant"}, {"role": "user", "content": "{{question}}"}]'
```

**With Config and Labels:**
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  create \
  --name "summarizer" \
  --type text \
  --prompt "Summarize: {{content}}" \
  --config '{"model": "gpt-4o", "temperature": 0.7}' \
  --labels production staging
```

### Update Prompt (New Version)

```bash
# Update prompt text (creates new version)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  update \
  --name "summarizer" \
  --prompt "Please provide a concise summary of: {{content}}"

# Update with commit message
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  update \
  --name "summarizer" \
  --prompt "Please provide a concise summary of: {{content}}" \
  --commit-message "Improved clarity of instructions"

# Update config
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  update \
  --name "summarizer" \
  --config '{"model": "gpt-4o-mini", "temperature": 0.5}'
```

### Promote Version

```bash
# Promote version 5 to production
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  promote --name "summarizer" --version 5 --label production

# Add multiple labels
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  promote --name "summarizer" --version 5 --labels production stable
```

### Compare Versions

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  compare --name "summarizer" --v1 3 --v2 5
```

Shows diff-style output of changes between versions.

## Prompt Types

### Text Prompts

Simple string templates with `{{variable}}` placeholders:

```
Summarize the following content in {{style}} style:

{{content}}

Focus on: {{focus_areas}}
```

### Chat Prompts

JSON array of messages with role and content:

```json
[
  {"role": "system", "content": "You are an expert {{domain}} assistant"},
  {"role": "user", "content": "{{question}}"}
]
```

## Labels and Versioning

- **`latest`** - Automatically points to most recent version
- **`production`** - Default label fetched when no label specified
- **`staging`** - Common label for testing before production
- **Custom labels** - Create any labels for your workflow

**Deployment flow:**
1. Create/update prompt (new version created)
2. Test with `--label latest`
3. Promote to `staging` for team review
4. Promote to `production` for live use

## Config Object

Store model parameters and metadata:

```json
{
  "model": "gpt-4o",
  "temperature": 0.7,
  "max_tokens": 1000,
  "custom_field": "any value"
}
```

Access in your application after fetching prompt.

## Required Environment Variables

```bash
LANGFUSE_PUBLIC_KEY=pk-...    # Required
LANGFUSE_SECRET_KEY=sk-...    # Required
LANGFUSE_HOST=https://cloud.langfuse.com  # Optional
```

## Common Workflows

### Workflow 1: Create and Deploy New Prompt

```bash
# 1. Create prompt
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  create --name "qa-bot" --type chat \
  --prompt '[{"role": "system", "content": "Answer questions accurately"}, {"role": "user", "content": "{{question}}"}]'

# 2. Test the prompt (version 1)
# ... test in your application with --label latest ...

# 3. Promote to production
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  promote --name "qa-bot" --version 1 --label production
```

### Workflow 2: Iterate and Compare

```bash
# 1. Update prompt with improvement
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  update --name "qa-bot" \
  --prompt '[{"role": "system", "content": "Answer questions accurately and concisely"}, {"role": "user", "content": "{{question}}"}]' \
  --commit-message "Added conciseness requirement"

# 2. Compare with production version
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  compare --name "qa-bot" --v1 1 --v2 2

# 3. If satisfied, promote new version
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  promote --name "qa-bot" --version 2 --label production
```

### Workflow 3: Rollback

```bash
# Promote previous version back to production
python3 ${CLAUDE_PLUGIN_ROOT}/skills/prompt-management/helpers/prompt_manager.py \
  promote --name "qa-bot" --version 1 --label production
```

## Troubleshooting

**Prompt not found:**
- Verify prompt name is correct (case-sensitive)
- Check if version/label exists

**Version already has label:**
- Labels can be reassigned - the old version will lose the label

**Invalid JSON for chat prompt:**
- Ensure proper JSON array format
- Escape quotes if needed in shell
