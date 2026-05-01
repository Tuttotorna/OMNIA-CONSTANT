# CO-CHANGE TOPOLOGY TEST

## Goal

Determine whether Ω correlates with:

- historical co-evolution patterns
- structural memory
- cross-cluster evolutionary jumps

rather than with:

- churn
- static dependency centrality
- file count
- modular dispersion

---

# Core Hypothesis

Two files may:

- never import each other
- belong to distant modules
- appear unrelated statically

but still form a strong evolutionary coupling if they are repeatedly modified together over time.

This experiment tests whether Ω reacts to violations of these historical coupling structures.

---

# Main Idea

Instead of building a graph from:

```text
A imports B

build a graph from:

A changed together with B

across the full commit history.

The resulting graph represents:

historical structural co-evolution

rather than static architecture.


---

Experimental Pipeline

STEP 1 — Collect Commit Windows

For each commit:

changed_files = commit.files

Store all co-occurrences.


---

STEP 2 — Build Co-Change Matrix

For every pair:

(A, B)

inside the same commit:

cochange[A][B] += 1

Result:

weighted co-evolution graph


---

STEP 3 — Build Co-Change Graph

Nodes:

files

Edges:

historical co-change frequency

Edge weight:

number of co-occurrences

Optional normalization:

weight = shared_commits / total_commits


---

STEP 4 — Discover Evolutionary Clusters

Run community detection:

Louvain

spectral clustering

Girvan-Newman


Goal:

discover historical structural neighborhoods


---

STEP 5 — Compute Window Metrics

For each Ω window:

1. Intra-Cluster Ratio

Fraction of file changes occurring inside the same historical cluster.

High:

historically coherent evolution

Low:

cross-structural perturbation


---

2. Cross-Cluster Jump Rate

Fraction of co-changes between distant clusters.

Candidate strong Ω driver.


---

3. Evolutionary Distance

Mean graph distance between changed files in the co-change graph.

Measures:

historical incompatibility


---

4. Historical Surprise

Deviation between:

current co-change pattern

and:

historical expected pattern

Possible implementation:

surprise = -log(P(current_pattern))


---

5. Cluster Fragmentation

Measures whether the current window:

breaks stable historical communities

disperses normally coherent regions



---

Main Prediction

Ω should correlate more strongly with:

cross-cluster evolutionary stress

than with:

file count

churn

PageRank

static dependency centrality



---

Deep Interpretation

If confirmed:

Ω is not measuring architecture itself

but:

violation of historical structural memory

Meaning:

systems possess preferred evolutionary trajectories

and Ω increases when evolution deviates from historically compatible paths.


---

Strong Theoretical Consequence

This would imply:

Ω is fundamentally temporal

rather than spatial.

Not:

"how the system is built"

but:

"how the system historically evolves"


---

Expected Outcomes

Weak Result

Small correlation increase over static topology metrics.

Interpretation:

co-change contains partial Ω information


---

Strong Result

Moderate or strong correlation between Ω and:

cross-cluster jumps

historical surprise

evolutionary distance


Interpretation:

Ω behaves as a detector of structural memory rupture


---

Failure Condition

If correlations remain weak:

Ω is likely not reducible to any known software topology variable

which would strengthen its orthogonality.


---

Suggested Output Files

results/COCHANGE_TOPOLOGY_TEST.json
results/COCHANGE_TOPOLOGY_TEST.md
results/COCHANGE_TOPOLOGY_TEST_RESULT.md


---

Current Status

Previous tests eliminated reduction to:

churn

file count

static centrality

modular breadth


The remaining viable direction is:

dynamic historical topology

This is now the primary hypothesis frontier.