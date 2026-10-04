# Mixed seventh-power exceptional-field finite-certificate assessment

TARGET: Critically audit Chocian's Section 6.2 finite certificate at q=29 by reproducing the four genus-two Frobenius trace polynomials and all 24 resultants modulo 7, without assuming completeness of the modular-packet list.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-signature discovery and primary reference comparison in 2026-10-04-mixed-cube-fifth-seventh.md. The unchanged arXiv v1 Section 6.2 supplies every input to this finite subtarget; no additional search or inaccessible global-descent source is required for its arithmetic.
SOURCE_EVIDENCE: Chocian, arXiv:2609.26996v1 (22 September 2026), Section 6.2, equations (34), (38)–(40), including the point-count formula and the six-factor annihilating family, read at https://arxiv.org/html/2609.26996v1 ; PVT arXiv:2512.17845v1, Theorem 7.8, read as supporting context, not as coverage of the six-factor list.
COMPARISON: The printed table and resultant matrix are a full match for the intended finite arithmetic. Reproduction is justified as a bounded correctness check of a load-bearing certificate in an unverified fixed-signature candidate. The proposed test supplies neither a new global exclusion nor evidence beyond this checked source claim.
GAP: Independently count the complete smooth projective curves over F_29 and F_(29^2), reconstruct their two-trace polynomials, and verify all pairwise resultants modulo 7. Even a pass leaves completeness of the modular and character list, the reduction to four parameters, the pure-field argument and the global descent unverified.
REASON: This is essential verification of an unverified computational claim, an allowed SPECIALIZE exception to citation-only reuse. The displayed finite calculation is independently testable while the unread original descent and the larger certificate packages remain parked.
SCOPE: One bounded mathematical audit of the four explicitly printed curves, their Frobenius trace polynomials and the 24 resultant entries. Use REPRODUCTION classification. No assumption that every Beal solution yields one of these parameters, or that every relevant newform/character is represented, is approved. The entire source proof is not preapproved for import.
COVERED_TARGET: Critically audit Chocian's Section 6.2 finite certificate at q=29 by reproducing the four genus-two Frobenius trace polynomials and all 24 resultants modulo 7, without assuming completeness of the modular-packet list.

## Relevance and continue/stop test

The main gap is uniform residual-signature emptiness. The parent assessment found an unverified source claim for (3,5,7); its exceptional-field elimination depends on this finite comparison. A mismatch would change the decision to pursue the printed certificate. A pass would check one necessary component of that argument, with the global coverage gap expressly retained. Neither outcome alone establishes or refutes the original signature claim.

Reproduction rather than a new derivation is appropriate because the exact values are already claimed by the closest source. The notebook has not checked this certificate previously. Attempts 001–004 do not duplicate it: the proposed calculation concerns a named candidate's constrained global interface, not an unrestricted local sieve or a primitive-divisor multiplicity inference. No calculation was performed in preparing this assessment.

## Source data, not verified notebook results

Source: Peter Chocian, *The Primitive Generalized Fermat Equation x^3+y^5=z^7: A computer-assisted proof*, [arXiv:2609.26996v1, Section 6.2](https://arxiv.org/html/2609.26996v1). The following inputs and expected outputs are transcribed for an independent future audit, with their original variable qualifications.

At q=29 the source lists eta=10,14,24,28, corresponding respectively to t0=14,10,25,15 under equation (34). For each t0 the curve is

\[
C_{t_0}:\quad y^2=5x^6-12x^5+10t_0x^3+t_0^2.
\]

Let N1 and N2 be its complete projective point counts over F_29 and F_(29^2). Section 6.2 defines

\[
A=30-N1,\qquad B=\frac{A^2-(842-N2)}2,
\]

and prints the degree-four Frobenius polynomial X^4-A X^3+B X^2-29 A X+29^2 and the two-trace polynomial T^2-A T+(B-58). Smoothness, the projective points at infinity, and arithmetic over the quadratic extension must be handled explicitly by the audit; an affine-only count does not meet its predicate.

Equation (38) claims the following reductions modulo 7:

| eta | t0 | Two-trace polynomial |
| --- | --- | --- |
| 10 | 14 | T^2+6T+6 |
| 14 | 10 | T^2+6T+4 |
| 24 | 25 | T^2+4 |
| 28 | 15 | T^2+2T+3 |

Equation (39) lists the comparison family in this order:

\[
T,\quad T^2,\quad T^2+5T+2,\quad T^2+3T+4,\quad T-2,\quad T-5.
\]

The source calls this an annihilating family; it does not claim its factors are squarefree or irreducible. Preserve multiplicities when comparing the printed resultant matrix. Equation (40) claims, in the displayed row and column orders,

\[
\begin{pmatrix}
6&1&5&1&1&5\\
4&2&3&1&6&3\\
4&2&6&1&1&1\\
3&2&6&2&4&3
\end{pmatrix}\pmod7.
\]

The future pass criterion is agreement of every reconstructed trace polynomial and all 24 resultant entries, together with the required nonzero test. This is a finite arithmetic certificate relative to the displayed comparison family. Its success cannot certify that the family exhausts all relevant representations.

## Imported context and remaining boundaries

[Pacetti–Villagra Torcomian, arXiv:2512.17845v1](https://arxiv.org/html/2512.17845v1), Theorem 7.8, is the cited supporting modular statement under residual irreducibility; it does not contain equation (39)'s exhaustive family. Chocian's Section 6.2 supplies an additional Brandt-module/filter argument and a separate reducible-character argument. Their truth is outside this audit, as are the four-parameter reduction, the six pure fields and the original local lists. No small-exponent irreducibility is inferred from PVT's C(2)=13 criterion.

No essential input for the stated finite test is missing: the four curves, field sizes, expected polynomials, comparison factors and expected resultant matrix are all printed in the inspected source. The original Dahmen–Siksek paper, companion package, imported software logs and original modular programs are not needed to test these explicit arithmetic assertions, and remain uninspected. A later change of target to their completeness would require separate coverage. Source corrections or inconsistent count data would also require reassessment.

## Mathlib

Coverage of the full candidate exclusion, the stated finite certificate and supporting finite-field/Frobenius results: **not checked**. The source equations are precise mathematical references; no matching Mathlib theorem or formal verification is claimed. This assessment authorizes a research audit next turn and does not report any of its arithmetic as verified.
