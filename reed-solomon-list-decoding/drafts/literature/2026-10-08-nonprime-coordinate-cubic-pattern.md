# One non-prime-subfield coordinate — completed source comparison

TARGET: Test whole-pattern avoidance for the shortened cubic family over F_121 on {0,1,2,3,4,5,6,u}.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched cubic polynomial graph/four-intersection packings, exact F_121 parameters, subfield evaluation obstructions and GRS fractional-linear equivalence; compared L032, ATTEMPTS/023, L031, L034 and the prior cubic/extremal assessments. No inspected source settles this prescribed shortened family; failed searches establish no novelty.
SOURCE_EVIDENCE: Inspected Alrabiah–Guruswami–Li arXiv:2304.09445v3 (26 July 2023), Definition 2.5, Lemma 2.7 including its proof, Remark 2.8 and Theorem 2.9, printed pp. 7–9; inspected Marquez-Corbella–Pellikaan arXiv:1508.02187v1 (10 August 2015), Section 3.1, Proposition 3.6, Remark 3.7 and Corollary 3.8 with proof, printed pp. 7–9; reused the exact high-girth theorem comparison in 2026-10-07-sixty-core-extremal-transfer.md.
COMPARISON: Signed evaluation constraints are available over K and GRS representation equivalence has precise fractional-transform/multiplier conditions; neither fixed-coordinate avoidance nor equivalence of these shortened families follows from the inspected statements. Random/generic rank and asymptotic packing theorems do not decide this finite target.
GAP: Determine presence or complete absence of the entire four-block incidence pattern on this exact changed evaluation set, including opposite-edge coordinate reuse and shortening; no calculation or equivalence certificate has been produced.
REASON: The coordinate change alters an untested fixed matrix specialization, and a verified witness can independently stop this family without a full cap or RS realization; ready source coverage now supports one bounded diagnostic, subject to separate supervisor approval.
SCOPE: Only the prescribed changed family, exact witness verification or complete whole-pattern exclusion, and checking whether known equivalence transformations actually transfer an existing witness; no new evaluation sets, labeled-cap theorem, triple-admissibility proof or RS realization.

## Target, relevance and threshold

The main gap remains arbitrary-center 67/68-agreement safety with
955<=t_star(m)<=957. Use K=F_11[u]/(u^2-2),
T={0,1,2,3,4,5,6,u}, and Omega=(T times K) minus
{(0,0),(0,1),(0,2),(0,3)}. Retain every degree-at-most-three graph
whose value at zero is outside the deleted values. Seek four distinct
blocks with all six complete pair intersections of size two, mutually
disjoint as graph-point sets, and two private points in each block.
No changed-family arithmetic or incidence claim was derived in this review.

If avoidance survives a complete check, this may inform an obstruction
to a uniform local cap. The eventual sufficient-cap benchmark is L034's
184665717. Whole quadruple avoidance alone does not imply L034
admissibility: L033 triples must also be checked separately. The old
207272637 count is L032's original-family result, not a certified count
for this changed family. A large admissible auxiliary family would still
not be an unsafe RS list.

## Primary statements and applicability

Alrabiah, Guruswami and Li, *Randomly punctured Reed–Solomon codes
achieve list-decoding capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
Definition 2.5 uses signed Vandermonde difference rows over any finite
field; Lemma 2.7 produces a nonzero kernel from distinct RS messages
by subtracting the final message. Its complete proof was inspected.
Remark 2.8 allows row permutations for equal hyperedge types.
Theorem 2.9 assumes weak partition connectivity and concludes rank
over a rational function field, not every fixed evaluation.
Theorem 1.1 is a random-puncturing result with an explicit field-size
condition, not a guarantee for this prescribed T. No generic-rank
proof needs redoing: only concrete equality and inequality verification
is authorized. Auxiliary K is not the actual subgroup-label field.

Opposite edges may share x with different y. Thus their equalities
must both be retained; they cannot both be encoded as agreement to one
received value at x. The signed polynomial-equality tool can be used
without asserting that such a configuration is one AGL agreement
hypergraph. Singular matrices alone do not certify the six distinctions,
exact intersections, private parts or deleted-point avoidance. L031's
actual-label criterion is a separate restriction, not an exclusion of
all abstract incidences. These are verification obligations for the
approved finite diagnostic, not newly proved converses.

Marquez-Corbella and Pellikaan, *A characterization of MDS codes that
have an error correcting pair*,
[arXiv:1508.02187v1](https://arxiv.org/pdf/1508.02187v1),
Section 3.1, Proposition 3.6: for 2<=k<=n-2, equality
GRS_k(a,b)=GRS_k(c,d) is equivalent to an invertible 2-by-2 matrix M
and nonzero lambda with c_i=phi(M,a_i) and
 d_i=lambda*theta(M,a_i)^(k-1)*b_i at every position.
The vectors have distinct projective locators and nonzero multipliers;
phi is the fractional transformation, and theta is its projective
normalization factor. Here the proposed length/dimension are n=8,k=4.
Remark 3.7 supplies uniqueness on three specified distinct locators;
Corollary 3.8 treats equality with three corresponding locators fixed.
Its proof was read; Proposition 3.6 itself cites earlier proofs.
These statements do not automatically handle an unspecified permutation
or preservation of four deleted values. No transformed-family equality
or inequivalence is claimed here. Any use to transfer a witness must
verify all locators, value multipliers, distinctness and shortening.

The DOI/publisher direct fetch failed; the immutable arXiv primary
manuscript was readable, so this is not an essential source blocker.
The 2016 published version uses different section numbering; the
citation above deliberately pins the inspected 2015 version.

Reuse Glock–Joos–Kim–Kuehn–Lichev,
[arXiv:2205.05564v1](https://arxiv.org/pdf/2205.05564v1),
Theorems 1.1/1.6 and Section 9, exactly as assessed in
[the sixty-core review](2026-10-07-sixty-core-extremal-transfer.md).
The four-block union has 20 points and fits the (s,t)=(8,4)
asymptotic high-girth comparison. No explicit usable cutoff at 964,
prescribed polynomial-family guarantee or actual-label cap is supplied.
That adequate assessment was reused, not browsed again. Its stronger
sparse-hypergraph exclusions and coprimality rejection remain applicable.

## Duplicate/failure comparison and bounded test

L032 and ATTEMPTS/023 refute T={0,...,7} using h,h+f,h+g,h+f+g
and complete graph-point checks. Changing one coordinate is outside that
assessment; no witness was evaluated on the new set during this turn.
A permutation of old coordinate names alone is not evidence that the
new polynomial graph family is the old one. The equivalence source
above identifies conditions to check, without establishing that they
hold. An existing witness transferred by a valid transformation is
sufficient; there is no need to search from scratch in that case.

L030's seven-position quadratic result and L036–L038's fixed affine
neighbors are different prescribed families. Their avoidance does not
extend to these cubics. ATTEMPTS/019–021,023–024 are preserved; none
contains a completed test on this T. No cross-notebook input is used.

After separate gate approval, make one bounded attempt at this exact
family. An exactly verified four-polynomial witness stops whole-pattern
avoidance here. Save coefficients, all eight evaluations of every block,
all six complete pair intersections, private parts and deletion checks.
Testing only the old witness or parallelogram configurations may find a
witness but cannot establish exclusion. A miss leaves the target open.
Complete exclusion would require every coordinate assignment, all
kernels/intercepts, repeated opposite-edge coordinates and unintended
equalities; unsupported completeness is an abandonment condition for
that attempted proof, not evidence of avoidance. Do not change T during
this step or derive a cap from quadruple avoidance alone.

Essential continuation inputs are L032, ATTEMPTS/023, L031 and L034;
L033 supplies an unresolved independent triple condition, and L038 is
comparison only. Changed-family size, quadruple avoidance, triple
admissibility, actual-label ranks, cap conversion, cross-core consistency,
RS realization, 67/68 safety and ABF equivalence remain unresolved.
Full matching Mathlib coverage is not checked. Joyner–Ksir–Traves
arXiv:0801.4007 and generic higher-order-MDS papers were search leads
only; their theorem statements were not inspected and are not inputs.

Queries included `Reed Solomon polynomial graphs cubic four pair
intersections configuration finite field conflict free packing`,
`Reed Solomon evaluation points projective equivalence subfield higher
order MDS 2304.09445`, `generalized Reed Solomon codes equivalence
fractional linear transformation evaluation points automorphism Duer`,
`"polynomial graphs" "high girth" packing`, and
`"Reed-Solomon" "F_121" "cubic"`. Irrelevant snippets were discarded;
no snippet or failed query establishes theorem coverage or originality.
