#!/usr/bin/env python3
"""
Domain Separation Analysis · OMNIA-CONSTANT

Purpose:
    Test whether Ω distributions meaningfully separate domains.

Core question:

    Does Ω distinguish different structural regimes,
    or do all domains collapse into the same distribution?

This experiment compares Ω distributions across imported
OMNIA-INVARIANCE trajectory families.
"""

import json
import statistics
from pathlib import Path
from collections import defaultdict


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INPUT_RESULTS_DIR = Path(
    "imported_results/invariance"
)

OUTPUT_DIR = Path(
    "results/import_from_invariance"
)

SUMMARY_FILE = OUTPUT_DIR / "domain_separation_summary.json"
ASCII_FILE = OUTPUT_DIR / "domain_separation_ascii.txt"

OMEGA_CENTER = 0.6

MIN_VALUES_PER_DOMAIN = 5


# -------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------

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
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    return rows


def load_all_results(results_dir):
    rows = []

    if not results_dir.exists():
        return rows

    for path in sorted(results_dir.glob("*.jsonl")):
        loaded = load_jsonl(path)

        for row in loaded:
            row["_source_file"] = path.name

        rows.extend(loaded)

    return rows


def extract_omega(row):
    for key in ["omega", "omega_score", "omega_mean"]:
        value = row.get(key)

        if isinstance(value, (int, float)):
            return float(value)

    return None


def classify_domain(row):
    text = " ".join([
        str(row.get("domain", "")),
        str(row.get("experiment_name", "")),
        str(row.get("_source_file", "")),
    ]).lower()

    if "noise" in text or "random" in text:
        return "random"

    if "symbolic" in text:
        return "symbolic"

    if "graph" in text:
        return "graph"

    if "crypto" in text:
        return "crypto"

    if "financial" in text:
        return "financial"

    if "topology" in text:
        return "topology"

    if "chaotic" in text:
        return "chaotic"

    if "oscill" in text:
        return "oscillatory"

    if "persistent" in text:
        return "persistent"

    if "adversarial" in text:
        return "adversarial"

    return "unknown"


def summarize(values):
    if not values:
        return {
            "count": 0,
            "mean": None,
            "std": None,
            "min": None,
            "max": None,
        }

    return {
        "count": len(values),
        "mean": statistics.mean(values),
        "std": statistics.pstdev(values),
        "min": min(values),
        "max": max(values),
    }


def distribution_overlap(a_values, b_values):
    """
    Approximate overlap score using interval intersection.

    1.0 = identical interval
    0.0 = no overlap
    """

    if not a_values or not b_values:
        return None

    a_min = min(a_values)
    a_max = max(a_values)

    b_min = min(b_values)
    b_max = max(b_values)

    overlap_low = max(a_min, b_min)
    overlap_high = min(a_max, b_max)

    if overlap_high <= overlap_low:
        return 0.0

    overlap = overlap_high - overlap_low

    union_low = min(a_min, b_min)
    union_high = max(a_max, b_max)

    union = union_high - union_low

    if union == 0:
        return 1.0

    return overlap / union


def mean_distance(a_values, b_values):
    if not a_values or not b_values:
        return None

    return abs(
        statistics.mean(a_values)
        - statistics.mean(b_values)
    )


def variance_distance(a_values, b_values):
    if len(a_values) < 2 or len(b_values) < 2:
        return None

    return abs(
        statistics.pstdev(a_values)
        - statistics.pstdev(b_values)
    )


def classify_separation(overlap_score):
    if overlap_score is None:
        return "unknown"

    if overlap_score >= 0.8:
        return "weak_separation"

    if overlap_score >= 0.5:
        return "moderate_separation"

    return "strong_separation"


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

def main():
    rows = load_all_results(INPUT_RESULTS_DIR)

    grouped = defaultdict(list)

    for row in rows:
        omega = extract_omega(row)

        if omega is None:
            continue

        domain = classify_domain(row)

        grouped[domain].append(omega)

    # Filter small groups
    grouped = {
        k: v
        for k, v in grouped.items()
        if len(v) >= MIN_VALUES_PER_DOMAIN
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    summary = {
        "omega_center": OMEGA_CENTER,
        "domains": {},
        "pairwise_comparisons": [],
    }

    # ----------------------------------------------------------------
    # DOMAIN STATS
    # ----------------------------------------------------------------

    for domain, values in sorted(grouped.items()):
        summary["domains"][domain] = summarize(values)

    # ----------------------------------------------------------------
    # PAIRWISE COMPARISON
    # ----------------------------------------------------------------

    domains = sorted(grouped.keys())

    ascii_lines = []

    ascii_lines.append("=" * 80)
    ascii_lines.append("DOMAIN SEPARATION ANALYSIS")
    ascii_lines.append("=" * 80)
    ascii_lines.append("")

    for i in range(len(domains)):
        for j in range(i + 1, len(domains)):
            a = domains[i]
            b = domains[j]

            a_values = grouped[a]
            b_values = grouped[b]

            overlap = distribution_overlap(a_values, b_values)

            comparison = {
                "domain_a": a,
                "domain_b": b,
                "overlap_score": overlap,
                "mean_distance": mean_distance(a_values, b_values),
                "variance_distance": variance_distance(a_values, b_values),
                "separation_class": classify_separation(overlap),
            }

            summary["pairwise_comparisons"].append(comparison)

            ascii_lines.append("-" * 80)
            ascii_lines.append(f"{a} vs {b}")
            ascii_lines.append("-" * 80)

            ascii_lines.append(
                json.dumps(comparison, indent=2)
            )

            ascii_lines.append("")

    # ----------------------------------------------------------------
    # WRITE
    # ----------------------------------------------------------------

    with SUMMARY_FILE.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    with ASCII_FILE.open("w", encoding="utf-8") as f:
        f.write("\n".join(ascii_lines))

    print("=" * 80)
    print("DOMAIN SEPARATION ANALYSIS")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"ASCII report written to: {ASCII_FILE}")


if __name__ == "__main__":
    main()