# Split stabilizer and actual section image — completed source comparison

TARGET: Assess whether the split-fibre stabilizer action ad(h_0) preserves the actual section image rho_z(H), before attempting to constrain its bracket rank.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 576 searched restriction-image invariance, automorphisms of restricted bundles, equivariant Kuranishi maps and deformation restriction terminology; inspected the three primary texts below, L116/L164/L170/L172 and ATTEMPTS/092–094, and reused the step-540 formality warning. No inspected theorem or family-matching counterexample decides the actual image's invariance.
SOURCE_EVIDENCE: Buchdahl–Schumacher arXiv:2002.03548v1, Theorem 1 p. 2, Lemma 4.1/Corollaries 4.2–4.3 with proof p. 10 and Section 5 pp. 14–16; Chen–Pertusi–Zhao author-hosted 15-page version, Section 2 hypotheses p. 3, Lemmas 2.2–2.4/Remark 2.5 pp. 3–6 and Section 2.3 pp. 6–7; Arbarello–Sacca Adv. Math. 329 (2018), Proposition 6.1 and proof pp. 680–681 and (5.5) p. 675. Version/access qualifications are below.
COMPARISON: The sources give the fixed object's deformation complex or Ext space an action of its own automorphisms. Their equivariance does not identify the image of H^1(X,End_0(F)) in a split fibre's Ext^1 as a subrepresentation of that fibre's larger automorphism group. L116 retains H^0(X,End_0(F))=0; no extension of h_0 or equivariant structure on the restriction morphism is supplied.
GAP: Actual preservation ad(h_0)rho_z(H) subset rho_z(H) remains undecided. Neither a precise theorem with the required restriction-image conclusion nor an evaluable actual-map test was found; this is not a proof of noninvariance, nonexistence of F or novelty.
REASON: The bounded source comparison meets the proposal's abandonment test: park invariance-only control absent a new compatible action or independently evaluable map. EXPLORE records completed discovery with an unanswered geometric question, not approval to repeat this mechanism. Prepare a different star/duality compatibility question separately.
SCOPE: The unchanged hypothetical K3 product family and actual maps of L164/L170–L172; z in nonempty finite reduced Z, h_0=diag(1,-1), H=H^0(B,M), general t, with no global extension of the fibre stabilizer, section integrability or F existence assumed.

LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changed from section/KS position to a restriction-image group action; essential equivariance hypotheses and proof cases had not been inspected. Existing cup/base-change and harmonic assessments are reused.

## Invocation-start proposal (historical)

The proposal below is preserved as the question reviewed. Its pending
instructions are superseded by the completed comparison at the end.

### Purpose and bounded comparison

The main gap is primitive Hodge realization. On the conditional F
branch the actual point quadrics, complementary operation and square
length remain unknown. L172 controls the section image's position
relative to the actual KS radical, but leaves its pairing unevaluated.
This proposal tests a different possible source of geometric control:
whether the specific split-fibre stabilizer preserves that actual
image. A justified compatibility could help constrain actual point
quadrics for L167's polynomial-lift question. A nonzero bracket alone
would still not exclude F.

Essential inputs for the comparison are L116,L164,L170,L171,L172,
with the original conditional hypotheses inherited through
L071/L094/L095/L108/L109/L111/L115. L163 is a contrast and source of
the harmonic-operator warning, not an invariance premise. No
cross-notebook result is proposed. Keep the identical marked K3
factors, common metric/triple/forms, actual compatible connection,
locally free rank-two product-polystable F with integral c_1=0 and
ch=2-14e_1-21e_2-tau_D+62e_1e_2. Retain ordinary M(z), full derived
E_z, actual e_z,j,i,r, H and rho_z. Do not replace rho_z(H) by an
arbitrary subspace, assume generic position, or extend the fibre
automorphism to F. Empty Z and t=0 are vacuous for this test.

Search the exact statement, standard terminology and stronger
restriction/equivariance results, including counterexamples for
restriction of global bundle deformations to a nonsimple fibre.
Read primary hypotheses and essential proof cases before declaring
applicability. Compare any global-equivariance requirement with this
actual conditional family, retaining L116's H^0(X,End_0(F))=0;
do not assume a global stabilizer exists. Reuse existing actual-map
coverage where unchanged, but it does not cover the new invariance.
No novelty inference follows from the local phrase search.

Continue only if a precise theorem or a genuinely source-covered
actual-map test can decide preservation of rho_z(H) by ad(h_0).
If the available equivariance needs a global automorphism that is
not present, or only gives a quadratic local model, record that
obstruction and abandon this invariance-only mechanism unless a
materially different, independently testable comparison is found.
In particular, no connection-parallelness or derivation property may
be inferred from L163's positive forms. ATTEMPTS/092–094 remain
preserved: this proposal asserts neither additive-splitting vanishing,
scalar-isotropy exclusion nor cyclicity-only complementary vanishing.

No new result or creative mathematical attempt is approved here.
The next task is literature_comparison, not proof_attempt. If a
genuinely new bounded actual-map mechanism becomes ready, a later
checkpoint should nominate proof_attempt/creative with its precise
obstruction and decisive test. Full matching Mathlib coverage for
this proposed invariance has not been checked.

## Completed comparison — step 576

2026-10-26. LITERATURE / EXPLORATION / NOVELTY_UNCHECKED; actual task
literature_comparison. The main gap remains uniform primitive Hodge
realization; this review establishes no new mathematical result.

### Inspected primary statements and essential cases

1. Buchdahl–Schumacher, *Polystability and the Hitchin–Kobayashi
   correspondence*, [arXiv:2002.03548v1](https://arxiv.org/pdf/2002.03548v1),
   10 February 2020, 37 pages. Theorem 1, PDF p. 2, assumes a polystable
   bundle with Hermite–Einstein connection on a compact Kähler manifold
   and makes its Kuranishi map Aut(E_0)-equivariant. Lemma 4.1 and
   Corollaries 4.2–4.3, p. 10, use parallelness of holomorphic
   endomorphisms for the central contracted-curvature connection. The
   proof commutes conjugation with the differential and its adjoint,
   then uses uniqueness of the small correction. Section 5, pp. 14–16,
   identifies the conjugation representation and its moment map
   (Corollary 5.3). Applied to the split fibre these concern its whole
   deformation space; applied on X they concern Aut(F). They do not
   relate the two actions on a restriction image.

   This is the inspected **2020 preprint**, not a claim to have reread
   the 2022 article *Polystable bundles and representations of their
   automorphisms*, DOI 10.1515/coma-2021-0131. Its d-nb PDF returned 429
   and the publisher PDF 405; the accessible primary preprint suffices
   for the stated scope comparison. No new source-access blocker is
   the reason for parking the geometric mechanism.

2. Chen–Pertusi–Zhao, *Some remarks about deformation theory and
   formality conjecture*, [author-hosted 15-page version](https://sites.unimi.it/pertusi/Papers/Formality.pdf),
   retrieved 2026-10-26; no version date is printed in the inspected
   text. Section 2, p. 3, takes a smooth projective complex variety,
   a full admissible derived subcategory and an object with no negative
   Exts. Lemma 2.2 constructs an Aut(F)-equivariant locally free
   replacement; Lemmas 2.3–2.4 and Remark 2.5, p. 6, give its rational
   action and deformation comparison. Section 2.3, pp. 6–7, assumes
   linear reductivity and chooses invariant splittings to obtain an
   equivariant Kuranishi functor. The proof begins with an action on
   that same object and complex. Both local bundles here are honest
   sheaves; this removes the negative-Ext issue but supplies no common
   larger group acting on the restriction map. Reductivity cannot
   create a missing action. No new formality result is imported.

3. Arbarello–Sacca, *Singularities of moduli spaces of sheaves on K3
   surfaces and Nakajima quiver varieties*, Adv. Math. 329 (2018),
   649–703, DOI 10.1016/j.aim.2018.02.003,
   [Proposition 6.1 and proof, pp. 680–681](https://www.math.columbia.edu/~giulia/Quiver.pdf#page=32).
   For a polarized K3 and a polystable sum of distinct stable sheaves
   with multiplicities, the proposition identifies the Ext representation
   with a doubled-quiver representation. The proof decomposes Exts
   between the factors; its quadratic/moment-map comparison refers to
   Kaledin–Lehn–Sorger Section 3.4. Equation (5.5), p. 675, is the
   equivariant moment map. These concern the full Ext space, not the
   global restriction image. As in L164, the real-Kähler fibre scope
   comes from the existing analytic coverage; no algebraic-polarization
   chart is transferred here. The further cited proof was not needed
   or newly inspected to assert a restriction-image conclusion.

### Exact scope decision and stopping test

L164 identifies rho_z with restriction of the actual global deformation
classes; L172 places its image in the fixed normal summand and away
from the actual KS radical. Neither is an equivariance statement.
In particular an invariant splitting chosen inside the **fibre's**
deformation complex is not a splitting of the actual global restriction
map. L116's vanishing of global trace-free endomorphisms remains an
essential qualification. No argument here excludes a different,
non-global reason for invariance.

The desired intermediate target could have constrained the actual
section quadrics, hence L167's polynomial-lift test. The bounded review
found only fixed-object equivariance and local obstruction models, not
the requisite compatibility or a computable defect for this conditional
family. Park the invariance-only route, preserving ATTEMPTS/092–094
and the harmonic-operator warning. Reopening requires materially new
restriction-compatible input; another formality or positivity audit is
insufficient. Empty Z and t=0 remain vacuous. Independent F existence,
actual bracket values, transport and primitive realization are unresolved.

Search queries included `deformations restriction map vector bundles
automorphism stabilizer equivariant Kuranishi image`, `restriction Ext
deformation image invariant automorphisms restricted bundle`,
`"restriction map" "Ext" "automorphism" deformation sheaves equivariant
image`, and `deformation restriction homotopy fiber vector bundles
Manetti`. No matching counterexample was inspected; unrelated search
results are not theorem evidence. No novelty inference is made.

Mathlib: matching restriction-image invariance coverage was not checked.
No lemma, proof repair, mathematical script or DAG/PROOF change is made.
The next, different star/duality target is REVIEW_REQUIRED and is not
approved by this completed review.
