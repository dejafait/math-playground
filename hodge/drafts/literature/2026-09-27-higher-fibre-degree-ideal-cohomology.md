# Higher fibre-degree ideal cohomology — literature assessment

TARGET: Determine whether H^1(X,I_C(rH)) vanishes for every r>0 for the remaining ample polarizations with L.F>=3, retaining the original L and the three normalization gluing conditions.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched RM/Dickson restriction cohomology, K3 normal generation, elliptic-curve multiplication and multiplication on reducible curves; followed Franciosi's references and author publication list to primary theorem texts, with queries and scope below.
SOURCE_EVIDENCE: Franciosi--Tenni, The canonical ring of a 3-connected curve (2014), Theorem 4.2, p. 49, https://people.dm.unipi.it/franciosi/lavori/franciosi-tenni2.pdf#page=13; Franciosi, On the canonical ring of curves and surfaces (2013), Propositions 2.5 and 2.10, PDF pp. 6 and 9, https://pagine.dm.unipi.it/franciosi/lavori/manuscripta-ele.pdf#page=9; Gallego--Purnaprajna, arXiv:alg-geom/9608008v1, Proposition 2.2 and Corollary 2.3, p. 4, https://arxiv.org/pdf/alg-geom/9608008v1#page=4; original reference and reused vanishing statements below.
COMPARISON: Known results control complete multiplication on a K3 or suitable curves, and conditional multiplication with one prescribed subsystem; they do not identify the product of the two actual projection subspaces on W or its image in the three-condition descent space. The added fibre-degree hypothesis does not by itself discharge those missing checks.
GAP: Determine the global restriction image for each original ample L with L.F>=3, including the resolved fibre and all three gluing conditions, and justify every positive degree or exhibit a genuine nonzero cokernel.
REASON: Import the inspected multiplication and vanishing tools where their hypotheses hold; reserve the two-projection and global compatibility calculation for a later research turn. No checked theorem settles the exact target, and no vanishing, exceptional degree or transverse lift is derived here.

## Hypotheses

Retain the very general cubic RM surface S, X=S x S, reduced support C,
its normalization nu:W -> C with projections g_0,g_1, and the original
ample L with H=L external tensor L. The saved remaining range is
L.F>=3. The universal rational target and family source audit are
unchanged; reuse the primary-source reading of 2026-09-27 in the
[support-cohomology assessment](2026-09-27-positive-degree-normalization-cohomology.md).

The fixed L has no specified numerical class.
[L020](../../lemmas/L020-fibre-degree-two-positive-ideal-cohomology.md)
answers the question conditionally on L.F=2, without replacing L by a
power or an unrelated choice. Its r=1 exception and vanishing for r>=2
remain existing inputs, not results of this review. Its reduction to
O+P+bF and explicit section basis have not been extended to this range.

The prior [assessment](2026-09-27-positive-ideal-cohomology.md) remains
unchanged. Reuse its comparisons of regularity, eventual vanishing
and singular ideal-sheaf vanishing. The new source work below screens
multiplication results relevant to the changed fibre-degree range.

## Conclusion

The assessment is complete with decision SPECIALIZE. The curve and
K3 multiplication results are known supporting inputs to import by
citation. The exact global restriction statement was not matched in
the sources checked; this is not certified originality. This step is
LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, using one exploration
turn since L020's advance. No result has been reproduced or established
beyond the checked literature in this turn.

The intermediate target could locate further failures of the sufficient
summand-recovery argument when 0<m<n, or confine that cohomological
exception to the settled fibre-degree-two range. A nonzero group would
still leave the obstruction of an actual inclusion and cancellation of
the transverse RM obstruction uncomputed. Higher-order lifting,
algebraization and the universal Hodge gap would remain separate steps.

The attained cycle span is still 21 on the same family. The excluded
representatives still allow three RM directions against four required.
The m>n>0 exclusion is preserved. No complete candidate exists, and
no mathematical argument in PROOF.md or dependency in DAG.md changes.

## Proof

This section gives source statements and applicability comparisons.
It contains no new calculation of the saved cohomology groups.

### The actual restriction problem

The existing ideal sequence and ambient vanishing in L018 identify
H^1(X,I_C(rH)) with the cokernel of restriction from
H^0(S,rL) tensor H^0(S,rL) to H^0(C,H^r|_C). On W this uses precisely
the two pullback subspaces supplied by g_0 and g_1. The target is the
subspace satisfying all three pairwise gluing conditions, as recorded
in L019. These are reused notebook statements.

An argument about a complete linear system on S, a fibre, or W must
therefore explain its passage to these particular subspaces and this
descent target. Equality of the two pulled-back line bundles would not
by itself identify their section subspaces. No such equality, extension
of L020's translation reduction, or global surjectivity is assumed.

### K3 multiplication: reused and reread

Reread Gallego--Purnaprajna, *Vanishing Theorems and Syzygies for K3
Surfaces and Fano Varieties*, [arXiv:alg-geom/9608008v1, 7 August 1996,
section 2, Lemma 2.1, Proposition 2.2 and Corollary 2.3,
pp. 3--4](https://arxiv.org/pdf/alg-geom/9608008v1#page=3).
For a globally generated A on a smooth K3 with smooth nonhyperelliptic
general curve of genus at least three, the proposition gives
H^1(M_(A^p) tensor A^r)=0 for p,r>=1; the corollary gives normal
generation. Lemma 2.1 transfers curve multiplication to the ambient
regular variety with its stated H^1 hypothesis. These are complete
section-space statements. This review does not infer their hypotheses
for every L in the target from its degree on the selected fibre F.
Even when applicable on S, they leave the correspondence map above
unidentified.

Cross-checked [Huybrechts, *Lectures on K3 surfaces*, author-hosted
449-page copy, Chapter 2, Corollary 2.5 and Theorem 2.7,
pp. 26--27](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=26).
These give the same conditional normal-generation statement and global
generation of ample L^k for k>=2, very ampleness for k>=3. They provide
no conclusion for the target restriction in the original degree one.

### Multiplication on reduced and reducible curves

Read Franciosi--Tenni, *The canonical ring of a 3-connected curve*,
Rend. Lincei Mat. Appl. 25 (2014), 37--51, published copy,
[section 2 conventions, p. 39, Theorem 4.2 and proof, p. 49,
and Remark 4.4, p. 50](https://people.dm.unipi.it/franciosi/lavori/franciosi-tenni2.pdf#page=13).
For a projective reduced curve D with planar singularities, an invertible
A satisfying deg(A|_B)>=2p_a(B)+1 for every subcurve B, including D,
has surjective Sym^k H^0(D,A) -> H^0(D,A^k) for every k>=1.
Theorem 4.2 does not require the 3-connectedness of the paper's separate
canonical-ring theorem. Its reduced hypothesis is retained.

This is the strongest complete curve normal-generation criterion
selected in this review. It can support a later fibre calculation after
checking the actual bundle and every subcurve condition. It is not a
theorem about the surface C or the product of two specified subspaces.
No fibre application or consequence for the global restriction rank
is derived here.

Read Franciosi, *On the canonical ring of curves and surfaces*,
Manuscripta Math. 140 (2013), 573--596, author-hosted typeset copy
revised 11 January 2012, [section 2.1, Proposition 2.5 and its proof,
PDF pp. 4, 6--7, and Proposition 2.10, PDF p. 9](https://pagine.dm.unipi.it/franciosi/lavori/manuscripta-ele.pdf#page=6).
For a curve D on a smooth surface, Proposition 2.10 gives complete
mixed multiplication when A_i is numerically B tensor G_i, with
deg(B|_Z)>=p_a(Z)+1 and deg(G_i|_Z)>=p_a(Z) for every subcurve Z.
Proposition 2.5 also permits a base-point-free subsystem V of H^0(D,B):
under its connectedness and vanishing or dualizing-bundle hypotheses,
V tensor H^0(D,A) maps onto H^0(D,A tensor B). In particular its
case (ii) retains A tensor B^(-1)=omega_D and dim(V)>=3.

These statements improve on a comparison limited to equal complete
systems. They still require the second factor in full, and concern
curves. The two actual projection spaces, their restrictions, and the
passage from fibre statements to global sections need separate checks.
The symbol D here denotes a curve, not the notebook's surface C.

Followed the reference to Franciosi, *Adjoint divisors on algebraic
curves*, Adv. Math. 186 (2004), 317--333. Read the author's preprint
dated 10 September 2003, [Theorem A, p. 2, section 1.1, p. 4, and
proof of Theorem A, pp. 11--12](https://pagine.dm.unipi.it/franciosi/lavori/aim02-038.pdf#page=2).
On a numerically connected curve in a smooth surface it proves normal
generation under the numerical factorization and subcurve inequalities
quoted by the later paper. Its proof uses general auxiliary bundles
in specified Picard components; it does not require replacing the
given bundle by a general one. The later mixed-product criterion is
the closer tool if the two bundles differ. Neither source supplies
the global two-projection image in this notebook.

### Vanishing and the required bound

Reuse the prior assessment's inspected [Stacks Lemma 30.17.1,
tag 0B5U](https://stacks.math.columbia.edu/tag/0B5U), which gives
eventual vanishing for I_C with the original ample H. Its conclusion
has no effective starting degree. The saved regularity comparison
requires an actual regularity bound and suitable global generation.

Also reuse the inspected [de Fernex--Ein, corrected
arXiv:0805.3863v4, Theorem 1.1 and Example 5.7](https://arxiv.org/pdf/0805.3863v4#page=1)
and [Chou, arXiv:1311.5545v2, Theorems 1.1--1.2](https://arxiv.org/pdf/1311.5545v2#page=1).
Their ideal-vanishing statements retain positivity and ideal-generation
hypotheses; the new numerical restriction on L supplies no checked
generating degrees for I_C. C's isolated non-lci points alone are not
a reason to reject these tools, as the earlier assessment explains.

Thus the literature supplies conditional multiplication and a qualitative
tail, while the required assertion starts at r=1 and includes every
original ample class in the stated range. A failed sufficient theorem
hypothesis would not establish nonvanishing. L019's positive support
vanishing also leaves this restriction cokernel undecided.

### Search record, reuse and source access

Representative queries on 2026-09-27 were:

- `"K3" "real multiplication" "ideal sheaf" cohomology`
- `"real multiplication" "K3" "projective normality"`
- `"K3" "dihedral" correspondence cohomology line bundle`
- `"Dickson" "K3" "restriction" sections`
- `"elliptic K3" "multiplication" "line bundles"`
- `"multiplication" "elliptic curve" "line bundles" "degree at least" surjective`
- `"normal generation" "every subcurve" Franciosi Tenni`
- `"Franciosi" "Adjoint divisors on algebraic curves" pdf`
- `"Normal generation of vector bundles over a curve" site:projecteuclid.org`

Exact-geometry searches returned no inspected theorem deciding the
saved target. The known family paper reappeared; reuse its unchanged
[family audit](../../foundations/05-cubic-rm-family.md) and the prior
assessment's section 4.9 comparison, rather than repeat that review.
The [author's publication list](https://people.dm.unipi.it/franciosi/ric.html)
led to the original Franciosi reference and the stronger 2014 theorem.

The first host for the 2003 preprint timed out; the author's pagine.dm
mirror was readable. A Butler/Project Euclid lead exposed no theorem
text and remains unread, with no claim based on it. Saint-Donat's
original remains unread as recorded in the prior assessment; the
needed conditional K3 multiplication statement and its proof were
read directly in Gallego--Purnaprajna. No essential source gap remains
for this decision. Search snippets, bibliographic records and other
uninspected references are not counted as theorem-level evidence.
This is a bounded assessment, not an exhaustive novelty search.

### Remaining specialization and continuation test

One calculation of the unchanged target is justified. Keep the original
L as a parameter and test its actual two-projection image; any use of
a curve theorem must retain its full hypotheses and explain how its
sections arise from the global factors. Include the resolved fibre at
infinity, its scheme-theoretic tangency, and all three normalization
gluing conditions. A calculation with a different polarization or with
enlarged complete section spaces would not answer TARGET.

Continue toward a separately reviewed union-lifting test if a genuine
nonzero group is certified for some original L and positive r in this
range. A partial parameter result must leave its complementary range
explicit. Abandon this cohomological escape in the remaining range
only after proving vanishing for every such L and r>0, with a justified
tail if the calculation checks only finitely many degrees. The existing
fibre-degree-two exception would still remain available for an eventual
inclusion-obstruction test.

This screening does not reopen the stopped diagonal, fibre, rotation
or sheaf representatives. L020 is the closest local calculation and
does not already settle the remaining range; L018--L019 retain their
m>n>0 conclusion. The exact Next action is preserved. This is the first
exploration turn after the last mathematical input; assess continuation
within the shared three-turn budget if no advance or informative
negative result follows. No new cohomology value, rank, numerical-class
reduction, effective cutoff, or deformation result was obtained here.

## Mathlib

Coverage: **not checked** for the full target or supporting
multiplication, vanishing, restriction and gluing results. The named
theorems and direct links above are mathematical references, with
supporting scope distinguished from a match for the full target.
No Mathlib theorem match, absence, or certified originality is asserted.
