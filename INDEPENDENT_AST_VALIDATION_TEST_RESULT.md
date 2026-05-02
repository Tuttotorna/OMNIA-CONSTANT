# INDEPENDENT AST VALIDATION TEST — RESULT

## Goal

Validate whether Ω correlates with AST deformation metrics even when Ω is computed independently from the AST-based measurements.

This test attempts to break the circularity observed in previous PATCH_GEOMETRY_AST_TEST experiments.

Core question:

```text
Does Ω independently react to structural deformation of code logic?


---

Setup

Repository:

django

Configuration:

commits_loaded = 2500
events          = 2491
windows         = 247
window_size     = 25
window_step     = 10

For each commit window:

Ω was computed independently

AST deformation metrics were extracted separately

Correlations were computed only afterward



---

Metrics

AST Metrics

mean_ast_distance

Approximate structural deformation of AST shape.

mean_depth_delta

Average nesting-depth deformation.

mean_control_delta

Control-flow deformation:

if

elif

try

except

while

for

match

branching structure


mean_node_delta

Raw AST node-count deformation.


---

Correlations

mean_control_delta = 0.376327
mean_node_delta    = 0.368875
mean_ast_distance  = 0.366671
mean_depth_delta   = 0.132138


---

Interpretation

1. AST deformation survives independence

Previous AST experiments contained possible circularity because Ω and AST metrics were partially derived from similar structural primitives.

This experiment removes that dependency.

Result:

The signal remains.

This is the first strong indication that Ω is sensitive to intrinsic computational deformation rather than repository metadata.


---

2. Control-flow deformation is the strongest signal

The dominant surviving metric is:

mean_control_delta = 0.376327

This suggests:

Ω reacts more strongly to changes in execution structure
than to file topology or repository history.

In practical terms:

changing strings matters little

changing imports matters little

changing repository centrality matters little


But:

changing the decision structure of code
produces measurable Ω increase


---

3. Repository-level explanations continue to fail

Earlier hypotheses tested:

Hypothesis	Result

File count / churn	Weak
Modular dispersion	Weak
Import graph centrality	Weak
Historical co-change	Weak
Commit surprise	Weak


Only AST deformation remains consistently explanatory.


---

4. Depth alone is insufficient

mean_depth_delta = 0.132138

This is much weaker.

Meaning:

Ω is not simply reacting to nesting depth.

Instead:

Ω reacts to deformation of computational pathways.

This is important.

It suggests Ω is sensitive to logical branching complexity rather than indentation geometry alone.


---

Working Hypothesis

Current strongest interpretation:

Ω measures structural stress induced by computational-flow deformation.

Or more precisely:

Ω appears partially sensitive to transformations
that alter execution topology.


---

Important Limitation

This is NOT proof that:

Ω = AST deformation

Only:

AST deformation is a viable explanatory component.

Further falsification is still required.


---

Most Important Result

This experiment demonstrates:

Ω is not well explained by:
- quantity
- repository position
- historical memory
- static centrality

but shows measurable sensitivity to:
- logical deformation
- execution-structure modification
- control-flow perturbation


---

Proposed Next Step

CONTROL_FLOW_ABLATION_TEST

Separate commits into categories:

A:
commits that modify control-flow structures

B:
commits that avoid control-flow changes

Then compare Ω distributions.

Core question:

Does Ω systematically increase
when control-flow structures are modified?

This is stronger than correlation analysis.

It becomes a structural discrimination test.


---

Current Status of OMNIA

Current evidence suggests:

Ω behaves less like a repository metric
and more like a local computational stress signal.

The strongest surviving candidate mechanism is now:

execution-topology deformation