# OMNIA-CONSTANT Results Index

## Purpose

This file gives a public entrypoint into OMNIA-CONSTANT result reports.

## Main result families

### Candidate region / discovery scans

Relevant files:

- `results/FIRST_DISCOVERY_SCAN.md`
- `results/CONFIRMED_CANDIDATE_REGION.md`
- `results/NARROW_BAND_SENSITIVITY_RESULT.md`
- `results/DUPLICATE_AWARE_SCAN_RESULT.md`
- `results/SOURCE_GROUP_SCAN_RESULT.md`

Purpose:

- identify and stress-test candidate Ω regions
- check whether recurrent bands survive filtering and source grouping

### Random / null baselines

Relevant files:

- `results/NULL_RANDOM_BASELINE_RESULT.md`
- `results/INVARIANCE_RANDOM_TRAJECTORY_BASELINE_RESULT.md`

Purpose:

- test whether observed Ω behavior collapses under random or null baselines

### Patch geometry and AST deformation

Relevant files:

- `results/PATCH_GEOMETRY_TEST_RESULT.md`
- `results/PATCH_GEOMETRY_AST_TEST_RESULT.md`
- `papers/PATCH_GEOMETRY_TEST_RESULT.md`
- `papers/PATCH_GEOMETRY_AST_TEST_RESULT.md`
- `papers/INDEPENDENT_AST_VALIDATION_TEST_RESULT.md`

Purpose:

- test whether Ω is sensitive to observable code-form deformation

### Control-flow and semantic invariance

Relevant files:

- `results/CONTROL_FLOW_ABLATION_TEST_RESULT.md`
- `papers/CONTROL_FLOW_ABLATION_TEST_RESULT.md`
- `papers/SEMANTIC_INVARIANCE_TEST_RESULT.md`
- `docs/OMNIA_SEMANTIC_INVARIANCE_PROTOCOL_v0.md`

Purpose:

- test whether Ω is explained by control-flow alone
- test whether Ω behaves like semantic correctness

### Co-change and topology

Relevant files:

- `results/COCHANGE_TOPOLOGY_TEST_RESULT.md`
- `results/COMMIT_LEVEL_COCHANGE_SURPRISE_TEST_RESULT.md`
- `papers/COCHANGE_TOPOLOGY_TEST_RESULT.md`
- `papers/COMMIT_LEVEL_COCHANGE_SURPRISE_TEST_RESULT.md`

Purpose:

- test whether Ω is reducible to historical co-change or topology memory

## Reading rule

```text
result report = falsification evidence
negative result = boundary evidence
candidate region = hypothesis, not final law
No universal structural constant is declared.
```
