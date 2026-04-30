# First Discovery Scan

## Source

Repository scanned:

```text
https://github.com/Tuttotorna/OMNIA-INVARIANCE

Scan date:

2026-04-30


---

Purpose

This scan checks whether the Ω≈0.6 candidate region appears in existing OMNIA-INVARIANCE outputs.

No new metric was introduced.

The scan only searched existing JSON / JSONL result files.


---

Raw scan summary

{
  "omega_count": 20,
  "omega_mean": 0.5113864149467715,
  "omega_std": 0.19202211146465722,
  "omega_min": 0.1275,
  "omega_max": 0.6446806798878102,
  "transition_band": [0.55, 0.65],
  "transition_count": 15,
  "transition_rate": 0.75
}


---

Important correction

The raw scan included fields such as:

omega_volatility

These are not equivalent to mean Ω.

Therefore the raw mean is not yet clean evidence.

A filtered scan is required using only fields such as:

mean_omega
mean_Omega
omega_score
omega

and excluding:

omega_volatility
nearest_distance
embedding_pc1


---

Visible candidate evidence

The following cross-domain Ω values were observed:

physics ≈ 0.644
logic   ≈ 0.619
finance ≈ 0.638
crypto  ≈ 0.598
llm     ≈ 0.602

These values all fall near the provisional transition band:

0.55 ≤ Ω ≤ 0.65


---

Provisional interpretation

Ω≈0.6 is not yet a confirmed constant.

However, the candidate region is visibly present in existing OMNIA-INVARIANCE outputs.

Current status:

observed candidate region

not:

confirmed structural constant


---

Next step

Run a filtered scan using only canonical mean Ω fields.

Target fields:

mean_omega
mean_Omega
omega_score
omega

Excluded fields:

omega_volatility
nearest_distance
embedding_pc1

