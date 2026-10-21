# Completed coverage review for a different pole family

TARGET: Assess source coverage for a 67-agreement dictionary and uniform upper test for degree-68 monic numerator centers with a fourth-order pole at zero.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the existing Gao/Hayes, linear-cofactor and Li-Wan assessments; searched rational received words, higher poles, Hayes subgroup zeros and prescribed ending coefficients with linear factors; checked local residual-factor failures and duplicates. Exact queries and inspected passages are recorded below.
SOURCE_EVIDENCE: Reopened Gao 2203.06729v5 definitions (1)-(2), Proposition 2 and proof (15)-(16), definition (17), Theorem 3 and proof (18)-(19), Proposition 1 and Section 4 (21),(25)-(28); Li-Wan 1806.00152v3 Lemma 4.1 and complete proof; Li-Wan 1507.06329v1 Theorem 2.1, Corollary 2.2 and Lemma 2.6 cycle identity. Reused prior theorem comparisons for excluded full-field and nearest-distance results.
COMPARISON: The arbitrary-domain Hayes identity covers the residual-degree-one counting framework, and the arbitrary-modulus character lemma and weighted sieve cover the tools for one upper test. No inspected theorem supplies the entire interleaved subgroup list bound or its threshold verdict; L099-L100 do not extend by citation alone.
GAP: The RS dictionary, residual coefficient-field descent, extra-root multiplicities, actual Fourier group, residual character sum, all powered/twisted exceptions and finite upper comparison remain mathematical obligations. No formula or bound for the changed family is established in this review.
REASON: The changed pole introduces a residual factor and a different modulus; adequate general tools are now identified, permitting a separate bounded specialization without new character estimates or reopening the stopped energy route.
SCOPE: E=F_65537, H of order 1024, F=F_(65537^28), degree<64, m>=1, threshold T=65537^28/2^128; centers ((X^68+a3 X^3+a2 X^2+a1 X+a0)/X^4,0,...,0), ai in E and a0 nonzero, with at least 67 simultaneous agreements.

LITERATURE_REASON: The fourth-order-pole/residual-factor target was outside the ready X^3 pure-subset assessments; this completed turn supplies only its missing source comparison.

## Scope and relevance

This completes the saved source-review action, without deriving the
dictionary, a specialized character formula or a list bound. Essential
local context is C012a, L099, L100 and foundations/01–02, retaining the
unresolved ABF comparison. L015 and ATTEMPTS/008 are contrasts only.

The main gap remains arbitrary-center 67/68 safety. A valid dictionary
and one finite upper test could decide whether this different family
also cannot witness unsafety at index 957. No passing bound is assumed.
The changed residual-factor issue must be assessed rather than hidden
in the old pure-subset count. The source comparison should preserve
the proposed test while determining which precise theorem statements
cover it and what, if any, specialization remains.

## Primary comparison

Gao, *Asymptotic distributions of the number of zeros of random
polynomials in Hayes equivalence class over a finite field*,
[arXiv:2203.06729v5](https://arxiv.org/html/2203.06729v5), 2024-01-07:
definitions (1)-(2) allow ell=0 and monic modulus Q; D avoids its zeros.
Proposition 2, (15)-(16), and Theorem 3, (17)-(19), count chosen-root
incidences with a monic residual polynomial on arbitrary D. Their
factorization/coefficient-extraction proofs and Proposition 1's
exact-root inversion were inspected. The relevant parameters are
q=65537, Q=X^4, t=4, ell=0, D=H, k_source=64, j=67 or 68;
the residual degrees in (17) are respectively one and zero. Nonzero
a0 supplies coprimality. This covers the counting framework, leaving
the RS/extension-field interpretation to a later proof. Section 4's
Proposition 3 requires ell>=1 and the full zero-complement domain (21);
its proof (28) completes root sums over that domain. Neither its bound
nor Theorem 2 is imported for H. Theorem 1's asymptotic regime does not
decide this fixed extreme-agreement instance. No general identity
needs reproof.

Li and Wan, *Distance Distribution in Reed-Solomon Codes*,
[arXiv:1806.00152v3](https://arxiv.org/html/1806.00152v3#S4), 2019-07-30,
Lemma 4.1, printed pp. 9–10: for a nontrivial character of the units
modulo any positive-degree monic f, extended by zero on nonunits, the
degree-j monic sum is bounded by binomial(deg(f)-1,j) q^(j/2).
Its complete L-polynomial proof includes imprimitive characters and
vanishing high-degree coefficients; squarefreeness is not required.
Thus X^4 is within its stated modulus scope. The separate cumulative
bound requires triviality on field units and must not be used for an
arbitrary character. Reuse the prior Theorem 5.1 comparison: its
full-field root estimate is not a subgroup theorem. The future test
must justify every restricted cycle sum and retain the residual-factor
character sum before applying this input; no such estimate is derived here.

Li and Wan, *Counting polynomial subset sums*,
[arXiv:1507.06329v1](https://arxiv.org/html/1507.06329v1#S2), 2015-07-22,
Theorem 2.1 and Corollary 2.2, printed p. 5, allow arbitrary finite
domains and complex weights; conjugacy grouping needs a symmetric
domain and weight. The cycle exponential identity in the Lemma 2.6
proof was rechecked. These cover the weighted distinct-coordinate
tool, including fixed-point cycles and ordered/unordered conversion.
The additive-ring fiber formula in Lemma 3.1 is not asserted directly
for multiplicative unit residues. Import the general sieve instead.

## Discovery, duplicates and preserved failures

Queries included `"Reed Solomon" "rational" "prescribed" "coefficients"
list decoding`; `"Hayes" "linear factors" "residue" polynomials subgroup`;
`"Reed-Solomon" "higher order" "pole" list`; `site.arxiv.org "Hayes"
"subgroup" "zeros"`; `site.arxiv.org "prescribed" "ending coefficients"
"linear factors"`; and `"polynomials" "prescribed ending coefficients"
"subgroup"`. Several searches returned irrelevant material. No search
snippet is used as a theorem, and no absence/novelty conclusion follows.
An irreducible-enumeration hit duplicates the Gao–Kuttner–Wang lead
already excluded in the order-three assessment; it is not a root-list
counting input. No newly found lead is essential or source-blocked.

Reuse the [order-three dictionary comparison](2026-10-20-order-three-pole-67-agreements.md),
the [linear-cofactor comparison](2026-10-04-degree-sixty-seven-linear-cofactor.md)
and the [uniform-upper comparison](2026-10-20-order-three-pole-uniform-fiber-upper.md)
for their inspected exclusions and named tools. L099 has no residual
factor; L100 uses its restricted constant-H class group. Neither gives
this family's admissible classes or normalization. L015's leading
coefficient descent proof is not a trailing-coefficient descent proof.
ATTEMPTS/007–008 stop specified energy/norm allowances, and ATTEMPTS/083
stops an averaging certificate. None is repeated or erased. Local
searches found only the present proposal for the fourth-order family.

## Bounded continuation

The [ready specialization assessment](2026-10-20-order-four-pole-dictionary-uniform-upper.md)
records the exact later target and all outstanding checks. It is newly
written and receives separate supervisor approval next turn. This
review has established adequate tool coverage, not a successful
specialization. A later proof must distinguish incidences from messages,
allow repeated residual roots, prove descent for ambient-field candidates
and eliminate all nonfirst tuple rows. It must determine the correct
group instead of copying L100's denominator, treat principal and
constant-only characters exactly, and prove nontriviality after every
cycle power and subgroup twist before using Lemma 4.1. Retain the
residual summation and factorial throughout.

Continuation test: approve a later bounded mathematical target only
if exact source hypotheses cover the needed dictionary/counting tools
and the proposed finite certificate has a specified comparison to T.
If coverage is inadequate or a theorem already decides the family,
record that precise result or obstruction and reroute; do not assume
uniformity, extension-field descent, or a missing character estimate.
No arbitrary-center bound, exact fiber maximum or novelty is claimed.
Outcome EXPLORATION / LITERATURE / REPRODUCTION: actionable source
coverage, with no new mathematical result or threshold calculation.
Mathematical exploration usage remains 0/3. PROOF.md, DAG.md, lemmas/
and scripts/ are unchanged. No cross-notebook theorem input is used.
Mathlib coverage for this full specialization and its supporting facts
is not checked; that is not evidence of absence.
