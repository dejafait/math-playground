# Equality stable double-point tangent lines — source comparison

TARGET: Assess whether L099's actual equality family forces equal quaternionic tangent lines at two distinct stable parameters with isomorphic fibres.
CHECKED: 2026-10-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared L095/L098/L099, L097's uniform-stratum passage, the older geodesy application/audit assessments and ATTEMPTS/046; bounded two-branch/normalization/rigidity searches found a stronger primary tangent-cone and desingularization result, but no theorem forcing coincidence for this actual equality family.
SOURCE_EVIDENCE: Verbitsky, Desingularization of singular hyperkahler varieties I, Math. Res. Lett. 4 (1997), 259--271, Definition 3.1/Remark 3.2(c), Theorems 5.1--5.2, Corollary 5.3 and Theorem 6.1 with relevant proofs, pp. 265, 268--270; Verbitsky alg-geom/9610010v1, Propositions 5.1--5.2, Definition 5.3/Corollary 5.4 and Appendix 5.3, PDF pp. 29--31; reused inspected local-moduli coverage listed below.
COMPARISON: The stronger normalization theorem describes separate quaternionic linear components and smooth normalization, without a coincidence conclusion. Individual-branch geodesy needs its own applicability check and supplies no cross-branch comparison. L099's degree one likewise leaves original-image identifications open.
GAP: No forcing mechanism for equality of the two actual tangent images was identified; a family-specific constraint beyond the inspected normalization and individual-branch results would be needed. This is not a counterexample satisfying the F hypotheses or a theorem that coincidence is impossible.
REASON: Stop the direct tangent-coincidence inference from quaternionic structure, equal scale or normalization; retain the exact proposed target and this negative source comparison. Prepare a distinct stable-open geodesy applicability test with covered tools for separate approval, without undertaking it here.
SCOPE: Comparison of the hypothetical equality family's two stable branches only; EXPLORE does not authorize deriving general coincidence or assuming local geodesy. No essential source blocker was found, and no mathematical application is completed.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because equality-family two-branch rigidity was outside the older charge-seven assessment; the new primary singularity result and its componentwise proof are essential to that comparison.

## Completed comparison

[Verbitsky, *Desingularization of singular hyperkahler varieties I*,
Mathematical Research Letters **4** (1997), 259--271](https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/1997/0004/0002/MRL-1997-0004-0002-a007.pdf#page=10):
Definition 3.1 supplies a hypercomplex variety with compatible positive
metric and holomorphic two-form data; Remark 3.2(c) includes trianalytic
subvarieties. Theorems 5.1--5.2 make the reduced tangent cone a union
of quaternionic linear components. The proof treats each smooth
component separately, uses its geodesy in the flat tangent space,
and takes its closure. Corollary 5.3 and Theorem 6.1 additionally
assume locally homogeneous singularities. Their proofs normalize
the disjoint local smooth components, then glue the structures;
they do not identify different components. Read through the end
of Theorem 6.1, printed pp. 268--270. These conclusions do not
assert point separation by the normalization.

This stronger source does not meet the requested coincidence threshold.
In particular, it cannot be applied to the actual image W just because
L099 identifies its normalization: the required structures and local
homogeneity have not been verified here. Global integrality of W is
already an L099 input, but the inspected theorem gives no replacement
for the missing local branch comparison. No new example or specialized
theorem is derived in this turn.

Reuse [the local-geodesy assessment](2026-10-07-charge-seven-classifying-map-total-geodesy.md)
and [its source audit](2026-10-07-charge-seven-geodesy-critical-audit.md).
Their primary local connection-moduli statements remain relevant general
tools, not equality-family conclusions. The geodesy source was checked
again narrowly: [Verbitsky, alg-geom/9610010v1, Propositions 5.1--5.2,
Definition 5.3/Corollary 5.4 and Appendix 5.3](https://arxiv.org/pdf/alg-geom/9610010v1#page=29).
It requires quaternionic and metric compatibility and works without
ambient compactness. Retain the stronger all-hyperholomorphic connection
hypotheses of Proposition 5.2: the Appendix proof uses zero contraction
of the ambient curvature despite the broader wording of Proposition 5.5.
No point-separation or two-tangent-coincidence conclusion is supplied.

At an isomorphism F_y ~= F_z, HE uniqueness and scalar automorphisms
give the common harmonic connection tangent used in the saved target.
L095's norm identity and L098's natural derivative describe each
inclusion separately. Their statements contain no comparison between
the actual curvature along S_1 x {y} and S_1 x {z}. Comparing primary
theorem hypotheses therefore leaves an essential family-specific gap;
it does not refute such a possible comparison. The old Euler/linearized
Hom method remains stopped by ATTEMPTS/046, with its original scope
and evidence intact.

Queries: `Verbitsky trianalytic subvarieties normalization branches tangent
spaces immersion singularities`; `hyperkahler totally geodesic subvarieties
self intersection tangent quaternionic lines rigidity`; `Verbitsky
"desingularization" "locally" "branches" hyperkahler`; `Verbitsky
"singularities" "linear subspaces" trianalytic`; `"trianalytic"
"self-intersections"`; `"hyperkahler" "totally geodesic" "tangent"
"intersection" Verbitsky`; `"hyperholomorphic" "isomorphic" "fibres"
"classifying"`. Search snippets alone were not theorem evidence.
The ETH singularities-survey PDF failed to open; the accessible primary
1997 paper resolved the relevant theorem scope, so no essential access
blocker remains. Generic-Hilbert-scheme exclusion is reused only as the
previously inspected, inapplicable lead: its genericity hypotheses are
not established at this marked RM metric. Higgs/flat-connection search
leads were not inspected or imported and do not certify K3 coverage.
Absence of a matching result is not a novelty claim.

The source comparison supplies useful NEGATIVE evidence about this
inference. Stop the proposed coincidence route until a specific new
family-level mechanism and discriminating test are identified. A
different, independently testable prerequisite is the actual stable-open
local geodesy specialization, assessed in
[the proposed continuation](2026-10-13-equality-stable-local-geodesy.md).
That continuation needs separate approval next turn. It is not a
substitute for coincidence or a promise of stable-image separation.
Full matching Mathlib coverage remains **not checked**.

## Initial proposal retained (superseded as current routing)

Essential local inputs: L095, L098 and audited L099, retaining
L096/L097 and the rank-four marked scope. Hypotheses are the same
hypothetical locally free rank-two polystable F, identical metrics,
integral c_1=0 and ch_2=-14e_1-21e_2-tau_D, common H and finite
possibly empty Z. At a putative double stable-image point take
distinct y,z in U with F_y isomorphic to F_z. Their actual harmonic
derivatives define lines in the harmonic connection tangent after
that identification; the ambiguity is scalar and does not change
the subspaces. Equality of these subspaces is a target, not an input.

The main gap remains universal primitive Hodge-class realization.
This is a proposed prerequisite for stable-image separation. A
later branch-coincidence argument would additionally need actual
local geodesy and its uniqueness implications; those are not proved
or approved here. Integrated split germs, separation at m_0, F
existence, reconstruction and transport remain independent gaps.

The discriminating literature test is an applicable theorem or
concrete, independently testable rigidity condition forcing equality
of the two tangent images. A result giving only equal dimensions,
equal metric scales or separate quaternionic lines is insufficient.
If no forcing mechanism is found, stop this proposed coincidence
route or identify a materially different covered test; do not repeat
the relative-Hom Euler/first-order calculation stopped in ATTEMPTS/046.
That stop concerned the older charge-seven family, so it is evidence
about a method, not an exclusion of this equality kernel. The older
geodesy assessment is a source lead only; L067 is not imported as a
changed-family theorem. Full matching Mathlib coverage is not checked.

This initial proposal did not approve or undertake previously uncovered
mathematics. At proposal time the next turn was literature-only. The completed L099
audit is retained independently of this continuation's review.
