# COMMIT-LEVEL CO-CHANGE SURPRISE TEST

## Goal

Test whether Ω reacts to local co-change surprise at the individual commit level.

This experiment attempts to eliminate the signal dilution observed in the previous window-level co-change topology test.

---

# Repository

```text
django


---

Dataset Summary

{
  "commits_loaded": 2500,
  "events": 2499,
  "usable_events": 1472,
  "unique_files": 1781,
  "unique_cochange_pairs": 30228,
  "pair_observation_count": 36786,
  "windows": 248
}


---

Tested Variables

The following commit-level co-change metrics were measured:

file_count

commit_pair_count

commit_mean_cochange_strength

commit_max_cochange_strength

commit_weak_pair_rate

commit_novel_pair_rate

commit_historical_surprise

commit_cochange_density



---

Commit-Level Correlation Results

Metric	Correlation with Ω

file_count	0.027811
commit_pair_count	-0.000778
commit_mean_cochange_strength	0.042094
commit_max_cochange_strength	0.104802
commit_weak_pair_rate	0.053335
commit_novel_pair_rate	0.000000
commit_historical_surprise	0.093527
commit_cochange_density	0.000000



---

Window-Level Aggregated Results

Metric	Correlation with Ω

usable_commit_rate	0.240691
mean_files_per_commit	-0.021100
mean_commit_pair_count	-0.075748
mean_commit_cochange_strength	0.042603
mean_commit_max_cochange_strength	0.102984
mean_commit_weak_pair_rate	0.210591
mean_commit_novel_pair_rate	0.000000
mean_commit_historical_surprise	0.147761
mean_commit_cochange_density	0.000000



---

Main Observation

Even after removing window-level inflation effects, correlations remained weak.

This weakens the hypothesis that Ω primarily reacts to:

co-change novelty

historical surprise

repository memory

local evolutionary expectation violation



---

Critical Result

The key target metric:

commit_historical_surprise

produced only:

0.093527

at commit level.

This is far below the strength observed later for AST deformation and control-flow restructuring.


---

Important Counterexample

Several very high-Ω commits occurred inside historically coherent co-change groups.

Example:

commit: d61f33f03b31
Ω ≈ 0.76

despite:

fully coherent co-change structure

no novel pair introduction

maximum co-change density


This directly weakens the interpretation of Ω as a historical surprise detector.


---

Interpretation

Observed evidence suggests that Ω is largely independent from:

repository history

co-change memory

commit novelty

evolutionary topology


The result shifts explanatory focus toward:

local patch geometry

AST restructuring

control-flow deformation

representational morphology



---

Consequence

The experiment strongly weakens:

Ω = historical instability

and strengthens:

Ω = local structural perturbation


---

Important Limitation

Historical co-change was measured through observable file co-occurrence only.

Hidden semantic coupling or runtime dependency effects were not measured.


---

Follow-Up

This experiment directly motivated:

PATCH_GEOMETRY_TEST

and later:

PATCH_GEOMETRY_AST_TEST

which shifted analysis from repository history to internal structural deformation.


---

Status

Localized co-change reduction unsupported
Historical explanation weakened
Structural deformation hypothesis strengthened