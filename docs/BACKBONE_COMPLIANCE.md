# OMNIA-CONSTANT Backbone Compliance

## Role

OMNIA-CONSTANT is a Constant / Stability Producer-Adapter.

It adapts constant/stability measurements into the canonical OMNIA backbone.

It observes validated backbone output.

It is not the measurement core.

It is not the boundary validator.

It is not the validation control plane.

It is not a decision engine.

It does not claim absolute constancy.

## Canonical flow

OMNIA-CONSTANT must use the existing backbone:

constant/stability measurement
  -> OMNIA-CONSTANT adapter
  -> BoundaryCertificate-compatible artifact
  -> omnia-limit validate_certificate()
  -> OMNIA-VALIDATION process_boundary_step()
  -> ValidationEnvelope
  -> OMNIA-CONSTANT observation

## Public API

OMNIA-CONSTANT exposes:

adapt_constant_measurement_to_boundary_certificate(...)
run_constant_backbone_flow(...)
observe_constant_envelope(...)

## Contract rule

OMNIA-CONSTANT does not redefine BoundaryCertificate.

OMNIA-CONSTANT does not redefine ValidationEnvelope.

OMNIA-CONSTANT does not bypass omnia-limit.

OMNIA-CONSTANT does not bypass OMNIA-VALIDATION.

OMNIA-CONSTANT does not declare final absolute constancy.

## Constant/stability mapping

constant_break
  -> ast_deformation_index

constant_drift
  -> ast_deformation_index

stability_drift
  -> ast_deformation_index

residual_variance
  -> ast_deformation_index

variance
  -> ast_deformation_index

constant_score
  -> ast_deformation_index = 1.0 - constant_score

stability_score
  -> ast_deformation_index = 1.0 - stability_score

invariance_score
  -> ast_deformation_index = 1.0 - invariance_score

## Forbidden interpretation

OMNIA-CONSTANT must not emit final claims such as:

absolute constant
universal constant
proven constant
final constant
immutable truth
complete proof

Those are not backbone measurement outputs.

OMNIA-CONSTANT may report validated structural stability evidence.

## Boundary

stability evidence != absolute constancy
constant measurement != proof
adapter != validator
validator != control plane
control plane != decision
decision != measurement

OMNIA-CONSTANT stays in the Constant / Stability Producer-Adapter layer.
