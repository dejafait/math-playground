# Global degree-three support moments — primary source input

## Hypotheses

Fix nonnegative integers n,d,w and the universe V of binary words of
length n and weight w. Let C_r be all subsets of V of cardinality at
most r. The moment order r is unrelated to RS message dimension or
interleaving width. The following theorem is used at r=3, with
n=1024,d=10,w=68. Moment coordinates are real.

## Conclusion

Import the constant-weight moment program A_r: maximize
sum_(S in V) x({S}), with x(empty)=1, nonnegative moments through size r,
zeros on families violating minimum distance d, and all union matrices

\[
 M_{r,D}(x)_{I,J}=x(I\cup J),\qquad
 I,J\supseteq D,\quad |D|+2|I\setminus D|\le r,
 \quad |D|+2|J\setminus D|\le r
\]

positive semidefinite. Its value upper-bounds A(n,d,w). For r=3 the
empty-conditioned indices are empty and singletons; a singleton anchor
has indices that anchor and its unions with one support. Larger anchors
give scalar matrices. Singular PSD matrices are allowed.

This is the ordinary known theorem. A version adding L020 nonfaces,
any retained-principal-matrix certificate and the proposed trial's
normalization are specializations to verify in research, not results
established by this source record. No representing measure is asserted.

## Proof

Precise import: Sven C. Polak, *Semidefinite Programming Bounds for
Constant-Weight Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800; inspected
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 equations (1)–(3), Proposition 1.1 and its complete
indicator proof, printed p. 2. The display ends with A(n,d), but the
proof establishes A(n,d,w); retain the latter. Section 1.2, p. 3,
requires constraint-preserving group actions for averaging. Its
symmetric-group implementation is not imported for labeled triples.

Cross-check: Andries E. Brouwer and Sven C. Polak, *Uniqueness of codes
using semidefinite programming*,
[arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1),
7 September 2017, Section 2 equation (1), printed p. 2, explicitly
uses nonnegative moments; equations (2)–(3), pp. 2–3, give primal and
dual coefficient identities. Their ordinary orbit reduction cannot be
assumed for extra nonfaces. No uniqueness conclusion is used.

Supporting comparison: Alexander Schrijver, *New code upper bounds
from the Terwilliger algebra and semidefinite programming*, IEEE
Trans. Inform. Theory 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748;
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Section III.B (60)–(65), printed p. 7, freshly inspected. Both
included/excluded-anchor constructions in (60) are PSD outer-product
averages. The printed complement prefactor in (61) is not used;
the existing qualifications are retained in
[foundations/04](04-constant-weight-triple-sdp-source.md).

No hierarchy, block diagonalization or spectral theorem is reproved.
Pair spectral and Schur inputs are separately recorded in
[foundations/09](09-global-pair-johnson-source.md).

## Mathlib

Full matching global degree-three constant-weight hierarchy or labeled
RS certificate: not checked. Supporting finite-set and PSD coverage:
not checked. Unknown availability is not evidence of absence.
