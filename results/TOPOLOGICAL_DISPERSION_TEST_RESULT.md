# TOPOLOGICAL DISPERSION TEST RESULT

## Purpose

Determine whether Ω correlates with the topological dispersion of changes across repository structure.

Core question:

```text
Does Ω increase when modifications
are distributed across distant regions
of a software system?

This experiment attempts to distinguish between:

quantity of change

and:

geometric distribution of change


---

Scientific Motivation

Previous experiments demonstrated:

Ω is not strongly reducible to:
- files changed
- lines added
- lines deleted
- author entropy

This suggested that Ω may encode:

structural organization

rather than simple activity magnitude.

The next hypothesis became:

Ω may react to topological dispersion.


---

Core Hypothesis

If Ω measures structural interference, then:

small changes distributed across distant
regions of the system

should produce higher Ω than:

large localized changes


---

Experimental Design

For each sliding commit window:

measure:
- Ω
- module dispersion
- path entropy
- directory spread
- path depth
- path variance
- pairwise path distance

Then compute:

corr(Ω, metric)


---

Dataset

Repositories analyzed:

django
react
numpy
atom
brackets
phonegap

Total windows analyzed:

634


---

Window Parameters

window_size = 25 commits
window_step = 10 commits


---

Topological Variables

file_count

Total changed files


---

top_module_count

Number of distinct top-level modules/directories


---

second_module_count

Number of distinct second-level module regions


---

top_module_entropy

Entropy of change distribution
across top-level modules


---

second_module_entropy

Entropy of change distribution
across second-level modules


---

mean_path_depth

Average filesystem path depth

Example:

src/core/parser/runtime/file.py

has greater depth than:

docs/readme.md


---

path_depth_std

Variance of path depths

Measures structural heterogeneity.


---

pairwise_path_distance

Approximate geometric distance
between changed files

Based on shared path prefixes.


---

single_module_concentration

Fraction of changes concentrated
inside one dominant module


---

Global Summary

{
  "repos": [
    "django",
    "react",
    "numpy",
    "atom",
    "brackets",
    "phonegap"
  ],
  "window_size": 25,
  "window_step": 10,
  "total_windows": 634,
  "correlations": {
    "file_count": 0.126318,
    "mean_files_per_commit": 0.126318,
    "top_module_count": -0.035594,
    "second_module_count": 0.084344,
    "top_module_entropy": 0.016554,
    "second_module_entropy": -0.247787,
    "mean_path_depth": 0.371249,
    "path_depth_std": 0.346505,
    "pairwise_path_distance": -0.058722,
    "single_module_concentration": -0.038529
  },
  "controlled_correlations": {
    "mean_files_per_commit_controlled_for_file_count": 0.071231,
    "top_module_count_controlled_for_file_count": -0.073262,
    "second_module_count_controlled_for_file_count": 0.020805,
    "top_module_entropy_controlled_for_file_count": 0.061688,
    "second_module_entropy_controlled_for_file_count": -0.220456,
    "mean_path_depth_controlled_for_file_count": 0.353012,
    "path_depth_std_controlled_for_file_count": 0.32677,
    "pairwise_path_distance_controlled_for_file_count": -0.051496,
    "single_module_concentration_controlled_for_file_count": -0.066597
  }
}


---

Primary Result

The original hypothesis:

Ω = topological dispersion

is NOT strongly supported.

Most dispersion-related variables show weak correlations.

Examples:

top_module_count       = -0.036
pairwise_path_distance = -0.059
module concentration   = -0.039

These values are close to noise level.


---

Important Negative Result

This experiment does NOT support:

Ω simply increases
when changes are spread across modules.

The expected signature of strong geometric dispersion was absent.


---

Unexpected Positive Signal

Two variables showed moderate correlation:

mean_path_depth = 0.371
path_depth_std  = 0.347

Even after controlling for file count:

mean_path_depth controlled = 0.353
path_depth_std controlled  = 0.327

This is the strongest signal in the experiment.


---

Interpretation

Ω appears more sensitive to:

structural depth

than to:

horizontal module dispersion.

In practice:

deep infrastructural regions

correlate more with elevated Ω than:

broad distribution across modules.


---

Possible Meaning

This suggests Ω may react to:

nested structural layers

rather than:

simple spatial spread.

Potential interpretations:

- infrastructure sensitivity
- deep dependency chains
- architectural nesting
- hidden coupling layers
- stratified structural complexity


---

Critical Scientific Boundary

This experiment does NOT prove:

Ω measures architecture

nor:

Ω measures dependency depth

However, it DOES suggest:

Ω is more sensitive to vertical structure
than horizontal dispersion.


---

High Ω / Low Churn Windows

Several windows exhibited:

high Ω
+
low file count

Examples include:

Atom
React
PhoneGap

These windows often displayed:

- deep paths
- heterogeneous nesting
- high path depth variance

despite relatively modest churn.

This reinforces the earlier conclusion:

Ω is not reducible to raw activity volume.


---

Important Epistemological Shift

Before this experiment:

possible interpretation:
Ω = dispersion metric

After this experiment:

better interpretation:
Ω may reflect structural stratification.

This is a major conceptual refinement.


---

What Was NOT Confirmed

Not confirmed:

- broad module spread
- wide path separation
- distributed module entropy

as dominant explanations for Ω.


---

What Was Partially Supported

Partially supported:

- deep structural nesting
- path hierarchy complexity
- infrastructural depth

as contributors to Ω behavior.


---

Current Best Interpretation

The strongest currently supported interpretation is:

Ω reacts more strongly
to changes occurring in deeper,
more stratified structural regions
than to simple module dispersion.


---

Scientific Consequence

This result weakens the hypothesis:

Ω = dispersion of change

but strengthens a more subtle possibility:

Ω may encode interaction with
structural depth layers.


---

Next Logical Experiment

The next experiment should focus on:

STRUCTURAL DEPTH TEST

Core question:

Does Ω increase when modifications
occur closer to infrastructural,
deeply nested,
or dependency-critical regions?

Potential future variables:

- import graph centrality
- dependency depth
- call graph position
- infrastructure/core proximity
- architectural criticality


---

Final Conclusion

The Topological Dispersion Test produced a mixed result.

Not Supported

Ω is not strongly explained
by broad topological dispersion
across repository modules.


---

Partially Supported

Ω shows moderate correlation
with structural depth metrics.

Especially:

- mean path depth
- path depth variance

even after controlling for file count.


---

Current Best Summary

At this stage, Ω appears less like:

a module spread metric

and more like:

a latent structural-depth coordinate
sensitive to nested architectural regions.