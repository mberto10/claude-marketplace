#!/usr/bin/env python3
"""
Langfuse Annotation Manager

Manage human annotations and scores on traces.

USAGE:
    python annotation_manager.py create-score --trace-id "abc" --name "quality" --value 8.5
    python annotation_manager.py update-score --score-id "xyz" --value 9.0
    python annotation_manager.py delete-score --score-id "xyz"
    python annotation_manager.py list-scores --trace-id "abc"
    python annotation_manager.py pending --score-name "review" --days 7
    python annotation_manager.py export --score-name "quality" --days 30 --format json
    python annotation_manager.py configs
"""

import argparse
import csv
import io
import json
import sys
from datetime import datetime, timedelta, timezone
from typing import Optional, List, Dict, Any

from langfuse_client import get_langfuse_client


def get_time_range(days: int) -> tuple:
    """Get ISO formatted time range for the last N days."""
    now = datetime.now(timezone.utc)
    from_time = now - timedelta(days=days)
    return (
        from_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        now.strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def create_score(
    trace_id: str,
    name: str,
    value: Optional[float] = None,
    string_value: Optional[str] = None,
    comment: Optional[str] = None,
    data_type: str = "NUMERIC",
    observation_id: Optional[str] = None
) -> Dict[str, Any]:
    """Create a new score on a trace."""
    client = get_langfuse_client()

    try:
        kwargs = {
            "trace_id": trace_id,
            "name": name,
        }

        if data_type == "NUMERIC":
            if value is None:
                return {"error": "Numeric score requires --value"}
            kwargs["value"] = value
        elif data_type == "CATEGORICAL":
            if string_value is None:
                return {"error": "Categorical score requires --string-value"}
            kwargs["value"] = string_value
        elif data_type == "BOOLEAN":
            if value is None:
                return {"error": "Boolean score requires --value (0 or 1)"}
            kwargs["value"] = bool(value)

        if comment:
            kwargs["comment"] = comment

        if observation_id:
            kwargs["observation_id"] = observation_id

        # Use the score method
        client.score(**kwargs)

        return {
            "status": "created",
            "trace_id": trace_id,
            "name": name,
            "value": value if data_type == "NUMERIC" else string_value if data_type == "CATEGORICAL" else bool(value),
            "data_type": data_type
        }
    except Exception as e:
        print(f"Error creating score: {e}", file=sys.stderr)
        return {"error": str(e)}


def update_score(
    score_id: str,
    value: Optional[float] = None,
    string_value: Optional[str] = None,
    comment: Optional[str] = None
) -> Dict[str, Any]:
    """Update an existing score."""
    client = get_langfuse_client()

    try:
        # Get the existing score first
        # Note: Langfuse SDK may not support direct score update
        # This is a best-effort implementation

        # Try to use the API directly if available
        if hasattr(client.api, 'scores') and hasattr(client.api.scores, 'update'):
            kwargs = {}
            if value is not None:
                kwargs["value"] = value
            if string_value is not None:
                kwargs["value"] = string_value
            if comment is not None:
                kwargs["comment"] = comment

            client.api.scores.update(score_id, **kwargs)

            return {
                "status": "updated",
                "score_id": score_id
            }
        else:
            return {"error": "Score update not supported by current SDK version"}

    except Exception as e:
        print(f"Error updating score: {e}", file=sys.stderr)
        return {"error": str(e)}


def delete_score(score_id: str) -> Dict[str, Any]:
    """Delete a score."""
    client = get_langfuse_client()

    try:
        if hasattr(client.api, 'scores') and hasattr(client.api.scores, 'delete'):
            client.api.scores.delete(score_id)
            return {"status": "deleted", "score_id": score_id}
        else:
            return {"error": "Score deletion not supported by current SDK version"}
    except Exception as e:
        print(f"Error deleting score: {e}", file=sys.stderr)
        return {"error": str(e)}


def list_scores(
    trace_id: Optional[str] = None,
    name: Optional[str] = None,
    limit: int = 100
) -> List[Dict[str, Any]]:
    """List scores for a trace or by name."""
    client = get_langfuse_client()

    try:
        kwargs = {"limit": limit}
        if trace_id:
            kwargs["trace_id"] = trace_id
        if name:
            kwargs["name"] = name

        scores = client.api.scores.get_many(**kwargs)

        result = []
        if hasattr(scores, 'data'):
            for score in scores.data:
                score_dict = {
                    "id": score.id,
                    "name": score.name,
                    "trace_id": getattr(score, 'trace_id', None),
                }

                # Handle value based on type
                if hasattr(score, 'value'):
                    score_dict["value"] = score.value
                if hasattr(score, 'string_value'):
                    score_dict["string_value"] = score.string_value

                if hasattr(score, 'comment') and score.comment:
                    score_dict["comment"] = score.comment
                if hasattr(score, 'data_type'):
                    score_dict["data_type"] = score.data_type
                if hasattr(score, 'timestamp'):
                    score_dict["timestamp"] = str(score.timestamp)

                result.append(score_dict)

        return result
    except Exception as e:
        print(f"Error listing scores: {e}", file=sys.stderr)
        return []


def find_pending_traces(
    score_name: str,
    days: int,
    trace_name: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """Find traces that don't have a specific score."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        # Get recent traces
        kwargs = {
            "limit": limit * 5,  # Fetch more since we'll filter
            "from_timestamp": from_time,
            "to_timestamp": to_time
        }
        if trace_name:
            kwargs["name"] = trace_name

        traces = client.api.trace.list(**kwargs)

        # Get traces that already have this score
        scored_traces = set()
        scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=from_time,
            to_timestamp=to_time,
            limit=1000
        )
        if hasattr(scores, 'data'):
            for score in scores.data:
                if hasattr(score, 'trace_id'):
                    scored_traces.add(score.trace_id)

        # Filter to traces without the score
        pending = []
        if hasattr(traces, 'data'):
            for trace in traces.data:
                if trace.id not in scored_traces:
                    pending.append({
                        "id": trace.id,
                        "name": getattr(trace, 'name', None),
                        "timestamp": str(trace.timestamp) if hasattr(trace, 'timestamp') else None,
                        "input_preview": str(getattr(trace, 'input', ''))[:100] if getattr(trace, 'input', None) else None
                    })
                    if len(pending) >= limit:
                        break

        return pending
    except Exception as e:
        print(f"Error finding pending traces: {e}", file=sys.stderr)
        return []


def export_scores(
    score_name: str,
    days: int,
    format: str = "json"
) -> str:
    """Export scores to JSON or CSV format."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=from_time,
            to_timestamp=to_time,
            limit=10000
        )

        data = []
        if hasattr(scores, 'data'):
            for score in scores.data:
                row = {
                    "id": score.id,
                    "name": score.name,
                    "trace_id": getattr(score, 'trace_id', None),
                    "value": getattr(score, 'value', None),
                    "string_value": getattr(score, 'string_value', None),
                    "comment": getattr(score, 'comment', None),
                    "data_type": getattr(score, 'data_type', None),
                    "timestamp": str(score.timestamp) if hasattr(score, 'timestamp') else None
                }
                data.append(row)

        if format == "json":
            return json.dumps(data, indent=2)
        elif format == "csv":
            if not data:
                return "No data to export"

            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            return output.getvalue()
        else:
            return json.dumps(data, indent=2)

    except Exception as e:
        print(f"Error exporting scores: {e}", file=sys.stderr)
        return json.dumps({"error": str(e)})


def list_score_configs() -> List[Dict[str, Any]]:
    """List available score configurations."""
    client = get_langfuse_client()

    try:
        # Try to get score configs if the API supports it
        if hasattr(client.api, 'score_configs'):
            configs = client.api.score_configs.list()
            result = []
            if hasattr(configs, 'data'):
                for config in configs.data:
                    result.append({
                        "name": config.name,
                        "data_type": getattr(config, 'data_type', None),
                        "min_value": getattr(config, 'min_value', None),
                        "max_value": getattr(config, 'max_value', None),
                        "categories": getattr(config, 'categories', None),
                        "description": getattr(config, 'description', None)
                    })
            return result
        else:
            # Fall back to listing unique score names
            scores = client.api.scores.get_many(limit=1000)
            seen_names = {}
            if hasattr(scores, 'data'):
                for score in scores.data:
                    name = score.name
                    if name not in seen_names:
                        seen_names[name] = {
                            "name": name,
                            "data_type": getattr(score, 'data_type', 'NUMERIC'),
                            "sample_value": getattr(score, 'value', None)
                        }
            return list(seen_names.values())

    except Exception as e:
        print(f"Error listing score configs: {e}", file=sys.stderr)
        return []


# Formatting functions

def format_result(result: Dict[str, Any]) -> str:
    """Format operation result."""
    if "error" in result:
        return f"Error: {result['error']}"

    status = result.get('status', 'completed')
    lines = [f"**Status:** {status}"]

    for key, value in result.items():
        if key != 'status' and value is not None:
            lines.append(f"**{key}:** {value}")

    return "\n".join(lines)


def format_score_list(scores: List[Dict[str, Any]]) -> str:
    """Format score list for display."""
    if not scores:
        return "No scores found"

    lines = ["# Scores\n"]
    lines.append("| Name | Value | Type | Trace ID | Comment |")
    lines.append("|------|-------|------|----------|---------|")

    for s in scores:
        name = s.get('name', '-')
        value = s.get('value', s.get('string_value', '-'))
        dtype = s.get('data_type', '-')
        trace_id = s.get('trace_id', '-')
        if trace_id and len(trace_id) > 15:
            trace_id = trace_id[:15] + "..."
        comment = s.get('comment', '-') or '-'
        if len(comment) > 30:
            comment = comment[:30] + "..."

        lines.append(f"| {name} | {value} | {dtype} | {trace_id} | {comment} |")

    return "\n".join(lines)


def format_pending(traces: List[Dict[str, Any]], score_name: str) -> str:
    """Format pending traces for display."""
    if not traces:
        return f"No traces pending for score '{score_name}'"

    lines = [f"# Traces Pending '{score_name}' Annotation\n"]
    lines.append("| Trace ID | Name | Timestamp | Input Preview |")
    lines.append("|----------|------|-----------|---------------|")

    for t in traces:
        trace_id = t.get('id', '-')
        if len(trace_id) > 20:
            trace_id = trace_id[:20] + "..."
        name = t.get('name', '-') or '-'
        timestamp = t.get('timestamp', '-')
        if timestamp and len(timestamp) > 19:
            timestamp = timestamp[:19]
        preview = t.get('input_preview', '-') or '-'
        if len(preview) > 40:
            preview = preview[:40] + "..."

        lines.append(f"| {trace_id} | {name} | {timestamp} | {preview} |")

    return "\n".join(lines)


def format_configs(configs: List[Dict[str, Any]]) -> str:
    """Format score configs for display."""
    if not configs:
        return "No score configurations found"

    lines = ["# Score Configurations\n"]
    lines.append("| Name | Type | Range/Categories |")
    lines.append("|------|------|------------------|")

    for c in configs:
        name = c.get('name', '-')
        dtype = c.get('data_type', 'NUMERIC')

        if c.get('min_value') is not None or c.get('max_value') is not None:
            range_str = f"{c.get('min_value', '?')} - {c.get('max_value', '?')}"
        elif c.get('categories'):
            range_str = ", ".join(c['categories'][:3])
            if len(c['categories']) > 3:
                range_str += "..."
        elif c.get('sample_value') is not None:
            range_str = f"(sample: {c['sample_value']})"
        else:
            range_str = "-"

        lines.append(f"| {name} | {dtype} | {range_str} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Langfuse Annotation Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create score command
    create_parser = subparsers.add_parser("create-score", help="Create a score")
    create_parser.add_argument("--trace-id", required=True, help="Trace ID to score")
    create_parser.add_argument("--name", required=True, help="Score name")
    create_parser.add_argument("--value", type=float, help="Numeric value")
    create_parser.add_argument("--string-value", help="String value for categorical")
    create_parser.add_argument("--comment", help="Optional comment")
    create_parser.add_argument("--data-type", default="NUMERIC",
                               choices=["NUMERIC", "CATEGORICAL", "BOOLEAN"],
                               help="Score data type")
    create_parser.add_argument("--observation-id", help="Optional observation ID")

    # Update score command
    update_parser = subparsers.add_parser("update-score", help="Update a score")
    update_parser.add_argument("--score-id", required=True, help="Score ID")
    update_parser.add_argument("--value", type=float, help="New numeric value")
    update_parser.add_argument("--string-value", help="New string value")
    update_parser.add_argument("--comment", help="New comment")

    # Delete score command
    delete_parser = subparsers.add_parser("delete-score", help="Delete a score")
    delete_parser.add_argument("--score-id", required=True, help="Score ID")

    # List scores command
    list_parser = subparsers.add_parser("list-scores", help="List scores")
    list_parser.add_argument("--trace-id", help="Filter by trace ID")
    list_parser.add_argument("--name", help="Filter by score name")
    list_parser.add_argument("--limit", type=int, default=100, help="Max results")

    # Pending command
    pending_parser = subparsers.add_parser("pending", help="Find traces needing annotation")
    pending_parser.add_argument("--score-name", required=True, help="Score name to check")
    pending_parser.add_argument("--days", type=int, default=7, help="Days to look back")
    pending_parser.add_argument("--trace-name", help="Filter by trace name")
    pending_parser.add_argument("--limit", type=int, default=20, help="Max results")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export scores")
    export_parser.add_argument("--score-name", required=True, help="Score name")
    export_parser.add_argument("--days", type=int, default=30, help="Days to export")
    export_parser.add_argument("--format", default="json",
                               choices=["json", "csv"], help="Output format")
    export_parser.add_argument("--output", help="Output file (prints to stdout if not set)")

    # Configs command
    subparsers.add_parser("configs", help="List score configurations")

    args = parser.parse_args()

    if args.command == "create-score":
        result = create_score(
            trace_id=args.trace_id,
            name=args.name,
            value=args.value,
            string_value=args.string_value,
            comment=args.comment,
            data_type=args.data_type,
            observation_id=args.observation_id
        )
        print(format_result(result))

    elif args.command == "update-score":
        result = update_score(
            score_id=args.score_id,
            value=args.value,
            string_value=args.string_value,
            comment=args.comment
        )
        print(format_result(result))

    elif args.command == "delete-score":
        result = delete_score(args.score_id)
        print(format_result(result))

    elif args.command == "list-scores":
        scores = list_scores(
            trace_id=args.trace_id,
            name=args.name,
            limit=args.limit
        )
        print(format_score_list(scores))

    elif args.command == "pending":
        traces = find_pending_traces(
            score_name=args.score_name,
            days=args.days,
            trace_name=args.trace_name,
            limit=args.limit
        )
        print(format_pending(traces, args.score_name))

    elif args.command == "export":
        output = export_scores(
            score_name=args.score_name,
            days=args.days,
            format=args.format
        )
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Exported to {args.output}")
        else:
            print(output)

    elif args.command == "configs":
        configs = list_score_configs()
        print(format_configs(configs))


if __name__ == "__main__":
    main()
