# Corollary C032i: obstruction to the fixed coupled polynomial core intertwiner

## Hypotheses

Use C032e's full smooth theta density Psi, its positive-axis bound (8),
and the unchanged operators A,B of C032f(1)-(3). In particular, put

\[
 v(t)=\Psi(t)\begin{pmatrix}e^{-t/8}\\e^{t/8}\end{pmatrix},\qquad
 a(t)=(1+t)v(t),\qquad
 b(t)=\big((1-c)-(1+c)t\big)v(t),\quad t>0.
 \tag{1}
\]

The scalar c is the fixed finite value in C032f. The component order is
sigma=-1,+1. The spaces are the unweighted complex spaces
H=L2((0,infinity);C), Y=L2((0,infinity);C^2), with the single input
core D=C_c^infinity((0,infinity);C). Thus
Af(x)=integral a(x+y)f(y)dy and Bf(x)=integral b(x+y)f(y)dy.

Let p,q be real scalar polynomials and P,Q real symmetric two-by-two
matrix polynomials, all of degree at most two, with

\[
 p(0)=0,\quad P(0)=0,\quad p(x)>0,\quad P(x)>0\quad(x>0),
 \tag{2}
\]

where the last inequality is positive definiteness. Set
T_H f=-(pf')'+qf and T_Y g=-(Pg')'+Qg, with matrices acting on
columns on the left. Proposed intertwining means the local identities
T_Y Af=A T_H f and T_Y Bf=B T_H f for every f in D, as smooth
functions on the open half-line. No closed operator domain, L2
membership of the differentiated outputs, or self-adjoint realization
is assumed.

## Conclusion

There are no p,q,P,Q satisfying these hypotheses and both compact-core
intertwining identities. This includes nondiagonal P,Q, linear p,
constant q,Q, singular endpoint leading coefficients, and all allowed
degree degeneracies. The contradiction already follows from a necessary
first-derivative system; it is unnecessary to solve the potential equations.

This rejects only this fixed differential class. It determines neither
delta in C032f nor its actual-range inclusion or relative-output bound.
It supplies no completed source metric, signed-Xi inequality, transport,
initialization, all-degree assembly, or RH candidate. No extension to
higher degree or other interfaces is claimed.

## Proof

### Known calculus and the required rectangular adaptation

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-17-coupled-hankel-core-test-review-1288.md`.
Reuse the primary comparison in source-notes1288. The known compact-input
Green calculation is Gordon Blower, *Hankel operators that commute with
second-order differential operators*, J. Math. Anal. Appl. **342**
(2008), 601-614, [arXiv:0712.1013v1](https://arxiv.org/pdf/0712.1013v1),
Theorem 2.1, proof (2.3)-(2.5), printed pp.3-4,
[DOI](https://doi.org/10.1016/j.jmaa.2007.12.028).
For matrix right action, use W. Riley Casper, F. Alberto Grunbaum,
Milen Yakimov and Ignacio Zurrian, *Matrix valued discrete-continuous
functions with the prolate spheroidal property and bispectrality*,
[arXiv:2302.05750v2](https://arxiv.org/html/2302.05750v2),
Section 2.3/(2.4), Definition 5.3 and Proposition 5.4. Those references
supply Green calculus, not a rectangular theta existence or exclusion
theorem. Their bispectral existence hypotheses are not imported.

Here the output acts on columns on the left. The needed adaptation
is made explicit, since the input and output dimensions differ. For a
smooth two-component column k(t), let Gamma_k f(x)=integral k(x+y)f(y)dy.
For fixed f in D and x in a compact positive interval, local smoothness
of k bounds its first two derivatives on the relevant compact rectangle.
Differentiation under the integral is therefore valid. Moving T_H off
f, component by component, gives

\[
 \Gamma_k T_Hf(x)
 =[-k(x+y)p(y)f'(y)+k'(x+y)p(y)f(y)]_0^\infty
 +\int_0^\infty\big[-p(y)k''(x+y)-p'(y)k'(x+y)+q(y)k(x+y)\big]f(y)\,dy.
 \tag{3}
\]

Both endpoint brackets vanish: f and f' vanish on
neighborhoods of zero and infinity. If applying the cited compact-support
Green identity, first choose a smooth compact cutoff chi(y) equal to
one on a neighborhood of supp(f). For each fixed x apply it to each
scalar component chi(y)k_j(x+y) and f(y). All terms involving derivatives
of chi have disjoint support from f and its derivatives. This proves the
same formula without pretending that the kernel slice is compactly
supported. No decay of k' at infinity is used. There is no integration
in x, so no output-endpoint bracket is being suppressed.

On the output side differentiation gives the integrand
-P(x)k''-P'(x)k'+Q(x)k. Thus the necessary kernel identity is

\[
 D(x,y)k''(t)+E(x,y)k'(t)+Z(x,y)k(t)=0,\quad t=x+y,
 \tag{4}
\]
\[
 D=p(y)I-P(x),\qquad E=p'(y)I-P'(x),\qquad Z=Q(x)-q(y)I.
\]

Indeed the difference of the two core expressions is the integral of
the left side against every compact smooth scalar f. For each fixed x,
the fundamental lemma applied to each continuous component forces (4)
for every y>0. If the proposed equalities were initially only almost
everywhere in x, local smoothness first upgrades each equality for each
fixed f to all x; no uncountable intersection of exceptional sets is
needed. There is no conjugation of k: these integral maps are complex
linear. Testing componentwise with real test functions already suffices.
The real scalar p,q and the left matrix products have exactly the order
shown in (3)-(4); no right-action or transpose convention is assumed.

### Eliminating both potentials with the unchanged kernels

The exact constant combinations

\[
 (1+c)a+b=2v,\qquad (1-c)a-b=2t v
 \tag{5}
\]

hold for the same fixed c. There is no division by 1+c or 1-c.
Linearity over C and the use of one common T_H,T_Y therefore imply
(4) for both k=v and k=tv. With primes denoting t derivatives,
(tv)'=v+tv' and (tv)''=2v'+tv''. Subtract t times the v equation
from the tv equation. The resulting necessary identity is

\[
 2D(x,y)v'(t)+E(x,y)v(t)=0\qquad(x,y>0).
 \tag{6}
\]

Both potentials have canceled, including all nondiagonal entries of Q.
This is only a necessary subset; a contradiction in it suffices.

### Exact polynomial coefficients, with nondiagonal terms retained

Write

\[
 p(y)=\alpha y^2+\beta y,\qquad P(x)=M x^2+N x,
 \tag{7}
\]

where alpha,beta are real and M,N are real symmetric matrices. Fix any
t>0 and let 0<x<t, y=t-x. Then

\[
 D=(\alpha t^2+\beta t)I
   -x\big((2\alpha t+\beta)I+N\big)+x^2(\alpha I-M),
\]
\[
 E=(2\alpha t+\beta)I-N-2x(\alpha I+M).
 \tag{8}
\]

Equation (6) is a vector polynomial in x vanishing on (0,t), so each
coefficient is zero. The complete coefficients at x^2,x,1 are

\[
 2(\alpha I-M)v'=0,
 \tag{9}
\]
\[
 -2\big((2\alpha t+\beta)I+N\big)v'-2(\alpha I+M)v=0,
 \tag{10}
\]
\[
 2(\alpha t^2+\beta t)v'+\big((2\alpha t+\beta)I-N\big)v=0.
 \tag{11}
\]

No off-diagonal matrix entry has been set to zero in obtaining these
identities. Only (9)-(10) will be needed.

C032e (8), restricted to the positive axis, gives

\[
 0<\Psi(t)\leq C\exp(9t/4-\pi e^t),\qquad
 \|v(t)\|\leq\sqrt2 C\exp(19t/8-\pi e^t).
 \tag{12}
\]

Consequently every fixed polynomial in t times v(t) tends to zero.
For a degree m polynomial this follows because
pi e^t-19t/8-m log(1+t) tends to infinity. This is a bound on
values only; no theta derivative-tail estimate is inferred.

From (9), ((alpha I-M)v)'=0 on the connected interval (0,infinity).
It is a constant vector, and (12) makes that constant zero. The vectors
v(t) span R^2: for any t1<t2 the determinant with columns v(t1),v(t2)
is

\[
 \Psi(t_1)\Psi(t_2)
 \big(e^{(t_2-t_1)/8}-e^{-(t_2-t_1)/8}\big)>0.
 \tag{13}
\]

Thus alpha I-M annihilates two independent vectors, and M=alpha I.
This is a consequence of (9), rather than an assumption that the matrix
is diagonal. Now (10) becomes

\[
 W(t)v'(t)+2\alpha v(t)=0,\qquad
 W(t)=(2\alpha t+\beta)I+N.
 \tag{14}
\]

Since W'=2alpha I, equation (14) is (Wv)'=0. Again (12), now with
a linear matrix factor, makes its constant vector zero. Hence

\[
 W(t)v(t)=0\qquad(t>0).
 \tag{15}
\]

### Positivity contradiction and all degeneracies

The scalar positivity in (2) gives alpha>=0 by letting y tend to
infinity in p(y)/y^2, and beta>=0 by letting y decrease to zero
in p(y)/y. They cannot both vanish, so 2alpha t+beta>0 for every
t>0. The matrix positivity in (2) gives N positive semidefinite:
for any real vector z,

\[
 z^T N z=\lim_{x\downarrow0}z^T(P(x)/x)z\geq0.
 \tag{16}
\]

The limit exists by (7). Thus, using the nonzero real vector v(t),

\[
 v(t)^T W(t)v(t)
 =(2\alpha t+\beta)\|v(t)\|^2+v(t)^TNv(t)>0,
 \tag{17}
\]

contradicting (15). This proves the conclusion.

When alpha=0, scalar positivity forces beta>0 and the same strict
inequality holds; linear p is included. When beta=0, alpha>0 suffices
at every t>0. N may be singular, including zero; its nonnegative term
was never required to be strictly positive. M was not inverted. The
case p identically zero is excluded by the original hypothesis, not by
an implicit normalization. Neither q nor Q was restricted after (6),
so all their constant and lower-degree cases are included. Equation
(11) and the remaining second-derivative/potential equations need not
be solved because (9)-(10) already contradict the hypotheses.

### Relevance and limits

The source calculus is known. The rectangular action adaptation and
this fixed-theta coefficient exclusion are the local work of step1289;
the bounded search in review1288 found no matching verdict, without
certifying originality. C032h's earlier common scalar commutant stop
is a contrast, not an input to this proof. C032e and C032f supply all
direct local mathematical inputs. The four-kernel coupled class is
now parked; a higher-degree sweep is not inferred or proposed. The
relative inequality B*B>=d^2 A*A and the main actual-Xi mixed-sign
problem remain unresolved. The separate conceptual audit1295 below
accepts this fixed-class obstruction without strengthening it.

### Independent conceptual audit — 17 November 2026, step1295

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-17-coupled-core-obstruction-audit-nomination-1293.md`,
separately approved1294, covers exactly this proof. The primary Green
calculus and its qualifications are reused from source-notes1288 and
approval1294; no new literature theorem or global domain is imported.
The following independent reconstruction accepts (3)-(17).

**Rectangular action and compact core.** Fix x>0 and a scalar test
function f supported in [a,b] inside (0,infinity). Integrating first
against -(pf')' and then against f' gives, in that order, the brackets
-kpf' and k'pf and the integral coefficient -pk''-p'k'+qk.
This verifies both signs in (3). A cutoff equal to one on an open
neighborhood of [a,b] has all its derivative terms outside the support
of f and f'. It can therefore be inserted in each kernel component
when using the compact-support source identity. On any compact x
interval, k,k',k'' are bounded on the resulting compact t interval,
which justifies the two x differentiations. The output expression is
-P(x)k''-P'(x)k'+Q(x)k, with matrices on the left throughout.
Subtracting the input expression gives exactly D,E,Z in (4).

This is a bilinear integration-by-parts calculation, not an assertion
about a Hilbert-space adjoint. It has no conjugated kernel, matrix
transpose or output boundary term. For each fixed x, all complex
compact scalar tests are allowed; testing real functions componentwise
already forces the continuous residual to vanish at every y>0.
If the premise is read in an almost-everywhere sense, the residual
integral for each fixed f is a smooth function of x and vanishes
identically. This yields the same quantifier order without selecting
a common exceptional set for uncountably many tests. No L2 property
of differentiated outputs is required.

**Kernel and coefficient elimination.** The coefficients of a and b
in (5) give 2v and 2tv identically for every finite c, including the
degenerate values c=1 and c=-1. These are constant linear combinations
of operator identities with the same input expression and the same
output expression. Once their kernel equations hold, subtracting
t times the v equation from the tv equation is pointwise algebra;
the derivatives of tv have already been taken. Its residual is
2Dv'+Ev, with all potential terms canceled.

At a fixed t>0, substitute y=t-x before collecting coefficients. The
coefficient of x^2 is 2(alpha I-M)v'. The coefficient of x is
-2((2alpha t+beta)I+N)v'-2(alpha I+M)v, and the constant coefficient
is 2(alpha t^2+beta t)v'+((2alpha t+beta)I-N)v. These agree with all
three equations (9)-(11), retaining every off-diagonal entry. Vanishing
on the nonempty interval 0<x<t forces each coefficient vector to
vanish. The proof uses only the first two; it does not claim that this
subsystem is sufficient for intertwining.

**Value tail and integration constants.** C032e(8) applies at positive
t to the full Psi with no truncation. Multiplying by the larger tilt
exp(t/8) yields the exponent 19t/8 in (12). In particular v(t)->0
and t v(t)->0. With R=alpha I-M constant, (9) implies (Rv)'=0;
the first limit gives Rv=0. Strict positivity of Psi and the determinant
(13) for any distinct positive t1,t2 then force R=0. This step needs
neither a spanning assertion about v' nor a limit of v'.

After M=alpha I, (10) is Wv'+2alpha v=0. Since W'=2alpha I,
the derivative of Wv is zero. The two value limits show
Wv=2alpha(t v)+(beta I+N)v tends to zero. Hence its constant value
is zero, exactly (15). Matrix inversion, derivative-tail asymptotics
and division by a leading coefficient never enter this argument.

**Strict contradiction and degeneracies.** From p(y)>0 for every
y>0, the limits of p(y)/y^2 at infinity and p(y)/y at zero give
alpha>=0 and beta>=0. The polynomial cannot vanish identically.
Independently, for each real z, P(x)>0 and the limit of P(x)/x at
zero give z^T N z>=0. Thus W has the strictly positive scalar part
(2alpha t+beta)I for every fixed t>0, plus a positive semidefinite N.
The vector v(t) is real and nonzero, so (17) contradicts (15).
If alpha=0 then beta>0; if beta=0 then alpha>0. No uniform margin
as t decreases to zero is needed. N may be singular or zero, and
M may be singular before its forced identification. Constant or zero
potentials and their nondiagonal matrix entries have already canceled.
The identically zero p case is excluded solely by the stated strict
positivity. These checks cover every allowed degree degeneracy.

**Verdict.** No defective reduction or missing analytic hypothesis was
found in the stated class. This verifies a retained local obstruction,
not a discovery beyond the sources checked or an enlargement of its
scope. C032e's full-theta smoothness, positivity and value bound, and
C032f's unchanged kernel definitions, are the only local mathematical
inputs used. C032f(21)-(25), C032h, actual-range inclusion and any
assumed sign of the actual-Xi form are not premises. The common compact
core, fixed degree bound, endpoint zeros, and strict scalar/matrix
positivity remain essential hypotheses of the accepted claim.

## Mathlib

Full matching coverage of the compact-core rectangular identity or this
fixed-theta exclusion has not been checked; availability is unknown.
The cited matrix Green calculus is an informal reference, not a Lean
verification. No absence claim or numerical certificate is asserted.
