# CO-CHANGE TOPOLOGY TEST v0

## Goal

Test whether Ω correlates with historical co-change structure inside repository evolution.

The experiment investigates whether commits that violate historical co-change expectations produce elevated Ω.

---

# Repository

```text
django


---

Dataset Summary

{
  "commits_loaded": 2000,
  "events": 1999,
  "usable_commits_for_cochange": 1182,
  "unique_files": 1613,
  "unique_cochange_pairs": 26000,
  "total_pair_observations": 31455,
  "windows": 198
}


---

Tested Variables

The following co-change metrics were measured:

mean_files_per_commit

unique_files_in_window

pair_count

mean_cochange_strength

max_cochange_strength

weak_pair_rate

novel_pair_rate

historical_surprise

cochange_density



---

Correlation Results

Metric	Correlation with Ω

mean_files_per_commit	-0.003032
unique_files_in_window	0.009489
pair_count	-0.042072
mean_cochange_strength	0.023967
max_cochange_strength	0.000000
weak_pair_rate	0.046887
novel_pair_rate	0.052476
historical_surprise	0.072726
cochange_density	-0.052476



---

Main Observation

All observed correlations were weak.

No meaningful relationship emerged between Ω and historical co-change topology.


---

Historical Surprise Result

The key target variable:

historical_surprise

produced only:

0.072726

This weakens the hypothesis that Ω measures violation of historical repository memory.


---

Interpretation

The experiment does not support the idea that Ω primarily reacts to:

historical coupling

co-evolutionary structure

repository memory

cross-cluster jumps


Observed evidence instead suggests that Ω is largely orthogonal to aggregated co-change topology.


---

Important Methodological Observation

Window-level aggregation generated extremely large synthetic pair spaces.

Example:

472 unique files
→ more than 111000 synthetic file pairs

This likely diluted local co-change signals.

The experiment therefore may suffer from:

window-level pair inflation


---

Consequence

The weak result does not fully falsify local co-change effects.

It mainly falsifies:

aggregated historical co-change topology

as a dominant explanation of Ω.


---

Updated Hypothesis

The result shifts attention away from:

repository-scale topology

historical memory

co-change evolution


and toward:

local structural deformation

patch geometry

AST restructuring

execution morphology



---

Important Limitation

This experiment used aggregated windows rather than isolated commit-level perturbation analysis.

A more localized test was required afterward.


---

Follow-Up

This experiment directly motivated:

COMMIT_LEVEL_COCHANGE_SURPRISE_TEST

which attempted to eliminate window-level dilution effects.


---

Status

Weak signal
Historical reduction unsupported
Further localized testing required