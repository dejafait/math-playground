# Independent twist-five source review — preserved working record

The review is now completed in
[the canonical assessment](literature/2026-10-07-independent-twist-five-value.md).
The notes below preserve the unfinished checkpoint from before its final
source comparison; current routing is only in PROGRESS.md.

2026-10-07. Literature-only step; no value, nonvanishing assertion,
denominator specialization or mathematical script has been produced.
The main gap is rank equality at complex analytic order at least two.
The missing intermediate input is independent exact q for L028, potentially
feeding its Neron scale and L027's all-argument denominator certificate.

Primary passages inspected so far: Wuthrich, arXiv:1608.06423,
Proposition 1 with full torsion-reduction proof (pp. 3--4), Sections
2.2 and 3.1--3.3 (pp. 6--8), Lemmas 4 and 6 with their proofs,
and Section 4.1--4.2 equations (6)--(9) (p. 9).
Cesnavicius, arXiv:1703.02951, Theorem 1.2 = Theorem 2.13,
squarefree-conductor optimal-quotient case. Cremona corrected second
edition, Chapter 2 Proposition 2.11.1 and Section 2.11's twist identity;
Chapter 3 Section 3.7 equation (3.7.1) and the positive-discriminant
real-root case. DLMF Section 19.8(i), positive AGM definitions.

The primary Cremona allcurves table's only conductor-389 row is
`389 a 1 [0,1,1,-2,0] 2 1`. The ecdata documentation identifies the
coefficients, torsion column and optimal-label convention for this range.
Its rank column is irrelevant to this review. Theorem 5.2 in Cremona's
appendix to Agashe--Ribet--Stein also covers optimal curves at N<60000.
These are exact source inputs, not decimal rounding or BSD data.

The safer potential specialization works at level 389: apply
Wuthrich's unitary-cusp bound to the base curve, carry the established
positive-twist and total-period conventions, and enclose the needed
integrals independently of L030's scalar. The denominator and period
factors still have to be assembled in a later mathematical turn.
The source review is checking effective error control before approval.

Do not repeat ATTEMPTS/022--023 or line audits. Continue only with a
finite theorem-backed rational isolation test that accounts for every
period and truncation error; zero must remain a possible outcome.
