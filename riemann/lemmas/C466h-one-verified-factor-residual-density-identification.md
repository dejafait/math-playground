# Corollary 466h: one verified-factor residual density identification

## Hypotheses

Use C466a's actual probability density p=c_0 Theta=theta_1, with
Laplace transform 1/h, and its C^infinity zero extension to R.
Use C466b's finite multiset M_100 of rates gamma^2 for gamma<=100,
with exactly one first-zero occurrence deleted and all other
multiplicities retained. These are the only local mathematical inputs;
no hypothetical contact is needed here.

Import the one-sided part of Suvrit Sra, *On some positivity properties
of the Riemann Xi function*, [arXiv:2611.02944v1, Theorem C.20,
pp41-42, (C.55) and (C.57)](https://arxiv.org/pdf/2611.02944v1).
It gives an independent exponential decomposition of S_1 with the
specified finite factors and a positive residual having a smooth,
strictly positive density on (0,infinity). Its transform is P_100/h,
where P_100(s)=product_(lambda in M_100)(1+s/lambda).

The theorem requires 100<=U<=U_PT and a verified retained anchor with
2<=gamma_*^2<=U^2/4-1/4. Here U=100 and gamma_*=gamma_1, so
196<gamma_1^2<225<2499.75 verifies that restriction. The verified
height, zero counting, strip and symmetry inputs remain the external
qualifications in C466a/b. This application does not independently
replay them, the source theorem, or its finite numerical certificates.
The normalization of S_1 agrees with p, not Theta: both use L018's
completion, c_0=xi(1/2), and transform 1/h. The source version above
is not silently identified with another version's theorem numbering.

## Conclusion

For every indexed occurrence lambda in M_100, the function

    r_lambda(x)=p(x)+p'(x)/lambda,       x in R,             (1)

is a C^infinity probability density, zero on (-infinity,0] and
strictly positive on (0,infinity). Every derivative at zero vanishes.
It is the density of the law obtained by putting back every extracted
exponential except that one occurrence. In particular, with
e_lambda(t)=lambda exp(-lambda t) for t>=0, zero otherwise,

    p=e_lambda*r_lambda,
    integral_0^infinity exp(-sx)r_lambda(x)dx
       =(1+s/lambda)/h(s),                 s>=0.           (2)

The convolution equality is pointwise. Removing a selected occurrence
of a repeated rate removes exactly one factor, not the other copies.
Moreover p' is absolutely integrable, lim_(x->infinity)p(x)=0, and
integral_0^infinity p'=0; thus normalization in (1) has no unpaid
endpoint term. No decay at infinity of every higher derivative is
asserted or needed. For Theta the corresponding expression is
r_lambda/c_0 and has mass 1/c_0, not one.

This is an applicability specialization of a known factor law, not
a new positivity theorem. It proves no higher-order differential
determinant sign for r_lambda, no C466b(22) inequality, and no global
PF property or RH. First-zero signed mass, full tail, strict forcing,
simultaneous contacts, propagation and L030-L032/C032a transfer remain
unresolved.

## Proof

### Occurrences and the put-back law

Index M_100 by a finite set I, with rates lambda_i>0; equal values
are allowed at different indices. Import C.20 in the form

    S_1 =_law R + sum_(i in I) E_i,

with independent summands and E_i exponential of rate lambda_i.
Write f for the density of R supplied by that theorem; it has mass
one on (0,infinity), is smooth there and is strictly positive there.
Fix a in I and form Y_a=R+sum_(i!=a)E_i. These summands are
independent of E_a. This constructs a probability law on (0,infinity)
and S_1=_law E_a+Y_a. There is no rescaling or shift.

For clarity, construct its density on the positive axis by convolving
f successively with the factors at i!=a. If v is any locally
integrable probability density on that axis, one such convolution is

    (e_mu*v)(x)=mu exp(-mu x) integral_0^x exp(mu t)v(t)dt. (3)

For finite x the integral exists because its exponential weight is
bounded on [0,x] and v is integrable there. Its indefinite integral
is continuous, so (3) is continuous for x>0. If v is strictly positive
on that axis, (3) is strictly positive, because the integral over any
closed subinterval of (0,x) is positive. Tonelli's theorem gives
mass one: integral of the nonnegative convolution is the product of
the two masses. These arguments can be iterated through the finite
list. If the list is empty use f itself. We obtain a continuous,
strictly positive, unit-mass density g_a of Y_a on (0,infinity).
No derivative estimate or boundary smoothness for f has been assumed.

### From equality of laws to pointwise differentiation

The continuous density of E_a+Y_a on (0,infinity) is

    k(x)=lambda_a exp(-lambda_a x)
                 integral_0^x exp(lambda_a t)g_a(t)dt.     (4)

Equality of laws identifies k with p almost everywhere. Both are
continuous on this open interval, hence they agree at every point:
if their continuous difference were nonzero at a point, it would
stay nonzero on an interval of positive Lebesgue measure.

At any x>0 the integrand in (4) is continuous near x. The fundamental
theorem of calculus therefore differentiates its indefinite integral
there, even if its integrand has not been extended continuously to
zero. Equivalently split the integral at any fixed b in (0,x) and
differentiate the second, ordinary compact-interval integral. The
product rule yields

    p'(x)=lambda_a g_a(x)-lambda_a p(x).                  (5)

Thus g_a(x)=p(x)+p'(x)/lambda_a pointwise for x>0.
This is the necessary local differentiation of the exponential
convolution, not a reproof of C.20. The elementary calculus tool is
the fundamental-theorem/product-rule argument underlying Hunter,
*The Riemann Integral*, [Chapter1, Theorem1.53 and proof,
p32](https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf), already
assessed in assessment909/review910. No infinite-interval transform
formula for p' is used to infer (5).

Define r_lambda by (1) on the whole real line. Since the actual p
is C^infinity there, so is this function. On the negative axis both
p and p' vanish. At zero all derivatives vanish because

    r_lambda^(j)(0)=p^(j)(0)+p^(j+1)(0)/lambda=0

for each finite j. Its positive-axis values equal g_a, hence are
strictly positive and have mass one. This proves the claimed flat
extension without importing an unproved extension for f or g_a.
There is no atom at zero: the put-back law already has the density
g_a of mass one on (0,infinity).

The right side of (2)'s convolution agrees with (4) for x>0 and is
zero for x<0. At x=0 its integral is zero, equal to p(0). This pays
all finite endpoint claims. Each occurrence other than a remains in
Y_a; the argument does not require distinct rates or zero simplicity.

### Infinity, mass, and the transform

From (5), p'=lambda_a(g_a-p) on the positive axis. Since both
densities have mass one, integral |p'|<=2lambda_a. To check the
endpoint at infinity directly, split (4) at A>0. For x>A its first
piece is at most lambda_a exp(-lambda_a(x-A)), and its second piece
is at most lambda_a integral_A^infinity g_a(t)dt. First send x to
infinity with A fixed, then send A to infinity. Nonnegativity gives
lim p(x)=0. Together with p(0)=0, the finite-interval fundamental
theorem and absolute integrability of p' yield integral p'=0.
Consequently integrating (1) also confirms mass one with both
endpoint terms included.

For s>=0 all Laplace integrals of these probability laws exist.
Tonelli applied to the nonnegative exponential convolution gives

    1/h(s) = [lambda_a/(lambda_a+s)] integral exp(-sx)g_a(x)dx.

Division by the strictly positive displayed factor proves (2).
It also shows precisely which one factor has been removed. No
passage to an infinite family, interchange of signed integrals, or
unproved derivative growth condition occurs. Scaling back by c_0
gives the stated Theta normalization. This completes the approved
identification and endpoint audit. No contact inequality was used
or obtained.

## Mathlib

Full matching coverage of the one-factor reciprocal-Xi identification
has not been checked. C466b records supporting compact-support
convolution differentiation results, but those do not by themselves
identify the source law or justify this put-back construction. The
proof here uses Tonelli, elementary finite-interval calculus and
continuity of densities; no specific matching declaration is claimed.
Unknown coverage is not evidence of absence.
