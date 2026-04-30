#!/usr/bin/env python3
"""
Ω Distribution Map · OMNIA-CONSTANT

Purpose:
    Visualize and summarize Ω distributions across baseline classes.

This script reads JSONL experiment outputs from:

    results/controlled_destruction/

and produces:

    results/controlled_destruction/omega_distribution_summary.json
    results/controlled_destruction/omega_distribution_ascii.txt

Optional future extension:
    add matplotlib histogram export.
"""

import json
import statistics
from pathlib import Path
from collections import defaultdict


INPUT_DIR = Path("results/controlled_destruction")
SUMMARY_FILE = INPUT_DIR / "omega_distribution_summary.json"
ASCII_FILE = INPUT_DIR / "omega_distribution_ascii.txt"

OMEGA_MIN = 0.0
OMEGA_MAX = 1.0
BIN_SIZE = 0.05
OMEGA_TARGET = 0.6
TARGET_LOW = 0.55
TARGET_HIGH = 0.65


def load_jsonl_files(input_dir):
    rows = []

    if not input_dir.exists():
        return rows

    for path in sorted(input_dir.glob("*.jsonl")):
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


def extract_omega_values(row):
    if isinstance(row.get("omega_values"), list):
        return [float(v) for v in row["omega_values"] if isinstance(v, (int, float))]

    if isinstance(row.get("omega_mean"), (int, float)):
        return [float(row["omega_mean"])]

    return []


def classify_row(row):
    domain = str(row.get("domain", "")).lower()
    attack_type = str(row.get("attack_type", "")).lower()
    source = str(row.get("_source_file", "")).lower()

    text = f"{domain} {attack_type} {source}"

    if "noise" in text or "random" in text:
        return "D0_random_distribution"

    if "mixed" in text or "structure_noise" in text:
        return "D2_transition_distribution"

    if "adversarial" in text or "false" in text or "pseudo" in text:
        return "D4_adversarial_false_persistence"

    if "persistent" in text or "recursive" in text or "stable" in text:
        return "D3_strong_persistence_distribution"

    if "weak" in text:
        return "D1_weak_persistence_distribution"

    return "D_unknown"


def make_bins():
    bins = []
    x = OMEGA_MIN

    while x < OMEGA_MAX:
        low = round(x, 2)
        high = round(min(x + BIN_SIZE, OMEGA_MAX), 2)
        bins.append((low, high))
        x += BIN_SIZE

    return bins


def bin_index(value, bins):
    for i, (low, high) in enumerate(bins):
        if low <= value < high:
            return i

    if value == OMEGA_MAX:
        return len(bins) - 1

    return None


def histogram(values, bins):
    counts = [0 for _ in bins]

    for value in values:
        idx = bin_index(value, bins)
        if idx is not None:
            counts[idx] += 1

    return counts


def summarize_values(values):
    if not values:
        return {
            "count": 0,
            "mean": None,
            "std": None,
            "min": None,
            "max": None,
            "target_band_count": 0,
            "target_band_rate": 0.0,
        }

    target_count = sum(1 for v in values if TARGET_LOW <= v <= TARGET_HIGH)

    return {
        "count": len(values),
        "mean": statistics.mean(values),
        "std": statistics.pstdev(values),
        "min": min(values),
        "max": max(values),
        "target_band_count": target_count,
        "target_band_rate": target_count / len(values),
    }


def ascii_histogram(label, values, bins):
    counts = histogram(values, bins)
    max_count = max(counts) if counts else 0

    lines = []
    lines.append("=" * 80)
    lines.append(label)
    lines.append("=" * 80)

    summary = summarize_values(values)
    lines.append(json.dumps(summary, indent=2, ensure_ascii=False))
    lines.append("")

    if max_count == 0:
        lines.append("(no values)")
        return "\n".join(lines)

    for (low, high), count in zip(bins, counts):
        bar_len = int((count / max_count) * 40) if max_count else 0
        bar = "#" * bar_len
        marker = " <== Ω≈0.6 band" if low <= OMEGA_TARGET < high or TARGET_LOW <= low <= TARGET_HIGH else ""

        lines.append(f"{low:0.2f}-{high:0.2f} | {bar} {count}{marker}")

    return "\n".join(lines)


def main():
    rows = load_jsonl_files(INPUT_DIR)
    bins = make_bins()

    grouped = defaultdict(list)

    for row in rows:
        group = classify_row(row)
        grouped[group].extend(extract_omega_values(row))

    all_values = []
    for values in grouped.values():
        all_values.extend(values)

    summary = {
        "omega_target": OMEGA_TARGET,
        "target_band": [TARGET_LOW, TARGET_HIGH],
        "bin_size": BIN_SIZE,
        "total_rows_loaded": len(rows),
        "total_omega_values": len(all_values),
        "overall": summarize_values(all_values),
        "groups": {
            group: summarize_values(values)
            for group, values in sorted(grouped.items())
        },
    }

    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    with SUMMARY_FILE.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    ascii_sections = []
    ascii_sections.append(ascii_histogram("OVERALL Ω DISTRIBUTION", all_values, bins))

    for group, values in sorted(grouped.items()):
        ascii_sections.append(ascii_histogram(group, values, bins))

    with ASCII_FILE.open("w", encoding="utf-8") as f:
        f.write("\n\n".join(ascii_sections))

    print("=" * 80)
    print("Ω DISTRIBUTION MAP")
    print("=" * 80)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"ASCII map written to: {ASCII_FILE}")


if __name__ == "__main__":
    main()