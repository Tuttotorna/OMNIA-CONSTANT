# CONTROL FLOW ABLATION TEST — RESULT

## Objective

Test whether commits that modify control-flow structures
(`if`, `for`, `while`, `try`, `match`, etc.)
produce systematically higher Ω values than commits that do not.

This experiment attempts to isolate logical-structural deformation
from generic code modification activity.

---

# Dataset

- Repository: `django`
- Commits analyzed: `2500`
- Parsed events: `1601`

Groups:

- `A_CONTROL_FLOW`
  - commits modifying control-flow nodes
- `B_NON_CONTROL`
  - commits modifying non-control structures only

---

# Core Result

## Group Counts

| Group | Count |
|---|---:|
| A_CONTROL_FLOW | 88 |
| B_NON_CONTROL | 1513 |

---

# Ω Distribution

## Mean Ω

| Group | Mean Ω |
|---|---:|
| A_CONTROL_FLOW | 6.1153 |
| B_NON_CONTROL | 5.6205 |

Difference:

```text
ΔΩ ≈ +0.495

Control-flow commits show higher average Ω.


---

Median Ω

Group	Median Ω

A_CONTROL_FLOW	5.8403
B_NON_CONTROL	5.4564


Median separation persists.


---

Variance

Group	Variance

A_CONTROL_FLOW	4.2557
B_NON_CONTROL	4.3425


Variances are comparable.

This suggests the effect is not caused by extreme outliers alone.


---

Tail Analysis

P90

Group	P90 Ω

A_CONTROL_FLOW	9.0607
B_NON_CONTROL	8.4002


P95

Group	P95 Ω

A_CONTROL_FLOW	9.5290
B_NON_CONTROL	9.3580


Upper-tail stress remains higher for control-flow commits.


---

Statistical Tests

Kolmogorov–Smirnov

Metric	Value

KS statistic	0.1411
p-value	0.0658


Weak-to-borderline distributional separation.


---

Mann–Whitney U

Metric	Value

U statistic	75924.5
p-value	0.0265


Statistically significant difference between groups.


---

Interpretation

The result supports:

Control-flow deformation contributes to Ω elevation.

But the result also falsifies the stronger hypothesis:

Ω != pure control-flow metric

because many extremely high-Ω commits belong to the non-control group.


---

Critical Observation

Several top Ω commits contain:

control_delta = 0
non_control_delta = 0

yet still produce extremely high Ω.

Examples:

Commit	Ω

f81e6e3a53ee	16.23
69a93a88edb5	15.87
305757aec19c	13.53


This demonstrates:

Control-flow change is neither necessary nor sufficient for high Ω.


---

Structural Conclusion

The experiment establishes:

Ω is partially sensitive to logical branching deformation,
but cannot be reduced to AST control-flow alone.

This places Ω in a broader category:

Ω behaves as a generalized structural deformation measure.

Not:

churn

topology

repository history

import centrality

co-change memory

pure AST size

pure control-flow mutation



---

Current Evidence Hierarchy

Hypothesis	Status

Churn explains Ω	Rejected
Graph centrality explains Ω	Rejected
Co-change history explains Ω	Rejected
Patch geometry explains Ω	Partial
AST deformation explains Ω	Supported
Control-flow alone explains Ω	Rejected
Ω measures generalized structural deformation	Current best fit



---

Important Methodological Note

This test reduces — but does not fully eliminate — possible proxy overlap between Ω and AST-derived metrics.

Further validation should involve:

semantic-preserving rewrites

token permutation stability

representation invariance

execution-trace deformation

latent structural perturbation



---

Provisional Interpretation

Current evidence suggests:

Ω reacts to transformation stress
inside the logical geometry of code.

The strongest surviving signal is not:

where the change occurs

nor:

how historically unusual it is

but rather:

how strongly the modification deforms executable structure.


---

Final Status

RESULT: PARTIAL SUPPORT

Control-flow deformation elevates Ω statistically, but Ω is not reducible to control-flow mutation itself.

The surviving hypothesis is:

Ω measures higher-order structural instability.