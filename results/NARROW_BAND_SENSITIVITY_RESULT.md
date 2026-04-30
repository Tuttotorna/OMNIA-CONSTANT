# Narrow-Band Sensitivity Result

## Purpose

This scan tests how the observed Ω candidate region behaves as the transition band progressively narrows.

Goal:

```text
determine whether the candidate behaves like:
- broad statistical region
- narrow persistence band
- sharp singularity


---

Initial candidate region

Initial observed candidate:

0.55 ≤ Ω ≤ 0.65

Observed unique Ω values:

0.598
0.602
0.610
0.619
0.619048
0.638
0.644
0.644681


---

Narrow-band results

Band 0.55 – 0.65

8 / 8 survive
transition_rate = 1.000


---

Band 0.58 – 0.64

6 / 8 survive
transition_rate = 0.750

Dropped values:

0.644
0.644681


---

Band 0.59 – 0.65

8 / 8 survive
transition_rate = 1.000


---

Band 0.60 – 0.65

7 / 8 survive
transition_rate = 0.875

Dropped value:

0.598


---

Band 0.60 – 0.64

5 / 8 survive
transition_rate = 0.625

Dropped values:

0.598
0.644
0.644681


---

Band 0.61 – 0.63

3 / 8 survive
transition_rate = 0.375

Surviving core:

0.610
0.619
0.619048


---

Main observation

The candidate region does NOT behave like:

Ω = exact singular value

Instead, it behaves like:

narrow persistence band

The candidate survives moderate narrowing, but progressively collapses under aggressive compression.


---

Observed robust region

Current robust region:

0.598 ≤ Ω ≤ 0.644681

Practical approximation:

Ω ≈ 0.62 ± 0.02


---

Observed central core

The most resistant inner cluster observed during aggressive narrowing:

0.610
0.619
0.619048

Approximate central core:

Ω ≈ 0.616


---

Structural interpretation

Current evidence suggests:

Ω behaves more like a critical persistence band
than a sharp singular constant.

The region appears structurally stable across:

duplicate reduction

source grouping

moderate band contraction


but not under extreme narrowing.


---

Current evidence status

Current status:

observed narrow persistence band

Not yet:

universal invariant constant


---

Important limitations

Current limitations remain:

very small sample size

limited independent domains

no null/random baseline comparison

no adversarial falsification

no metric substitution test

no alternative Ω definitions tested



---

Next required test

Next required step:

null/random baseline scan

Goal:

determine whether random or synthetic systems
also collapse toward the same Ω band.