# Everywhere stable pointed reduction — completed source comparison

TARGET: Determine whether L049's everywhere semistability yields stable one-pointed reduction of the retained X_F at every finite F-place, as required by IUT I Definition 3.1(b).
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L049,L051 and their ready reduction/duality assessments, L059's existing minimal-model citations, history/229 and ATTEMPTS/028; searched semistable elliptic minimal Weierstrass stable one-pointed models, small residue characteristics and Neron identity components. Primary statements and relevant proof cases inspected below; no novelty inferred.
SOURCE_EVIDENCE: Conrad, Minimal models for elliptic curves (21 November 2015), section 2 pp.2,6 and Theorem 5.5/full proof pp.14–15; Milne, Elliptic Curves second edition (2021), II.3 pp.59–61; Hassett, arXiv:math/0205009v1 section 2 pp.2–3; reproduced May 2020 IUT I Definition 3.1(b) pp.61–62. Reuse Silverberg–Zarhin and the precise Stacks duality/ampleness coverage already assessed for L049,L051; direct URLs and scope below.
COMPARISON: Known minimal-model results bridge Neron reduction to smooth or geometrically nodal Weierstrass fibers without excluding residue characteristics 2,3 or requiring splitness. Known pointed stability and relative-duality inputs cover the remaining model checks. The retained all-place application is unwritten; this is source coverage, not a proof of that application or progress beyond the checked literature.
GAP: Apply these inputs at each actual F-completion, keeping the same pointed generic curve; check the general Weierstrass model's family, marking, dualizing and ampleness hypotheses. Do not assume the original integer equation is minimal at every place or substitute a regular I_n polygon for the stable pointed fiber.
REASON: SPECIALIZE standard reduction/model results and the already assessed pointed-cubic method; only the application to the retained curve and general local equations needs writing. No new general reduction theorem or reproof is justified.
LITERATURE_REASON: The expanded all-finite-place predicate required the previously unassembled Neron-to-pointed-model bridge; L049 and L051 coverage alone did not assess this scope. Reuse their adequate inputs and L059's minimal-model source rather than repeat their audits.
SCOPE: Same E_0,F and origin; every finite F-place. No F_mod computation, field enlargement, new curve, everywhere splitness assertion, theta descent or numerical comparison.

Essential inputs for the proposed continuation are L049 and L051,
with inherited L045,L048. Keep E_0/Q at fixed
M>=max(M_tors,31), F=Q(zeta_60,E_0[30]), full rational 30-torsion,
K_glob=F(E_0[7]), the embedded H subset N and places u,w, and the
changed pointed Tate parameter q_0 in Q_3 with v_3(q_0)=30 and
v_3(3)=1. Do not change the curve or parameter, identify K_glob with N,
or set F_mod=Q. The retained cover and selected-place data remain
untouched; L053's global audit is completed independently of this target.

The main gap is still finite B>=A and actual input/action/pilot/
essentiality. A positive comparison could authorize a known-result
application removing the everywhere stable pointed-reduction obligation;
it would not assemble full initial data or resolve the main gap.
Continue only with a precise theorem covering all finite residue
characteristics and the actual pointed curve. Preserve the distinction
between a regular I_n polygon and a stable one-pointed nodal model.
Do not infer absence of a stable model from lack of splitness.

This target differs from L051's all-place-above-3 argument and L049's
Neron-identity-component criterion. No duplicate completed application
was found in the scoped proofs, assessments and history.
It is independent of the parked AbsTopIII field-of-moduli retrieval
in step 217 and of ATTEMPTS/030,031. Source inspection, exact hypothesis
comparison, duplicate/failure review and approval were required in a
separate literature turn before any expanded mathematical application;
the completed review below discharges that requirement.
Full matching Mathlib coverage for this target has not been checked.

## Completed review — 2026-10-15

### Native predicate and source qualification

The [May 2020 IUT I reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf#page=61),
Definition 3.1(b), pp.61–62, was inspected through the complete clause.
It imposes stable reduction on the fixed type-(1,1) X_F at every
nonarchimedean F-place; its separate selected-place requirement is
multiplicative reduction at all F-lifts of the selected moduli places.
It does not require good reduction everywhere, a regular stable total
space, or a split node at every finite place. The native curve conventions
and pointed interpretation reuse
`2026-10-12-native-selected-place-model-comparison.md` in this directory.

The [author endpoint](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf)
again returned 186-page metadata, but its targeted text/screenshot calls
did not expose readable passages. The reproduced primary text was
read instead. Retain the existing May 2020 reproduction qualification:
author/reproduction byte identity and the distinct 2021 journal text
are unverified. The newly attempted SemiAnbd endpoint's targeted text
searches also failed; its already adequate inspected conventions are
reused, not represented as freshly retrieved. Neither source issue is
essential missing coverage for this unchanged predicate.

### Minimal-model bridge actually inspected

[Brian Conrad, *Minimal models for elliptic curves*, 21 November 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
section 2 pp.2,6, supplies integral pointed Weierstrass models over a
DVR and discriminant minimality. Theorem 5.5, pp.14–15, identifies
the smooth locus of a minimal W with the Neron identity open subgroup;
good reduction corresponds to smooth W_k, and geometric multiplicative
reduction to a node. The complete proof was read, including its
minimality argument and cusp/node distinction. Its discussion through
p.16 treats residue characteristics 2,3, imperfect fields and splitness
separately. Here residue fields are finite and perfect. The theorem is
imported, not reproved. This reuses the source identified in
`2026-10-14-retained-adjacent-cusp-critical-audit.md`, extending its
comparison beyond the retained 3-adic split case.

[J.S. Milne, *Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf#page=63),
II.3 pp.59–61, was inspected for the arbitrary-characteristic general
Weierstrass node/cusp criterion, minimal equations, reduction types and
the explicit extension of the discussion to every finite Q_p-extension.
The short-form square test excludes 2,3 and is unnecessary. A single
global minimal equation is neither supplied nor needed. L049's precise
Silverberg–Zarhin Definition 3.1/Theorem 3.5 import is reused unchanged;
no second torsion-adjunction or Raynaud proof is proposed.

### Pointed-family coverage and remaining application

[Hassett, *Moduli spaces of weighted pointed stable curves*,
arXiv:math/0205009v1 (1 May 2002)](https://arxiv.org/pdf/math/0205009v1#page=3),
section 2 pp.2–3, was reinspected completely for the family definition:
noetherian base, proper flat family with connected nodal geometric
fibers of fixed arithmetic genus, sections in the smooth locus and
relative ampleness of the weighted log canonical divisor. Weight one
is the ordinary pointed definition; the moduli theorem is over Z.
No residue-characteristic exclusion occurs in this definition.

Reuse `2026-10-12-native-all-place-critical-audit.md`, whose inspected
statements/proof cases cover the relative cubic method, without
expanding any theorem hypotheses: [Stacks 0A9W](https://stacks.math.columbia.edu/tag/0A9W)
for projective-space duality, [0A9X](https://stacks.math.columbia.edu/tag/0A9X)
and [0AA4](https://stacks.math.columbia.edu/tag/0AA4) for the closed
Cartier immersion, [0ATX](https://stacks.math.columbia.edu/tag/0ATX)
for composition, [0E6N](https://stacks.math.columbia.edu/tag/0E6N)
and [0E6R](https://stacks.math.columbia.edu/tag/0E6R) for the relative
curve dualizing sheaf, [01XT](https://stacks.math.columbia.edu/tag/01XT)
for projective cohomology, and [01VG](https://stacks.math.columbia.edu/tag/01VG)
for ampleness and positive tensor powers. Preserve that assessment's
noetherian, finite-presentation, flatness, Cartier and fiber hypotheses
and its live-tag version qualification. These are already covered;
no additional Stacks browsing is needed.

For the separate mathematical application, use a general integral
minimal Weierstrass equation at each F-place and the pointed generic
identification in the source. Verify its family and genus conditions,
smooth Cartier origin, the whole-DVR hyperplane divisor at infinity,
and relative duality/ampleness. L051's written proof supplies the method
above 3, not an automatic proof of those checks for general coefficients
elsewhere. In particular allow nonzero a1,a3 in residue characteristics
2,3. A node's nonsplit branches must be tested geometrically, without
adjoining a splitting field or changing F. No new divisor computation,
model construction or lemma has been carried out in this review.

Continue if the application meets every cited hypothesis for good and
multiplicative reduction at every finite place, over unchanged F_t.
Stop or qualify the proposed conclusion if any family/marking/ampleness
check fails or needs a field extension; a failure of the original
nonminimal equation alone is not an obstruction. A successful application
would remove just the everywhere pointed-stability prerequisite.
Full initial data, the conditional native field/rho assumptions and the
actual input/action/pilot/essentiality bridges remain independent.
No numerical bound, finite B>=A or essential IUT flaw is established.

The exact TARGET above is ready as SPECIALIZE for a separate known-method
application, classified REPRODUCTION; no general theorem needs reproof.
The original proposal's request for a separate review is discharged by
this completed literature turn. No lemmas/, mathematical scripts/,
PROOF.md or DAG.md were changed.
