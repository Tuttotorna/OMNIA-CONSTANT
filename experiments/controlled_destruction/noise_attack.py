#!/usr/bin/env python3
"""
Noise Attack · OMNIA-CONSTANT

Purpose:
    Test whether the Ω≈0.6 candidate boundary appears spontaneously
    in pure random noise.

If Ω≈0.6 appears frequently in pure noise, the candidate weakens.

This is a baseline destruction experiment.
"""

import json
import math
import random
import statistics
from pathlib import Path


OMEGA_TARGET = 0.6
TOLERANCE = 0.05
DEFAULT_SEEDS = list(range(30))
DEFAULT_SAMPLE_SIZE = 256
DEFAULT_RUNS_PER_SEED = 20

OUTPUT_DIR = Path("results/controlled_destruction")
OUTPUT_FILE = OUTPUT_DIR / "noise_attack_results.jsonl"


def omega_proxy(values):
    """
    Provisional Ω proxy.

    Measures structural persistence as inverse normalized volatility.

    This is NOT the final OMNIA Ω.

    It is a placeholder until the canonical OMNIA scoring function
    is connected.
    """
    if len(values) < 2:
        return 0.0

    mean_value = statistics.mean(values)
    stdev_value = statistics.pstdev(values)

    if mean_value == 0:
        return 0.0

    cv = abs(stdev_value / mean_value)

    omega = 1.0 / (1.0 + cv)

    return max(0.0, min(1.0, omega))


def generate_uniform_noise(sample_size):
    return [random.random() for _ in range(sample_size)]


def generate_gaussian_noise(sample_size):
    return [random.gauss(0.0, 1.0) for _ in range(sample_size)]


def generate_shuffled_noise(sample_size):
    values = list(range(sample_size))
    random.shuffle(values)
    max_value = max(values) if values else 1
    return [v / max_value for v in values]


def generate_binary_noise(sample_size):
    return [random.choice([0.0, 1.0]) for _ in range(sample_size)]


NOISE_GENERATORS = {
    "uniform_noise": generate_uniform_noise,
    "gaussian_noise": generate_gaussian_noise,
    "shuffled_noise": generate_shuffled_noise,
    "binary_noise": generate_binary_noise,
}


def candidate_detected(omega):
    return abs(omega - OMEGA_TARGET) <= TOLERANCE


def run_noise_attack(
    seeds=DEFAULT_SEEDS,
    sample_size=DEFAULT_SAMPLE_SIZE,
    runs_per_seed=DEFAULT_RUNS_PER_SEED,
):
    results = []

    for noise_type, generator in NOISE_GENERATORS.items():
        for seed in seeds:
            random.seed(seed)

            omega_values = []

            for _ in range(runs_per_seed):
                values = generator(sample_size)
                omega_values.append(omega_proxy(values))

            omega_mean = statistics.mean(omega_values)
            omega_std = statistics.pstdev(omega_values)
            omega_distance = abs(omega_mean - OMEGA_TARGET)

            detected = candidate_detected(omega_mean)

            result = {
                "experiment_name": "noise_attack",
                "domain": "pure_random_noise",
                "attack_type": noise_type,
                "seed": seed,
                "sample_size": sample_size,
                "runs_per_seed": runs_per_seed,
                "omega_values": omega_values,
                "omega_mean": omega_mean,
                "omega_std": omega_std,
                "omega_distance_from_0_6": omega_distance,
                "candidate_detected": detected,
                "candidate_rejected": detected,
                "rejection_reason": (
                    "omega_0_6_appears_in_pure_noise" if detected else None
                ),
                "notes": (
                    "If Ω≈0.6 appears frequently in pure noise, "
                    "the candidate boundary is weakened."
                ),
            }

            results.append(result)

    return results


def summarize(results):
    total = len(results)
    detections = sum(1 for r in results if r["candidate_detected"])
    detection_rate = detections / total if total else 0.0

    by_attack = {}

    for r in results:
        attack = r["attack_type"]
        by_attack.setdefault(attack, [])
        by_attack[attack].append(r["omega_mean"])

    attack_summary = {
        attack: {
            "count": len(values),
            "omega_mean": statistics.mean(values),
            "omega_std": statistics.pstdev(values),
            "min": min(values),
            "max": max(values),
        }
        for attack, values in by_attack.items()
    }

    return {
        "experiment_name": "noise_attack",
        "omega_target": OMEGA_TARGET,
        "tolerance": TOLERANCE,
        "total_trials": total,
        "candidate_detections": detections,
        "detection_rate": detection_rate,
        "candidate_status": (
            "weakened" if detection_rate > 0.05 else "not_rejected_by_noise_attack"
        ),
        "attack_summary": attack_summary,
    }


def write_jsonl(results, output_file=OUTPUT_FILE):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        for row in results:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    results = run_noise_attack()
    write_jsonl(results)

    summary = summarize(results)

    print("=" * 80)
    print("NOISE ATTACK · Ω≈0.6")
    print("=" * 80)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print()
    print(f"Results written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()