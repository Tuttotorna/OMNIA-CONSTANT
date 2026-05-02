# INDEPENDENT AST VALIDATION TEST

## Goal

Test whether Ω still correlates with AST deformation metrics when measured independently from the original proxy construction process.

This experiment attempts to reduce coupling between Ω and AST-derived measurements.

---

# Repository

```text
django


---

Dataset Summary

{
  "commits_loaded": 2500,
  "events": 2491,
  "windows": 247,
  "window_size": 25,
  "window_step": 10
}


---

Tested Variables

The following independently measured AST metrics were evaluated:

mean_ast_distance

mean_depth_delta

mean_control_delta

mean_node_delta



---

Correlation Results

Metric	Correlation with Ω

mean_ast_distance	0.366671
mean_depth_delta	0.132138
mean_control_delta	0.376327
mean_node_delta	0.368875



---

Main Observations

Signal survives independence test

The strongest signal remained:

mean_control_delta → 0.376327

This is weaker than the previous AST deformation test, but importantly:

the signal survives after partial decoupling.

This weakens the hypothesis that previous correlations were purely circular artifacts.


---

Structural deformation remains relevant

Both:

mean_ast_distance

mean_node_delta


remain moderately correlated with Ω.

This suggests that representational restructuring still contributes meaningful signal even under more independent measurement conditions.


---

Nesting depth remains weak

The weakest signal again appears in:

mean_depth_delta → 0.132138

This weakens the idea that Ω primarily measures nesting complexity or indentation depth.


---

Interpretation

The experiment supports a narrower and more defensible interpretation:

Ω appears sensitive to executable structural deformation,
especially control-flow restructuring.

However:

Ω does not appear reducible to any single AST metric.

Observed evidence suggests an emergent interaction between:

AST restructuring

execution topology

representational compression

local transformation intensity



---

Important Boundary

This experiment does not establish causation.

It also does not demonstrate:

semantic understanding

bug detection

correctness verification

execution equivalence reasoning


Observed signals remain structural and morphological.


---

Current Working Hypothesis

Ω behaves as a morphology-sensitive perturbation measure
rather than a semantic metric.

The strongest surviving signals currently emerge from:

control-flow deformation

AST restructuring

node-level transformation intensity



---

Important Limitation

Although partially decoupled, AST-derived measurements may still share hidden dependencies with Ω.

Further falsification-oriented testing remains necessary.


---

Status

Independent validation passed partially
Signal reduced but preserved
Further testing required