#!/usr/bin/env python3
"""
Filtered Discovery Scan · OMNIA-CONSTANT

Purpose:
    Extract only canonical Ω fields from existing
    OMNIA-INVARIANCE outputs.

This scan intentionally excludes derived metrics such as:

    - omega_volatility
    - nearest_distance
    - embedding_pc1
    - embedding_pc2
    - variance
    - std

Goal:
    determine whether the Ω≈0.6 region persists
    when only canonical Ω measurements are analyzed.
"""

import json
import statistics
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INPUT_DIR = Path("imported_results/invariance")

OUTPUT_DIR = Path("results")

SUMMARY_FILE = OUTPUT_DIR / "FILTERED_DISCOVERY_SCAN.json"
REPORT_FILE = OUTPUT_DIR / "FILTERED_DISCOVERY_SCAN.md"

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
                        "value": float(v),
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

    results = []

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
                    results,
                )

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
        "canonical_omega_count": len(omega_values),
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

    lines.append("# Filtered Discovery Scan")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(summary, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Canonical Ω Hits")
    lines.append("")

    for r in results:
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
    print("FILTERED DISCOVERY SCAN")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"Report written to: {REPORT_FILE}")


if __name__ == "__main__":
    main()