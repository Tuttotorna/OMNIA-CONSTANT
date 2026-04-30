#!/usr/bin/env python3
"""
Band Sensitivity Analysis · OMNIA-CONSTANT

Purpose:
    Test how sensitive the Ω transition-region hypothesis is
    to the width of the selected Ω band.

Core question:

    Does Ω≈0.6 emerge because of a genuinely stable region,
    or only because the selected band is too wide?

This script analyzes imported Ω values from OMNIA-INVARIANCE
and compares multiple transition-band widths.
"""

import json
import statistics
from pathlib import Path
from collections import defaultdict


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INPUT_FILE = Path(
    "results/import_from_invariance/transition_region_summary.json"
)

INPUT_RESULTS_DIR = Path(
    "imported_results/invariance"
)

OUTPUT_DIR = Path(
    "results/import_from_invariance"
)

SUMMARY_FILE = OUTPUT_DIR / "band_sensitivity_summary.json"
ASCII_FILE = OUTPUT_DIR / "band_sensitivity_ascii.txt"

OMEGA_CENTER = 0.6

BANDS = [
    (0.59, 0.61),
    (0.575, 0.625),
    (0.55, 0.65),
    (0.50, 0.70),
    (0.40, 0.80),
]


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


def summarize_band(values, low, high):
    if not values:
        return {
            "count": 0,
            "inside_band": 0,
            "inside_rate": 0.0,
        }

    inside = [
        v for v in values
        if low <= v <= high
    ]

    return {
        "count": len(values),
        "inside_band": len(inside),
        "inside_rate": len(inside) / len(values),
        "mean": statistics.mean(values),
        "std": statistics.pstdev(values),
    }


def ascii_bar(rate, width=40):
    filled = int(rate * width)
    return "#" * filled + "-" * (width - filled)


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

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    overall_values = []

    for values in grouped.values():
        overall_values.extend(values)

    summary = {
        "omega_center": OMEGA_CENTER,
        "bands": {},
        "domains": {},
    }

    ascii_lines = []

    ascii_lines.append("=" * 80)
    ascii_lines.append("BAND SENSITIVITY ANALYSIS")
    ascii_lines.append("=" * 80)
    ascii_lines.append("")

    # ----------------------------------------------------------------
    # OVERALL
    # ----------------------------------------------------------------

    summary["overall"] = {}

    ascii_lines.append("OVERALL")
    ascii_lines.append("-" * 80)

    for low, high in BANDS:
        band_name = f"{low:.3f}-{high:.3f}"

        stats = summarize_band(overall_values, low, high)

        summary["overall"][band_name] = stats

        rate = stats["inside_rate"]

        ascii_lines.append(
            f"{band_name} | "
            f"{ascii_bar(rate)} "
            f"{rate:.4f}"
        )

    ascii_lines.append("")
    ascii_lines.append("")

    # ----------------------------------------------------------------
    # DOMAINS
    # ----------------------------------------------------------------

    for domain, values in sorted(grouped.items()):
        summary["domains"][domain] = {}

        ascii_lines.append("=" * 80)
        ascii_lines.append(f"DOMAIN: {domain}")
        ascii_lines.append("=" * 80)

        for low, high in BANDS:
            band_name = f"{low:.3f}-{high:.3f}"

            stats = summarize_band(values, low, high)

            summary["domains"][domain][band_name] = stats

            rate = stats["inside_rate"]

            ascii_lines.append(
                f"{band_name} | "
                f"{ascii_bar(rate)} "
                f"{rate:.4f}"
            )

        ascii_lines.append("")
        ascii_lines.append("")

    # ----------------------------------------------------------------
    # WRITE
    # ----------------------------------------------------------------

    with SUMMARY_FILE.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    with ASCII_FILE.open("w", encoding="utf-8") as f:
        f.write("\n".join(ascii_lines))

    print("=" * 80)
    print("BAND SENSITIVITY ANALYSIS")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"ASCII report written to: {ASCII_FILE}")


if __name__ == "__main__":
    main()