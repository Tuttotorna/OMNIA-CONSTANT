#!/usr/bin/env python3
"""
Narrow-Band Sensitivity Scan · OMNIA-CONSTANT

Purpose:
    Measure how long the Ω candidate region survives
    as the transition band progressively narrows.

Goal:
    determine whether Ω≈0.6 behaves like:

        - broad statistical region
        - narrow persistence band
        - sharp singularity
"""

import json
import statistics
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INPUT_DIR = Path("imported_results/invariance")

OUTPUT_DIR = Path("results")

SUMMARY_FILE = OUTPUT_DIR / "NARROW_BAND_SENSITIVITY_SCAN.json"
REPORT_FILE = OUTPUT_DIR / "NARROW_BAND_SENSITIVITY_SCAN.md"

ALLOWED_KEYS = {
    "mean_omega",
    "mean_Omega",
    "omega_score",
    "omega",
}

EXCLUDED_PATTERNS = [
    "volatility",
    "distance",
    "embedding",
    "variance",
    "std",
]

# progressively narrower windows
BANDS = [
    (0.55, 0.65),
    (0.58, 0.64),
    (0.59, 0.65),
    (0.60, 0.65),
    (0.60, 0.64),
    (0.61, 0.63),
]


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

    # Try JSON
    try:
        rows.append(json.loads(text))
        return rows
    except Exception:
        pass

    # Try JSONL
    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        try:
            rows.append(json.loads(line))
        except Exception:
            pass

    return rows


def is_excluded(key):
    key_lower = key.lower()

    return any(
        pattern in key_lower
        for pattern in EXCLUDED_PATTERNS
    )


def walk(obj, results, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            key_path = f"{path}.{k}" if path else k

            if isinstance(v, (int, float)):

                key_lower = k.lower()

                allowed = (
                    k in ALLOWED_KEYS
                    or key_lower in {
                        x.lower()
                        for x in ALLOWED_KEYS
                    }
                )

                if allowed and not is_excluded(k):
                    results.append(round(float(v), 6))

            walk(v, results, key_path)

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            walk(
                item,
                results,
                f"{path}[{i}]",
            )


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

def main():
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    raw_values = []

    scanned_files = 0

    for path in INPUT_DIR.rglob("*"):
        if (
            path.is_file()
            and path.suffix.lower()
            in [".json", ".jsonl"]
        ):
            scanned_files += 1

            rows = load_json_or_jsonl(path)

            for row in rows:
                walk(row, raw_values)

    # remove duplicates
    omega_values = sorted(set(raw_values))

    summary = {
        "scanned_files": scanned_files,
        "unique_omega_count": len(omega_values),
        "omega_values": omega_values,
        "omega_mean": (
            statistics.mean(omega_values)
            if omega_values else None
        ),
        "omega_std": (
            statistics.pstdev(omega_values)
            if len(omega_values) > 1 else 0.0
        ),
        "bands": [],
    }

    previous_rate = None

    for low, high in BANDS:

        surviving = [
            v for v in omega_values
            if low <= v <= high
        ]

        rate = (
            len(surviving) / len(omega_values)
            if omega_values else 0.0
        )

        dropped = [
            v for v in omega_values
            if v not in surviving
        ]

        band_result = {
            "band": [low, high],
            "surviving_count": len(surviving),
            "transition_rate": rate,
            "surviving_values": surviving,
            "dropped_values": dropped,
        }

        if previous_rate is not None:
            band_result["rate_delta"] = (
                rate - previous_rate
            )

        previous_rate = rate

        summary["bands"].append(band_result)

    # ---------------------------------------------------------------
    # WRITE FILES
    # ---------------------------------------------------------------

    with SUMMARY_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(summary, f, indent=2)

    lines = []

    lines.append("# Narrow-Band Sensitivity Scan")
    lines.append("")
    lines.append("## Global Summary")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(summary, indent=2))
    lines.append("```")
    lines.append("")

    lines.append("## Band Results")
    lines.append("")

    for band in summary["bands"]:

        lines.append(
            f"### Band {band['band'][0]} – {band['band'][1]}"
        )
        lines.append("")

        lines.append("```json")
        lines.append(json.dumps(band, indent=2))
        lines.append("```")
        lines.append("")

    with REPORT_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        f.write("\n".join(lines))

    print("=" * 80)
    print("NARROW-BAND SENSITIVITY SCAN")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"Report written to: {REPORT_FILE}")


if __name__ == "__main__":
    main()