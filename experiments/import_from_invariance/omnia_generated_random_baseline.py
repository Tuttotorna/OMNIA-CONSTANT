#!/usr/bin/env python3
"""
OMNIA-Generated Random Baseline · OMNIA-CONSTANT

Purpose:
    Generate random systems and push them through
    the same OMNIA / INVARIANCE scoring path used
    by real datasets.

Goal:
    determine whether the observed Ω candidate band:

        0.598 ≤ Ω ≤ 0.644681

    naturally emerges from random systems.
"""

import json
import random
import statistics
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

OUTPUT_DIR = Path("results")

SUMMARY_FILE = (
    OUTPUT_DIR
    / "OMNIA_GENERATED_RANDOM_BASELINE.json"
)

REPORT_FILE = (
    OUTPUT_DIR
    / "OMNIA_GENERATED_RANDOM_BASELINE.md"
)

NUM_RANDOM_SYSTEMS = 1000

RANDOM_SEED = 42

# observed candidate band
OBSERVED_LOW = 0.598
OBSERVED_HIGH = 0.644681

# observed core
CORE_LOW = 0.610
CORE_HIGH = 0.619048


# -------------------------------------------------------------------
# RANDOM SYSTEM GENERATORS
# -------------------------------------------------------------------

def random_sequence():
    return [
        random.random()
        for _ in range(128)
    ]


def random_binary():
    return [
        random.randint(0, 1)
        for _ in range(128)
    ]


def random_walk():
    x = 0.5

    values = []

    for _ in range(128):
        x += random.uniform(-0.1, 0.1)

        x = max(0.0, min(1.0, x))

        values.append(x)

    return values


# -------------------------------------------------------------------
# PLACEHOLDER OMNIA SCORE
# -------------------------------------------------------------------

def omnia_like_score(values):
    """
    IMPORTANT:

    Replace this placeholder with the real
    OMNIA / INVARIANCE scoring pipeline.

    Current version is only structural bootstrap logic.
    """

    mean = statistics.mean(values)

    std = statistics.pstdev(values)

    stability = 1.0 - min(std, 1.0)

    omega = (
        0.7 * mean
        + 0.3 * stability
    )

    return max(
        0.0,
        min(1.0, omega),
    )


# -------------------------------------------------------------------
# ANALYSIS
# -------------------------------------------------------------------

def analyze_scores(name, scores):

    observed_hits = [
        s for s in scores
        if OBSERVED_LOW <= s <= OBSERVED_HIGH
    ]

    core_hits = [
        s for s in scores
        if CORE_LOW <= s <= CORE_HIGH
    ]

    return {
        "distribution": name,
        "sample_count": len(scores),

        "omega_mean": statistics.mean(scores),
        "omega_std": statistics.pstdev(scores),

        "omega_min": min(scores),
        "omega_max": max(scores),

        "observed_band_hits": len(observed_hits),

        "observed_band_rate": (
            len(observed_hits) / len(scores)
        ),

        "core_band_hits": len(core_hits),

        "core_band_rate": (
            len(core_hits) / len(scores)
        ),
    }


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    random.seed(RANDOM_SEED)

    # ---------------------------------------------------------------
    # GENERATE RANDOM SYSTEMS
    # ---------------------------------------------------------------

    sequence_scores = []

    binary_scores = []

    walk_scores = []

    for _ in range(NUM_RANDOM_SYSTEMS):

        sequence_scores.append(
            omnia_like_score(
                random_sequence()
            )
        )

        binary_scores.append(
            omnia_like_score(
                random_binary()
            )
        )

        walk_scores.append(
            omnia_like_score(
                random_walk()
            )
        )

    # ---------------------------------------------------------------
    # ANALYZE
    # ---------------------------------------------------------------

    analyses = [

        analyze_scores(
            "random_sequence",
            sequence_scores,
        ),

        analyze_scores(
            "random_binary",
            binary_scores,
        ),

        analyze_scores(
            "random_walk",
            walk_scores,
        ),
    ]

    summary = {
        "num_random_systems": NUM_RANDOM_SYSTEMS,

        "observed_candidate_band": [
            OBSERVED_LOW,
            OBSERVED_HIGH,
        ],

        "observed_core_band": [
            CORE_LOW,
            CORE_HIGH,
        ],

        "results": analyses,
    }

    # ---------------------------------------------------------------
    # WRITE JSON
    # ---------------------------------------------------------------

    with SUMMARY_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(summary, f, indent=2)

    # ---------------------------------------------------------------
    # WRITE REPORT
    # ---------------------------------------------------------------

    lines = []

    lines.append(
        "# OMNIA-Generated Random Baseline"
    )

    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "Generate random systems and pass them "
        "through the OMNIA-like scoring path."
    )

    lines.append("")
    lines.append(
        "IMPORTANT:"
    )

    lines.append(
        "Current version still uses placeholder "
        "bootstrap scoring logic."
    )

    lines.append("")
    lines.append(
        "Real OMNIA integration is still required."
    )

    lines.append("")

    for analysis in analyses:

        lines.append(
            f"## {analysis['distribution']}"
        )

        lines.append("")

        lines.append("```json")

        lines.append(
            json.dumps(
                analysis,
                indent=2,
            )
        )

        lines.append("```")
        lines.append("")

    with REPORT_FILE.open(
        "w",
        encoding="utf-8",
    ) as f:
        f.write("\n".join(lines))

    # ---------------------------------------------------------------
    # PRINT
    # ---------------------------------------------------------------

    print("=" * 80)
    print("OMNIA-GENERATED RANDOM BASELINE")
    print("=" * 80)

    print(
        json.dumps(
            summary,
            indent=2,
        )
    )

    print()

    print(
        f"Summary written to: {SUMMARY_FILE}"
    )

    print(
        f"Report written to: {REPORT_FILE}"
    )


if __name__ == "__main__":
    main()