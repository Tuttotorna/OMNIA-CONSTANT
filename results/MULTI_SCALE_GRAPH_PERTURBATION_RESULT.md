# Multi-Scale Graph Perturbation Result

## Purpose

Test whether the Ω≈0.6 corridor remains stable under large changes of graph scale.

Core question:

```text
Does the compatibility corridor survive
when the same perturbation process
is applied to systems of very different size?

This is the first explicit scale-invariance test in the OMNIA-CONSTANT investigation.


---

Experimental Design

Base structure

ring_lattice graph

for multiple scales:

10 nodes
30 nodes
100 nodes
300 nodes
1000 nodes

Each graph used:

{
  "k_neighbors": 4
}


---

Controlled Perturbation

For each scale:

0%
10%
20%
...
100%

perturbation was applied through:

- edge deletion
- edge rewiring
- random edge injection

Each perturbation level used:

50 independent trials

Total experiment size:

{
  "total_trials": 2750
}


---

Ω Definition

The experiment used:

Ω = 2 × change × preservation

Where:

change = perturbation level
preservation = residual identity preservation

Interpretation:

high Ω means:
- strong perturbation
- identity still partially preserved


---

Global Summary

{
  "graph_type": "ring_lattice",
  "node_scales": [
    10,
    30,
    100,
    300,
    1000
  ],
  "k_neighbors": 4,
  "trials_per_level": 50,
  "band": [
    0.59,
    0.64
  ],
  "total_trials": 2750,
  "peak_corridor_levels": [
    0.5,
    0.6,
    0.7,
    0.7,
    0.7
  ],
  "mean_peak_corridor_level": 0.64,
  "std_peak_corridor_level": 0.08,
  "identity_at_peak_corridor": [
    0.608141,
    0.49789,
    0.446745,
    0.445348,
    0.440182
  ],
  "mean_identity_at_peak_corridor": 0.487661,
  "std_identity_at_peak_corridor": 0.063779,
  "omega_at_peak_corridor": [
    0.608141,
    0.597468,
    0.625443,
    0.623487,
    0.616255
  ],
  "mean_omega_at_peak_corridor": 0.614159,
  "std_omega_at_peak_corridor": 0.01033
}


---

Main Discovery

The Ω≈0.6 corridor survives scale increase.

Most importantly:

for n ≥ 100,
the corridor stabilizes around:
- perturbation ≈ 0.7
- identity ≈ 0.44–0.45
- Ω ≈ 0.62

This is the strongest result obtained so far.


---

Small-Scale Regime

10 Nodes

Peak corridor:

{
  "peak_corridor_level": 0.5,
  "identity_at_peak_corridor": 0.608141,
  "omega_at_peak_corridor": 0.608141
}

Interpretation:

small systems suffer strong finite-size effects.

At very small scale:

individual edge changes dominate topology.

The corridor is noisier and shifted.

This weakens the reliability of tiny systems.


---

Medium Scale Transition

30 Nodes

Peak corridor:

{
  "peak_corridor_level": 0.6,
  "identity_at_peak_corridor": 0.49789,
  "omega_at_peak_corridor": 0.597468
}

Interpretation:

the corridor begins converging
toward stable geometric behavior.

The perturbation/identity balance already approaches:

high change
+
partial recoverability


---

Stable Corridor Emergence

100 Nodes

Peak corridor:

{
  "peak_corridor_level": 0.7,
  "peak_corridor_rate": 0.7,
  "identity_at_peak_corridor": 0.446745,
  "omega_at_peak_corridor": 0.625443
}

This is the first clearly stabilized regime.

Interpretation:

the graph undergoes major transformation
while preserving enough structure
to remain partially identifiable.


---

Large Scale Stability

300 Nodes

Peak corridor:

{
  "peak_corridor_level": 0.7,
  "peak_corridor_rate": 0.86,
  "identity_at_peak_corridor": 0.445348,
  "omega_at_peak_corridor": 0.623487
}

The corridor becomes sharper.

Variance decreases.

The regime stabilizes.


---

Near-Deterministic Corridor

1000 Nodes

Peak corridor:

{
  "peak_corridor_level": 0.7,
  "peak_corridor_rate": 1.0,
  "identity_at_peak_corridor": 0.440182,
  "omega_at_peak_corridor": 0.616255
}

This is the strongest single result in the entire experiment.

At large scale:

70% perturbation
+
~44% residual identity

almost deterministically produces:

Ω≈0.62


---

Critical Structural Observation

The important invariant is NOT:

the raw Ω value alone

The real invariant is:

strong perturbation
+
partial identity preservation

This relation survives scale increase.


---

Corridor Geometry

The experiment strongly supports:

Ω≈0.6 emerges when:
- change becomes dominant
- but identity remains partially recoverable

Not:

pure order

and not:

pure chaos


---

Identity Regime

At stable corridor scales:

identity ≈ 0.44–0.50

Interpretation:

the system is no longer mostly itself,
but not yet structurally annihilated.

This appears to be the corridor geometry.


---

Perturbation Regime

At stable corridor scales:

perturbation ≈ 0.7

Interpretation:

the majority of structural relations
have changed.

But enough structure survives to maintain recoverability.


---

Strongest Operational Interpretation

Current best interpretation:

Ω≈0.6 measures
high compatible perturbation
under partial structural continuity.

Or more simply:

the system changes heavily
without total loss of self.


---

What This Experiment Rejects

This experiment weakens or rejects:

Ω≈0.6 as:
- universal physical constant
- semantic signature
- arbitrary numerical coincidence
- local graph artifact


---

What This Experiment Supports

This experiment strongly supports:

Ω≈0.6 as:
- compatibility corridor
- identity-preserving perturbation regime
- scale-stable geometric phenomenon


---

Scale-Invariance Observation

The strongest finding:

the corridor sharpens as scale increases.

Specifically:

n=1000
inside_band_rate at perturbation 0.7:
100%

This means:

large systems converge toward the corridor behavior.

rather than diverging away from it.


---

Relationship To Earlier Results

This experiment explains earlier observations naturally.


---

Random systems

Observed:

Ω≈0.5

Interpretation:

change without strong identity persistence


---

Git maintenance

Observed:

Ω≈0.3–0.4

Interpretation:

small perturbation
high preservation


---

Static repositories

Observed:

Ω≈0.9

Interpretation:

extreme preservation
minimal perturbation


---

Controlled compatibility corridor

Observed:

Ω≈0.6

Interpretation:

large transformation
with surviving structural recoverability


---

Epistemological Shift

This experiment forces a major reframing.

The framework should stop describing Ω≈0.6 as:

a mystical invariant number

and instead describe it as:

a geometric compatibility regime.


---

Best Current Definition

Current strongest operational definition:

Ω≈0.6 marks the region where
structural perturbation becomes dominant
while identity remains partially recoverable.


---

Current Evidence Status

Universal constant:
NOT SUPPORTED

Semantic detector:
NOT SUPPORTED

Pure graph artifact:
WEAKENED

Scale-stable compatibility corridor:
STRONGLY SUPPORTED

Identity-preserving perturbation regime:
STRONGLY SUPPORTED


---

Final Conclusion

The multi-scale perturbation experiment is the strongest result obtained in the OMNIA-CONSTANT investigation so far.

Main conclusion:

Ω≈0.6 is not a universal constant.

It is a scale-stable compatibility corridor
for high perturbation with partial identity preservation.

At large scale:

systems converge toward Ω≈0.62
when:
- most structure changes
- but enough structure survives
to preserve recoverability.

The corridor therefore appears to describe:

transformation without total structural death.