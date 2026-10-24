# Opposite-coefficient trace-sign exclusion — critical-audit coverage

TARGET: Critically audit L159's opposite-coefficient harmonic map, both normalized trace signs and exclusion of the two z=0 extremal branches.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 523 compared the complete L159 proof with step-521 discovery/operator coverage, step-516/518/519 actual cup/trace coverage and step-520 audit; checked L071's retained hypotheses, L157's preferred-line/rotation-IT passage, L158's four actual edges and ATTEMPTS/069,/089,/090. No fresh external search or novelty claim; the exact scope is unchanged.
SOURCE_EVIDENCE: Reuse inspected Verbitsky alg-geom/9307008v1 (29 July 1993), Section 3 Proposition 3.2 pp. 11–12, Section 4 setup/Propositions 4.1–4.3/Theorem 4.1/Corollary 4.3 pp. 12–16 and Theorem 4.2.A doubled-dual proof p. 17, https://arxiv.org/pdf/alg-geom/9307008v1; Demailly alg-geom/9410022v3 (28 February 1995), Sections 1.A/4.A pp. 4–5/27–28, https://arxiv.org/pdf/alg-geom/9410022v3; qualified Stacks and supporting coefficient/transform coverage below. These are reused primary reads, not fresh retrievals.
COMPARISON: Known results cover parallel-real harmonic operators, the doubled-dual proof case, arbitrary locally free coefficient Dolbeault/Serre products and natural restriction/trace comparisons. They support auditing L159's specialization but do not state its extracted square, both strict normalized signs or branch exclusion; those remain separate mathematical audit obligations.
GAP: Critically verify the actual determinant/dual connections, ordinary (0,1) operator extraction, both raw-form restriction and normalized trace comparisons, separate strictness arguments and final quartic contradiction. No proof-audit verdict is established by this source review.
REASON: Separate source-scope comparison now approves exactly one bounded critical audit under SPECIALIZE; no changed hypothesis or essential unread source case was identified. Preserve the completed attempt and prior relaxation witnesses pending that audit.
LITERATURE_REASON: The newly written L159 audit required separate coverage approval after its derivation turn; this step reuses ready operator and trace assessments without refreshing unchanged sources or attempting more mathematics.
SCOPE: Exactly the full canonical L159 argument and its registered z=0 branches (12,2),(6,8), at the retained common metric and preferred dual HE connections; no other branch, positive-z extension, lower count, kernel construction or transport.

This file selects no new mathematical claim. Its startup proposal requested
a separate coverage decision for an independent critical audit of the
completed known-tool specialization. Step 523 completes that comparison
below. Its source starting point is
`2026-10-24-dual-coefficient-quaternionic-trace-sign.md`, unchanged from
invocation start. A source comparison can approve reuse if those exact
hypotheses and essential proof cases suffice. Additional retrieval
requires a specific essential uncertainty, not a search quota.

The main gap remains universal primitive Hodge realization. The local
result to audit is L159's exclusion of the two branches (12,2),(6,8)
at z=0, not nonexistence of all F or a lower count. The relevant inputs
are L071's actual hyperholomorphic connection, L157's preferred dual
line connections and L158's audited actual edges and quartic identity;
L147's M,W and L093/L153/L156 enter through those retained hypotheses.
Keep identical marked K3 factors and common g,h; locally free
Omega-polystable rank-two F with integral c_1=0 and
ch(F)=2-14e_1-21e_2-tau_D+62P; k=(-4,-2,1,2), k.h=0,
k^2=-14 eta, integral eta=1; and z=0.

The audit must inspect the complete canonical proof in
`lemmas/L159-opposite-coefficient-common-trace-sign.md`. In particular:

- Check unit determinant parallelness and both actual dual line connections.
- Match the doubled real operator to ordinary (0,1) harmonic forms using
  (-I,J,-K), then check the skew determinant identification and square +1.
- Check pullback of the raw form operator in both directions, without
  assuming harmonic restriction or choosing separate cohomology classes.
- Recompute the oriented frame identity, both normalized Serre ratios,
  and strictness from each actual edge separately.
- Check that both branches have nonzero spaces in both opposite pairs
  and that all other terms in the polarized quartic identity vanish.

A successful later audit would preserve or repair this scoped exclusion;
a substantive failed bridge must be recorded, without discarding the
completed attempt or L158's valid necessary-relaxation witness. F
existence, other branches, positive-z behaviour, independent lower
control, transport and universal primitive Hodge realization remain
unresolved. Full matching Mathlib coverage is not checked.

## Completed source-scope comparison — step 523

This is LITERATURE / EXPLORATION / REPRODUCTION; actual task type
literature_comparison. The full 311-line L159 proof was read to identify
source uses and scope, without recomputing its identities or conducting
the independent proof audit. No lemma, mathematical script, PROOF.md or
DAG.md changes. L159's scoped exclusion remains pending critical audit.

The main gap is universal primitive rational Hodge realization. The
intermediate target is the exact TARGET above. Its downstream use is
deciding whether to retain the actual-connection sign constraint as an
audited exclusion of two formally compatible kernel branches. F existence,
other branches, positive-z behaviour, independent lower split-count
control and transport remain separate gaps.

**Harmonic input.** Reuse the primary read register in
[step 521's assessment](2026-10-24-dual-coefficient-quaternionic-trace-sign.md).
Verbitsky's 1993 preprint, at the locations in SOURCE_EVIDENCE, treats
parallel real hyperholomorphic coefficients and explicitly treats general
coefficients through their direct sum with the Hermitian dual. Step 521
inspected that essential proof case. It is the relevant coverage for
checking L159, which does not assume either individual Q_s has a parallel
real involution. The compact hyperkähler product and diagonal sphere
remain the scope; no later irreducible-base cone or vanishing theorem is
imported. The printed endpoint-injection and scalar cohomology-ring claims
remain unused. The triple (-I,J,-K), tensor-product anti-linearity,
determinant identification and extracted square remain specialization
checks, not conclusions quoted from Verbitsky. No reproof of general
harmonic theory is needed or justified.

Supporting coefficient identities are available in Verbitsky,
*Quaternionic Dolbeault complex and vanishing theorems on hyperkähler
manifolds*, [math/0604303v2](https://arxiv.org/pdf/math/0604303v2),
16 September 2006, Sections 3.2–3.4, Proposition 3.3 and Theorems 3.5–3.6,
PDF pp. 14–16. Step 521 read the curvature-component and graded-Jacobi
proof cases. Their curvature term must be retained if that alternative
check is used. No changed coefficient hypothesis or essential unread
operator case was identified in this comparison.

**Metric and trace inputs.** Demailly, at the version and sections in
SOURCE_EVIDENCE, supplies coefficient Dolbeault products, compact
coefficient Hodge theory and the generalized-star Serre integral. Locally
free Q_s on X and its K3 fibres fit that scope. It does not give a
degree-one-to-degree-one map in complex dimension four, restriction
harmonicity or L159's signs. L159 claims a raw-form restriction argument;
checking it uses the actual connections and closed representatives,
rather than a missing theorem asserting restriction harmonicity.

Bartocci–Bruzzo–Hernández Ruipérez, *A hyperkähler Fourier transform*,
Differential Geom. Appl. 8 (1998), 239–249,
[Definition 2 and Section 3.3, Lemmas 1–2/Theorem 3, pp. 244–246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf),
retains the natural Dirac-metric/base-change proof cases inspected in
step 521. Its compact source, compatible spheres, Hermitian quaternionic
kernel and IT coefficient hypotheses are retained in L157/L158. It does
not make an individual signed Q_s real or identify a raw restriction with
a fibre harmonic representative. The later audit may reuse the existing
image/edge inputs without reproving preservation.

The [four-twist audit assessment](2026-10-24-four-twist-cup-critical-audit.md)
retains these direct primary sources and previously inspected proof cases:

- Coefficient products/interchange: [Stacks 20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3) and [15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN).
- Counit/base-change: [20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6) and [20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99). The latter's proof is omitted; reuse the earlier inspected counit proof, without claiming a new proof read.
- Line-valued Kunneth: [36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN), both proof cases recorded in step 516.
- Right-adjoint base change, trace and smooth-proper dualizing complex: [48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB), [48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J) and [48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT). Step 519 retrieved the complete 0BRT statement and diagonal/Koszul proof again.

These cover arbitrary derived coefficients and the smooth proper K3
projection squares here, which are Tor-independent over Noetherian
bases; the closed point itself need not be flat. Kunneth's affine base
is Spec(C). Compatibility is distinct from concentration, perfection
and strictness. L158's separately audited four degree-one edges supply
the comparison input. L159's use of each edge to find a nonzero
restriction on some fibre remains an independent audit obligation.
Dividing the Serre traces by their respective fixed nonzero generator
traces and matching common orientation/wedge conventions are specialized
checks, not unquoted positivity theorems. No general duality reproof is
needed.

**Duplicates and continuation test.** Step 521's exact/terminological
search already found the machinery without an inspected theorem stating
the two-projection strict sign. L159 stays within that assessed scope;
no new discovery is needed and no originality inference follows.
ATTEMPTS/069's unknown global entry, /089's compatible additive spectrum
and /090's compatible multiplicative relaxation remain intact. Source
approval does not invalidate L158's witness or reopen its finite filter.

Continue by auditing the complete L159 proof against the checklist above.
Retain the exclusion only if the actual dual connections, harmonic
convention, both normalized comparisons, both strictness arguments and
quartic contradiction pass. Record any substantive failed bridge or
repair canonically before reuse. If it cannot be repaired within scope,
preserve the evidence and park this sign mechanism; do not supply a
chosen matrix or broaden to unassessed branches. This review establishes
none of those mathematical conclusions.

The continuation retains L159, L071, L157 and audited L158; L147's M,W
and L093/L153/L156 enter through their stated hypotheses. All numerical
and geometric assumptions above, including z=0 and the two branches,
are unchanged. Full matching Mathlib coverage remains **not checked**,
not absent. No cross-notebook input is used. Mathematical exploration
usage stays at zero after step 522's informative negative; this literature
turn spends none.
