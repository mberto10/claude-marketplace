#!/usr/bin/env python3
"""
Langfuse Setup Validator

Validate environment configuration and test Langfuse connection.

USAGE:
    python setup_validator.py check
    python setup_validator.py test-trace
"""

import argparse
import os
import sys


def check_environment() -> dict:
    """Check if required environment variables are set."""
    results = {
        "LANGFUSE_PUBLIC_KEY": {
            "set": bool(os.getenv("LANGFUSE_PUBLIC_KEY")),
            "value_preview": os.getenv("LANGFUSE_PUBLIC_KEY", "")[:10] + "..." if os.getenv("LANGFUSE_PUBLIC_KEY") else None
        },
        "LANGFUSE_SECRET_KEY": {
            "set": bool(os.getenv("LANGFUSE_SECRET_KEY")),
            "value_preview": os.getenv("LANGFUSE_SECRET_KEY", "")[:10] + "..." if os.getenv("LANGFUSE_SECRET_KEY") else None
        },
        "LANGFUSE_HOST": {
            "set": bool(os.getenv("LANGFUSE_HOST")),
            "value": os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com (default)")
        }
    }

    return results


def check_sdk_installed() -> dict:
    """Check if Langfuse SDK is installed."""
    try:
        import langfuse
        version = getattr(langfuse, "__version__", "unknown")
        return {"installed": True, "version": version}
    except ImportError:
        return {"installed": False, "version": None}


def test_connection() -> dict:
    """Test connection to Langfuse."""
    try:
        from langfuse import Langfuse
        client = Langfuse()

        # Try to create a minimal trace
        trace = client.trace(
            name="connection-test",
            metadata={"test": True}
        )
        trace.update(output="Connection successful")

        # Flush to ensure it's sent
        client.flush()

        return {
            "success": True,
            "trace_id": trace.id,
            "message": "Successfully connected and created test trace"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to connect to Langfuse"
        }


def create_test_trace() -> dict:
    """Create a more comprehensive test trace."""
    try:
        from langfuse import Langfuse
        client = Langfuse()

        with client.start_as_current_observation(
            name="setup-validation-trace",
            input="Test input",
            metadata={"purpose": "setup validation"}
        ) as trace:

            # Create a test span
            with client.start_as_current_observation(
                as_type="span",
                name="test-span",
                input="span input"
            ) as span:
                span.update(output="span output")

            # Create a test generation (simulated)
            with client.start_as_current_observation(
                as_type="generation",
                name="test-generation",
                model="test-model",
                input=[{"role": "user", "content": "test message"}]
            ) as gen:
                gen.update(
                    output="test response",
                    usage_details={"input": 10, "output": 5}
                )

            # Add a test score
            trace.score(name="test-score", value=1.0)

            trace.update(output="Test completed successfully")

        client.flush()

        return {
            "success": True,
            "trace_id": trace.id,
            "message": "Created comprehensive test trace with span, generation, and score"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to create test trace"
        }


def format_check_results(env_results: dict, sdk_results: dict) -> str:
    """Format check results as markdown."""
    lines = ["# Langfuse Setup Check\n"]

    # SDK Status
    lines.append("## SDK Installation\n")
    if sdk_results["installed"]:
        lines.append(f"Langfuse SDK installed (version: {sdk_results['version']})")
    else:
        lines.append("Langfuse SDK NOT INSTALLED")
        lines.append("\nInstall with: `pip install langfuse`")

    # Environment Variables
    lines.append("\n## Environment Variables\n")
    lines.append("| Variable | Status | Value |")
    lines.append("|----------|--------|-------|")

    for var, info in env_results.items():
        status = "Set" if info["set"] else "NOT SET"
        value = info.get("value_preview") or info.get("value") or "-"
        lines.append(f"| {var} | {status} | {value} |")

    # Overall Status
    lines.append("\n## Status\n")
    all_required_set = env_results["LANGFUSE_PUBLIC_KEY"]["set"] and env_results["LANGFUSE_SECRET_KEY"]["set"]

    if sdk_results["installed"] and all_required_set:
        lines.append("Ready to connect to Langfuse!")
        lines.append("\nRun `python setup_validator.py test-trace` to verify connection.")
    else:
        lines.append("Setup incomplete. Please:")
        if not sdk_results["installed"]:
            lines.append("1. Install SDK: `pip install langfuse`")
        if not env_results["LANGFUSE_PUBLIC_KEY"]["set"]:
            lines.append("2. Set LANGFUSE_PUBLIC_KEY environment variable")
        if not env_results["LANGFUSE_SECRET_KEY"]["set"]:
            lines.append("3. Set LANGFUSE_SECRET_KEY environment variable")

    return "\n".join(lines)


def format_test_results(results: dict) -> str:
    """Format test results as markdown."""
    lines = ["# Langfuse Connection Test\n"]

    if results["success"]:
        lines.append("**Status:** SUCCESS")
        lines.append(f"\n**Trace ID:** `{results['trace_id']}`")
        lines.append(f"\n{results['message']}")
        lines.append("\nYou can view this trace in the Langfuse dashboard.")
    else:
        lines.append("**Status:** FAILED")
        lines.append(f"\n**Error:** {results.get('error', 'Unknown error')}")
        lines.append(f"\n{results['message']}")
        lines.append("\n## Troubleshooting")
        lines.append("1. Verify your API keys are correct")
        lines.append("2. Check if LANGFUSE_HOST is set correctly (if self-hosted)")
        lines.append("3. Ensure network access to Langfuse servers")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Langfuse Setup Validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Check command
    subparsers.add_parser("check", help="Check environment setup")

    # Test trace command
    subparsers.add_parser("test-trace", help="Create a test trace to verify connection")

    args = parser.parse_args()

    if args.command == "check":
        env_results = check_environment()
        sdk_results = check_sdk_installed()
        print(format_check_results(env_results, sdk_results))

    elif args.command == "test-trace":
        # First check environment
        env_results = check_environment()
        sdk_results = check_sdk_installed()

        if not sdk_results["installed"]:
            print("Error: Langfuse SDK not installed. Run `pip install langfuse` first.")
            sys.exit(1)

        if not env_results["LANGFUSE_PUBLIC_KEY"]["set"] or not env_results["LANGFUSE_SECRET_KEY"]["set"]:
            print("Error: Required environment variables not set.")
            print("Set LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY first.")
            sys.exit(1)

        results = create_test_trace()
        print(format_test_results(results))

        if not results["success"]:
            sys.exit(1)


if __name__ == "__main__":
    main()
