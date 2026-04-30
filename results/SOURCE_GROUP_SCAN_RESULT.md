# Source Group Scan Result

## Purpose

This scan tests whether the observed `Ω≈0.6` candidate region appears across distinct source groups.

The goal is to distinguish:

```text
repeated exports

from:

independent structural domains


---

Global summary

{
  "scanned_files": 10,
  "unique_global_omega_count": 8,
  "transition_band": [0.55, 0.65],
  "transition_count": 8,
  "transition_rate": 1.0,
  "omega_mean": 0.621841125,
  "omega_std": 0.017291400083838646,
  "omega_min": 0.598,
  "omega_max": 0.644681
}


---

Distinct source groups

Observed canonical Ω values by group:

crypto  → 0.598
llm     → 0.602
logic   → 0.619
finance → 0.638
physics → 0.644

Additional grouped summaries:

cross_domain → 0.598, 0.619, 0.619048, 0.644, 0.644681
trajectory   → 0.598, 0.602, 0.610, 0.638, 0.644


---

Observation

The candidate region survives source grouping.

All unique canonical Ω values remain inside:

0.55 ≤ Ω ≤ 0.65

The observed region remains narrow:

0.598 ≤ Ω ≤ 0.644681


---

Current interpretation

The Ω≈0.6 candidate region is present across multiple source groups, including:

crypto

LLM

logic

finance

physics

trajectory-space summaries

cross-domain summaries


Current status:

candidate region survives source-group scan


---

Important limitation

Most individual domain groups currently contain only one unique canonical Ω value.

Therefore this scan supports cross-source presence, but not yet full statistical independence.

The result is stronger than duplicate survival, but weaker than large-sample cross-domain replication.


---

What this does NOT prove

This does not yet prove:

universal structural constant

domain-independent law

causal principle

final invariant

metric inevitability



---

Evidence status

Current evidence level:

observed cross-source candidate region

Not yet:

confirmed structural constant


---

Next required test

The next required test is:

narrow-band sensitivity scan

Goal:

determine whether the candidate survives when the transition band is tightened
from 0.55–0.65 to narrower intervals around Ω≈0.6.