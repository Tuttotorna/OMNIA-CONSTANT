#!/usr/bin/env python3
"""
Duplicate-Aware Scan · OMNIA-CONSTANT

Purpose:
    Re-run the filtered Ω discovery scan while attempting
    to remove duplicated or repeated exported values.

Goal:
    determine whether the Ω≈0.6 candidate region survives
    after duplicate reduction.
"""

import json
import statistics
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INPUT_DIR = Path("imported_results/invariance")

OUTPUT_DIR = Path("results")

SUMMARY_FILE = OUTPUT_DIR / "DUPLICATE_AWARE_SCAN.json"
REPORT_FILE = OUTPUT_DIR / "DUPLICATE_AWARE_SCAN.md"

TRANSITION_LOW = 0.55
TRANSITION_HIGH = 0.65

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


def walk(obj, source, results, path=""):
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
                    results.append({
                        "value": round(float(v), 6),
                        "key": k,
                        "path": key_path,
                        "source": source,
                    })

            walk(v, source, results, key_path)

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            walk(
                item,
                source,
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

    raw_results = []

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
                walk(
                    row,
                    str(path.relative_to(INPUT_DIR)),
                    raw_results,
                )

    # ---------------------------------------------------------------
    # DUPLICATE REDUCTION
    # ---------------------------------------------------------------

    unique_values = {}
    duplicate_count = 0

    for r in raw_results:
        value_key = f"{r['value']:.6f}"

        if value_key not in unique_values:
            unique_values[value_key] = r
        else:
            duplicate_count += 1

    results = list(unique_values.values())

    omega_values = [
        r["value"]
        for r in results
    ]

    transition_values = [
        v for v in omega_values
        if TRANSITION_LOW <= v <= TRANSITION_HIGH
    ]

    summary = {
        "scanned_files": scanned_files,
        "raw_canonical_omega_count": len(raw_results),
        "unique_canonical_omega_count": len(omega_values),
        "duplicate_count_removed": duplicate_count,
        "transition_band": [
            TRANSITION_LOW,
            TRANSITION_HIGH,
        ],
        "transition_count": len(transition_values),
        "transition_rate": (
            len(transition_values) / len(omega_values)
            if omega_values else 0.0
        ),
    }

    if omega_values:
        summary.update({
            "omega_mean": statistics.mean(omega_values),
            "omega_std": statistics.pstdev(omega_values),
            "omega_min": min(omega_values),
            "omega_max": max(omega_values),
        })

    with SUMMARY_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(summary, f, indent=2)

    lines = []

    lines.append("# Duplicate-Aware Scan")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(summary, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Unique Canonical Ω Values")
    lines.append("")

    for r in sorted(results, key=lambda x: x["value"]):
        marker = ""

        if (
            TRANSITION_LOW
            <= r["value"]
            <= TRANSITION_HIGH
        ):
            marker = "  <-- transition band"

        lines.append(
            f"- {r['value']:.6f} | "
            f"{r['source']} | "
            f"{r['path']}{marker}"
        )

    with REPORT_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        f.write("\n".join(lines))

    print("=" * 80)
    print("DUPLICATE-AWARE SCAN")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"Report written to: {REPORT_FILE}")


if __name__ == "__main__":
    main()