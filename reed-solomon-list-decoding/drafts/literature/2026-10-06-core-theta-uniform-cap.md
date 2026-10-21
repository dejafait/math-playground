# Uniform local theta cap — completed quantitative comparison

TARGET: Establish a uniform bound beta_C<1532496 for L027's labeled pair-plus-recursive-theta model over every 61-core.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched recursive-theta dual certificates, constant-weight packing at (963,7,3), determinant/finite-field forbidden-intersection bounds and high-dimensional Hoffman mechanisms; inspected the primary statements below and reused the recorded local source/failure comparisons. No inspected theorem supplies the target cap.
SOURCE_EVIDENCE: Castro-Silva et al., Combinatorica 43 (2023), Theorems 2.4–2.5 pp. 917–919 with complete proofs, Section 4 pp. 924–926 and Section 5 pp. 926–928; Liu–Shangguan, arXiv:2401.00733v2 (21 January 2024), definitions pp. 1–2 and Theorem 1.4 p. 4; reused Filmus–Golubev–Lifshitz v1 Theorem 4.1/proof and checked the published Theorem 4.2/proof pp. 1014–1015. Exact recursive supporting statements are in foundations/07-core-conditioned-theta-source.md.
COMPARISON: Weighted graph-link theta inequalities are available without regularity, but their numerical coefficients and their joint combination with pair packing remain uncomputed. Weak optimization does not give the requested finite cap or a practical exact certificate. Packing asymptotics neither decide n=963 nor include labeled determinant exclusions.
GAP: An analytic, label-aware upper certificate on the same shared matrix with sufficient quantitative strength uniformly over C is missing; no inspected source covers that specialization or proves the cap impossible.
REASON: Source coverage now supports one bounded analytic certificate attempt using weighted link inequalities and pair-clique constraints; retain the finite cap target without claiming novelty or assigning equal optima to cores.
LITERATURE_REASON: The quantitative cap is outside the previous soundness/counting SPECIALIZE scope and was REVIEW_REQUIRED; weighted upper-certificate tools and local packing obstructions were essential missing comparisons.
SCOPE: One proof attempt at the exact saved cap, using L027's unchanged shared lift, imported weighted graph-link inequalities and ordinary pair-clique constraints; no generic labels, extra forbidden triples, unproved symmetry reduction or new SDP hierarchy.

## Gap, intermediate target and downstream test

The main gap is arbitrary-center safety at 68 agreements in C001a's
fixed instance. The intermediate target is the exact TARGET above.
L027 proves that this uniform strict cap yields integer local bounds
1532495 and hence a list bound at most 65537^28/2^128, for every m>=1.
Its ordinary local bound is 148379361/35, with floor 4239410, and
fails this test. These are existing L027 results, not new calculations.

The next attempt should seek an analytic certificate using nonnegative
weighted theta bounds on actual graph links and the pair-clique rows,
keeping a single shared F. Theorem 2.4 is source coverage for supporting
inequalities, not a completed joint dual or its numerical coefficients.
Any proposed certificate must justify every coefficient and PSD claim,
work on all cores, and compare its achieved cap with 1532496. A useful
intermediate certificate can be reported without closing the gap.

Continue if the attempt supplies a rigorously justified saving or a
concrete certificate family with an explicit sufficient strength test.
Stop its specific prescription if it only reproduces L027's ordinary
cap, needs missing uniformity/transitivity, or has an exact feasible
shared-lift witness at or above 1532496 for some core. Such a witness
would refute this uniform-cap prescription, not prove RS unsafety.
A failed upper certificate alone would not refute the cap. No huge
black-box optimization or toy-instance optimum is an exact certificate.

## Primary results and their limitations

Davi Castro-Silva, Fernando Mário de Oliveira Filho, Lucas Slot and Frank
Vallentin, [A Recursive Theta Body for Hypergraphs](https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf),
final version, Combinatorica 43 (2023), 909–938,
DOI 10.1007/s00493-023-00040-9. Reuse Definition 1.1, Theorem 2.1
and Corollary 2.3 from the canonical source note. Newly inspected
Theorem 2.4, pp. 917–918, exactly describes TH by all nonnegative
weighted theta inequalities. It covers arbitrary finite graph links,
including empty ones; no vertex measure is prescribed. Full proof
was read, including the base, removal of negative weights, separation
and downward closure. No weighted link optimum has been evaluated.

Theorem 2.5 and full proof, pp. 918–919, concern weak optimization in
explicit input size with fixed uniformity. The all-7-subset vertex set
and all-core requirement make this different from a compact algorithm
in the 1024 point labels. The proof's interior-ball step is for the
unsliced lift; it does not directly establish the same claim after
L027's pair-zero equations. Thus do not cite it as a tractable exact
solver for K_C. Section 4's complement/antiblocker counterexamples,
equation (17), Theorem 4.1 and proof were read at pp. 924–926.
The complementary-hypergraph shortcut fails in general; TH-circle
is a distinct body. Appendix A's auxiliary duality theorem was not
independently audited and is not an imported input. Section 5's
averaging proof and Theorem 5.1/full proof, pp. 926–928, require
objective-preserving automorphisms and actual transitivity for the
one-row reduction. Arbitrary relabelings or one representative core
are not justified. No joint-dual theorem is silently imported.

Yuval Filmus, Konstantin Golubev and Noam Lifshitz,
[High dimensional Hoffman bound and applications in extremal combinatorics](https://alco.centre-mersenne.org/item/10.5802/alco.190.pdf),
Algebraic Combinatorics 4(6) (2021), 1005–1026,
DOI 10.5802/alco.190. The earlier assessment read v1 Theorem 4.1
and full proof. The published statement is numbered **Theorem 4.2**,
pp. 1014–1015, and its full induction proof was read here. For a
weighted r-uniform hypergraph its bound is
alpha(X)<=1-1/product_(i=0)^(r-2)(1-lambda_i), using the induced
vertex measure and minimum supported-link skeleton eigenvalues.
It is not a uniform-cardinality cap without a suitable edge measure
and a conversion. Neither that measure nor spectra for the labeled
core model are established. Reuse the old rejection of the
empty-symmetric-difference triangle application: it is not L020's
pattern with unique portions. No repeated spectral calculation is
approved merely by renaming the old route.

Miao Liu and Chong Shangguan,
[Approximate generalized Steiner systems and near-optimal constant weight codes](https://arxiv.org/pdf/2401.00733v2),
v2, 21 January 2024, definitions pp. 1–2, Theorem 1.4 p. 4.
For fixed alphabet size q, weight w and odd distance d, putting
t=(2w-d+1)/2, it states that sufficiently large n admit codes of
size at least (1-o(1))(q-1)^t binomial(n,t)/binomial(w,t).
For binary weight seven, distance at least nine is equivalent to
at least ten, corresponding to intersection at most two. This is
the relevant ordinary-packing regime. The statement provides no
usable finite error bound at n=963 and no determinant condition.
No lower bound for alpha(G_C,J_C), beta_C or actual lists is imported.
Its matching proof was not needed for this scope rejection and was
not audited. The original Rödl publisher PDF failed to load; it is
an unread lead, not an essential blocker because this inspected
primary theorem suffices for the limited asymptotic comparison.

## Duplicates, failures and mechanism choice

Read L027's entire model/proof and L020's criterion and degeneracy
proofs. Targeted local searches and reads covered ATTEMPTS/010,
history/056–058, the core-conditioned determinant and pair/theta
assessments, and the earlier triple-extremal assessment. L001/C001a
are reused through L027's established transfer, without rechecking
unchanged arithmetic certificates. No local quantitative theta cap
or joint dual was found; absence from this bounded search is not
novelty evidence. L021–L026 and ATTEMPTS/017–018 remain independent
stops on their fixed distance-only diagnostics.

Three candidate mechanisms were compared: weighted link inequalities
plus pair packing; edge-measure Hoffman spectra; explicit full joint
optimization. The first is selected for one bounded attempt because
it retains unit-cardinality accounting and uses inspected source tools.
The second retains the earlier unresolved measure/spectral obstacles.
The third has no compact representation or exact-certificate plan.
Allowed antipodal/singular triples in ATTEMPTS/010 remain essential;
none is removed to make the bound easier. This assessment approves
exploration, not the mathematics or success of a certificate.

Essential continuation inputs: L001, C001a, L020, L027 and
foundations/07-core-conditioned-theta-source.md. Unresolved assumptions
include uniform quantitative link estimates, any proposed joint PSD
certificate and actual automorphisms. Empty links, zero diagonals,
all core incidences and exact local floors must be retained. The
955–957 bracket, 67-agreement safety, local/list realization, earlier
full-SDP feasibility, sharpness and ABF equivalence remain open.
Matching quantitative or graph-link theta coverage in Mathlib is
not checked; unknown coverage is not evidence of absence.

Queries: `"recursive theta" hypergraphs dual bound certificate`;
`"constant weight" "A(963" 7`;
`hypergraph independence packing forbidden intersection determinant finite field theta bound`;
`"High dimensional Hoffman bound" Filmus Golubev Lifshitz pdf`;
`"theta" "constant weight" "packing" upper bound 7 3`;
`"packing" "Rödl" 1985 "theorem" partial Steiner systems pdf`;
`"Approximate generalized Steiner systems and near-optimal constant weight codes" arxiv`;
`"On a Packing and Covering Problem" Rödl pdf`.
Uninspected incidence/container hits and configuration-free matching
theorems are leads only, outside this approved certificate scope.

No cap, spectrum, new lemma or mathematical script was produced.
The next mathematical classification may be POTENTIALLY_NEW because
this bounded review established no matching quantitative result;
that label certifies no originality. The completed source review is
EXPLORATION, not a mathematical advance or a disproof.
