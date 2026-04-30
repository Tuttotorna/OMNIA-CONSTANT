#!/usr/bin/env python3
"""
Cross-Metric Independence Test · OMNIA-CONSTANT

Purpose:
    Test whether the observed Ω≈0.62 persistence band is specific
    to mean_omega, or whether comparable structural concentration
    appears under independent trajectory metrics.

Core question:
    Does the candidate region emerge from the phenomenon,
    or from the mean_omega metric itself?
"""

import json
import math
import statistics
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INPUT_DIR = Path("imported_results/invariance")

OUTPUT_DIR = Path("results")

SUMMARY_FILE = OUTPUT_DIR / "CROSS_METRIC_INDEPENDENCE_TEST.json"
REPORT_FILE = OUTPUT_DIR / "CROSS_METRIC_INDEPENDENCE_TEST.md"

OBSERVED_LOW = 0.598
OBSERVED_HIGH = 0.644681

CORE_LOW = 0.610
CORE_HIGH = 0.619048


# -------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------

def load_json_or_jsonl(path):
    rows = []

    text = path.read_text(
        encoding="utf-8",
        errors="ignore",
    ).strip()

    if not text:
        return rows

    try:
        rows.append(json.loads(text))
        return rows
    except Exception:
        pass

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        try:
            rows.append(json.loads(line))
        except Exception:
            pass

    return rows


def find_omega_trajectories(obj, source, found, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            key_path = f"{path}.{k}" if path else k

            if k == "omega_trajectory" and isinstance(v, list):
                values = [
                    float(x)
                    for x in v
                    if isinstance(x, (int, float))
                ]

                if values:
                    found.append({
                        "source": source,
                        "path": key_path,
                        "omega_trajectory": values,
                    })

            find_omega_trajectories(
                v,
                source,
                found,
                key_path,
            )

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            find_omega_trajectories(
                item,
                source,
                found,
                f"{path}[{i}]",
            )


def clamp01(x):
    return max(0.0, min(1.0, x))


def safe_std(values):
    if len(values) < 2:
        return 0.0

    return statistics.pstdev(values)


def normalize_range(values):
    if not values:
        return []

    lo = min(values)
    hi = max(values)

    if hi == lo:
        return [0.5 for _ in values]

    return [
        (v - lo) / (hi - lo)
        for v in values
    ]


# -------------------------------------------------------------------
# INDEPENDENT METRICS
# -------------------------------------------------------------------

def mean_omega(values):
    return clamp01(statistics.mean(values))


def variance_stability(values):
    """
    Higher when the trajectory has lower variance.
    """

    std = safe_std(values)

    return clamp01(1.0 - std)


def range_stability(values):
    """
    Higher when min-max range is narrow.
    """

    if not values:
        return 0.0

    r = max(values) - min(values)

    return clamp01(1.0 - r)


def smoothness_score(values):
    """
    Higher when adjacent jumps are small.
    """

    if len(values) < 2:
        return 1.0

    jumps = [
        abs(values[i] - values[i - 1])
        for i in range(1, len(values))
    ]

    mean_jump = statistics.mean(jumps)

    return clamp01(1.0 - mean_jump)


def entropy_stability(values, bins=5):
    """
    Higher when distribution entropy is lower.
    """

    if not values:
        return 0.0

    normalized = normalize_range(values)

    counts = [0 for _ in range(bins)]

    for v in normalized:
        idx = min(
            bins - 1,
            int(v * bins),
        )
        counts[idx] += 1

    total = sum(counts)

    if total == 0:
        return 0.0

    entropy = 0.0

    for c in counts:
        if c == 0:
            continue

        p = c / total
        entropy -= p * math.log(p, 2)

    max_entropy = math.log(bins, 2)

    if max_entropy == 0:
        return 1.0

    normalized_entropy = entropy / max_entropy

    return clamp01(1.0 - normalized_entropy)


def compression_stability(values):
    """
    Approximate compressibility using repeated rounded values
    and local difference simplicity.

    Higher = more compressible / less structurally noisy.
    """

    if not values:
        return 0.0

    rounded = [
        round(v, 2)
        for v in values
    ]

    unique_ratio = len(set(rounded)) / len(rounded)

    if len(values) < 2:
        jump_complexity = 0.0
    else:
        jumps = [
            round(abs(values[i] - values[i - 1]), 2)
            for i in range(1, len(values))
        ]

        jump_complexity = len(set(jumps)) / len(jumps)

    complexity = (
        0.5 * unique_ratio
        + 0.5 * jump_complexity
    )

    return clamp01(1.0 - complexity)


METRICS = {
    "mean_omega": mean_omega,
    "variance_stability": variance_stability,
    "range_stability": range_stability,
    "smoothness_score": smoothness_score,
    "entropy_stability": entropy_stability,
    "compression_stability": compression_stability,
}


# -------------------------------------------------------------------
# ANALYSIS
# -------------------------------------------------------------------

def summarize_metric(name, values):
    candidate_hits = [
        v for v in values
        if OBSERVED_LOW <= v <= OBSERVED_HIGH
    ]

    core_hits = [
        v for v in values
        if CORE_LOW <= v <= CORE_HIGH
    ]

    summary = {
        "metric": name,
        "count": len(values),
        "candidate_band": [
            OBSERVED_LOW,
            OBSERVED_HIGH,
        ],
        "candidate_hits": len(candidate_hits),
        "candidate_rate": (
            len(candidate_hits) / len(values)
            if values else 0.0
        ),
        "core_band": [
            CORE_LOW,
            CORE_HIGH,
        ],
        "core_hits": len(core_hits),
        "core_rate": (
            len(core_hits) / len(values)
            if values else 0.0
        ),
    }

    if values:
        summary.update({
            "mean": statistics.mean(values),
            "std": safe_std(values),
            "min": min(values),
            "max": max(values),
            "values": values,
        })

    return summary


def classify_result(metric_summary):
    rate = metric_summary["candidate_rate"]

    if rate >= 0.75:
        return "strong_alignment"

    if rate >= 0.40:
        return "partial_alignment"

    if rate >= 0.15:
        return "weak_alignment"

    return "no_alignment"


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

def main():
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    trajectories = []

    scanned_files = 0

    for path in INPUT_DIR.rglob("*"):
        if (
            path.is_file()
            and path.suffix.lower() in [".json", ".jsonl"]
        ):
            scanned_files += 1

            rows = load_json_or_jsonl(path)

            for row in rows:
                find_omega_trajectories(
                    row,
                    str(path.relative_to(INPUT_DIR)),
                    trajectories,
                )

    metric_values = {
        name: []
        for name in METRICS
    }

    per_trajectory = []

    for item in trajectories:
        values = item["omega_trajectory"]

        row = {
            "source": item["source"],
            "path": item["path"],
            "trajectory": values,
            "metrics": {},
        }

        for metric_name, metric_func in METRICS.items():
            score = round(
                float(metric_func(values)),
                6,
            )

            metric_values[metric_name].append(score)
            row["metrics"][metric_name] = score

        per_trajectory.append(row)

    metric_summaries = {}

    for name, values in metric_values.items():
        summary = summarize_metric(name, values)
        summary["alignment_class"] = classify_result(summary)
        metric_summaries[name] = summary

    summary = {
        "scanned_files": scanned_files,
        "trajectory_count": len(trajectories),
        "candidate_band": [
            OBSERVED_LOW,
            OBSERVED_HIGH,
        ],
        "core_band": [
            CORE_LOW,
            CORE_HIGH,
        ],
        "metric_summaries": metric_summaries,
        "per_trajectory": per_trajectory,
    }

    with SUMMARY_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(summary, f, indent=2)

    lines = []

    lines.append("# Cross-Metric Independence Test")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "Test whether the Ω≈0.62 candidate band is specific to mean_omega "
        "or appears under independent trajectory metrics."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- scanned files: {scanned_files}")
    lines.append(f"- trajectory count: {len(trajectories)}")
    lines.append(f"- candidate band: {OBSERVED_LOW} – {OBSERVED_HIGH}")
    lines.append(f"- core band: {CORE_LOW} – {CORE_HIGH}")
    lines.append("")

    for name, metric_summary in metric_summaries.items():
        lines.append(f"## Metric: {name}")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(metric_summary, indent=2))
        lines.append("```")
        lines.append("")

    lines.append("## Per-Trajectory Metrics")
    lines.append("")

    for row in per_trajectory:
        lines.append(f"### {row['source']} · {row['path']}")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(row, indent=2))
        lines.append("```")
        lines.append("")

    with REPORT_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        f.write("\n".join(lines))

    print("=" * 80)
    print("CROSS-METRIC INDEPENDENCE TEST")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f