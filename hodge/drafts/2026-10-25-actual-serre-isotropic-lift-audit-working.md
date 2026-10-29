# Step 549 — Actual Serre-isotropic lift critical audit

Invocation-start SPECIALIZE coverage:
`literature/2026-10-25-actual-serre-isotropic-lift-critical-audit.md`.
Main gap: primitive Hodge realization and existence of the hypothetical F.
Exact intermediate target: audit L165's actual Serre restriction,
trace-adjoint orthogonal splitting and pointwise isotropic lifts.
Downstream use: preserve or correct the scalar-isotropy-only stopping
decision before testing any actual obstruction component.
Test: check the global adjoint identity, tensor sign, nondegeneracy,
dimension and lift; retain the conclusion only if all survive. A common
scalar or sign change alone cannot obstruct null-cone surjectivity.

Existing notebook changes were inspected by scoped git status and are
preserved. Read L165 in full, L116's hypotheses, retraction, cohomology
and prior audit, L071's hypotheses/conclusion, L109's actual adjoint
and normalization, and L108's defining ordered trace form. Reused the
supplied primary-source assessment. ATTEMPTS/068,/092,/093 distinguish
the parked counting, point-bracket and scalar-only tests. No fresh
source search, numerical script or cross-notebook input is needed.

Checks so far: the shifted adjoint has the stated target M^vee[-1];
fj=b[-1] is an equality of sheaf maps after shifting, not a generic
agreement of arbitrary derived maps. L109/L116 fix the ordered flat-map
convention. Base-first totalization moves the relative degree-one input
past one base degree and gives the minus sign. The remaining check is
to spell out that the mixed pairing factors through f globally, including
Z, so its kernel is precisely ker R. The linear lift and dimension
arguments must then be checked with unknown t and possibly empty Z.

Continuation planning only: an actual complementary quadratic-obstruction
component R[j_1u,j_1v] is not evaluated by L164 or L165. Its vanishing is
not implied by scalar isotropy or additive splitting. Any such new target
requires a separate literature assessment; no computation or approval of
that target belongs to this audit.

Completed: the mixed derived pairing factors through the actual f before
global sections; the resulting base-first evaluation has the same minus
sign as the restriction. Full verification, including all edge cases,
is in L165's separate step 549 audit. It finds no substantive correction
or stronger conclusion (EXPLORATION / REPRODUCTION). No new dependency
is needed. The prospective complementary-component assessment remains
REVIEW_REQUIRED; no result for it was derived in this turn.
