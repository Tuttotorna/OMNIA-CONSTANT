# SEMANTIC_INVARIANCE_TEST_RESULT

## Status

```text
RESULT: FAILED
```

---

# Objective

Evaluate whether Ω remains stable under:

- semantic-preserving transformations
- semantic-changing transformations

The goal was to determine whether Ω reacts primarily to:

```text
syntax
vs
semantic deformation
```

---

# Dataset

Total cases:

```text
20
```

Groups:

| Group | Count |
|---|---:|
| semantic_preserving | 10 |
| semantic_changing | 10 |

---

# Core Results

## Mean ΔΩ

| Group | Mean ΔΩ |
|---|---:|
| semantic_preserving | 1.302535 |
| semantic_changing | 0.373546 |

Difference:

```text
changing - preserving = -0.928989
```

Unexpected inversion.

Semantic-preserving transformations produced
larger ΔΩ than semantic-changing transformations.

---

## Median ΔΩ

| Group | Median ΔΩ |
|---|---:|
| semantic_preserving | 0.893893 |
| semantic_changing | 0.0 |

This confirms the inversion is not caused only by outliers.

---

# Strongest Counterexamples

## Semantic-preserving transforms with very high ΔΩ

### case_007

```python
if flag:
    return True
else:
    return False
```

↓

```python
return bool(flag)
```

Result:

```text
ΔΩ = 5.163589
```

---

### case_002

```python
if key in d:
    x = d[key]
```

↓

```python
x = d.get(key)
```

Result:

```text
ΔΩ = 3.098612
```

---

### case_004

```python
tmp = f(x)
return tmp
```

↓

```python
return f(x)
```

Result:

```text
ΔΩ = 1.516291
```

---

# Semantic-changing transforms with ΔΩ ≈ 0

### case_102

```python
if a and b:
    run()
```

↓

```python
if a or b:
    run()
```

Result:

```text
ΔΩ = 0.0
```

---

### case_103

```python
for x in xs:
    break
```

↓

```python
for x in xs:
    continue
```

Result:

```text
ΔΩ = 0.0
```

---

### case_104

```python
items.append(x)
```

↓

```python
items.extend(x)
```

Result:

```text
ΔΩ = 0.0
```

---

### case_105

```python
return value
```

↓

```python
return None
```

Result:

```text
ΔΩ = 0.0
```

---

### case_108

```python
total += x
```

↓

```python
total -= x
```

Result:

```text
ΔΩ = 0.0
```

---

# Interpretation

The v0 proxy failed to distinguish:

```text
semantic equivalence
vs
semantic mutation
```

Instead, it reacted strongly to:

- syntactic compression
- keyword count variation
- representation style
- surface structural rewriting

while ignoring:

- logical operator inversion
- control transfer mutation
- semantic arithmetic mutation
- execution behavior changes

---

# Structural Conclusion

The experiment falsifies the hypothesis:

```text
The current Ω proxy captures semantic deformation.
```

Instead, the evidence supports:

```text
The v0 proxy is syntax-sensitive and semantic-blind.
```

---

# Important Scientific Outcome

This is not a failure of methodology.

This is a successful falsification of an insufficient proxy.

The test eliminated a false interpretation:

```text
Ω != simple keyword/control-count metric
```

---

# Implications

The following interpretation is no longer defensible:

```text
High Ω automatically implies semantic instability.
```

At least not with the current proxy implementation.

---

# What Survived

The test does NOT invalidate previous findings that:

- Ω resists reduction to churn
- Ω resists reduction to topology
- Ω resists reduction to co-change history
- Ω partially correlates with AST deformation

It only invalidates this specific simplified semantic proxy.

---

# Next Step

```text
SEMANTIC_INVARIANCE_TEST v1
```

Requirements for v1:

- no keyword-count proxy
- AST-aware comparison
- operator-sensitive analysis
- semantic mutation sensitivity
- execution-path deformation metrics

---

# Final Verdict

```text
The v0 semantic invariance proxy failed.

It measures representational perturbation,
not semantic deformation.
```