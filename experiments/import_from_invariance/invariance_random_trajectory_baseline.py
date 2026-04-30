# experiments/import_from_invariance/invariance_random_trajectory_baseline.py

import json
import random
import statistics
from pathlib import Path

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True, parents=True)

OBSERVED_BAND = (0.598, 0.644681)
CORE_BAND = (0.61, 0.619048)

NUM_TRAJECTORIES = 10000
TRAJECTORY_LENGTH = 5


def clamp(v, low=0.0, high=1.0):
    return max(low, min(high, v))


def mean_omega(trajectory):
    return sum(trajectory) / len(trajectory)


def random_uniform_trajectory():
    return [
        random.random()
        for _ in range(TRAJECTORY_LENGTH)
    ]


def random_gaussian_trajectory():
    return [
        clamp(random.gauss(0.5, 0.15))
        for _ in range(TRAJECTORY_LENGTH)
    ]


def edge_random_trajectory():
    out = []

    for _ in range(TRAJECTORY_LENGTH):
        if random.random() < 0.5:
            out.append(random.uniform(0.0, 0.1))
        else:
            out.append(random.uniform(0.9, 1.0))

    return out


def smooth_random_walk():
    start = random.uniform(0.0, 1.0)

    out = [start]

    for _ in range(TRAJECTORY_LENGTH - 1):
        step = random.uniform(-0.08, 0.08)
        out.append(clamp(out[-1] + step))

    return out


def oscillatory_random():
    base = random.uniform(0.2, 0.8)

    out = []

    for i in range(TRAJECTORY_LENGTH):
        direction = -1 if i % 2 == 0 else 1
        noise = random.uniform(0.0, 0.12)
        out.append(clamp(base + direction * noise))

    return out


GENERATORS = {
    "uniform_random": random_uniform_trajectory,
    "gaussian_random": random_gaussian_trajectory,
    "edge_random": edge_random_trajectory,
    "smooth_random_walk": smooth_random_walk,
    "oscillatory_random": oscillatory_random,
}


def run_distribution(name, generator):
    means = []

    for _ in range(NUM_TRAJECTORIES):
        trajectory = generator()
        means.append(mean_omega(trajectory))

    observed_hits = [
        x for x in means
        if OBSERVED_BAND[0] <= x <= OBSERVED_BAND[1]
    ]

    core_hits = [
        x for x in means
        if CORE_BAND[0] <= x <= CORE_BAND[1]
    ]

    return {
        "distribution": name,
        "sample_count": NUM_TRAJECTORIES,
        "trajectory_length": TRAJECTORY_LENGTH,
        "mean": statistics.mean(means),
        "std": statistics.pstdev(means),
        "min": min(means),
        "max": max(means),
        "observed_band": OBSERVED_BAND,
        "observed_band_hits": len(observed_hits),
        "observed_band_rate": len(observed_hits) / NUM_TRAJECTORIES,
        "core_band": CORE_BAND,
        "core_band_hits": len(core_hits),
        "core_band_rate": len(core_hits) / NUM_TRAJECTORIES,
    }


def main():
    results = []

    for name, generator in GENERATORS.items():
        results.append(run_distribution(name, generator))

    summary = {
        "num_trajectories": NUM_TRAJECTORIES,
        "trajectory_length": TRAJECTORY_LENGTH,
        "observed_candidate_band": OBSERVED_BAND,
        "observed_core_band": CORE_BAND,
        "results": results,
    }

    out_json = RESULTS_DIR / "INVARIANCE_RANDOM_TRAJECTORY_BASELINE.json"

    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2)

    report_lines = []

    report_lines.append("# Invariance Random Trajectory Baseline")
    report_lines.append("")
    report_lines.append("## Purpose")
    report_lines.append(
        "Test whether random trajectories generated in the same format as OMNIA-INVARIANCE naturally reproduce the observed Ω persistence band."
    )
    report_lines.append("")
    report_lines.append(
        f"- observed candidate band: {OBSERVED_BAND[0]} – {OBSERVED_BAND[1]}"
    )
    report_lines.append(
        f"- observed core band: {CORE_BAND[0]} – {CORE_BAND[1]}"
    )
    report_lines.append("")

    for row in results:
        report_lines.append(f"## {row['distribution']}")
        report_lines.append("")
        report_lines.append("```json")
        report_lines.append(json.dumps(row, indent=2))
        report_lines.append("```")
        report_lines.append("")

    out_md = RESULTS_DIR / "INVARIANCE_RANDOM_TRAJECTORY_BASELINE.md"

    with open(out_md, "w") as f:
        f.write("\n".join(report_lines))

    print("=" * 80)
    print("INVARIANCE RANDOM TRAJECTORY BASELINE")
    print("=" * 80)

    print(json.dumps(summary, indent=2))

    print()
    print(f"Summary written to: {out_json}")
    print(f"Report written to: {out_md}")


if __name__ == "__main__":
    main()