# Pole-at-zero sum/product witnesses: completed source assessment

TARGET: Review pole-at-zero received words y_{b,d}(x)=x^65-bx^64+d/x on H for a 66-agreement sum-and-product subset-fiber construction, comparing its hypotheses and attainable-list counts with known rational-word RS results.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Reed Solomon rational received word prescribed sum product subsets deep holes 1/x; finite field prescribed leading coefficients constant coefficient subset sum product Reed Solomon; Gao Kuttner Wang prescribed leading ending coefficients linear factors; rational deep holes Cheng Wan; and Computing Error Distance of Reed-Solomon Codes Zhu Wan pdf. Compared local L013-L018 and the existing two-leading-coefficient assessment.
SOURCE_EVIDENCE: Read Gao arXiv:2105.12845v3 Section 2 Proposition 1 and Theorem 1 with factorization proof; Gao-Kuttner-Wang arXiv:2109.02000v1 Section 2 Type I, Proposition 1 and its inverse-recursion proof, and Theorem 1; Wu-Hong arXiv:1108.3524 Theorem 1.2 and Section 3 conclusion; Keti-Wan-Zhu author-hosted errordistance.pdf Theorem 9, pp. 6 and 11-14, including denominator assumptions and the r<d/r=d counting cases.
COMPARISON: Prescribed leading/ending coefficient classes and rational-word root-factor reductions are known; inspected rational distance theorems do not cover the proposed zero-pole denominator directly, nor certify the required subgroup list size. Approve only the elementary applicability and finite-threshold specialization below.
GAP: Verify the pole-at-zero scalar subset dictionary, strict degree cancellation, signs, distinct messages, ambient-extension candidates and simultaneous interleaving; then test the attained sum/product fiber certificate against 65537^28/2^128, without assuming uniform fibers.
REASON: This changes the parked cubic-energy mechanism to a leading/constant coefficient witness; a direct known quantitative theorem is unavailable under these hypotheses, while the elementary specialization is independently testable and needs no blocked source.
SCOPE: H of order 1024 in E=F_65537, F=F_{65537^28}, k=64, A=66, every m>=1; root subsets in H; only a root-factor applicability proof and class-count averaging with exact integer threshold comparison. Excludes new character estimates, fixed-fiber uniformity, arbitrary-center safety, other agreement levels and a complete sharp-boundary claim.
COVERED_TARGET: Verify the pole-at-zero sum/product subset-fiber construction at 66 agreements for y_{b,d}(x)=x^65-bx^64+d/x on the order-1024 subgroup H of F_65537, using L013's coefficient-collision mechanism and the inspected leading/ending coefficient framework; check strict message degree, injectivity, ambient-extension messages and simultaneous agreement, then compare its averaging certificate with 65537^28/2^128.
LITERATURE_REASON: The saved target introduces rational received words with a pole at zero, outside the previous polynomial-center coverage; theorem-level screening was missing at turn start.

## Gap, relevance and bounded test

The unresolved local question is safety or unsafety at error index 958
(66 agreements) for rate 1/16 on the pinned subgroup instance. L014
bounds the earlier two-additive-coefficient family below threshold;
L015-L018 leave the degree-67 family unresolved and park its tested
energy estimates. This assessment does not reopen those estimates.
The pole witness is a proposed intermediate construction, not a proved
new lemma. Its plausible use is an attained list excluding another grid
radius if its certified size strictly exceeds the threshold.

The next mathematical turn should verify the root-factor correspondence
and test whether restricting the constant coefficient to products of H
yields a sufficiently small class space. Check degree after division by
X, the sign of the constant term, nonzero d, injectivity, exact agreement
sets, and extension-field messages. Establish simultaneous agreement for
zero remaining rows rather than raising a scalar count to the power m.
Use class-count averaging only after proving the valid parameter space;
compare its integer lower certificate with the ambient threshold by
clearing denominators. No new count or bound is calculated here.

Continue an unsafe-radius conclusion only if this certificate strictly
exceeds 65537^28/2^128. If cancellation or injectivity fails, abandon the
construction. If the certificate misses the threshold, stop this averaging
certificate without claiming family safety. A favorable test would still
leave arbitrary-center upper bounds and the full sharp boundary open.
L013's achieved lower certificate at this rate lies between 2^316 and
2^317, whereas the actual threshold lies between 2^320 and 2^321; those
previously checked values motivate the changed class space but do not
establish any bound for this rational family.

## Primary comparisons and reusable locators

**Leading coefficients and root factors.** Gao,
[arXiv:2105.12845v3](https://arxiv.org/html/2105.12845v3#S2),
2022-11-10, Section 2, Proposition 1, Proposition 2 equations (5)-(6),
and Theorem 1 equations (7)-(8). The coefficient-class group tracks
leading coefficients; factorization reduces arbitrary-domain counts to
distinct root tuples and residual polynomials. This supports the known
construction mechanism. It does not track a separately prescribed
constant term. The explicit subfield formulas previously assessed for
L013 are not estimates on the proper subgroup H. Its X+alpha convention
requires checking signs. Reproof of this general counting theorem is
unnecessary; only the changed rational applicability needs verification.

**Leading and ending coefficients together.** Gao, Kuttner and Wang,
[arXiv:2109.02000v1](https://arxiv.org/html/2109.02000v1#S2),
2021-09-05, Section 2, Type I definition, Proposition 1 and proof
(equations (1)-(7)), Theorem 1 (equations (27)-(28)). Type I requires
nonzero constant term and tracks ell leading and t ending coefficients.
Proposition 1 supplies the abelian class group with cardinality
(Q-1)Q^(ell+t-1). Its proof determines the inverse from leading and
trailing triangular recursions. Theorem 1 expresses logarithms of
all-polynomial generating functions in character components for
irreducible enumeration. Neither statement counts squarefree products
whose roots are restricted to H, or gives a maximizing fiber there.
Import the class framework; the restricted root set and RS interpretation
are the identified specialization, not a claim of novelty.

**Reciprocal deep holes are a different statement.** Wu and Hong,
[arXiv:1108.3524](https://arxiv.org/pdf/1108.3524), Theorem 1.2,
printed p. 2; Section 3, printed pp. 7-8, final proof passage.
For Q>=4 and 2<=k<=Q-2 on the full nonzero field, a nonzero multiple
of X^(Q-2), plus a polynomial of degree at most k-1, is a deep hole;
the theorem also includes the analogous X^k family. These are maximum
nearest-distance statements, not large-list lower bounds at k+2
agreements. The proposed polynomial part has terms above the message
degree and the domain is a proper subgroup, so this theorem is not a
match for the full target. No reciprocal obstruction is inferred for
that changed word.

**Rational-word distance reduction.** Keti, Wan and Zhu,
[author-hosted errordistance.pdf](https://www.math.uci.edu/~mketi/research/errordistance.pdf),
18-page unversioned manuscript, no reliable title/date recovered from
its first page. Read Theorem 9, printed p. 6, and proof passages on
printed pp. 11-14: factorization, reversed congruence and weighted
r<d versus unweighted r=d cases. It assumes a representation w/h with
h having no roots in D or at zero, deg h+k<=deg w<=|D|-1, and
minimal numerator degree. With a uniform quotient-ring character bound
and further size inequalities it concludes existence of a codeword
with k+r agreements. The proposed h=X violates its zero condition;
its existence conclusion is also weaker than our threshold requirement.
The factorization passage is supporting mechanism coverage, not an
import of the theorem's quantitative conclusion or its counting
normalizations.

## Unread leads and access limits

Zhu-Wan, Computing Error Distance of Reed-Solomon Codes, TAMC 2012,
LNCS 7287, pp. 214-224,
[publication locator](https://doi.org/10.1007/978-3-642-29952-0_24),
is referenced by the inspected rational manuscript. Direct author-PDF
retrieval returned 502 and one CiteSeer mirror timed out. Its theorem
is not independently imported. The Keti dissertation retrieval also
failed; it is not evidence of coverage. Park these dependent quantitative
routes; the approved elementary test does not use either unread source.
Kuttner-Wang [arXiv:2105.07550v1](https://arxiv.org/html/2105.07550v1),
Theorem 1, was inspected only for scope: prescribed leading coefficients
and irreducible-factor counts, not this trailing constraint on H.
The WAIFI 2024 distinct-root paper was located bibliographically but
not read, and is not essential to the elementary test or claimed as a match.

The [prize page](https://proximityprize.org/) was reread on 2026-10-04:
the designated rates, constant m, threshold epsilon*|F| and field-existence
proviso still agree with the frozen website formulation. The parked
ABF26 definition comparison remains unresolved. Existing work is preserved.

## Review outcome and classification

This is a literature EXPLORATION with an actionable SPECIALIZE decision,
not a mathematical advance. Known scalar coefficient and root-factor
methods supply partial coverage. The proposed next calculation is a
reproduction/application with explicit changed-hypothesis checks; neither
its full statement nor its finite threshold result is imported here.
No novelty is inferred from this bounded search. No lemma, script,
DAG edge or assembled proof has changed. Literature review consumes
no mathematical exploration turn; the count remains 0/3.

## Mathlib

Full rational-center sum/product list statement: **not checked**.
Supporting finite-field groups, polynomial factorization/division and
finite counting: **not checked** in Mathlib. Pinned ArkLib list-model
definitions are **present** as recorded in foundations/02-pinned-list-model.md;
these support definitions, not the proposed construction or list bound.
