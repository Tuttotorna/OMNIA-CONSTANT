# Cross-Metric Independence Result

## Purpose

This test checks whether the observed `Ω≈0.62` candidate band is numerically preserved across independent trajectory metrics.

The central question was:

```text
Does the candidate band emerge from the underlying structure,
or is it specific to the mean_omega metric?


---

Candidate band tested

0.598 ≤ Ω ≤ 0.644681

Core band:

0.610 ≤ Ω ≤ 0.619048


---

Metrics tested

The same omega_trajectory profiles were evaluated using:

mean_omega
variance_stability
range_stability
smoothness_score
entropy_stability
compression_stability


---

Result summary

mean_omega              → 5/5 = 100%  strong_alignment
variance_stability      → 0/5 = 0%    no_alignment
range_stability         → 1/5 = 20%   weak_alignment
smoothness_score        → 0/5 = 0%    no_alignment
entropy_stability       → 1/5 = 20%   weak_alignment
compression_stability   → 0/5 = 0%    no_alignment


---

Detailed metric results

mean_omega

{
  "count": 5,
  "candidate_hits": 5,
  "candidate_rate": 1.0,
  "core_hits": 1,
  "core_rate": 0.2,
  "mean": 0.6184,
  "std": 0.018948350851723236,
  "min": 0.598,
  "max": 0.644,
  "values": [0.638, 0.598, 0.644, 0.61, 0.602],
  "alignment_class": "strong_alignment"
}

variance_stability

{
  "count": 5,
  "candidate_hits": 0,
  "candidate_rate": 0.0,
  "core_hits": 0,
  "core_rate": 0.0,
  "mean": 0.7645796,
  "std": 0.07472377271150059,
  "min": 0.652057,
  "max": 0.850414,
  "values": [0.850414, 0.730972, 0.652057, 0.844437, 0.745018],
  "alignment_class": "no_alignment"
}

range_stability

{
  "count": 5,
  "candidate_hits": 1,
  "candidate_rate": 0.2,
  "core_hits": 1,
  "core_rate": 0.2,
  "mean": 0.398,
  "std": 0.2041959842896035,
  "min": 0.15,
  "max": 0.67,
  "values": [0.61, 0.27, 0.15, 0.67, 0.29],
  "alignment_class": "weak_alignment"
}

smoothness_score

{
  "count": 5,
  "candidate_hits": 0,
  "candidate_rate": 0.0,
  "core_hits": 0,
  "core_rate": 0.0,
  "mean": 0.8180000000000001,
  "std": 0.042379240200834174,
  "min": 0.7425,
  "max": 0.8725,
  "values": [0.8725, 0.8175, 0.7425, 0.835, 0.8225],
  "alignment_class": "no_alignment"
}

entropy_stability

{
  "count": 5,
  "candidate_hits": 1,
  "candidate_rate": 0.2,
  "core_hits": 0,
  "core_rate": 0.0,
  "mean": 0.25871920000000004,
  "std": 0.1728964,
  "min": 0.172271,
  "max": 0.604512,
  "values": [0.172271, 0.172271, 0.172271, 0.604512, 0.172271],
  "alignment_class": "weak_alignment"
}

compression_stability

{
  "count": 5,
  "candidate_hits": 0,
  "candidate_rate": 0.0,
  "core_hits": 0,
  "core_rate": 0.0,
  "mean": 0.0533334,
  "std": 0.06863764435235231,
  "min": 0.0,
  "max": 0.166667,
  "values": [0.0, 0.0, 0.1, 0.166667, 0.0],
  "alignment_class": "no_alignment"
}


---

Main finding

The Ω≈0.62 band is strongly preserved under:

mean_omega

but is not numerically preserved under independent trajectory metrics.

Therefore, the current evidence does NOT support the stronger claim:

Ω≈0.62 is a metric-independent numerical constant.


---

Corrected interpretation

The correct current claim is:

Ω≈0.62 is a candidate critical band observed in the mean_omega channel of OMNIA-INVARIANCE.

Not:

Ω≈0.62 is a universal cross-metric constant.


---

Why this does not destroy the candidate

Different metrics do not necessarily share the same numerical scale.

For example:

mean_omega
variance_stability
range_stability
smoothness_score
entropy_stability
compression_stability

measure different structural aspects.

Therefore, failure to land numerically in the same 0.598–0.644681 band does not automatically mean that the underlying structural region is false.

It only means:

the numerical value 0.62 is not directly portable across metrics.


---

Updated hypothesis

The hypothesis must shift from:

Ω≈0.62 is a universal numerical constant.

to:

Ω≈0.62 may represent a critical position in the mean_omega metric,
while the deeper invariant may be a cross-metric structural position.


---

Evidence status

Current status:

mean_omega candidate survives
cross-metric numerical independence fails

This is a partial weakening, not a full rejection.


---

Next required test

The next required test is:

rank_based_cross_metric_test.py

Purpose:

Normalize each metric internally and test whether the same trajectories occupy comparable critical positions across metrics.

This avoids incorrectly comparing raw numerical values across metrics with different scales.


---

Boundary statement

This result prevents overclaiming.

Current valid statement:

The observed Ω≈0.62 band is a strong mean_omega-channel candidate,
but not yet a metric-independent structural constant.