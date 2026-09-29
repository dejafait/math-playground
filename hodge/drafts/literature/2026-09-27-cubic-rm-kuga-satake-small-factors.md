# Small abelian factors of the cubic Kuga--Satake variety — literature assessment

TARGET: Determine whether A=KS(T) at a very general point of the rank-eighteen cubic-RM locus has any nonzero abelian subquotient of dimension at most six, as a prerequisite for transferring the reviewed Weil cycles to A^4 by abelian homomorphisms.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact rank-eighteen/cubic-RM factor and subquotient terminology, spin branching, isogeny decompositions and rational descent; inspected primary statements and the same-rank example listed below. No exact factor statement for the saved E and q was identified.
SOURCE_EVIDENCE: Schlickewei, arXiv:0907.2503v1, Theorem 3.3.1, https://arxiv.org/pdf/0907.2503v1#page=9; van Geemen, arXiv:math/0609839v1, section 5.4 and Lemma 5.5, https://arxiv.org/pdf/math/0609839v1#page=16; Mayanskiy, arXiv:1210.0190v2, Corollary 1 and Theorem 1, https://arxiv.org/pdf/1210.0190v2#page=8; supporting and comparison statements below.
COMPARISON: The general RM group, complete spin restriction and rational-descent framework apply to the saved hypotheses. Published small-factor examples impose different dimension or form data; maximal-orthogonal universality bounds have a group hypothesis unavailable here. No rational factor bound for this A is imported from an example.
GAP: Apply the cited representation statements to the full H^1(A,Q), retain all constituents and multiplicities, and justify the implication for rational Hodge subquotients before comparing with the required dimension at most twelve. Neither a numerical bound nor a sharp rational factor decomposition is established in this review.
REASON: Import the general theorems and perform only this threshold specialization in a separate research turn. A complex constituent lower bound may suffice without a complete rational simple-factor classification; a positive answer still requires rational descent, Weil data and the whole tensor image.

## Hypotheses

Retain L031's full very-general data: T=T(S), dim_Q T=18,
End_Hdg(T)=E=Q(zeta_7+zeta_7^(-1)), dim_E T=6, the inherited
polarization q, and the full A=KS(T,q) with H^1(A,Q)=C^+(T,q).
The locus is the four-dimensional NS-fixed cubic-RM locus, not
an assertion about every specialization. The universal rational
target and the previous primary-statement audit are unchanged.

Subquotient means a nonzero abelian quotient of an abelian
subvariety, up to isogeny. Six is an abelian dimension bound;
twelve is the corresponding rational weight-one dimension bound.
Neither is a rank convention for T. All simple constituents of
the full Kuga--Satake variety must be retained.

## Conclusion

The exact saved target is screened. The general inputs below are
known and will be reused by citation. The remaining task is their
application to this subquotient threshold, expected to be a
REPRODUCTION, not research beyond the checked representation theory.
The present step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION.
SPECIALIZE permits the calculation only in a later invocation.

No factor-existence answer, numerical lower bound, rational
decomposition, cycle, or new lemma is obtained here. This review
does not repeat the earlier divisor obstruction: it identifies
the sources for a different necessary condition on one cycle
supply. There is no essential unread source for that bounded test.

## Proof

This section records source statements and applicability, not a
proof of the saved mathematical target. Pagination is PDF pagination
unless journal pages are explicitly given.

### RM group and the full Kuga--Satake representation

Reread Schlickewei, *The Hodge conjecture for self-products of certain
K3 surfaces*, arXiv:0907.2503v1 (15 July 2009),
[Theorem 3.3.1 and its hypotheses, p. 9](https://arxiv.org/pdf/0907.2503v1#page=9),
and the factorwise action in section 3.5, pp. 16--17. For
irreducible K3-type T with full totally real endomorphism field E,
the Hodge group on the even Clifford algebra is the image of
Res_(E/Q) Spin(Q_E). Writing d=[E:Q] and
W=Cores_(E/Q) C^0(Q_E), the theorem gives
V isomorphic to W^(direct sum 2^(d-1)) as Hodge structures,
with the corresponding matrix endomorphism algebra. The factor
with H^1=W need not be simple.

These hypotheses match the saved T. The theorem supplies the full
representation, not merely L031's sign spaces. Also reread
[Corollary 3.7.1 and its remark, pp. 18--19](https://arxiv.org/pdf/0907.2503v1#page=18):
its explicit small-factor discussion assumes dim_E T=3.
That condition is not the saved dim_E T=6, so its factor dimensions
cannot be copied. No reproof of the group theorem is warranted.

### Spin branching and half-spin dimensions

Read van Geemen, *Real multiplication on K3 surfaces and Kuga Satake
varieties*, arXiv:math/0609839v1 (29 September 2006),
[sections 5.2--5.4 and Lemma 5.5 with proof, pp. 16--17](https://arxiv.org/pdf/math/0609839v1#page=16).
For even m=2l the source states

\[
S(m)=S^+(m)\oplus S^-(m),\qquad
\dim S^\pm(m)=2^{l-1},\qquad
S(dm)|_{\mathfrak{so}(m)^d}
 =S(m)\boxtimes\cdots\boxtimes S(m).
\]

The half-spin summands are irreducible. This is the even-dimensional
branching statement relevant here; its symbols d and m have not
been numerically specialized in this review. The abstract spin
module must still be related to the full Clifford representation,
including its multiplicities, using the preceding theorem.
Section 5.2's generic full-orthogonal group assumption must not
replace the RM group. The examples in sections 5.6--5.8 again
have E-dimension three. This source supplies a representation
formula, not rational abelian factors attached to this q.

### Rational descent and the closest same-rank example

Read Mayanskiy, *Endomorphism algebras of Kuga-Satake varieties*,
arXiv:1210.0190v2 (2 November 2012),
[section 2, Lemma 3 and its corollary, pp. 3--4](https://arxiv.org/pdf/1210.0190v2#page=3),
[section 4.1, Corollary 1, p. 8](https://arxiv.org/pdf/1210.0190v2#page=8),
and [Theorem 1 and its qualification, p. 10](https://arxiv.org/pdf/1210.0190v2#page=10).
Corollary 1 describes the full even-Clifford restriction with
multiplicity 2^(d-1) relative to the tensor product of the
factorwise Clifford representations. Theorem 1 organizes rational
irreducibles and their endomorphism algebras using Galois orbits
and multiplicities; its totally real range m>=5 includes our m.
This is supporting descent machinery, not permission to declare
each complex half-spin block rational.

Read the setup of [section 7 and Example (2), pp. 23, 25--26](https://arxiv.org/pdf/1210.0190v2#page=23).
The example has d=3, m=6, but specifies a root rho of
z^3-3z+1 and the form diag(-rho,-rho,-1,...,-1). It computes
two rational constituents and their endomorphism algebras.
No identification with our E and q is supplied, so those
arithmetic factors cannot be imported. The corrected v2 was
used; the detailed cocycle calculation was not independently
reproduced.

### From subquotients to the required dimension test

Read Milne, *Abelian Varieties*, course notes v2.00 (March 2008),
[Chapter I, Proposition 10.1 with proof and the subsequent simple-factor discussion, printed pp. 42--43, PDF pp. 48--49](https://www.jmilne.org/math/CourseNotes/AV.pdf#page=48).
Poincare complete reducibility supplies complements to abelian
subvarieties up to isogeny and decomposition into simple factors.
These are standard supporting inputs for handling quotients of
subvarieties. They do not give a dimension estimate for A.

For the later test, start with an actual rational subquotient and
its H^1 before extending scalars. A positive certificate must
establish a rational polarizable Hodge summand, not just a complex
representation. For an exclusion, test whether a bound for every
complex constituent already rules out rational dimension at most
twelve. If it does, an exact list of rational simple factors is
unnecessary. This is the proposed proof obligation, not a bound
derived in this turn. Account explicitly for cohomological
contravariance and isogeny invariance.

### Stronger-looking bounds have a different group hypothesis

Read Charles, *Two results on the Hodge structure of complex tori*,
Math. Z. 300 (2022), 3623--3643,
[published Theorem 1.2, p. 3624](https://www.math.ens.psl.eu/~charles/Tori_MathZ.pdf#page=2).
Its universality conclusion assumes that the K3-type
Mumford--Tate group is the full special orthogonal group.
That is not the RM hypothesis used here.

Read Voisin, *Footnotes to papers of O'Grady and Markman*,
[11-page revised author PDF, section 2 and Theorem 2.1, pp. 6--7](https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/footnotesrevised.pdf#page=7),
accessed 2026-09-27. The subquotient bounds in that statement also
assume the full special orthogonal group and a specified tensor
embedding. They are not an unconditional bound depending only on
rank(T) for our RM locus. The revised file has no version date
verified here. Neither comparison changes the selected RM input.

### Search record and reuse

Queries on 2026-09-27 included:

- `"Kuga-Satake" "real multiplication" "decomposition" spin even dimension`
- `"Kuga-Satake" "dimension 6" "cubic"`
- `"Schlickewei" "Theorem 3.3.1"`
- `"Kuga-Satake" "real multiplication" "half spin"`
- `"Kuga-Satake" "64" "real multiplication"`
- `"Endomorphism algebras of Kuga-Satake varieties" arxiv`
- `"Kuga-Satake" "eighteen" factors`
- `"Kuga-Satake" "dim" "6" "cubic field"`
- `"Kuga-Satake" "subquotient" spin`
- `"Kuga-Satake" "small" "factors" "real multiplication"`

The numeric query was a search probe, not a calculated or adopted
bound. Follow-up searches located the original PDFs and the
abelian reducibility reference. Inspected theorem text, not search
snippets, supports the comparisons above. Schlickewei's thesis,
the original Fulton--Harris treatment, and Poon's Picard-rank-14
construction remain uninspected leads for this step; none is
needed for the selected threshold test. No originality is inferred
from failing to locate the exact statement.

Reuse the [exceptional-cycle review](2026-09-27-cubic-rm-exceptional-weil-cycles.md)
for the supplies, and the [divisor review](2026-09-27-cubic-rm-kuga-satake-divisor-tensor.md)
and L031 for their distinct obstruction. The earlier support and
bundle failures remain scoped as recorded. This review does not
reopen those recipes or redo L031's tensor calculation.

### Relevance, remaining work and stopping test

The main local gap is algebraic realization of the cubic action
beyond the Dickson family. The proposed intermediate target is
the existence of a small abelian subquotient needed by the
selected homomorphism-based exceptional-cycle supply. The
downstream objective is still the whole beta_U, including the
component already detected in L031; algebraic kappa is a separate
requirement. Arbitrary primitive fourfold classes and higher
dimensions remain outside this route.

Continue the bounded factor test by applying the inspected
formulas to the saved data and comparing with twelve, retaining
rational descent and all multiplicities. Stop the low-dimensional
homomorphism recipe if every nonzero rational weight-one
subquotient exceeds that threshold. If a small factor exists,
its required Weil data and full tensor image must be checked
before treating it as a useful cycle supply. A merely inconclusive
bound is not a positive answer. Generalized Pryms, higher-dimensional
sources and arbitrary algebraic correspondences remain outside
this exclusion test.

This is consecutive exploration turn two after L031's informative
negative result, within the same three-turn allowance. The
preserved target now has a ready SPECIALIZE assessment; the next
turn must complete the test and continuation/stop assessment
within that allowance, without renaming the route to reset it.
The attained span stays 21 on the Dickson family and three
directions against four required. No complete candidate appears.

## Mathlib

Coverage: **not checked** for the full factor statement or its
supporting representation and reducibility results. No Mathlib
theorem name or absence is asserted. The named citations above
match their stated general inputs; none is presented as a theorem
already deciding the exact saved subquotient question.
