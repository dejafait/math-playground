# Parallel tangent summand — source coverage for one bounded test

TARGET: Test the parallel tangent summand forced by L067 against relative GRR and Riemann--Roch for R^1p_{B*}End_0(F).
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded relative-Ext/tangent, parallel-normal-bundle and stronger geodesy/Chern searches; scoped comparison of L060/L067, ready tangent/geodesy/factor assessments and ATTEMPTS/041--046. Huybrechts--Lehn Section 10.2 supplies the missing descended tangent theorem; no matching fixed-F obstruction located and no novelty inferred.
SOURCE_EVIDENCE: Huybrechts--Lehn (1997), 10.1.8/Example 10.1.9 and complete Section 10.2/Theorem 10.2.1 proof, printed pp. 220--223; Stacks 0B91, 0BDI and 36.31.3 in 0BDH, statements/relevant proofs, and 02UO; Verbitsky alg-geom/9610010v1 Proposition 4.1/Lemma 4.3 and Section 5.1--5.3 including proof, PDF pp. 21--22, 29--31; alg-geom/9307008v1 Theorems 2.2--2.3/Lemma 2.1, PDF pp. 6--7; Huybrechts K3Global draft Chapter 9 Section 1.2--1.3, equations (1.2)--(1.4), PDF pp. 168--170; Barros--Flapan--Marian--Silversmith author manuscript Section 2.2.2 and introduction/Section 2.1 scope, pp. 1--2, 7, 10; accessed 2026-10-07.
COMPARISON: Natural descended relative Ext, parallel holomorphic splitting and zero-contraction results cover the prerequisites; relative GRR and K3 RR cover necessary character/index tests. The sources do not evaluate this fixed kernel or assert complement simplicity, acyclicity or F existence. The published tangent-character formula is known overlap.
GAP: In the separate research turn verify trace-free all-fibre concentration, compare the actual family's direct image with the descended tangent bundle, glue the local parallel summand on B, and evaluate the signed full character and only justified complement/index conditions. The numerical verdict is uncomputed.
REASON: Essential coverage is ready for the unchanged target; import general theorems and perform only actual-family applicability and fixed-character specialization, without reproof or originality claim.
SCOPE: Conditional L052/L060 F, L062 KS, L063/L064 common-H map and audited L067; End_0(F) base change, global tangent comparison along B, parallel orthogonal complement, full relative GRR and necessary K3 RR/summand tests. No embedding, completeness, simple or acyclic complement, reconstruction, F existence or transport.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and lacked essential global relative tangent/descent coverage; this review adds Huybrechts--Lehn 10.2.1 while reusing ready local geometry and surface assessments.

## Proposed scope and relevance

Retain L052/L060's conditional actual F on B x Y, with rank two,
c_1=0, ch_2=-6e_1-7e_2+tau_D, and the exact common metric. Use
L062's actual KS map, L063/L064's common-H morphism and L067's
now-audited constant-scale total geodesy. Here p_B:B x Y -> B and
End_0(F) is the kernel of trace on End(F). No global universal sheaf
on the coarse moduli space is assumed.

The proposed test would compare the actual relative endomorphism
bundle with the tangent summand forced by the geometry, retaining
all higher characters forced by F's rank and all direct-image terms.
Its possible downstream use is a new necessary obstruction to this
F, independent of off-diagonal Hom jumps. It would neither construct F
nor settle separation or transport. Do not assume the complement is
stable, trivial, acyclic, or an actual transform of a specified bundle.

Continue if the actual-bundle comparison is justified and a violated
necessary character/cohomology condition results. If all tested
conditions are compatible, record that compatibility and stop this
bounded character/index test; it is not existence. A missing geometric
identification must be named, not silently added as an assumption.

ATTEMPTS/046 concerns a two-parameter off-diagonal Hom test and does
not compute this one-parameter trace-free endomorphism bundle with
its parallel tangent summand. ATTEMPTS/041--045 and the flat-index
source blocker remain preserved. Their comparison is recorded below.
The attempt's scope is approved; no numerical value or mathematical
conclusion is calculated or approved here. Mathlib coverage: not checked.

## Primary tangent theorem

[Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
Aspects of Mathematics E31, Vieweg (1997), Section 10.2,
Theorem 10.2.1, pp. 222--223](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=234)
works on the positive-rank stable-sheaf locus M_0 of a smooth projective
surface where trace-free Ext^2 vanishes. It identifies descended
relative Ext^1 with T M_0. The preceding Quot construction descends
Ext, trace and cup product because scalar conjugation acts trivially;
no universal family is required. Its full proof checks base change
and local freeness, identifies KS through the Quot tangent boundary,
and descends the natural isomorphism. Section 10.1.8/Example 10.1.9,
pp. 220--221, defines family KS and identifies its dual-number value
with the extension class. General statements are imported, not reproved.

The later application must check every fibre lies in M_0, pull back
this comparison for actual F using local families, and keep scalar
automorphisms/base-line twists in gluing. Removing the scalar summand
requires the characteristic-zero trace projection and H^1(O_Y)=0.
Do not replace naturality by matching tangent dimensions. Reuse
[L064's audit coverage](2026-10-07-charge-seven-finite-unramified-critical-audit.md)
for GAGA/Dolbeault and the actual differential, and
[L067's audit coverage](2026-10-07-charge-seven-geodesy-critical-audit.md)
for smooth h-stable analytic/coarse germs and harmonic L2. Image
normality, injectivity and a global universal family are not prerequisites.
No specialization is proved by this source review.

## Direct image and signed character tools

[Stacks 36.30.4, 0B91](https://stacks.math.columbia.edu/tag/0B91)
gives perfect pushforward and arbitrary derived base change for a
proper finitely presented flat map and perfect coefficient. Read its
proof reduction to 36.30.1. Smooth projective p_B and locally free
End_0(F) meet that scope. [36.31.3 in 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
gives the open locus of fixed-rank concentration in one degree; read
its finite-complex proof and [36.31.1, 0BDI](https://stacks.math.columbia.edu/tag/0BDI)
including the rank/minor cases. Verify trace-free cohomology on every
fibre before applying concentration; a generic Euler number is insufficient.

[Stacks 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO)
states smooth proper relative GRR for a finite locally free coefficient
with finite locally free higher images, using their alternating
characters and the relative tangent Todd class. Reuse L060's precise
Fulton citation: *Intersection Theory*, second edition (1998),
Theorem 15.2, pp. 286--287, Example 15.2.8, pp. 291--292, and the
assessed Chern/rank-truncation tools. The later calculation must
retain F's forced higher characters and full mixed square, and remove
the actual scalar term of End(F). Full End and End_0 have different
degree-zero/degree-two contributions; no new formula is evaluated here.

## Splitting and permissible index tests

[Verbitsky, *Deformations of trianalytic subvarieties of hyperkahler
manifolds*, alg-geom/9610010v1, 9 October 1996,
Proposition 4.1/Lemma 4.3 and Propositions 5.1--5.2,
PDF pp. 21--22, 29--30](https://arxiv.org/pdf/alg-geom/9610010v1#page=21)
cover the parallel orthogonal decomposition, holomorphic compatibility
and hyperholomorphic normal connection. Ambient compactness is not
required. Read the full relevant proofs including Appendix 5.3.
Proposition 5.5's broader printed wording omits middle-curvature zero
contraction used in its proof; do not import it. Audited L067 supplies
the local geometric hypotheses. Transfer through the natural tangent
comparison and gluing over B remain application obligations, using
the parametrized differential even at intersecting image branches.

[Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
alg-geom/9307008v1, 29 July 1993, Theorems 2.2--2.3/Lemma 2.1,
PDF pp. 6--7](https://arxiv.org/pdf/alg-geom/9307008v1#page=6)
gives compact-Kahler stable/Hermite--Einstein correspondence and zero
contraction for hyperholomorphic curvature. Read the invariant-form
orthogonality proof. Once the complement connection and holomorphic
structure are justified, this framework permits polystability at
the original h, allowing reducibility. Do not substitute an unassessed
projected index connection from the parked flat mechanism.

[Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication
draft, Chapter 9 Section 1.2--1.3, equations (1.2)--(1.4),
PDF pp. 168--170](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=168)
supplies HRR, Serre duality, the Euler pairing and simple-sheaf
self-Ext inequality. Reuse [the fixed-metric surface assessment](2026-10-04-corrected-rank-two-factor-restrictions.md)
for real-h stability, dual stability and Hermite--Einstein coverage.
HRR computes Euler characteristic, not separate cohomology dimensions.
Allow arbitrary c_1 on individual stable summands, trivial summands
and multiplicities. Check simplicity or section vanishing before
using stronger bounds. Neither total relative tangent nor complement
is assumed simple or acyclic; rank-two charge bounds do not apply
to higher rank. Any real-h discriminant test must use the covered
connection argument, not Huybrechts--Lehn 3.4.1's ample-divisor
hypothesis alone. No complement character or index is computed here.

## Known overlap and recorded failures

[Barros--Flapan--Marian--Silversmith, *On product identities and the
Chow rings of holomorphic symplectic varieties*, inspected author
manuscript, Section 2.2.2, p. 10](https://wrap.warwick.ac.uk/id/eprint/169152/1/WRAP-On-product-identities-and-the-Chow-rings-of-holomorphic-symplectic-varieties-Silversmith-2022.pdf#page=10)
already expresses the tangent character by relative Ext and GRR.
Read introductory scope (pp. 1--2) and the universal-character
qualification (Section 2.1, p. 7): primitive vector, generic
polarization and smooth projective moduli are imposed there. L063
does not establish the genericity/projectivity package. This is known
formula overlap; use Huybrechts--Lehn's broader descended tangent
theorem and GRR for the actual F. No Chow conjecture or broader
identity from this manuscript is an input.

ATTEMPTS/041--045 stop directional F-transform characters, cohomology,
orthogonal parity or projective lifting; ATTEMPTS/046 stops the
two-parameter Hom/Euler/first-order test. None evaluates this actual
one-parameter End_0(F) direct image with L067's parallel tangent
summand. Their compatible indices warn against imposing complement
stability or inferring vanishing from Euler data. Preserve every
stop and the separate SOURCE_BLOCKED flat-index route. This test
does not need that unavailable curvature-detection formula.

Queries: "moduli" "totally geodesic" "tangent bundle" hyperkahler
stable bundles; "relative Ext" "tangent bundle" "moduli" K3;
"hyperholomorphic" "normal bundle" "totally geodesic"; "Mukai
symplectic structure moduli sheaves abelian K3 surface relative Ext
tangent Kodaira Spencer pdf"; "K3" "parallel" "normal bundle"
"Chern" trianalytic; "moduli" "End" "totally geodesic" K3 bundle.
van Bree's exposition was a discovery lead only. Zhang's cotangent
PDF returned an access error and was not read; it is nonessential
after inspection of the primary tangent theorem. Search failure
does not establish novelty. Mathlib coverage remains not checked.

The unchanged target is ready for one REPRODUCTION application attempt.
A violated justified necessary condition permits an obstruction;
compatibility ends this bounded mechanism without existence. A failed
comparison is a named gap, never a silent extra assumption. This
review adds source coverage, no lemma, calculation, family or cycle.
