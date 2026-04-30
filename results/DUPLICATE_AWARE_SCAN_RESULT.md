# Duplicate-Aware Scan Result

## Purpose

This scan tests whether the observed `Ω≈0.6` candidate region survives after duplicate reduction.

The previous filtered scan found all canonical Ω values inside the provisional transition band:

```text
0.55 ≤ Ω ≤ 0.65

This test removes repeated canonical Ω values and re-evaluates the result.


---

Summary

{
  "scanned_files": 10,
  "raw_canonical_omega_count": 15,
  "unique_canonical_omega_count": 8,
  "duplicate_count_removed": 7,
  "transition_band": [0.55, 0.65],
  "transition_count": 8,
  "transition_rate": 1.0,
  "omega_mean": 0.621841125,
  "omega_std": 0.017291400083838646,
  "omega_min": 0.598,
  "omega_max": 0.644681
}


---

Unique canonical Ω values

0.598000
0.602000
0.610000
0.619000
0.619048
0.638000
0.644000
0.644681


---

Observation

After removing duplicate exported values, all unique canonical Ω values still fall inside:

0.55 ≤ Ω ≤ 0.65

The candidate region therefore survives duplicate reduction.


---

Current interpretation

The Ω≈0.6 region is not only present in repeated summary files.

It remains present after reducing duplicates.

Current status:

candidate region survives duplicate-aware scan


---

What this does NOT prove

This does not yet prove:

universal structural constant

domain-independent law

metric inevitability

causal principle

final invariant



---

Next required test

The next required step is source-level grouping.

Goal:

determine whether the Ω≈0.6 region is coming from independent domains
or from repeated exports of the same underlying experiment family

