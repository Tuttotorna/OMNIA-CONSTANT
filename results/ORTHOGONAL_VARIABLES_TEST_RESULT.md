# ORTHOGONAL VARIABLES TEST RESULT

## Purpose

Determine whether Ω is reducible to simple software churn metrics.

Core question:

```text
Does Ω contain independent structural information,
or is it simply a proxy for:
- commit size
- line count
- file count
- contributor activity
?

This is one of the most important falsification tests in the entire framework.


---

Scientific Risk Being Tested

The primary failure mode:

Ω = disguised churn metric

Equivalent interpretation:

Ω only measures:
- large commits
- many changed files
- many inserted lines
- chaotic development

If true:

the framework collapses immediately.


---

Experimental Design

For each sliding commit window:

measure:
- Ω
- files changed
- lines added
- lines deleted
- author entropy

Then compute:

corr(Ω, variable)

Goal:

determine whether Ω is strongly reducible
to standard software activity metrics.


---

Dataset

Repositories analyzed:

django
react
numpy
atom
brackets
phonegap

Mix includes:

- healthy systems
- abandoned systems
- overloaded systems
- cooling systems
- high-churn ecosystems


---

Experimental Parameters

Sliding Window

window_size = 25 commits
window_step = 10 commits

Total Windows

634


---

Variables Tested

Files Changed

mean files modified per window

Lines Added

mean inserted lines per window

Lines Deleted

mean removed lines per window

Author Entropy

contributor diversity proxy


---

Global Summary

{
  "repos": [
    "django",
    "react",
    "numpy",
    "atom",
    "brackets",
    "phonegap"
  ],
  "window_size": 25,
  "window_step": 10,
  "total_windows": 634,
  "correlations": {
    "files_changed": 0.126318,
    "lines_added": 0.145773,
    "lines_deleted": 0.114889,
    "author_entropy": -0.158781
  },
  "interpretation": {
    "files_changed": {
      "correlation": 0.126318,
      "strength": "weak"
    },
    "lines_added": {
      "correlation": 0.145773,
      "strength": "weak"
    },
    "lines_deleted": {
      "correlation": 0.114889,
      "strength": "weak"
    },
    "author_entropy": {
      "correlation": -0.158781,
      "strength": "weak"
    }
  }
}


---

Primary Result

All measured correlations are weak.

Observed range:

0.11 → 0.15

This is far below what would be expected if Ω were merely:

- commit magnitude
- churn volume
- raw development activity


---

Critical Interpretation

The experiment does NOT support:

Ω = simple churn proxy

This is one of the strongest results obtained so far.


---

Why This Matters

If Ω were merely measuring:

- large diffs
- many changed files
- many inserted lines

then expected correlations would likely resemble:

0.7+

Instead:

all correlations remain weak.

This strongly suggests:

Ω captures something structurally distinct
from raw commit volume.


---

Important Scientific Boundary

This experiment does NOT prove:

Ω measures resilience

nor:

Ω measures collapse

However, it DOES support:

Ω is not trivially redundant.

This is a crucial distinction.


---

Structural Interpretation

Current evidence suggests Ω reacts more strongly to:

organization of change

than to:

quantity of change

Possible interpretations include sensitivity to:

- structural dispersion
- fragmentation
- incompatibility
- topology disturbance
- coherence disruption
- geometric distribution of modifications

rather than simple magnitude.


---

Author Entropy Result

Observed:

corr(Ω, author_entropy) = -0.158781

Interpretation:

Ω is not strongly explained
by contributor diversity either.

This weakens the hypothesis that Ω simply measures:

"many people touching many files"


---

Most Important Scientific Consequence

This experiment prevents immediate collapse of the framework.

Because the strongest reductionist criticism was:

"You reinvented changed line count."

The data currently do NOT support that criticism.


---

Conceptual Transition

This experiment changes the nature of the investigation.

Before:

search for universal constant

Now:

search for latent structural coordinate

This is a major conceptual shift.


---

What The Experiment Supports

Supported:

- Ω is weakly correlated with churn
- Ω is not reducible to simple commit size
- Ω appears structurally non-trivial
- Ω likely captures organization patterns


---

What The Experiment Does NOT Support

Not supported:

- universal meaning of Ω
- causal interpretation
- resilience measurement proof
- collapse prediction proof


---

Current Best Interpretation

The strongest currently supported interpretation is:

Ω behaves like a latent structural variable
sensitive to organization and distribution of change,
not merely its magnitude.


---

Most Important Open Question

The next critical question becomes:

What structural property
is Ω actually responding to?

Current candidates include:

- topological dispersion
- module fragmentation
- structural incompatibility
- distributed perturbation
- coherence instability

This becomes the next major direction of investigation.


---

Final Conclusion

The Orthogonal Variables Test is one of the strongest falsification-survival results obtained so far.

The experiment demonstrates that:

Ω is NOT strongly explained
by:
- changed files
- inserted lines
- deleted lines
- contributor entropy

All measured correlations remain weak.

This does NOT validate the full theory.

However, it strongly supports:

Ω contains non-trivial structural information
not reducible to standard churn metrics.

At this stage, Ω appears less like:

a simple activity counter

and more like:

a latent dynamical structural coordinate.