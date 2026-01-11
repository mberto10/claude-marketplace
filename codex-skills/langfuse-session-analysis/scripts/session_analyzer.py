#!/usr/bin/env python3
"""
Langfuse Session Analyzer

Analyze multi-trace user sessions, debug conversation flows, and understand session-level metrics.

USAGE:
    python session_analyzer.py list --limit 20
    python session_analyzer.py get --session-id "session-123"
    python session_analyzer.py analyze --session-id "session-123"
    python session_analyzer.py find-issues --days 7 --has-errors
    python session_analyzer.py timeline --session-id "session-123"
"""

import argparse
import sys
from datetime import datetime, timedelta, timezone
from typing import Optional, List, Dict, Any
from collections import defaultdict

from langfuse_client import get_langfuse_client


def get_time_range(days: int) -> tuple:
    """Get ISO formatted time range for the last N days."""
    now = datetime.now(timezone.utc)
    from_time = now - timedelta(days=days)
    return (
        from_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        now.strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def list_sessions(limit: int = 20, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """List recent sessions with summary stats."""
    client = get_langfuse_client()

    try:
        # Fetch sessions
        kwargs = {"limit": limit}
        if user_id:
            kwargs["user_id"] = user_id

        response = client.api.sessions.list(**kwargs)

        sessions = []
        if hasattr(response, 'data'):
            for session in response.data:
                session_dict = {
                    "id": session.id,
                    "created_at": str(session.created_at) if hasattr(session, 'created_at') else None,
                    "user_id": getattr(session, 'user_id', None),
                    "trace_count": getattr(session, 'trace_count', 0),
                }

                # Add any available metrics
                if hasattr(session, 'total_cost'):
                    session_dict["total_cost"] = session.total_cost
                if hasattr(session, 'traces'):
                    session_dict["trace_count"] = len(session.traces)

                sessions.append(session_dict)

        return sessions
    except Exception as e:
        print(f"Error listing sessions: {e}", file=sys.stderr)
        return []


def get_session(session_id: str) -> Optional[Dict[str, Any]]:
    """Get full session details with traces."""
    client = get_langfuse_client()

    try:
        session = client.api.sessions.get(session_id)

        if not session:
            return None

        result = {
            "id": session.id,
            "created_at": str(session.created_at) if hasattr(session, 'created_at') else None,
            "user_id": getattr(session, 'user_id', None),
            "traces": []
        }

        # Get traces for this session
        if hasattr(session, 'traces'):
            for trace in session.traces:
                trace_dict = {
                    "id": trace.id,
                    "name": getattr(trace, 'name', None),
                    "timestamp": str(trace.timestamp) if hasattr(trace, 'timestamp') else None,
                    "input": getattr(trace, 'input', None),
                    "output": getattr(trace, 'output', None),
                    "status": getattr(trace, 'status', None),
                }

                # Add metrics if available
                if hasattr(trace, 'total_cost'):
                    trace_dict["cost"] = trace.total_cost
                if hasattr(trace, 'usage'):
                    trace_dict["tokens"] = trace.usage

                result["traces"].append(trace_dict)

        return result
    except Exception as e:
        print(f"Error getting session '{session_id}': {e}", file=sys.stderr)
        return None


def analyze_session(session_id: str) -> Dict[str, Any]:
    """Deep analysis of session quality and metrics."""
    client = get_langfuse_client()

    try:
        session = client.api.sessions.get(session_id)

        if not session:
            return {"error": f"Session '{session_id}' not found"}

        result = {
            "id": session.id,
            "user_id": getattr(session, 'user_id', None),
            "metrics": {
                "turn_count": 0,
                "duration_seconds": None,
                "total_tokens": 0,
                "total_cost": 0.0,
            },
            "scores": {},
            "has_errors": False,
            "error_count": 0,
            "traces": []
        }

        traces = session.traces if hasattr(session, 'traces') else []
        result["metrics"]["turn_count"] = len(traces)

        if not traces:
            return result

        # Parse timestamps and calculate duration
        timestamps = []
        for trace in traces:
            if hasattr(trace, 'timestamp'):
                ts = trace.timestamp
                if isinstance(ts, str):
                    ts = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                timestamps.append(ts)

            # Accumulate metrics
            if hasattr(trace, 'total_cost') and trace.total_cost:
                result["metrics"]["total_cost"] += trace.total_cost

            if hasattr(trace, 'usage') and trace.usage:
                if isinstance(trace.usage, dict):
                    result["metrics"]["total_tokens"] += trace.usage.get('total', 0)

            # Check for errors
            status = getattr(trace, 'status', None)
            if status and status.lower() == 'error':
                result["has_errors"] = True
                result["error_count"] += 1

            # Get trace info for summary
            result["traces"].append({
                "id": trace.id,
                "name": getattr(trace, 'name', None),
                "status": status
            })

        # Calculate duration
        if len(timestamps) >= 2:
            timestamps.sort()
            duration = timestamps[-1] - timestamps[0]
            result["metrics"]["duration_seconds"] = duration.total_seconds()

        # Aggregate scores across traces
        score_values = defaultdict(list)
        for trace in traces:
            trace_id = trace.id
            try:
                scores = client.api.scores.get_many(trace_id=trace_id, limit=100)
                if hasattr(scores, 'data'):
                    for score in scores.data:
                        if hasattr(score, 'value') and score.value is not None:
                            score_values[score.name].append(float(score.value))
            except:
                pass

        # Calculate average for each score
        for name, values in score_values.items():
            result["scores"][name] = {
                "count": len(values),
                "mean": sum(values) / len(values),
                "min": min(values),
                "max": max(values)
            }

        return result
    except Exception as e:
        print(f"Error analyzing session '{session_id}': {e}", file=sys.stderr)
        return {"error": str(e)}


def find_problematic_sessions(
    days: int,
    has_errors: bool = False,
    min_turns: Optional[int] = None,
    min_score: Optional[float] = None,
    score_name: Optional[str] = None,
    limit: int = 20
) -> List[Dict[str, Any]]:
    """Find sessions with issues."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        # Fetch recent sessions
        response = client.api.sessions.list(limit=100)

        problematic = []
        if hasattr(response, 'data'):
            for session in response.data:
                session_id = session.id

                # Get session details
                try:
                    details = client.api.sessions.get(session_id)
                except:
                    continue

                traces = details.traces if hasattr(details, 'traces') else []
                turn_count = len(traces)

                # Check min turns filter
                if min_turns and turn_count < min_turns:
                    continue

                # Check for errors
                session_has_errors = False
                for trace in traces:
                    status = getattr(trace, 'status', None)
                    if status and status.lower() == 'error':
                        session_has_errors = True
                        break

                if has_errors and not session_has_errors:
                    continue

                # Check score threshold
                if min_score and score_name:
                    session_scores = []
                    for trace in traces:
                        try:
                            scores = client.api.scores.get_many(
                                trace_id=trace.id,
                                name=score_name,
                                limit=10
                            )
                            if hasattr(scores, 'data'):
                                for score in scores.data:
                                    if hasattr(score, 'value') and score.value is not None:
                                        session_scores.append(float(score.value))
                        except:
                            pass

                    if session_scores:
                        avg_score = sum(session_scores) / len(session_scores)
                        if avg_score >= min_score:
                            continue
                    else:
                        continue  # No scores found, skip

                # Session matches filters
                problematic.append({
                    "id": session_id,
                    "user_id": getattr(session, 'user_id', None),
                    "turn_count": turn_count,
                    "has_errors": session_has_errors,
                    "created_at": str(session.created_at) if hasattr(session, 'created_at') else None
                })

                if len(problematic) >= limit:
                    break

        return problematic
    except Exception as e:
        print(f"Error finding problematic sessions: {e}", file=sys.stderr)
        return []


def get_session_timeline(session_id: str) -> str:
    """Get formatted timeline of session events."""
    client = get_langfuse_client()

    try:
        session = client.api.sessions.get(session_id)

        if not session:
            return f"Session '{session_id}' not found"

        traces = session.traces if hasattr(session, 'traces') else []

        if not traces:
            return "No traces in session"

        # Sort traces by timestamp
        sorted_traces = []
        for trace in traces:
            ts = getattr(trace, 'timestamp', None)
            if ts:
                if isinstance(ts, str):
                    ts = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                sorted_traces.append((ts, trace))

        sorted_traces.sort(key=lambda x: x[0])

        lines = [f"# Session Timeline: {session_id}\n"]

        for i, (ts, trace) in enumerate(sorted_traces, 1):
            time_str = ts.strftime("%H:%M:%S")
            name = getattr(trace, 'name', 'Unnamed')
            status = getattr(trace, 'status', '-')

            lines.append(f"## Turn {i} [{time_str}]")
            lines.append(f"**Trace:** {trace.id}")
            lines.append(f"**Name:** {name}")
            lines.append(f"**Status:** {status}")

            # Add input/output previews
            input_val = getattr(trace, 'input', None)
            if input_val:
                if isinstance(input_val, str):
                    preview = input_val[:200] + "..." if len(input_val) > 200 else input_val
                else:
                    preview = str(input_val)[:200]
                lines.append(f"\n**Input:** {preview}")

            output_val = getattr(trace, 'output', None)
            if output_val:
                if isinstance(output_val, str):
                    preview = output_val[:200] + "..." if len(output_val) > 200 else output_val
                else:
                    preview = str(output_val)[:200]
                lines.append(f"\n**Output:** {preview}")

            lines.append("")

        return "\n".join(lines)
    except Exception as e:
        print(f"Error getting timeline: {e}", file=sys.stderr)
        return f"Error: {e}"


# Formatting functions

def format_session_list(sessions: List[Dict[str, Any]]) -> str:
    """Format session list for display."""
    if not sessions:
        return "No sessions found"

    lines = ["# Sessions\n"]
    lines.append("| ID | User | Traces | Created |")
    lines.append("|----|------|--------|---------|")

    for s in sessions:
        session_id = s.get('id', '?')[:20]
        user_id = s.get('user_id', '-') or '-'
        if len(user_id) > 15:
            user_id = user_id[:15] + "..."
        trace_count = s.get('trace_count', 0)
        created = s.get('created_at', '-')
        if created and len(created) > 19:
            created = created[:19]

        lines.append(f"| {session_id} | {user_id} | {trace_count} | {created} |")

    return "\n".join(lines)


def format_session_detail(session: Dict[str, Any]) -> str:
    """Format session detail for display."""
    if not session:
        return "Session not found"

    if "error" in session:
        return f"Error: {session['error']}"

    lines = [f"# Session: {session['id']}\n"]

    if session.get('user_id'):
        lines.append(f"**User:** {session['user_id']}")
    if session.get('created_at'):
        lines.append(f"**Created:** {session['created_at']}")

    lines.append(f"\n## Traces ({len(session.get('traces', []))})\n")

    for i, trace in enumerate(session.get('traces', []), 1):
        lines.append(f"### {i}. {trace.get('name', 'Unnamed')}")
        lines.append(f"- **ID:** {trace.get('id')}")
        lines.append(f"- **Status:** {trace.get('status', '-')}")
        lines.append(f"- **Time:** {trace.get('timestamp', '-')}")
        lines.append("")

    return "\n".join(lines)


def format_analysis(analysis: Dict[str, Any]) -> str:
    """Format session analysis for display."""
    if "error" in analysis:
        return f"Error: {analysis['error']}"

    lines = [f"# Session Analysis: {analysis['id']}\n"]

    if analysis.get('user_id'):
        lines.append(f"**User:** {analysis['user_id']}")

    # Health status
    if analysis.get('has_errors'):
        lines.append(f"**Status:** HAS ERRORS ({analysis['error_count']} traces failed)")
    else:
        lines.append("**Status:** Healthy")

    lines.append("\n## Metrics\n")

    metrics = analysis.get('metrics', {})
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Turn Count | {metrics.get('turn_count', 0)} |")

    duration = metrics.get('duration_seconds')
    if duration:
        if duration > 3600:
            duration_str = f"{duration/3600:.1f} hours"
        elif duration > 60:
            duration_str = f"{duration/60:.1f} minutes"
        else:
            duration_str = f"{duration:.0f} seconds"
        lines.append(f"| Duration | {duration_str} |")

    tokens = metrics.get('total_tokens', 0)
    if tokens:
        lines.append(f"| Total Tokens | {tokens:,} |")

    cost = metrics.get('total_cost', 0)
    if cost:
        lines.append(f"| Total Cost | ${cost:.4f} |")

    # Scores
    scores = analysis.get('scores', {})
    if scores:
        lines.append("\n## Scores\n")
        lines.append("| Score | Count | Mean | Min | Max |")
        lines.append("|-------|-------|------|-----|-----|")

        for name, stats in scores.items():
            lines.append(f"| {name} | {stats['count']} | {stats['mean']:.3f} | {stats['min']:.3f} | {stats['max']:.3f} |")

    # Trace summary
    traces = analysis.get('traces', [])
    if traces:
        lines.append("\n## Traces\n")
        for i, trace in enumerate(traces, 1):
            status_icon = "X" if trace.get('status') == 'error' else "OK"
            lines.append(f"{i}. [{status_icon}] {trace.get('name', 'Unnamed')} - {trace.get('id')}")

    return "\n".join(lines)


def format_problematic(sessions: List[Dict[str, Any]]) -> str:
    """Format problematic sessions for display."""
    if not sessions:
        return "No problematic sessions found"

    lines = ["# Problematic Sessions\n"]
    lines.append("| ID | User | Turns | Errors | Created |")
    lines.append("|----|------|-------|--------|---------|")

    for s in sessions:
        session_id = s.get('id', '?')[:20]
        user_id = s.get('user_id', '-') or '-'
        if len(user_id) > 12:
            user_id = user_id[:12] + "..."
        turns = s.get('turn_count', 0)
        errors = "Yes" if s.get('has_errors') else "No"
        created = s.get('created_at', '-')
        if created and len(created) > 16:
            created = created[:16]

        lines.append(f"| {session_id} | {user_id} | {turns} | {errors} | {created} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Langfuse Session Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # List command
    list_parser = subparsers.add_parser("list", help="List sessions")
    list_parser.add_argument("--limit", type=int, default=20, help="Max sessions to return")
    list_parser.add_argument("--user-id", help="Filter by user ID")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get session details")
    get_parser.add_argument("--session-id", required=True, help="Session ID")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze session")
    analyze_parser.add_argument("--session-id", required=True, help="Session ID")

    # Find issues command
    issues_parser = subparsers.add_parser("find-issues", help="Find problematic sessions")
    issues_parser.add_argument("--days", type=int, default=7, help="Days to look back")
    issues_parser.add_argument("--has-errors", action="store_true", help="Only sessions with errors")
    issues_parser.add_argument("--min-turns", type=int, help="Minimum turn count")
    issues_parser.add_argument("--min-score", type=float, help="Score threshold (find below)")
    issues_parser.add_argument("--score-name", help="Score name for threshold")
    issues_parser.add_argument("--limit", type=int, default=20, help="Max results")

    # Timeline command
    timeline_parser = subparsers.add_parser("timeline", help="Show session timeline")
    timeline_parser.add_argument("--session-id", required=True, help="Session ID")

    args = parser.parse_args()

    if args.command == "list":
        sessions = list_sessions(args.limit, args.user_id)
        print(format_session_list(sessions))

    elif args.command == "get":
        session = get_session(args.session_id)
        print(format_session_detail(session))

    elif args.command == "analyze":
        analysis = analyze_session(args.session_id)
        print(format_analysis(analysis))

    elif args.command == "find-issues":
        sessions = find_problematic_sessions(
            days=args.days,
            has_errors=args.has_errors,
            min_turns=args.min_turns,
            min_score=args.min_score,
            score_name=args.score_name,
            limit=args.limit
        )
        print(format_problematic(sessions))

    elif args.command == "timeline":
        timeline = get_session_timeline(args.session_id)
        print(timeline)


if __name__ == "__main__":
    main()
