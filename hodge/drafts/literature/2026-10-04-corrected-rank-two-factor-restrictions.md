# Nonsymmetric survivor — factor-restriction literature assessment

TARGET: Test whether restrictions to the two K3 factors obstruct slope-polystable locally free realizations of L050's topological survivor a=-7,b=-6 at the fixed common metric.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched hyperholomorphic restriction to hyperkahler submanifolds, polystable invariant-Chern criteria, and low-second-Chern K3 bundles; read primary statements below and compared the existing stable-bundle and stable-sheaf assessments. No direct theorem for the full fixed-tensor target was identified.
SOURCE_EVIDENCE: Verbitsky, arXiv:math/0205210v1, Definitions 3.2--3.4, Theorem 3.5, Proposition 3.7, Lemma 3.8 and Theorem 3.9, pp. 12--15; Verbitsky, arXiv:math/0107182v10, Definition 3.4, Proposition 3.7, Lemma 3.8 and Theorem 3.9, pp. 12--14; Huybrechts, Lectures on K3 Surfaces, author-hosted prepublication draft, Chapter 1, equations (2.5)--(2.6) and Proposition 2.4, PDF pp. 11--13, and Chapter 9, Section 3.1 and Theorem 4.9, PDF pp. 175--176 and 182. Direct links and scope comparison below.
COMPARISON: Known hyperholomorphic and Kobayashi--Hitchin inputs cover the connection framework at a real Kahler metric; K3 Riemann--Roch, dual stability and line-bundle parity cover the surface tools. They do not evaluate the saved mixed tensor or supply the full stable/split case analysis for this product bundle.
GAP: Verify full-class rotation invariance, justify curvature restriction to each quaternionic factor, and test restricted low Chern data without assuming restriction preserves stability. Retain split cases on both product and factors.
REASON: Import the inspected framework and perform only its finite-rank fixed-data specialization in a separate mathematical turn. This category change is essential after topological existence; no new obstruction or holomorphic existence result is derived here.
SCOPE: Rank two, c_1=0, X=S x S, the integral mixed tensor and final common metric of L048--L050, and the single survivor (-7,-6). Locally free slope-polystable holomorphic bundles only; no Gieseker-only or torsion-free substitution. No general correction-region classification or transverse transport is approved.

## Hypotheses

Retain the pending assessment's exact target. L050 already records
p=4+a=-3 and t=4+b=-2, with ch_2=p e_1+t e_2+tau_D and
c_2=-ch_2. With e_1=eta tensor 1 and e_2=1 tensor eta, its
restrictions have second Chern numbers 3 on S x {y} and 2 on
{x} x S. This reads existing formulas; it is not a new calculation.
Keep the full mixed action and actual real polarization
Omega=p_1^*omega_c+p_2^*omega_c. The bundle's Sp(1) structure group
and the diagonal rotation action remain distinct.

Reuse the [compatible-bundle assessment](2026-09-27-compatible-cubic-rm-stable-bundle.md),
[real-metric assessment](2026-10-04-fixed-lower-chern-stability-test.md)
and [topological assessment](2026-10-04-corrected-rank-two-topological-realization.md)
for their unchanged scopes.

## Conclusion

SPECIALIZE: the exact saved target now has ready coverage. Its
restriction argument and stable/split alternatives still need a
proof. The survivor is neither excluded nor holomorphically realized
by this review. A subsequent application should be REPRODUCTION,
without a claim beyond the checked literature.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, with
ACTUAL_TASK_TYPE literature_comparison. No lemma, mathematical script
or complete candidate is produced. Mathematical exploration usage
stays zero; the span 21 and three attained RM directions against four
required remain unchanged. The universal rational Hodge gap is open.

## Proof — inspected sources and comparison

### Connection framework and a version qualification

Read Verbitsky, *Coherent sheaves on generic K3 surfaces and tori*,
[arXiv:math/0205210v1, 20 May 2002, pp. 12--15](https://arxiv.org/pdf/math/0205210v1#page=12).
Theorem 3.9 explicitly states the invariant-Chern criterion for a
polystable bundle. Definitions 3.2--3.4, Theorem 3.5, Proposition 3.7
and Lemma 3.8 supply integrability, Hermitian Yang--Mills and
zero-contraction statements. These local statements impose no
genericity of the induced complex structure. Definition 3.3 has
inconsistent strict inequalities; use the standard slope convention
from the surface source below.

Also read Verbitsky, *Hyperholomorphic connections on coherent sheaves
and stability*, [arXiv:math/0107182v10, 24 June 2010,
pp. 12--14](https://arxiv.org/pdf/math/0107182v10#page=12).
Theorem 3.9 is stated for stable bundles. Proposition 3.7 and Lemma 3.8
again give zero contraction for invariant curvature. Total invariant
classes do not by this statement give invariant classes for each
stable summand. The bounded application can handle product splitting
separately and use the stable criterion on the remaining branch,
avoiding dependence on the older stronger formulation.

Reuse the [1993 stable criterion](https://arxiv.org/pdf/alg-geom/9307008v1#page=9)
from the compatible-bundle assessment; its general proof needs no
reproduction. A topological reduction alone does not supply a
hyperholomorphic connection. No ordinary restriction-stability theorem
is imported for arbitrary product bundles.

### Surface tools at the actual metric

Read Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication
draft: [Chapter 1, equations (2.5)--(2.6), Proposition 2.4,
PDF pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11);
[Chapter 9, Section 3.1, PDF pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175);
and [Theorem 4.9, PDF p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182).
These provide sheaf and line Riemann--Roch, Serre duality, even divisor
pairing, strict slope stability and dual stability, and the
Hermite--Einstein/polystability equivalence. Section 3.1 explicitly
allows a real Kahler class. No rational approximation of omega_c or
Picard-rank-one hypothesis is needed. These are supporting tools,
not a complete theorem for the prescribed product.

### Bounded specialization and discrimination

The main local gap is a compatible representative of the cubic action
that might reach the fourth NS-fixed RM direction. This intermediate
target tests whether the simplest topological survivor can meet the
holomorphic polystability prerequisite. An exclusion would reject this
input before transport; an inconclusive test would leave existence
open. Neither outcome settles arbitrary primitive fourfold classes.

The separate mathematical turn must discharge these obligations:

1. Retain stable and rank-one direct-sum alternatives for product
   polystability. Compare the latter with the full mixed character,
   using previously assessed Whitney and character identities. Do not
   assume invariance of each summand's classes from total invariance.
2. For the stable branch, check invariance of the full saved c_2 at
   the common metric, then import the stable criterion. Verify that
   factor embeddings commute with the quaternionic structures and
   that curvature pullback gives the surface Hermite--Einstein
   condition. Ambient contraction alone does not imply this.
3. On each factor retain both stable locally free restrictions and
   equal-slope direct sums. Compare stable cases using Riemann--Roch,
   dual stability and Serre duality; retain actual line determinants
   in split cases and test parity/effectivity and positivity against
   the real Kahler class. No zero-dimensional quotient may substitute
   for local freeness.

These are proof obligations, not a derivation of an obstruction.
Continue if the restriction passage is valid and the complete case
analysis discriminates this input. If a case remains feasible, record
it and stop this obstruction test without inferring existence or
repeating settled topological/index filters. Other nonsymmetric pairs
remain outside this assessment; transverse transport remains later work.

L039's hull result assumes Gieseker-stable torsion-free sheaves with
vector (2,0,-1); it does not automatically answer a slope-polystable
locally free restriction question at omega_c. Preserve the earlier
presentation, fixed-data and symmetric stops with their recipe scopes.
No local proof already settles this exact target.

### Search record and parked access leads

Queries on CHECKED included:

- `hyperholomorphic bundles restriction hyperkahler submanifold polystable Verbitsky`
- `K3 surface rank two stable locally free bundle c1 zero c2 2 3 4 Mukai existence`
- `"hyperholomorphic" "polystable" "restriction" Verbitsky bundle`
- `"Stable vector bundles with c1 = 0 on K3 surfaces" Yoshioka pdf`
- `"K3" "locally free" "c_2=2" stable`
- `Nakashima "stable" "K3" "c_2" "2r"`
- `"Stable vector bundles with" "K3" "pdf" Nakashima`
- `"hyperholomorphic" "restriction" "submanifold" bundle polystable`
- `"hyperholomorphic connections on coherent sheaves and stability" arxiv`

Title/reference follow-ups led to the inspected author preprints and
book. The query naming Yoshioka actually located Nakashima's paper;
no authorship inference from the query is retained. Nakashima,
*Stable vector bundles with c1=0 on K3 surfaces*, Archiv der
Mathematik 74 (2000), 148--155,
[DOI 10.1007/PL00000419](https://link.springer.com/article/10.1007/PL00000419),
was accessible only at its publisher abstract; the PDF link redirects
to a purchase page. Its necessary/sufficient existence statement is
unread and supplies no theorem evidence. Access is parked: the
selected test specializes inspected cohomological tools instead and
needs no existence theorem. The RIMS Nakashima PDF returned an
internal error; the published Verbitsky PDF returned a JavaScript
challenge. Pinned arXiv copies supply the connection inputs.

Nonprimary snippets, general Mukai moduli nonemptiness,
Picard-rank-one constructions and tangent-bundle restriction examples
are discovery leads only. A stable torsion-free moduli point need not
be locally free or slope-stable. Failed searches certify neither
novelty nor absence of a stronger theorem. No new result is derived.

## Mathlib

Coverage of the full factor-restriction target: **not checked**.
No matching declaration or absence from checked Mathlib sources is
asserted. Directly linked Verbitsky criteria, Huybrechts Theorem 4.9
and surface formulas support the application; none matches the
entire fixed-tensor target. Character/Whitney coverage is reused.
