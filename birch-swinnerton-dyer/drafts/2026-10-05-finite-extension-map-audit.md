# L020 map audit — saved working record

Approved target: audit the non-Galois transfer application, finite Kummer
diagram and equality boundary in the saved SPECIALIZE assessment
`literature/2026-10-04-finite-extension-certificate-audit.md`.
Essential mathematical input: L018; audited application: L020.

The finite-index subgroup need not be normal. A continuous cocycle
descends after choosing an open normal subgroup contained in G_F,
annihilating the cocycle and fixing its finitely many values; finite
transfer then inflates to continuous cohomology. Check the composite
on H^1(Q,E), rather than its reverse over F.

Working equality test: with k = 2-r > 0 and a fixed degree valuation a,
use B_Q = B_F = (Q_p/Z_p)^k, restriction [p^a] and corestriction identity.
At depth n, Q's exact row has middle R_n^r direct-sum R_n^k and
F's formal row has middle R_n^2 direct-sum R_n^k with point kernel R_n^2.
Proposed finite maps are (u,v) -> ((u,v),p^a v) and
((z_u,z_v),w) -> (p^a z_u,w). Verify both rows, quotient maps and
downward coefficients before placing the complete test in L020.
At n=a, both standard basis columns enter the formal point kernel;
for n>a a quotient column does not. No arithmetic realization is proposed.

Unresolved: actual global points over a common field with n>a, production
of the two-prime premise from analytic order two, analytic comparison
and higher ranks. This is unfinished reasoning, not a completed result.

## Completion

The canonical proof and full equality-boundary test are now in
[L020](../lemmas/L020-finite-extension-global-kummer-certificate.md).
The essential direct input remains L018; the DAG has no new edge.
The non-normal profinite transfer application and both coefficient
directions pass the audit. No error or hidden finite-Sha assumption
was found. The completed formal test verifies the proposed rows and
maps at every depth. It is NEGATIVE for weakening the strict threshold
on these tested data, classified REPRODUCTION. No arithmetic field,
curve or torsor realization is asserted.

The unresolved assumptions above remain unresolved. Do not redo the
boundary calculation or the parked determinant/height imports. The
next checkpoint selects a separate, uncovered geometric source
comparison; this record approves no new mathematical target.
