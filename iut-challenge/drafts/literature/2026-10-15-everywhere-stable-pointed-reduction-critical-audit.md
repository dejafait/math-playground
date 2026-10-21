# Everywhere stable pointed reduction — critical-audit coverage

TARGET: Critically audit L062's everywhere stable one-pointed reduction over unchanged F, including small residue characteristics, geometric nonsplit nodes and whole-DVR pointed ampleness.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read full L062 and the completed 2026-10-15 application assessment; compared the 2026-10-12 L051 and 2026-10-11 L049 audit assessments, scoped input statements, histories/162,171,230,231 and ATTEMPTS/028. Reuse recorded general-Weierstrass/small-characteristic and Stacks searches; no fresh external search or primary retrieval was needed.
SOURCE_EVIDENCE: Reuse inspected Conrad, Minimal models for elliptic curves (21 November 2015), section 2 pp.2,6 and Theorem 5.5/proof pp.14–16; Milne, Elliptic Curves second edition (2021), II.3 pp.59–61; Hassett math/0205009v1 section 2 pp.2–3; precise live Stacks statements/proof cases recorded in the L051 audit assessment. References and hypothesis comparison below.
COMPARISON: Existing coverage includes general a_i, residue characteristics 2,3, geometric nonsplit nodes and relative Cartier duality without regular total space. The proposed audit changes no source hypothesis and requires no new general theorem. L062 adds the all-completion application whose computations still need independent mathematical checking.
GAP: Coverage is sufficient for exactly TARGET; the verdict on actual flat models, geometric fibers, smooth Cartier origins, whole-DVR Z=3S, duality and ampleness is deferred. Independent initial-data conditions and original finite B>=A remain open.
REASON: SPECIALIZE already assessed standard inputs to critically check the existing application, with repairs or narrowing only within this scope. This is coverage approval by reuse, not a new mathematical input or an audit pass.

LITERATURE_REASON: The saved continuation was REVIEW_REQUIRED and required a separate audit-specific coverage comparison; no changed source or essential unread theorem was found, so further retrieval would repeat adequate coverage.
SCOPE: Exactly TARGET for L062 with L049,L051 and inherited L045,L048, unchanged E_0,F,origin and retained packet; no new curve, field, reduction theorem or numerical bound.

Essential local inputs are L062 and its direct inputs L049,L051, with
inherited L045,L048. Retain exactly the same E_0,F,origin, fixed precision,
K_glob and embedded H,N,q_0 data. No need to reopen the source-blocked
F_mod retrieval, the coordinate mechanism, or ATTEMPTS/027,028,030,031.
Native field/rho and independent initial-data predicates remain
conditional; no actual input/action, pilot, essentiality or finite
B>=A conclusion follows even if the audit passes.

## Completed scope comparison — 2026-10-15

The application assessment `2026-10-15-everywhere-stable-pointed-reduction.md`
in this directory records prior queries, inspected primary statements
and proof cases, strongest relevant conclusions and access limitations.
Those records and the L049/L051 audit assessments are reused here;
none is represented as a fresh primary retrieval.

1. [Conrad, *Minimal models for elliptic curves*, 21 November 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
   section 2 and Theorem 5.5/proof pp.14–16, cover integral pointed
   minimal Weierstrass models over a DVR and the smooth-locus/Neron
   bridge. The prior inspection includes good versus multiplicative
   reduction, node/cusp distinction, small characteristics and splitness.
   [Milne, *Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
   II.3 pp.59–61, covers general equations and finite Q_p-extensions.
   L062's audit therefore needs no short-form square test excluding
   2,3 or new split-reduction theorem. It must check the actual local
   minimal equation and its pointed generic identification.
2. `2026-10-11-global-semistability-critical-audit.md` covers L049's
   [Silverberg–Zarhin (1995), Theorem 3.5 p.406 and Definition 3.1 p.405](https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf)
   import. Semistability permits nonsplit tori and does not itself
   verify a stable pointed Weierstrass family. L049's completed audit
   is reused. L051's completed audit verifies its original cubic above
   3, not L062's application to general equations elsewhere.
3. [Hassett, arXiv:math/0205009v1, section 2 pp.2–3](https://arxiv.org/pdf/math/0205009v1)
   gives the weight-one family definition over a noetherian base,
   without excluding small residue characteristics: proper flatness,
   connected nodal geometric fibers of fixed arithmetic genus, smooth
   marking and relative ampleness. A nonsplit node is tested
   geometrically, without a splitting extension. This definition
   supplies the test, not a verdict on L062's checks.
4. `2026-10-12-native-all-place-critical-audit.md` records the relative
   hypotheses and relevant proof cases for [Stacks 0A9W](https://stacks.math.columbia.edu/tag/0A9W)
   (projective-space right adjoint), [0A9X](https://stacks.math.columbia.edu/tag/0A9X)
   and [0AA4](https://stacks.math.columbia.edu/tag/0AA4) (pseudo-coherent
   closed immersion and Cartier formula), [0ATX](https://stacks.math.columbia.edu/tag/0ATX)
   (composition), [0E6N](https://stacks.math.columbia.edu/tag/0E6N)
   and [0E6R](https://stacks.math.columbia.edu/tag/0E6R) (relative curve
   dualizing sheaf and Gorenstein base change). The noetherian,
   proper finite-presentation, flatness, Cartier and fiber hypotheses
   remain obligations; regular total space is not required. Changing
   coefficients changes the local verification, not these theorem
   hypotheses. Check the global sheaf computation and shifts rather
   than substituting fiberwise adjunction.
5. The same assessment covers [Stacks 01XT](https://stacks.math.columbia.edu/tag/01XT)
   for projective-space cohomology and [01VG](https://stacks.math.columbia.edu/tag/01VG)
   with [01PT](https://stacks.math.columbia.edu/tag/01PT) for positive
   tensor powers and relative ampleness. L062's section,
   nonzerodivisor arguments and whole-DVR divisor identity remain
   independent audit obligations; no new divisor computation occurs here.

No duplicate completed L062 audit appears in the scoped application
and history records. L049 and L051 are narrower audited inputs.
ATTEMPTS/028 concerns different descent models at a moduli completion
under a different quantifier; it does not test fixed X_F over F_t.
Preserve that stop and the distinction from regular I_n polygons.
The application assessment already compared the other parked routes;
none needs reopening. No new source gap or blocker emerged, and no
novelty claim follows from reuse.

The native predicate retains the May 2020 reproduced IUT I Definition
3.1(b), pp.61–62, qualification: author/reproduction byte identity and
agreement with the separate 2021 journal text remain unverified.
Stacks tags retain their prior live-version qualification. Full matching
Mathlib coverage remains unchecked, without an absence claim.

The discriminating audit is whether every finite F-place is covered by
the actual pointed generic identification and the minimal Weierstrass
model over its unchanged R, including p=2,3 and nonsplit nodes. Check
whole-DVR Cartier identities and duality shifts, not just fiber degrees.
A correct application removes only the everywhere stable-reduction
prerequisite; any failed hypothesis must be recorded precisely.

SPECIALIZE now approves exactly TARGET for a separate REPRODUCTION
critical audit. Import general results by citation rather than reprove
them. Repair or narrow the written application only within its unchanged
scope; an essential uncovered claim requires source review before
dependent new mathematics. This turn supplies no mathematical verdict,
new lemma or new source evidence. No lemmas/, scripts/, PROOF.md or
DAG.md modification was made.
