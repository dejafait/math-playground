# Lemma 679: polynomial positive-arc mass for every norm-budgeted full action

## Hypotheses

Let q>=1 be an integer, n=12q+3, J=n-1 and tau=J/n. Use
the complete L666 product with normalized angular measure:

    x=-d=-5/4, R=11/8, U=R^2=121/64, t_j=j/n,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a), |u|=1,
    A_n(a)=mean_u conjugate(psi_n(u))*W_a(u), |a|>tau,
    mean_u F=(1/(2*pi))*integral_(-pi)^pi F(exp(i*phi)) dphi.

Interpret the quotient by its rational continuation at removable
singularities. Let C be any fixed real number, and let psi_n be any
complex L2 function for this normalized measure satisfying

    ||psi_n||_2<=exp(n/100)*n^C,
    A_n(x)=1,
    Re A_n(x+i*y)>=0 for every real |y|<=9/20.

Set theta0=2*arctan(9/25) and define exactly

    M_n=(1/(2*pi))*integral_(-theta0)^theta0
                  Re A_n(x+i*d*tan(theta/2)) dtheta.

No symmetry, prescribed zero, pole ansatz, finite-degree representation
of A_n, or restriction on the free Fourier modes is assumed.

## Conclusion

Put C_+=max(C,0) and D_C=21+4*C_+. For every admissible n with

    n>=n_C=ceil(128*D_C^2),

one has

    M_n>=1/(128*D_C^2*n^2)>=n^(-3).                       (1)

Thus the proposed uniform polynomial mass assertion holds with K_C=3
and the displayed onset, conditional on the stated feasible action.
This does not prove that any such action exists. It imports known
analytic approximation and Markov inequalities and specializes their
applicability and error transfer to the full kernel. It is not a claim
of progress beyond those known tools or a proof of the cone bound.
Complementary-ray/parameter-circle coupling, cone/H/support/Xi
realization and actual-Xi mixed positivity remain separate gaps.
The independent replay in Section 6 confirms this conditional bound
and its stated uniform onset; it does not verify any downstream bridge.

## Proof

### 1. Assessed scope and imported theorems

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-02-full-action-positive-arc-mass.md`.
This proof performs exactly its full-kernel approximation, real-trace,
sign-error and normalized-mass tasks. The approximation degree below
is a proof parameter and imposes no degree condition on the action.
L677's finite-degree mass, L678's rational-family attenuation and
L674's open-domain positivity are comparisons only and are not inputs.

Import L. N. Trefethen, *Approximation Theory and Approximation Practice*,
Chapter 8, Theorems 8.1--8.2, especially (8.2): if a complex function
is holomorphic on the open Bernstein ellipse E_rho, rho>1, and bounded
there by B, its degree-m Chebyshev projection has uniform error on
[-1,1] at most 2*B*rho^(-m)/(rho-1). The inspected author chapter
[source, lines 104--169](https://raw.githubusercontent.com/chebfun/ATAP/development/chap8.m)
and Chapter 4 (4.8)--(4.9),
[lines 151--157](https://raw.githubusercontent.com/chebfun/ATAP/development/chap4.m),
were retrieved 2 November 2026; the assessment records the coefficient
proof and limiting contours. We use complex approximation first,
rather than assuming the real part is holomorphic.

Import the named A. A. Markov polynomial inequality in V. Totik and
Y. Zhou, *Sharp constants in asymptotic higher order Markov inequalities*,
[author manuscript](https://www.math.u-szeged.hu/pot/Markovk.pdf),
21 November 2016, Section 1, equation (2), printed p.1:
for degree at most m on [-1,1], ||p'||_infinity<=m^2*||p||_infinity.
We apply it to a real polynomial with m>=1. Neither known theorem
is reproved; the following family-specific estimates and transfer
are the required specialization.

### 2. Fixed-neighborhood growth for the complete product

L666 (6), retaining j=0 and the denominator angle 1/u, gives

    W_a(u)=(x/a)*product_(1<=j<n)
             [(x-t_j*u)/(a-t_j*u)]
             *[(U*u-t_j*a)/(U*u-t_j*x)].                 (2)

Its possible parameter poles are a=0 and a=t_j*u. For |a|>tau
these are absent, and |U*u-t_j*x|>=U-d=41/64>21/64>0.
On each compact subset of |a|>tau, (2) and its parameter derivatives
are uniformly bounded in u. Normalized L2 embeds in L1 by
Cauchy--Schwarz, so differentiation under the angular integral is
justified by those uniform bounds. Thus A_n is holomorphic there.
Zeros of U*u-t_j*a cause no singularity in (2); apparent quotient
singularities of the original B_u ratio have already been removed.

Write b=9/20 and f_n(z)=A_n(x+i*b*z). Choose rho=3/2. The closed
Bernstein ellipse has semiaxes 13/12 and 5/12, so every point of
it satisfies |z|<=13/12 and |Im z|<=5/12. Consequently

    Re(x+i*b*z)<=-5/4+(9/20)*(5/12)=-17/16,
    17/16<=|x+i*b*z|<=5/4+(9/20)*(13/12)=139/80.

This closed ellipse and a neighborhood of it map into |a|>tau,
since tau<1. In particular f_n is holomorphic on an open neighborhood
of the closed ellipse, uniformly separated from every parameter pole.
For a in its image and |u|=1, each j>=1 factor of (2) obeys

    |x-t_j*u|<=9/4,       |a-t_j*u|>=1/16,
    |U*u-t_j*a|<=U+139/80=1161/320,
    |U*u-t_j*x|>=21/64.

Hence the modulus of each paired factor is at most

    36*(1161/105)=13932/35<400.

The j=0 factor has |x/a|<=20/17<400. Multiplying all n factors
gives |W_a(u)|<=400^n. By normalized Cauchy--Schwarz and the actual
norm budget,

    |f_n(z)|<=400^n*||psi_n||_2
             <=exp(7*n)*n^C=:B_n                         (3)

throughout the closed ellipse. Here log(400)+1/100<7; for example,
400<2^9 and log 2<7/10 suffice. No norm or degree bound on a finite
collection of angular modes has replaced the full L2 budget.

### 3. Complex approximation and real-trace errors

Choose the positive integer

    m=ceil((20+4*C_+)*n),  epsilon_n=4*exp(-n).

Then m<=(21+4*C_+)*n=D_C*n, using n>=1. The cited approximation
theorem, (3) and rho-1=1/2 give a complex polynomial P_m of degree
at most m satisfying

    ||f_n-P_m||_[-1,1]<=4*exp(7*n)*n^C*(3/2)^(-m)
                          <=epsilon_n.                  (4)

For completeness, log(3/2)>2/5 and log n<=n imply that the exponent
after the factor 4 is at most

    7*n+C*log n-(2/5)*(20+4*C_+)*n
      =-n+C*log n-(8/5)*C_+*n <=-n.

This covers negative C as well as nonnegative C, since log n>=0.
The strict logarithm inequality follows, for example, by integrating
the tangent-line lower bound for the convex function 1/t at t=5/4
over [1,3/2].

For real t set h_n(t)=Re f_n(t). Define the real-coefficient polynomial
p_m by taking real parts of the monomial coefficients of P_m. Then
p_m(t)=Re P_m(t) on the real interval, so (4) implies

    |p_m(t)-h_n(t)|<=epsilon_n,
    h_n(t)>=0 on [-1,1],    h_n(0)=1.

The polynomial g_m=p_m+epsilon_n is therefore nonnegative on the
whole closed interval and g_m(0)>=1. Moreover

    0<=g_m(t)-h_n(t)<=2*epsilon_n.                        (5)

No reflected holomorphic extension of a real part and no symmetry
of psi_n is needed.

### 4. Markov mass and absorption of the sign error

Let S=max_[-1,1] g_m>=1, attained at t_*. The cited Markov inequality
gives ||g_m'||_infinity<=m^2*S, even if its actual degree is smaller.
On the intersection of [-1,1] with
[t_*-1/(2*m^2),t_*+1/(2*m^2)], one has g_m>=S/2. This intersection
has length at least 1/(2*m^2), including when the maximum is at an
endpoint, because m>=1. Since g_m>=0 everywhere else,

    integral_(-1)^1 g_m(t) dt>=S/(4*m^2)>=1/(4*m^2).

Subtracting (5) over an interval of length two yields

    integral_(-1)^1 h_n(t) dt>=1/(4*m^2)-4*epsilon_n.

If n>=n_C=ceil(128*D_C^2), then n>=24 and the exponential series
gives exp(n)>=n^4/24>=n^3>=128*D_C^2*n^2. Therefore

    epsilon_n=4*exp(-n)<=1/(32*D_C^2*n^2)<=1/(32*m^2).

It follows that

    integral_(-1)^1 h_n(t) dt>=1/(8*m^2).                (6)

The possible constant-polynomial case also satisfies this argument:
we use the positive approximation parameter m, not the actual degree,
and Markov's derivative bound remains valid when the derivative is zero.

### 5. Exact angular mass and the fixed-C onset

The substitution

    theta(t)=2*arctan((9/25)*t), -1<=t<=1,

is an increasing smooth bijection onto [-theta0,theta0], including
both endpoints. Since d*(9/25)=b, the integrand defining M_n becomes
exactly h_n(t). With r=9/25,

    theta'(t)=2*r/(1+r^2*t^2)>=2*r/(1+r^2)=225/353>1/2.

Because h_n>=0, this lower density bound and (6) give

    M_n=(1/(2*pi))*integral_(-1)^1 h_n(t)*theta'(t) dt
         >=1/(32*pi*m^2)>=1/(128*m^2)
         >=1/(128*D_C^2*n^2)>=n^(-3),

using pi<4 and n>=128*D_C^2. This proves (1) with the exact saved
normalized mass. Both the approximation degree and onset depend only
on C and n, never on the eligible input psi_n. No finite sampling,
stronger-domain positivity or limit interchange is used.

### 6. Independent proof replay — 2 November 2026, step 61

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-02-full-action-mass-audit.md` covers exactly
this audit. Its inspected primary theorem statements and proofs are
reused, not replaced by a new search. Replayed the complete proof
above against L666 (6), without assuming the other conclusions of
L666 or the stopped classes in L674, L677 and L678. No failed
implication or correction to (1) was found. This is a REPRODUCTION
audit of a local specialization of known tools, not a new theorem
beyond the sources checked.

For fixed n, exact division gives (2), including x/a from j=0.
Its parameter denominators are a and a-t_j*u; its other denominator
U*u-t_j*x is separated from zero by at least U-d=41/64>21/64.
Thus parameter poles remain inside |a|<=tau, while apparent poles
of B_u(a) become numerator zeros of the continued quotient. Compact
parameter bounds are uniform for the actual angular circle. Since
the measure has mass one, ||psi_n||_1<=||psi_n||_2, which supplies
the integrable domination for the holomorphic action and all local
parameter differentiations. This argument applies to arbitrary
complex L2 inputs, without a finite Fourier restriction.

The ellipse computation has the correct rotation and both signs:
Re(x+i*b*z)=x-b*Im z lies between -23/16 and -17/16.
Consequently its image has |a|>=17/16>tau, and the triangle bound
is |a|<=139/80. Its compact image has a neighborhood in the same
pole-free domain. The estimates |a-t_j*u|>=1/16 and
|U*u-t_j*x|>=21/64 therefore hold on the entire closed ellipse.
The paired-factor arithmetic is

    (9/4)/(1/16) * (1161/320)/(21/64)
      =36*(1161/105)=13932/35<400.

There are n-1 such pairs and the remaining factor satisfies
|x/a|<=20/17<400. Normalized Cauchy--Schwarz gives the full-action
bound, with no assumption on which modes carry its norm. The
slack log(400)+1/100<7 is valid, for example from 400<2^9
and exp(7/10)>1+7/10+(7/10)^2/2+(7/10)^3/6>2.

The cited Chebyshev projection estimate applies to the complex
holomorphic f_n with B_n on this ellipse. With C_+=max(C,0),
m=ceil((20+4*C_+)*n) is positive and at most D_C*n.
The projection constant is 2/(rho-1)=4. The bound
log(3/2)>2/5 follows by integrating the strict tangent-line bound
for 1/t at 5/4. If C>=0, C*log n<=C*n<=8*C*n/5; if C<0,
C*log n<=0 and C_+=0. In both cases the complete exponent in
(4) is at most -n. Taking real monomial coefficients on the real
interval preserves the uniform error for every complex input.
Adding epsilon_n gives exactly 0<=g_m-h_n<=2*epsilon_n, using
the stated closed-segment sign condition and h_n(0)=1.

For Markov, nonnegativity makes S both the maximum and the
supremum absolute norm of g_m. The neighborhood of a maximum
has intersection length at least 1/(2*m^2) even at either endpoint,
and the derivative estimate gives g_m>=S/2 there. This verifies
the integral bound 1/(4*m^2), including constant polynomials.
The integrated approximation error is at most 4*epsilon_n,
not 2*epsilon_n. At the stated onset D_C>=21 and n>=24;
exp(n)>=n^4/24>=n^3>=128*D_C^2*n^2 implies
epsilon_n<=1/(32*D_C^2*n^2)<=1/(32*m^2).
Subtracting the error therefore leaves at least 1/(8*m^2).

Finally y=b*t corresponds exactly to theta=2*arctan(9*t/25).
Its derivative is at least 225/353>1/2, on the closed interval.
Nonnegativity of h_n is essential to this density comparison.
With the saved 1/(2*pi) normalization the successive lower bounds
are 1/(32*pi*m^2), 1/(128*m^2), and
1/(128*D_C^2*n^2). The last is at least n^(-3) precisely under
n>=128*D_C^2. Every bound and the integer ceiling depend only
on fixed C and n, uniformly over the eligible psi_n. Neither the
special congruence n=12q+3 nor an assumption of feasible-action
existence is used to absorb an error.

The continuation test is met: (1) survives all its hypotheses,
normalizations, endpoint cases and the fixed-C onset. This does
not audit L674's separate attenuation argument, prove any Poisson
coupling, exclude all feasible actions, or close cone/H/support/Xi
realization or actual-Xi positivity. No mathematical script or
numerical approximation was needed for these explicit inequalities.

## Mathlib

Full matching coverage of this norm-budgeted full-action mass bound
has not been checked. The source assessment did not check matching
Mathlib coverage of the quantitative Chebyshev/Markov inputs either.
Supporting holomorphy, integration or polynomial facts would not by
themselves establish the family-specific estimate. No formal
verification is claimed. Section 6 is an informal proof audit only;
matching Mathlib coverage remains unchecked.
