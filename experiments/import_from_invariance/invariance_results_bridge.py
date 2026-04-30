
#!/usr/bin/env python3
"""
OMNIA-INVARIANCE Results Bridge · OMNIA-CONSTANT

Purpose:
    Import trajectory-space experiment results from OMNIA-INVARIANCE,
    extract Ω values,
    compare distributions across domains,
    and analyze the Ω transition region.

This script does NOT prove a structural constant.

It tests whether a transition region repeatedly emerges
across imported trajectory families.
"""

import json
import statistics
from pathlib import Path
from collections import defaultdict


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INVARIANCE_RESULTS_DIR = Path("imported_results/invariance")
OUTPUT_DIR = Path("results/import_from_invariance")

SUMMARY_FILE = OUTPUT_DIR / "transition_region_summary.json"
ASCII_FILE = OUTPUT_DIR / "transition_region_ascii.txt"

OMEGA_TARGET = 0.6
TRANSITION_LOW = 0.55
TRANSITION_HIGH = 0.65

BIN_SIZE = 0.05


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
    """
    Flexible Ω extraction.

    Accepts:
    - omega
    - omega_score
    - omega_mean
    """

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


def make_bins():
    bins = []

    x = 0.0

    while x < 1.0:
        low = round(x, 2)
        high = round(x + BIN_SIZE, 2)

        bins.append((low, high))

        x += BIN_SIZE

    return bins


def histogram(values, bins):
    counts = [0 for _ in bins]

    for value in values:
        for i, (low, high) in enumerate(bins):
            if low <= value < high:
                counts[i] += 1
                break

    return counts


def summarize(values):
    if not values:
        return {
            "count": 0,
            "mean": None,
            "std": None,
            "transition_count": 0,
            "transition_rate": 0.0,
        }

    transition_count = sum(
        1 for v in values
        if TRANSITION_LOW <= v <= TRANSITION_HIGH
    )

    return {
        "count": len(values),
        "mean": statistics.mean(values),
        "std": statistics.pstdev(values),
        "min": min(values),
        "max": max(values),
        "transition_count": transition_count,
        "transition_rate": transition_count / len(values),
    }


def ascii_histogram(label, values, bins):
    lines = []

    lines.append("=" * 80)
    lines.append(label)
    lines.append("=" * 80)

    stats = summarize(values)

    lines.append(json.dumps(stats, indent=2))
    lines.append("")

    counts = histogram(values, bins)
    max_count = max(counts) if counts else 0

    for (low, high), count in zip(bins, counts):
        if max_count > 0:
            bar_len = int((count / max_count) * 40)
        else:
            bar_len = 0

        bar = "#" * bar_len

        marker = ""

        if (
            TRANSITION_LOW <= low <= TRANSITION_HIGH
            or TRANSITION_LOW <= high <= TRANSITION_HIGH
        ):
            marker = " <== transition region"

        lines.append(
            f"{low:0.2f}-{high:0.2f} | {bar} {count}{marker}"
        )

    return "\n".join(lines)


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

def main():
    rows = load_all_results(INVARIANCE_RESULTS_DIR)

    grouped = defaultdict(list)

    for row in rows:
        omega = extract_omega(row)

        if omega is None:
            continue

        domain = classify_domain(row)

        grouped[domain].append(omega)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    bins = make_bins()

    overall_values = []

    for values in grouped.values():
        overall_values.extend(values)

    summary = {
        "omega_target": OMEGA_TARGET,
        "transition_region": [
            TRANSITION_LOW,
            TRANSITION_HIGH,
        ],
        "total_rows": len(rows),
        "total_omega_values": len(overall_values),
        "overall": summarize(overall_values),
        "domains": {
            domain: summarize(values)
            for domain, values in sorted(grouped.items())
        },
    }

    with SUMMARY_FILE.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    ascii_sections = []

    ascii_sections.append(
        ascii_histogram(
            "OVERALL TRANSITION REGION MAP",
            overall_values,
            bins,
        )
    )

    for domain, values in sorted(grouped.items()):
        ascii_sections.append(
            ascii_histogram(
                f"DOMAIN: {domain}",
                values,
                bins,
            )
        )

    with ASCII_FILE.open("w", encoding="utf-8") as f:
        f.write("\n\n".join(ascii_sections))

    print("=" * 80)
    print("OMNIA-INVARIANCE TRANSITION REGION ANALYSIS")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"ASCII map written to: {ASCII_FILE}")


if __name__ == "__main__":
    main()