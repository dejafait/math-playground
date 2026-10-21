# L130 — Equality diagonal restriction has compatible stable charge twenty-five

## Hypotheses

Retain the identical marked projective K3 factors S of L071, the common
ordered hyperkähler structures I,J,K, the common metric g, and L044's
exact real Kähler class h. Write X=S x S and Omega=p_1^*h+p_2^*h.
Let eta generate H^4(S,Z) with integral one, e_1=eta tensor 1 and
e_2=1 tensor eta. Use L071's full integral mixed tensor tau_D. Its
cup-product correspondence operator is q-self-adjoint and satisfies

\[
D|_N=2A_c+4\pi_K,\qquad D|_T=2U,
\]

where N=NS(S)_Q has dimension four, T=N^perp has dimension eighteen,
A_c has characteristic polynomial z f(z), pi_K is the projection to
its one-dimensional kernel, and f(z)=z^3+z^2-2z-1. The field Q(U)
has degree three, with U corresponding to a root of f. These are the
operators and dimensions in L025, L044 and L071, not only their
restrictions to the metric's positive three-plane.

Suppose that a locally free holomorphic rank-two bundle F on X is
slope-polystable at Omega and has integral c_1(F)=0 and

\[
\operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\tag{1}
\]

No existence of F is asserted. Let delta:S -> X be the algebraic
diagonal z -> (z,z). No arbitrary graph is considered.

## Conclusion

The actual restricted bundle E=delta^*F, if F exists, is locally free
and slope-polystable at h, with integral Chern classes

\[
c_1(E)=0,\qquad c_2(E)=25\eta.
\tag{2}
\]

In fact E must be slope-stable at h: its charge is not a split value
14r^2. The stable Euler test c>=4 passes and gives chi(E)=-21 and
h^1(E)=21. This is a necessary non-exclusion result, not an existence
theorem for E or F. This diagonal filter is therefore parked. It
neither excludes the equality kernel nor supplies a cycle, image
separation, compact ambient extension, reconstruction or transverse
transport. Universal primitive rational Hodge realization is unchanged.

The calculation is a NEGATIVE / REPRODUCTION specialization of the
assessed connection, Chern-naturality and surface tools. The separate
2026-10-19 critical audit below preserves this conditional conclusion;
no progress beyond the sources checked or certified originality is claimed.

## Proof

**Actual metric and curvature pullback.** The prescribed data are
L071's a=-18,b=-25 case, so its stable-product passage applies and
supplies an actual compatible unitary hyperholomorphic connection
nabla on the hypothetical F. This imports Verbitsky,
*Hyperholomorphic connections on coherent sheaves and stability*,
[math/0107182v10, Theorem 3.9, Section 3](https://arxiv.org/html/math/0107182v10#S3),
under the stability and invariant first-two-Chern-class hypotheses
checked there. It is not a claim that arbitrary stable restrictions
remain stable.

For tangent vectors u,v on S,

\[
(\delta^*(g\oplus g))(u,v)=g(u,v)+g(u,v)=2g(u,v).
\]

Its ordered complex structures are exactly I,J,K and its I-Kähler
class is 2h. For A in {I,J,K},
d delta(Au)=(Au,Au)=(A direct sum A)d delta(u).
Thus d delta intertwines every quaternionic rotation. For the actual
curvature R of nabla, naturality gives R_E=delta^*R; equivariance of
d delta shows that R_E is an SU(2)-invariant endomorphism-valued
surface two-form. The action concerns the form arguments and leaves
the coefficient endomorphisms unchanged. Apply Verbitsky,
[Proposition 3.7 and Lemma 3.8, Section 3](https://arxiv.org/html/math/0107182v10#S3),
coefficient by coefficient: Lambda_(2h) R_E=0. The pulled-back
unitary connection is compatible with E's actual holomorphic
structure. The real-Kähler Hermite–Einstein correspondence,
Huybrechts, *Lectures on K3 Surfaces*,
[Chapter 9, Definition 4.7, Remark 4.8 and Theorem 4.9, printed pp. 181–182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
therefore gives slope-polystability at 2h.

On a surface, replacing h by 2h multiplies every coherent subsheaf's
slope by two. All stability, semistability and equal-slope direct-sum
conditions are consequently identical. Equivalently,
Lambda_(2h)=(1/2)Lambda_h. Hence E is polystable at the exact h;
no factor-restriction stability assertion or rational replacement of
the polarization has entered.

**Full mixed contraction.** Use Chern naturality for the finite locally
free F and the diagonal, as in
[Stacks, Lemma 42.38.9(2), Tag 02UA](https://stacks.math.columbia.edu/tag/02UA),
and the character polynomial in
[Stacks, Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
The diagonal is a regular algebraic embedding; no flatness is required
for pulling back the bundle or its integral topological Chern classes.
In particular c_1(E)=0 integrally and ch_2(E)=delta^*ch_2(F).
Both e_1 and e_2 pull back to eta.

Here is the complete cup/trace identity with its sign fixed. Put
V=H^2(S,Q) and choose any rational basis b_1,...,b_22 with q-dual
b^1,...,b^22, so q(b_i,b^j)=delta_i^j. The convention for tau_D
sends a tensor x tensor y to the map w -> q(w,x)y. Therefore

\[
\tau_D=\sum_{i=1}^{22} b_i\otimes Db^i,
\qquad
\delta^*\tau_D=\sum_i b_i\smile Db^i
 =\left(\sum_i q(b_i,Db^i)\right)\eta
 =\operatorname{Tr}_{\mathbb Q}(D)\eta.
\tag{3}
\]

Indeed w=sum_i q(w,b_i)b^i proves the first equality, and the
q(b_i,-) are the coordinate functionals dual to the basis b^i,
so the last sum is the ordinary linear trace of D. Each factor
has degree two; no odd-degree interchange sign or factorial occurs
in (3). This computation is on the whole rational cup space, not
an assumed integral orthogonal decomposition.

For its evaluation we may use the rational orthogonal decomposition
V=N direct sum T. By L025, Tr(A_c)=-1, since its characteristic
polynomial is z f(z); conjugation to L044's final chamber preserves
the trace. Since Tr(pi_K)=1,

\[
\operatorname{Tr}(D|_N)=2(-1)+4=2.
\tag{4}
\]

The T-space is a six-dimensional vector space over the cubic field
Q(U), since dim_Q T=18. On each field copy U is multiplication by
the defining root, whose field trace is -1 by f's quadratic
coefficient. It follows that

\[
\operatorname{Tr}(D|_T)=2\cdot6\cdot(-1)=-12,
\qquad \operatorname{Tr}(D)=-10.
\tag{5}
\]

In particular both rational blocks have been retained; the metric
eigenvalue alone would not compute (3). Substituting (3)–(5) in (1)
gives

\[
\operatorname{ch}_2(E)=(-14-21-(-10))\eta=-25\eta.
\tag{6}
\]

For c_1(E)=0 the character formula is ch_2(E)=-c_2(E), proving
(2). Although the trace was evaluated rationally, the pulled-back
c_2 is integral; H^4(S,Z)=Z eta is torsion-free, so (6) determines
the integral class. No integral N/T splitting is needed.

**Exact-h alternatives and verdict.** L052 proves that a rank-two
locally free polystable bundle with c_1=0 at this h is either stable
with charge c>=4, or split as L direct sum L^(-1) with
c=14r^2, r an integer. The zero-slope line lattice is precisely
Z k with k=(-4,-2,1,2) and k^2=-14. Scaling h to 2h changes
neither that lattice nor any slope condition. Thus these are the
appropriate alternatives for the actual diagonal restriction.

The value 25 is not divisible by 14, so the split alternative is
impossible. The stable alternative passes since 25>=4. L052's
stable endpoint vanishings and surface RR give
H^0(E)=H^2(E)=0 and 4-25=-h^1(E), yielding the stated cohomology.
There is no contradiction. Passing this necessary stable test
does not construct a diagonal bundle or extend one to X. This is
the stipulated stopping test for the single approved calculation;
it does not reopen earlier stopped collision or vanishing routes.

**Separate critical audit, 2026-10-19.** The pre-invocation assessment
for this exact audit is SPECIALIZE. The following checks reuse its
inspected primary theorem hypotheses; they do not treat the assessment
or the original calculation's numerical answer as verification.

First, the connection theorem is applied on X only after stability is
justified. Here p=-14,t=-21 correspond to a=-18,b=-25 in L071.
If F were a two-line polystable sum, Künneth and H^1(S)=0 would make
its mixed character a product of divisor classes. That operator kills
sigma, whereas the prescribed operator sends sigma to -2lambda sigma.
Thus L071 really supplies a stable F with invariant c_1,c_2, the
hypotheses of Verbitsky's Theorem 3.9. This is not an assertion that
irreducibility alone makes a connection on a product split.

The diagonal differential is (u,u); the same ordered I,J,K on both
factors is essential. Its curvature is R((u,u),(v,v)), which retains
both pure blocks and both mixed blocks of R. Equivariance of this
whole expression proves invariance without discarding mixed curvature.
The induced metric is exactly 2g. Zero contraction for its invariant
surface two-form gives a compatible Hermite–Einstein connection, and
the cited real-Kähler correspondence gives polystability. Scaling
every subsheaf slope by two identifies the tests at 2h and h. Neither
ordinary restriction stability nor a rational-polarization substitution
is needed. These checks preserve the actual-connection passage.

Independently, the dual-basis formula in (3) represents exactly the
stated correspondence convention: contraction against w reconstructs
Dw, not D squared. Pullback is ordinary degree-two cup product, with
positive interchange sign. For the divisor trace one can also read
L025's displayed A_0 matrix: its diagonal is (1,0,-2,0), of trace -1.
Chamber conjugation preserves this trace, and its one-dimensional
kernel projection has trace one. On T the field action has dimension
18/3=6 over Q(U); multiplication by its defining root has trace -1
on each field copy. The complete trace is therefore 2-12=-10. This
checks the full-space answer independently of the metric eigenvalue
and of the mixed-square computation used elsewhere.

Integral topological Chern naturality applies to the actual pullback
bundle along the smooth algebraic diagonal. Stacks 02UA supplies the
related algebraic Chern-operation compatibility, not by itself an
integral singular-cohomology theorem. The character polynomial gives
ch_2=-c_2 because the integral c_1 is zero. Thus the rational calculation
-14-21+10=-25 determines c_2=25 eta integrally, since H^4(S,Z) has no
torsion. There is no integral N/T decomposition assumption or missing
factor of two in this identification.

Finally the surface test applies to E itself, independently of how its
connection was obtained. For a nonstable polystable E, the rank-one
stable summands are line bundles, their product is trivial by Picard
injection, and both have zero slope. In L052's integral basis the
three independent coefficients in q(l,h) force l=r(-4,-2,1,2).
With L025's G, G(-4,-2,1,2)^T=(0,0,0,-7)^T, so l^2=-14r^2.
The split charge is indeed 14r^2, excluding 25. In the stable branch
the section and dual-section vanishings give chi(E)=4-25=-21 and
h^1(E)=21. These are compatible necessary data, not an existence
argument. No substantive error or stronger obstruction was found.
The parked-filter verdict survives this audit; all independent
existence and transport gaps remain open. This audit is REPRODUCTION
and confirmation, not a second mathematical advance.

## Mathlib

Full diagonal specialization, exact-h stable/split classification and
the matching bundle statement: **not checked**. No absence claim is
made. The cited primary theorems and canonical local inputs supply
the informal argument. The finite-dimensional trace calculation is
written out to verify its specialization and signs, not to reprove
the imported general connection or Chern-class theorems.
