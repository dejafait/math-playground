# Mixed-core embedding of an existing four-support obstruction

TARGET: Test whether L031's consecutive-pair obstruction embeds with two supports per core into L130's zero-star ambient families using the prescribed labeling constraints.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed mixed-core comparison in 2026-10-26-mixed-core-common-center-rank.md records six queries, the scoped duplicate search and the single-core failures; no inspected source or local result supplies this embedding. This assessment selects a later finite test, without claiming its success or novelty.
SOURCE_EVIDENCE: Reuse Alrabiah–Guruswami–Li arXiv:2304.09445v3, Definition 2.5 and Lemma 2.7, pp. 7–8, and Shangguan–Tamo arXiv:1911.01502v1, Lemma 4.3's common-root case, pp. 11–12, through L031's audited consecutive-pair example. L030's arbitrary-label packing and L130's conditional-label hypotheses were read; no additional interpolation theorem is needed for this prescribed pattern.
COMPARISON: L031 already supplies the fixed-subgroup nonrealizability for every m>=1, but does not place its four supports in two L030 families. The remaining task is a finite labeling specialization. L130's large-retention existence theorem supplies no particular labeling or survival of the four supports.
GAP: Establish or reject the prescribed two label maps and four memberships, while preserving both distinguished-label conditions. Survival under deletion, simultaneous large retention, universal occurrence and quantitative RS list bounds are outside this target.
REASON: A two-left/two-right embedding would locate a known common-center obstruction in the mixed ambient model, independently of the exhausted retention-only overlap bridge and fixed-core cap tests.
SCOPE: One fixed four-support example on E=F_65537, F=F_(65537^28), H=<g> with g=19139 and order 1024, k=64 and arbitrary m>=1; two 61-cores meeting in a 60-core, arbitrary set bijections satisfying the constraints below. No new rank search or theorem reproof.

## Exact finite prescription — not yet verified

Import L031's consecutive example, in its original vertex order 1,2,3,4.
Use its six pairs U_ij, in order 12,13,14,23,24,34, equal to
{g^(2r),g^(2r+1)} for r=0,...,5. Use its deterministic 60-core K
(first 60 unused subgroup powers) and its private two-sets W_i
(next eight powers, assigned in vertex order). Let S_i be precisely
L031's supports. These are existing data, not a new construction claim.

For the proposed mixed placement, prescribe a=g^0 in U_12 and b=g^10
in U_34, C=K union {a}, C'=K union {b}. Test these choices without
changing the example when an obligation fails.

Use L030's T={16,64,70,102,112,118,121} in F_137, its graph blocks B_p
and four distinct dummy labels d_0,d_1,d_2,d_3. On each side test the
same two candidate auxiliary polynomials p(Z)=0 and r(Z)=Z-16.
The task is to construct and verify bijections

    sigma: Omega -> H minus C,
    sigma': Omega -> H minus C'

subject simultaneously to

    C union sigma(B_p) = S_1,
    C union sigma(B_r) = S_2,
    C' union sigma'(B_p) = S_3,
    C' union sigma'(B_r) = S_4,
    sigma(16,1) = b,
    sigma'(d_0) = a.

Thus L130's left distinguished-column condition uses y_0=1 and the
right uses a dummy mapped to a. No such maps have been exhibited in
this literature turn. In particular an arbitrary set relabeling cannot
be used to transport the subgroup rank certificate.

For a deterministic finite attempt, match domain labels according to
their membership signatures in the two graph blocks, with the two
prescribed distinguished assignments fixed first. Order graph labels
by T's displayed order and then symbol representatives 0,...,136;
put the four dummies last in their displayed order. Order actual labels
by their unique subgroup exponents 0,...,1023. Within each membership
signature, try matching the remaining domain and target labels in
these orders. Compare all signature cardinalities and check injectivity,
surjectivity and every required image. A signature mismatch rejects
this exact prescription; it does not refute all mixed embeddings.
This is an algorithm prescription, not a proved extension argument.

## Acceptance, evidence and limits

Accept the embedding only after the two full bijections or an equally
complete finite-set proof verify every condition. Check the six complete
support intersections, all higher intersections, 68-point cardinalities,
core sizes and left omission of b. Import L031's consecutive-example
nonrealizability with its exact hypotheses and arbitrary-tuple conclusion.
Its rank certificate is already separately audited; no rerun or reproof
is required unless the actual support data differ. A different pattern
requires a new assessment rather than silently changing labels.

If a script is useful in the later research turn, save complete maps,
supports and all checks under scripts/finite-support/; print only actual
and required counts, failures and certificate paths. No script is needed
for a complete direct finite-set proof. This review writes neither.

A success concerns four ambient supports satisfying pairwise packing,
not L130's particular retained output. Do not assert that its conditional
averaging or endpoint deletion preserves this pattern, that the full
ambient union is packed, or that two large retained families must contain
it. Zero right ambient star must be verified from the dummy condition
for the selected labeling; it is not a common-center conclusion.
Occurrence, survival with large retention and an extremal cap remain
separate unsolved steps. The safety bracket is unchanged.

Canonical later proof, if this succeeds, should specialize L030/L031
and the relevant L130 hypotheses, with Hypotheses, Conclusion, Proof and
Mathlib sections; it must not duplicate their full proofs. Primary method
citations are [AGL v3](https://arxiv.org/pdf/2304.09445v3) and
[Shangguan–Tamo v1](https://arxiv.org/pdf/1911.01502v1), with exact passages
given above. Full and supporting Mathlib coverage for this embedding:
not checked. Future classification: REPRODUCTION. No cross-notebook input.
The new ready scope requires separate supervisor approval next turn.
