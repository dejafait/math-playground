# Degree-one cyclotomic determinant model — completed calculation

Approved target: the exact dimension-two marked-Kummer model test in
the saved [assessment](literature/2026-10-03-cyclotomic-kato-derivative.md).
This is a mathematical specialization, with the prior assessment reused.

The full calculation and proof are now in
[L013](../lemmas/L013-cyclotomic-determinant-descent-with-sha-direction.md).
The signed inverse-parameter duality, local adjoint boundary and
chain homotopy, degree-one determinant descent with its dual H^2
factor, and scalar order-two computation all pass the
[exact polynomial check](../scripts/cyclotomic-determinant/check_model.py).

The resulting model has marked rational/Sha dimensions (1,1). Its
leading vector is rational, but its determinant preimage has a nonzero
mixed component. The required two rational directions are still missing.
The symmetric local Tate form and explicit local triangles are essential
compatibility checks; the model is not an arithmetic realization.

This reproduces the known determinant formalism in a concrete model.
The negative result stops the proposed formal inference and isolates
the arithmetic exclusion it would need. Actual Euler-system relations
at auxiliary primes are outside this completed test's coverage. They
are only a proposed follow-up, with their separate assessment marked
REVIEW_REQUIRED; no new source review is performed in this step.
