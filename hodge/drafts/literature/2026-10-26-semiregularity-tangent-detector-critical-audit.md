# Actual semiregularity tangent detector — proposed critical audit

TARGET: Critically audit L173's global Atiyah lift, rank-20 Serre detector and reduced quadratic-square constraint using the actual fixed maps.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 578's completed trace–Atiyah comparison and the invocation-start base-tangent assessment; no broadened target or new theorem discovery is proposed. Step 579 applied their covered constructions and spot-checked the original commutator theorem and truncation triangle.
SOURCE_EVIDENCE: Buchweitz–Flenner arXiv:math/9912245v1 Corollary 4.8, printed p.32, https://arxiv.org/pdf/math/9912245v1#page=32; Stacks 08J5 https://stacks.math.columbia.edu/tag/08J5, 0G81 https://stacks.math.columbia.edu/tag/0G81 and 0FVU https://stacks.math.columbia.edu/tag/0FVU freshly inspected 2026-10-26; reuse Huybrechts–Lehn E31 (1997) 10.1.5,10.1.7–9 and Kuhn (2024) Lemma 4.4/Claim 4.5, Corollaries 4.6–4.7, Lemmas 6.11–6.12 as retained in L171, plus L167's inspected cyclic DG-Lie and diagonalization sources.
COMPARISON: The imported theorems cover commutator annihilation, the family Atiyah construction and trace duality. The audit concerns L173's conditional identification of those operations with the specific j,r,iota and orthogonal point lift; no claim beyond the checked sources or new general theorem is proposed.
GAP: Independently check the global negative-Ext comparison, the cohomological/shift/trace orders in the Serre transpose, the nondegenerate tangent restriction, and the exact polynomial consequence with the full normal and point terms retained.
REASON: L173 is a new source-covered specialization and needs a separate conceptual audit before its rank-20 restriction is used in another mechanism. Step 580 repairs the missing direct source URL and approves the unchanged audit scope through literature comparison only; it does not perform the mathematical audit.
SCOPE: Precisely L173's conditional L108/L116/L165/L166/L167/L171 family and fixed maps; all s,t including empty Z and t=0. No extra semiregularity injectivity, global projectivity, metric-star compatibility, integrability or F existence. No cross-notebook input.

The main gap remains primitive realization and existence of F. The
intermediate target is reliability of the actual tangent detector, whose
downstream use is removal of twenty directions from the allowable
complementary quadratic lift. Audit the completed proof, not a broader
normal-component or other-factor claim.

Check that the actual triangle has no degree-zero sheaf and that both
outer global Hom groups are negative Ext. Verify the global factorization
uses H^1(alpha)=iota from L171 rather than gluing stalk equalities.
Then compare the contraction of the base Atiyah class against a global
H^1(T_B) class with H^2(alpha), retaining the trace-free projection,
the degree-one/degree-two cup order, the relative trace shift -2 and
one fixed Atiyah sign and volume normalization. In particular confirm
that the Serre transpose really is the actual i H^1(iota), so no
point-quotient term cancels a tangent component.

Check that L108's coefficient orthogonality and perfect alternating
forms induce nondegenerate symmetric blocks on H^1. Confirm rank 20
and the exact kernel claim; commutator annihilation alone does not
provide either. Reuse only the dimension-free cyclic part of L167 for
general s,t, and verify the reduced square count n=704-s+2t. At n=0
the quartic vanishes, but complex isotropy must not be promoted to
bracket vanishing or a cardinality exclusion. Retain empty Z and t=0.

Continue if these identities hold with the actual arrows and a common
nonzero convention scalar. Repair or withdraw the affected conclusion
if an extra global derived component, trace-order error or missing
orthogonality invalidates detection. Do not infer vanishing of L166's
global Ext^1 morphism from vanishing of its section evaluations.
Preserve ATTEMPTS/004,/009,/068,/092–095 and the earlier formal witness.

This is a conceptual proof audit, not creative discovery. A genuinely
new mechanism for the residual normal or point bracket needs its own
specific test and source coverage. The audit is essential before such
a mechanism can safely use L173. Full matching Mathlib coverage is not
checked, with no absence claim.

## Step 580: source-record repair and scope approval

LITERATURE_REASON: The supervisor requires a direct source URL in the ready assessment; this bounded repair supplies and checks it without broadening the saved target or repeating discovery.

Fresh retrieval on 2026-10-26 inspected Buchweitz–Flenner's printed
p.32, Corollary 4.8, including its preceding graded-centrality/trace
argument and the following second-order-obstruction paragraph. It
annihilates graded Yoneda commutators, not arbitrary Leray components.
Reuse the perfect-complex hypotheses and q=1 applicability recorded in
`2026-10-26-trace-atiyah-semiregularity-actual-obstruction.md`, primary
results section, and in L173's imported-input paragraph. A locally free
F on the smooth projective product is within that scope; no simplicity
or injectivity hypothesis is added.

Freshly read all of Stacks Remark 13.12.4 (08J5), including construction
of the canonical triangles from the short exact sequence and quotient
quasi-isomorphism; Remark 48.12.6 (0G81), including its evaluation/cup
and trace comparison; and Lemma 48.27.1 with proof and Remark 48.27.2
(0FVU). The relative duality statement requires the stated dualizing
setup, pseudo-coherent M and the evaluation-induced duality isomorphism;
the field-valued pairings are two-sided perfect for bounded coherent
complexes on a proper scheme, with the smooth dualizing shift as in
48.27.1(7). These are supporting constructions, not a theorem identifying
L173's particular transpose or proving its rank. Their actual-map and
shift applicability remains the exact mathematical audit target.

Reuse the prior Huybrechts–Lehn/Kuhn reads retained in L171, with direct
locators https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=230 and
https://doi.org/10.1017/fms.2024.109. The latter DOI retrieval returned a
tool access error this turn; no fresh Kuhn read is claimed or needed to
renew the unchanged recorded coverage. No essential source remains
uncovered for this audit. The parent assessment and L173 contain the
same imported inputs; this repair introduces no duplicate theorem.
ATTEMPTS/004,/009,/068,/092–095 remain scope exclusions as specified
above; none is reopened. Full matching Mathlib coverage remains unchecked.

Decision: SPECIALIZE is retained for the exact saved target, now approved
for a separate research invocation. This is a process repair, not a new
mathematical advance. No lemma, script, DAG edge or argument is changed.
