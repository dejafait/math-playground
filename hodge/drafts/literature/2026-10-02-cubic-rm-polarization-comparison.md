# Comparing two cubic-RM Kuga--Satake quadratic forms — literature assessment

TARGET: Assess whether algebraic comparison of the Kuga-Satake realizations for q and q_a(x,y)=q(ax,y), with a=2 id+U, can realize U on the cubic-RM transcendental Hodge structure.
CHECKED: 2026-10-02
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched changes of Kuga-Satake input quadratic form, RM polarization twists, square twists, similarities and isogenies; read the closest primary statements and their proofs below. No inspected theorem gives the full unconditional algebraic comparison for the saved rank-eighteen target.
SOURCE_EVIDENCE: van Geemen, arXiv:math/0609839v1, Lemma 4.2, Example 4.3 and sections 4.7, 7.7--7.10, https://arxiv.org/pdf/math/0609839v1#page=13; Varesco, arXiv:2304.02519v3, Definition 1.2, Proposition 3.1, Remark 4.3, Lemma 4.4 and Theorem 4.5, https://arxiv.org/pdf/2304.02519v3#page=11; further read statements and source limits below.
COMPARISON: Known square-twist and similarity results provide conditional abelian comparisons, while the algebraic transfer retains Kuga-Satake cycles for geometric forms. Changing an ample divisor or the abelian polarization does not cover replacing q on T by q_a. The square-twist applicability and changed-adjoint specialization remain to be tested.
GAP: For the specified a, check polarization and square-twist applicability, identify the resulting comparison's actual action with the geometric q-adjoint, and decide whether the required algebraic q_a embedding can be supplied independently of U. Neither that embedding nor a non-scalar algebraic self-correspondence is supplied by this review.
REASON: Import the known criteria without reproof and allow one bounded specialization of their precise hypotheses. This can distinguish a useful comparison prerequisite from a circular encoding of U; the separate cycle-algebraicity gaps remain explicit.

## Hypotheses

Keep T=T(S), End_Hdg(T)=E=Q(zeta_7+zeta_7^(-1)),
dim_Q T=18, dim_E T=6 and the generator U from the
[cubic-family audit](../../foundations/05-cubic-rm-family.md).
Retain the four-dimensional NS-fixed RM locus beyond the
three-dimensional Dickson locus, rather than changing to a
smaller-rank family. The proposed form is exactly q_a(x,y)=q(ax,y)
with a=2 id+U. Use one consistent sign convention for q and q_a;
some cited sources use the negative of the K3 cup product.

The original pending target and its noncircularity test are
preserved. An intermediate source checkpoint was saved during
this turn; its readings are incorporated below. No total-positivity
certificate, square identity, Clifford comparison, new adjoint
formula or cycle is derived in this literature-only turn.

Reused the [exact target audit](../../foundations/01-target-and-scope.md)
and reread [Deligne, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2):
the target is rational cycle-class surjectivity on every smooth
projective complex variety. The
[Clay page](https://www.claymath.org/millennium/hodge-conjecture/)
still labels the problem unsolved. The auxiliary comparison is
only an intermediate test.

## Conclusion

The exact saved action now has a ready SPECIALIZE assessment.
The imported supporting results give a concrete square-twist
branch and an algebraic transfer with explicit hypotheses.
They do not establish that this branch realizes U on S.

A separate research turn may check the specified element and
the actual comparison and transpose maps. It must retain the
algebraicity of every map used to return to S. The ordinary
Kuga--Satake correspondence is already an unresolved input on
this locus; the modified one cannot be silently added to it.
A conditional comparison can be useful, but an isogeny alone
does not reach the cycle threshold.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The
supporting mathematics is known and imported by citation;
there is no reproduction or result beyond the checked literature.
One consecutive exploration turn is used after L036. The exact
Next action is retained for the bounded specialization rather
than replaced by an unscreened target. No complete candidate
appears and STATUS remains IN_PROGRESS.

## Proof

This section contains precise citations and hypothesis comparisons,
not a proof of the proposed mixed algebraic comparison.

### Input-form twisting and its square branch

Read van Geemen, *Real multiplication on K3 surfaces and Kuga
Satake varieties*, arXiv:math/0609839v1, 29 September 2006,
[sections 4.1--4.3, PDF p. 13](https://arxiv.org/pdf/math/0609839v1#page=13),
[section 4.7, p. 15](https://arxiv.org/pdf/math/0609839v1#page=15),
and [sections 7.7--7.10, pp. 23--24](https://arxiv.org/pdf/math/0609839v1#page=23).

Lemma 4.2 says q_a is a polarization exactly when a is totally
positive. Example 4.3 gives a Hodge isometry from (T,q_a) to
(T,q) by multiplication by b when a=b^2 in E. These results
supply the first applicability tests, not their evaluation for
our chosen element. Do not assume that a non-scalar twist is
outside this square case.

Section 4.7's geometric realization statement assumes
dim_Q T<=11, while the saved rank is eighteen. This limit
does not prevent an abstract Kuga--Satake construction, but it
does prevent importing that geometric existence statement here.
Sections 7.8 and 7.10 distinguish Hodge identifications from
algebraic cycles. Their historical open-problem comments are
not current nonexistence theorems.

### Similarity functoriality and algebraic return maps

Read Varesco, *Hodge similarities, algebraic classes, and
Kuga--Satake varieties*, arXiv:2304.02519v3, 2 November 2023,
[Definition 1.2 and Remark 2.2, pp. 4 and 6](https://arxiv.org/pdf/2304.02519v3#page=4),
[Proposition 3.1 and its proof, pp. 11--14](https://arxiv.org/pdf/2304.02519v3#page=11),
and [Remark 4.3, Lemma 4.4, Theorem 4.5 and Corollary 4.6,
pp. 16--18](https://arxiv.org/pdf/2304.02519v3#page=16).
Cross-checked the
[published open-access text, Mathematische Zeitschrift 305 (2023), article 69](https://link.springer.com/article/10.1007/s00209-023-03390-8),
published 6 November 2023; theorem numbers agree.

Proposition 3.1 lifts a Hodge similarity to an abelian isogeny
commuting with the Kuga--Satake embeddings. Definition 1.2
requires a rational scalar multiplier. An unpolarized identity
between the two copies of T does not meet this hypothesis merely
because its Hodge decomposition agrees.
Its proof, Lemmas 3.2--3.5, uses compatible embedding vectors
and abelian polarizations; retain those choices in the specialization.

Remark 4.3 changes auxiliary embedding vectors and the abelian
polarization at fixed input form. Lemma 4.4's nonzero rational
scalar retraction is stated for the geometric form; its proof
deforms the construction to a Mumford--Tate general point.
Theorem 4.5 assumes algebraic Kuga--Satake correspondences on
both geometric sides. None states that an arbitrary q_a embedding
on the same S is algebraic. Applying this argument with a changed
input form requires an adjoint and algebraicity audit.

### Tensor transfer already assessed

Reused the [prior Kuga--Satake review](2026-09-27-cubic-rm-kuga-satake-realization.md)
and reread Varesco, *The Hodge conjecture for powers of K3
surfaces of Picard number 16*, arXiv:2203.09778v3, 13 May 2024,
[Lemma 1.6 and its proof, p. 5](https://arxiv.org/pdf/2203.09778v3#page=5).
Under algebraicity of the Kuga--Satake correspondence, a tensor
of T is algebraic exactly when its abelian image is. Its projection
does not itself supply the missing tensor or a second-form
correspondence. The earlier rank-six and generalized-Kummer
scope comparisons are reused; they do not supply the rank-eighteen
cycle here. Their sources need no mechanical rereading.

### A different meaning of two polarizations

Read Huybrechts, *Finiteness of polarized K3 surfaces and
hyperkahler manifolds*, Annales Henri Lebesgue 1 (2018),
[section 3, printed pp. 241--242, including Corollary 3.1](https://www.numdam.org/article/AHL_2018__1__227_0.pdf#page=15).
The discussion compares ample divisors L_1,L_2 on one surface.
It leaves the cup-product form on T(S) fixed and changes the
algebraic primitive complement. Its abelian isogeny comparison
therefore does not answer the q-to-q_a question. This is an
inspected nearby statement, not a matching theorem.

### Search evidence and access limits

Queries on 2026-10-02 included:

- `Kuga Satake different polarizations real multiplication twisted quadratic form isogeny algebraic correspondence`
- `"Kuga-Satake" "polarizations" comparison`
- `"Kuga-Satake" "q_a"`
- `"Kuga-Satake" "different" "quadratic forms"`
- `"Kuga-Satake" "twisting" polarization`
- `"Kuga-Satake" "different polarizations" "isogeny"`
- `"Kuga-Satake" "twisted polarization"`
- `"real multiplication" "K3" "twisting" "square"`
- `"Kuga-Satake" "totally positive" isogenous`

Additional exact cyclotomic-term searches did not identify a
theorem for this mixed comparison. Failed queries establish
neither novelty nor mathematical impossibility.

The initial Numdam DOI-PDF route failed; the direct article PDF
was then read. No essential source-access gap remains for the
criteria above. Nikulin's originals, van Geemen's older Banff
chapter and Kleiman's projection theorem were not separately
read; no additional claim from them is used beyond the inspected
statements and the prior transfer assessment. The square example
and Varesco's explicit functoriality proof suffice to screen the
selected applicability test.

Search also returned Poon's rank-fourteen constructions, uniform
Kuga--Satake/finiteness papers and recent Preprints.org claims.
They are unread leads, not evidence for this target. No inference
of algebraicity, nonalgebraicity or originality is drawn from them.

### Relevance, redundancy and continuation test

The main gap on this locus is algebraic realization of U beyond
the Dickson family. The intermediate target is an abelian comparison
with a precisely controlled action and algebraic maps returning to S.
Its plausible use is to realize a and subtract its scalar part,
or realize an element whose algebraic compositions recover U.

The isometry stop in L004 retains the original geometric form.
Changing the form is a different question, but merely identifying
(T,q_a) with (T,q) does not evade its cycle requirement. L035--L036
stop inherited half twists, not input-form comparisons. The
divisor/Prym exclusions remain scoped to their actual embeddings
and sources. No stopped support, sheaf or bundle test is reopened.

For the one bounded specialization, use Lemma 4.2 and Example 4.3
to check the specified a; if the square branch applies, import
Proposition 3.1's isogeny rather than rebuilding its Clifford
proof. Track its direction, the two embeddings and the actual
q-based geometric transpose, distinguishing that transpose from
an abstract q_a-adjoint. Determine exactly which algebraic
correspondences would be required. Do not assume a new cycle
just because its associated abelian map is algebraic.

Continue if this gives a relevant noncircular prerequisite or
an independently supplied algebraic map with the desired
non-scalar action. Keep any remaining cycle-algebraicity gap
explicit. Stop this selected recipe if its only supply for the
modified embedding already requires algebraicity of U or an
equivalent non-scalar endomorphism. Failure of the square branch
alone would stop that branch, not all possible comparisons.
An inconclusive test spends the existing exploration allowance.

The required threshold is the full U action on the intended
transverse RM points, not an unpolarized identification or scalar
component. The achieved span stays 21 on the Dickson family;
three RM directions are attained against four required.
The ordinary Kuga--Satake cycle, the earlier beta_U supply,
arbitrary primitive fourfold classes and higher-dimensional
cases remain unresolved. The review changes the available
source-based test, not these mathematical bounds.

## Mathlib

Coverage: **not checked** for the complete mixed comparison or
its supporting polarization, similarity and transfer theory.
The named citations above match supporting criteria within their
stated hypotheses, not the full unconditional realization target.
No Mathlib match or absence is asserted.
