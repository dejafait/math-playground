# Corollary 673a: a real-crossing barrier for the fixed phase gauge

## Hypotheses

Use L673's admissible symmetric displacement sequence and its fixed gauge

    q>=1, n=12q+3, h=27/(10n), rho=h/10,
    x=-d=-5/4, U=121/64, r=9/20,
    c=10*pi/27, gamma=3/5,
    g_n(z)=(1-z/rho)*exp(-c*n*z-gamma*n*z^2).

Retain all factors of L673's W, including j=0. In particular its exact
continuum exponent is

    F(z,u)=integral_0^1 log|[(x-t*u)/(x+z-t*u)]
                           *[(U*u-t*(x+z))/(U*u-t*x)]| dt,
    K(z)=(10/27) integral_(-r)^r [log|t|-log|z-i*t|] dt,
    E(z,u)=F(z,u)-c*Re z-gamma*Re(z^2)+K(z),  |u|=1.

Let Gamma be a rectifiable Jordan curve with bounded interior Omega,
with 0 in Omega and

    closure(Omega) subset D={z: |x+z|>1}.

For its use as L673's interpolation contour, also require all the nodes
+-i*h*s_k to lie in Omega. The obstruction below uses only 0 in Omega.
The region D is a common pole-free parameter region for every q and
every angular u. This is an explicit restriction on the contour test;
finite-n pole-free regions can be slightly larger.

## Conclusion

For every real 0<s<1/4,

    E(s,-1)>-147/16000=-0.0091875>-1/100.              (1)

Every such Gamma has a point s on this real interval. Consequently

    sup_(z in Gamma, |u|=1) E(z,u)>-147/16000,         (2)

so no change of contour shape within D can make this fixed continuum
exponent uniformly <=-1/100, let alone <=-1/100-epsilon. The positive
gap in (1) above the desired upper threshold is 13/16000.

This is a new local cost obstruction for the specified sufficient
absolute-contour criterion under the unchanged approved EXPLORE
assessment `drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
The bounded literature search does not certify originality. A separate
critical audit of this extension has not yet been performed.

Neither (1) nor (2) is a lower bound on kappa_e, on the actual contour
integrand, or on its signed integral. L673's rate-1/200 construction
remains valid. The rate-1/100 cone question remains unresolved. Original
residues remain one; no conclusion about their sum, H, Xi realization
or mixed signs follows.

## Proof

### 1. The exact exponent on the real crossing

Put e(s)=E(s,-1) for 0<s<1/4. Every factor in the following real
formula is positive, since d-s>1 and U-d=41/64>0:

    F(s,-1)=integral_0^1 [log(d-t)-log(d-s-t)
                         +log(U-t*(d-s))-log(U-t*d)] dt.       (3)

These signs follow directly from the full rational formula; in
particular the numerator's U term contributes a positive first
s derivative and a negative second derivative. Differentiating on
any compact subinterval of [0,1/4), with uniformly positive
denominators, gives

    F_s(s,-1)=integral_0^1 [1/(d-s-t)+t/(U-t*(d-s))] dt,
    F_ss(s,-1)=integral_0^1 [1/(d-s-t)^2
                              -t^2/(U-t*(d-s))^2] dt.         (4)

In the kernel integral, the integrable log|t| term is fixed. Direct
integration for s>0 yields

    K(s)=(10/27)*[r*log(r^2/(s^2+r^2))-2*s*atan(r/s)],
    K'(s)=-(20/27)*atan(r/s),
    K''(s)=(20*r/27)/(s^2+r^2).                              (5)

Thus K extends continuously to K(0)=0, with right derivative
K'(0+)=-10*pi/27. Formula (3) also gives F(0,-1)=0, so e(0)=0.
Evaluating the first derivative at zero, using the elementary
antiderivatives in (4), gives exactly

    e'(0+)=log 5+(121/100)*log(121/41)-4/5-20*pi/27.           (6)

Here U/d^2=121/100 and U/(U-d)=121/41. One copy of -10*pi/27
comes from the gauge and one from the kernel. No finite product has
been replaced in a claim about its norm: (3)--(6) evaluate precisely
the continuum exponent already defined in L673.

### 2. Uniform curvature and the strict threshold

For 0<=s<1/4, the first term in F_ss satisfies

    integral_0^1 1/(d-s-t)^2 dt
       =1/[(d-s)*(d-s-1)] >=16/5.

For the negative term, U-t*(d-s)>=U-d=41/64, whence

    integral_0^1 t^2/(U-t*(d-s))^2 dt <=4096/5043.

Also s^2+r^2<1/16+81/400=53/200. By (5), K''(s)>200/159.
The second derivative of the quadratic gauge term is -6/5.
Combining these bounds gives

    e''(s)>=16/5-4096/5043+200/159-6/5
           =217890/89093>12/5.                              (7)

The exact arithmetic below certifies

    log 5>1609/1000, log(121/41)>541/500, pi<22/7.

Applying these inequalities in (6), with the correct sign for pi,

    e'(0+)>1609/1000+(121/100)*(541/500)-4/5-(20/27)*(22/7)
            =-1982821/9450000>-21/100.                       (8)

The right limits in (5) and the smoothness of (3) justify integrating
(7) twice from zero. For s>0, (8) supplies strictness, and hence

    e(s)>-(21/100)*s+(6/5)*s^2
         =(6/5)*(s-7/80)^2-147/16000
         >=-147/16000.                                      (9)

This proves (1) on the whole open segment, not a mesh. Subtracting
-1/100 from the final bound gives 13/16000>0. The weaker curvature
constant 12/5 is deliberate: it suffices for the decisive threshold
without optimizing the minimum of e.

### 3. Why every tested contour meets the segment

The real point 0 lies in Omega, while 1/4 is outside closure(Omega):
|x+1/4|=1, contrary to membership in D. Consider the connected
component containing 0 of

    {s in [0,1/4]: s in Omega}.

Since Omega is open and contains 0, this component extends to some
positive s. Since 1/4 is outside its closure, its right endpoint s_*
satisfies 0<s_*<1/4. That endpoint is in boundary(Omega)=Gamma.
This uses the usual interior/boundary property of a Jordan curve;
no convexity, symmetry, or rectangular shape is assumed. Evaluating
(1) at s_* and at the single allowed angle u=-1 proves (2).

For completeness, D is indeed pole-free for the interpolation
functions for every q: a parameter pole requires x+z=t_j*u and
therefore |x+z|=t_j<1, including t_0=0. The angle-only denominators
U*u-t_j*x are nonzero because U>d. The entire gauge adds no poles.
These facts justify D's use; they do not assert it exhausts the
finite-n analytic region.

### 4. Exact constant certificate and qualifications

Run from this notebook:

    python3 scripts/one-sided-hankel/positive-cone-real-crossing-certificate.py

The complete rational certificate is
`scripts/one-sided-hankel/positive-cone-real-crossing-certificate.json`.
It records every series term and remainder, both interval endpoints,
and all 14 checks, with zero failures. The analytic arguments (3)--(9)
and the crossing argument remain necessary; the script verifies their
constants, not those arguments or the cone target.

Specifically, for 1<=v<=2 put z=(v-1)/(v+1). The first 12 terms
of 2*sum_(j>=0) z^(2j+1)/(2j+1) lower-bound log v, and the omitted
positive tail is at most 2*z^25/[25*(1-z^2)]. Scale the two needed
arguments by powers of 2, using the same enclosure for log 2.
For atan v, 0<v<=1/2, the first 12 alternating terms have absolute
error at most v^25/25. Apply the classical Machin identity
pi=16*atan(1/5)-4*atan(1/239), with signed interval endpoints.
The identity follows from tangent addition and the angle's quadrant;
the series and remainders are the elementary evaluations already
used in L673. The shorter series here suffice for the coarse rational
bounds in (8). No decimal approximation enters a pass/fail decision.

The floating diagnostic
`scripts/one-sided-hankel/positive-cone-real-crossing-screen.json`
suggested this barrier but is not a proof input. In particular its
sampled minimum neither establishes (1) nor proves optimality.

The conclusion only blocks the criterion sup E<=-1/100 for this
fixed gauge and contours satisfying the displayed D hypothesis.
It remains true if such contours vary with n. It does not block
n-dependent contours entering the additional finite-n collar, nor
more refined estimates using the zero of 1-z/rho, angular integration,
or cancellation in the signed contour integral. Different gauges,
different coefficients, and a cone separating functional are also
outside this obstruction. Polynomial prefactor estimates cannot
repair the failed sup E criterion itself, but (2) alone does not
lower-bound the finite-n integrand, because the gauge can vanish.

This strengthens L673's one-point rectangle obstruction to every
contour in the stated common region. It is therefore an informative
stop for contour-shape-only improvement of that sufficient estimate,
not a stop of the positive-cone target or of the unit-residue H route.

## Mathlib

Full matching coverage for this fixed-gauge contour obstruction has
not been checked; no absence claim is made. Elementary differentiation,
logarithm/arctangent series bounds, the interval crossing argument and
the Jordan interior property support the proof. Supporting formal
results would not supply the evaluated rate barrier by themselves.
