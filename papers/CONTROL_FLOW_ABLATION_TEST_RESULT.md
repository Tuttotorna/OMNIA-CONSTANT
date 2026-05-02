# CONTROL FLOW ABLATION TEST

## Goal

Test whether commits that modify control-flow structures produce systematically higher Ω values than commits that do not.

This experiment evaluates whether Ω can be reduced to control-flow deformation alone.

---

# Repository

```text
django


---

Dataset Summary

{
  "events": 1601,
  "A_CONTROL_FLOW": 88,
  "B_NON_CONTROL": 1513
}


---

Group Definition

A_CONTROL_FLOW

Commits that modify at least one control-flow structure:

if

for

while

try

match

boolean branching

async control structures


B_NON_CONTROL

Commits without detected control-flow modification.


---

Results

Mean Ω

Group	Mean Ω

A_CONTROL_FLOW	6.115279
B_NON_CONTROL	5.620511



---

Median Ω

Group	Median Ω

A_CONTROL_FLOW	5.840331
B_NON_CONTROL	5.456373



---

Variance

Group	Variance

A_CONTROL_FLOW	4.255667
B_NON_CONTROL	4.342500



---

Tail Percentiles

Metric	A_CONTROL_FLOW	B_NON_CONTROL

P90	9.060700	8.400177
P95	9.528991	9.358033



---

Statistical Tests

Test	Statistic	p-value

Kolmogorov-Smirnov	0.141065	0.065817
Mann-Whitney U	75924.5	0.026535



---

Interpretation

Control-flow commits show higher Ω on average.

This supports the hypothesis that control-flow deformation contributes to Ω elevation.

However, the separation is not strong enough to reduce Ω to control-flow alone.


---

Critical Observation

Some extremely high-Ω commits occurred in the non-control group.

Examples:

Commit	Ω	control_delta

f81e6e3a53ee	16.231548	0
69a93a88edb5	15.871335	0
305757aec19c	13.531613	0


This shows:

control-flow deformation is not necessary for high Ω.


---

Main Conclusion

The test supports:

control-flow deformation contributes to Ω.

But rejects:

Ω = control-flow deformation.


---

Updated Interpretation

Ω appears to be a composite structural perturbation signal.

Likely contributing components:

control-flow deformation

AST restructuring

patch magnitude

deletion pressure

representational compression or expansion

latent structural perturbation



---

Current Working Hypothesis

Ω behaves as a higher-order structural deformation measure
rather than a single-factor control-flow metric.


---

Status

Partial support
Reduction rejected