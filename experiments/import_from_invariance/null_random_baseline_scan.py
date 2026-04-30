#!/usr/bin/env python3
"""
Null / Random Baseline Scan · OMNIA-CONSTANT

Purpose:
    Compare the observed Ω candidate band against
    synthetic random baselines.

Goal:
    determine whether the observed Ω persistence band
    is structurally meaningful or easily reproduced by noise.
"""

import json
import random
import statistics
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------

OUTPUT_DIR = Path("results")

SUMMARY_FILE = OUTPUT_DIR / "NULL_RANDOM_BASELINE_SCAN.json"
REPORT_FILE = OUTPUT_DIR / "NULL_RANDOM_BASELINE_SCAN.md"

# observed candidate region
OBSERVED_LOW = 0.598
OBSERVED_HIGH = 0.644681

# approximate observed core
CORE_LOW = 0.610
CORE_HIGH = 0.619048

NUM_SAMPLES = 10000

RANDOM_SEED = 42


# -------------------------------------------------------------------
# RANDOM GENERATORS
# -------------------------------------------------------------------

def uniform_random():
    """
    Uniform random baseline in [0,1].
    """
    return random.random()


def gaussian_random():
    """
    Gaussian baseline centered at 0.5.
    """
    x = random.gauss(0.5, 0.15)

    # clamp
    return max(0.0, min(1.0, x))


def edge_random():
    """
    Edge-biased random baseline.
    Produces values closer to 0 or 1.
    """

    if random.random() < 0.5:
        return random.uniform(0.0, 0.2)

    return random.uniform(0.8, 1.0)


# -------------------------------------------------------------------
# ANALYSIS
# -------------------------------------------------------------------

def analyze_distribution(name, values):

    observed_hits = [
        v for v in values
        if OBSERVED_LOW <= v <= OBSERVED_HIGH
    ]

    core_hits = [
        v for v in values
        if CORE_LOW <= v <= CORE_HIGH
    ]

    return {
        "distribution": name,
        "sample_count": len(values),
        "mean": statistics.mean(values),
        "std": statistics.pstdev(values),
        "min": min(values),
        "max": max(values),

        "observed_band": [
            OBSERVED_LOW,
            OBSERVED_HIGH,
        ],

        "observed_band_hits": len(observed_hits),

        "observed_band_rate": (
            len(observed_hits) / len(values)
        ),

        "core_band": [
            CORE_LOW,
            CORE_HIGH,
        ],

        "core_band_hits": len(core_hits),

        "core_band_rate": (
            len(core_hits) / len(values)
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
    # GENERATE BASELINES
    # ---------------------------------------------------------------

    uniform_values = [
        uniform_random()
        for _ in range(NUM_SAMPLES)
    ]

    gaussian_values = [
        gaussian_random()
        for _ in range(NUM_SAMPLES)
    ]

    edge_values = [
        edge_random()
        for _ in range(NUM_SAMPLES)
    ]

    # ---------------------------------------------------------------
    # ANALYZE
    # ---------------------------------------------------------------

    analyses = [
        analyze_distribution(
            "uniform_random",
            uniform_values,
        ),

        analyze_distribution(
            "gaussian_random",
            gaussian_values,
        ),

        analyze_distribution(
            "edge_random",
            edge_values,
        ),
    ]

    summary = {
        "num_samples": NUM_SAMPLES,
        "observed_candidate_band": [
            OBSERVED_LOW,
            OBSERVED_HIGH,
        ],
        "observed_core_band": [
            CORE_LOW,
            CORE_HIGH,
        ],
        "baseline_results": analyses,
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

    lines.append("# Null / Random Baseline Scan")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "Test whether synthetic random baselines "
        "naturally reproduce the observed Ω persistence band."
    )
    lines.append("")

    lines.append("## Candidate regions")
    lines.append("")
    lines.append(
        f"- observed band: "
        f"{OBSERVED_LOW} – {OBSERVED_HIGH}"
    )

    lines.append(
        f"- observed core: "
        f"{CORE_LOW} – {CORE_HIGH}"
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
    print("NULL / RANDOM BASELINE SCAN")
    print("=" * 80)

    print(json.dumps(summary, indent=2))

    print()
    print(
        f"Summary written to: {SUMMARY_FILE}"
    )

    print(
        f"Report written to: {REPORT_FILE}"
    )


if __name__ == "__main__":
    main()