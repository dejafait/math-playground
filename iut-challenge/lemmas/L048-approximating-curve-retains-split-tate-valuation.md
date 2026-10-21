# L048 — Approximation retains split reduction and Tate valuation

## Hypotheses

Retain L044's fixed algebraic closure Omega of Q_3, absolute valuation
v_3(3)=1, embedded H=Q_3(zeta_60) and
N=Q_3(zeta_420,3^(1/7)). Its standard Tate curve has q=3^30 and
integral monic cubic

f(x)=x^3+(1/4)x^2-b_2(q)x-b_3(q).

The symbols b_2(q),b_3(q) are Milne's Tate-series labels, not the
general Weierstrass b-invariants. Let M_tors be a sufficient integer
precision from L044's Bisatt–Dokchitser application at m=210,
including the squarefree neighborhood. Fix any integer

M>=max(M_tors,31).

Let g=x^3+c x^2+d x+e be a monic integer cubic congruent to f
coefficientwise modulo 3^M in Z_3[x]. Give E_0:y^2=g(x) its
point at infinity. Global coordinate division fields below contain
both coordinates of every geometric torsion point.

## Conclusion

The original integral equation for E_0 is minimal over Q_3 and has
discriminant valuation 30 and unit c4. E_0 over Q_3 has split
multiplicative reduction. Its unique geometric Tate parameter
q_0 in Q_3 with 0<|q_0|_3<1 satisfies

v_3(q_0)=30,

and E_0 over Q_3 is isomorphic over Q_3 to the standard Tate curve
E_(q_0). No equality q_0=3^30 is asserted.

There exists such a g for which all of L046's conclusions also hold.
Apply L045 and L047 to that same choice, with
F=Q(zeta_60,E_0[30]) and D=F(E_0[7]). Then the full 30-torsion
is F-rational, F/Q is Galois with degree dividing 2^14*3^3*5,
the induced embedded completions are F_u=H and D_w=N, and
rho_(E_0,7)(G_F) contains SL_2(F_7). The full global mod-7 image
over Q is GL_2(F_7), and the complete local 210-torsion module
agrees with that of L044's original E_q.

This is a known-method specialization validated by the separate
2026-10-11 critical audit below. It closes one local geometric prerequisite, not sufficient
initial theta data or the original finite B>=A comparison.

## Proof

### Cited inputs and specialization scope

Reuse the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-11-approximating-curve-geometric-tate-parameter.md`.
J.S. Milne, *Elliptic Curves*, second edition (2021),
[II.2, pp.52–53, Theorem 2.4; II.3, pp.58–61; III.3,
(23)–(26), pp.102–103](https://www.jmilne.org/math/Books/EC2.pdf),
supplies the general integral invariant formulas, nodal reduction
criterion and standard Tate coefficient/product formulas.
J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second
edition (1997), [III.1 (3.1.2)–(3.1.3), pp.62–63; III.2,
Tate's Algorithm, pp.66–67](https://johncremona.github.io/book/fulltext/chapter3.pdf),
supplies invariant scaling and the characteristic-3/multiplicative
branches. K.S. Kedlaya, *Introduction: the Tate curve*, fall 2004,
[Theorem 2, p.4](https://kskedlaya.org/18.727/tate-curve.pdf),
states the named Tate parameter theorem. Import these results,
without reproving Tate uniformization or local constancy. The extra
work is the congruence, minimality and split-node test for this cubic;
finite-torsion agreement alone would not prove them.

### Integral invariants and the fixed precision

For the equation y^2=x^3+c x^2+d x+e the general coefficients are
(a1,a2,a3,a4,a6)=(0,c,0,d,e). Denote their b-invariants by B_i
to avoid confusing them with the Tate series. Substitution gives

B2=4c, B4=2d, B6=4e, B8=4ce-d^2,
c4=B2^2-24B4=16c^2-48d,
Delta=-B2^2 B8-8B4^3-27B6^2+9B2 B4 B6
     =16(c^2 d^2-4d^3-4c^3 e-27e^2+18cde).

These are polynomials with integer coefficients. Consequently
coefficientwise congruence modulo 3^M preserves their values modulo
3^M: for each monomial the difference of its two evaluations is
a sum of terms each containing a coefficient difference.

L044 completes the square from the standard Tate equation by
t=y+x/2, without scaling x or y. This is a Weierstrass coordinate
change with u=1, so the displayed discriminant evaluated on f is
exactly the Tate discriminant, not a rescaled one. Its value is

Delta(f)=3^30 U, where U=product_(r>=1)(1-3^(30r))^24
belongs to 1+3^30 Z_3.

For completeness, each factor differs from 1 by an element of
3^(30r) Z_3. A finite product over r>=R differs from 1 by an
element of 3^(30R) Z_3. Thus the partial products are Cauchy and
their limit is in 1+3^30 Z_3, which consists of units.
This checks the convergent product needed for the valuation.
Write Delta(g)=Delta(f)+3^M z with z in Z_3. Then

Delta(g)=3^30(U+3^(M-30)z).

Since M>=31, the parenthesis is a unit, proving v_3(Delta(g))=30
and nonsingularity. This is a sufficient threshold, not a claimed
optimal one; the existence and effective value of M_tors are separate.

L044's integral Tate series have zero constant terms, so
b_2(q),b_3(q) belong to 3^30 Z_3. The congruences therefore give
c=1/4=1 modulo 3 and d=e=0 modulo 3. In particular c4(g)=1
modulo 3, hence v_3(c4(g))=0.

### Local minimality and splitness in residue characteristic 3

If a pointed Q_3-isomorphic integral Weierstrass equation had a
smaller discriminant valuation, the general coordinate change would
give u^12 Delta'=Delta(g) and u^4 c4'=c4(g), with u in Q_3^times.
The first equality would force v_3(u)>0. The second would then
give v_3(c4')=-4v_3(u)<0, impossible because c4' is an integral
polynomial in that equation's integral coefficients. Thus the
original equation is minimal over Q_3. This argument permits all
general Weierstrass models, including nonzero a1 and a3; it does not
compare only short equations or assume global minimality.

Its reduced affine equation over F_3 is

y^2=x^3+x^2.

For F(x,y)=y^2-x^3-x^2 the partials in characteristic 3 are
F_x=x and F_y=2y. Hence (0,0) is the only affine singular point,
even over the algebraic closure. The only point at infinity is
[0:1:0]; for the homogeneous equation Y^2 Z-X^3-X^2 Z its
Z-partial at that point is 1, so it is smooth. At (0,0) the
quadratic tangent cone is y^2-x^2=(y-x)(y+x). These are distinct
lines defined over F_3, as 1 and -1 are distinct there. Thus this
minimal model has a split node and split multiplicative reduction.
The general nodal criterion is applicable at characteristic 3;
no short-model square test restricted to p!=2,3 is used.

As a direct check against Cremona's p=3 branch, B2=1 and B4=0
modulo 3 and a1=a3=0. Its initial r=-B2 B4 and t=a1 r+a3
are both zero modulo 3, so the adjusted residue equation is this
same model. Its multiplicative quadratic is X^2+a1 X-a2=X^2-1,
with two roots over F_3. This agrees with the tangent computation;
none of the later additive branches is needed.

### The changed curve's geometric parameter

The invariant formula now gives
v_3(j(E_0))=3v_3(c4(g))-v_3(Delta(g))=-30.
Thus |j(E_0)|_3>1. Apply the cited Tate Theorem 2 over K=Q_3:
there is a unique nonzero q_0 in Q_3 with |q_0|_3<1 giving the
geometric Tate isomorphism. Because split multiplicative reduction
has been proved, that isomorphism is defined over Q_3 itself.

Use Milne's standard integral Tate series at this q_0. Their zero
constant terms imply b_2(q_0) in q_0 Z_3; the product
U_0=product_(r>=1)(1-q_0^r)^24 converges to a unit in Z_3 by
the same tail-product argument, since v_3(q_0)>0. Formula (26) gives

q_0 j(E_(q_0))=(1+48b_2(q_0))^3/U_0,

which is a unit. Invariance of j under the Tate isomorphism
therefore yields v_3(q_0)=-v_3(j(E_0))=30. This uses the complete
convergent expression, not a numerical truncation. The valuation
is the absolute one with v_3(3)=1, not a uniformizer-normalized
valuation in H or N and not the valuation of a pilot root.

### Reselection and same-curve retention

Choose the stronger M once, before using L046. A congruence modulo
3^M implies congruence modulo 3^(M_tors), so L044's full local
210-module constancy and squarefree neighborhood still apply.
L046 explicitly works at any fixed sufficient M and therefore
supplies a monic integer g in this stronger neighborhood with full
global mod-7 image GL_2(F_7). Its lattice count requires only that
M is fixed; no estimate uniform in M is needed. All preceding
reduction/parameter conclusions hold for every g in the neighborhood,
so they hold for that reselected curve without a second selection.
The short scaled equation used for L046's counting does not replace
the original cubic in the minimality or residue tests.

Apply L045 to exactly this E_0 to obtain its field F, degree
divisibility, full rational 30-torsion and embedded completions
F_u=H and D_w=N. L047 applies to the same E_0 and F and supplies
SL_2(F_7) containment over F. Their hypotheses are unchanged:
the full local 210-module and the global image over Q have both
been retained. These results are reused, not reproved.

All tests for this target pass. The result supplies local progress
by known methods; it does not establish progress beyond the sources
checked or an essential IUT flaw. ATTEMPTS/027 excludes the exact
curve with q=3^30 and is not reopened: this is a changed curve with
only the same parameter valuation and finite modules asserted.
Other-place conditions, sufficient field-of-moduli/global initial
data, native/input/action realization, marked pilot transport,
essentiality and the original finite B>=A comparison remain open.

### Separate critical audit — 2026-10-11

**Verdict and scope.** The unchanged statement passes the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-11-approximating-curve-geometric-parameter-critical-audit.md`.
Reuse its inspected primary criteria, cited above, and the completed
input audits. No stronger constancy theorem, new reduction theorem or
additional direct lemma input is required. The following verifies the
specialization independently of the construction's verdict.

**Invariant algebra and precision.** Substituting
(a1,a2,a3,a4,a6)=(0,c,0,d,e) into the general integral formulas
gives B2=4c, B4=2d, B6=4e and B8=4ce-d^2. The four discriminant
terms expand respectively to

-64c^3 e+16c^2 d^2, -64d^3, -432e^2, 288cde.

Their sum is precisely the displayed 16 times the cubic
discriminant. Likewise c4=16c^2-48d. In particular no division
by 3 or 1728 occurs in these polynomials. The square completion
t=y+x/2 changes (a1,a2)=(1,0) to (0,1/4), with u=1; the
invariant scaling laws therefore retain the original Tate Delta.
All coefficients belong to Z_3, including 1/4, so evaluating any
integer polynomial at coefficient tuples congruent modulo 3^M
gives values congruent modulo 3^M. This applies to the actual
original cubic, irrespective of L046's later scaled short model.

For q=3^30, each factor (1-q^r)^24 lies in 1+3^(30r)Z_3.
Any finite tail starting at r=R consequently lies in
1+3^(30R)Z_3. Since every partial product is a unit, these tail
bounds also bound the differences of partial products, proving
convergence and that the limit U lies in 1+3^30 Z_3. Thus the
complete product gives Delta(f)=3^30 U, not just a truncated
approximation. The error in Delta(g) has valuation at least M.
The required strict inequality is M>30, and the stated M>=31
ensures it. Hence U+3^(M-30)z reduces to 1 and cannot cancel.
This proves both v_3(Delta(g))=30 and nonsingularity. Precision
M=30 would not justify this argument; no such weakening is used.

The integral positive-degree Tate series give b_i(3^30) in
3^30 Z_3: their terms have valuations tending to infinity and
each is divisible by 3^30. Accordingly c=1,d=e=0 in F_3,
and c4=16c^2-48d=1 there. These are statements about the
original integral model, not invariants of a presumed integral
isomorphism to the short model used for counting.

**Minimality and the complete residue curve.** For an arbitrary
pointed Q_3-isomorphic integral Weierstrass equation, the cited
general transformation laws read Delta(g)=u^12 Delta' and
c4(g)=u^4 c4'. A strictly smaller v_3(Delta') would force
v_3(u)>0, giving v_3(c4')=-4v_3(u)<0. But the general c4'
polynomial is integral on every integral Weierstrass equation,
including those with nonzero a1',a3'. Thus no integral model with
smaller discriminant exists. This proves precisely the minimality
needed by the nodal reduction criterion.

For the reduced affine equation F=y^2-x^3-x^2, the partials are
F_x=x and F_y=2y in characteristic 3. Their simultaneous zero
locus consists only of (0,0), which lies on the curve. On the
projective equation, Z=0 forces X=0; the only point there is
[0:1:0], and the Z-partial is Y^2-X^2=1 at that point.
Thus there is no omitted singularity at infinity. The degree-two
part at the unique singularity is (y-x)(y+x), with distinct
F_3-rational tangent lines. Milne's general nodal criterion applies
in this residue characteristic and proves split multiplicative
reduction. In the inspected Cremona p=3 adjustment, B2=1,B4=0
and a1=a3=0 give r=t=0; its multiplicative residue quadratic
is X^2-1, with roots 1 and 2. This checks the relevant algorithm
branch without importing a short-form test that excludes p=3.

**Tate hypotheses and the whole analytic expression.** The invariant
ratio yields v_3(j)=-30, so E_0/Q_3 meets Kedlaya Theorem 2's
finite-extension and |j|>1 hypotheses. That named theorem gives
the unique q_0 in Q_3 with 0<|q_0|<1; the already proved splitness
gives the isomorphism over Q_3. For this q_0, let s=v_3(q_0)>0.
The product tails lie in 1+q_0^R Z_3, so the full U_0 converges
to a unit. Integral positive-degree coefficients give
b_2(q_0) in q_0 Z_3. Therefore 1+48b_2(q_0) is a unit, and
Milne's complete identity

q_0 j(E_(q_0))=(1+48b_2(q_0))^3/U_0

has valuation zero on the right. The j-values of the isomorphic
curves coincide, giving s-30=0. This proves v_3(q_0)=30 in
the fixed absolute normalization. No coefficient from the warned
Kedlaya display, truncated series, q-root or normalization in H,N
has been substituted for Milne's identity. In particular this
calculation does not identify q_0 with the old q=3^30.

**One fixed precision and one curve.** Choose an integer
M>=max(M_tors,31) first. Every monic integer cubic in that
3^M-neighborhood belongs to L044's squarefree 3^(M_tors)
neighborhood. Its entire local 210-module statement therefore
holds for every member. L046 quantifies over any such fixed M;
its positive count has fixed leading constant 4/3^(2M+10), and
the full-box exceptional count is o(R^2) as R tends to infinity
at this fixed M. It thus supplies one member with full global
GL_2(F_7) image. The reduction and parameter checks above hold
for every member and hence for this same chosen E_0. There is
no interchange of the limits in M and R or second incompatible
curve selection.

L044's restriction of the complete module to the actual G_H gives
full H-rational 30-torsion and the pointwise-kernel equality for
the embedded 7-division field N. L045's hypotheses require exactly
these conclusions for the chosen curve, so its F and D are the
same Q(zeta_60,E_0[30]) and F(E_0[7]) used here. Its audited
global/local torsion-set agreement and closure argument give
F_u=H and D_w=N in Omega, together with the stated Galois degree
divisibility and rational 30-torsion. L047 then uses this same F
and L046's full image; both its Galoisness and prime-to-7 index
hypotheses hold. Its conclusion is SL_2(F_7) containment over F,
not a claim of full GL_2 image there. Thus all retained conclusions
hold simultaneously. L042 is retained through L044; the direct
inputs remain L044,L045,L046,L047, with no DAG change.

Every approved test passes, with no mathematical correction needed.
This validates a local prerequisite by known methods and makes no
claim beyond the checked sources. ATTEMPTS/027's exact-curve stop
and ATTEMPTS/022,025,026 remain intact. Sufficient initial data,
conditions at other places, native/input/action realization, marked
pilot transport, essentiality and original finite B>=A remain open.
No numerical certificate or mathematical script is needed for these
symbolic and quantified checks; full matching Mathlib coverage is
still unchecked.

## Mathlib

Full matching coverage of this simultaneous approximation,
characteristic-3 split-reduction and geometric-parameter conclusion
has not been checked in Mathlib. No absence claim is made. The
primary cited invariant, reduction and Tate theorems supply the
inputs; the integral congruence and same-curve arguments are their
explicit specialization. No mathematical script or numerical
evidence is used.
