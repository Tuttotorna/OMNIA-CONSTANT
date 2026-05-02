# SEMANTIC INVARIANCE TEST v0

## Goal

Test whether Ω behaves as a semantic-change detector or as a morphology-sensitive structural perturbation measure.

The experiment compares:

- semantic-preserving rewrites
- semantic-changing rewrites

and measures resulting ΔΩ variation.

---

# Dataset Summary

```json
{
  "cases_total": 20,
  "semantic_preserving_count": 10,
  "semantic_changing_count": 10
}


---

Global Results

Metric	Semantic-Preserving	Semantic-Changing

Mean ΔΩ	1.302535	0.373546
Median ΔΩ	0.893893	0.000000
Max ΔΩ	5.163589	2.223144
Min ΔΩ	0.000000	0.000000



---

Delta Gap

Metric	Value

Mean gap (changing - preserving)	-0.928989
Median gap (changing - preserving)	-0.893893



---

Highest ΔΩ Semantic-Preserving Cases

case_007

if flag:
    return True
else:
    return False

↓

return bool(flag)

ΔΩ = 5.163589


---

case_002

if key in d:
    x = d[key]

↓

x = d.get(key)

ΔΩ = 3.098612


---

case_004

tmp = f(x)
return tmp

↓

return f(x)

ΔΩ = 1.516291


---

Lowest ΔΩ Semantic-Changing Cases

case_102

if a and b:
    run()

↓

if a or b:
    run()

ΔΩ = 0.0


---

case_103

for x in xs:
    break

↓

for x in xs:
    continue

ΔΩ = 0.0


---

case_105

return value

↓

return None

ΔΩ = 0.0


---

Main Observation

The experiment produced the opposite of a semantic detector.

Semantic-preserving rewrites often generated larger ΔΩ than semantic-changing rewrites.

This strongly weakens the interpretation of Ω as a semantic correctness signal.


---

Interpretation

Observed evidence suggests:

Ω reacts more strongly to representational restructuring
than to semantic meaning.

In particular:

branch collapse

syntactic compression

structural simplification

AST reshaping


appear more important than logical equivalence.


---

Critical Insight

Changing meaning without changing structure often produced:

ΔΩ ≈ 0

Changing structure while preserving meaning often produced:

large ΔΩ

This suggests that Ω is:

shape-sensitive
meaning-insensitive

under the tested conditions.


---

Updated Working Hypothesis

Ω behaves as a morphology-sensitive perturbation measure
rather than a semantic transformation detector.


---

Important Boundary

This experiment does not prove that Ω is purely syntactic.

It only demonstrates that semantic equivalence alone does not explain observed ΔΩ behavior.

Further testing remains necessary.


---

Implication

Ω may be useful for:

refactoring intensity estimation

structural rewrite analysis

representational stability measurement

AI-generated code morphology evaluation


rather than:

semantic verification

correctness validation

bug detection



---

Status

Semantic reduction rejected
Morphological interpretation strengthened