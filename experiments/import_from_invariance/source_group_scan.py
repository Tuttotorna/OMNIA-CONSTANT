#!/usr/bin/env python3
"""
Source Group Scan · OMNIA-CONSTANT

Purpose:
    Determine whether the Ω≈0.6 candidate region
    appears across independent source groups.

Goal:
    distinguish:
        repeated exports
    from:
        independent structural domains.
"""

import json
import statistics
from pathlib import Path
from collections import defaultdict


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

INPUT_DIR = Path("imported_results/invariance")

OUTPUT_DIR = Path("results")

SUMMARY_FILE = OUTPUT_DIR / "SOURCE_GROUP_SCAN.json"
REPORT_FILE = OUTPUT_DIR / "SOURCE_GROUP_SCAN.md"

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


def classify_source_group(path_str):
    text = path_str.lower()

    if "physics" in text:
        return "physics"

    if "logic" in text:
        return "logic"

    if "finance" in text:
        return "finance"

    if "crypto" in text:
        return "crypto"

    if "llm" in text:
        return "llm"

    if "trajectory" in text:
        return "trajectory"

    if "cross_domain" in text:
        return "cross_domain"

    return "unknown"


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
                        "group": classify_source_group(source),
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
    # GROUP REDUCTION
    # ---------------------------------------------------------------

    grouped = defaultdict(list)

    for r in raw_results:
        grouped[r["group"]].append(r["value"])

    summary_groups = {}

    for group, values in grouped.items():

        unique_values = sorted(set(values))

        transition_values = [
            v for v in unique_values
            if TRANSITION_LOW <= v <= TRANSITION_HIGH
        ]

        summary_groups[group] = {
            "unique_count": len(unique_values),
            "transition_count": len(transition_values),
            "transition_rate": (
                len(transition_values) / len(unique_values)
                if unique_values else 0.0
            ),
            "omega_mean": (
                statistics.mean(unique_values)
                if unique_values else None
            ),
            "omega_std": (
                statistics.pstdev(unique_values)
                if len(unique_values) > 1 else 0.0
            ),
            "omega_min": (
                min(unique_values)
                if unique_values else None
            ),
            "omega_max": (
                max(unique_values)
                if unique_values else None
            ),
            "values": unique_values,
        }

    # ---------------------------------------------------------------
    # GLOBAL SUMMARY
    # ---------------------------------------------------------------

    all_unique = sorted(set(
        r["value"]
        for r in raw_results
    ))

    transition_values = [
        v for v in all_unique
        if TRANSITION_LOW <= v <= TRANSITION_HIGH
    ]

    summary = {
        "scanned_files": scanned_files,
        "unique_global_omega_count": len(all_unique),
        "transition_band": [
            TRANSITION_LOW,
            TRANSITION_HIGH,
        ],
        "transition_count": len(transition_values),
        "transition_rate": (
            len(transition_values) / len(all_unique)
            if all_unique else 0.0
        ),
        "omega_mean": (
            statistics.mean(all_unique)
            if all_unique else None
        ),
        "omega_std": (
            statistics.pstdev(all_unique)
            if len(all_unique) > 1 else 0.0
        ),
        "omega_min": (
            min(all_unique)
            if all_unique else None
        ),
        "omega_max": (
            max(all_unique)
            if all_unique else None
        ),
        "source_groups": summary_groups,
    }

    # ---------------------------------------------------------------
    # WRITE FILES
    # ---------------------------------------------------------------

    with SUMMARY_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(summary, f, indent=2)

    lines = []

    lines.append("# Source Group Scan")
    lines.append("")
    lines.append("## Global Summary")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(summary, indent=2))
    lines.append("```")
    lines.append("")

    lines.append("## Source Groups")
    lines.append("")

    for group, stats in sorted(summary_groups.items()):
        lines.append(f"### {group}")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(stats, indent=2))
        lines.append("```")
        lines.append("")

    with REPORT_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        f.write("\n".join(lines))

    print("=" * 80)
    print("SOURCE GROUP SCAN")
    print("=" * 80)
    print(json.dumps(summary, indent=2))
    print()
    print(f"Summary written to: {SUMMARY_FILE}")
    print(f"Report written to: {REPORT_FILE}")


if __name__ == "__main__":
    main()