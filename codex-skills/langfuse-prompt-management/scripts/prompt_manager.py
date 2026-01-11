#!/usr/bin/env python3
"""
Langfuse Prompt Manager

Full CRUD operations for Langfuse prompts with version control and deployment labels.

USAGE:
    python prompt_manager.py list
    python prompt_manager.py get --name "my-prompt"
    python prompt_manager.py create --name "new-prompt" --type text --prompt "..."
    python prompt_manager.py update --name "my-prompt" --prompt "..."
    python prompt_manager.py promote --name "my-prompt" --version 5 --label production
    python prompt_manager.py compare --name "my-prompt" --v1 3 --v2 5
"""

import argparse
import json
import sys
from typing import Optional, List, Dict, Any
from difflib import unified_diff

from langfuse_client import get_langfuse_client


def list_prompts() -> List[Dict[str, Any]]:
    """List all prompts in the project."""
    client = get_langfuse_client()

    try:
        # Use the API to list prompts
        response = client.api.prompts.list()
        prompts = []

        if hasattr(response, 'data'):
            for prompt in response.data:
                prompt_dict = prompt.dict() if hasattr(prompt, 'dict') else dict(prompt)
                prompts.append(prompt_dict)

        return prompts
    except Exception as e:
        print(f"Error listing prompts: {e}", file=sys.stderr)
        return []


def get_prompt(
    name: str,
    version: Optional[int] = None,
    label: Optional[str] = None,
    prompt_type: str = "text"
) -> Optional[Dict[str, Any]]:
    """Get a specific prompt by name, version, or label."""
    client = get_langfuse_client()

    try:
        kwargs = {"type": prompt_type}
        if version is not None:
            kwargs["version"] = version
        elif label is not None:
            kwargs["label"] = label

        prompt = client.get_prompt(name, **kwargs)

        if prompt:
            return {
                "name": prompt.name,
                "version": prompt.version,
                "prompt": prompt.prompt,
                "config": prompt.config if hasattr(prompt, 'config') else {},
                "labels": prompt.labels if hasattr(prompt, 'labels') else [],
                "type": prompt_type,
            }
        return None
    except Exception as e:
        print(f"Error getting prompt '{name}': {e}", file=sys.stderr)
        return None


def create_prompt(
    name: str,
    prompt_type: str,
    prompt: str,
    config: Optional[Dict[str, Any]] = None,
    labels: Optional[List[str]] = None
) -> Optional[Dict[str, Any]]:
    """Create a new prompt."""
    client = get_langfuse_client()

    try:
        # Parse prompt for chat type
        if prompt_type == "chat":
            try:
                prompt_content = json.loads(prompt)
            except json.JSONDecodeError as e:
                print(f"Error parsing chat prompt JSON: {e}", file=sys.stderr)
                return None
        else:
            prompt_content = prompt

        result = client.create_prompt(
            name=name,
            type=prompt_type,
            prompt=prompt_content,
            config=config or {},
            labels=labels or []
        )

        if result:
            return {
                "name": name,
                "version": result.version if hasattr(result, 'version') else 1,
                "type": prompt_type,
                "labels": labels or [],
                "status": "created"
            }
        return None
    except Exception as e:
        print(f"Error creating prompt '{name}': {e}", file=sys.stderr)
        return None


def update_prompt(
    name: str,
    prompt: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None,
    commit_message: Optional[str] = None,
    prompt_type: str = "text"
) -> Optional[Dict[str, Any]]:
    """Update a prompt (creates new version)."""
    client = get_langfuse_client()

    try:
        # Get current prompt to preserve values
        current = get_prompt(name, label="latest", prompt_type=prompt_type)
        if not current:
            print(f"Prompt '{name}' not found", file=sys.stderr)
            return None

        # Parse prompt for chat type
        if prompt:
            if prompt_type == "chat":
                try:
                    prompt_content = json.loads(prompt)
                except json.JSONDecodeError as e:
                    print(f"Error parsing chat prompt JSON: {e}", file=sys.stderr)
                    return None
            else:
                prompt_content = prompt
        else:
            prompt_content = current["prompt"]

        # Merge config
        new_config = current.get("config", {})
        if config:
            new_config.update(config)

        kwargs = {
            "name": name,
            "type": prompt_type,
            "prompt": prompt_content,
            "config": new_config,
        }

        if commit_message:
            kwargs["commit_message"] = commit_message

        result = client.create_prompt(**kwargs)

        if result:
            return {
                "name": name,
                "version": result.version if hasattr(result, 'version') else current["version"] + 1,
                "type": prompt_type,
                "status": "updated"
            }
        return None
    except Exception as e:
        print(f"Error updating prompt '{name}': {e}", file=sys.stderr)
        return None


def promote_prompt(
    name: str,
    version: int,
    labels: List[str]
) -> Optional[Dict[str, Any]]:
    """Promote a prompt version by adding labels to it."""
    client = get_langfuse_client()

    try:
        client.update_prompt(
            name=name,
            version=version,
            new_labels=labels
        )

        return {
            "name": name,
            "version": version,
            "labels": labels,
            "status": "promoted"
        }
    except Exception as e:
        print(f"Error promoting prompt '{name}' version {version}: {e}", file=sys.stderr)
        return None


def compare_prompts(name: str, v1: int, v2: int, prompt_type: str = "text") -> str:
    """Compare two versions of a prompt and return diff."""
    p1 = get_prompt(name, version=v1, prompt_type=prompt_type)
    p2 = get_prompt(name, version=v2, prompt_type=prompt_type)

    if not p1:
        return f"Error: Version {v1} not found"
    if not p2:
        return f"Error: Version {v2} not found"

    # Format prompts for diff
    if prompt_type == "chat":
        text1 = json.dumps(p1["prompt"], indent=2).splitlines(keepends=True)
        text2 = json.dumps(p2["prompt"], indent=2).splitlines(keepends=True)
    else:
        text1 = p1["prompt"].splitlines(keepends=True)
        text2 = p2["prompt"].splitlines(keepends=True)

    diff = list(unified_diff(
        text1,
        text2,
        fromfile=f"{name} (v{v1})",
        tofile=f"{name} (v{v2})",
        lineterm=""
    ))

    if not diff:
        return "No differences in prompt text"

    result = "\n".join(diff)

    # Also compare configs if they differ
    if p1.get("config") != p2.get("config"):
        result += "\n\n## Config Changes\n"
        config1 = json.dumps(p1.get("config", {}), indent=2).splitlines(keepends=True)
        config2 = json.dumps(p2.get("config", {}), indent=2).splitlines(keepends=True)
        config_diff = list(unified_diff(config1, config2, fromfile="config v" + str(v1), tofile="config v" + str(v2)))
        result += "\n".join(config_diff)

    return result


def format_prompt_list(prompts: List[Dict[str, Any]]) -> str:
    """Format prompt list for display."""
    if not prompts:
        return "No prompts found"

    lines = ["# Prompts\n"]
    lines.append("| Name | Type | Latest Version | Labels |")
    lines.append("|------|------|----------------|--------|")

    for p in prompts:
        name = p.get("name", "?")
        ptype = p.get("type", "text")
        version = p.get("version", "?")
        labels = ", ".join(p.get("labels", [])) or "-"
        lines.append(f"| {name} | {ptype} | {version} | {labels} |")

    return "\n".join(lines)


def format_prompt_detail(prompt: Dict[str, Any]) -> str:
    """Format single prompt for display."""
    if not prompt:
        return "Prompt not found"

    lines = [f"# Prompt: {prompt['name']}\n"]
    lines.append(f"**Version:** {prompt.get('version', '?')}")
    lines.append(f"**Type:** {prompt.get('type', 'text')}")

    labels = prompt.get('labels', [])
    if labels:
        lines.append(f"**Labels:** {', '.join(labels)}")

    lines.append("\n## Prompt Content\n")

    if prompt.get('type') == 'chat':
        lines.append("```json")
        lines.append(json.dumps(prompt['prompt'], indent=2))
        lines.append("```")
    else:
        lines.append("```")
        lines.append(prompt['prompt'])
        lines.append("```")

    if prompt.get('config'):
        lines.append("\n## Config\n")
        lines.append("```json")
        lines.append(json.dumps(prompt['config'], indent=2))
        lines.append("```")

    return "\n".join(lines)


def format_result(result: Dict[str, Any], action: str) -> str:
    """Format action result for display."""
    if not result:
        return f"Failed to {action}"

    status = result.get('status', 'completed')
    name = result.get('name', '?')
    version = result.get('version', '?')

    msg = f"Prompt '{name}' {status}"
    if version:
        msg += f" (version {version})"

    labels = result.get('labels', [])
    if labels:
        msg += f" with labels: {', '.join(labels)}"

    return msg


def main():
    parser = argparse.ArgumentParser(
        description="Langfuse Prompt Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # List command
    subparsers.add_parser("list", help="List all prompts")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get a prompt")
    get_parser.add_argument("--name", required=True, help="Prompt name")
    get_parser.add_argument("--version", type=int, help="Specific version number")
    get_parser.add_argument("--label", help="Label (e.g., production, staging, latest)")
    get_parser.add_argument("--type", dest="prompt_type", default="text",
                           choices=["text", "chat"], help="Prompt type")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new prompt")
    create_parser.add_argument("--name", required=True, help="Prompt name")
    create_parser.add_argument("--type", dest="prompt_type", required=True,
                              choices=["text", "chat"], help="Prompt type")
    create_parser.add_argument("--prompt", required=True,
                              help="Prompt text (or JSON for chat)")
    create_parser.add_argument("--config", help="Config JSON object")
    create_parser.add_argument("--labels", nargs="+", help="Labels to assign")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a prompt (creates new version)")
    update_parser.add_argument("--name", required=True, help="Prompt name")
    update_parser.add_argument("--prompt", help="New prompt text (or JSON for chat)")
    update_parser.add_argument("--config", help="Config JSON to merge")
    update_parser.add_argument("--commit-message", help="Commit message for version")
    update_parser.add_argument("--type", dest="prompt_type", default="text",
                              choices=["text", "chat"], help="Prompt type")

    # Promote command
    promote_parser = subparsers.add_parser("promote", help="Promote a version with labels")
    promote_parser.add_argument("--name", required=True, help="Prompt name")
    promote_parser.add_argument("--version", type=int, required=True, help="Version to promote")
    promote_parser.add_argument("--label", help="Single label to assign")
    promote_parser.add_argument("--labels", nargs="+", help="Multiple labels to assign")

    # Compare command
    compare_parser = subparsers.add_parser("compare", help="Compare two versions")
    compare_parser.add_argument("--name", required=True, help="Prompt name")
    compare_parser.add_argument("--v1", type=int, required=True, help="First version")
    compare_parser.add_argument("--v2", type=int, required=True, help="Second version")
    compare_parser.add_argument("--type", dest="prompt_type", default="text",
                               choices=["text", "chat"], help="Prompt type")

    args = parser.parse_args()

    if args.command == "list":
        prompts = list_prompts()
        print(format_prompt_list(prompts))

    elif args.command == "get":
        prompt = get_prompt(
            args.name,
            version=args.version,
            label=args.label,
            prompt_type=args.prompt_type
        )
        print(format_prompt_detail(prompt))

    elif args.command == "create":
        config = json.loads(args.config) if args.config else None
        result = create_prompt(
            args.name,
            args.prompt_type,
            args.prompt,
            config=config,
            labels=args.labels
        )
        print(format_result(result, "create"))

    elif args.command == "update":
        config = json.loads(args.config) if args.config else None
        result = update_prompt(
            args.name,
            prompt=args.prompt,
            config=config,
            commit_message=args.commit_message,
            prompt_type=args.prompt_type
        )
        print(format_result(result, "update"))

    elif args.command == "promote":
        labels = args.labels or ([args.label] if args.label else [])
        if not labels:
            print("Error: Must specify --label or --labels", file=sys.stderr)
            sys.exit(1)
        result = promote_prompt(args.name, args.version, labels)
        print(format_result(result, "promote"))

    elif args.command == "compare":
        diff = compare_prompts(args.name, args.v1, args.v2, args.prompt_type)
        print(diff)


if __name__ == "__main__":
    main()
