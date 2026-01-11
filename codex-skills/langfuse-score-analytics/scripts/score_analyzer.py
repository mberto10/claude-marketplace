#!/usr/bin/env python3
"""
Langfuse Score Analyzer

Analyze score trends, detect regressions, and understand score distributions.

USAGE:
    python score_analyzer.py list-scores --days 30
    python score_analyzer.py summary --score-name "accuracy" --days 30
    python score_analyzer.py trend --score-name "accuracy" --days 14 --granularity day
    python score_analyzer.py compare --score-name "accuracy" --dimension release --days 7
    python score_analyzer.py regression --score-name "accuracy" --baseline-days 14 --current-days 7
    python score_analyzer.py distribution --score-name "accuracy" --days 30 --bins 10
"""

import argparse
import json
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


def list_scores(days: int) -> List[Dict[str, Any]]:
    """List all unique score names in the project."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        # Fetch scores and extract unique names
        scores = client.api.scores.get_many(
            from_timestamp=from_time,
            to_timestamp=to_time,
            limit=1000
        )

        score_counts = defaultdict(lambda: {"count": 0, "types": set()})

        if hasattr(scores, 'data'):
            for score in scores.data:
                name = score.name
                score_counts[name]["count"] += 1
                if hasattr(score, 'data_type') and score.data_type:
                    score_counts[name]["types"].add(score.data_type)

        result = []
        for name, info in sorted(score_counts.items()):
            result.append({
                "name": name,
                "count": info["count"],
                "types": list(info["types"])
            })

        return result
    except Exception as e:
        print(f"Error listing scores: {e}", file=sys.stderr)
        return []


def get_score_summary(score_name: str, days: int) -> Dict[str, Any]:
    """Get aggregate statistics for a score."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        # Fetch all scores with the given name
        scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=from_time,
            to_timestamp=to_time,
            limit=10000
        )

        values = []
        if hasattr(scores, 'data'):
            for score in scores.data:
                if hasattr(score, 'value') and score.value is not None:
                    values.append(float(score.value))

        if not values:
            return {"error": f"No numeric scores found for '{score_name}'"}

        values.sort()
        n = len(values)

        return {
            "score_name": score_name,
            "days": days,
            "count": n,
            "mean": sum(values) / n,
            "min": values[0],
            "max": values[-1],
            "p50": values[n // 2],
            "p95": values[int(n * 0.95)] if n > 1 else values[0],
            "std_dev": (sum((x - sum(values)/n)**2 for x in values) / n) ** 0.5
        }
    except Exception as e:
        print(f"Error getting score summary: {e}", file=sys.stderr)
        return {"error": str(e)}


def get_score_trend(score_name: str, days: int, granularity: str) -> List[Dict[str, Any]]:
    """Get score values over time with specified granularity."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        # Fetch all scores with the given name
        scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=from_time,
            to_timestamp=to_time,
            limit=10000
        )

        # Group by time bucket
        buckets = defaultdict(list)

        if hasattr(scores, 'data'):
            for score in scores.data:
                if hasattr(score, 'value') and score.value is not None:
                    # Parse timestamp
                    ts = score.timestamp if hasattr(score, 'timestamp') else None
                    if ts:
                        if isinstance(ts, str):
                            ts = datetime.fromisoformat(ts.replace('Z', '+00:00'))

                        # Create bucket key based on granularity
                        if granularity == "hour":
                            key = ts.strftime("%Y-%m-%d %H:00")
                        elif granularity == "day":
                            key = ts.strftime("%Y-%m-%d")
                        elif granularity == "week":
                            # Get start of week
                            week_start = ts - timedelta(days=ts.weekday())
                            key = week_start.strftime("%Y-%m-%d")
                        elif granularity == "month":
                            key = ts.strftime("%Y-%m")
                        else:
                            key = ts.strftime("%Y-%m-%d")

                        buckets[key].append(float(score.value))

        # Calculate stats for each bucket
        result = []
        for key in sorted(buckets.keys()):
            values = buckets[key]
            result.append({
                "period": key,
                "count": len(values),
                "mean": sum(values) / len(values),
                "min": min(values),
                "max": max(values)
            })

        return result
    except Exception as e:
        print(f"Error getting score trend: {e}", file=sys.stderr)
        return []


def compare_by_dimension(score_name: str, dimension: str, days: int) -> Dict[str, Any]:
    """Compare scores across a dimension (release, environment, name)."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        # Fetch scores
        scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=from_time,
            to_timestamp=to_time,
            limit=10000
        )

        # We need to get trace info for each score to get the dimension
        trace_cache = {}
        dimension_values = defaultdict(list)

        if hasattr(scores, 'data'):
            for score in scores.data:
                if hasattr(score, 'value') and score.value is not None:
                    trace_id = score.trace_id

                    # Get trace info if not cached
                    if trace_id not in trace_cache:
                        try:
                            trace = client.api.trace.get(trace_id)
                            trace_cache[trace_id] = trace
                        except:
                            trace_cache[trace_id] = None

                    trace = trace_cache[trace_id]
                    if trace:
                        # Get dimension value
                        if dimension == "release":
                            dim_value = getattr(trace, 'release', None) or "unknown"
                        elif dimension == "environment":
                            metadata = getattr(trace, 'metadata', {}) or {}
                            dim_value = metadata.get('environment', 'unknown')
                        elif dimension == "name":
                            dim_value = getattr(trace, 'name', None) or "unknown"
                        else:
                            dim_value = "unknown"

                        dimension_values[dim_value].append(float(score.value))

        # Calculate stats for each dimension value
        result = {
            "score_name": score_name,
            "dimension": dimension,
            "days": days,
            "breakdown": {}
        }

        for dim_value, values in sorted(dimension_values.items()):
            values.sort()
            n = len(values)
            result["breakdown"][dim_value] = {
                "count": n,
                "mean": sum(values) / n,
                "min": values[0],
                "max": values[-1],
                "p50": values[n // 2]
            }

        return result
    except Exception as e:
        print(f"Error comparing scores: {e}", file=sys.stderr)
        return {"error": str(e)}


def detect_regression(score_name: str, baseline_days: int, current_days: int) -> Dict[str, Any]:
    """Compare scores between baseline and current periods."""
    client = get_langfuse_client()

    now = datetime.now(timezone.utc)

    # Current period: last current_days
    current_end = now
    current_start = now - timedelta(days=current_days)

    # Baseline period: current_days before current period
    baseline_end = current_start
    baseline_start = baseline_end - timedelta(days=baseline_days)

    try:
        # Fetch baseline scores
        baseline_scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=baseline_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            to_timestamp=baseline_end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            limit=10000
        )

        # Fetch current scores
        current_scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=current_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            to_timestamp=current_end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            limit=10000
        )

        # Extract values
        baseline_values = []
        if hasattr(baseline_scores, 'data'):
            for score in baseline_scores.data:
                if hasattr(score, 'value') and score.value is not None:
                    baseline_values.append(float(score.value))

        current_values = []
        if hasattr(current_scores, 'data'):
            for score in current_scores.data:
                if hasattr(score, 'value') and score.value is not None:
                    current_values.append(float(score.value))

        if not baseline_values:
            return {"error": "No baseline data found"}
        if not current_values:
            return {"error": "No current data found"}

        baseline_mean = sum(baseline_values) / len(baseline_values)
        current_mean = sum(current_values) / len(current_values)

        delta = current_mean - baseline_mean
        pct_change = (delta / baseline_mean * 100) if baseline_mean != 0 else 0

        # Determine if this is a regression (assuming higher is better)
        is_regression = delta < 0 and abs(pct_change) > 5  # 5% threshold

        return {
            "score_name": score_name,
            "baseline": {
                "period": f"{baseline_start.strftime('%Y-%m-%d')} to {baseline_end.strftime('%Y-%m-%d')}",
                "days": baseline_days,
                "count": len(baseline_values),
                "mean": baseline_mean
            },
            "current": {
                "period": f"{current_start.strftime('%Y-%m-%d')} to {current_end.strftime('%Y-%m-%d')}",
                "days": current_days,
                "count": len(current_values),
                "mean": current_mean
            },
            "delta": delta,
            "pct_change": pct_change,
            "is_regression": is_regression,
            "severity": "high" if abs(pct_change) > 20 else "medium" if abs(pct_change) > 10 else "low"
        }
    except Exception as e:
        print(f"Error detecting regression: {e}", file=sys.stderr)
        return {"error": str(e)}


def get_distribution(score_name: str, days: int, bins: int) -> Dict[str, Any]:
    """Get score value distribution."""
    client = get_langfuse_client()
    from_time, to_time = get_time_range(days)

    try:
        # Fetch all scores with the given name
        scores = client.api.scores.get_many(
            name=score_name,
            from_timestamp=from_time,
            to_timestamp=to_time,
            limit=10000
        )

        values = []
        if hasattr(scores, 'data'):
            for score in scores.data:
                if hasattr(score, 'value') and score.value is not None:
                    values.append(float(score.value))

        if not values:
            return {"error": f"No numeric scores found for '{score_name}'"}

        min_val = min(values)
        max_val = max(values)

        # Handle edge case where all values are the same
        if min_val == max_val:
            return {
                "score_name": score_name,
                "days": days,
                "count": len(values),
                "min": min_val,
                "max": max_val,
                "bins": [{"range": f"{min_val:.2f}", "count": len(values), "pct": 100.0}]
            }

        # Create histogram bins
        bin_width = (max_val - min_val) / bins
        histogram = [0] * bins

        for value in values:
            # Determine bin index
            idx = min(int((value - min_val) / bin_width), bins - 1)
            histogram[idx] += 1

        # Format bins for output
        bin_data = []
        for i, count in enumerate(histogram):
            bin_start = min_val + i * bin_width
            bin_end = bin_start + bin_width
            pct = count / len(values) * 100
            bin_data.append({
                "range": f"{bin_start:.2f}-{bin_end:.2f}",
                "count": count,
                "pct": round(pct, 1)
            })

        return {
            "score_name": score_name,
            "days": days,
            "count": len(values),
            "min": min_val,
            "max": max_val,
            "bins": bin_data
        }
    except Exception as e:
        print(f"Error getting distribution: {e}", file=sys.stderr)
        return {"error": str(e)}


# Formatting functions

def format_score_list(scores: List[Dict[str, Any]]) -> str:
    """Format score list for display."""
    if not scores:
        return "No scores found"

    lines = ["# Available Scores\n"]
    lines.append("| Name | Count | Types |")
    lines.append("|------|-------|-------|")

    for s in scores:
        types = ", ".join(s.get("types", [])) or "-"
        lines.append(f"| {s['name']} | {s['count']} | {types} |")

    return "\n".join(lines)


def format_summary(summary: Dict[str, Any]) -> str:
    """Format score summary for display."""
    if "error" in summary:
        return f"Error: {summary['error']}"

    lines = [f"# Score Summary: {summary['score_name']}\n"]
    lines.append(f"**Period:** Last {summary['days']} days")
    lines.append(f"**Count:** {summary['count']} scores\n")
    lines.append("## Statistics\n")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Mean | {summary['mean']:.4f} |")
    lines.append(f"| Min | {summary['min']:.4f} |")
    lines.append(f"| Max | {summary['max']:.4f} |")
    lines.append(f"| Median (p50) | {summary['p50']:.4f} |")
    lines.append(f"| p95 | {summary['p95']:.4f} |")
    lines.append(f"| Std Dev | {summary['std_dev']:.4f} |")

    return "\n".join(lines)


def format_trend(trend: List[Dict[str, Any]], score_name: str, granularity: str) -> str:
    """Format score trend for display."""
    if not trend:
        return "No trend data found"

    lines = [f"# Score Trend: {score_name}\n"]
    lines.append(f"**Granularity:** {granularity}\n")
    lines.append("| Period | Count | Mean | Min | Max |")
    lines.append("|--------|-------|------|-----|-----|")

    for t in trend:
        lines.append(f"| {t['period']} | {t['count']} | {t['mean']:.4f} | {t['min']:.4f} | {t['max']:.4f} |")

    return "\n".join(lines)


def format_comparison(comparison: Dict[str, Any]) -> str:
    """Format dimension comparison for display."""
    if "error" in comparison:
        return f"Error: {comparison['error']}"

    lines = [f"# Score Comparison: {comparison['score_name']}\n"]
    lines.append(f"**Dimension:** {comparison['dimension']}")
    lines.append(f"**Period:** Last {comparison['days']} days\n")
    lines.append("| Value | Count | Mean | Min | Max | Median |")
    lines.append("|-------|-------|------|-----|-----|--------|")

    for dim_value, stats in comparison.get("breakdown", {}).items():
        lines.append(f"| {dim_value} | {stats['count']} | {stats['mean']:.4f} | {stats['min']:.4f} | {stats['max']:.4f} | {stats['p50']:.4f} |")

    return "\n".join(lines)


def format_regression(regression: Dict[str, Any]) -> str:
    """Format regression analysis for display."""
    if "error" in regression:
        return f"Error: {regression['error']}"

    lines = [f"# Regression Analysis: {regression['score_name']}\n"]

    # Status indicator
    if regression['is_regression']:
        lines.append(f"**Status:** REGRESSION DETECTED ({regression['severity'].upper()} severity)")
    else:
        lines.append("**Status:** No significant regression detected")

    lines.append("")
    lines.append("## Baseline Period")
    lines.append(f"- **Period:** {regression['baseline']['period']}")
    lines.append(f"- **Count:** {regression['baseline']['count']} scores")
    lines.append(f"- **Mean:** {regression['baseline']['mean']:.4f}")

    lines.append("")
    lines.append("## Current Period")
    lines.append(f"- **Period:** {regression['current']['period']}")
    lines.append(f"- **Count:** {regression['current']['count']} scores")
    lines.append(f"- **Mean:** {regression['current']['mean']:.4f}")

    lines.append("")
    lines.append("## Change")
    lines.append(f"- **Delta:** {regression['delta']:+.4f}")
    lines.append(f"- **Percent Change:** {regression['pct_change']:+.2f}%")

    return "\n".join(lines)


def format_distribution(distribution: Dict[str, Any]) -> str:
    """Format score distribution for display."""
    if "error" in distribution:
        return f"Error: {distribution['error']}"

    lines = [f"# Score Distribution: {distribution['score_name']}\n"]
    lines.append(f"**Period:** Last {distribution['days']} days")
    lines.append(f"**Count:** {distribution['count']} scores")
    lines.append(f"**Range:** {distribution['min']:.4f} - {distribution['max']:.4f}\n")

    lines.append("## Histogram\n")
    lines.append("| Range | Count | % |")
    lines.append("|-------|-------|---|")

    for b in distribution.get("bins", []):
        # Create simple bar visualization
        bar = "#" * int(b['pct'] / 5)
        lines.append(f"| {b['range']} | {b['count']} | {b['pct']}% {bar} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Langfuse Score Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # List scores command
    list_parser = subparsers.add_parser("list-scores", help="List available scores")
    list_parser.add_argument("--days", type=int, default=30, help="Days to look back (default: 30)")

    # Summary command
    summary_parser = subparsers.add_parser("summary", help="Get score statistics")
    summary_parser.add_argument("--score-name", required=True, help="Score name")
    summary_parser.add_argument("--days", type=int, default=30, help="Days to analyze (default: 30)")

    # Trend command
    trend_parser = subparsers.add_parser("trend", help="Show score trend over time")
    trend_parser.add_argument("--score-name", required=True, help="Score name")
    trend_parser.add_argument("--days", type=int, default=14, help="Days to analyze (default: 14)")
    trend_parser.add_argument("--granularity", default="day",
                              choices=["hour", "day", "week", "month"],
                              help="Time granularity (default: day)")

    # Compare command
    compare_parser = subparsers.add_parser("compare", help="Compare scores by dimension")
    compare_parser.add_argument("--score-name", required=True, help="Score name")
    compare_parser.add_argument("--dimension", required=True,
                               choices=["release", "environment", "name"],
                               help="Dimension to compare")
    compare_parser.add_argument("--days", type=int, default=7, help="Days to analyze (default: 7)")

    # Regression command
    regression_parser = subparsers.add_parser("regression", help="Detect score regressions")
    regression_parser.add_argument("--score-name", required=True, help="Score name")
    regression_parser.add_argument("--baseline-days", type=int, default=14,
                                   help="Baseline period days (default: 14)")
    regression_parser.add_argument("--current-days", type=int, default=7,
                                   help="Current period days (default: 7)")

    # Distribution command
    dist_parser = subparsers.add_parser("distribution", help="Show score distribution")
    dist_parser.add_argument("--score-name", required=True, help="Score name")
    dist_parser.add_argument("--days", type=int, default=30, help="Days to analyze (default: 30)")
    dist_parser.add_argument("--bins", type=int, default=10, help="Number of bins (default: 10)")

    args = parser.parse_args()

    if args.command == "list-scores":
        scores = list_scores(args.days)
        print(format_score_list(scores))

    elif args.command == "summary":
        summary = get_score_summary(args.score_name, args.days)
        print(format_summary(summary))

    elif args.command == "trend":
        trend = get_score_trend(args.score_name, args.days, args.granularity)
        print(format_trend(trend, args.score_name, args.granularity))

    elif args.command == "compare":
        comparison = compare_by_dimension(args.score_name, args.dimension, args.days)
        print(format_comparison(comparison))

    elif args.command == "regression":
        regression = detect_regression(args.score_name, args.baseline_days, args.current_days)
        print(format_regression(regression))

    elif args.command == "distribution":
        distribution = get_distribution(args.score_name, args.days, args.bins)
        print(format_distribution(distribution))


if __name__ == "__main__":
    main()
