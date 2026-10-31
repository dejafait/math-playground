# Global sparse-Gram dual obstruction: source comparison

TARGET: Assess a global dual-functional obstruction to parity-preserving bandwidth-two Hermite Gram representations of complete D(P_N) at an unbounded sequence of L564 cutoffs, requiring nonnegativity on every allowed one- or two-Hermite square.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact Hermite/dual/Gram/Romik searches and stronger binomial-square, factor-width, SDSOS and conic-separation searches completed; primary statements and relevant proof cases below inspected. Reused the parent Gram assessment, actual-Hermite comparison, L564/L566 statements and recorded L565/L566 stops. No inspected source decides the actual complete-polynomial obstruction; no novelty inference follows.
SOURCE_EVIDENCE: Vandenberghe–Andersen DOI 10.1561/2400000006 section 10.1 pp. 356–357, including its stated Rockafellar Theorem 9.1 criterion and duality proof, plus parent Theorem 9.2 coverage; MOSEK Modeling Cookbook 3.4.0 section 8.2 Lemma 8.3 and full proof, section 8.1 Lemma 8.2; Ahmadi–Majumdar arXiv:1706.02586v3 Definition 3.2, Theorems 3.6–3.9 and Lemma 3.8 proof pp. 9–14; Gouveia–Kovacec–Saee arXiv:1912.01371v2 Propositions 3.1–3.3 pp. 5–7; Papp–Yildiz arXiv:1712.01792v3 Propositions 1.1/6.1/6.2 and Appendix B pp. 3,17–18,30–31.
COMPARISON: Sparse-PSD clique decomposition, factor-width dual block tests and conic alternatives are known. Monomial SDSOS and complete-degree WSOS are not automatically this fixed Hermite-pair cone. L566's top-four test passes N>=3 and L565 concerns another cone. No inspected theorem supplies actual-coefficient separation at large cutoffs or its uniform negative pairing.
GAP: Specific image-closedness and dual-map specialization, certified complete-coefficient feasibility or separation, and any unbounded negative family remain unproved; sources now suffice to attempt them separately. Full Gram matching, signed Xi transfer and higher forms remain independent gaps.
REASON: New exact image-closedness and three-alternative separation coverage removes the essential source gap without claiming a Hermite specialization. A bounded complete-polynomial dual screen is justified before pursuing an unbounded family; no reproof of generic Gram or separation theory is needed.
SCOPE: Ready for the supplied global obstruction proposal and the exact covered finite screen below, using L564's actual coefficients and all allowed Hermite squares. Mathematical specialization and certification are deferred; no source asserts the desired separator. No coefficient-only leading diagnostic, automatic SOS-to-bandwidth implication, or Xi sign transfer is covered.
COVERED_TARGET: Test the complete bandwidth-two Hermite dual problem for actual L564 cutoffs N=64,128,256, certifying all allowed-square constraints and the full discriminant pairing as a screen for an unbounded separator family.
LITERATURE_REASON: The supplied REVIEW_REQUIRED target lacked essential complete-polynomial duality/closedness comparison; this separate source turn fills that gap and reuses ready Hermite and Gram assessments.

The main gap is actual-Xi all-degree positivity. The proposed
intermediate target is a global obstruction to the *restricted* full
Gram certificate, not a sign theorem for Xi. The desired test would
produce, for an explicitly specified unbounded sequence of cutoffs
N=ceil(16(T+1)^2), a real linear functional on polynomials of degree
at most 4N-2 that is nonnegative on every square of a real combination
of H_j and H_(j-2), j>=2, and on every individual H_j square, for
0<=j<=2N-1, yet is strictly negative on the complete D(P_N).
These are target conditions to assess, not a result derived here.

The review should first determine the precise sparse-SOS dual
statement and whether strict separation is available for this finite
coefficient map, retaining any closedness or limit qualifications.
It should compare exact terminology, stronger known results and
actual-coefficient applications before nominating one bounded
mathematical test. Reuse the parent's inspected sparse-PSD statements;
do not reprove generic Gram theory or infer novelty from search failure.

Downstream use: a verified global functional could reject the proposed
bandwidth restriction at relevant unbounded cutoffs and redirect sign
work. It would not refute RH or nonnegativity in the unrestricted SOS
cone. A finite N=2 separator is already implicit in L566 and is not
new evidence for this target. Abandon or materially refine the dual
mechanism if the assessed source theorem is inapplicable, or if the
bounded actual-coefficient test has no sign/control beyond that finite
exception. Do not turn absence of a found separator into feasibility.

Essential inputs: L564's actual coefficients and cutoff, L566's
audited leading-test limitation, and the cited sparse-PSD framework.
L565 is contrast only. Full matching, uniform actual-coefficient
estimates, any Xi signed transfer compatible with zeros and
multiplicities, and all higher forms remain unresolved. No
cross-notebook input. Mathlib coverage unknown/not checked.

The preceding proposal was not approved or attempted in the L566
audit. This separate literature turn completes its source comparison.
The following scope permits a mathematical attempt after continuation
approval; it does not report performing that attempt.

## Inspected theorem coverage and qualifications

**Sparse cone and closedness.** Reuse the full inspected
Theorem 9.2/proof and singular-pivot cases in
`2026-10-31-hermite-banded-gram-diagnostic.md`.
Vandenberghe–Andersen, *Chordal Graphs and Semidefinite Optimization*,
[author PDF](https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf),
volume 1(4) (2014), copyright 2015,
[DOI 10.1561/2400000006](https://doi.org/10.1561/2400000006),
section 10.1 pp. 356–357 was inspected. It states the sufficient
criterion from Rockafellar, *Convex Analysis* (1970), Theorem 9.1:
for a closed convex cone C in finite dimension and linear A,
ker(A) intersect C={0} implies A(C) closed. The source verifies this
for the matrix projection retaining all diagonals. It also proves
sparse-PSD/completion duality using the trace adjoint and bipolar
theorem. Theorem 10.1 then tests clique PSD for the COMPLETION cone.

This is adequate cited coverage for a future nullspace check of the
polynomial coefficient map; that check has not been performed here.
Matrix-projection closedness alone is not polynomial-image closedness.
The next attempt must specify its real finite-dimensional spaces,
linear map, closed cone and nullspace hypothesis before claiming
completeness of a strict-separator alternative. Direct verification
of an explicit negative functional does not need that completeness
claim. Neither strict primal feasibility nor a PSD completion may be
substituted for the requested zero-filled sparse Gram certificate.

**Conic alternatives.** [MOSEK Modeling Cookbook 3.4.0,
section 8.2](https://docs.mosek.com/modeling-cookbook/duality.html#infeasibility-in-conic-optimization),
Lemma 8.3 and its full proof were read, together with PSD
self-duality in section 8.1, Lemma 8.2. For Ax=b, x in a convex
cone K, its alternatives are feasibility; infeasibility with b in
the closure of A(K); or y with -A^T y in K* and b^T y>0.
The proof explicitly separates a point outside the CLOSED image
closure and rules out coexistence with either feasibility or its
limit. Thus infeasibility by itself does not always give a strict
certificate. No Slater or optimizer-attainment claim is needed for
a directly checked certificate. The sign convention must be translated
when writing a polynomial functional nonnegative on the cone and
negative on the proposed polynomial. This is a standard import;
no original separation theorem or Hermite consequence is proved here.

**Binomial-square overlap.** Ahmadi–Majumdar,
*DSOS and SDSOS Optimization: More Tractable Alternatives to Sum of
Squares and Semidefinite Optimization*,
[arXiv:1706.02586v3](https://arxiv.org/pdf/1706.02586v3),
29 August 2018, Definition 3.2 and Theorem 3.6 use monomial
binomial squares and scaled-diagonally-dominant Gram matrices.
Theorem 3.7 identifies factor width two; Lemma 3.8 decomposes it
into embedded PSD two-by-two blocks. Its complete forward rank-one
and reverse block-factorization proof was read. Theorem 3.9/proof
encodes coefficient equality and each two-by-two PSD block by SOCP.
Pages are 9,12–14 of this version. This establishes terminology and
a stronger all-pairs matrix framework; it does not authorize a
fixed Hermite basis or a fixed subset of edges. An arbitrary basis
change preserves unrestricted PSD Gram equivalence, but cannot
silently preserve this additional restriction. No monomial SDSOS
impossibility or hierarchy-convergence claim is transferred.

Gouveia–Kovacec–Saee, *On sums of squares of k-nomials*,
[arXiv:1912.01371v2](https://arxiv.org/pdf/1912.01371v2),
12 January 2021, Propositions 3.1–3.2 and their rank-one/monomial
factorization arguments, pp. 5–6, were read. Proposition 3.3, p. 7,
states the dual factor-width cone as symmetric matrices with all
k-by-k principal blocks PSD; it refers its proof to an earlier
source, which was not independently retrieved. This is matrix-level
comparison, not a theorem about Romik's polynomial family. All
pairs and all monomial k-nomials differ from the proposed prescribed
Hermite pairs. The existing chordal theorem remains the cited route
for justifying that particular restriction during research.

**Broader SOS dual maps.** Papp–Yildiz, *Sum-of-squares optimization
without semidefinite programming*,
[arXiv:1712.01792v3](https://arxiv.org/pdf/1712.01792v3),
20 December 2018, Proposition 1.1 (p. 3), section 6 Propositions
6.1–6.2 (pp. 17–18), and Appendix B's full Proposition 6.1 proof
(pp. 30–31) were read. The Gram-adjoint/dual-PSD descriptions use
bases of complete degree spaces. Properness of the WSOS cone requires
the stated absence of a nonzero zero-sum of weighted SOS terms;
the closedness part cites Rockafellar Corollary 9.1.3. These statements
give stronger general terminology but are not automatic imports for
the prescribed two-Hermite subspaces. Do not infer closedness simply
from linear-image notation. No numerical algorithm or accuracy claim
from that paper is used as a certificate here.

## Exact comparison with local inputs

L564 fixes the actual b_(2n), degree 2N and cutoff, with an absolute
derivative-tail bound. L566 fixes D(f)=f'^2-f f'', the vector through
H_(2N-1), and precisely the parity/band restriction. Its audited
positive leading-block construction for N>=3 prevents repeating the
top-four test. Its actual N=2 negative value is below every L564
cutoff. The two recorded attempt files and the last L566 audit
history were inspected; their stops retain exactly those scopes.
L565's diagonal-CD stop remains a contrast, not a premise.

The ready `2026-10-31-actual-hermite-signed-cross-term-review.md`
already compares CD/Turan identities, Romik's actual coefficients
and O'Sullivan's different Hermite/Jensen families. Reuse it; no
new expansion, asymptotic or hyperbolicity import is proposed.
None of these inspected results decides the complete restricted
Gram identity or supplies the requested functional's negative value.
Known convex duality is not a new mechanism theorem, and no
originality claim is made for its proposed actual-coefficient use.

## Bounded mathematical continuation specification

The single covered screen is N=64,128,256. Derive the exact finite
dual coefficient map using the cited framework; justify the
particular sparsity and any image-closedness assertion. Search using
the COMPLETE D(P_N), and require nonnegativity on every prescribed
one- or two-Hermite square, not only coefficientwise positivity or
selected blocks. A candidate may be located numerically, but every
claimed certificate must verify all constraints and the full signed
pairing with rigorous coefficient enclosures, including all theta
summands and integral tails. A solver status or preview is not proof.
No new solver or quadrature theorem is asserted in this source turn.

Continue toward an unbounded family only if certified complete
negative pairings persist and their functional structure suggests
an independently checkable uniform estimate. Three finite tests do
not themselves satisfy the unbounded-cutoff target. If no such
structure appears, park or materially refine this particular dual
search; do not extend the old leading-coefficient diagnostic.
An unsuccessful separator search does not establish full feasibility.
Even a proved unbounded obstruction would reject this global Gram
restriction only; interval signs, zero-compatible signed Xi transfer,
multiplicities and all higher forms remain unresolved.

## Search and access record

Queries executed on 2026-10-31 included:

- `sum of squares cone linear image closed sparse polynomial Gram dual separation`
- `"Hermite" "Laguerre" "sparse" "sum of squares"`
- `"Xi" "Hermite" "Gram" polynomial positivity`
- `"sum of squares" "subspaces" "closed" cone linear`
- `"sum of squares" "closed" "Papp" "Yildiz"`
- `"linear image" "closed" "kernel" "cone" Rockafellar 9.1.3`
- `"Hermite" "dual" "sum of squares" polynomial`
- `"Romik" "Hermite" "semidefinite"`
- `"Hermite" "banded" "dual" polynomial Gram`
- `"sum of squares" "subspaces" "separation" closed cone`
- `"DSOS" "SDSOS" "dual" "binomial" squares Ahmadi Majumdar`
- `"sum of binomial squares" "Hermite"`
- `"Romik" "discriminant" "Hermite"`
- `"Hermite" "sparse" "Gram" "separation"`
- `"On sums of squares of k-nomials" arxiv`

Followed the primary PDFs/documents above. Other results included
third-party RH portfolios, unrelated Hermite interpolation and
moment algorithms; these were not read as theorem evidence.
Boyd's Stanford PDF and the NSF Papp–Yildiz mirror timed out;
the arXiv manuscript and accessible conic-alternative source supply
the necessary coverage. The original Rockafellar proof and the
earlier reference for Proposition 3.3 remain unread; the exact
sufficient criterion is explicitly reproduced in the inspected
Vandenberghe–Andersen section, and the separator proof is accessible.
These are source provenance limits, not claims of independent audits
of those originals or persistent blockers to this direct test.

Mathlib: full restricted-Hermite dual/separation coverage not checked;
unknown availability is not absence. This literature turn changes
source coverage only: no lemma, mathematical script, DAG edge or
PROOF assembly change. The ready continuation receives the separate
supervisor approval required for a newly changed assessment.
