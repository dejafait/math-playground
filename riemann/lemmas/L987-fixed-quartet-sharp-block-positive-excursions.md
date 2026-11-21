# Lemma 987: positive exponential excursions of the fixed synthetic quartet

## Hypotheses

For integers n>=2 use the usual generalized Laguerre polynomials and

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u).

Fix tau=10^13, rho=3/4+i*tau and the four distinct prescribed numbers
Q={rho,conj(rho),1-rho,1-conj(rho)}, each with weight1. Define

    W_n=-Re sum_(q in Q) integral_n^(2*n) exp((q-1)*u)*K_n(u)du.

These are finite ordinary integrals. The quartet is synthetic: none
of its members is asserted to be a zeta zero. The height is fixed as
n tends to infinity. No RH, zero isolation, zeta-zero simplicity,
infinite zero-sum interchange or estimate for actual primes is assumed.

## Conclusion

Put omega=1+pi/2 and, for sigma in {+1,-1},

    alpha_sigma=2*tau+sigma*omega,
    c_sigma=1/(1/4+i*(tau+sigma/2)),
    F_n=Re(c_+*exp(i*n*alpha_+)+c_-*exp(i*n*alpha_-)).

Then, for fixed tau and n tending through integers,

    W_n=exp(n/2)/(2*sqrt(pi)*n^(3/2)) * [F_n+O(1/n)].       (1)

The error is additive, including when F_n vanishes. In particular,

    limsup_(n->infinity) log(1+max(W_n,0))/n = 1/2.         (2)

Both endpoints, the -1 in the exact averaged kernel and all four
quartet terms are retained in (9) below before any smaller terms are
bounded. The onset is existential; no explicit first positive index
or assertion uniform in a growing height is made.

Step248, 10 November2026: REPRODUCTION under the pre-existing
SPECIALIZE assessment review246, separately approved in step247.
This is a local signed specialization of the checked tools, not a
claim of progress beyond those sources, an actual B_n lower bound,
payment of L984(H), an RH equivalence or an RH candidate. Step249,
10 November2026: separate conceptual audit passed for this exact
fixed-height synthetic statement. No new bound is claimed by the audit.

## Proof

### Source inputs and uniform kernel specialization

Use L985 only for its exact finite connection and bulk setup; its
Vaughan conclusions are not inputs. The connection is
[DLMF18.18.18](https://dlmf.nist.gov/18.18.E18), at degree n-1,
alpha=1, beta=2. Every connection coefficient (1)_j/j! is1, so

    K_n(u)=[L_(n-1)^(2)(u)-1]/(n-1).                      (3)

The source-to-kernel specialization is justified here. Let

    nu=4*n+2, t=u/nu,
    xi(t)=[sqrt(t-t^2)+arcsin(sqrt(t))]/2,
    Phi_n(u)=nu*xi(t)-5*pi/4,
    D(t)=4*t^(5/4)*(1-t)^(1/4),
    A_n(u)=sqrt(2/(pi*nu))/[(n-1)*D(t)].

For n>=2 and n<=u<=2n, t is in J=[1/5,1/2]. This compact
interval stays away from zero and the turning point; xi is positive
and bounded away from zero on J. Apply the uniform scaled expansion
[DLMF18.15.17-20](https://dlmf.nist.gov/18.15#iv) at degree n-1,
alpha=2, M=1, with its fixed-delta uniformity. Its specialized form is

    L_(n-1)^(2)(u)=exp(u/2)/D(t) *
      [sqrt(xi)*J_2(nu*xi)+B_0(xi)/(nu*sqrt(xi))*J_3(nu*xi)
                         +sqrt(xi)*envJ_2(nu*xi)*O(nu^(-1))].

Here the explicit coefficient18.15.20 is smooth and bounded on J;
in this specialization it is

    B_0(xi(t))=-1/2*[-15/8+xi(t)*sqrt((1-t)/t)*
                  (15/8+t/(4*(1-t))+5*t^2/(24*(1-t)^2))].

The exact prefactor, coefficient and uniformity in18.15.17-20 were
rechecked directly in the live source on10 November2026. This was
application of the approved source, not a new literature assessment.
Use the fixed-order large-positive-argument expansion
[DLMF10.17.2-3](https://dlmf.nist.gov/10.17#i):
J_2(z)=sqrt(2/(pi*z))*(cos(z-5*pi/4)+O(1/z)),
J_3(z)=O(z^(-1/2)) and envJ_2(z)=O(z^(-1/2)). For the last
bound the envelope definition in [DLMF2.8.34](https://dlmf.nist.gov/2.8.E34)
is sqrt(J_2(z)^2+Y_2(z)^2) beyond the fixed positive crossover X_2;
[DLMF10.17.3-4](https://dlmf.nist.gov/10.17#i) bounds both functions
by O(z^(-1/2)) there. Here z=nu*xi is comparable to n, so this
range holds uniformly beyond one onset. This makes explicit the
envelope convention in the approved source, without adding a new
asymptotic hypothesis. The explicit J_3 correction and the two additive
source remainders are therefore all bounded at the following scale:

    K_n(u)=exp(u/2)*A_n(u)*cos(Phi_n(u))-1/(n-1)+E_n(u),
    |E_n(u)|<=C_B*exp(u/2)*n^(-5/2).                     (4)

There is one finite C_B for all n>=2 and u in[n,2n]. The sources
first give it beyond an onset; each of the finitely many earlier
n has a continuous difference on its compact interval, so enlargement
of C_B includes them. No first-neglected-term remainder rule is
used. No derivative of E_n is asserted or needed. In particular,
(4) is an additive bound at every cosine zero.

For the finite integration estimate, define the finite constants

    M_0=max_(t in J) |1/D(t)|,
    M_1=max_(t in J) |(1/D)'(t)|,
    C_0=sqrt(2/pi)*M_0, C_1=sqrt(2/pi)*M_1/4.

Since nu>=4n and n-1>=n/2,

    |A_n(u)|<=C_0*n^(-3/2),
    |A_n'(u)|<=C_1*n^(-5/2).                            (5)

Direct differentiation of the explicit phase gives

    p_n(u)=Phi_n'(u)=sqrt(nu-u)/(2*sqrt(u)),
    p_n'(u)=-nu/[4*u^(3/2)*sqrt(nu-u)].

On the block, nu<=5n and nu-u>=2n. Thus |p_n'|<=
5/(4*sqrt(2)*n)<1/n. These estimates concern only explicit smooth
functions, not the unknown remainder in (4).

### Exact finite endpoint reduction with an integrated error

For a in {1/4,-1/4}, put

    I_a(n)=integral_n^(2*n) exp((a-1/2+i*tau)*u)*K_n(u)du,
    g_(a,sigma,n)(u)=a+i*(tau+sigma*p_n(u)),
    Z_a(n)=[exp((a-1/2+i*tau)*2*n)-exp((a-1/2+i*tau)*n)]
                           /[(n-1)*(a-1/2+i*tau)],
    T_a(n)=integral_n^(2*n) exp(a*u)du.

The original four terms give exactly

    W_n=-2*Re(I_(1/4)(n)+I_(-1/4)(n)).                   (6)

Indeed K_n is real, and each real-part pair consists of conjugates.
In particular the pair with real part1/4 has not been suppressed.

Expand the cosine into its two exponentials. Since |g|>=|a|=1/4,
one integration by parts gives the finite identity

    integral_n^(2*n) exp(a*u+i*(tau*u+sigma*Phi_n(u)))*A_n(u)du
      =[exp(a*u+i*(tau*u+sigma*Phi_n(u)))*A_n(u)/g(u)]_n^(2*n)
       -integral_n^(2*n) exp(a*u+i*(tau*u+sigma*Phi_n(u)))
                                      *(A_n/g)'(u)du.    (7)

Here [f]_n^(2*n) means f(2n)-f(n). The smooth functions are on a
finite real interval and the denominator never vanishes. This is
the finite integration-by-parts tool underlying
[DLMF2.3.4-6](https://dlmf.nist.gov/2.3#i), applied directly with
its remaining integral bounded below. We do not invoke a
fixed-amplitude asymptotic for an unchecked n-dependent family or
the analytic-contour theorem2.4.10-13.

Using (5) and |p_n'|<=1/n yields the explicit family estimate

    |(A_n/g)'|<=4*|A_n'|+16*|A_n|*|p_n'|
                <=C_D*n^(-5/2),   C_D=4*C_1+16*C_0.     (8)

The integral of E_n in (4) is bounded in absolute value by
C_B*n^(-5/2)*T_a(n). Combining (4), (7) and (8), with both
endpoint evaluations still present, gives

    I_a(n)=1/2*sum_(sigma=+-1)
        [exp(a*u+i*(tau*u+sigma*Phi_n(u)))*A_n(u)
                                     /g_(a,sigma,n)(u)]_n^(2*n)
          -Z_a(n)+R_a(n),
    |R_a(n)|<=(C_B+C_D)*n^(-5/2)*T_a(n),
    T_(1/4)(n)=4*(exp(n/2)-exp(n/4)),
    T_(-1/4)(n)=4*(exp(-n/4)-exp(-n/2)).                (9)

Together (6) and (9) are a signed endpoint expansion for the full
quartet, including the exact -1 correction from (3). Constants
refer to finite source and compact-interval bounds, not an
unproved oscillatory saving or a differentiated O term.

For clarity, the elementary estimates that will remove the smaller
pieces are

    |Z_(1/4)(n)|<=8*n^(-1)*exp(-n/4),
    |Z_(-1/4)(n)|<=(8/3)*n^(-1)*exp(-3*n/4).            (10)

These follow by integrating exp((a-1/2)*u)/(n-1) in absolute
value. Each of the two-endpoint sums in (9) has modulus at most
4*C_0*n^(-3/2)*(exp(2*a*n)+exp(a*n)). Thus the entire a=-1/4
pair, including its error and Z term, decays exponentially. The
lower endpoint of the a=1/4 pair costs O(exp(n/4)*n^(-3/2)).
Its upper endpoint is the only term on the exp(n/2)*n^(-3/2)
scale. These estimates explicitly prevent cancellation by any of
the retained smaller pieces.

### Upper endpoint amplitude, phase and sign

At u=2n, t=1/2-1/nu. Since xi(1/2)=1/4+pi/8 and
xi'(1/2)=1/2, Taylor's theorem on J gives

    Phi_n(2n)=n*(1+pi/2)-pi+epsilon_n,
    |epsilon_n|<=M_2/(2*nu),
    M_2=max_(t in J)|xi''(t)|<infinity.                 (11)

The bounded Taylor remainder is multiplied by nu, not
differentiated. Also

    p_n(2n)=sqrt(1+1/n)/2=1/2+O(1/n),
    A_n(2n)=n^(-3/2)/(2*sqrt(pi))+O(n^(-5/2)).          (12)

For the second estimate use D(1/2)=sqrt(2), the derivative
bound M_1, (n-1)^(-1)=n^(-1)*(1+O(1/n)) and
nu^(-1/2)=(4n)^(-1/2)*(1+O(1/n)). These are ordinary real
Taylor estimates with bounded derivatives on compact intervals.

The difference between 1/g_(1/4,sigma,n)(2n) and c_sigma is
at most16*|p_n(2n)-1/2|. Also |exp(i*sigma*epsilon_n)-1|
<=|epsilon_n|. Using (11)-(12) in the upper endpoint of (9)
therefore introduces O(exp(n/2)*n^(-5/2)). The lower endpoint
is absorbable at this scale since n*exp(-n/4) is bounded;
(10) and the negative-a pair are absorbable as well. Finally,

    exp(i*sigma*Phi_n(2n))
       =-exp(i*sigma*n*omega)*(1+O(1/n)).

The minus sign here cancels the minus sign in (6); its factor2
cancels the cosine expansion's factor1/2. Consequently (1)
follows with precisely the positive prefactor displayed there.
Even though |c_sigma| is small at the prescribed large height,
it is a fixed nonzero constant. The additive O(1/n) eventually
becomes smaller than any fixed positive sign margin. No finite
moderate-n numerical experiment is used to assert this comparison.

### Positive integer subsequence without a density assumption

Only finitely many frequency coincidences must be excluded. The
approved Lindemann-Weierstrass input is L. Fukshansky,
*Geometric Number Theory*, live undated author notes,
[Theorem6.2.1, printed p138](https://www1.claremontmckenna.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf#page=142):
exponentials of distinct algebraic numbers are linearly independent
over the algebraic numbers. Its elementary specialization supplies
irrationality of pi: if pi were rational, 0 and i*pi would be
distinct algebraic numbers, whereas exp(0)+exp(i*pi)=0 contradicts
the theorem. No stronger transcendence or independence premise is
used, and no general theorem is reproved.

The frequencies alpha_+, alpha_-, 2*alpha_+, 2*alpha_-,
alpha_+-alpha_- and alpha_++alpha_- are all nonzero modulo2*pi.
For the first four, a putative equality to2*pi*k would respectively
give

    2*tau+1=pi*(2*k-1/2),  2*tau-1=pi*(2*k+1/2),
    4*tau+2=pi*(2*k-1),    4*tau-2=pi*(2*k+1).

The left sides are nonzero integers, the coefficients on the right
are nonzero rationals, and pi is irrational. The difference
frequency would give2=pi*(2*k-1), also impossible. The sum
frequency is4*tau; equality4*tau=2*pi*k either has k=0,
which is impossible, or makes pi rational. This checks all
characters needed for the first and second moments, even though
the joint orbit need not be dense in the full two-dimensional torus.

For any theta nonzero modulo2*pi, the finite geometric-sum identity
gives

    |N^(-1)*sum_(n=1)^N exp(i*n*theta)|
                      <=2/[N*|1-exp(i*theta)|] -> 0.    (13)

This uses only the finite-character calculation in the approved
linear-sequence source, T. Tao, *Higher Order Fourier Analysis*,
[5June2012 author manuscript, Proposition1.1.2 and Exercise1.1.5,
printed pp5-6](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf#page=13).
There is no appeal to unverified rational independence, full-torus
equidistribution or an infinite Fourier expansion.

Define M=|c_+|+|c_-|>0 and V=(|c_+|^2+|c_-|^2)/2>0.
Expanding the real parts and their square, (13) and the complete
frequency check give

    N^(-1)*sum_(n=1)^N F_n -> 0,
    N^(-1)*sum_(n=1)^N F_n^2 -> V,   |F_n|<=M.          (14)

Since F_n^2<=M*|F_n| and max(F_n,0)=(|F_n|+F_n)/2,
the liminf of the average of max(F_n,0) is at least V/(2*M).
Hence F_n>=delta:=V/(4*M)>0 for infinitely many integer n;
otherwise that average would be at most delta+o(1), a contradiction.
Removing n=1 does not change this statement.

On that infinite subsequence, (1) gives, eventually,

    W_n>=delta*exp(n/2)/(4*sqrt(pi)*n^(3/2)).            (15)

The same formula bounds |W_n| by C*exp(n/2)*n^(-3/2) for
all sufficiently large n. Taking logarithms in this upper bound
and (15) proves the equality (2). This is a positive signed
excursion result, not merely an envelope.

### Scope toward the main gap

The computed rate1/2 exceeds a subexponential allowance for this
synthetic mode. It diagnoses a spectral obligation for the sharp
moving block. It supplies no transfer from Q to the actual B_n,
no dominance over other zeros, and no realization of Q in zeta.
L981/L982's actual-Lambda normalization, L986's proper-power payment,
both complementary ranges and L984(H) remain unchanged and unpaid
where previously open. Those lemmas are context, not proof inputs.
The only local lemma input is L985's finite connection/bulk setup;
the needed source specialization has been checked explicitly above.
Numerical evidence, infinite sums and target-equivalent positivity
are not used.

### Separate critical audit, step249

The full argument (3)-(15) was independently checked under unchanged
review246. The live source equations18.18.18 and18.15.17-20 agree
with the degree n-1 and alpha=2 substitutions. Their prefactor is
exactly 1/D(t); no factorial normalization is missing. The additional
envelope citation above spells out the source's own definition.

In (5), the bounds follow from
1/((n-1)*sqrt(nu))<=n^(-3/2) and
1/((n-1)*nu^(3/2))<=n^(-5/2)/4. Thus (8) and the integral
of (4)'s unknown error are uniform over the entire moving interval.
For each a, their combined contribution is bounded by exactly the
T_a(n) factor displayed in (9), including the decaying pair. There
is no factor of n lost by replacing T_(1/4) with its exponential
upper bound. Both corrections in (10) have the asserted exponents.

The constant phase at the upper endpoint was recomputed as
2*xi(1/2)-xi'(1/2)-5*pi/4=-pi. It therefore contributes -1
for both sigma, and cancels (6)'s minus sign. The cosine factor1/2
and conjugate-pair factor2 cancel as asserted. The endpoint
amplitude in (12) is positive. Every discarded term is bounded by
O(exp(n/2)*n^(-5/2)); no relative error at a zero of F_n is used.

To check that (14) lists all needed resonances, write
z_sigma=c_sigma*exp(i*n*alpha_sigma). Then exactly

    F_n^2=(|c_+|^2+|c_-|^2)/2
       +Re(z_+^2+z_-^2)/2+Re(z_+*z_-+z_+*conj(z_-)).

The nonconstant frequencies are precisely the two doubles, the sum
and the difference checked above; the mean of F_n uses the two
single frequencies. Irrationality of pi suffices for this finite
list at the specified integer tau. The positive-mean bound for
max(F_n,0), hence delta=V/(4*M), survives every listed resonance
test. Since tau is fixed, delta>0 is fixed, and the additive
O(1/n) is eventually below delta/2. This verifies (15) and the
limsup equality. It supplies no effective onset or uniformity when
tau grows, and audits no other portion of L985.

## Mathlib

Full matching Mathlib coverage of this fixed-quartet moving-integral
asymptotic and positive excursion statement is not checked. The
named analytic inputs are the precise external results cited above;
elementary finite sums and calculus do not constitute a checked
formalization of the full result. Unknown coverage is not absence.
