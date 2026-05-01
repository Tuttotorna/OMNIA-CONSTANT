# IMPORT GRAPH QUALITY TEST

## Goal

Validate whether the extracted dependency graph
contains enough structural information
to support centrality analysis.

---

# Required Metrics

## Basic Structure

- node count
- edge count
- graph density
- directed vs undirected ratio

## Connectivity

- largest connected component size
- isolated node rate
- weakly connected component count
- strongly connected component count

## Degree Distribution

- in-degree distribution
- out-degree distribution
- max degree
- median degree
- power-law fit quality

## Centrality Stability

- PageRank variance
- PageRank entropy
- top-1 / median ratio
- centrality concentration index

## Import Resolution Quality

- resolved import rate
- unresolved import rate
- relative import resolution rate
- internal vs external import ratio

---

# Failure Conditions

Graph considered unreliable if:

- PageRank variance ~ 0
- isolated node rate too high
- giant component too small
- degree distribution nearly uniform
- unresolved import rate too high

---

# Success Conditions

Graph considered structurally informative if:

- clear hierarchy exists
- degree distribution is heavy-tailed
- giant component dominates graph
- PageRank distribution is non-uniform
- import resolution rate sufficiently high