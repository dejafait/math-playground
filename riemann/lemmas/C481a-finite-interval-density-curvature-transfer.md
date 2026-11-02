# Corollary 481a: finite-interval density/curvature transfer

## Hypotheses

Let T>=e^2 be real, L=log T, h=1/L,
M=floor(sqrt(T/(2 pi))), and J=[T+h,2T-h]. Set

    A_M(t)=sum_(1<=n<=M)n^(-1/2-it),  F_M(t)=|A_M(t)|^2,
    D_h(t)=F_M(t+h)-2F_M(t)+F_M(t-h).

Use precisely L481's complete ordered-pair ratio component

    U_T(t)=sum_(1<=n,m<=M)log(n/m)^2/sqrt(nm)
                                      exp(it log(m/n)).

The integer M is fixed throughout every differentiation and integration
for this T. No moving cutoff, RH, zero assumption, phase independence,
moment estimate or density lower bound is imposed. The chosen lower
bound on T ensures M>=1 and T>4h, so the intervals below are ordered.

## Conclusion

For every real t,

    F_M''(t)=-U_T(t),
    D_h(t)=-integral_(t-h)^(t+h)(h-|x-t|)U_T(x) dx.       (1)

Define q_T on the whole real line by zero outside [T,2T] and by

    (x-T)^2/2,                       T<=x<=T+h;
    h^2-(T+2h-x)^2/2,                T+h<=x<=T+2h;
    h^2,                            T+2h<=x<=2T-2h;
    h^2-(x-(2T-2h))^2/2,            2T-2h<=x<=2T-h;
    (2T-x)^2/2,                     2T-h<=x<=2T.

Adjacent formulas agree at their common endpoints. Then exactly

    integral_J D_h(t) dt=-integral_T^(2T)q_T(x)U_T(x) dx, (2)
    integral_J |D_h(t)| dt
       <=integral_T^(2T)q_T(x)|U_T(x)| dx
       <=h^2 integral_T^(2T)|U_T(x)| dx.                 (3)

In particular, if a fixed c>0 satisfies

    integral_J |D_h(t)|dt>=c T log T                     (4)

for every sufficiently large real T, then at those same T

    integral_T^(2T)|U_T(t)|dt>=c T(log T)^3.             (5)

The identical implication holds on any specified unbounded sequence
where (4) holds. Equation (4) is an unresolved conditional premise,
not a result of this corollary. Nothing here compares U_T with L477's
full residual R_T, proves either defect threshold, saves negative mass,
or establishes a Xi sign. This is a known-input calculus specialization;
it claims no mathematical novelty beyond the sources checked.

## Proof

### 1. Finite curvature and the imported Peano formula

Expansion of the finite square gives

    F_M(t)=sum_(n,m<=M)(nm)^(-1/2)exp(it log(m/n)).

Twice differentiating this finite sum multiplies each term by
-log(m/n)^2. Since log(m/n)^2=log(n/m)^2, this proves the first
identity in (1), with no factor 2 or omitted ordered pair. Diagonal
terms are constant in F_M and zero in U_T. Interchanging n,m shows
that U_T is real: the two off-diagonal terms are conjugates.

Import Carl de Boor, *Divided Differences*, Surveys in Approximation
Theory 1 (2005), 46--69, Section 9, p. 62, equations (46)--(48),
[primary journal text](https://surveys-in-approximation-theory.com/papers/2/2.pdf#page=17).
For real knots tau_0<tau_1<tau_2 in a closed interval and a C^2
function f on that interval, the cited representation reads

    [tau_0,tau_1,tau_2]f=(1/2)integral M(x|tau)f''(x) dx,
    M(x|tau)=2 DD_tau g_x, where g_x(y)=(y-x)_+.

The normalized kernel has integral one. We cite this representation
rather than reprove its general Taylor-remainder argument. Here F_M
is C^infinity on the real line and the three knots t-h,t,t+h are
distinct, since h>0. Thus its hypotheses hold on [t-h,t+h].

For these knots the finite divided-difference formula is

    [t-h,t,t+h]f=(f(t+h)-2f(t)+f(t-h))/(2h^2).

Applying it to (.-x)_+ gives

    M(x|t-h,t,t+h)=(h-|x-t|)_+/h^2.

Indeed the numerator is zero outside [t-h,t+h], equals x-(t-h)
on [t-h,t], and equals t+h-x on [t,t+h], before division by h^2.
Consequently its integral is h^2/h^2=1. Substitution into the
imported representation cancels both the factor 2 and h^2, giving
D_h(t)=integral (h-|x-t|)_+ F_M''(x)dx. The first curvature identity
then gives the second identity in (1). Only this normalization and
the finite polynomial identification are specialized here.

### 2. Complete finite-interval weight

All functions are continuous on the compact integration region;
the triangular kernel is nonnegative. Ordinary Fubini therefore
applies both to U_T and |U_T|. The integrated kernel is exactly

    q_T(x)=integral_(T+h)^(2T-h)(h-|x-t|)_+ dt.           (6)

If x<T or x>2T, its support has no overlap of positive length
with J; the integral is zero, also at x=T and x=2T. On
[T,T+h] the overlapping t interval is [T+h,x+h] and integration
of h+x-t gives (x-T)^2/2. On [T+h,T+2h] the full triangle of area
h^2 loses only its left tail below T+h, of area (T+2h-x)^2/2.
On [T+2h,2T-2h] the full triangle is present. The substitution
t -> 3T-t in (6) gives q_T(3T-x)=q_T(x), supplying precisely the
last two pieces displayed in the conclusion. The condition T>4h
ensures the left and right losses do not overlap.

At T,T+h,T+2h,2T-2h,2T-h,2T the values are respectively
0,h^2/2,h^2,h^2,h^2/2,0. Thus q_T is continuous, everywhere
nonnegative, positive on (T,2T), has support [T,2T], and is at
most h^2. Equivalently the upper bound follows directly by enlarging
the t interval in (6) to the whole real line. No boundary strip has
been deleted or identified with the central plateau.

Integrating (1) and applying Fubini gives (2). The pointwise triangle
inequality in (1), followed by Fubini for the nonnegative integrand,
gives the first inequality in (3). The verified bound q_T<=h^2
gives its second inequality. Finally h^(-2)=(log T)^2 converts (4)
and (3) to (5), with exactly the same c and the same heights. There
is no loss of endpoints, interval extension or asymptotic error.
This deduction establishes no instance of the premise (4).

## Mathlib

Full matching and supporting Mathlib coverage have not been checked.
The finite differentiation, Peano specialization and compact Fubini
argument above are informal proofs, not a formal verification. Unknown
Mathlib availability is not an absence claim.
