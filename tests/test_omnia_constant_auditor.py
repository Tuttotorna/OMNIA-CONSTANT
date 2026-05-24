import subprocess
import sys

from omnia_constant_auditor.core import (
    Observation,
    analyze_observations,
    normalize_value,
    numeric_variation,
    parse_number,
    read_jsonl,
    structural_variation,
)


def test_normalize_value():
    assert normalize_value("  STOP!! ") == "stop"
    assert normalize_value("A   B") == "a b"


def test_parse_number():
    assert parse_number("1.25") == 1.25
    assert parse_number("-2") == -2.0
    assert parse_number("abc") is None


def test_numeric_variation_stable():
    assert numeric_variation([1.0, 1.001, 0.999]) < 0.01


def test_numeric_variation_large():
    assert numeric_variation([1.0, 10.0]) >= 0.40


def test_structural_variation_stable():
    assert structural_variation(["STOP", "stop", " STOP "]) == 0.0


def test_structural_variation_large():
    assert structural_variation(["observer suspended", "privileged observer restored"]) >= 0.40


def test_analyze_observations_counts():
    observations = [
        Observation("a", "run1", "1.0", "", "", "", ""),
        Observation("a", "run2", "1.001", "", "", "", ""),
        Observation("b", "run1", "1.0", "", "", "", ""),
        Observation("b", "run2", "1.2", "", "", "", ""),
        Observation("c", "run1", "access denied", "", "", "", ""),
        Observation("c", "run2", "access granted", "", "", "", ""),
    ]

    result = analyze_observations(observations)
    assert result["summary"]["total_constants"] == 3
    assert result["summary"]["constant"] >= 1
    assert result["summary"]["drift"] >= 1
    assert result["summary"]["rupture"] >= 1
    assert "certificate" in result


def test_read_jsonl(tmp_path):
    p = tmp_path / "obs.jsonl"
    p.write_text(
        '{"constant_id":"x","context_id":"run1","value":1}\n'
        '{"constant_id":"x","context_id":"run2","value":1}\n',
        encoding="utf-8",
    )

    rows = read_jsonl(str(p))
    assert len(rows) == 2
    assert rows[0].constant_id == "x"


def test_duplicate_rejected(tmp_path):
    p = tmp_path / "obs.jsonl"
    p.write_text(
        '{"constant_id":"x","context_id":"run1","value":1}\n'
        '{"constant_id":"x","context_id":"run1","value":2}\n',
        encoding="utf-8",
    )

    try:
        read_jsonl(str(p))
        assert False, "expected duplicate error"
    except ValueError as e:
        assert "Duplicate" in str(e)


def test_cli_writes_reports(tmp_path):
    input_path = tmp_path / "obs.jsonl"
    out_dir = tmp_path / "report"

    input_path.write_text(
        '{"constant_id":"a","context_id":"run1","value":1.0}\n'
        '{"constant_id":"a","context_id":"run2","value":1.0}\n'
        '{"constant_id":"b","context_id":"run1","value":"observer suspended"}\n'
        '{"constant_id":"b","context_id":"run2","value":"privileged observer restored"}\n',
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omnia_constant_auditor.cli",
            "--input",
            str(input_path),
            "--out-dir",
            str(out_dir),
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0
    assert (out_dir / "report.json").exists()
    assert (out_dir / "report.csv").exists()
    assert (out_dir / "report.html").exists()
    assert (out_dir / "drift_constants.jsonl").exists()
    assert (out_dir / "rupture_constants.jsonl").exists()
    assert (out_dir / "certificate.json").exists()


def test_cli_fail_on_rupture(tmp_path):
    input_path = tmp_path / "obs.jsonl"
    out_dir = tmp_path / "report"

    input_path.write_text(
        '{"constant_id":"b","context_id":"run1","value":"access denied"}\n'
        '{"constant_id":"b","context_id":"run2","value":"account unlocked"}\n',
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omnia_constant_auditor.cli",
            "--input",
            str(input_path),
            "--out-dir",
            str(out_dir),
            "--fail-on-rupture",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 3


def test_cli_stable_only_passes_gate(tmp_path):
    input_path = tmp_path / "obs.jsonl"
    out_dir = tmp_path / "report"

    input_path.write_text(
        '{"constant_id":"a","context_id":"run1","value":1.0}\n'
        '{"constant_id":"a","context_id":"run2","value":1.001}\n',
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "omnia_constant_auditor.cli",
            "--input",
            str(input_path),
            "--out-dir",
            str(out_dir),
            "--fail-on-drift",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0
