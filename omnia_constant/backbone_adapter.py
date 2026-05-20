from __future__ import annotations

from typing import Any

from omnia import build_boundary_certificate
from omnia_limit import validate_certificate
from omnia_validation.enveloper import process_boundary_step


def _coerce_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _coerce_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _clamp_01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _derive_constant_deformation_index(measurement: dict[str, Any]) -> float:
    """Normalize constant/stability signals into the backbone deformation field.

    OMNIA-CONSTANT is a constant/stability Producer-Adapter.

    It does not define BoundaryCertificate.
    It does not define ValidationEnvelope.
    It does not decide that a structure is absolutely constant.
    It reports measured stability evidence into the canonical backbone.
    """

    if "ast_deformation_index" in measurement:
        return _coerce_float(measurement["ast_deformation_index"])

    if "deformation_index" in measurement:
        return _coerce_float(measurement["deformation_index"])

    if "constant_break" in measurement:
        return _coerce_float(measurement["constant_break"])

    if "constant_drift" in measurement:
        return _coerce_float(measurement["constant_drift"])

    if "stability_drift" in measurement:
        return _coerce_float(measurement["stability_drift"])

    if "residual_variance" in measurement:
        return _coerce_float(measurement["residual_variance"])

    if "variance" in measurement:
        return _coerce_float(measurement["variance"])

    if "constant_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["constant_score"], 1.0))
        return 1.0 - score

    if "stability_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["stability_score"], 1.0))
        return 1.0 - score

    if "invariance_score" in measurement:
        score = _clamp_01(_coerce_float(measurement["invariance_score"], 1.0))
        return 1.0 - score

    return _coerce_float(
        measurement.get(
            "drift_score",
            measurement.get("delta_omega", measurement.get("delta", 0.0)),
        )
    )


def _derive_boundary_state(measurement: dict[str, Any], deformation_index: float) -> tuple[bool, bool, str]:
    """Derive explicit boundary fields without claiming absolute constancy."""

    should_continue = measurement.get("should_continue")
    saturation_detected = measurement.get("saturation_detected")

    gate = str(
        measurement.get(
            "gate",
            measurement.get("gate_status", measurement.get("status", "")),
        )
    ).upper()

    if should_continue is None:
        if gate in {"STOP", "NO_GO", "CLOSED", "GATE_CLOSED", "SATURATED"}:
            should_continue = False
        elif gate in {"GO", "CONTINUE", "OPEN", "GATE_OPEN"}:
            should_continue = True

    if saturation_detected is None:
        if gate in {"STOP", "NO_GO", "CLOSED", "GATE_CLOSED", "SATURATED"}:
            saturation_detected = True
        elif gate in {"GO", "CONTINUE", "OPEN", "GATE_OPEN"}:
            saturation_detected = False

    if should_continue is None and saturation_detected is None:
        saturation_detected = deformation_index <= 0.05
        should_continue = not saturation_detected

    if should_continue is None:
        should_continue = not bool(saturation_detected)

    if saturation_detected is None:
        saturation_detected = not bool(should_continue)

    reason = measurement.get("reason")
    if reason is None:
        reason = (
            "Constant/stability structural saturation reached"
            if bool(saturation_detected)
            else "Constant/stability measurement still yields structural information"
        )

    return bool(should_continue), bool(saturation_detected), str(reason)


def _extract_constant_extra_metrics(measurement: dict[str, Any]) -> dict[str, Any]:
    known_keys = {
        "ast_deformation_index",
        "deformation_index",
        "constant_break",
        "constant_drift",
        "stability_drift",
        "residual_variance",
        "variance",
        "constant_score",
        "stability_score",
        "invariance_score",
        "drift_score",
        "delta_omega",
        "delta",
        "perturbation_step",
        "should_continue",
        "saturation_detected",
        "gate",
        "gate_status",
        "status",
        "reason",
    }

    return {
        key: value
        for key, value in measurement.items()
        if key not in known_keys and isinstance(value, (int, float, str, bool, type(None)))
    }


def adapt_constant_measurement_to_boundary_certificate(
    measurement: dict[str, Any],
    *,
    target_repository: str = "OMNIA-CONSTANT",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Adapt constant/stability measurements into the canonical BoundaryCertificate.

    OMNIA-CONSTANT is a Constant / Stability Producer-Adapter.

    It does not validate the contract directly.
    It does not emit a competing envelope.
    It does not claim absolute truth.
    """

    ast_deformation_index = _derive_constant_deformation_index(measurement)
    perturbation_step = _coerce_int(measurement.get("perturbation_step", 0))
    should_continue, saturation_detected, reason = _derive_boundary_state(
        measurement,
        ast_deformation_index,
    )

    extra_metrics = _extract_constant_extra_metrics(measurement)
    extra_metrics["domain"] = "constant_stability"

    for key in [
        "constant_break",
        "constant_drift",
        "stability_drift",
        "residual_variance",
        "variance",
        "constant_score",
        "stability_score",
        "invariance_score",
    ]:
        if key in measurement:
            extra_metrics[key] = measurement[key]

    return build_boundary_certificate(
        target_repository=target_repository,
        ast_deformation_index=ast_deformation_index,
        perturbation_step=perturbation_step,
        should_continue=should_continue,
        saturation_detected=saturation_detected,
        reason=reason,
        certificate_id=certificate_id,
        timestamp=timestamp,
        extra_metrics=extra_metrics,
    )


def observe_constant_envelope(envelope: dict[str, Any]) -> dict[str, Any]:
    """Observe a ValidationEnvelope from a constant/stability viewpoint.

    This is observation over validated backbone output.

    It is not a final claim that a structure is absolutely constant.
    """

    details = envelope.get("details", {})

    return {
        "observer": "OMNIA-CONSTANT",
        "role": "constant_stability_producer_adapter",
        "observed_status": envelope.get("validation_status"),
        "target_repository": details.get("target_repository"),
        "certificate_id": details.get("certificate_id"),
        "saturation_detected": details.get("saturation_detected"),
        "ast_deformation_index": details.get("ast_deformation_index"),
        "perturbation_step": details.get("perturbation_step"),
        "absolute_constancy_claim": None,
        "backbone_contract_preserved": True,
    }


def run_constant_backbone_flow(
    measurement: dict[str, Any],
    *,
    target_repository: str = "OMNIA-CONSTANT",
    certificate_id: str | None = None,
    timestamp: str | None = None,
) -> dict[str, Any]:
    """Run a constant/stability measurement through the canonical backbone.

    Flow:

    constant/stability measurement
      -> OMNIA-CONSTANT adapter
      -> BoundaryCertificate-compatible artifact
      -> omnia-limit validate_certificate()
      -> OMNIA-VALIDATION process_boundary_step()
      -> ValidationEnvelope
      -> OMNIA-CONSTANT observation

    OMNIA-CONSTANT only adapts and observes.
    """

    raw_certificate = adapt_constant_measurement_to_boundary_certificate(
        measurement,
        target_repository=target_repository,
        certificate_id=certificate_id,
        timestamp=timestamp,
    )

    validate_certificate(raw_certificate)
    envelope = process_boundary_step(raw_certificate)

    return observe_constant_envelope(envelope)
