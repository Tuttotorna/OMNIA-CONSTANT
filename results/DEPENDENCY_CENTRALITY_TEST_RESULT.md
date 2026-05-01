# DEPENDENCY CENTRALITY TEST RESULT

## Purpose

Test whether Ω correlates with dependency centrality in a real software repository.

Core question:

```text
Does Ω increase when commits modify files
that are central in the dependency/import graph?


---

Repository

django

Reason for selection:

Python import structure is directly inspectable
through AST-based import parsing.


---

Hypothesis

If Ω measures architectural pressure, then changes to highly central files should produce higher Ω.

Expected signal:

high Ω
+
high dependency centrality

Measured centrality variables:

- pagerank_mean
- pagerank_max
- pagerank_std
- in_degree_mean
- out_degree_mean

Control variable:

files_changed_mean


---

Experimental Setup

{
  "repo": "django",
  "window_size": 25,
  "window_step": 10,
  "events": 755,
  "windows": 74
}


---

Results

{
  "correlations": {
    "pagerank_mean": 0.045225,
    "pagerank_max": 0.047453,
    "pagerank_std": 0.049522,
    "in_degree_mean": 0.043386,
    "out_degree_mean": -0.096097,
    "files_changed_mean": -0.119949
  },
  "strengths": {
    "pagerank_mean": "weak",
    "pagerank_max": "weak",
    "pagerank_std": "weak",
    "in_degree_mean": "weak",
    "out_degree_mean": "weak",
    "files_changed_mean": "weak"
  }
}


---

Main Result

The dependency-centrality hypothesis is not supported by this v0 test.

Observed correlations are all weak:

pagerank_mean   = 0.045
pagerank_max    = 0.047
pagerank_std    = 0.050
in_degree_mean  = 0.043
out_degree_mean = -0.096
files_changed   = -0.120

This means:

Ω does not currently show meaningful correlation
with dependency centrality in this test.


---

Important Technical Limitation

The result is negative, but not final.

The import graph appears too weak or under-resolved.

Evidence:

in_degree_mean = 0

in the top high-Ω windows.

Also:

PageRank values are nearly uniform

around:

0.00006–0.00007

This suggests the dependency graph did not capture enough real structure.


---

Likely Causes

Possible causes:

- relative imports were not fully resolved
- module matching was too approximate
- many changed files were not mapped to modules
- external imports dominated parsing noise
- internal Django imports were under-detected
- PageRank collapsed toward uniformity
- graph sparsity reduced centrality signal

Therefore this test should be interpreted as:

negative with current graph construction

not:

final disproof of dependency centrality.


---

Top High-Ω Windows

The highest-Ω windows did not show high centrality.

Example pattern:

high Ω
low PageRank
low in-degree
low files changed

This reinforces two points:

1. Ω is not explained by simple file count.
2. v0 dependency centrality did not explain Ω either.


---

Interpretation

The current test rejects the simple version of the hypothesis:

Ω = dependency centrality of changed files

At least with this v0 import graph.

However, because graph quality is questionable, the stronger claim:

Ω is unrelated to dependency structure

is not justified yet.


---

Scientific Status

Dependency centrality hypothesis:
NOT SUPPORTED BY v0

Strong disproof:
NOT ACHIEVED

Graph quality:
INSUFFICIENT / SUSPECT

Result type:
NEGATIVE-INCONCLUSIVE


---

Why This Result Matters

This result is important because it prevents premature narrative inflation.

It shows that the framework does not automatically confirm every structural hypothesis.

That increases credibility.

A serious investigation must preserve:

positive results
negative results
inconclusive results
technical limitations

This test belongs in that category.


---

Methodological Lesson

Before using dependency centrality as an explanatory variable, the dependency graph must be validated.

The next necessary step is not another centrality test.

The next necessary step is:

IMPORT_GRAPH_QUALITY_TEST


---

Required Next Test

IMPORT_GRAPH_QUALITY_TEST

Purpose:

Determine whether the extracted import graph
is structurally informative enough
to support centrality analysis.

Required metrics:

- node count
- edge count
- edge density
- isolated node rate
- resolved import rate
- internal import rate
- in-degree distribution
- out-degree distribution
- PageRank variance
- largest component size

Only after this can dependency centrality be tested seriously.


---

Current Best Conclusion

The Dependency Centrality Test v0 does not support the hypothesis that Ω correlates with import-graph centrality.

But because the graph appears under-resolved, the result is best classified as:

negative / technically inconclusive

Final statement:

With the current import graph construction,
dependency centrality does not explain Ω.
A better graph-quality validation is required
before the hypothesis can be fairly tested.