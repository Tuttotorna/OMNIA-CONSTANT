# PATCH GEOMETRY TEST v0

## Goal

Test whether Ω correlates with local patch geometry properties rather than repository-level topology or historical co-change structure.

The experiment focuses on transformation intensity inside patches.

---

# Repository

```text
django


---

Dataset Summary

{
  "commits_loaded": 2500,
  "events": 2499,
  "windows": 248,
  "window_size": 25,
  "window_step": 10
}


---

Tested Variables

The following patch-level metrics were measured:

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

Metric	Correlation with Ω

file_count	0.478728
hunk_count	0.435468
added_lines	0.341131
deleted_lines	0.468651
total_changes	0.410162
add_delete_ratio	-0.341421
edit_dispersion	-0.000917
hunk_distance_mean	0.057672
hunk_distance_std	0.141600
mean_path_depth	0.113160



---

Main Observations

Strongest signals

The strongest positive correlations were:

file_count

deleted_lines

hunk_count

total_changes


This suggests that Ω reacts more strongly to transformation intensity than to repository topology or historical co-change.


---

Negative signal

The add_delete_ratio produced a negative correlation:

-0.341421

This suggests that deletion-heavy transformations may generate stronger structural perturbation than additive transformations.

Interpretation remains provisional.


---

Weak or near-zero signals

The following metrics produced weak or negligible correlations:

edit_dispersion

hunk_distance_mean

hunk_distance_std


This suggests that spatial distance between hunks is not a dominant explanatory factor.


---

Interpretation

The experiment weakens repository-level explanations of Ω and shifts attention toward local transformation geometry.

Observed evidence suggests that Ω may react to:

structural deformation intensity

representational compression or expansion

local modification density


rather than:

graph position

historical coupling

static centrality



---

Important Limitation

This experiment is partially coupled to the construction of Ω proxies.

Correlation therefore does not establish independence.

Further independent validation is required.


---

Status

Exploratory
Non-final
Falsification-oriented