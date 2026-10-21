# Minimum product pair — relative-cohomology literature assessment

TARGET: Test whether relative cohomology and Grothendieck–Riemann–Roch obstruct a slope-polystable locally free rank-two bundle with c_1=0 and L048's fixed mixed character at corrections (-9,-10).
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped searches found the earlier index/factor tests and Fourier–Mukai comparison; bounded external searches for K3 rank-two product bundles, higher direct images, WIT and relative GRR found supporting general theorems but no inspected theorem deciding this fixed pair. Exact queries and scope comparison appear below.
SOURCE_EVIDENCE: Inspected Stacks Lemma 36.30.1 (0A1H), Lemma 36.31.3 and its full proof (0BDH), and Section 42.66 (02UO); checked Fulton, Intersection Theory, second edition (1998), Theorem 15.2, pp. 286–287, and Example 15.2.8, pp. 291–292, https://djvu.online/file/87GFN2nbfbdF7. Reuse the assessed surface stability/duality/HRR and Maciocia statements identified below.
COMPARISON: Perfect base change and the single-degree local-freeness criterion cover the direct-image passage once fibre concentration is verified; relative GRR gives its alternating character. L052 supplies all-fibre stability for this pair, whereas L048–L049 test only indices. Fourier–Mukai equivalence is not assumed, so its stronger classification results cannot be imported unconditionally.
GAP: In a separate mathematical turn verify fibre concentration everywhere, identify the actual first higher direct image and rank, compute its full relative character from L048, and compare with finite-rank Chern identities; neither contradiction nor compatibility has been calculated here.
REASON: Essential unread base-change and relative-GRR coverage is now inspected. Import the general theorems and specialize only to this fixed projection and character; no known general theorem needs reproof and no novelty is claimed.
SCOPE: Only the fixed minimum pair (-9,-10) on L044's S x S at Omega=p_1^*h+p_2^*h, projecting to the second factor with c_2=5 fibres; no arbitrary correction region or transverse transport.

## Gap, intermediate target and decision test

The universal main gap remains algebraic realization of every primitive
rational Hodge class, already open on arbitrary fourfolds. The local
route lacks a common product bundle carrying the prescribed mixed
action, before stability and transverse transport could be used.

The intermediate target is the saved relative-cohomology test. Its
plausible downstream use is to exclude or retain the minimum pair as
an input for a global construction. A contradiction would preserve
L053's individual factor existence and L050's topological realization.
Compatible identities would supply no product bundle and would end
this obstruction test. Neither outcome supplies a Hodge counterexample.

Continue with one mathematical application if all-fibre cohomology
concentration justifies an actual locally free direct image and its
rank/Chern test is decidable. If concentration fails, record the failed
premise rather than treating a virtual pushforward as a bundle. If the
finite-rank identities agree, stop this test without repeating the
settled index filters. Broader corrections require their own review.

Essential input IDs: L044, L048, L051, L052 and L053. Read L048 and
L051 in full, L052 through its factor-stability and exact zero-slope
lattice argument, and L053's hypotheses and existence conclusion.
L044's metric and tensor conventions are retained through their
explicit restatement in L051–L052; no chamber recalculation is needed.
Compatible global realization, product stability, transverse transport
and universal primitive-Hodge algebraicity remain independent gaps.

## Hypotheses and reused coverage

Let S be precisely L044's smooth projective complex K3, h its real
Kahler class, X=S x S and pi=p_2. The hypothetical F is holomorphic
locally free, rank two and slope-polystable at p_1^*h+p_2^*h, with
TARGET's cohomological Chern data. Serre's GAGA theorem allows treating
F as an algebraic vector bundle on the projective X. The real h is
used for stability, not as an algebraic line bundle in base change.

L051's curvature argument treats every j_y, not merely generic fibres.
L052 explicitly reuses that coefficient-independent passage for every
pair in its hypotheses. Its minimum-pair conclusion excludes split
factor restrictions with second Chern numbers 5 and 6. Thus the
all-fibre stability premise is already local input, not a new
restriction theorem. L052 equation (4) records stable factor
cohomology: H^0=H^2=0 and h^1=c_2-4. The next proof must apply these
facts to the specified projection, retaining every fibre.

Reuse [the factor-restriction assessment](2026-10-04-corrected-rank-two-factor-restrictions.md):
Verbitsky, arXiv:math/0107182v10, Theorem 3.9 and Proposition 3.7/Lemma
3.8, pp. 12–14; Huybrechts, *Lectures on K3 Surfaces*, author-hosted
draft, Chapter 1 equations (2.5)–(2.6), Proposition 2.4, pp. 11–13;
Chapter 9 Section 3.1, pp. 175–176, and Theorem 4.9, p. 182.
Use the stable hyperholomorphic criterion after excluding product
line splitting. Ambient stability alone does not imply restriction
stability. No renewed individual-factor existence search is needed.

## Inspected primary theorems

**Perfect base change.** [Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
assumes a morphism f of finite presentation, a perfect object E, and
a bounded complex G of finitely presented modules, flat over the
base with proper support. It states that Rf_*(E tensor^L G) is perfect
and commutes with arbitrary derived base change. The proof separates
its Noetherian case from approximation. Here pi is smooth projective,
its base is Noetherian, F is coherent and base-flat, and its support
is proper; take E=O_X and G=F[0]. This theorem alone does not say that
each R^i pi_*F is locally free.

**Single-degree local freeness.** [Stacks Lemma 36.31.3, in Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
states that for a perfect K and integers i,r there is an open locus
where K is a locally free rank-r module placed in degree i. A morphism
factors through this locus exactly when its derived pullback has that
property. Read the full proof: other fibre Betti numbers vanish on
an open locus, and the finite-free complex criterion gives concentration
and local freeness there. This is the required case rather than flat
base change alone. The next application must check concentration at all
closed fibres, use this open locus on the finite-type complex base,
and retain arbitrary derived base change for the concentrated complex.

**Relative GRR.** Fulton, *Intersection Theory*, second edition (1998),
[Theorem 15.2, pp. 286–287, and Example 15.2.8, pp. 291–292](https://djvu.online/file/87GFN2nbfbdF7),
gives GRR for a proper morphism of nonsingular varieties, and the
smooth relative formula ch(f_!alpha)=f_*(ch(alpha) td(T_f)).
The theorem's quasi-projective factorization case covers X and S.
Import it with f_! the alternating coherent higher-direct-image
class, then pass through the rational cycle-class map. The scan host
labels the book 1997; edition and printed pagination follow the
inspected second edition, 1998, as in the earlier assessment.

[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO)
states the same formula for smooth proper f, finite locally free
input, and finite locally free higher direct images. It postpones
the general proof, so Fulton is the theorem citation. In the future
application retain the alternating sign and T_{X/S}=p_1^*T_S.
L048 supplies the K3 Todd terms and forced character, including the
transcendental contribution to the mixed square. No evaluated relative
character or obstruction is calculated here.

Stacks statements were inspected online on CHECKED with stable tags.
General theorems are imported, not reproved. Finite-rank truncation
and character expansions reuse L048's inspected Fulton Theorem 3.2(a)
and Stacks Tags 02TZ and 02UM.

## Comparison, duplicates and recorded failures

Reuse [the fourth-character assessment](2026-10-03-rank-two-fourth-chern-test.md),
which read Maciocia, *Rank Two Fourier–Mukai Transforms for K3 Surfaces*,
J. Geom. Phys. 118 (2017), 192–201, accepted manuscript,
[Theorem 0.1, Proposition 1.1 and Theorem 2.5, pp. 2–5](https://www.pure.ed.ac.uk/ws/portalfiles/portal/30370169/Rank_Two_Fourier_Mukai_Transforms_for_K3_Surfaces.pdf).
These classify equivalence kernels under extra line-subsheaf,
determinant and acyclic-line hypotheses; Theorem 2.5 uses a product-line
extension of a twist of I_Delta. Its character computation applies to
that ansatz. TARGET assumes neither an equivalence nor that presentation,
so those stronger results do not decide it. The general direct-image
test is available without those assumptions.

Scoped searches in drafts/literature, foundations, history and ATTEMPTS
located no prior completed test of this relative direct image.
L048–L049 test indices, L050 topology, L051–L052 factor necessity,
and L053 individual existence; none performs this calculation.
The previous fixed-K-class, uncorrected Bogomolov, symmetric, boundary
and rank-divisible-presentation stops retain their scopes and evidence.
History 100's proposed continuation is this target, not its solution.

Exact external queries on CHECKED included:

- site.stacks.math.columbia.edu cohomology base change locally free constant dimension higher direct image
- site.stacks.math.columbia.edu Grothendieck Riemann Roch proper smooth varieties pushforward
- site.stacks.math.columbia.edu "36.32.2"
- "K3" "rank two" "higher direct image" bundle product
- "K3" "stable" "c_2=5" bundle Fourier Mukai family obstruction
- "K3" "rank two" "cohomology" "product" Maciocia
- "K3" "rank two" "direct images" stable bundles
- "K3" "rank two" "c_1=0" "product" bundle obstruction
- "K3" "higher direct image" "Grothendieck" bundle
- "K3" "WIT" "rank two" "Maciocia"
- "hyperholomorphic" "rank two" "product" "K3"
- "K3" "rank two" "Riemann-Roch" "direct image" bundle
- "K3 surfaces" "families" "rank two" "obstruction" Fourier Mukai

Hits about Fano threefolds with c_1=1, Nahm-transform examples and
moduli/derived-equivalence constructions are discovery leads only.
Their full statements were not inspected or imported, and snippets
supply no theorem evidence. Failed searches imply no novelty.
No essential source remains blocked for this bounded application.

## Outcome and Mathlib

This is LITERATURE / EXPLORATION / NOVELTY_UNCHECKED: a new completed
source comparison, not a mathematical exclusion. SPECIALIZE approves
the exact TARGET for a separate REPRODUCTION attempt. No lemma,
mathematical script or argument-overview change is made. Mathematical
exploration usage stays zero; no candidate solution, additional
algebraic class, enlarged span or transverse surface is supplied.

Mathlib coverage of a full matching obstruction and supporting coherent
base change/relative GRR: **not checked**. No absence claim is made.
The inspected sources are supporting theorems, not a matching evaluated
result.
