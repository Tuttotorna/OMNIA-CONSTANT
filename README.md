# OMNIA-CONSTANT

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20369144.svg)](https://doi.org/10.5281/zenodo.20369144)

<!-- OMNIA_CONSTANT_AUDITOR_TOP_START -->


## Foundational Principle

OMNIA-CONSTANT is a persistence-focused application of the L.O.N. Multi-Form Invariance Principle:

> No single form is sovereign.

In OMNIA-CONSTANT, this becomes:

> No constant is sovereign unless its persistence survives transformation.

A constant is not trusted because it appears stable in one form, one representation, one scale, or one observation. Its persistence must remain structurally compatible across independent transformations.

OMNIA-CONSTANT exists to distinguish apparent constancy from structural persistence.

See:

- https://github.com/Tuttotorna/lon-mirror/tree/main/foundation

## Concrete entrypoint: OMNIA Constant Auditor

This repository now has a direct operational tool:

    python -m omnia_constant_auditor.cli --input examples/sample_constant_observations.jsonl --out-dir report

It solves a concrete problem:

    given observations across runs, domains, contexts, or perturbations,
    measure what remains constant,
    what drifts,
    and what ruptures.

In short:

    observations across runs/domains -> constant / drift / rupture report

## What problem does it solve?

A measurement can look stable in one run and fail across repeated observations.

OMNIA-CONSTANT turns this into a reproducible audit:

    group observations by constant_id
    compare values across contexts
    measure numeric or structural variation
    classify each candidate as constant, drift, or rupture
    emit a reproducible certificate
    optionally fail CI when rupture appears

## Install

Clone the repository:

    git clone https://github.com/Tuttotorna/OMNIA-CONSTANT.git
    cd OMNIA-CONSTANT

Install locally:

    pip install -e .

The auditor only uses the Python standard library.

## Run

Run the sample audit:

    python -m omnia_constant_auditor.cli --input examples/sample_constant_observations.jsonl --out-dir report

Run and fail if rupture is detected:

    python -m omnia_constant_auditor.cli --input examples/sample_constant_observations.jsonl --out-dir report --fail-on-rupture

Run and fail if drift or rupture is detected:

    python -m omnia_constant_auditor.cli --input examples/sample_constant_observations.jsonl --out-dir report --fail-on-drift

## Input format

The auditor accepts JSONL.

Required fields:

    constant_id
    context_id
    value

Optional fields:

    domain
    run_id
    expected
    note

Example:

    {"constant_id":"omega_floor","context_id":"run_001","value":0.99}
    {"constant_id":"omega_floor","context_id":"run_002","value":0.98}
    {"constant_id":"omega_floor","context_id":"run_003","value":0.10}

Classification rule:

    constant = values remain stable within tolerance
    drift    = values vary but remain partially compatible
    rupture  = values break beyond the configured rupture threshold

## Output

The auditor writes:

    report.json
    report.csv
    report.html
    drift_constants.jsonl
    rupture_constants.jsonl
    certificate.json

Meaning:

    report.json
    Full structured constant analysis.

    report.csv
    Spreadsheet-friendly constant summary.

    report.html
    Human-readable audit report.

    drift_constants.jsonl
    One JSON object per drifting constant candidate.

    rupture_constants.jsonl
    One JSON object per ruptured constant candidate.

    certificate.json
    Reproducibility certificate with thresholds, counts, and boundary statement.

## CI gate

Fail when rupture appears:

    python -m omnia_constant_auditor.cli --input examples/sample_constant_observations.jsonl --out-dir report --fail-on-rupture

Fail when drift or rupture appears:

    python -m omnia_constant_auditor.cli --input examples/sample_constant_observations.jsonl --out-dir report --fail-on-drift

Exit codes:

    0 = analysis completed without selected blocking condition
    2 = drift detected under --fail-on-drift
    3 = rupture detected under --fail-on-rupture or --fail-on-drift
    4 = invalid input or measurement error

## What this is not

This is not a metaphysical claim about absolute constants.

It does not decide truth.

It does not infer meaning.

It measures candidate constants inside the supplied observation boundary.

The boundary is explicit:

    measurement only;
    constant means stability across supplied contexts,
    not universal semantic truth.

## Why the rest of the repository still matters

The rest of this repository documents the constant concept:

    structural constancy
    persistence across observation contexts
    stability under perturbation
    drift
    rupture
    measurement boundary

The code above is the operational entrypoint.

The repository below is the derivation path.

<!-- OMNIA_CONSTANT_AUDITOR_TOP_END -->

---

<!-- MB-X.01 LON RELEASE:START -->

## MB-X.01 / L.O.N. release state

Repository: Tuttotorna/OMNIA-CONSTANT
Release tag: v2026.05.21
Release commit: 82b86e3
Release DOI: 10.5281/zenodo.20322695

Boundary:

measurement != validation
validation != orchestration
orchestration != decision
decision != measurement

<!-- MB-X.01 LON RELEASE:END -->

<!-- ZENODO DOI:START -->

## DOI

Zenodo DOI badge for this repository.

Repository: Tuttotorna/OMNIA-CONSTANT
GitHub repository id: 1225428060
Release tag: v2026.05.21
Latest release DOI: 10.5281/zenodo.20322695

<!-- ZENODO DOI:END -->

## DOI

Release DOI: [10.5281/zenodo.19970512](https://doi.org/10.5281/zenodo.19970512)

GitHub release: [OMNIA-CONSTANT v1.0.0 release](https://github.com/Tuttotorna/OMNIA-CONSTANT/releases/tag/v1.0.0)

## Current position

This repository does **not** claim that Ω is a universal constant.

Current evidence supports a narrower and more careful interpretation:

```text
Ω appears to behave as a structural / morphological perturbation signal.

In the tested software experiments, Ω is more strongly associated
with observable deformation in code form than with semantic correctness.

Current working hypothesis:
Ω measures representational and morphological deformation, not semantic truth.
```

This is a falsification-first position, not a proclamation.

---

## What this repository tests

OMNIA-CONSTANT tests whether observed Ω regions can be reduced to simpler explanations such as:

- churn
- file count
- line count
- dependency centrality
- import graph topology
- historical co-change
- commit novelty
- control-flow mutation alone
- semantic correctness
- measurement artifact

The strongest surviving direction is local structural deformation of the transformation itself, especially:

- patch geometry
- AST deformation
- control-flow restructuring
- representational compression / expansion
- morphological perturbation

---

## What OMNIA-CONSTANT is not

OMNIA-CONSTANT does not claim that Ω detects:

- bugs
- correctness
- semantic equivalence
- logical truth
- program intent
- runtime behavior
- universal physical law
- final truth

The semantic invariance test produced a critical negative result:

```text
semantic-preserving transformations sometimes produced larger ΔΩ
than semantic-changing transformations
```

Therefore Ω must not currently be interpreted as a semantic correctness signal.

---

## Current working hypothesis

The current best interpretation is:

```text
Ω behaves as a morphology-sensitive structural perturbation measure.
```

More specifically, Ω appears to measure observable transformation stress in the representation of a system.

In software, this means Ω may react to:

- AST reshaping
- control-flow restructuring
- representational compression
- representational expansion
- local structural deformation
- transformation intensity

It does not currently demonstrate semantic understanding.

---

## Main experimental findings

### 1. Churn and file count are insufficient

Ω was not strongly explained by files changed, lines added, lines deleted, or basic churn metrics.

### 2. Static dependency centrality is insufficient

Import graph centrality and PageRank did not explain Ω.

### 3. Historical co-change is insufficient

Co-change surprise tests produced weak results.

### 4. Patch geometry is partially informative

Patch-level measurements showed partial associations, but not a full explanation.

### 5. AST deformation is the strongest current signal

AST-based experiments produced the strongest observed signals.

### 6. Control-flow contributes but does not explain Ω

Control-flow deformation contributes to Ω, but Ω is not reducible to control-flow alone.

### 7. Semantic invariance test failed

The tested proxy reacted more strongly to representational changes than to some semantic changes.

---

## Repository structure

```text
README.md       public entrypoint
docs/           protocols and scope notes
papers/         paper-style result summaries
results/        result reports and falsification records
experiments/    experiment scripts imported from invariance workflows
LICENSE         MIT license
```

---

## Public entrypoints

- [`docs/CONSTANT_SCOPE.md`](docs/CONSTANT_SCOPE.md)
- [`docs/RESULTS_INDEX.md`](docs/RESULTS_INDEX.md)
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)
- [`papers/README.md`](papers/README.md)
- [`papers/OMNIA_MORPHOLOGICAL_PERTURBATION_ABSTRACT.md`](papers/OMNIA_MORPHOLOGICAL_PERTURBATION_ABSTRACT.md)

---

## Relationship to the OMNIA ecosystem

```text
OMNIA             = structural measurement core
OMNIA-INVARIANCE  = invariance / trajectory-space analysis
OMNIA-CONSTANT    = Ω-region post-analysis / falsification layer
OMNIA-VALIDATION  = evidence / reproducibility layer
Decision           = external layer
```

The separation remains strict:

```text
measurement != inference != decision
```

---

## Methodological principle

This repository follows a falsification-first approach.

The goal is not to force Ω into a preferred interpretation.

The goal is to eliminate weak explanations.

Negative results are preserved because they define what Ω is not.

---

## Testing note

This repository contains legacy experiment scripts under `experiments/`.

Some are research scripts, not package tests.

The repository test configuration intentionally restricts pytest collection to:

```text
tests/
```

This prevents unfinished legacy experiment scripts from being interpreted as test modules.

---

## Public position

OMNIA-CONSTANT public positioning is documented here:

- [`docs/OMNIA_CONSTANT_PUBLIC_POSITION.md`](docs/OMNIA_CONSTANT_PUBLIC_POSITION.md)

Core thesis:

```text
A constant is not assumed.
A constant is measured as persistence.
```

Core boundary:

```text
constant != absolute truth
measurement != inference != decision
```

Core role:

```text
OMNIA-CONSTANT studies what remains unchanged across defined transformation regimes.
```

OMNIA-CONSTANT does not claim metaphysical constants.

It does not claim absolute truth.

It does not decide semantic correctness.

It treats constancy as a measurable structural persistence property.
---

## Citation

If you reference this repository, use the archived Zenodo record:

```text
DOI: 10.5281/zenodo.19970512
https://doi.org/10.5281/zenodo.19970512
```

Citation metadata is available in:

- [`CITATION.cff`](CITATION.cff)

---

## Summary

OMNIA-CONSTANT is not a declaration of a universal constant.

It is a falsification layer for Ω-region behavior.

Its current position is narrow:

```text
Ω appears to behave as a morphology-sensitive structural perturbation signal.
Ω is not currently validated as semantic truth.
No universal structural constant is declared.
measurement != inference != decision
```

## Boundary terms

    Structural truth = invariance under transformation
    One invariant is not a constant

---

## Related repositories

| Repository | Role |
|---|---|
| [lon-mirror](https://github.com/Tuttotorna/lon-mirror) | Canonical public entry point |
| [OMNIA-VALIDATION](https://github.com/Tuttotorna/OMNIA-VALIDATION) | Public validation showroom |
| [OMNIA](https://github.com/Tuttotorna/OMNIA) | Core structural measurement engine |
| [OMNIABASE](https://github.com/Tuttotorna/OMNIABASE) | Representation invariance foundation |
| [omnia-limit](https://github.com/Tuttotorna/omnia-limit) | Stop / continue boundary layer |
| [OMNIA-RADAR](https://github.com/Tuttotorna/OMNIA-RADAR) | Structural signal detection layer |
| [OMNIA-INVARIANCE](https://github.com/Tuttotorna/OMNIA-INVARIANCE) | Structural invariance layer |
| [OMNIA-CONSTANT](https://github.com/Tuttotorna/OMNIA-CONSTANT) | Structural constant candidate layer |
| [OMNIAMIND](https://github.com/Tuttotorna/OMNIAMIND) | Structural cognition orchestration layer |
| [OMNIA-THREE-BODY](https://github.com/Tuttotorna/OMNIA-THREE-BODY) | Dynamic divergence stress test |
| [OMNIA-SECURITY](https://github.com/Tuttotorna/OMNIA-SECURITY) | Bounded structural security diagnostics |
| [OMNIA-CRYPTO](https://github.com/Tuttotorna/OMNIA-CRYPTO) | Bounded structural crypto diagnostics |

---

## Boundary and smoke-test required terms

    not a truth oracle
    not a semantic judge
    Decision remains external

<!-- OMNIA_ECOSYSTEM_BOUNDARY_V1 -->

## Ecosystem Boundary

```text
measurement != inference != decision
```

This repository is part of the MB-X.01 / OMNIA ecosystem. Its outputs must be read as structural measurement, validation, detection, orchestration or adapter artifacts according to the repository role. They are not autonomous semantic truth claims and they do not make external decisions.

<!-- STRUCTURAL_OBSERVABILITY_ROLE_START -->
## Structural Observability role

This repository is one bounded measurement role inside **Structural Observability**.

Role:

~~~text
candidate-constant and stable-region auditor
~~~

Boundary:

~~~text
Constant means stable under supplied observations. It is not a universal constant claim.
~~~

Structural Observability foundation:

- lon-mirror: https://github.com/Tuttotorna/lon-mirror
- Foundation release: https://github.com/Tuttotorna/lon-mirror/releases/tag/v0.2.2
- DOI: https://doi.org/10.5281/zenodo.20379374

Role document:

- [Structural Observability Role](docs/STRUCTURAL_OBSERVABILITY_ROLE.md)
<!-- STRUCTURAL_OBSERVABILITY_ROLE_END -->

<!-- OMNIA_ZENODO_CITATION_BLOCK_START -->

## Citation and archival

This repository is prepared for GitHub-Zenodo archival.

Repository:
https://github.com/Tuttotorna/OMNIA-CONSTANT

Latest GitHub release: v0.1.1 (https://github.com/Tuttotorna/OMNIA-CONSTANT/releases/tag/v0.1.1)

Detected Zenodo DOI(s):
- https://doi.org/10.5281/zenodo.20369144
- https://doi.org/10.5281/zenodo.20322695
- https://doi.org/10.5281/zenodo.19970512
- https://doi.org/10.5281/zenodo.20379374

Metadata files used for archival/citation:

- .zenodo.json
- CITATION.cff

Zenodo note:

GitHub-Zenodo archiving works after the repository is enabled in Zenodo GitHub settings and a GitHub release is created.

<!-- OMNIA_ZENODO_CITATION_BLOCK_END -->
