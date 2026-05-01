# COMMIT_LEVEL_COCHANGE_SURPRISE_TEST_RESULT

## Purpose

Test whether Ω correlates with real commit-level historical co-change surprise.

Core question:

```text
Does Ω increase when a commit touches file pairs
that historically do not change together?

This test refines the previous window-level co-change experiment by avoiding artificial pair inflation.


---

Why This Test Was Needed

The previous co-change topology test aggregated all unique files inside a sliding window.

That created synthetic file pairs that never actually changed together.

Example:

Commit 1: A, B
Commit 2: C, D

Window-level aggregation incorrectly creates:
A-C
A-D
B-C
B-D

This caused pair explosion and flattened historical surprise.

The commit-level test fixes this by using only real file pairs inside each commit.


---

Repository

django


---

Dataset

{
  "commits_loaded": 2500,
  "events": 2499,
  "usable_events": 1472,
  "usable_commit_count_for_history": 1472,
  "unique_files": 1781,
  "unique_cochange_pairs": 30228,
  "pair_observation_count": 36786,
  "window_size": 25,
  "window_step": 10,
  "windows": 248
}


---

Metrics Tested

Commit-Level Metrics

file_count
commit_pair_count
commit_mean_cochange_strength
commit_max_cochange_strength
commit_weak_pair_rate
commit_novel_pair_rate
commit_historical_surprise
commit_cochange_density

Window-Level Aggregates

usable_commit_rate
mean_files_per_commit
mean_commit_pair_count
mean_commit_cochange_strength
mean_commit_max_cochange_strength
mean_commit_weak_pair_rate
mean_commit_novel_pair_rate
mean_commit_historical_surprise
mean_commit_cochange_density


---

Commit-Level Correlations

{
  "file_count": 0.027811,
  "commit_pair_count": -0.000778,
  "commit_mean_cochange_strength": 0.042094,
  "commit_max_cochange_strength": 0.104802,
  "commit_weak_pair_rate": 0.053335,
  "commit_novel_pair_rate": 0.0,
  "commit_historical_surprise": 0.093527,
  "commit_cochange_density": 0.0
}

All commit-level correlations are weak.


---

Window-Level Correlations

{
  "usable_commit_rate": 0.240691,
  "mean_files_per_commit": -0.0211,
  "mean_commit_pair_count": -0.075748,
  "mean_commit_cochange_strength": 0.042603,
  "mean_commit_max_cochange_strength": 0.102984,
  "mean_commit_weak_pair_rate": 0.210591,
  "mean_commit_novel_pair_rate": 0.0,
  "mean_commit_historical_surprise": 0.147761,
  "mean_commit_cochange_density": 0.0
}

Most window-level correlations are weak.

Two values are weak-to-moderate:

usable_commit_rate = 0.240691
mean_commit_weak_pair_rate = 0.210591

But neither is strong enough to support the historical-surprise hypothesis.


---

Main Result

The commit-level co-change surprise hypothesis is not supported.

Observed:

commit_historical_surprise = 0.093527
window_historical_surprise = 0.147761

This means:

Ω does not meaningfully increase
when commits contain historically surprising file pairs.


---

Strong Negative Evidence

Many high-Ω commits show:

cochange_density = 1.0
novel_pair_rate = 0.0

This is important.

It means:

high Ω commits often touch file pairs
that are already historically known.

Therefore high Ω is not explained by:

novel file pairings

or:

historical co-change surprise


---

Examples from High-Ω Commits

Example 1

{
  "commit": "a523d5c8336f",
  "omega": 0.797077,
  "files": [
    "scripts/backport.sh",
    "scripts/confirm_release.sh",
    "scripts/do_django_release.py",
    "scripts/test_new_version.sh"
  ],
  "file_count": 4,
  "commit_mean_cochange_strength": 1.0,
  "commit_novel_pair_rate": 0.0,
  "commit_historical_surprise": 6.399176,
  "commit_cochange_density": 1.0
}

Interpretation:

high Ω, but historically coherent file set.


---

Example 2

{
  "commit": "4289966d1b8e",
  "omega": 0.756565,
  "file_count": 29,
  "commit_mean_cochange_strength": 0.77531,
  "commit_novel_pair_rate": 0.0,
  "commit_cochange_density": 1.0
}

Interpretation:

large structural change,
but not novel from co-change perspective.


---

Example 3

{
  "commit": "d61f33f03b31",
  "omega": 0.763828,
  "files": [
    "tests/mail/test_backends.py",
    "tests/mail/tests.py"
  ],
  "file_count": 2,
  "commit_mean_cochange_strength": 1.0,
  "commit_novel_pair_rate": 0.0,
  "commit_cochange_density": 1.0
}

Interpretation:

very high Ω even with only two historically coherent files.

This is especially damaging to the hypothesis that Ω requires historical surprise.


---

What This Test Rejects

This test weakens or rejects:

Ω = historical co-change surprise
Ω = novelty of file pairings
Ω = weak historical coupling
Ω = co-change density anomaly

At least for this Django dataset and this implementation.


---

What This Test Does NOT Reject

This does not reject all temporal interpretations of Ω.

It only rejects this specific reduction:

Ω explained by commit-level historical co-change surprise.

Other temporal variables may still matter, such as:

- temporal burstiness
- patch-local entropy
- diff grammar instability
- edit operation diversity
- structural depth of edits


---

Updated Reduction Status

Candidate Explanation	Status

Churn / file count	Not supported
Lines added/deleted	Not supported
Module dispersion	Not supported
Static dependency centrality	Not supported
Co-change topology v0	Not supported
Commit-level co-change surprise	Not supported
Path depth / nesting	Partially supported



---

Current Best Interpretation

Ω does not appear to be explained by:

where files are located in a co-change history

nor by:

whether those files have changed together before.

The surviving hypothesis is that Ω reacts more directly to:

the internal structure of the patch itself

rather than external repository topology.


---

Emerging Direction

The next serious direction is:

PATCH STRUCTURE / PATCH ENTROPY TEST

Potential variables:

- diff entropy
- edit dispersion inside files
- added/deleted balance
- hunk count
- hunk distance
- token-level disruption
- syntactic edit diversity
- path depth
- nesting depth

This is a shift from:

file-level topology

to:

patch-level geometry


---

Scientific Conclusion

The Commit-Level Co-Change Surprise Test produced a negative result.

It shows that Ω is not meaningfully correlated with historical co-change surprise.

This is important because it eliminates another plausible reduction.

The strongest conclusion:

Ω is not explained by historical memory of file pairings.

The framework therefore becomes more constrained:

Ω is not churn.
Ω is not static centrality.
Ω is not module dispersion.
Ω is not co-change novelty.

The remaining plausible direction is:

Ω as a patch-internal structural metric.


---

Final Status

COMMIT_LEVEL_COCHANGE_SURPRISE_TEST:
NEGATIVE RESULT

But methodologically valuable.

It eliminates another reductionist explanation and points toward the internal geometry of the diff as the next target.