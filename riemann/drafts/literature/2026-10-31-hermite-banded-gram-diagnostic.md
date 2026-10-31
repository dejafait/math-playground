# Hermite banded Gram diagnostic: source comparison

TARGET: Test a parity-preserving bandwidth-two Hermite Gram certificate for the complete D(P_N) by matching its highest four even coefficients and checking the resulting necessary positive-semidefinite principal-block conditions for actual b_(2n), uniformly for integers N>=2.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact Hermite/banded-Gram and stronger univariate SOS/symmetry/chordal-PSD searches, followed primary statements and proofs below, and reused the named local actual-Hermite comparison, finite-audit assessment, cone stop and last audit history. No inspected source decides the actual-coefficient restricted test; no novelty inference follows from unsuccessful exact searches.
SOURCE_EVIDENCE: Gatermann–Parrilo arXiv:math/0211450v1, Lemma 2.1 and proof pp. 4–5, Definition 3.1/Theorem 3.3 and averaging proof pp. 7–9; Laurent author manuscript dated 2008-02-05, Lemmas 3.1/3.5/3.8 and relevant proofs pp. 22–25; Vandenberghe–Andersen DOI 10.1561/2400000006, section 9.1 pp. 337–338 including singular pivots, Theorem 9.2/proof pp. 340–341 and Theorem 10.1/proof pp. 356–357. Actual coefficients and finite Hermite tools reuse the ready L564/L565 assessments.
COMPARISON: General univariate nonnegativity/SOS and unrestricted PSD-Gram equivalence are known. Symmetry reduction does not supply fixed Hermite bandwidth. Chordal sparse-PSD decomposition and PSD completion concern different cones; PSD clique submatrices alone certify completion, not the zero-filled Gram matrix. No inspected theorem supplies the actual b-dependent leading equations or their feasibility, and L565's diagonal-CD stop does not decide them.
GAP: The highest-four-coefficient affine constraints and necessary PSD conditions for the proposed restricted Gram matrix remain uncomputed, including N=2 and uniform large cutoffs. Full coefficient matching, a signed Xi transfer margin and higher forms remain separate gaps.
REASON: Essential framework coverage now supports one bounded test of off-diagonal cancellation after the audited diagonal-CD stop; known framework results are to be cited, while the actual-coefficient feasibility question must be attempted separately.
SCOPE: Ready only for the exact TARGET: real symmetric PSD G_N on (H_0,...,H_(2N-1)), entries zero for opposite parity or index distance greater than two, actual b_(2n), integers N>=2, highest four even coefficients and resulting necessary principal-block tests. No full Gram construction, general feasibility assertion, Xi sign or new equations are established in this source-only turn.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because its changed off-diagonal mechanism lacked essential Gram/SOS and sparse-PSD coverage; this separate review fills that specific source gap and reuses the ready Hermite/coefficient coverage.

## Bounded mechanism and downstream use

The main gap is actual-Xi all-degree positivity. The intermediate
proposal concerns the first discriminant only. Keep the actual P_N
and D(P_N) of L564/L565 and use the vector
v=(H_0,...,H_(2N-1)). Seek an identity D(P_N)=v^T G_N v,
with a real symmetric positive-semidefinite matrix G_N whose entries
vanish unless the indices have the same parity and differ by at most
two. This is a proposed certificate, not an asserted representation.
Its free off-diagonal entries offer a concrete way to retain mixed
terms excluded by the failed nonnegative diagonal-CD certificate.

With the source coverage below, the next turn's bounded first test is to match
only the highest four even polynomial coefficients and test necessary
PSD conditions on the principal blocks they involve, using the actual
positive b sequence. Include N=2 separately wherever an index would
be negative. A contradiction valid for all sufficiently large N, or
an unbounded sequence of L564 cutoffs, would abandon this bandwidth
restriction. Feasible leading blocks would justify only a later,
separately reviewed construction of the remaining entries, not a
discriminant sign theorem. No such equations or conclusions have been
worked out in this proposal.

If a full PSD construction eventually existed, it could give a signed
truncation certificate. L564's absolute derivative errors would still
need a quantitative, zero-compatible signed transfer; no such margin
is supplied by this proposal. Multiplicities, all higher forms and
all-height RH remain independent unresolved requirements. Essential
local inputs are L564 and audited L565, with normalization inherited
from L018–L020. No cross-notebook input is proposed.

The source comparison below clears this exact test for the next turn.
Reuse the ready finite Hermite formulas and Romik coefficient coverage;
do not repeat inaccessible Turan-original retrievals or reopen the
audited diagonal cone. Nominate proof_attempt/creative for this changed
sign mechanism: the precise obstruction is the negative second
diagonal-CD weight, and the bounded test asks whether off-diagonal PSD
blocks can accommodate the complete leading mixed coefficients.
Standard Gram theory itself is known; this routing does not claim
originality for the framework or novelty for its unattempted application.

## Inspected primary inputs and exact scope

**Gram and symmetry framework.** Karin Gatermann and Pablo A. Parrilo,
*Symmetry groups, semidefinite programs, and sums of squares*,
[arXiv:math/0211450v1](https://arxiv.org/pdf/math/0211450v1),
28 November 2002 (published in J. Pure Appl. Algebra 192 (2004),
95–128, DOI 10.1016/j.jpaa.2003.12.011). The inspected version is v1;
page/theorem numbers here refer to it. Lemma 2.1, pp. 4–5, identifies
SOS with a PSD matrix in the affine space representing the polynomial
in monomials of degree at most half its degree. Its proof uses a real
factorization Q=B^T B and the converse coefficient expansion.
Definition 3.1/Theorem 3.3, pp. 7–9, require a finite group,
orthogonal linear action preserving the PSD cone, invariant feasible
set and invariant cost. Finite group averaging gives an invariant
feasible matrix of the same cost. Both proofs were read. The latter
proof's prose calls the affine space linear and PSD matrices positive
definite; its averaging argument uses affine convexity and the PSD
cone and needs no strict-feasibility premise. This supplies the
standard symmetry tool, not a bandwidth theorem.

**Univariate comparison.** Monique Laurent, *Sums of squares, moment
matrices and optimization over polynomials*,
[author manuscript](https://homepages.cwi.nl/~monique/files/moment-ima.pdf),
dated 5 February 2008, Lemmas 3.1, 3.5 and 3.8, pp. 22–25.
The [CWI repository](https://ir.cwi.nl/pub/13237/) lists a 2009
publication, but its 13237C.pdf resolves to the inspected 2008 text;
no November 2009 numbering is asserted. Lemma 3.1 bounds degrees of
square summands. Lemma 3.5 states that a real polynomial nonnegative
on all of R is a sum of two squares; its real-root/even-multiplicity,
complex-conjugate factorization and two-square product proof were
read, including the concluding identity. Lemma 3.8, for real p of
degree <=2d, equates SOS with coefficient-matching and a real PSD
Gram matrix indexed by all monomials of degree <=d; its full finite
factorization proof was read. These unrestricted results presuppose
the unknown sign when invoked through nonnegativity, and they do not
impose a fixed band in a prescribed Hermite basis.

**Sparse PSD versus completion.** Lieven Vandenberghe and Martin S.
Andersen, *Chordal Graphs and Semidefinite Optimization*, Foundations
and Trends in Optimization 1(4), 241–433 (volume dated 2014,
copyright 2015), [author PDF](https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf),
[DOI 10.1561/2400000006](https://doi.org/10.1561/2400000006).
For a chordal sparsity pattern E, Theorem 9.2, pp. 340–341, says a
real symmetric matrix with zeros outside E is PSD iff it is a sum
of embedded PSD clique matrices. The entire clique-factorization
proof was inspected. Section 9.1, pp. 337–338, includes singular
LDL^T pivots: a zero leading pivot requires its coupling vector to
vanish. Theorem 10.1 and proof, pp. 356–357, instead characterize
PSD-completable partial entries by their PSD clique submatrices.
Thus clique tests on given entries do not, by that theorem, establish
PSD of their zero-filled matrix. Do not divide by an assumed positive
pivot or replace the proposed matrix by a dense completion.

## Applicability boundary and remaining difference

The standard tools above are citation inputs, not results to reprove.
The next attempt must justify its finite basis change using the ready
physicists' Hermite formula and track the actual complete discriminant.
It must retain every free matrix entry that can affect the four
matched coefficients; dropping one requires a degree justification.
No source symmetry reduction licenses the additional bandwidth
restriction. No source coefficient-matching identity has been
specialized to P_N here. Checking this specialization and the source
hypotheses is part of the separately authorized mathematical attempt.

Necessary principal-block conditions can reject a certificate; passing
them is not a full PSD certificate, an exact polynomial identity, or a
nonnegative Xi discriminant. A freely adjustable block or an
underdetermined affine system must be reported honestly. If the four
coefficients give no discriminating restriction, record that limitation
and reassess rather than announcing feasibility of the complete form.
An obstruction only at a bounded cutoff does not settle the stated
unbounded-cutoff abandonment test. Include the direct N=2 boundary
case; do not invoke nonexistent negative Hermite indices.

Actual-coefficient normalization, positivity and finite Hermite
formulas reuse `2026-10-31-l565-leading-cd-weight-audit.md` and
`2026-10-31-actual-hermite-signed-cross-term-review.md`. The latter's
CD/Turan/O'Sullivan comparison already distinguishes adjacent-index
inequalities and different Jensen coefficients from the actual mixed
discriminant. Its inaccessible originals remain unused leads, not
essential blockers. L565 and its saved cone stop concern the unique
diagonal-CD coordinates only; the old parity/Pollaczek stops keep
their recorded scopes. No sibling proof or cross-notebook input was read.

## Bounded search record and decision

Queries executed on 2026-10-31 included:

- `sum of squares univariate polynomial Gram matrix orthogonal basis Hermite sparse banded`
- `sparse sum of squares Gram matrix chordal sparsity tridiagonal polynomial Hermite`
- `Laurent sums squares moment matrices optimization polynomials 2009 Theorem univariate Gram matrix pdf`
- `Vandenberghe Andersen chordal graphs semidefinite optimization 2015 Theorem 2.3 2.4 pdf`
- `Gatermann Parrilo symmetry groups semidefinite programs sums squares theorem 3.3 2004 pdf`
- `"Hermite" "Gram" "banded" "squares"`
- `"Hermite" "sum of squares" "Turan"`
- `"Hermite" "bandwidth" "Gram matrix" polynomial`
- `"Hermite" "tridiagonal" "sum of squares" polynomial`
- `"Romik" "Hermite" "Gram" discriminant`
- `"Hermite" "Laguerre inequality" "sum of squares"`
- `"Hermite" "banded" "sum-of-squares"`
- `"Hermite" "Gram matrix" "Riemann"`

Followed the author/repository PDFs above, retrieved their statements
before proof passages, and inspected the essential proof cases.
Searches also returned finite-group Fourier SOS, chordal-TSSOS,
polynomial-matrix decomposition, Hermite interpolation/lattices and
third-party RH portfolios. These are uninspected leads or irrelevant
search hits, not theorem evidence for this test. No matching
actual-coefficient bandwidth-two feasibility or obstruction was found
in the inspected sources. This bounded comparison supports EXPLORE,
not a claim of novelty, feasibility or impossibility.

Mathlib: coverage of the full restricted Hermite-Gram diagnostic was
not checked; no absence claim. Standard supporting matrix/polynomial
facts are distinct from a matching theorem for the actual b sequence.
No new lemma, mathematical script, DAG edge or argument change is
made. The source gate is cleared; exactly the saved TARGET is the
next mathematical action.
