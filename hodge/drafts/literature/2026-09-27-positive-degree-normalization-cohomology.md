# Positive-degree normalization cohomology — literature assessment

TARGET: Determine whether H^1(C,O_C(nH)) vanishes for every n>0 for the fixed product polarization H, using the normalization and its three double-point gluing conditions.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact Dickson/RM correspondence cohomology, normalization at isolated double points, elliptic-surface vanishing, adjoint restriction and cyclic-cover point separation; primary statements and representative queries are recorded below.
SOURCE_EVIDENCE: Fujino, A transcendental approach to Kollar's injectivity theorem II, version 1.25 (2011-01-23), Corollary 1.7, p. 4, https://www.math.kyoto-u.ac.jp/preprint/2011/02fujino.pdf#page=5; Stacks Lemmas 30.17.1, 30.2.4, 20.54.2 and 37.67.8, https://stacks.math.columbia.edu/tag/0B5U, https://stacks.math.columbia.edu/tag/089W, https://stacks.math.columbia.edu/tag/01E8 and https://stacks.math.columbia.edu/tag/0B7M; cyclic-cover and K3 theorem versions and direct links below.
COMPARISON: Serre vanishing covers only large n; Kawamata--Viehweg covers an adjoint bundle on the smooth normalization under a nef-and-big hypothesis; cyclic-cover separation and K3 vanishing have further hypotheses. None of the inspected statements supplies all-positive-degree vanishing on this singular support with the specified product polarization and all three gluing conditions.
GAP: Check the positivity or cover-theoretic description of the actual pulled-back product bundle, and the simultaneous restriction map at the three identified pairs, without strengthening the fixed ample L to a very ample one or replacing it by a power.
REASON: Import the general tools and specialize only these uncomputed geometric data. This can decide whether L018 excludes every positive containing degree or leaves exceptions worth testing; the review itself proves no new vanishing, exception, or lifting statement.

## Hypotheses

Retain the fixed ample L on S, H=p_1^*L tensor p_2^*L, and the very
general cubic family and normalization nu:W -> C from L008. Write
M=nu^*(H|_C)=g_0^*L tensor g_1^*L. L008 already records the finite flat
double covers, their smooth branch fibres, K_W=2F_W, and the three
identified pairs over infinity. These are existing notebook inputs,
not results obtained in this review. Retain both points of each pair
and the resolved fibre components.

L is fixed but its numerical class was not specified in the saved
target. Keep its original ample hypothesis; do not choose a more
positive polarization, assume very ampleness, or assert that the two
pullbacks of L coincide. Any conditional answer must identify its
additional hypothesis and leave the other polarizations unresolved.

Reuse the rational target in [the scope audit](../../foundations/01-target-and-scope.md).
On 2026-09-27 the [Clay page](https://www.claymath.org/millennium/hodge-conjecture/)
still labels it unsolved; Deligne's [section 1, pp. 1--2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=1)
retains smooth projective complex varieties and rational cycle classes.

## Conclusion

The source assessment is complete with decision SPECIALIZE. The
framework is known and should be cited. The all-positive-degree
statement was not matched in the sources checked; this is not a
novelty claim. This completed step is LITERATURE / NOVELTY_UNCHECKED /
EXPLORATION, using one exploration turn since L018's informative
negative result. No calculation on the saved target has been performed.

The completed [union test](../../lemmas/L018-high-degree-complete-intersection-unions-retain-obstruction.md)
excludes every admissible containing degree with the stated H^1 equal
to zero. Determining whether exceptional degrees actually remain would
either extend that exclusion or identify degrees requiring a different
compatibility calculation. The available cutoff remains qualitative;
this review does not produce an effective finite range. Nonzero
cohomology alone would not construct a transverse lift.

The achieved embedded lifting kernel remains three-dimensional against
four RM directions required. The known 21-dimensional cycle span covers
the same family. Higher-order lifting, algebraization and the universal
primitive-cycle gap remain unresolved even if an exceptional degree
eventually permits a first-order lift. No complete candidate exists.

## Proof

The evidence here is a comparison of inspected source statements.
The remaining applicability checks and cohomology computations are
reserved for a later research turn.

### Normalization, gluing and the existing large-degree bound

Read the following Stacks Project statements online on 2026-09-27:

- [Lemma 37.67.8, tag 0B7M](https://stacks.math.columbia.edu/tag/0B7M)
  gives the structure-sheaf exact sequence for the pushout of two
  closed immersions. Its maps include the difference of the two
  restrictions on their intersection. This is the standard local
  gluing tool for the two branches already recorded in L008.
- [Proposition 37.67.3, tag 0E25](https://stacks.math.columbia.edu/tag/0E25)
  gives the broader pinching construction and its fibre-product
  structure sheaf. [Situation 37.67.1, tag 0ECI](https://stacks.math.columbia.edu/tag/0ECI)
  requires a closed immersion, an integral second map, and a suitable
  affine neighbourhood for each fibre. These hypotheses must be
  checked before identifying C with such a global pushout.
- [Lemma 30.2.4, tag 089W](https://stacks.math.columbia.edu/tag/089W)
  identifies coherent cohomology with that of the pushforward under
  an affine morphism. [Lemma 20.54.2, tag 01E8](https://stacks.math.columbia.edu/tag/01E8)
  supplies the projection formula for a finite locally free factor.
  These justify the finite-normalization and line-bundle framework;
  neither proves surjectivity of a global restriction map.
- [Lemma 30.17.1, tag 0B5U](https://stacks.math.columbia.edu/tag/0B5U)
  states eventual higher-cohomology vanishing for every coherent sheaf
  twisted by an ample bundle on a proper scheme over a Noetherian
  ring. [Lemma 30.17.2, tag 0B5V](https://stacks.math.columbia.edu/tag/0B5V)
  treats ampleness under finite surjective pullback. The former already
  covers L018's large-degree input directly on C, despite singularities.
  It specifies neither n_0=1 nor an effective threshold here.

The specialization must retain the finite gluing quotient and its
connecting map in cohomology. Vanishing on W alone and separate
separation of each pair are not substitutes for the required
simultaneous gluing test. No new normalization sequence for C or rank
of its restriction map is established in this turn.

### Adjoint vanishing on W and the singular-support mismatch

Read Fujino, *A transcendental approach to Kollar's injectivity theorem
II*, author-hosted version 1.25,
dated 23 January 2011, [Corollary 1.7, p. 4](https://www.math.kyoto-u.ac.jp/preprint/2011/02fujino.pdf#page=5).
For a smooth projective variety and a nef and big line bundle A,
H^q(K tensor A)=0 for q>0. Corollary 1.4, p. 3, also states a
relative version. Applied to the desired M^n, this framework requires
checking M^n tensor K_W^(-1), not just ampleness of M. L008's
nontrivial canonical bundle must remain in that check. No such
positivity or intersection calculation is made here. The theorem
does not supply the three gluing conditions.

Also inspected Fujino's earlier [*Kawamata--Viehweg vanishing theorem*,
version 1.04, 22 July 2009, Theorem 0.1, p. 1](https://www.math.kyoto-u.ac.jp/~fujino/kawamata--viehweg2.pdf#page=1).
It states the smooth relative nef-and-big theorem for a rational
divisor with normal-crossing fractional part. The later explicit
Corollary 1.7 is the selected absolute citation; the older draft's
unresolved cross-references are not needed.

Read Berquist, *A Semi-Smooth Kodaira Vanishing Theorem and Demi-Normal
Cyclic Covering Lemma*, [arXiv:1606.07679v1, section 1, p. 3, and
Theorem 2.1, p. 5](https://arxiv.org/pdf/1606.07679v1#page=3).
The file carries the v1 submission stamp of 24 June 2016 and a title-page
date of 24 September 2018. The theorem concerns omega_X tensor A for
ample A on a projective semi-smooth variety. Its allowed singularities
are hypersurface double crossings and pinch points; the surrounding
demi-normal framework includes S_2. L008 and L018 instead retain
isolated non-Cohen--Macaulay surface crossings. Smoothness of their
normalization does not meet this theorem's hypotheses. This source
therefore supplies no direct vanishing theorem for the saved C.

### Cyclic-cover restriction tools and sharper K3 vanishing

Read Bauer--Di Rocco--Szemberg, *Cyclic coverings and higher order
embeddings of algebraic varieties*, [arXiv:math/9806153v1, 29 June 1998,
section 1, p. 2, Theorem 2.1 and equation (1), p. 3, and Theorem 3.1,
p. 6](https://arxiv.org/pdf/math/9806153v1#page=3).
Theorem 2.1 gives k-jet ampleness of pi^*A for a degree-d cyclic cover
branched along a smooth divisor dD when A-qD is (k-q)-jet ample for
0<=q<=min(k,d-1). Theorem 3.1 gives a weaker sufficient condition
for k-very ampleness using its stated sigma(k,d,q). Equation (1)
decomposes sections into covering-character summands.

These results distinguish sections constant on a cover fibre from
sections that can separate its sheets. They concern a single pullback
pi^*A. The actual M is a tensor product from two projections. A
single-pullback identification, its character summands and the required
restriction properties remain to be checked. No such identification
is assumed. Full higher-order separation is a sufficient framework;
failure of its hypotheses would not prove failure of the particular
three-pair restriction map. No k-value or degree bound is derived here.

Read Knutsen--Lopez, *A sharp vanishing theorem for line bundles on K3
or Enriques surfaces*, [arXiv:math/0610068v2, 22 June 2007, unnumbered
main Theorem, p. 1, and Remark 2.2, p. 3](https://arxiv.org/pdf/math/0610068v2#page=1).
For an effective nonzero line bundle A with A^2>=0 on a K3, the theorem
characterizes nonzero H^1 by either A being a multiple rE, r>=2, of a
primitive nef isotropic divisor, or an effective divisor Delta with
Delta^2=-2 and A.Delta<=-2. The Enriques cases have their own canonical
twists and multiplicity formulas. Remark 2.2 stresses that testing
irreducible (-2)-curves alone is insufficient.

This is a possible input for actual character summands on S if they
are identified and its effectiveness and square hypotheses checked.
It does not apply directly to W or to the nonnormal C and supplies
no simultaneous evaluation theorem. Any use must preserve the
effective-divisor qualification; no divisor class is tested here.

### Search, reuse and source access

Representative queries used on 2026-09-27 were:

- `"K3" "real multiplication" "correspondence" "cohomology" normalization`
- `"K3" "Dickson" "normalization" cohomology`
- `"normalization" "isolated" "double points" "vanishing" surface`
- `"elliptic surfaces" "ample" "H^1" vanishing line bundles`
- `Kawamata Viehweg vanishing theorem nef big line bundle original paper pdf`
- `Reider theorem adjoint line bundle length two separate points nef big surface`
- `Beltrametti Sommese zero dimensional subscheme adjoint linear systems surfaces k very ample pdf`
- `"Cyclic coverings and higher order embeddings of algebraic varieties"`
- `"A sharp vanishing theorem for line bundles on K3 or Enriques surfaces"`

The exact-geometry searches returned the known family and general
tools, without a match for this all-degree statement. Reused the
family audit and the prior [complete-intersection assessment](2026-09-27-ample-complete-intersection-union.md)
for unchanged linkage and obstruction inputs. The [published family
paper, sections 4.8--4.9 and 5.3--5.4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=13)
constructs the cycles and identifies the special cubic family; the
existing audit does not contain the requested line-bundle cohomology.
No repeated deformation-theory search was needed.

Esnault--Viehweg's *Lectures on Vanishing Theorems* was an unread lead:
both attempted Duisburg PDF URLs were inaccessible. The selected
vanishing theorem was read directly in Fujino, so there is no essential
access gap. Reider and Beltrametti--Sommese search results were discovery
leads, not inspected original theorems or inputs to a claimed bound.
The cyclic-cover paper above provides an inspected restriction theorem.
Search snippets, secondary summaries and uninspected references are
not counted as theorem evidence. The search is bounded, not exhaustive.

### Remaining specialization and decision test

L018 is the closest local result and already stops all degrees with
the required vanishing. Its Serre argument does not duplicate the
all-positive-degree target. The stopped diagonal, fibre, rotation and
sheaf representatives in L009--L017 do not answer this cohomology
question; none is reopened by this review.

One bounded specialization of the unchanged target is justified:

1. Identify the actual M and the twisted normalization/gluing data,
   retaining the fixed L and all three pairs. Any reduction to a single
   double-cover pullback needs an argument, including fibre identifications.
2. Use the cited vanishing and restriction theorems where their
   hypotheses hold, and test the remaining small-degree data. The
   required threshold is every n>0 with the simultaneous gluing map
   accounted for. Eventual vanishing merely recovers L018's regime.
3. If all-positive-degree vanishing is proved, stop the remaining
   complete-intersection construction via L018's recovery implication.
   This would exclude transverse lifts; equality with V_D still has
   L018's separate ideal-cohomology hypothesis. If a genuine nonzero
   group is found, isolate its degree and gluing contribution before
   testing obstruction cancellation. A failed sufficient positivity
   test alone settles neither alternative.

This preserves the original research target. No new cohomology value,
normalization computation, intersection inequality, effective cutoff,
transverse lift or lemma is claimed. The initial pending registration
after L018 is superseded only as a source assessment; its unresolved
small-degree question and all existing mathematical work are preserved.

## Mathlib

Coverage: **not checked** for the full cohomology statement or its
supporting vanishing, cyclic-cover, restriction and gluing tools. No
formal match or absence is claimed. The named theorems and direct
links above are supporting mathematical references, not matches for
the full saved statement.
