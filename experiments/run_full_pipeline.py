#!/usr/bin/env python3
"""
Run Full Pipeline · OMNIA-CONSTANT

Purpose:
    Execute the complete OMNIA-CONSTANT experimental pipeline.

This script orchestrates:

    1. Controlled destruction experiments
    2. Ω distribution mapping
    3. OMNIA-INVARIANCE bridge analysis
    4. Band sensitivity analysis
    5. Domain separation analysis
    6. Transition drift analysis

The goal is not to confirm Ω≈0.6.

The goal is to stress-test the transition-region hypothesis.
"""

import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent

PIPELINE = [
    (
        "Noise Attack",
        ROOT / "controlled_destruction" / "noise_attack.py",
    ),
    (
        "Ω Distribution Map",
        ROOT / "controlled_destruction" / "omega_distribution_map.py",
    ),
    (
        "OMNIA-INVARIANCE Bridge",
        ROOT / "import_from_invariance" / "invariance_results_bridge.py",
    ),
    (
        "Band Sensitivity Analysis",
        ROOT / "import_from_invariance" / "band_sensitivity_analysis.py",
    ),
    (
        "Domain Separation Analysis",
        ROOT / "import_from_invariance" / "domain_separation_analysis.py",
    ),
    (
        "Transition Drift Analysis",
        ROOT / "import_from_invariance" / "transition_drift_analysis.py",
    ),
]


def run_step(name, path):
    print("=" * 80)
    print(f"RUNNING: {name}")
    print("=" * 80)
    print(f"Script: {path}")
    print()

    if not path.exists():
        print(f"[ERROR] Missing script: {path}")
        return False

    start = time.time()

    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
    )

    elapsed = time.time() - start

    print(result.stdout)

    if result.stderr.strip():
        print("-" * 80)
        print("STDERR")
        print("-" * 80)
        print(result.stderr)

    print("-" * 80)
    print(f"Exit code: {result.returncode}")
    print(f"Elapsed: {elapsed:.2f}s")
    print()

    return result.returncode == 0


def main():
    print("=" * 80)
    print("OMNIA-CONSTANT FULL PIPELINE")
    print("=" * 80)
    print()

    success_count = 0
    failure_count = 0

    failures = []

    pipeline_start = time.time()

    for name, path in PIPELINE:
        ok = run_step(name, path)

        if ok:
            success_count += 1
        else:
            failure_count += 1
            failures.append(name)

    total_elapsed = time.time() - pipeline_start

    print("=" * 80)
    print("PIPELINE SUMMARY")
    print("=" * 80)
    print(f"Successful steps: {success_count}")
    print(f"Failed steps: {failure_count}")
    print(f"Total elapsed: {total_elapsed:.2f}s")
    print()

    if failures:
        print("FAILED STEPS:")
        for failure in failures:
            print(f"- {failure}")
        print()

    if failure_count == 0:
        print("Pipeline completed successfully.")
    else:
        print("Pipeline completed with failures.")

    print()
    print("Core principle:")
    print("measurement != interpretation != decision")


if __name__ == "__main__":
    main()