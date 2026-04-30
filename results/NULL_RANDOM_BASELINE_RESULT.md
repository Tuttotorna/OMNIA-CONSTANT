# Null / Random Baseline Result

## Purpose

This scan tests whether simple random numeric baselines naturally reproduce the observed Ω candidate band.

Observed candidate band:

```text
0.598 ≤ Ω ≤ 0.644681

Observed core band:

0.610 ≤ Ω ≤ 0.619048


---

Baselines tested

Three synthetic numeric baselines were tested:

uniform random

Gaussian random centered at 0.5

edge-biased random


Each baseline used:

10,000 samples


---

Result summary

Observed OMNIA-INVARIANCE candidate band

real observed Ω values inside band: 8 / 8
rate = 1.000


---

Uniform random

{
  "observed_band_rate": 0.0478,
  "core_band_rate": 0.0099
}


---

Gaussian random

{
  "observed_band_rate": 0.0849,
  "core_band_rate": 0.0164
}


---

Edge random

{
  "observed_band_rate": 0.0,
  "core_band_rate": 0.0
}


---

Main observation

Simple random numeric baselines do not reproduce the observed concentration.

Comparison:

real observed band rate: 1.000

uniform random band rate: 0.0478
gaussian random band rate: 0.0849
edge random band rate: 0.0000

Core comparison:

real observed core rate: 0.375

uniform random core rate: 0.0099
gaussian random core rate: 0.0164
edge random core rate: 0.0000


---

Interpretation

The observed Ω band is not trivially reproduced by simple numeric randomness.

Current status:

candidate region survives simple null/random baseline comparison


---

Important limitation

This is not yet a full OMNIA null baseline.

The random values in this test are synthetic numeric samples.

The stronger test requires:

random input
↓
OMNIA / OMNIA-INVARIANCE scoring
↓
canonical Ω output
↓
band comparison

Therefore this result strengthens the candidate, but does not finalize it.


---

Evidence status

Current evidence level:

candidate survives synthetic numeric null baseline

Not yet:

candidate survives full OMNIA-generated null baseline


---

Next required test

Next test:

OMNIA-generated random baseline

Goal:

feed random/noise systems through the same OMNIA/INVARIANCE scoring path
and test whether their canonical Ω values converge to the same band.