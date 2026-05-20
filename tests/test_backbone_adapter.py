from omnia_constant import (
    adapt_constant_measurement_to_boundary_certificate,
    observe_constant_envelope,
    run_constant_backbone_flow,
)
from omnia_limit import validate_certificate


def test_adapt_constant_measurement_to_boundary_certificate_continue_flow():
    measurement = {
        "constant_score": 0.82,
        "perturbation_step": 2,
        "gate_status": "CONTINUE",
        "constant_family": "numeric_residual",
        "measurement_window": "local",
    }

    raw_certificate = adapt_constant_measurement_to_boundary_certificate(
        measurement,
        target_repository="OMNIA-CONSTANT",
        certificate_id="constant-boundary-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    cert = validate_certificate(raw_certificate)

    assert cert.certificate_id == "constant-boundary-cert"
    assert cert.target_repository == "OMNIA-CONSTANT"
    assert round(cert.ast_deformation_index, 2) == 0.18
    assert cert.perturbation_step == 2
    assert cert.should_continue is True
    assert cert.saturation_detected is False
    assert raw_certificate["metrics"]["domain"] == "constant_stability"
    assert raw_certificate["metrics"]["constant_family"] == "numeric_residual"
    assert raw_certificate["metrics"]["measurement_window"] == "local"
    assert raw_certificate["metrics"]["constant_score"] == 0.82


def test_run_constant_backbone_flow_stop_flow():
    measurement = {
        "stability_score": 0.97,
        "perturbation_step": 5,
        "gate_status": "STOP",
        "constant_family": "structural_fixed_point",
        "measurement_window": "trajectory",
    }

    observation = run_constant_backbone_flow(
        measurement,
        target_repository="OMNIA-CONSTANT",
        certificate_id="constant-stop-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-CONSTANT"
    assert observation["role"] == "constant_stability_producer_adapter"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "constant-stop-cert"
    assert observation["target_repository"] == "OMNIA-CONSTANT"
    assert observation["saturation_detected"] is True
    assert round(observation["ast_deformation_index"], 2) == 0.03
    assert observation["perturbation_step"] == 5
    assert observation["absolute_constancy_claim"] is None
    assert observation["backbone_contract_preserved"] is True


def test_run_constant_backbone_flow_continue_flow():
    measurement = {
        "constant_drift": 0.21,
        "perturbation_step": 1,
        "gate_status": "CONTINUE",
        "constant_family": "symbolic_stability",
        "measurement_window": "single_step",
    }

    observation = run_constant_backbone_flow(
        measurement,
        target_repository="OMNIA-CONSTANT",
        certificate_id="constant-continue-cert",
        timestamp="2026-05-20T20:00:00Z",
    )

    assert observation["observer"] == "OMNIA-CONSTANT"
    assert observation["role"] == "constant_stability_producer_adapter"
    assert observation["observed_status"] == "GATE_OPEN_MEASUREMENT_REQUIRED"
    assert observation["certificate_id"] == "constant-continue-cert"
    assert observation["target_repository"] == "OMNIA-CONSTANT"
    assert observation["saturation_detected"] is False
    assert observation["ast_deformation_index"] == 0.21
    assert observation["perturbation_step"] == 1
    assert observation["absolute_constancy_claim"] is None
    assert observation["backbone_contract_preserved"] is True


def test_observe_existing_envelope_without_absolute_constancy_claim():
    envelope = {
        "envelope_id": "constant-env",
        "timestamp": "2026-05-20T20:00:00Z",
        "validation_status": "GATE_CLOSED_SATURATION_REACHED",
        "details": {
            "target_repository": "OMNIA",
            "certificate_id": "existing-constant-cert",
            "saturation_detected": True,
            "ast_deformation_index": 0.04,
            "perturbation_step": 9,
        },
    }

    observation = observe_constant_envelope(envelope)

    assert observation["observer"] == "OMNIA-CONSTANT"
    assert observation["role"] == "constant_stability_producer_adapter"
    assert observation["observed_status"] == "GATE_CLOSED_SATURATION_REACHED"
    assert observation["certificate_id"] == "existing-constant-cert"
    assert observation["target_repository"] == "OMNIA"
    assert observation["absolute_constancy_claim"] is None
    assert observation["backbone_contract_preserved"] is True
