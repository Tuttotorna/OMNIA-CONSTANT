import csv
import json
import math
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class Observation:
    constant_id: str
    context_id: str
    value: str
    domain: str
    run_id: str
    expected: str
    note: str


@dataclass(frozen=True)
class ConstantAnalysis:
    constant_id: str
    observations: int
    contexts: int
    domains: int
    status: str
    constancy_score: float
    variation_score: float
    rupture_score: float
    mode: str
    reference_value: str
    min_value: Optional[float]
    max_value: Optional[float]
    mean_value: Optional[float]
    values: Dict[str, str]
    notes: List[str]


def normalize_value(value: Any) -> str:
    text = "" if value is None else str(value)
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\.\-\+\s]", "", text)
    return text.strip()


def parse_number(value: Any) -> Optional[float]:
    text = normalize_value(value)
    if not text:
        return None

    if re.fullmatch(r"[-+]?\d+(\.\d+)?", text):
        try:
            return float(text)
        except Exception:
            return None

    return None


def tokenize(value: str) -> List[str]:
    normalized = normalize_value(value)
    if not normalized:
        return []
    return normalized.split()


def char_similarity(a: str, b: str) -> float:
    na = normalize_value(a)
    nb = normalize_value(b)

    if na == nb:
        return 1.0

    if not na or not nb:
        return 0.0

    m = len(na)
    n = len(nb)

    previous = list(range(n + 1))

    for i in range(1, m + 1):
        current = [i] + [0] * n
        for j in range(1, n + 1):
            cost = 0 if na[i - 1] == nb[j - 1] else 1
            current[j] = min(
                previous[j] + 1,
                current[j - 1] + 1,
                previous[j - 1] + cost,
            )
        previous = current

    distance = previous[n]
    scale = max(m, n)

    return max(0.0, 1.0 - (distance / scale))


def jaccard_similarity(a: str, b: str) -> float:
    ta = set(tokenize(a))
    tb = set(tokenize(b))

    if not ta and not tb:
        return 1.0

    if not ta or not tb:
        return 0.0

    return len(ta & tb) / len(ta | tb)


def structural_similarity(a: str, b: str) -> float:
    if normalize_value(a) == normalize_value(b):
        return 1.0

    return round((0.65 * char_similarity(a, b)) + (0.35 * jaccard_similarity(a, b)), 12)


def numeric_variation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0

    if len(numbers) == 1:
        return 0.0

    lo = min(numbers)
    hi = max(numbers)
    mean_abs = sum(abs(x) for x in numbers) / len(numbers)

    scale = max(abs(hi), abs(lo), mean_abs, 1.0)
    return round((hi - lo) / scale, 12)


def structural_variation(values: List[str]) -> float:
    if len(values) <= 1:
        return 0.0

    sims = []

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            sims.append(structural_similarity(values[i], values[j]))

    if not sims:
        return 0.0

    return round(1.0 - min(sims), 12)


def read_jsonl(path: str) -> List[Observation]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)

    observations = []

    with p.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw:
                continue

            try:
                obj = json.loads(raw)
            except json.JSONDecodeError as e:
                raise ValueError("Invalid JSONL at line " + str(line_no) + ": " + str(e))

            for field in ["constant_id", "context_id", "value"]:
                if field not in obj:
                    raise ValueError("Missing required field '" + field + "' at line " + str(line_no))

            observations.append(
                Observation(
                    constant_id=str(obj["constant_id"]),
                    context_id=str(obj["context_id"]),
                    value=str(obj["value"]),
                    domain=str(obj.get("domain", "")),
                    run_id=str(obj.get("run_id", "")),
                    expected=str(obj.get("expected", "")),
                    note=str(obj.get("note", "")),
                )
            )

    if not observations:
        raise ValueError("No observations found in " + path)

    seen = set()
    for obs in observations:
        key = (obs.constant_id, obs.context_id, obs.run_id)
        if key in seen:
            raise ValueError("Duplicate constant_id + context_id + run_id: " + obs.constant_id + " / " + obs.context_id + " / " + obs.run_id)
        seen.add(key)

    return observations


def group_observations(observations: List[Observation]) -> Dict[str, List[Observation]]:
    grouped = defaultdict(list)
    for obs in observations:
        grouped[obs.constant_id].append(obs)
    return dict(grouped)


def analyze_constant(
    constant_id: str,
    observations: List[Observation],
    drift_threshold: float = 0.05,
    rupture_threshold: float = 0.40,
) -> ConstantAnalysis:
    ordered = sorted(observations, key=lambda x: (x.domain, x.context_id, x.run_id))
    values = {}

    for obs in ordered:
        key = obs.context_id if not obs.run_id else obs.context_id + "::" + obs.run_id
        values[key] = obs.value

    normalized_values = [normalize_value(obs.value) for obs in ordered]
    parsed = [parse_number(obs.value) for obs in ordered]
    numeric_values = [x for x in parsed if x is not None]

    all_numeric = len(numeric_values) == len(ordered)

    if all_numeric:
        mode = "numeric"
        variation = numeric_variation(numeric_values)
        min_value = min(numeric_values)
        max_value = max(numeric_values)
        mean_value = round(sum(numeric_values) / len(numeric_values), 12)
    else:
        mode = "structural"
        variation = structural_variation([obs.value for obs in ordered])
        min_value = None
        max_value = None
        mean_value = None

    rupture_score = variation
    constancy_score = round(max(0.0, 1.0 - variation), 12)

    if variation <= drift_threshold:
        status = "constant"
    elif variation >= rupture_threshold:
        status = "rupture"
    else:
        status = "drift"

    notes = [obs.note for obs in ordered if obs.note]
    domains = len(set(obs.domain for obs in ordered if obs.domain))
    contexts = len(set(obs.context_id for obs in ordered))

    return ConstantAnalysis(
        constant_id=constant_id,
        observations=len(ordered),
        contexts=contexts,
        domains=domains,
        status=status,
        constancy_score=constancy_score,
        variation_score=round(variation, 12),
        rupture_score=round(rupture_score, 12),
        mode=mode,
        reference_value=ordered[0].value,
        min_value=min_value,
        max_value=max_value,
        mean_value=mean_value,
        values=values,
        notes=notes,
    )


def analyze_observations(
    observations: List[Observation],
    drift_threshold: float = 0.05,
    rupture_threshold: float = 0.40,
) -> Dict[str, Any]:
    grouped = group_observations(observations)

    constants = [
        analyze_constant(
            constant_id=constant_id,
            observations=items,
            drift_threshold=drift_threshold,
            rupture_threshold=rupture_threshold,
        )
        for constant_id, items in sorted(grouped.items())
    ]

    rows = [asdict(c) for c in constants]

    constant_rows = [r for r in rows if r["status"] == "constant"]
    drift_rows = [r for r in rows if r["status"] == "drift"]
    rupture_rows = [r for r in rows if r["status"] == "rupture"]

    total_constants = len(rows)
    total_observations = len(observations)

    mean_constancy_score = (
        sum(r["constancy_score"] for r in rows) / total_constants if total_constants else 0.0
    )

    worst = min(rows, key=lambda r: r["constancy_score"]) if rows else None

    summary = {
        "total_constants": total_constants,
        "total_observations": total_observations,
        "constant": len(constant_rows),
        "drift": len(drift_rows),
        "rupture": len(rupture_rows),
        "constant_rate": round(len(constant_rows) / total_constants, 12) if total_constants else 0.0,
        "drift_rate": round(len(drift_rows) / total_constants, 12) if total_constants else 0.0,
        "rupture_rate": round(len(rupture_rows) / total_constants, 12) if total_constants else 0.0,
        "mean_constancy_score": round(mean_constancy_score, 12),
        "worst_constant_id": worst["constant_id"] if worst else None,
        "worst_constancy_score": worst["constancy_score"] if worst else None,
        "problem_solved": "Measures whether candidate constants remain stable across supplied observation contexts.",
    }

    certificate = {
        "audit_type": "omnia_constant_audit",
        "summary": summary,
        "thresholds": {
            "drift_threshold": drift_threshold,
            "rupture_threshold": rupture_threshold,
        },
        "boundary": "measurement only; constant means stability across supplied contexts, not universal semantic truth",
        "measurement_language": [
            "constant_id",
            "context_id",
            "numeric_variation",
            "structural_variation",
            "constancy_score",
            "variation_score",
            "constant_drift_rupture",
        ],
    }

    return {
        "summary": summary,
        "thresholds": {
            "drift_threshold": drift_threshold,
            "rupture_threshold": rupture_threshold,
        },
        "certificate": certificate,
        "constants": rows,
    }


def write_json(path: str, obj: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "constant_id",
        "status",
        "observations",
        "contexts",
        "domains",
        "mode",
        "constancy_score",
        "variation_score",
        "rupture_score",
        "reference_value",
        "min_value",
        "max_value",
        "mean_value",
        "notes",
    ]

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        for row in result["constants"]:
            out = dict(row)
            out["notes"] = " | ".join(row.get("notes", []))
            writer.writerow({k: out.get(k, "") for k in fields})


def html_escape(x: Any) -> str:
    return (
        str(x)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def write_html_report(path: str, result: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    summary = result["summary"]

    rows = []
    for r in result["constants"]:
        if r["status"] == "constant":
            continue

        rows.append(
            "<tr>"
            + "<td>" + html_escape(r["constant_id"]) + "</td>"
            + "<td>" + html_escape(r["status"]) + "</td>"
            + "<td>" + html_escape(r["mode"]) + "</td>"
            + "<td>" + html_escape(r["observations"]) + "</td>"
            + "<td>" + html_escape(r["contexts"]) + "</td>"
            + "<td>" + html_escape(r["constancy_score"]) + "</td>"
            + "<td>" + html_escape(r["variation_score"]) + "</td>"
            + "<td><pre>" + html_escape(json.dumps(r["values"], indent=2, ensure_ascii=False)) + "</pre></td>"
            + "</tr>"
        )

    html = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>OMNIA Constant Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 32px;
      line-height: 1.45;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      vertical-align: top;
    }}
    th {{
      background: #f2f2f2;
    }}
    pre {{
      white-space: pre-wrap;
      margin: 0;
    }}
    .box {{
      background: #f8f8f8;
      padding: 16px;
      margin-bottom: 24px;
      border: 1px solid #eee;
    }}
  </style>
</head>
<body>
  <h1>OMNIA Constant Report</h1>

  <div class="box">
    <p><b>Total constants:</b> {total_constants}</p>
    <p><b>Total observations:</b> {total_observations}</p>
    <p><b>Constant:</b> {constant}</p>
    <p><b>Drift:</b> {drift}</p>
    <p><b>Rupture:</b> {rupture}</p>
    <p><b>Constant rate:</b> {constant_rate}</p>
    <p><b>Mean constancy score:</b> {mean_constancy_score}</p>
    <p><b>Worst constant:</b> {worst_constant_id}</p>
  </div>

  <h2>Drift / Rupture Constants</h2>

  <table>
    <tr>
      <th>Constant</th>
      <th>Status</th>
      <th>Mode</th>
      <th>Observations</th>
      <th>Contexts</th>
      <th>Constancy score</th>
      <th>Variation score</th>
      <th>Values</th>
    </tr>
    {rows}
  </table>

  <h2>Boundary</h2>
  <p>Constant means stability across supplied observation contexts. This is not a universal semantic truth claim.</p>
</body>
</html>
""".format(
        total_constants=summary["total_constants"],
        total_observations=summary["total_observations"],
        constant=summary["constant"],
        drift=summary["drift"],
        rupture=summary["rupture"],
        constant_rate=summary["constant_rate"],
        mean_constancy_score=summary["mean_constancy_score"],
        worst_constant_id=summary["worst_constant_id"],
        rows="".join(rows),
    )

    p.write_text(html, encoding="utf-8")


def write_constant_jsonl(path: str, result: Dict[str, Any], status: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", encoding="utf-8") as f:
        for r in result["constants"]:
            if r["status"] == status:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_all_reports(out_dir: str, result: Dict[str, Any]) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    write_json(str(out / "report.json"), result)
    write_csv_report(str(out / "report.csv"), result)
    write_html_report(str(out / "report.html"), result)
    write_constant_jsonl(str(out / "drift_constants.jsonl"), result, "drift")
    write_constant_jsonl(str(out / "rupture_constants.jsonl"), result, "rupture")
    write_json(str(out / "certificate.json"), result["certificate"])
