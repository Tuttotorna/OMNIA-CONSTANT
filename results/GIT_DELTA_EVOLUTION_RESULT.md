# Git Delta Evolution Result

## Purpose

Test whether real GitHub repository evolution reproduces the observed `Ω≈0.62` persistence corridor when measuring commit-to-commit structural deltas.

This test was designed after the first static GitHub snapshot test saturated near high values (`Ω≈0.9`) and failed to measure real evolution.

The delta test instead measures:

```text
commit_n
↓
diff
↓
commit_n+1

rather than the whole repository state.


---

Candidate band tested

0.598 ≤ Ω ≤ 0.644681


---

Tested repositories

linux
cpython
numpy
django
react

Each repository was sampled over recent commit deltas.


---

Global summary

{
  "tested_repositories": 5,
  "candidate_band": [0.598, 0.644681],
  "candidate_hits": 0,
  "candidate_rate": 0.0,
  "global_mean": 0.354356,
  "global_std": 0.021259
}


---

Repository-level results

linux

{
  "repo": "linux",
  "trajectory": [
    0.377751,
    0.338517,
    0.363728,
    0.357232,
    0.0,
    0.310328,
    0.34949,
    0.303958,
    0.916912,
    0.327219,
    0.610878
  ],
  "mean_omega": 0.38691,
  "std": 0.213694,
  "length": 11
}

cpython

{
  "repo": "cpython",
  "trajectory": [
    0.370688,
    0.37774,
    0.338859,
    0.348072,
    0.341407,
    0.424455,
    0.311883,
    0.378654,
    0.360873,
    0.289535,
    0.375303
  ],
  "mean_omega": 0.356134,
  "std": 0.034664,
  "length": 11
}

numpy

{
  "repo": "numpy",
  "trajectory": [
    0.333015,
    0.389295,
    0.37228,
    0.313093,
    0.287266,
    0.605509,
    0.331058,
    0.573331,
    0.291036,
    0.0,
    0.326966
  ],
  "mean_omega": 0.347532,
  "std": 0.150631,
  "length": 11
}

django

{
  "repo": "django",
  "trajectory": [
    0.288565,
    0.345233,
    0.333484,
    0.330652,
    0.321852,
    0.342902,
    0.339576,
    0.321372,
    0.305894,
    0.32716,
    0.273831
  ],
  "mean_omega": 0.320956,
  "std": 0.021753,
  "length": 11
}

react

{
  "repo": "react",
  "trajectory": [
    0.334002,
    0.325477,
    0.344144,
    0.312632,
    0.339456,
    0.346872,
    0.338785,
    0.341152,
    0.341135,
    0.554495,
    0.384568
  ],
  "mean_omega": 0.360247,
  "std": 0.063639,
  "length": 11
}


---

Main result

At repository-mean level, the Git delta evolution test does NOT reproduce the Ω≈0.62 corridor.

candidate_hits = 0 / 5
candidate_rate = 0.0

The repository means are substantially lower:

linux   → 0.386910
cpython → 0.356134
numpy   → 0.347532
django  → 0.320956
react   → 0.360247

Global mean:

Ω_mean ≈ 0.354356


---

Important observation

Although repository-level means do not fall inside the candidate corridor, isolated commit-delta events do appear near or inside the corridor.

Examples:

linux → 0.610878
numpy → 0.605509

Near-corridor event:

numpy → 0.573331
react → 0.554495

This suggests that the corridor may not be a system-global average in this domain.

Instead, it may appear as:

event-local transition behavior


---

Corrected interpretation

This test rejects the claim:

real Git repository evolution has global mean Ω≈0.62

under the current delta scoring adapter.

However, it leaves open a narrower hypothesis:

some local structural transition events in Git evolution may cross the Ω≈0.62 corridor


---

Methodological limitation

This test does not use canonical OMNIA-INVARIANCE scoring.

It uses a rough Git-delta adapter based on:

changed line count

diff entropy

unique character diversity


Therefore, this result should be treated as:

external adapter test

not as:

canonical OMNIA-INVARIANCE validation


---

What this result shows

The result shows that the Ω≈0.62 corridor is not automatically reproduced by arbitrary real-world data adapters.

This is useful because it prevents overclaiming.

The corridor is not trivially everywhere.

It appears strongly in OMNIA-INVARIANCE mean trajectories, but not automatically in rough Git repository delta means.


---

Evidence status

Git static snapshot:
FAILED / saturated high

Git delta evolution:
FAILED at repository-mean level

Git local events:
some near-band events observed


---

Current status

system-global Git replication:
NOT SUPPORTED

event-local Git transition hypothesis:
OPEN


---

Next required test

The next correct test is:

Git local transition event scan

Goal:

count how often individual commit deltas fall inside the Ω≈0.62 corridor
instead of averaging the whole repository trajectory.

This tests whether the corridor is:

a local transition signature

rather than:

a global repository mean