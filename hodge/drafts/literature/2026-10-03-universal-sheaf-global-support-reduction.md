# Global support-cycle reduction — literature assessment

TARGET: Review a global degree-three support-cycle reduction for the universal-sheaf action of maps S -> M_H(2,0,-1), including collisions and images contained in the boundary.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact vector, rank-two c_2=3 sheaves, Hilbert-cube descriptions, Donaldson--Uhlenbeck support cycles, relative double duals, simultaneous hulls and leading Chern-character terms; followed the primary surface and hull references listed below. No inspected statement supplies the full boundary-inclusive universal-action formula.
SOURCE_EVIDENCE: Huybrechts--Lehn, online 281-page text, Definition 8.2.7, Theorem 8.2.8, Definition 8.2.10, Theorem 8.2.11, Proposition 8.2.13 and Lemma 8.2.14, printed pp. 190--193, https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=202; Kollar, arXiv:0805.0576v4, Definition 17 and Theorem 21 with proof, pp. 8--9, https://arxiv.org/pdf/0805.0576v4#page=8; Fulton, Intersection Theory, second edition (1998), Theorem 18.3(3),(5) and Example 18.3.11, pp. 353--354,363, https://djvu.online/file/87GFN2nbfbdF7; O'Grady, arXiv:1205.4119v2, Proposition 4.2 and Remark 4.3, pp. 11--12, https://arxiv.org/pdf/1205.4119v2#page=11; additional inspected comparisons and the retained Markman convention below.
COMPARISON: Known theorems give a global slope-moduli invariant, fixed-polystable-bundle symmetric-product strata, a flat-hull stratification and the support-multiplicity/Chern framework. They do not identify every rank-two c_2=3 fibre's actual double dual, construct the required relative quotient for every pulled-back family, or identify its transcendental action; generic birationality and pointwise zero-cycle classes are insufficient.
GAP: Specialize the cited tools to the actual pulled-back universal family: distinguish the slope-graded double dual from F^{**}, justify a base-changing relative hull and a flat length-three quotient across every collision and boundary image, and compare the mixed Chern component with the weighted support action on T(S).
REASON: Import the general theorems rather than reprove them. One separate bounded research step may test the missing exact-vector and family/action specialization; a successful reduction would locate an independent non-scalar source, while failure would identify the stratum or hypothesis requiring a different mechanism. No global formula or originality claim is made in this literature turn.

## Hypotheses and relevance

Retain the rank-eighteen T(S), full cubic endomorphism field
E=Q(zeta_7+zeta_7^(-1)), and the four-dimensional NS-fixed RM
locus from the unchanged prior assessment. The main gap on this
route is a non-scalar algebraic action on a surface outside the
three-dimensional Dickson family. The universal target remains
the rational Hodge conjecture, with its separate arbitrary
fourfold and higher-dimensional gaps.

Write B=S for the parameter surface and X=S for the surface
carrying the sheaves. For an algebraic morphism
f:B -> M_H(2,0,-1), let F be the pulled-back universal sheaf on
B times X, allowing the usual line-bundle twist from B. The
existing assessment supplies v-generic H and an untwisted
universal sheaf. It does not supply f. The saved target asks
whether this family admits a global degree-three support
description that computes f^*theta_v on T(X), including f whose
whole image is outside the reduced three-point open set.

The proposed intermediate target is this global reduction,
not a new map or a proof that its action must be scalar. Its
plausible use is to turn a later non-scalar-family search into
a precise support-correspondence test. Neither the actual
double-dual identification nor descent of an ordered quotient
presentation is assumed here.

## Conclusion

SPECIALIZE is ready for the unchanged exact target. The source
review imports supporting results, not the full reduction.
The remaining family/action statement is a scoped application
to be proved or refuted in a separate research turn. No new
boundary classification, Chern calculation, action formula,
lemma or mathematical script was produced. This is local source
progress without a claim of mathematics beyond the literature.

## Inspected statements and strongest applicable conclusions

1. Read O'Grady, *Moduli of sheaves and the Chow group of K3
   surfaces*, [arXiv:1205.4119v2, 22 May 2012, Proposition 4.2
   and its proof, Remark 4.3, pp. 11--12](https://arxiv.org/pdf/1205.4119v2#page=11).
   The exact vector is the exceptional generic non-locally-free
   case. The three distinct point quotients of O_X^2 give the
   stated generic sheaf and a birational Hilbert-cube model.
   The quantifier is generic; no all-fibre or relative-hull
   assertion is substituted for it.

2. Read Huybrechts--Lehn, *The Geometry of Moduli Spaces of
   Sheaves*, [online 281-page text, section 8.2, Definition
   8.2.7 and Theorem 8.2.8, printed pp. 190--191; Definition
   8.2.10, Theorem 8.2.11, Proposition 8.2.13 and Lemma 8.2.14,
   pp. 191--193](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=202).
   These supply the Gieseker-to-slope-moduli morphism and its
   closed-point invariant: E_F=(gr_mu F)^{**}, with the lengths
   of E_F/gr_mu F. For fixed polystable E, Proposition 8.2.13
   embeds the appropriate symmetric product. Lemma 8.2.14
   treats a flat zero-dimensional sheaf family, including
   multiplicities. Also inspected Lemma 2.1.4, printed p. 33,
   for the fibrewise-injectivity criterion for a flat quotient.
   These are supporting results; no assertion about the mixed
   Chern component of every universal-family pullback is given.

3. Read Kollár, *Hulls and Husks*, [arXiv:0805.0576v4,
   21 September 2009, introduction, Definition 17, Lemma 18,
   Theorem 21 and its proof, pp. 1,8--9](https://arxiv.org/pdf/0805.0576v4#page=8).
   A simultaneous hull is a flat family of fibrewise hulls
   preserved by base change; its existence is represented by
   a locally closed decomposition of the base. The introduction
   explicitly warns that smoothness and torsion-free fibres
   alone do not give such a family. This removes any basis for
   assuming that taking the ordinary double dual on the product
   commutes with restriction to every fibre. Applicability to
   the actual F, including its hull Hilbert polynomials, remains
   a specialization question.

4. Read Fulton, *Intersection Theory*, **second edition, 1998**,
   [Theorem 18.3(3),(5), printed pp. 353--354, and Example
   18.3.11, p. 363, in the online scan](https://djvu.online/file/87GFN2nbfbdF7).
   The Riemann--Roch transformation has the support cycle as
   its leading term, with generic-stalk lengths, and relates
   to the Chern character on a smooth ambient variety.
   This supplies the weighted-cycle input once an actual
   quotient sheaf is justified, not existence of that quotient.
   The scan's imprint and second-edition preface were checked;
   the host's misleading 1997 label is not the edition used.
   Also read [Stacks, Definition 42.10.2, Tag 02QV](https://stacks.math.columbia.edu/tag/02QV),
   and [Lemma 42.23.2, Tag 02S9](https://stacks.math.columbia.edu/tag/02S9),
   for the associated-cycle convention and dimension filtration.

5. Re-read Markman, *On the monodromy of moduli spaces of
   sheaves on K3 surfaces*, [arXiv:math/0305042v3,
   6 October 2005, equation (29) and equations (32)--(33),
   pp. 22--23](https://arxiv.org/pdf/math/0305042v3#page=23).
   Retain x^vee, the quasi-universal similitude and the
   family-normalization qualification. The definition gives
   the action to compare; it does not determine f^* or turn
   a fibrewise CH_0 equality into a mixed Kunneth equality.

6. For stronger comparisons, read Tajakka, *Uhlenbeck
   compactification as a Bridgeland moduli space*,
   [arXiv:2007.12237v1, 23 July 2020, Theorem 1.1,
   pp. 3--4, Proposition 2.2, p. 11, section 7 and Theorem
   7.1, pp. 35--36](https://arxiv.org/pdf/2007.12237v1#page=3).
   The wall description retains a polystable locally free
   summand and shifted point summands; the Uhlenbeck comparison
   is bijective on points. It does not identify the locally
   free summand with O_X^2 for this vector or supply a pulled-back
   universal quotient. Bijectivity is not an asserted isomorphism.

   Read Greb--Toma, *Compact moduli spaces for slope-semistable
   sheaves*, published *Algebraic Geometry* 4 (2017), 40--78,
   [Main Theorem and Proposition 4.5, pp. 42,55--56](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=3),
   and [arXiv:1303.2480v3, Main Theorem, p. 4](https://arxiv.org/pdf/1303.2480v3#page=4).
   The theorem includes dimension n>=2 and flat families over
   weakly normal bases with fixed invariants and determinant.
   B is smooth, but determinant conventions still require care.
   Its determinant-line universal property does not state the
   transcendental Chern-action comparison. The arXiv text
   resolves the published PDF extraction's misleading n>2;
   the interim checkpoint's exclusion of the surface case is
   corrected here. No mathematical conclusion depends on it.

## Exact difference and continuation test

The closest global surface theorem is Huybrechts--Lehn's
Theorem 8.2.11, rather than the generic O'Grady presentation.
The distinction between its graded invariant and the actual
family is the central remaining issue. The difference is not
an effective constant or a gratuitous reproof of a known
moduli construction.

One separate bounded research step may test the following
single global reduction. First settle whether every stable
sheaf with this vector has the required trivial actual hull;
retain possible slope-graded line factors and special fibres.
Then justify a simultaneous hull of F and determine whether it
has the form p_B^*V for a rank-two bundle V on B, with an exact
sequence 0 -> F -> p_B^*V -> Q -> 0 whose quotient is B-flat
of length three on every fibre. These are **targets**, not
results of this assessment. Use the imported hull and flatness
theorems with their hypotheses instead of replacing this passage
by a pointwise identification.

If that sequence is established, use the imported cycle and
Mukai conventions to compare the action on T(X) with the
weighted support correspondence of Q, retaining base twists
and the mixed degree-four component. Include families entirely
in collision strata; they have no dense reduced-support open
set on which to start the previous calculation. A raw support
set or an unproved flat Fitting scheme is not the desired cycle.
An algebraic determinant identity alone does not settle an
identity on the transcendental space.

Continue if the global statement is proved, or a concrete
boundary exception identifies the extra source of action.
Abandon the unqualified reduction if its trivial-hull or flat
quotient assertion fails; preserve the correct conditional
or stratum-specific version. Merely applying a universal sheaf
after assuming f exists gives no non-scalar cycle. A successful
reduction still leaves independent support-family construction,
stable descent, non-scalar action and transverse coverage open.

## Redundancy, earlier failures and required threshold

The full overview, ID-only DAG and
[one-moving-point stop](../../ATTEMPTS/029-one-moving-point-universal-sheaf.md)
were inspected before this review. L038 controls its specific
family and hypothetical repairs at two parameter points only.
The global target is neither that scalar calculation nor the
earlier support/syzygy or Kuga--Satake recipes. Their exclusions
are preserved and not extrapolated to arbitrary f.
Reuse the unchanged moduli-existence, universal-family and
rational-target evidence in
[the earlier assessment](2026-10-03-cubic-rm-universal-sheaf-map.md).

No new algebraic class or transverse surface is obtained. The
known span remains 21 on the Dickson family; three RM directions
are attained against four required. The previous sheaf recipe
attains only the scalar direction, one transcendental dimension
against three required by E. The imported global invariant does
not improve these bounds. This is the first consecutive
EXPLORATION after L038, with an actionable specialization test;
there is no complete informal candidate or novelty claim.

## Search record and access qualifications

Queries actually used included:

- `K3 "2,0,-1" "double dual"`
- `K3 "rank two" "c_2=3" Uhlenbeck`
- `"K3" "c2 = 3" "Uhlenbeck"`
- `"Mukai" "(2, 0, -1)" "Hilbert"`
- `K3 Hilbert cube moduli rank two trivial determinant Uhlenbeck support cycle`
- `"K3" "relative double dual" sheaves`
- `"relative double dual" "flat" sheaf`
- `Greb Toma slope semistable sheaves Donaldson Uhlenbeck compactification morphism double dual zero cycle`
- `"Uhlenbeck Compactification as a Bridgeland Moduli Space" arxiv`
- `Kollar hulls husks simultaneous hulls numerical criterion base change double dual`
- `"Hulls and Husks" "Theorem 21"`
- `"Chern character" "fundamental cycle" "Fulton"`
- `"Fulton" "18.3.2" "dimension"`
- `"Compact moduli spaces for slope-semistable sheaves" "at least"`

The original Li (1993) PDF request returned an access error.
Its original proof was **not read** and is not separately
imported; the accessible surface statements and surrounding
proofs in Huybrechts--Lehn resolve the needed source scope.
The theorem statements named above were read, not inferred
from snippets. Broader Hilbert-cube and framed-moduli hits were
not used as full-statement evidence. No essential source remains
inaccessible for the stated SPECIALIZE decision, and an
unsuccessful full-match search is not evidence of originality.
The interim REVIEW_REQUIRED checkpoint is incorporated and its
Greb--Toma scope error corrected; no derivation followed the review.

## Mathlib

Coverage: **not checked** for the full reduction or supporting
moduli, simultaneous-hull, support-cycle and Mukai-map results.
The named direct citations above support parts of the framework;
none is a Mathlib match for the full statement. No absence from
checked Mathlib sources or originality is asserted.
