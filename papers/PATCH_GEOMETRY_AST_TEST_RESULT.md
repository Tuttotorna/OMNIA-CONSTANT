# PATCH GEOMETRY TEST v1 — AST DEFORMATION

## Goal

Test whether Ω correlates with structural deformation inside the Abstract Syntax Tree (AST) of source code.

This experiment moves beyond repository topology and patch size to investigate syntactic and control-flow deformation.

---

# Repository

```text
django


---

Dataset Summary

{
  "commits_loaded": 2500,
  "events": 1589,
  "windows": 157,
  "window_size": 25,
  "window_step": 10
}


---

Tested Variables

The following AST deformation metrics were measured:

mean_ast_distance

max_ast_distance

mean_depth_delta

mean_control_delta

mean_node_delta



---

Correlation Results

Metric	Correlation with Ω

mean_ast_distance	0.481167
max_ast_distance	0.442659
mean_depth_delta	0.221923
mean_control_delta	0.514636
mean_node_delta	0.479731



---

Main Observations

Strongest signal

The strongest observed signal was:

mean_control_delta → 0.514636

This suggests that Ω reacts strongly to control-flow deformation.

Changes affecting:

if

for

while

try

match


appear more structurally disruptive than purely linear modifications.


---

AST-wide deformation

Both:

mean_ast_distance

mean_node_delta


also produced strong correlations.

This suggests that Ω reacts not only to branching logic, but to broader syntactic restructuring.


---

Weak nesting signal

The weakest signal was:

mean_depth_delta → 0.221923

This weakens the hypothesis that Ω primarily measures nesting complexity.

Observed evidence instead points toward transformation of execution structure.


---

Interpretation

This experiment shifts the explanatory center of Ω from:

repository topology

commit history

graph structure


toward:

AST deformation

control-flow restructuring

representational morphology


The evidence suggests that Ω behaves more like a measure of structural perturbation than semantic correctness.


---

Important Boundary

This experiment does not demonstrate semantic understanding.

AST deformation and semantic meaning are not equivalent.

Observed correlations may reflect structural transformation intensity rather than logical correctness.


---

Current Working Hypothesis

Ω appears sensitive to representational deformation
inside executable structure.

More specifically:

branch restructuring

control-flow alteration

node-level AST transformation


currently produce the strongest observable signals.


---

Important Limitation

This experiment still depends on AST-derived proxy measurements.

Further independent validation is required to establish whether Ω captures an independent structural property.


---

Status

Exploratory
Strong preliminary signal
Requires independent validation