# Corollary C030n: a uniform two-level finite-phase orbital bound

## Hypotheses

Let n>=2 be finite, a,r,x>0, and b real with |x*b|<=1/4. For
j=0,...,n let P_j be an orthogonal projection of rank j on C^n.
Use probability Haar measure on U(n), and define, exactly as in C030m,

    D_b=diag(a+i*b,a-i*b,r,...,r),
    Z_(j,b)(x)=integral exp(-x tr(D_b V P_j V*))dV,
    G_(j,b)(x)=-Z'_(j,b)(x)/Z_(j,b)(x),
    E_(k,b)(x)=(G_(k+1,b)-G_(k,b))
                  -(G_(k+1,0)-G_(k,0)),   0<=k<n.

The x derivative holds a,r,b fixed. Each rank has its own partition
function. At n=2 the parameter r has no entries and is immaterial.
Both signs of a-r, a=r, repeated projection eigenvalues, b=0 and
both adjacent endpoint ranks are included. The full real tilted-array
comparison proved in C030l, including weak top rows and arbitrary
fixed real fields with separate normalizers, is used as established
local input. Its cited orbital-law theorem is qualified below.

## Conclusion

The partition functions Z_(j,b)(x) are positive real on this window,
so the displayed logarithmic derivatives are well defined and real.
For every rank j,

    |G_(j,b)(x)-G_(j,0)(x)| <= (32/95)*x*b^2.           (1)

Consequently the requested absolute constant can be taken to be

    |E_(k,b)(x)| <= (64/95)*x*b^2,   0<=k<n.           (2)

The rank-zero and rank-n responses vanish exactly. Thus the constant
in (2) improves to 32/95 for k=0,n-1. No sharpness is asserted.

This is the finite-phase result of bounded research attempt1210;
independent conceptual audit1212 retains (1)-(2), with unchanged
constants and hypotheses. The prior EXPLORE assessment1208,
approved1209, covered this exact target; its checked sources did not
supply (2). POTENTIALLY_NEW records only that comparison, not verified
originality. This result is restricted to the displayed common-background
family. It does not establish unequal-background control, a sum over
conjugate pairs, an actual-Xi degree/time comparison, all-degree
positivity, graph realization or RH. Audit1212 is REPRODUCTION of this
local proof, not a new result beyond it or an originality certification.

## Proof

### Exact orientation average and a lower bound for each denominator

Put Q=V P_j V*, S=Q_11+Q_22, and T=Q_11-Q_22. Let
0<=ell(Q)<=h(Q)<=1 be the eigenvalues of its leading two-by-two
corner, and let d(Q)=h(Q)-ell(Q), so 0<=d(Q)<=1. Write delta=a-r.
The trace identity and coordinate-swap symmetry in C030m give

    tr(D_b Q)=r*j+delta*S+i*b*T,
    Z_(j,b)/Z_(j,0)=E_(j,x*delta) cos(x*b*T).           (3)

Here E_(j,x*delta) is normalized Haar tilted by exp(-x*delta*S).
Its denominator is its own strictly positive integral for this rank.

Use C030m's U(2) block-invariance calculation: conditional orientation
averaging of the two-by-two corner replaces T by d(Q)*(2p-1),
where p is uniform on [0,1]. The tilt depends only on S and is
unchanged by this block conjugation. Applying that averaging to the
bounded cosine in (3), rather than to T^2, therefore gives exactly

    Z_(j,b)/Z_(j,0)=E_(j,x*delta) f(x*b*d(Q)),          (4)
    f(z)=integral_0^1 cos(z*s)ds=sin(z)/z,   f(0)=1.

All integrals are finite and bounded on each compact parameter set;
block averaging may be interchanged with the normalized Haar integral.
No statement about stochastic order for a complex law is used.

For real z, cos(z*s)>=1-z^2*s^2/2, so

    f(z)>=1-z^2/6.

Since d(Q)<=1 and |x*b|<=1/4, the quotient in (4) satisfies

    Z_(j,b)/Z_(j,0)>=1-(x*b)^2/6>=95/96.              (5)

This proves positivity separately at every rank. It also ensures a
nonvanishing real neighborhood of each point used in a logarithmic
derivative. The lower bound remains valid at |x*b|=1/4.

### Fixed real field on a scaled orbit

First suppose n>=3. For t>0 let Y=t V P_j V*, and tilt its orbital
law by exp(-delta*tr(Y_[2])), divided by its own expectation.
Denote this probability law by nu_t. The field is fixed as t varies:
in C030l's corner-array notation, c_2=-delta and every other c_s=0.
There is a proper two-by-two corner because n>=3. The constant
exp(-r*t*j) in the full trace has canceled only within the rank's
own quotient; it is not equated across ranks or different t.

Let ell_t<=h_t be the two corner eigenvalues under nu_t, and set

    phi(q)=f(b*q),
    F_j(t)=E_(nu_t) phi(h_t-ell_t).

At t=x, (4) reads F_j(x)=Z_(j,b)(x)/Z_(j,0)(x).
This equality also holds as a function of t with a,r,b fixed. In
particular, both the weight and the observable vary with the same
physical x derivative specified in the hypotheses. When delta=0
the field is zero; no division by delta or limiting argument is needed.
Negative delta is equally permitted by C030l.

For eta>0 the increasing top row lambda(t)=(0^(n-j),t^j) obeys

    lambda(t)<=lambda(t+eta)<=lambda(t)+eta*(1,...,1).

C030l's full real comparison applies to these weak rows and the
same fixed field. The law for the last top row is the law nu_t
translated by eta in every corner eigenvalue. Indeed translating
Y by eta*I adds 2*eta to tr(Y_[2]); its weight gains the constant
exp(-2*delta*eta), which cancels in that translated law's own
normalizer. Thus, for continuous increasing array tests, there are
two expectation orders

    nu_t <= nu_(t+eta) <= translation_eta(nu_t).        (6)

Applying them to the corner coordinates separately gives

    0<=Delta E ell<=eta,   0<=Delta E h<=eta,          (7)

where Delta is expectation at t+eta minus expectation at t. No
almost-sure coupling, derivative of eigenvalue paths or equality of
different partition functions is inferred from (6).

### Increasing tests for a decreasing function of the corner gap

Fix t with |b|*t<=1/4. Take eta>0 small enough that U=t+eta
satisfies |b|*U<pi. Differentiating the compact integral for phi gives

    phi'(q)=-b*integral_0^1 s*sin(b*q*s)ds.

For 0<=q<=U, b*sin(b*q*s)>=0, for either sign of b. Also
|sin(b*q*s)|<=|b|*q*s. Hence, with L=b^2*U/3,

    -L<=-b^2*q/3<=phi'(q)<=0.                        (8)

On the triangle 0<=ell<=h<=U consider

    A(ell,h)=phi(h-ell)+L*h,
    B(ell,h)=-phi(h-ell)+L*ell.

Their partial-derivative pairs are respectively
(-phi',phi'+L) and (phi'+L,-phi'), all nonnegative by (8).
To use genuinely global increasing tests in (6), define

    clip_U(v)=min(U,max(0,v)),
    l=clip_U(ell), H=clip_U(h), d=(H-l)_+,
    A_tilde(ell,h)=phi(d)+L*H,
    B_tilde(ell,h)=-phi(d)+L*l.

On H>=l these have the just-displayed nonnegative derivative pairs
in the clipped coordinates. On H<=l they equal 1+L*H and -1+L*l,
respectively, also coordinatewise increasing. They agree continuously
across H=l, and the clipping map is increasing in each coordinate.
Thus they are continuous increasing functions on all of R^2. Viewed
as functions of the full corner array, they are constant in the other
coordinates. They agree with A,B on both nu_t and nu_(t+eta)
supports, which lie in 0<=ell<=h<=U.

The first order in (6), applied to these two tests, yields

    Delta F_j >= -L*Delta E h,
    Delta F_j <=  L*Delta E ell.

Together with (7), this proves the finite-difference estimate

    |F_j(t+eta)-F_j(t)| <= (b^2/3)*(t+eta)*eta.        (9)

F_j is smooth for real t>0: in fixed Haar variables it is

    F_j(t)= [integral exp(-delta*t*S) f(b*t*d(Q))dV]
               / [integral exp(-delta*t*S)dV].

The denominator is positive, S and d(Q) are bounded, and all fixed
derivatives of the integrands are bounded on compact real t intervals.
Differentiation under each integral and ordinary quotient differentiation
are therefore legitimate. Dividing (9) by eta and taking eta down to
zero gives its ordinary derivative bound

    |F_j'(t)| <= b^2*t/3   when |b|*t<=1/4.           (10)

At the phase-window boundary, arbitrarily small positive eta still
satisfy |b|*(t+eta)<pi, as required by (8). Thus (10) includes the
closed endpoints. At b=0, F_j is identically one and (9)-(10) hold
with zero right side. There is no parameter-uniform Taylor expansion
or exchange of a supremum with a limit in this argument: (9) is a
proved finite difference for every fixed parameter choice, with the
displayed uniform bound.

### The remaining dimension and passage to adjacent ranks

At j=0 or j=n, the two corner eigenvalues coincide. Then F_j=1
and the phase response is zero exactly, in every n. If n=2,j=1,
the corner is the whole rank-one projection, with gap one and trace
one before scaling. Its tilt is constant on the orbit. Formula (4)
therefore gives F_1(t)=f(b*t), independently of a,r. Directly from
the integral for f,

    |F_1'(t)|<=|b|*integral_0^1 s*|sin(b*t*s)|ds
                 <=b^2*t/3.

This supplies (10) in the only remaining case without treating a
top-row trace as a proper-corner field. The same lower bound (5)
applies. In particular, no exceptional n=2 contrast case is omitted.

For every n,j we may now differentiate the positive quotient:

    G_(j,b)-G_(j,0)=-d/dx log(Z_(j,b)/Z_(j,0))
                      =-F_j'(x)/F_j(x).

Using (5) and (10) gives x*b^2/(3*(95/96))=(32/95)*x*b^2,
which proves (1). Subtracting the two rank responses and applying
the triangle inequality proves (2). At an adjacent endpoint only
one response is nonzero, yielding the stated endpoint improvement.
Every response has retained its own denominator throughout.

### Source qualification and downstream scope

The real comparison is used from C030l's complete proof, not inferred
from its scalar rank-increment conclusion. Its source is Suvrit Sra,
*On some positivity properties of the Riemann Xi function*,
[author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.7 and Theorem C.8, printed pp25-27. Its uniform orbital-law
input is G. Olshanski, *Projections of Orbital Measures, Gelfand-Tsetlin
Polytopes, and Splines*, J. Lie Theory 23 (2013), 1011-1022,
[Corollary 3.2, p1017](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf).
Olshanski's statement requires a strict top row; the weak-row extension
used here is the separately justified Haar-continuity extension in
C030l. No collapsed polytope is assigned ambient Lebesgue density.
Those general theorems are not reproved in this attempt. The new
calculation is the sinc-gap comparison (8)-(10) needed for the finite
phase target; the sources inspected in assessment1208 did not state it.

The bound pays only this one-pair perturbation in the stated finite
family. It supplies neither the other hypotheses of C030l's finite
reference use nor a signed all-degree comparison for Xi. The independent
review below retains this restricted bound; no complete RH candidate
is presented.

### Independent conceptual audit1212 (17 November 2026)

Verdict: (1)-(2) pass the exact audit approved in assessment1210/1211,
relative to C030l's full real-array comparison and its cited orbital-law
input. No constant, parameter range or downstream assertion is enlarged.
The full C030l and C030m proofs were read, not merely their conclusions.
The general orbital-law theorem remains an imported theorem, rather
than a source proof newly audited here.

For (4), invariance under diag(W,I), W in U(2), preserves both S and
the positive real weight. Averaging over independent W at fixed Q
therefore leaves the normalized integral unchanged. The uniform p
law gives integral_0^1 cos(z*(2p-1))dp=integral_0^1 cos(z*s)ds=f(z).
This works at repeated corner eigenvalues and does not condition on
a null event. The separate lower bound is 1-1/96=95/96, and the
real quotient remains positive in a neighborhood of every point of
the closed window. Reality follows from the coordinate-swap symmetry;
positivity is not assumed from reality or analyticity alone.

For (6), C030l's finite-mesh conditional comparisons use the same
positive field but different normalizing sums. Its stationary limits
precede the mesh limit, which uses the cited uniform orbital law only
for strict rows. Ordered strict rational approximations and positive
Haar normalizers give the weak-row extension. Thus the projection
rows here are covered without an ambient density on a collapsed
polytope. The required field is c_2=-delta, fixed as t varies, not
-t*delta on the already scaled orbit. It is a proper-corner field
exactly when n>=3. Translation by eta*I shifts both corner coordinates
by eta and multiplies the weight and its own normalizer by the same
exp(-2*delta*eta). Consequently the upper expectation comparison in
(6) gives the upper bounds eta in (7), for either sign of delta.

For the tests in (8)-(9), b*sin(b*q*s) is nonnegative on the stated
interval for both signs of b, and its magnitude is at most b^2*q*s.
Thus -L<=phi'(q)<=0. On H>=l the derivative pairs for the two clipped
tests are (-phi',phi'+L) and (phi'+L,-phi'); on H<=l they are (0,L)
and (L,0), in (l,H) order. They agree across the diagonal. Each
one-dimensional coordinate section is continuous and nondecreasing
on both pieces, and clipping preserves this property. This verifies
global monotonicity, not just monotonicity along the triangular support.
The first order in (6) therefore gives

    -L*Delta E h <= Delta F_j <= L*Delta E ell.

Using (7) yields -L*eta<=Delta F_j<=L*eta. No claim that the gap
itself is increasing, nor a simultaneous samplewise coupling, is needed.

The fixed-Haar quotient for F_j(t) includes both the derivative of
the real tilt and that of f(b*t*d(Q)). On a compact real t interval,
S<=2 and d(Q)<=1 bound all fixed derivatives of both integrands;
the real denominator is positive and continuous. Smooth quotient
differentiation is therefore valid with a,r,b fixed. Its ordinary
derivative equals the right difference limit in (9). Even at
|b|*t=1/4, sufficiently small positive eta has |b|*(t+eta)<pi;
the comparison never required t+eta to remain inside the smaller
phase window. No unproved uniform remainder or supremum-limit
interchange enters the uniform conclusion (10).

At delta=0 the field is simply zero. At b=0 the quotient is one.
At j=0,n its corner gap vanishes, so its response is zero. When
n=2,j=1 the corner is the whole matrix and the exact quotient f(b*t)
supplies the derivative bound directly; r cancels from the trace
identity because S=j. This covers all exceptional field, rank and
contrast cases, including k=0,n-1. Finally

    (1/3)/(95/96)=32/95,   2*(32/95)=64/95.

The minus sign in G_(j,b)-G_(j,0)=-F_j'/F_j is retained. Only the
last triangle inequality compares ranks, each with its own positive
quotient. The audit establishes the validity of the existing finite
input; it provides no unequal-background bound, multi-pair summation,
Xi realization, all-degree sign theorem or new result beyond C030n.

## Mathlib

Full matching coverage of (1)-(2), the sinc-gap comparison and the
tilted orbital-law input is unchecked; no absence claim is made.
Haar invariance, differentiation of bounded integrals and elementary
monotone-function estimates support the argument. Their matching
Mathlib theorem names were not checked or formalized in this step.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
