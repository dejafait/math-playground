# 2026-10-06 — Exact Fourier quadrature input

STEP_ID: YM-20261006-051-exact-fourier-quadrature

RESEARCH / REPRODUCTION / ADVANCE; actual task calculation. Reused
the unchanged SPECIALIZE combined-response assessment. The focused input
test in [L036](../lemmas/L036-exact-fourier-quadrature-bound.md) proves
uniform exact-rule errors below 7e-14 and 2.1e-13, against the requested
6e-12 and 9e-12 for h=0,1 and |n|<=224. A degree-200 auxiliary
polynomial and outward integer Taylor checks cover all 565 cells, including
both endpoint collars; the separate audit checks every saved cell and
complete coverage. Certificates and reproduction commands are canonical
in L036. The first two runs stopped on rational serialization/type errors;
both were repaired, and the completed calculation and audit have no failures.

This is a local input advance using standard approximation methods, not
a discovery beyond the checked literature or a response/sign enclosure.
It certifies only exact quadrature, leaving stored binary64 coefficients,
L035's sensitivity enclosure, inverse weights and tensor arithmetic open.
ATTEMPTS/011–016 and unfinished work are preserved. Continue within the
unchanged response target by bounding stored-transform error against
5.93e-12 and 8.79e-12, so L036 plus the triangle inequality supplies
the total normalized 1e-12 coefficient hypothesis. Inputs: L008, L034–L036,
the Integrals implementation and the exact-rule certificate. Other action
classes/pairings, nonlinear jets, L019 compensation, full logarithm,
matching and the interacting reflected error <=c_box/2 remain unresolved.
No new assessment is self-approved. The existing response assessment is
unchanged and reused for this numerical specialization.
