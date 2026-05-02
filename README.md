# OMNIA-CONSTANT

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19970512.svg)](https://doi.org/10.5281/zenodo.19970512)

**OMNIA-CONSTANT** is a post-analysis and falsification repository for the experimental results emerging from **OMNIA-INVARIANCE**.

It investigates whether the observed Ω regions, especially the recurrent Ω≈0.6 corridor, behave as meaningful structural transition regimes or collapse as artifacts of measurement.

No universal structural constant is declared.

---

# Current Position

This repository does **not** claim that Ω is a universal constant.

Current evidence supports a more careful interpretation:

```text
Ω appears to behave as a structural / morphological perturbation signal.

In the tested software experiments, Ω is more strongly associated with changes in observable code form than with semantic correctness.

The current working hypothesis is:

Ω measures representational and morphological deformation,
not semantic truth.


---

What This Repository Tests

This repository explores whether Ω can be reduced to simpler explanations such as:

churn

file count

line count

dependency centrality

import graph topology

historical co-change

commit novelty

control-flow mutation alone

semantic correctness


Most reduction attempts produced weak or incomplete explanations.

The strongest surviving direction is:

local structural deformation of the transformation itself

especially:

patch geometry

AST deformation

control-flow restructuring

representational compression / expansion

morphological perturbation



---

Important Boundary

OMNIA-CONSTANT does not claim that Ω detects:

bugs

correctness

semantic equivalence

logical truth

program intent

runtime behavior


The semantic invariance test produced a critical negative result:

semantic-preserving transformations sometimes produced larger ΔΩ
than semantic-changing transformations.

This means Ω should not currently be interpreted as a semantic correctness signal.

Instead, the evidence suggests that Ω reacts to how strongly the observable structure is transformed.


---

Why This Matters

Many software transformations preserve behavior while strongly changing representation.

Examples include:

refactoring

code compression

AST reshaping

AI-generated rewrites

representation normalization

structural simplification


A morphology-sensitive structural score may help measure:

refactoring intensity

representational stability

structural drift

AI-generated code rewrite impact

transformation violence

local structural perturbation


This is not semantic verification.

It is structural measurement.


---

Research Status

Current status:

exploratory
falsification-oriented
non-final

The repository is built around negative and positive results.

Negative results are preserved because they define what Ω is not.

This is central to the methodology.


---

Main Experimental Findings

1. Churn and file count are insufficient

Ω was not strongly explained by:

number of files changed

lines added

lines deleted

basic churn metrics


These variables produced weak or incomplete explanations.


---

2. Static dependency centrality is insufficient

Import graph centrality and PageRank did not explain Ω.

A separate import graph quality test showed that the Django import graph was structurally usable, so the weak result could not simply be dismissed as parser failure.

Conclusion:

Ω is not reducible to static dependency centrality.


---

3. Historical co-change is insufficient

Both window-level and commit-level co-change surprise tests produced weak results.

Ω did not strongly correlate with:

historical co-change novelty

pair surprise

co-change density

repository memory


Conclusion:

Ω is not explained by historical file-pair memory.


---

4. Patch geometry is partially informative

Patch-level measurements showed moderate associations with:

hunk count

file count

deleted lines

total changes


However, this result is partially coupled to proxy construction and should not be overinterpreted.

Conclusion:

patch geometry is relevant,
but not sufficient as a full explanation.


---

5. AST deformation is the strongest current signal

AST-based experiments produced the strongest observed signals.

Especially relevant:

AST node deformation

control-flow deformation

node-count variation


Independent AST validation preserved a moderate signal:

mean_control_delta ≈ 0.376
mean_node_delta    ≈ 0.369
mean_ast_distance  ≈ 0.367

Conclusion:

Ω appears partially sensitive to executable structural deformation.


---

6. Control-flow contributes but does not explain Ω

The control-flow ablation test showed that commits modifying control-flow had higher Ω on average.

However, high-Ω commits also appeared without control-flow changes.

Conclusion:

control-flow deformation contributes to Ω,
but Ω is not reducible to control-flow alone.


---

7. Semantic invariance test failed

The semantic invariance test showed that the tested proxy reacted more strongly to representational changes than to semantic changes.

Example:

if flag:
    return True
else:
    return False

to:

return bool(flag)

produced larger ΔΩ than some meaning-changing edits such as:

if a and b:
    run()

to:

if a or b:
    run()

Conclusion:

Ω should not be treated as a semantic correctness metric.


---

Current Working Hypothesis

The current best interpretation is:

Ω behaves as a morphology-sensitive structural perturbation measure.

More specifically:

Ω appears to measure observable transformation stress
in the representation of a system.

In software, this means Ω may react to:

AST reshaping

control-flow restructuring

representational compression

representational expansion

local structural deformation

transformation intensity


It does not currently demonstrate semantic understanding.


---

Research Files

The current research track is organized under:

papers/

Recommended structure:

papers/
├── README.md
├── OMNIA_MORPHOLOGICAL_PERTURBATION_ABSTRACT.md
├── PATCH_GEOMETRY_TEST_RESULT.md
├── PATCH_GEOMETRY_AST_TEST_RESULT.md
├── INDEPENDENT_AST_VALIDATION_TEST_RESULT.md
├── CONTROL_FLOW_ABLATION_TEST_RESULT.md
├── SEMANTIC_INVARIANCE_TEST_RESULT.md
├── COCHANGE_TOPOLOGY_TEST_RESULT.md
└── COMMIT_LEVEL_COCHANGE_SURPRISE_TEST_RESULT.md


---

Core Abstract

See:

papers/OMNIA_MORPHOLOGICAL_PERTURBATION_ABSTRACT.md

Summary:

Ω should not be interpreted as a semantic correctness signal.
The current evidence supports a narrower interpretation:
Ω is sensitive to representational deformation,
syntactic restructuring,
and morphological changes in code form.


---

Methodological Principle

This repository follows a falsification-first approach.

The goal is not to force Ω into a preferred interpretation.

The goal is to eliminate weak explanations.

Preserved negative results include:

failed semantic interpretation

weak co-change explanation

weak static centrality explanation

incomplete control-flow reduction

incomplete churn reduction


This is intentional.


---

What OMNIA-CONSTANT Is Not

OMNIA-CONSTANT is not:

a proof of a universal software constant

a semantic analyzer

a bug detector

a correctness verifier

a replacement for tests

a replacement for static analysis

a compiler-level semantic engine



---

What OMNIA-CONSTANT Is

OMNIA-CONSTANT is currently best understood as:

a falsification-oriented research repository
for studying whether Ω behaves as a structural perturbation signal.

Its current strongest interpretation is:

morphological perturbation measurement.


---

Next Research Directions

Future work should test:

semantic-preserving refactoring families

cross-language representation changes

runtime-equivalence controlled pairs

AI-generated code rewrites

bug-fixing vs bug-introducing commits

revert prediction

regression prediction

transformation stability across programming languages


The most important next validation step is:

controlled semantic-preserving refactoring
with independent runtime equivalence checks.


---

Current Verdict

No structural constant is declared.

Ω≈0.6 remains an observed structural corridor
under specific experimental conditions.

The broader and more defensible result is that Ω
appears to behave as a structural / morphological
perturbation signal rather than a semantic metric.


---

License

Add the repository license here.


---

Related

OMNIA-INVARIANCE

OMNIA

OMNIABASE

Logical Origin Node / MB-X.01
Author Brighindi Massimiliano 
Contact brighissimo@gmail.com