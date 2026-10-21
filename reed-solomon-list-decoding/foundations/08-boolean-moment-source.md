# Boolean moments for finite independence systems — source record

## Hypotheses

Let Delta be a finite simplicial complex on V containing every singleton.
Write I_Delta for its nonface-monomial ideal plus the Boolean equations
x_a^2-x_a, and Delta_<=r for its faces of size at most r. Let r>=1.

## Conclusion

The cited source describes TH_r(I_Delta) by the existence of moments
y_S, S in Delta_<=2r, with y_empty=1 and

\[
 (y_{I\cup J})_{I,J\in\Delta_{\le r}}\succeq0,
 \qquad y_S=0\text{ for nonfaces},
\]

projected onto singleton coordinates. This is a relaxation of the convex
hull of face indicators, not a representing-measure theorem at r=2.

## Proof

Import João Gouveia, Pablo A. Parrilo and Rekha R. Thomas,
*Theta Bodies for Polynomial Ideals*, SIAM J. Optim. 20(4) (2010),
2097–2118, DOI 10.1137/090746525. Inspected version:
[arXiv:0809.3480v3](https://arxiv.org/pdf/0809.3480v3),
Remark 3.6, printed p. 16; Theorem 2.14 and proof, pp. 9–10;
Corollary 2.15, p. 10; Proposition 2.18 and proof, pp. 10–11.
The basis must respect degree. The Boolean proposition removes the
closure qualification; it does not assert exactness at order two.
The v3 header records 3 December 2009; its generated title-page date is
28 May 2018. Numbering here is v3 numbering, not the earlier June draft.
No local reproof is made.

For the graph-only comparison, import Monique Laurent,
*A Comparison of the Sherali–Adams, Lovász–Schrijver, and Lasserre
Relaxations for 0–1 Programming*,
[CWI report PNA-R0108, 31 July 2001](https://ir.cwi.nl/pub/4319/04319D.pdf),
Section 6.1, Lemma 13 and its complete proof, printed pp. 13–14.
For a finite graph, t>=1 and moments through size 2t+2, PSD of
M_(t+1) together with pair-edge zeros is equivalent to zero moments on
every nonstable set in that range, and to the stated graph localizing
constraints. Its proof retains zero diagonal rows and treats both small
and large nonstable sets. Here t=1 is the degree-four graph case.
This theorem is not applied to cubic hyperedges.

For comparison only, Sven Polak,
*Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1, 15 March 2017](https://arxiv.org/pdf/1703.05171v1),
Section 1.1, equations (1)–(3), Proposition 1.1 and proof, p. 2;
Section 1.3, p. 4; Section 3, p. 5. These were inspected.
The A_4 program requires all M_(4,D), including nonempty D and scalar
nonnegativity for triples and quadruples. The saved diagnostic specifies
only its unconditioned degree-four moment matrix. Proposition 1.1's
display ends with A(n,d), but its proof establishes A(n,d,w); that
display is not imported as written. No numerical table or symmetry
reduction from this paper is used.

## Mathlib

Full matching finite-independence-system moment hierarchy: not checked.
Supporting PSD, Boolean polynomial and finite-set coverage: not checked.
Unknown availability is not evidence of absence.
