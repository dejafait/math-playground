# 2026-10-04 — Coordinate-Haar contraction and forest dependence test

Reused the saved SPECIALIZE assessment for the unchanged combined-response
TARGET. This is one mathematical step, with no further literature work.
Preserved existing work, the two earlier inconclusive direct-expansion
attempts, and all stopped branches. Edited only the active notebook.

[L018](../lemmas/L018-coordinate-haar-contraction-and-forest-change.md)
gives the exact three-color Wick trace for L011's M2 term, its justified
free-gauge-invariant lift, and its change-of-forest formula. An exact
unit-field test at N=24 changes the quadratic density by 11/2. Equality
of the original nonlinear covariance forces any contraction change to
be canceled by the sum of all the other terms in the full coefficient.
This proves neither a cancellation within a particular action term nor
a nonzero contraction difference for the original fixed probes.

The [working record](../drafts/2026-10-04-coordinate-haar-contraction.md)
was saved before computational work. The new matrix-free operators agree
with the independent dense N=4 one-site diagnostic within 5.2e-15;
full/slice contractions agree within 3e-11. That sample uses different
weights from the original displacement. The admitted N=24 original-probe
test retains all 1,168,032 one-form entries per color. Its 64 shared
Gaussian samples give paired triplet/shear differences (4776.32,16814.47)
with sample standard errors (315.38,256.75), as recorded in the
[output](../scripts/combined-ward-response/haar-original-results.json).
These are numerical diagnostics without a proven confidence guarantee,
exact nonvanishing conclusion or ultraviolet asymptotic.

Outcome: **NEGATIVE / RESEARCH / REPRODUCTION**, an informative local
obstruction to interpreting the isolated coordinate-density insertion
as forest independent, together with evaluated contraction evidence.
The [stopped interpretation](../ATTEMPTS/009-isolated-coordinate-haar-cutoff-coefficient.md)
does not stop the complete combined-response mechanism. No result beyond
the checked literature or ultraviolet advance is claimed. The full
Gamma, its logarithm, physical-boundary subtraction, finite matching and
the reflected-error bound <= c_box/2 remain missing, as do continuum
fields, full reflection positivity, infrared control and finite positive
mass. STATUS remains IN_PROGRESS; no candidate solution appears.

The unchanged exact TARGET and ready assessment are retained. Continue
with combined density/action contractions and all insertion/flow terms,
using fixed-mesh forest independence as a discriminating test before
interpreting cutoff growth. This needs no new source review. No
inconclusive mathematical exploration turn is spent; prior route
failures and counts remain recorded, and no external state is edited.

Validation: both recorded computational commands passed, as did the
integer density-function test. The documentation checker with
--problem yang-mills passes with 18 nodes and 35 unique edges; whitespace,
unique step fields and exact unchanged ready TARGET matching pass.
PROGRESS.md has 14 lines and PROOF.md 100. Mathematical review checked
the three-color factor 2, sign and ordering of the noncommuting trace,
the x=a A covariance scaling, full-flow normalization, justified density
lift, and the distinction between exact functional dependence and sampled
contraction differences. The new DAG row has exactly the quotient-law,
coefficient-expansion and compensated-free-comparison inputs actually
used in its proof. No assessment was changed and no interacting bound
was inferred from the diagnostics.
