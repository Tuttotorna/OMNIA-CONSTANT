
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_public_entrypoints_exist():
    required = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "pyproject.toml",
        "pytest.ini",
        "docs/CONSTANT_SCOPE.md",
        "docs/RESULTS_INDEX.md",
        "docs/REPOSITORY_STATUS.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_core_directories_exist():
    for rel in ["docs", "results", "papers", "experiments"]:
        assert (ROOT / rel).exists(), rel

def test_key_result_files_exist():
    required = [
        "results/CONFIRMED_CANDIDATE_REGION.md",
        "results/NULL_RANDOM_BASELINE_RESULT.md",
        "results/PATCH_GEOMETRY_TEST_RESULT.md",
        "results/PATCH_GEOMETRY_AST_TEST_RESULT.md",
        "results/CONTROL_FLOW_ABLATION_TEST_RESULT.md",
        "papers/SEMANTIC_INVARIANCE_TEST_RESULT.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_readme_boundary_terms():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "measurement != inference != decision" in text
    assert "not a truth oracle" in text
    assert "not a semantic judge" in text
    assert "Decision remains external" in text
    assert "No universal structural constant is declared" in text

def test_scope_terms():
    text = (ROOT / "docs" / "CONSTANT_SCOPE.md").read_text(encoding="utf-8")
    assert "falsification" in text
    assert "Ω-region behavior" in text
    assert "No universal structural constant is declared" in text
