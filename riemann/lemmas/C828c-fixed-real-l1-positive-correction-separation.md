# C828c — Strict real-L1 separation for the fixed positive correction class

## Hypotheses

Let S={z:|Im z|<pi/4}, and let Phi be exactly the holomorphic actual
kernel in C828b. Put K=2Phi on S; its series agrees with the L019 kernel
on the nonnegative real axis. On [-1,1], K always means this continuation.
Let B(z)=exp(-2pi cosh(2z)), an entire, nowhere-zero function. Define

\[
 \mathcal A=\left\{U:\ U\text{ is entire},\quad
 U(z)=\sum_{j=0}^\infty a_jz^{2j},\quad a_j\in[0,\infty)\right\}.
\]

There is no normalization, coefficient bound, degree bound or order bound.
All integrals below are Lebesgue integrals in the real variable.

## Conclusion

\[
 0<\Delta:=\inf_{U\in\mathcal A}
       \int_{-1}^1|B(x)U(x)-K(x)|\,dx<\infty.       \tag{1}
\]

Thus this class cannot approximate the actual kernel arbitrarily well
in the specified real-L1 norm. This is a qualitative separation, with no
explicit numerical lower bound. It is a REPRODUCTION/specialization of
known compactness tools and the audited C828b boundary obstruction, not
a new theta natural-boundary theorem or an estimate proving RH.

## Proof

### Real integral control gives complex local bounds

The function K is continuous on [-1,1], which is a compact subset of S,
so M=integral_[-1,1]|K(x)|dx is finite. The zero function belongs to
the class, hence 0<=Delta<=M<infinity. Suppose Delta=0. By the definition
of the infimum choose U_n in the class with error at most 1/n.
For real |x|<=1,

\[
 B(x)\ge b:=\exp(-2\pi\cosh2)>0,\qquad U_n(x)\ge0.
\]

The triangle inequality therefore gives, for every n>=1,

\[
 \int_{-1}^1 U_n(x)\,dx
 \le b^{-1}\int_{-1}^1|B(x)U_n(x)|\,dx
 \le b^{-1}(M+1)=:C.                              \tag{2}
\]

Fix any 0<r<1. Nonnegative coefficients and absolute convergence of
each entire series give, for |z|<=r and r<=x<=1,

\[
 |U_n(z)|\le\sum_{j\ge0}a_{n,j}r^{2j}=U_n(r)
       \le U_n(x).
\]

Integrating the last inequality on [r,1] and using (2) yields

\[
 \sup_{|z|\le r}|U_n(z)|\le \frac{C}{1-r}.        \tag{3}
\]

Every compact subset of the open unit disk E={z:|z|<1} lies in one
such closed r-disk. Thus (3) is a uniform bound on every complex compact
subset of E. It is not an assertion that real-L1 control alone implies
normality; the coefficient signs are essential to this argument.

### Imported compactness and agreement with the actual kernel

Import Montel's locally bounded family theorem, as stated and proved in
Alexander Nagel, *Math722, Complex Analysis*, Spring2009, Part5,
Section1.2 Theorem1.2, pp2-3 (with Section1.1 Theorem1.1, pp1-2),
[primary lecture notes](https://people.math.wisc.edu/~ajnagel/Math722Lectures5.pdf).
By (3), a subsequence U_(n_k) converges uniformly on compact subsets
of E to a holomorphic function U there. Holomorphy of a locally uniform
limit is also Terence Tao, *Math246A Notes3*, 2October2016,
[Theorem36](https://terrytao.wordpress.com/2016/10/02/math-246a-notes-3-cauchys-theorem-and-its-consequences/).
These general theorems are imported, not reproved. Their domain is E,
which is open and connected; every U_n is holomorphic on E, and (3)
checks their substantive compact-boundedness hypothesis.

On I=[-1/2,1/2], multiplication by the bounded continuous B preserves
uniform convergence. Consequently

\[
 \int_I|BU-K|\,dx
 \le |I|\sup_I|B(U-U_{n_k})|
       +\int_{-1}^1|BU_{n_k}-K|\,dx\longrightarrow0. \tag{4}
\]

The left side is independent of k. Its integrand is continuous and
nonnegative, so (4) implies BU=K at every point of I. For instance a
strictly positive value at any point of I would, by continuity, give
a positive integral on a one-sided or two-sided subinterval of I.

The domain V=E intersect S is a nonempty convex open set. Both BU and K
are holomorphic there. Their difference vanishes on I, whose zero set
has the interior accumulation point 0 in V. The identity theorem gives
BU=K throughout V. Here we import the connected-domain uniqueness
theorem, Tao2016 Notes3, Corollaries25-26 at the same primary URL; real
agreement is used through its accumulation-point hypothesis, not as
agreement on a complex open set.

### Fixed boundary disk, normalization and contradiction

Take the C828b disk with R=0:

\[
 D=\{z:|z-i\pi/4|<1/100\}.
\]

For z in D, the triangle inequality and pi<22/7 give

\[
 |z|<\pi/4+1/100<11/14+1/100<4/5<1.
\]

Thus D is contained in E, so f=BU/2 is holomorphic on all of D.
On D intersect S, which is nonempty, the preceding identity gives
f=K/2=Phi exactly. This is the forbidden disk extension in C828b with
its actual kernel, its fixed radius1/100 and its factor2 unchanged.
C828b forbids that extension at every real R, including 0. Contradiction.
Therefore Delta cannot be zero; combined with its nonnegativity and
finiteness this proves (1).

The limit U need only be holomorphic on E, not entire; that disk already
contains the forbidden crossing. No limit at a strip boundary, boundary
value of K, termwise boundary differentiation, global transform limit,
zero-location assumption or signed-log inequality is used.

### Scope of the obstruction

In particular, positive finite-product corrections
c exp(a z^2) product_(j=1)^m(1+z^2/r_j^2), with c>0, a>=0 and r_j>0,
belong to the stated class: each factor is entire with nonnegative even
Taylor coefficients, and a finite product preserves those properties.
This inclusion does not identify the class with all universal factors.
The proof does not exclude signed coefficients, other seeds or other
approximation topologies. It neither supplies the signed upper payment
in C029j nor proves H_d=o(d) in C028b; those are downstream gaps only.

### Independent conceptual audit1990 — 20 November 2026

The approved audit accepts (1) with no mathematical correction. This is
a REPRODUCTION of the stated specialization, not a new separation theorem
or an actual-Xi sign estimate. The general analytic theorems are imported
at the precise citations above; the already audited C828b is reused.

For (2), cosh(2x)<=cosh(2) on [-1,1], and B(x) is positive real.
Every summand of U_n(x) is nonnegative even when x<0. Hence
b U_n(x)<=B(x)U_n(x)=|B(x)U_n(x)|, which can be integrated and
bounded by |B(x)U_n(x)-K(x)|+|K(x)|. Positivity of K is unnecessary.
Its continuity on this closed real interval follows from holomorphy
inside S, not from any assertion about the boundary of S.

For (3), absolute convergence at r and coefficient nonnegativity give
|U_n(z)|<=U_n(r) for |z|<=r. For every x in [r,1], each even power
is nondecreasing in x, so U_n(r)<=U_n(x). Thus
(1-r)U_n(r)<=integral_[r,1]U_n<=C, with the same C for every n.
Given any compact subset of E, choose one r<1 containing it; the
constant may depend on r. Montel now supplies a single subsequence
on all of E. Choosing unrelated subsequences for individual radii,
bounding the family on all of C, or passing to the endpoints +/-1
would not be justified; none is done here.

On I=[-1/2,1/2], compact convergence and boundedness of B make the
first term on the right of (4) tend to zero; the other is at most
1/n_k and n_k tends to infinity. Continuity of |BU-K| promotes its
zero integral to equality at every point of I, including its endpoints.
The holomorphic difference BU-K is defined on the connected convex
open set E intersect S, and I accumulates at 0 inside that set.
The identity theorem therefore gives agreement on the entire overlap.
Neither an open complex zero set at the outset nor any boundary values
are required. No sign or coefficient property of the limit U is needed.

The normalization check is literal: twice C828b's Phi series has
coefficients 8pi^2 n^4 and -12pi n^2, exactly those of L019's K.
On negative real arguments the hypothesis defines K=2Phi directly;
L019's positivity statement is restricted to nonnegative arguments and
is not extended here. Finally pi/4+1/100<557/700<4/5<1, so the
whole specified disk D lies inside E. The point i(pi/4-1/200)
shows D intersect S is nonempty. On all that overlap BU/2=Phi.
Thus BU/2 on D meets precisely the extension forbidden by C828b
at R=0, including its radius and factor 2. It is irrelevant whether
the limit U continues beyond E or converges on the boundary of E.

The contradiction rules out Delta=0; Delta is already a finite
nonnegative real number since U=0 is allowed. This proves strict
positivity without an effective lower bound. The finite-product subclass
has nonnegative even coefficients by the power series of exp(a z^2)
and finite multiplication, under the stated c>0, a>=0 and r_j>0.
No universal-factor characterization, tail estimate, signed payment,
interchange of boundary limits or zero-location premise is being added.

## Mathlib

Full matching coverage is **not checked**. No formalization of this
actual-kernel real-L1 separation or its theta boundary input is claimed.
The known Montel and identity theorems are supporting analytic inputs;
their use here is fully specified by (2)-(4) and the stated domains.
