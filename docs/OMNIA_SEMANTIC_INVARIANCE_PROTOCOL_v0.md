# OMNIA Semantic Invariance Protocol v0

## Objective

Determine whether Ω reacts primarily to:

- syntactic deformation
- semantic deformation
- or both

The protocol isolates controlled transformations
on small code fragments.

---

# Core Question

```text
If program meaning is preserved,
does Ω remain stable?


---

Experimental Design

Two transformation groups are used.


---

Group A — Semantic Preserving

Transformations that preserve executable meaning.

Examples:

variable rename

comprehension rewrite

dict.get rewrite

inline temporary variable

formatting normalization

reorder independent assignments

extract helper function


Expected behavior:

ΔΩ should remain low.


---

Group B — Semantic Changing

Transformations that alter execution behavior.

Examples:

> -> >=



and -> or

break -> continue

append -> extend

return path modification

mutation insertion

exception behavior change


Expected behavior:

ΔΩ should increase.


---

Measurement

For each pair:

1. compute Ω(original)


2. compute Ω(transformed)


3. compute:



ΔΩ = |Ω_transformed - Ω_original|


---

Hypotheses

H1

Semantic-preserving transforms produce lower ΔΩ
than semantic-changing transforms.

H0

No significant difference exists between groups.


---

Statistical Tests

Recommended:

Mann-Whitney U

Kolmogorov-Smirnov

Distribution overlap analysis



---

Interpretation

Strong Support

ΔΩ_preserving << ΔΩ_changing

Possible interpretation:

Ω captures executable structural deformation.


---

Weak Support

Partial separation only.

Possible interpretation:

Ω reacts to mixed syntactic + semantic stress.


---

Failure

No separation.

Possible interpretation:

Ω is mainly representation-sensitive.


---

Constraints

The experiment must avoid:

repository history

co-change data

external metadata

commit topology

human annotations


Only code transformation itself is evaluated.


---

Current Status

Protocol Version: v0
Status: pending execution

```json id="o5h6qk"
{"id":"case_001","category":"semantic_preserving","original":"a = a + 1","transformed":"a += 1"}
{"id":"case_002","category":"semantic_preserving","original":"if key in d:\n    x = d[key]","transformed":"x = d.get(key)"}
{"id":"case_003","category":"semantic_preserving","original":"for x in xs:\n    out.append(f(x))","transformed":"out = [f(x) for x in xs]"}
{"id":"case_004","category":"semantic_preserving","original":"tmp = f(x)\nreturn tmp","transformed":"return f(x)"}
{"id":"case_005","category":"semantic_preserving","original":"a = 1\nb = 2","transformed":"b = 2\na = 1"}
{"id":"case_006","category":"semantic_preserving","original":"result = value","transformed":"output = value"}
{"id":"case_007","category":"semantic_preserving","original":"if flag:\n    return True\nelse:\n    return False","transformed":"return bool(flag)"}
{"id":"case_008","category":"semantic_preserving","original":"items = []\nfor x in xs:\n    items.append(x*x)","transformed":"items = [x*x for x in xs]"}
{"id":"case_009","category":"semantic_preserving","original":"x = x * 2","transformed":"x *= 2"}
{"id":"case_010","category":"semantic_preserving","original":"name = user_name","transformed":"n = user_name"}

{"id":"case_101","category":"semantic_changing","original":"if x > 0:\n    return 1","transformed":"if x >= 0:\n    return 1"}
{"id":"case_102","category":"semantic_changing","original":"if a and b:\n    run()","transformed":"if a or b:\n    run()"}
{"id":"case_103","category":"semantic_changing","original":"for x in xs:\n    break","transformed":"for x in xs:\n    continue"}
{"id":"case_104","category":"semantic_changing","original":"items.append(x)","transformed":"items.extend(x)"}
{"id":"case_105","category":"semantic_changing","original":"return value","transformed":"return None"}
{"id":"case_106","category":"semantic_changing","original":"if err:\n    raise Exception()","transformed":"if err:\n    pass"}
{"id":"case_107","category":"semantic_changing","original":"while x < 10:\n    x += 1","transformed":"while x <= 10:\n    x += 1"}
{"id":"case_108","category":"semantic_changing","original":"total += x","transformed":"total -= x"}
{"id":"case_109","category":"semantic_changing","original":"data[key] = value","transformed":"del data[key]"}
{"id":"case_110","category":"semantic_changing","original":"return a / b","transformed":"return a // b"}

# examples/run_semantic_invariance_test.py

import json
import math
import statistics
from pathlib import Path

DATASET = Path("examples/semantic_invariance_pairs.jsonl")

def simple_omega(code: str):
    lines = code.count("\n") + 1
    branches = sum(code.count(x) for x in ["if ", "for ", "while ", "try", "except"])
    assigns = code.count("=")
    returns = code.count("return")
    entropy = len(set(code.split()))

    return (
        branches * 2.0
        + assigns * 0.5
        + returns * 1.5
        + math.log(entropy + 1)
        + math.log(lines + 1)
    )

records = []

with open(DATASET, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            records.append(json.loads(line))

results = []

for r in records:
    omega_original = simple_omega(r["original"])
    omega_transformed = simple_omega(r["transformed"])

    delta = abs(omega_transformed - omega_original)

    results.append({
        "id": r["id"],
        "category": r["category"],
        "omega_original": omega_original,
        "omega_transformed": omega_transformed,
        "delta_omega": delta,
    })

preserving = [x["delta_omega"] for x in results if x["category"] == "semantic_preserving"]
changing = [x["delta_omega"] for x in results if x["category"] == "semantic_changing"]

summary = {
    "preserving_mean_delta": statistics.mean(preserving),
    "changing_mean_delta": statistics.mean(changing),
    "preserving_median_delta": statistics.median(preserving),
    "changing_median_delta": statistics.median(changing),
    "preserving_max_delta": max(preserving),
    "changing_max_delta": max(changing),
}

print("=" * 80)
print("SEMANTIC INVARIANCE TEST")
print("=" * 80)
print()

print(json.dumps(summary, indent=2))

Path("results").mkdir(exist_ok=True)

with open("results/SEMANTIC_INVARIANCE_TEST_RESULT.md", "w", encoding="utf-8") as f:
    f.write("# SEMANTIC INVARIANCE TEST RESULT\n\n")
    f.write("## Summary\n\n")
    f.write("```json\n")
    f.write(json.dumps(summary, indent=2))
    f.write("\n```\n\n")

    f.write("## Per-case Results\n\n")

    for r in results:
        f.write(
            f"- {r['id']} | {r['category']} | ΔΩ={r['delta_omega']:.4f}\n"
        )

print()
print("Saved:")
print("results/SEMANTIC_INVARIANCE_TEST_RESULT.md")

# results/SEMANTIC_INVARIANCE_TEST_RESULT.md

# SEMANTIC INVARIANCE TEST RESULT

## Status

```text
Pending execution


---

Objective

Measure whether Ω remains stable under:

semantic-preserving transformations

semantic-changing transformations



---

Expected Behavior

Semantic Preserving

Expected:

Low ΔΩ

Semantic Changing

Expected:

Higher ΔΩ


---

Interpretation Matrix

Result	Interpretation

preserving << changing	Ω sensitive to semantic deformation
preserving ≈ changing	Ω mostly syntactic
mixed separation	Ω reacts to hybrid structural stress



---

Important Note

This experiment isolates:

controlled causal perturbations

instead of noisy repository history.

This is a substantially stronger validation setting.


---

Final Status

Awaiting execution