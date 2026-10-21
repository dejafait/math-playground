# L411 critical audit checkpoint — step 128

Approved target: critically audit L411's uniform absolute clipped-square
physical/head transfer, including zero crossings, N-independent constants
and the H-first/N-second interpretation. Reuse the unchanged SPECIALIZE
assessment `literature/2026-10-14-clipped-square-transfer-critical-audit.md`.

Main gap: global mixed positivity; the nearby negative-Bcal clipped signed
mean is still unknown. Intermediate threshold: L411's exact absolute
C[(log H)^3+eta_N(log H)^4] error, with one constant/onset for all N>=1.
Its downstream use is to isolate the fixed-head signed clipping problem.
Continue if both product errors and uniform quantifiers pass; otherwise
preserve the failing term without assuming sign symmetry or extra moments.

Work saved before final documentation: read full L411; inspected L390's
complete response derivatives, physical minor identity, quartic conversion
and audit; L405's exact polarization/error and audit; L406's compatibility
bounds/audit; L409's head definitions. L389's precise Hardy identification
and cited pure fourth moments confirm the normalization used by L390.
Reuse step-124 discovery and primary statements, step-125 history and the
step-99 failed signed-clipping comparison. Existing edits are preserved.

Both exact product subtractions give the required pointwise bounds
CU^2/L and C eta_N U^2. Max contraction applies at zero; no clipped
function is differentiated. The complete response derivatives and the
opposite curvature signs in Delta and Bcal are retained. Only U^2 is
integrated, using the imported fixed-order fourth moments. Constants
come from the fixed physical family and zeta(5/2), with no head-dependent
onset. The sequential statement is a limsup comparison, not existence
or a sign of a clipped mean.

Completed: the full verification is saved in the separate step-128 audit
section of `lemmas/L411-uniform-absolute-clipped-square-transfer.md`.
The original threshold passes without a correction or new dependency.
The proposed half-carrier-turn scalar displacement test is left
REVIEW_REQUIRED for separate source review; no such calculation or
new source approval was performed here.
