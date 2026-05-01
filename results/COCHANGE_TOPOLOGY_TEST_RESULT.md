COCHANGE_TOPOLOGY_TEST_RESULT

Objective

Test whether Ω correlates with:

historical co-change structure

novelty of file pairings

structural surprise

co-change topology instability


Hypothesis:

High Ω windows should contain:
- more historically unusual file pairings
- lower co-change density
- higher evolutionary surprise
- more cross-cluster structural jumps


---

Experimental Setup

Repository:

django

Dataset:

2000 commits
1999 Ω events

Co-change extraction:

usable commits for co-change = 1182
unique files = 1613
unique co-change pairs = 26000
total pair observations = 31455

Window configuration:

window_size = 25
window_step = 10
total_windows = 198


---

Metrics Tested

For each window:

mean_files_per_commit
unique_files_in_window
pair_count
mean_cochange_strength
max_cochange_strength
weak_pair_rate
novel_pair_rate
historical_surprise
cochange_density

Definitions:

mean_cochange_strength
= average historical frequency of observed file pairs

weak_pair_rate
= fraction of low-frequency co-change pairs

novel_pair_rate
= fraction of previously unseen or near-unseen pairs

historical_surprise
= average -log(P(pair))

cochange_density
= density of historically established co-change relations


---

Global Correlations

mean_files_per_commit     = -0.003032
unique_files_in_window    =  0.009489
pair_count                = -0.042072
mean_cochange_strength    =  0.023967
max_cochange_strength     =  0.000000
weak_pair_rate            =  0.046887
novel_pair_rate           =  0.052476
historical_surprise       =  0.072726
cochange_density          = -0.052476


---

Correlation Strengths

ALL METRICS:
weak

No moderate or strong correlation detected.


---

Interpretation

Main Result

Ω does NOT correlate strongly with co-change topology v0.

Specifically:

Ω is not explained by:
- pair novelty
- historical surprise
- co-change density
- co-change strength


---

Important Methodological Observation

The v0 implementation aggregates all files across an entire window.

This creates artificial pair combinations between files that:

- never changed together
- never appeared in the same commit
- only coexist inside the sliding window

Example:

window 115:
unique_files = 472
pair_count = 111156

This causes:

historical_surprise ≈ constant

Observed range:

~6.8 to ~7.0

Meaning:

signal compression occurred

The aggregation method diluted commit-level structural information.


---

High Ω Windows

Example:

window_index = 181
mean_omega = 0.571988
historical_surprise = 6.979708
weak_pair_rate = 0.905473
novel_pair_rate = 0.904568

But similar surprise values also appeared in medium Ω windows.

No discriminative separation emerged.


---

Scientific Conclusion

This experiment does NOT support:

Ω = historical co-change surprise

at least under:

window-level aggregated co-change topology v0


---

Critical Distinction

This result does NOT prove:

memory topology is irrelevant

It only proves:

the current aggregation model failed to isolate the signal


---

Most Likely Failure Source

The signal was destroyed by:

window-level pair explosion

instead of measuring:

real commit-level co-change structure


---

Recommended Next Step

COMMIT_LEVEL_COCHANGE_SURPRISE_TEST

Instead of:

all files inside a window

Use:

only file pairs that actually changed together
inside each commit

Then compute:

commit surprise
→ aggregate afterward

This preserves:

true evolutionary coupling

and avoids synthetic pair inflation.


---

Current OMNIA Reduction Status

Candidate Reduction	Result

Churn	Failed
File Count	Failed
Module Dispersion	Failed
Static Centrality	Failed
Co-Change Topology v0	Failed
Path Depth	Partial Signal



---

Current Evidence

The only consistently surviving signal remains:

structural depth

suggesting Ω reacts more strongly to:

depth of perturbation

than to:

historical co-evolution frequency


---

Final Status

COCHANGE_TOPOLOGY_TEST v0:
NEGATIVE RESULT

But:

methodologically informative

and sufficient to justify a refined commit-level model.