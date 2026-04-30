#!/usr/bin/env python3
"""
Transition Drift Analysis · OMNIA-CONSTANT

Purpose:
    Test whether the Ω transition region remains stable across
    time windows, seeds, experiment versions, or source files.

Core question:

    Does the Ω≈0.6 transition region remain stable,
    or does it drift unpredictably?

A real boundary may move slightly.

A weak artifact may wander arbitrarily.
"""

import json
import statistics
from pathlib import Path
from collections import defaultdict


INPUT_RESULTS_DIR = Path("imported_results/invariance")

OUTPUT_DIR = Path("results/import_from_invariance")
SUMMARY_FILE = OUTPUT_DIR / "transition_drift_summary.json"
ASCII_FILE = OUTPUT_DIR / "transition_drift_ascii.txt"

OMEGA_CENTER = 0.6
TRANSITION_LOW = 0.55
TRANSITION_HIGH = 0.65

MIN_VALUES_PER_GROUP = 3


def load_jsonl(path):
    rows = []

    if not path.exists():
        return rows

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue

            row["_source_file"] = path.name
            rows.append(row)

    return rows


def load_all_results(results_dir):
    rows = []

    if not results_dir.exists():
        return rows

    for path in sorted(results_dir.glob("*.jsonl")):
        rows.extend(load_jsonl(path))

    return rows


def extract_omega(row):
    for key in ["omega", "omega_score", "omega_mean"]:
        value = row.get(key)

        if isinstance(value, (int, float)):
            return float(value)

    return None


def classify_group(row):
    """
    Drift grouping priority:

    1. explicit time_window
    2. explicit version
    3. explicit seed
    4. source file
    """

    if row.get("time_window") is not None:
        return f"time_window:{row.get('time_window')}"

    if row.get("version") is not None:
        return f"version:{row.get('version')}"

    if row.get("seed") is not None:
        return f"seed:{row.get('seed')}"

    return f"source:{row.get('_source_file', 'unknown')}"


def summarize(values):
    if not values:
        return {
            "count": 0,
            "mean": None,
            "std": None,
            "min": None,
            "max": None,
            "distance_from_0_6": None,
            "transition_count": 0,
            "transition_rate": 0.0,
        }

    mean = statistics.mean(values)

    transition_count = sum(
        1 for v in values
        if TRANSITION_LOW <= v <= TRANSITION_HIGH
    )

    return {
        "count": len(values),
        "mean": mean,
        "std": statistics.pstdev(values),
        "min": min(values),
        "max": max(values),
        "distance_from_0_6": abs(mean - OMEGA_CENTER),
        "transition_count": transition_count,
        "transition_rate": transition_count / len(values),
    }


def classify_drift(group_summaries):
    means = [
        s["mean"]
        for s in group_summaries.values()
        if isinstance(s.get("mean"), (int, float))
    ]

    if len(means) < 2:
        return {
            "drift_class": "insufficient_groups",
            "drift_range": None,
            "mean_of_means": statistics.mean(means) if means else None,
        }

    drift_range = max(means) - min(means)

    if drift_range <= 0.05:
        drift_class = "low_drift"

    elif drift_range <= 0.15:
        drift_class = "moderate_drift"

    else:
        drift_class = "high_drift"

    return {
        "drift_class": drift_class,
        "drift_range": drift_range,
        "mean_of_means": statistics.mean(means),
        "min_group_mean": min(means),
        "max_group_mean": max(means),
    }


def ascii_bar(value, width=40):
    if value is None:
        return ""

    value = max(0.0, min(1.0, value))
    filled = int(value * width)

    return "#" * filled + "-" * (width - filled)


def main():
    rows = load_all_results(INPUT_RESULTS_DIR)

    grouped = defaultdict(list)

    for row in rows:
        omega = extract_omega(row)

        if omega is None:
            continue

        group = classify_group(row)
        grouped[group].append(omega)

    grouped = {
        group: values
        for group, values in grouped.items()
        if len(values) >= MIN_VALUES_PER_GROUP
    }

    group_summaries = {
        group: summarize(values)
        for group, values in sorted(grouped.items())
    }

    drift_summary = classify_drift(group_summaries)

    summary = {
        "omega_center": OMEGA_CENTER,
        "transition_region": [TRANSITION_LOW, TRANSITION_HIGH],
        "min_values_per_group": MIN_VALUES_PER_GROUP,
        "total_rows_loaded": len(rows),
        "groups": group_summaries,
        "drift_summary": drift_summary,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with SUMMARY_FILE.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    lines = []
    lines.append("=" * 80)
    lines.append("TRANSITION DRIFT ANALYSIS")
    lines.append("=" * 80)
    lines.append("")
    lines.append(json.dumps(drift_summary, indent=2))
    lines.append("")

    for group, stats in group_summaries.items():
        lines.append("-" * 80)
        lines.append(group)
        lines.append("-" * 80)
        lines.append(f"count: {stats['count']}")
        lines.append(f"mean Ω: {stats['mean']}")
        lines.append(f"std Ω: {stats['std']}")
        lines.append(f"distance from 0.6: {stats['distance_from_0_6']}")
        lines.append(f"transition rate: {stats['transition_rate']}")
        lines.append(f"transition bar: {ascii_bar(stats['transition_rate'])}")
        lines.append("")

    with ASCII_FILE.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("=" * 80)
    print("TRANSITION DRIFT ANALYSIS")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"ASCII report written to: {ASCII_FILE}")


if __name__ == "__main__":
    main()