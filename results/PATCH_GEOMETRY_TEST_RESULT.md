# PATCH_GEOMETRY_TEST_RESULT

## Purpose

Investigate whether Ω correlates with the internal geometry of patches rather than:

```text
- repository history
- co-change memory
- static topology
- centrality
- churn alone

Core question:

Does Ω react to the internal structure of the diff itself?

This experiment marks a transition from:

repository-level topology

to:

patch-level structural geometry


---

Important Methodological Note

This v0 experiment uses a simplified Ω proxy partially constructed from patch properties.

The Ω proxy includes:

- file count
- hunk count
- add/delete balance

Therefore:

some correlations are partially circular

This result is informative but not definitive.

The test should be interpreted as:

exploratory structural validation

not final causal proof.


---

Repository

django


---

Dataset

{
  "commits_loaded": 2500,
  "events": 2499,
  "windows": 248,
  "window_size": 25,
  "window_step": 10
}


---

Metrics Tested

Patch Geometry Variables

file_count
hunk_count
added_lines
deleted_lines
total_changes
add_delete_ratio
edit_dispersion
hunk_distance_mean
hunk_distance_std
mean_path_depth


---

Correlation Results

{
  "file_count": 0.478728,
  "hunk_count": 0.435468,
  "added_lines": 0.341131,
  "deleted_lines": 0.468651,
  "total_changes": 0.410162,
  "add_delete_ratio": -0.341421,
  "edit_dispersion": -0.000917,
  "hunk_distance_mean": 0.057672,
  "hunk_distance_std": 0.1416,
  "mean_path_depth": 0.11316
}


---

First Observation

The strongest correlations are:

file_count      = 0.478728
deleted_lines   = 0.468651
hunk_count      = 0.435468
total_changes   = 0.410162

Moderate signal exists for:

added_lines     = 0.341131
add_delete_ratio = -0.341421

Weak or near-zero signal:

edit_dispersion    = -0.000917
hunk_distance_mean = 0.057672
hunk_distance_std  = 0.141600
mean_path_depth    = 0.113160


---

Immediate Interpretation

This suggests that the Ω proxy reacts strongly to:

patch magnitude
patch fragmentation
modification density

More specifically:

many files
many hunks
many deletions
large structural diffs

appear associated with higher Ω.


---

Critical Caveat

The Ω proxy itself was defined using:

files
hunks
add/delete balance

Therefore:

part of the observed correlation is expected by construction.

This means:

the result is partially circular.


---

What This Test Actually Demonstrates

This test DOES support:

patch geometry is a plausible explanatory direction.

But it DOES NOT yet prove:

real OMNIA Ω is reducible to patch geometry.

The distinction is critical.


---

Unexpected Negative Results

Several previously promising hypotheses weakened significantly:

1. Edit Dispersion

edit_dispersion = -0.000917

Almost zero.

Meaning:

spreading edits across many hunks
does not strongly affect Ω in this implementation.


---

2. Hunk Distance

hunk_distance_mean = 0.057672
hunk_distance_std  = 0.141600

Very weak.

Meaning:

physical spacing between edit blocks
is not currently a strong signal.


---

3. Mean Path Depth

mean_path_depth = 0.113160

Surprisingly weak here.

This is important because:

path depth survived earlier tests.

Possible explanation:

the simplified Ω proxy diluted the structural-depth effect.


---

Emerging Pattern

The surviving signal appears closer to:

patch intensity

than:

patch spatial topology.

This is an important conceptual shift.


---

Interpretation of add_delete_ratio

add_delete_ratio = -0.341421

Negative correlation means:

deletion-heavy patches tend to associate with higher Ω.

Possible interpretation:

destructive structural transformations
create stronger perturbations
than additive ones.

Potentially:

removing structure creates more instability
than extending structure.

This is one of the most interesting observations in the test.


---

Top High-Ω Windows

Example

{
  "window_index": 83,
  "mean_omega": 0.49894872,
  "file_count": 24.08,
  "hunk_count": 67.76,
  "added_lines": 199.2,
  "deleted_lines": 124.56,
  "total_changes": 323.76,
  "edit_dispersion": 0.286192,
  "hunk_distance_mean": 7.125603,
  "hunk_distance_std": 5.683965,
  "mean_path_depth": 3.026863
}

Interpretation:

large multi-hunk structural modifications
associate with elevated Ω.


---

Example

{
  "window_index": 65,
  "mean_omega": 0.45453776,
  "file_count": 9.44,
  "hunk_count": 57.28,
  "added_lines": 97.12,
  "deleted_lines": 118.24,
  "total_changes": 215.36,
  "hunk_distance_mean": 12.353098,
  "hunk_distance_std": 9.390112
}

Interpretation:

large fragmented diffs correlate with elevated Ω,
but fragmentation alone is not sufficient.


---

Scientific Interpretation

This experiment weakens the idea that Ω depends on:

historical relationships between files.

Instead, it strengthens the idea that Ω reacts to:

the local geometry of the transformation itself.

Potential interpretation:

Ω measures transformation stress
rather than repository memory.


---

Updated Reduction Table

Candidate Explanation	Status

Churn / file count	Partially supported
Lines added/deleted	Partially supported
Module dispersion	Not supported
Static centrality	Not supported
Co-change topology	Not supported
Historical surprise	Not supported
Patch geometry	Supported (partially circular)
Edit dispersion	Weak
Hunk distance	Weak



---

Current Best Interpretation

The current evidence suggests:

Ω may react to:
- structural intensity
- destructive edits
- multi-hunk transformations
- transformation magnitude

more than:

- repository topology
- historical co-change
- static graph structure


---

Key Limitation

This test cannot establish causality because the Ω proxy itself uses patch-derived quantities.

Therefore:

PATCH_GEOMETRY_TEST v0
is exploratory only.


---

Required Next Step

A valid next experiment requires:

real OMNIA Ω
vs
independent patch geometry metrics

or at minimum:

a proxy Ω independent from:
- file count
- hunk count
- line counts

This becomes:

PATCH_GEOMETRY_TEST v1


---

Recommended v1 Metrics

- token entropy
- AST edit distance
- syntax fragmentation
- nesting depth
- indentation deformation
- lexical disruption
- symbol replacement rate
- control-flow deformation

while keeping Ω independent from those metrics.


---

Structural Conclusion

This test narrows the search space significantly.

The evidence now suggests:

Ω is unlikely to be explained by:
- repository history
- co-change memory
- static topology

The strongest remaining direction is:

internal geometry of the transformation itself.

However:

the current evidence is not yet sufficient
to reduce Ω to patch geometry.


---

Final Status

PATCH_GEOMETRY_TEST v0:
PARTIALLY SUPPORTED
(BUT PARTIALLY CIRCULAR)

Scientifically useful because it redirects the investigation toward:

micro-structural transformation mechanics

rather than repository-scale topology.