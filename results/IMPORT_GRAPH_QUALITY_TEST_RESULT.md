# IMPORT GRAPH QUALITY TEST RESULT

## Purpose

Validate whether the extracted Django dependency/import graph contains enough structural information to support meaningful centrality analysis.

Core question:

```text
Is the graph structurally informative,
or is it too sparse / fragmented / uniform
to support dependency-centrality experiments?

This test was required after the initial Dependency Centrality Test produced weak correlations and suspiciously uniform PageRank distributions.


---

Repository

django


---

Experimental Goal

Before testing whether Ω correlates with dependency centrality, the dependency graph itself must be validated.

This test evaluates:

- graph connectivity
- hierarchy
- centrality distribution
- import resolution quality
- structural richness

without using Ω.


---

Summary

{
  "repo": "django",
  "basic_structure": {
    "python_files": 2903,
    "node_count": 2903,
    "edge_count": 8521,
    "density": 0.001011454
  },
  "connectivity": {
    "isolated_node_count": 685,
    "isolated_node_rate": 0.235963,
    "weak_component_count": 689,
    "strong_component_count": 2795,
    "largest_weak_component_size": 2212,
    "largest_weak_component_rate": 0.76197,
    "largest_strong_component_size": 36,
    "largest_strong_component_rate": 0.012401
  },
  "degree_distribution": {
    "in_degree_mean": 2.935239,
    "in_degree_median": 0,
    "in_degree_std": 24.765311,
    "in_degree_max": 785,
    "out_degree_mean": 2.935239,
    "out_degree_median": 2,
    "out_degree_std": 3.605495,
    "out_degree_max": 35,
    "total_degree_mean": 5.870479,
    "total_degree_median": 3,
    "total_degree_std": 25.228172,
    "total_degree_max": 788
  },
  "pagerank": {
    "pagerank_mean": 0.000344471237,
    "pagerank_median": 0.000118344487,
    "pagerank_std": 0.002108359757,
    "pagerank_variance": 4.44518086612e-06,
    "pagerank_entropy_normalized": 0.766789,
    "top_to_median_ratio": 441.804308
  },
  "import_resolution": {
    "raw_import_count": 11790,
    "resolved_internal_count": 8803,
    "unresolved_internal_count": 5,
    "external_import_count": 2982,
    "relative_import_count": 1106,
    "absolute_import_count": 10684,
    "resolved_internal_rate": 0.74665,
    "unresolved_internal_rate": 0.000424,
    "external_import_rate": 0.252926,
    "relative_import_rate": 0.093808,
    "absolute_import_rate": 0.906192
  },
  "quality_assessment": {
    "graph_quality_class": "usable",
    "failure_flags": []
  }
}


---

Main Result

The dependency graph is structurally usable.

This is a strong reversal of the previous suspicion that the graph was too weak to support centrality analysis.

The graph shows:

- real hierarchy
- non-uniform centrality
- strong giant component
- heavy-tailed degree distribution
- high internal import resolution

Most importantly:

graph_quality_class = usable
failure_flags = []


---

Connectivity Analysis

Giant Component

Largest weakly connected component:

2212 / 2903 nodes
= 76.2%

This means the graph contains a dominant structural backbone.

The system is not fragmented into tiny isolated islands.


---

Isolated Nodes

isolated_node_rate = 23.6%

This is non-trivial but acceptable for a large real-world Python repository.

Many isolated nodes are likely:

- tests
- scripts
- utility modules
- standalone tooling

The graph remains globally coherent.


---

Degree Distribution

The graph exhibits strong hierarchy.

Evidence:

in_degree_max = 785
in_degree_std = 24.76
median_in_degree = 0

This is extremely important.

A flat or uniform graph would produce:

low variance
low maxima
uniform degree spread

Instead, Django shows:

few highly central modules
many low-degree leaf modules

which is exactly what a real software dependency graph should look like.


---

PageRank Analysis

The earlier dependency-centrality failure was suspected to be caused by near-uniform PageRank.

This suspicion is now falsified.

Evidence:

top_to_median_ratio = 441.8

This is enormous.

Meaning:

top nodes are hundreds of times more central
than median nodes.

Also:

pagerank_std = 0.002108

and:

pagerank_entropy_normalized = 0.766

confirm substantial centrality structure.


---

Import Resolution Quality

Import extraction quality is strong.

Internal Resolution

resolved_internal_rate = 74.7%

Unresolved Internal Imports

unresolved_internal_rate = 0.04%

This is extremely low.

Meaning:

relative import resolution largely succeeded

and the graph is not dominated by parser failure.


---

Top Central Modules

The graph correctly identifies obvious architectural hubs.

Top PageRank nodes:

django.db
django.utils.functional
django.conf
django.core.exceptions
django.urls
django.test
django.apps

Top in-degree nodes:

django.test
django.db
django.core.exceptions
django.conf
django.db.models

These are exactly the kinds of modules expected to dominate Django's architecture.

This strongly supports graph validity.


---

Consequence for Ω Theory

This result changes the interpretation of the previous Dependency Centrality Test.

Before this test:

weak Ω-centrality correlation
could have been caused by poor graph quality

After this test:

graph quality appears sufficient

Therefore:

the weak correlation becomes meaningful.


---

Updated Scientific Interpretation

The following hypothesis is now weakened:

Ω = static dependency centrality

Because:

the graph contains real hierarchy
but Ω still does not correlate strongly with it.

This is a major result.


---

What Ω Probably Is NOT

Current evidence suggests Ω is NOT primarily:

- line churn
- file count
- static dependency centrality
- simple module spread


---

What Ω May Still Be Sensitive To

Current surviving signals:

- path depth
- nesting pressure
- structural asymmetry
- deep architectural perturbation
- dynamic co-change structure

This shifts the investigation away from static topology and toward temporal topology.


---

New Leading Hypothesis

The next logical candidate is:

historical co-change topology

Core idea:

Ω may respond to
which files evolve together through time,
not merely to static import relationships.

Meaning:

dynamic structural coupling

rather than:

static dependency centrality.


---

Methodological Importance

This test is extremely important because it prevents a false technical excuse.

The previous weak dependency-centrality result can no longer be dismissed as:

"bad graph extraction"

The graph is structurally valid.

Therefore the negative correlation result becomes scientifically informative.


---

Final Classification

Import Graph Quality:
PASSED

Dependency Graph:
STRUCTURALLY USABLE

Centrality Hierarchy:
REAL

Import Resolution:
HIGH QUALITY

Previous Centrality Failure:
LIKELY GENUINE

Current Scientific Status:
Ω does not appear to be explained
by static dependency centrality.


---

Next Step

DYNAMIC CO-CHANGE TOPOLOGY TEST

Goal:

Measure whether Ω correlates with
historical file co-evolution patterns
instead of static dependency structure.

Core question:

Does Ω increase when structurally distant files
begin changing together through time?

This is now the strongest remaining structural hypothesis.