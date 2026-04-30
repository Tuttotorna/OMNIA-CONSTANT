# Controlled Destruction Experiments

## Purpose

These experiments exist to intentionally break the `Ω≈0.6` candidate boundary.

Failure is informative.

Survival under attack is required before considering `Ω≈0.6` a meaningful structural invariant.

---

## Core hypothesis

```text
Ω≈0.6 may represent a structural persistence boundary.

This repository does not assume that the hypothesis is true.

It tests whether the hypothesis survives controlled destruction.


---

Experiment family

noise_attack.py
representation_attack.py
normalization_attack.py
adversarial_pattern_attack.py
scale_attack.py
metric_substitution_attack.py
temporal_drift_attack.py
cross_domain_replication.py


---

Destruction logic

Each experiment should ask:

Can this attack make Ω≈0.6 disappear, shift, collapse, or become indistinguishable from noise?

If yes, the candidate weakens.

If no, the candidate strengthens.


---

Required output

Each experiment should report:

experiment_name
domain
attack_type
seed
sample_size
omega_values
omega_mean
omega_std
omega_distance_from_0_6
candidate_detected
candidate_rejected
rejection_reason
notes


---

Candidate detection rule

Initial provisional rule:

candidate_detected = abs(omega_mean - 0.6) <= tolerance

Default tolerance:

tolerance = 0.05

This means:

0.55 <= Ω <= 0.65

The tolerance is provisional and must be stress-tested.


---

Rejection rule

Reject the candidate in a given experiment if:

candidate_rejected = true

Typical rejection reasons:

indistinguishable_from_noise
representation_dependent
normalization_dependent
metric_dependent
scale_dependent
seed_dependent
domain_specific
adversarial_false_positive
not_reproducible


---

Evidence interpretation

Ω≈0.6 appears only in one setting
→ weak evidence

Ω≈0.6 survives multiple attacks
→ stronger candidate

Ω≈0.6 survives attacks and rejects false patterns
→ strong structural boundary candidate

Ω≈0.6 appears equally in noise and structured systems
→ reject as meaningful boundary


---

Important boundary

These experiments do not prove a universal constant.

They only test whether Ω≈0.6 behaves like a persistent structural boundary under attack.


---

Core principle

measurement != interpretation != decision

