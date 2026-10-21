# 2026-10-11 — Approved finite-torsion specialization, working note

Approved target: specialize Bisatt–Dokchitser Theorem 2.2 at m=210
to construct a nonsingular E'/Q(zeta_60) with full H-rational
30-torsion and H(E'_H[7])=N as embedded fields.

The main gap is still the original finite B>=A inference. This target
could supply a global-curve replacement for L042's local packet;
it does not supply global initial data or original input/action bridges.
Use the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-11-finite-torsion-preserving-global-approximation.md`.
Scoped duplicate/failure checks preserve ATTEMPTS/022,025,026,027.

Proof plan: complete the square in Milne's standard Q_3 Tate equation,
giving a monic integral squarefree cubic. Apply the inspected theorem
at m=210, approximate its nonleading coefficients in Z_3 by integers
and keep the leading coefficient exactly 1. Identify each pointed
genus-one curve with its Jacobian over Q_3, restrict the full module
isomorphism to G_H and recover the 30- and 7-torsion submodules.
Pointwise kernels, rather than degrees or chosen points, must give N.

Unfinished obligations: verify the exact Tate coefficients and cubic
change of variables, nonzero discriminant/squarefreeness, theorem's
same-degree congruence hypothesis, pointed Jacobian identification,
and equality of the embedded full-coordinate fields.
Continue only if both torsion conclusions follow; failed model or
kernel hypotheses stop the mechanism. No effective precision or
explicit coefficient tuple is promised by the covered existential target.

Completed attempt: all listed obligations are proved in canonical
L044, `lemmas/L044-global-curve-preserving-local-finite-torsion.md`.
The result is an existential known-theorem specialization awaiting
separate critical audit. It passes both local torsion tests by the
full G_H pointwise kernels; it supplies no global rational 30-torsion
or original finite B>=A conclusion. No mathematical script was needed.
