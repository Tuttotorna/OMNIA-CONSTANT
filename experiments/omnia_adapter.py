#!/usr/bin/env python3
"""
OMNIA Adapter · OMNIA-CONSTANT

Purpose:
    Provide a unified bridge between OMNIA outputs
    and OMNIA-CONSTANT experiments.

OMNIA-CONSTANT does NOT define Ω independently.

It consumes canonical omega_score values produced by OMNIA.
"""

from typing import Any, Dict, List


# -------------------------------------------------------------------
# OPTIONAL IMPORT
# -------------------------------------------------------------------

try:
    import omnia  # type: ignore
except ImportError:
    omnia = None


# -------------------------------------------------------------------
# STANDARD OUTPUT FIELDS
# -------------------------------------------------------------------

STANDARD_FIELDS = [
    "omega_score",
    "sei_score",
    "iri_score",
    "drift_score",
    "limit_triggered",
    "gate_status",
    "reason_code",
]


# -------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------

def normalize_output(result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize OMNIA output into a stable schema.
    """

    normalized = {}

    for field in STANDARD_FIELDS:
        normalized[field] = result.get(field)

    return normalized


def validate_output(result: Dict[str, Any]) -> bool:
    """
    Minimal validation for OMNIA output compatibility.
    """

    omega = result.get("omega_score")

    if omega is None:
        return False

    if not isinstance(omega, (int, float)):
        return False

    if omega < 0.0 or omega > 1.0:
        return False

    return True


# -------------------------------------------------------------------
# MAIN ADAPTER
# -------------------------------------------------------------------

def run_omnia(
    data: Any,
    *,
    metadata: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Execute OMNIA and return normalized output.

    Parameters
    ----------
    data:
        Input system / trajectory / sequence / structure.

    metadata:
        Optional experiment metadata.

    Returns
    -------
    Dict[str, Any]
        Normalized OMNIA-compatible output.
    """

    metadata = metadata or {}

    if omnia is None:
        raise ImportError(
            "OMNIA package not installed.\n"
            "Install OMNIA before running OMNIA-CONSTANT experiments."
        )

    # ---------------------------------------------------------------
    # IMPORTANT:
    #
    # Replace this section with the canonical OMNIA call.
    #
    # Example placeholders:
    #
    # result = omnia.evaluate(data)
    # result = omnia.measure(data)
    # result = omnia.run(data)
    #
    # depending on actual OMNIA API structure.
    # ---------------------------------------------------------------

    if hasattr(omnia, "run"):
        raw_result = omnia.run(data)

    elif hasattr(omnia, "measure"):
        raw_result = omnia.measure(data)

    elif hasattr(omnia, "evaluate"):
        raw_result = omnia.evaluate(data)

    else:
        raise RuntimeError(
            "No compatible OMNIA execution function found."
        )

    # ---------------------------------------------------------------
    # Normalize
    # ---------------------------------------------------------------

    if not isinstance(raw_result, dict):
        raise TypeError(
            "OMNIA output must be a dictionary."
        )

    normalized = normalize_output(raw_result)

    normalized["metadata"] = metadata

    # ---------------------------------------------------------------
    # Validation
    # ---------------------------------------------------------------

    if not validate_output(normalized):
        raise ValueError(
            "Invalid OMNIA output format."
        )

    return normalized


# -------------------------------------------------------------------
# EXTRACTION HELPERS
# -------------------------------------------------------------------

def extract_omega(result: Dict[str, Any]) -> float:
    """
    Extract canonical Ω score.
    """

    return float(result["omega_score"])


def extract_transition_region(
    result: Dict[str, Any],
    *,
    low: float = 0.55,
    high: float = 0.65,
) -> bool:
    """
    Check whether Ω falls inside provisional transition region.
    """

    omega = extract_omega(result)

    return low <= omega <= high


# -------------------------------------------------------------------
# DEMO
# -------------------------------------------------------------------

def demo():
    """
    Minimal adapter demo.
    """

    sample_data = [1, 2, 3, 4, 5]

    try:
        result = run_omnia(
            sample_data,
            metadata={
                "experiment": "adapter_demo",
            },
        )

        print("=" * 80)
        print("OMNIA ADAPTER DEMO")
        print("=" * 80)

        for k, v in result.items():
            print(f"{k}: {v}")

        print()
        print(
            "inside_transition_region:",
            extract_transition_region(result),
        )

    except Exception as e:
        print("[ERROR]")
        print(e)


if __name__ == "__main__":
    demo()