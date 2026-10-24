# Preferred twisted stable-open connection — completed source comparison

TARGET: Assess whether hyperkähler transform preservation identifies the preferred twisted harmonic Chern connection as ASD on B minus Z.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October 5 preservation and October 23 preferred-metric assessments; searched hyperkahler Nahm projection/index-connection and Fourier-transform terminology; inspected BBHR (1998) Sections 3.1–3.3, Bartocci–Jardim (2003) Theorems 2–3, and author-hosted Bruzzo–Hernandez Ruiperez–Tejero Prieto notes Sections 3.2–3.4. Compared L094, L147, L148 and ATTEMPTS/063/066/086.
SOURCE_EVIDENCE: BBHR, A hyperkahler Fourier transform, Differential Geometry and its Applications 8 (1998), 239–249, Section 3.1 p. 243, Definition 2 p. 244, Section 3.3 Lemmas 1–2/Theorem 3 pp. 245–246; Bartocci–Jardim, math/0312045v1 (2 December 2003), Theorem 2/proof p. 4 and Theorem-Definition 3 p. 5; Bruzzo–Hernandez Ruiperez–Tejero Prieto, author-hosted DerCatCohSyst3-v4.pdf, Sections 3.2–3.4, PDF pp. 21–24, Definition 3.3 and Theorems 3.4–3.7 with surrounding metric/connection construction.
COMPARISON: The published transform setup requires compact source X, allows a second hyperkahler target Y without a compactness hypothesis, states rotation-independence of IT, and identifies natural holomorphic Hermitian bundles in Lemma 2. The later author notes explicitly identify the induced Hermitian connection as Chern for a general product kernel. These cover the changed framework; the actual preferred-line, concentration and metric specialization remains a separate mathematical step.
GAP: Verify the given HE dual line is a quaternionic instanton, localize to U with the actual kernel, retain IT for every induced structure, and identify the natural rank-24 transform metric with L148 under its specified higher-image map; only then infer ASD. No extension across Z or whole-base polystability is covered.
REASON: Ready coverage for exactly TARGET as a later REPRODUCTION specialization of known transform and Chern-connection results; this literature-only turn supplies source evidence and applicability obligations, without proving the conditional ASD assertion.
LITERATURE_REASON: Changed coefficient L^{-1} with its preferred HE dual metric, localization to B minus Z, and the essential actual harmonic-connection identification are outside the saved whole-base untwisted preservation scope.
SCOPE: Hypothetical L071 equality F on the identical marked K3 product with common metric, integral c_1=0, ch_2=-14e_1-21e_2-tau_D, k=(-4,-2,1,2), G=F tensor p_1^*L^{-1} with L150's preferred metric, and L147's rank-24 M on U=B minus the finite possibly empty Z. Only the Chern connection on U is the target; no conclusion across Z is included.

The universal primitive Hodge realization gap and equality-kernel
existence remain open. The proposed intermediate input would control
the differential equation of the *given* harmonic connection on U.
A positive answer could support a later attempt combining audited
L149/L150 with a surface removal theorem and L147's exact sheaf data.
Neither that curvature application nor a removable-singularity or
positivity argument is part of this proposal. F and nonempty Z are
not established.

## Three mechanisms compared

1. Arbitrary-metric central evaluation and scalar variation remain
   parked in ATTEMPTS/086. Their unevaluated weighted harmonic
   correction is not removed by the completed criterion audit.
2. Automatic extension from a reflexive sheaf or a punctured metric
   remains unsupported in ATTEMPTS/066; ATTEMPTS/063 also records the
   missing actual metric compatibility in the singular-quotient route.
   Neither is reopened by a source theorem with unmatched hypotheses.
3. Select connection preservation *only on U*, using the preferred
   coefficient and testing the index/transform theorem's precise
   connection construction. This is a different obligation from
   central-block evaluation or automatic extension. The target has
   its own decisive hypothesis and connection-identification tests.

## Reuse and essential missing comparison

Reuse the inspected theorem and proof-case record in
`2026-10-05-six-charge-direct-image-polystability.md`, including its
[published author scan](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6)
and [Nahm-transform discussion](https://arxiv.org/pdf/math/0312045v1#page=3).
The October 23 `2026-10-23-twisted-preferred-metric-central-test.md`
explicitly records the IT obstruction at Z; retain it. These are
previously inspected references, not freshly verified theorem claims
for this proposal. Locate and inspect only the essential primary
hypotheses and connection construction needed to decide the changed
scope before retrieving larger passages or making a mathematical
specialization. An unread localization or metric-identification lead
must remain labeled unread.

Essential continuation inputs: L071's compatible kernel assumptions,
L094's fixed HE line metric, L147's stable-open concentration and
ordinary bundle, L148's specified harmonic metric, and audited L150's
preferred metric convention. Audited L149 is downstream curvature
motivation, not an input proving connection preservation. The earlier
L056/L073 constructions are comparisons of technique and do not
import their different coefficient or whole-base IT conclusions.
No cross-notebook input is proposed; full matching Mathlib coverage
is not checked.

Continue only if the inspected primary theorem/proof supplies, or
leaves an explicitly assessed specialization proving, the instanton
connection on this actual harmonic Hermitian holomorphic bundle over
U. Check source compactness separately from target compactness and
retain every needed induced-complex-structure IT hypothesis. A theorem
giving merely some compatible connection on the same holomorphic
bundle does not identify the metric in this target. If localization
or actual metric compatibility fails, record that precise obstruction
and park the dependent removal application. No whole-base IT, real
structure on G, nonempty Z, or global polystability may be inserted.

At invocation start this proposal had been saved after the completed
step-484 mathematical audit as REVIEW_REQUIRED. The separate source
comparison below now approves coverage without rejecting or relabeling
that completed audit.

## Completed primary comparison — step 485

This section supersedes the proposal's REVIEW_REQUIRED decision, while
preserving its target and all prior stops. No lemma, mathematical script,
new curvature calculation or application to the conditional F is made.
The rational Hodge target remains the version already checked in
`foundations/01-target-and-scope.md` on this date; no target change is made.

**Published localization and rotation scope.** Read the primary
[BBHR published scan](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5)
at the locations in SOURCE_EVIDENCE, including both lemma proofs and
the descent passage before Theorem 3. Section 3.1 explicitly makes X
compact; it does not impose compactness or completeness on Y.
Section 3.3 asserts that the fibre cohomology is independent of induced
complex structure and transfers IT to the twistor projection in Lemma 1.
Lemma 2 is a *natural holomorphic Hermitian* comparison. The following
passage descends the same index connection and proves preservation.
Thus this is stronger than existence of an unrelated instanton on the
same holomorphic bundle. These are imported source statements, not
new rotation or localization theorems established here.

**Metric and connection construction.** Read
[Bartocci–Jardim, math/0312045v1](https://arxiv.org/pdf/math/0312045v1#page=4),
Theorem 2 and its proof on p. 4. The theorem has no target compactness
requirement and constructs the connection by orthogonal projection
onto Dirac kernels. The higher-image reformulation, Theorem-Definition
3 on p. 5, does assume both manifolds compact; it is therefore not the
standalone localization input. Its following remark allows reducibility.
The discussion on p. 6 expressly distinguishes a noncompact target's
finite-energy question from preservation itself. We do not obtain
finite energy or removal from this theorem.

For the general product, read the author-hosted notes by U. Bruzzo,
D. Hernandez Ruiperez and C. Tejero Prieto, *Introduction to
Fourier-Mukai and Nahm transforms with an application to coherent
systems on elliptic curves*,
[Sections 3.2–3.4, PDF pp. 21–24](https://mat.usal.es/ruiperez/Site/Papers_files/DerCatCohSyst3-v4.pdf#page=21).
Section 3.2 restricts the fibre L2 product to the Dirac realization.
Section 3.3 generalizes this construction to a proper submersion and
then X compact Kahler, Y Kahler, with an arbitrary Hermitian holomorphic
kernel Q on X times Y. The text immediately after Theorem 3.4 explicitly
identifies the induced connection as Chern; Theorem 3.5 identifies its
holomorphic higher image. Section 3.4 Theorem 3.7 preserves the
quaternionic-instanton condition for this Nahm transform. Use the
published BBHR proof as the primary preservation input and these author
notes to clarify its metric interpretation, without assuming Q universal.
Do not interpret the abbreviated 'trivial connection' wording in the
2003 proof as a global flat trivialization of a nontrivial kernel.

The notes contain a parity inconsistency: Definition 3.3 defines odd
IT by vanishing of even higher images, whereas Theorem 3.4 prints
'even IT' next to ker D=0 and the odd-image cokernel. Do not import
that printed parity label. State the actual endpoint vanishings and
Dirac chirality explicitly, using BBHR Definition 2 and the 2003
odd-IT formula. This is a source-text qualification, not a new lemma.

## Exact later specialization and stopping test

The inputs named in SCOPE and in the proposal are unchanged. L094
fixes the HE metric on L; L071 supplies the actual compatible product
connection on the hypothetical F. L147 proves endpoint vanishings
and rank 24 on U, with derived dimensions (1,26,1) at split parameters.
L148 specifies the natural higher-image identification and actual
harmonic L2 metric. L150 fixes precisely the dual HE twisting metric.
These are existing local inputs, not consequences of the transform
source review. L056 is only a technique comparison with a different
coefficient. L149 is downstream motivation, not a preservation premise.

The later mathematical attempt must:

1. Match the fixed line connection and its dual, the kernel connection,
   source metric and simultaneous induced structures to the theorem.
   Check the line's full triple orthogonality/ASD hypothesis rather
   than substituting degree zero for hyperholomorphicity.
2. Set source X=S_1 and target Y=U, with the restricted actual kernel
   and preferred source coefficient. Check properness of the product
   projection despite the open target. Retain L147's endpoint
   vanishings at every point of U and invoke the inspected rotation
   statement with its Hermitian-instanton hypotheses verified.
3. Match the positive rank-24 Dirac realization, its L2 product, and
   the natural holomorphic Hermitian comparison with L148's actual
   harmonic metric. Keep the alternating index sign distinct from
   that positive bundle. Use the Chern identification for that metric,
   not uniqueness of HE metrics on the noncompact target.
4. Only after these checks apply preservation and the four-real-
   dimensional quaternionic-instanton/ASD identification at the
   original base metric. No real structure on G is required by the
   inspected Hermitian transform theorem and none may be invented.

This is an assessed applicability task, with no need to reprove the
transform theorem. Continue only if all four identifications hold.
A genuine failure in the line, rotation or actual-metric identification
must be recorded precisely and parks the dependent removal application;
an arbitrary alternative metric or abstract holomorphic isomorphism
cannot repair it. The inspected sources leave no essential unread lead
for this bounded task. The book *Fourier-Mukai and Nahm Transforms*
(2009), Chapter 5, was located but not read and is not an input;
search snippets and non-author mirrors are not evidence used here.

ATTEMPTS/063 and /066 concern unsupported singular/automatic extension;
this review supplies no such theorem. ATTEMPTS/086's arbitrary-metric
stop remains. If Z is nonempty the full-base IT obstruction remains;
if it is empty U=B and no puncture is present. The proposed result
would control the given connection only on U. A later application of
audited L149/L150, surface removal, positive extension, Chern inequality
or split-set count needs its own exact target and assessed coverage.
Kernel existence, nonempty Z, reconstruction, transport and universal
primitive Hodge realization remain unresolved. Mathlib coverage of the
full transform theorem and this metric specialization is not checked.

Queries actually run included `"hyperkahler" "Nahm" "projection"
"connection" kernel L2 Bartocci`, `"A hyperkahler Fourier transform"
"index" connection`, and `Bartocci Bruzzo Hernandez Ruiperez
"Fourier-Mukai and Nahm Transforms" pdf`. Essential passages above
were opened directly after locating them; irrelevant Fourier-transform
search results were not used. A misspelled author-scan URL failed;
the correctly spelled published scan and author notes were accessible.
No source blocker remains and no novelty inference is made.
