# Corollary C033v: explicit interval-to-finite-node Laplace propagation

## Hypotheses

Let theta be a finite real signed Borel measure on X=[0,infinity),
and let 0<M<infinity be a prescribed allowance with

    ||theta||_TV=|theta|(X)<=M.

Atoms, singular parts and unbounded support are allowed. For Re z>0 set

    F(z)=integral_X exp(-z*t) dtheta(t).

Let S be any prescribed nonempty finite subset of (0,infinity).
Suppose epsilon>=0 and sup_(s in [1,2]) |F(s)|<=epsilon. There is no
assumption of an undamped moment, a density, a positive measure,
or a bounded inverse to the Laplace transform.

This is a generic statement. No zeta divisor, external preprint,
heat-error, Gaussian-variance or actual-Xi hypothesis is used here.

## Conclusion

The following choices depend only on the given node set:

    c=3/2,
    m_*=min({c} union S)>0,
    r=min{1/8,m_*/8}>0,
    N_s=ceil(|s-c|/r),                  s in S,
    N=max_(s in S) N_s,
    alpha(S)=2^(-(N+1)) in (0,1/2].                         (1)

All counts are finite integers and all constants are explicitly specified.
If 0<epsilon<M, then

    max_(s in S) |F(s)|<=M*(epsilon/M)^alpha(S).             (2)

If epsilon=0, F vanishes on the entire positive half-plane, so the
left side of (2) is zero. If epsilon>=M, the direct bound |F|<=M
applies; for epsilon>0 it also implies (2). If theta=0, F=0 and
all these conclusions hold without a separate limiting argument.
The excluded allowance M=0 would force theta=0 as well.

This is an explicit specialization of standard analytic-continuation
inequalities, not a claim of a new general stability theorem or an
optimal exponent. The bound can be extremely weak. It supplies no
cap-V Gaver extension, separator data, coefficient/deconvolution cost,
positive lower bound for d(V), observable evaluation or RH conclusion.
In particular it is not yet applied to the qualified laws in C033i/j/l/r.
The proof below was completed1791 and passes conceptual audit1880
under exactly these hypotheses; the downstream application remains open.

## Proof

### Imported estimates and scope of the application

Reuse SPECIALIZE assessment1790 and its inspected source evidence:
Lloyd N. Trefethen, *Quantifying the ill-conditioning of analytic
continuation*, BIT Numerical Mathematics 60 (2020), 901-915,
DOI 10.1007/s10543-020-00802-7,
[published author PDF, Lemma 2.1, p.904, and Theorem 3.1, pp.904-905](https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf).

Lemma 2.1 applies to a holomorphic h bounded in modulus by 1 on
0<Re w<1, with a uniform limiting bound q on its left boundary,
where 0<q<1. It gives |h(w)|<=q^(1-Re w). Its proof pays the
unbounded-strip maximum-principle issue. We import that theorem;
we do not apply an unqualified maximum principle on an infinite strip.

Theorem 3.1 applies to a holomorphic g bounded by 1 on |z|<R,
R>1, with |g|<=delta<1 on the unit disk. It gives

    |g(z)|<=delta^(1-log|z|/log R),   1<|z|<R.             (3)

We import (3), a normalized three-circle inequality, without reproving
it. The additional work here is the signed-measure applicability,
explicit real-interval-to-disk seed, and finite disk chain. Theorem 5.2's
unspecified conformal geometry and Theorem 7.1's small-data threshold
are not used. Dominated convergence, Fubini for absolute variation,
Morera's theorem, the identity theorem and maximum modulus on a bounded
domain are the other standard named inputs.

### Signed-transform existence, holomorphy and normalization

Write H={z:Re z>0}. For z in H and t>=0,
|exp(-z*t)|=exp(-Re z*t)<=1. Thus the complex signed integral exists
absolutely against |theta| and

    |F(z)|<=integral_X exp(-Re z*t) d|theta|(t)<=M.         (4)

Dominated convergence with dominator 1 against the finite measure
|theta| proves continuity on H. For any closed triangle with its
filled interior contained in H, the absolute iterated contour integral
is at most its boundary length times M. Fubini therefore permits

    integral_(boundary triangle) F(z) dz
      =integral_X [integral_(boundary triangle) exp(-z*t) dz] dtheta(t)
      =0.

The inner integral is zero because z maps to exp(-z*t) is entire
for each fixed t. Morera gives holomorphy on H. These arguments
retain the whole half-line, including its zero atom; no moment at
zero or support cutoff is introduced.

For 0<epsilon<M put q=epsilon/M in (0,1) and f=F/M. Then f is
holomorphic on H, |f|<=1 there, and |f(s)|<=q for 1<=s<=2.

### Explicit interval-to-disk seed

For w=x+iy define the entire map

    Z(w)=3/2+(2^w+2^(-w))/4,
    2^w=exp(w*log 2),                                      (5)

using the real positive value log 2. There is no inverse or branch
choice in (5). For 0<=x<=1 and every real y,

    Re Z(w)=3/2+[(2^x+2^(-x))/4]*cos(y*log 2),
    Im Z(w)=[(2^x-2^(-x))/4]*sin(y*log 2).

Since 2^x+2^(-x) increases from 2 to 5/2 on [0,1],

    7/8<=Re Z(w)<=17/8,   |Im Z(w)|<=3/8.                 (6)

Consequently h(w)=f(Z(w)) is holomorphic and bounded by 1 in the
open strip 0<Re w<1, and even extends across its boundary locally.
At x=0,

    Z(iy)=3/2+(1/2)*cos(y*log 2) in [1,2],

so |h(iy)|<=q. This is a uniform limiting boundary bound as required
by Lemma 2.1, not merely pointwise continuity at each y: the compact
rectangle in (6) is contained in H, so f is uniformly continuous
there, and

    sup_y |Z(x+iy)-Z(iy)|
      <=[(2^x-1)+(1-2^(-x))]/4
       =(2^x-2^(-x))/4 ->0 as x decreases to 0.

More precisely, if U(x)=sup_y |h(x+iy)|, then

    |U(x)-U(0)|<=sup_y |h(x+iy)-h(iy)| ->0,
    U(0)=sup_(s in [1,2]) |f(s)|<=q.

Thus the actual limit required in the source exists and is at most q.
The imported strip lemma now gives

    |f(Z(w))|<=q^(1-x),   0<x<1.                         (7)

At x=1/2, as y ranges over R, Z(w) traces the full ellipse

    z=c+A*cos u+i*B*sin u,
    c=3/2, A=3/(4*sqrt(2)), B=1/(4*sqrt(2)).               (8)

Equation (7) bounds f by q^(1/2) on its entire boundary. The closed
filled ellipse lies in H: its leftmost point is c-A>0. Since f is
holomorphic on a neighborhood of that compact ellipse, maximum
modulus on its bounded interior gives the same bound inside.

The closed disk |z-c|<=1/8 is strictly inside this ellipse. Indeed
A>=B and, writing z-c=u+iv, one has

    u^2/A^2+v^2/B^2 <=(u^2+v^2)/B^2
                    <=(1/8)^2/B^2=1/2<1.

We have therefore established the genuine complex seed

    |f(z)|<=q^(1/2),   |z-c|<=1/8.                        (9)

In particular the real segment was not substituted directly for a
complex disk in the three-circle estimate.

### One disk step and all boundary points

Use r in (1). Every real center a>=m_* has

    Re z>a-4r>=m_*-4r>=m_*/2>0,   |z-a|<4r.              (10)

Suppose a closed radius-r disk at such a center has a known bound
|f|<=q^beta, beta>0. Apply (3) with R=4 to
g(z)=f(a+r*z) and delta=q^beta. On 1<|z|<=2, the exponent
1-log|z|/log 4 is at least 1/2. As 0<q<1, (3) yields
|g(z)|<=q^(beta/2) there. On |z|<=1, the original bound q^beta
is at most q^(beta/2). Thus

    |f(z)|<=q^(beta/2),   |z-a|<=2r.                      (11)

The outer domain |z|<4 in (3) is open, but every radius-2 point
used in (11) lies strictly inside it. The radius-1 points are
covered by the original closed-disk bound. No passage to the
uncontrolled boundary of the outer disk occurs.

If a' is real and |a'-a|<=r, its closed radius-r disk is contained
in the closed radius-2r disk at a. Equation (11) therefore gives
the next radius-r seed with exponent beta/2. This includes touching
points when |a'-a|=r.

### Explicit finite iteration to every positive node

Since r<=1/8, (9) gives a radius-r seed at c with exponent 1/2.
Fix s in S. If N_s=0, then s=c, so no disk step is needed.
If N_s>0, set

    c_j=c+j*(s-c)/N_s,   j=0,...,N_s.

These centers lie on the real segment joining c to s, hence
c_j>=min{c,s}>=m_*. Also

    |c_(j+1)-c_j|=|s-c|/N_s<=r.

Starting with (9), apply the one-step implication (11) successively
N_s times. The result on the closed radius-r disk at c_j is
|f|<=q^(2^(-(j+1))). In particular

    |f(s)|<=q^(2^(-(N_s+1))).                             (12)

There are finitely many nodes, so N=max_s N_s is a finite integer,
even for very small positive nodes or very large nodes. Its exponent
alpha(S)=2^(-(N+1)) is strictly positive as an exact real number.
Because N_s<=N, the exponent in (12) is at least alpha(S).
For q in (0,1) this gives |f(s)|<=q^alpha(S) simultaneously for
all s in S. Multiplication by M proves (2). The whole construction
uses no unknown norm, unspecified map or small-error threshold.

### Zero error, trivial error and downstream qualifications

If epsilon=0, F=0 on [1,2]. The identity theorem on the connected
domain H applies to this set with an interior accumulation point,
and gives F identically zero. If epsilon>=M, (4) gives the stated
direct bound, and for epsilon>0 the right side of (2) is at least M.
If theta=0 the defining integral is zero for every z in H. This
finishes all cases under the hypotheses.

For a possible later application, C033r supplies only a cap2
witness. Neither variable-cap parameter choices nor any assembled
rate for the original residual follow from this proof. Such an
application would have to supply its signed residual measure,
an actual TV allowance, its finite nodes and coefficient costs, and
any exact transform division independently. All actual-divisor,
conjugation/multiplicity, excluded-zero-ordinate, strict-strip,
gamma>14, counting, through100/retained-real-zero, reciprocal-square
tail, heat positivity/separate fixed-j errors, Gaussian half-variance
and both fixed-v1 qualifications remain whenever those notebook
laws are used. None is verified by this generic continuation estimate.

### Conceptual audit1880 — 20 November 2026

The independent audit uses unchanged SPECIALIZE assessment1791 and
source evidence1790. It checks (1)-(12) and every degenerate case under
the stated finite signed-measure hypotheses. The conclusion and constants
are unchanged. The only proof clarification above makes explicit the
existence of the uniform boundary limit, rather than just its limsup.

Reopened the published Trefethen PDF cited above: printed p.904,
Lemma 2.1, its complete proof, and Theorem 3.1; p.905, the continuation
of Theorem 3.1 and its complete proof. The strip theorem requires the
uniform left-boundary limit, a bound throughout the open strip, and
0<q<1. Its proof uses the bounded-strip Phragmen--Lindelof theorem
after exponential normalization. The disk theorem uses R>1, a bound
throughout the open outer disk, and a smallness bound on the unit disk;
its proof transfers to the strip by an exponential map. Only their
forward inequalities are imported. No sharpness statement, numerical
chain estimate, or unspecified conformal map is used.

1. **Signed holomorphy and allowance.** The integrand is Borel and
   absolutely bounded by 1 against the finite positive measure |theta|.
   Dominated convergence proves continuity even with unbounded support.
   For each triangular contour, the product integral of the absolute
   integrand against arclength and |theta| is at most length times M.
   Signed Fubini is therefore legitimate before Morera is applied.
   Neither differentiation under an undamped moment integral nor
   positivity of theta is used. A nonsharp prescribed M is sufficient.

2. **Uniform seed.** Both Z(x+iy) and Z(iy) lie in the same compact
   rectangle (6), strictly inside H. The displayed uniform difference
   bound tends to zero, so uniform continuity proves convergence of
   U(x) to U(0); the source's actual limit hypothesis is satisfied.
   The exponential definition of 2^w has no branch choice. At x=1/2,
   u=y*log(2) covers the whole ellipse boundary. Its leftmost point
   c-A is positive, and B^2=1/32 while (1/8)^2=1/64. Hence maximum
   modulus applies on a bounded filled ellipse and the closed seed
   disk is strictly inside it. No disk estimate starts from a bare
   real segment.

3. **Propagation boundaries and iteration.** Since r<=m_*/8,
   even the closed disk of radius4r at every center a>=m_* has
   Re z>=m_*/2>0. The imported theorem is used only inside that disk,
   with R=4 and delta=q^beta in (0,1). Radius2 is strictly below R;
   radius1 is covered by the original closed seed. Translation by
   at most r therefore transfers the bound to the next closed disk,
   including a touching point. For s!=c, the positive integer N_s
   ensures every step is at most r. Induction starts with beta=1/2
   and makes exactly N_s halvings, yielding 2^(-(N_s+1)). Taking
   N=max N_s makes alpha no larger than any of these exponents;
   because 0<q<1 this weakens each bound in the required direction.

4. **Endpoint and exceptional cases.** If s=c, N_s=0 and the
   division defining c_j is not performed. Finiteness and positivity
   of the prescribed nodes give m_*>0 and finite N; no uniform
   positive lower bound on alpha is asserted as nodes approach zero
   or escape to infinity. The identity theorem handles epsilon=0
   without invoking either small-error estimate. For epsilon>=M, the
   integral bound implies (2) since (epsilon/M)^alpha>=1. The zero
   measure is covered directly; M=0 remains outside the hypotheses.

Verdict: all claimed inequalities and boundary cases pass. This resolves
the pending informal verification of the generic specialization, not
any upstream zeta-source verification or its later separator application.
It is reproduction of the cited analytic tools with checked geometry,
not progress beyond those sources or a new stability theorem. No
numerical check or mathematical script is needed for this audit.

## Mathlib

Full matching coverage for this signed-measure specialization with
the explicit ellipse and finite-node exponent has not been checked
and is unknown. Morera, maximum modulus, identity, signed integration
and three-circle results are supporting named mathematical inputs;
no particular Mathlib declaration for them is asserted here. No Lean
formalization or numerical certificate is claimed. The precise
analytic-continuation source imported above is the inspected Trefethen
Lemma 2.1 and Theorem 3.1, not a Mathlib homepage or a source snippet.
