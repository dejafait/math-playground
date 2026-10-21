# Equality-family classifying map — finiteness source coverage

TARGET: Assess whether L097's whole projective classifying morphism is finite onto its reduced image, using L095's actual derivative off L096's finite reducible locus.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused L064's two ready natural-tangent/image assessments; searched stable coarse-moduli Ext1 and proper finite-fibre/quasi-finite criteria, including isolated fibre points and the closed-point/all-points distinction. Targeted L095/L096/L097 and histories 245--252 plus ATTEMPTS/061 reveal no duplicate whole equality-family finiteness result; queries and inspected primary passages are recorded below.
SOURCE_EVIDENCE: Huybrechts--Lehn (1997) Theorem 4.5.1 with complete etale-slice proof and Corollary 4.5.2, printed p. 101; Biswas--Schumacher math/0605589v1 Section 3 Lemma 3.3, its preceding arbitrary-Hermitian-family setup and Proposition 3.4 with stability setup/full proof, printed pp. 7--8; Stacks 0B2G, 02G4, 02V5, 01TH, 02NG, 01TI, 01W6, 02OG, 02LS, 056B and 035D statements/relevant proofs; reused exact GAGA and kernel-ideal coverage from L064's audit assessment.
COMPARISON: The known natural stable tangent theorem, curvature representative formula and scheme finiteness/image criteria cover the tools needed; the changed stable/split family's actual derivative and exceptional fibre remain application obligations. L064's full charge-seven conclusion is not imported, and no coarse derivative statement at a split point is covered.
GAP: Separately identify L095's real harmonic derivative with the actual complex family Ext1 class on the stable open, justify quasi-finiteness at all scheme points including the finite exceptional fibre, and apply properness/finiteness plus reduced-image factorization to L097's actual map. No finiteness result is derived in this review.
REASON: Essential changed-scope source coverage is now available; perform one separate cited mathematical application, with no reproof of general deformation, harmonic-representative or scheme theorems and no originality claim.
SCOPE: Only the hypothetical rank-two locally free Omega-polystable F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D on the identical marked K3 product; retain L097's H and possible nonempty finite reducible set.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the earlier all-stable family to a charge-fourteen stable/split family; exact exceptional-fibre and actual raw-derivative comparison coverage was missing.
COVERED_TARGET: Assess whether L097's whole projective classifying morphism is finite onto its reduced image, using L095's actual derivative off L096's finite reducible locus.

## Target, use and discriminating test

The main gap is universal primitive rational Hodge realization. This
intermediate test could supply a controlled global image for the
equality-family route. The discriminating threshold is finiteness of
the actual whole map onto its reduced image, including the fibre over
[L plus L^{-1}]. Continue only if the natural stable derivative and
all-points quasi-finiteness checks succeed under the retained inputs;
otherwise isolate the failed passage and narrow the result. No coarse
injectivity or unramifiedness at a reducible point, global injectivity,
normality, degree-one statement or embedding is approved.

F existence, integrated germs, separation and transport remain
independent unresolved gaps. Coverage approval is not proof verification
or a complete candidate solution. This is a literature-only step.

## Reused coverage and inspected primary sources

The assessments
[2026-10-06 charge-seven application](2026-10-06-charge-seven-finite-unramified-map.md)
and [2026-10-07 critical audit](2026-10-07-charge-seven-finite-unramified-critical-audit.md)
already cover natural coarse deformation, exact analytification,
projective coherent-cohomology comparison, Dolbeault comparison and
image kernel ideals. Reuse those general inputs under their unchanged
hypotheses; do not import L064 as a theorem about this different F.

Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*, Aspects
of Mathematics E31 (1997 text, 281-page PDF),
[Theorem 4.5.1 and Corollary 4.5.2, printed p. 101 / PDF page 113](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113),
were inspected, including the complete proof. For a stable sheaf the
completed coarse local ring prorepresents its deformation functor;
the tangent is naturally Ext^1. The proof begins with the family
classifying transformation and obtains its inverse from an etale
slice and the restricted Quot family. Scalar automorphisms and absence
of a global universal sheaf are allowed by the already assessed stable
PGL quotient in 4.3.2/4.3.5. The theorem does not provide this tangent
identification at strictly semistable points. The numerical-class part
must retain L097's open-and-closed local scope. No fixed-determinant
tangent substitution or moduli smoothness is needed.

The reused analytic/algebraic bridge is Serre, *Geometrie algebrique
et geometrie analytique*, Ann. Inst. Fourier **6** (1956),
[sections 9, 11--13, Proposition 10 and Theorem 1, printed pp. 16--22](https://www.numdam.org/article/AIF_1956__6__1_0.pdf#page=19),
and the named Dolbeault theorem. It applies to the projective fibre
S_1 and coherent End(E_y), retaining the same first-order extension
and its central identification. Its detailed inspected evidence is in
the reused audit assessment; no repeated general GAGA proof is needed.

Biswas--Schumacher, *Geometry of moduli spaces of Higgs bundles*,
[arXiv:math/0605589v1, 22 May 2006, Section 3, printed pp. 7--8](https://arxiv.org/pdf/math/0605589v1#page=7),
was inspected from the setup preceding Lemma 3.3 through Proposition
3.4's complete proof. For a holomorphic family with a smooth Hermitian
metric, Lemma 3.3 represents the family Kodaira--Spencer class by the
covariant Higgs derivative and mixed Chern-curvature contraction.
At zero Higgs field this supplies the ordinary-bundle curvature
representative. Proposition 3.4 adds stable fibres and their HE
metrics, and obtains harmonicity using the adjoint formula and the
differentiated HE equation. Use the representative formula on the
stable open with the actual given metric; audited L095 already supplies
raw harmonicity. Import no stable-family theorem at split parameters.
The real-to-(0,1) comparison still needs a local applicability check
with L095's quaternionic convention and skew-adjoint reality condition.

## Scheme criteria: statements and essential proof cases

The following online Stacks statements/proofs were inspected on
2026-10-13; tags fix the references independently of chapter numbering.

- [0B2G, Lemma 33.16.8](https://stacks.math.columbia.edu/tag/0B2G):
  for schemes locally of finite type over a base, equality of residue
  fields at x and f(x) makes tangent injectivity equivalent to being
  unramified at x. Its proof uses the cotangent exact sequence and
  relative-differential vanishing. Apply this only with the checked
  closed complex-point residue fields on the stable open.
- [02G4, Definition 29.36.1](https://stacks.math.columbia.edu/tag/02G4)
  defines unramifiedness on affine neighborhoods, hence an open locus;
  [02V5, Lemma 29.36.10](https://stacks.math.columbia.edu/tag/02V5)
  gives quasi-finiteness at each unramified point. The cited algebra
  proof is already covered by the ready application assessment.
- [01TH, Lemma 29.21.6](https://stacks.math.columbia.edu/tag/01TH)
  equates quasi-finiteness with isolation in the fibre for locally
  finite type morphisms. Its proof checks affine fibre rings and the
  Jacobson property. [02NG, Lemma 29.21.7](https://stacks.math.columbia.edu/tag/02NG)
  requires local finite type and a finite underlying full fibre;
  that fibre is discrete and all its points are quasi-finite. The
  proof uses finite Jacobson spaces and 01TH. Nilpotent thickness
  is allowed; finitely many closed points without a full-support
  justification is not its hypothesis.
- [01TI, Lemma 29.57.2](https://stacks.math.columbia.edu/tag/01TI)
  makes the quasi-finite locus open, using the affine algebraic
  Zariski Main Theorem. It covers an alternative all-points passage
  once quasi-finiteness has been checked at every closed source point.
  Any use of closed-point density must retain finite type over C.
- [01W6, Lemma 29.42.7](https://stacks.math.columbia.edu/tag/01W6)
  makes a morphism from a proper base-scheme to a separated base-scheme
  proper. Its proof factors through the closed graph and a proper
  base change. [02OG, Lemma 30.21.1](https://stacks.math.columbia.edu/tag/02OG)
  gives finite iff proper with finite fibres over a locally Noetherian
  target; its proof uses formal functions and an affineness criterion.
  Closed fibres alone cannot be substituted into that statement.
  Prefer [02LS, Lemma 37.44.1](https://stacks.math.columbia.edu/tag/02LS):
  proper local quasi-finiteness implies finiteness, with no Noetherian
  addition. Its proof isolates finite fibre pieces after etale base
  change, removes the complementary piece by closedness, and descends.
- [056B, Lemma 29.6.7](https://stacks.math.columbia.edu/tag/056B)
  identifies the scheme-theoretic image of a reduced source with the
  reduced induced structure on the image closure. Its proof uses
  the minimal closed factorization. The quasi-compact kernel-ideal
  description in [01R5, Lemmas 29.6.1/29.6.3](https://stacks.math.columbia.edu/tag/01R5)
  is reused from L064's assessment. [035D, Lemma 29.45.14](https://stacks.math.columbia.edu/tag/035D)
  makes the first factor finite if its composite is finite and the
  second factor separated; the proof uses a closed graph and finite
  base change. A closed immersion of the image meets that criterion.

## Exact approved application and remaining obligations

Carry audited L095, audited L096 and audited L097 with L071's fixed
connection/metric scope. Set U equal to the exact stable-open preimage
in L097. Check the same pulled-back dual-number family under the
natural coarse Ext^1 identification and the GAGA/Dolbeault comparison.
Match its class to L095's mixed-curvature representative; justify
complex injectivity from real harmonic injectivity using the actual
quaternionic action and skew-adjoint reality. An arbitrary isomorphism
of tangent dimensions does not suffice. Restrict the tangent theorem
to U; no reducible coarse tangent is an input.

Verify finite type, separation and properness for the actual whole
map. Check quasi-finiteness on U at all scheme points, using the
closed-complex-point criterion and openness with the required density.
At the remaining parameters, check the full underlying fibre over
[L plus L^{-1}] against L097's exact stable-open preimage and L096's
finite set before using 02NG. Allow Z empty and do not require that
exceptional fibre be reduced. Apply a whole-map finiteness theorem
only after this check. Define the actual reduced image, justify
factorization, its finiteness and surjectivity separately, and avoid
normality, flatness, degree or embedding conclusions.

These are obligations for one later proof attempt, not a completed
specialization. Known theorems cover the general tools, so no reproof
is justified. No essential source remains blocked for this scope.

## Search record, duplicates and preserved stops

Queries were `site.stacks.math.columbia.edu proper quasi finite finite
fibres tangent injective unramified 0B2G`; `Huybrechts Lehn Corollary
4.5.2 tangent stable sheaf Ext1 natural Kodaira Spencer classifying
morphism`; `site.stacks.math.columbia.edu quasi finite at x isolated
point fibre residue finite type 01TI`; and
`site.stacks.math.columbia.edu proper finite fibres closed points
Jacobson quasi finite`. Discussion sites/search snippets were locators
only. All essential new scheme passages and the natural tangent and
curvature statements above were read in primary sources. No unread
lead is essential, and failed searches do not establish novelty.

Narrow local reads compared L064's natural-tangent/image passages and
its two assessments with L095's all-fibre harmonicity and quaternionic
convention, L094's real/Dolbeault bridge, L096's finite-set statement,
and L097's whole-map/stable-open scope. Histories 245--252 preserve the
finite-locus, placement and audit steps, not a whole-map finiteness
proof. ATTEMPTS/061's compatible quadratic tangent stops the earlier
local exclusion only; the index-curvature and strict-Euler stops also
remain intact. No cross-notebook input is used. The comparison changes
source readiness, not the mathematical argument or cycle span.

## Mathlib

Full matching coarse-sheaf tangent comparison and combined conditional
whole-image finiteness: not checked. No matching declaration or absence
claim is made; supporting formalization is not a completion gate here.
