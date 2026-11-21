# Corollary 999d: signed bulk endpoint formula for the complete kernel

## Hypotheses

Use C997c's complete kernel with exactly C997s's parameters:

    n>=64 integer, N=n+1, I=[7/4,9/4],
    Z={z_star=1+i/8} union E, E=[15/8,17/8],
    gamma_j=15/8+j/(4n), 0<=j<=n, B_n=exp(sqrt(n)),
    K(t)=(L_N^(2)(t)-1)/N,
    g(t)=K(t)exp(-t/2)cosh(3t/8),
    k_n(c,z)=-2exp(-cn/4)[integral_(cn)^(c(n+2))g(t)exp(izt)dt
                           -integral_n^(n+2)g(t)exp(izt)dt].

Here c is real in I, z is in the CLOSED set Z, and L_N^(2) has the
standard Laguerre normalization. Set v=Im(z), so v is 0 or 1/8.
No actual-zero reconstruction, positivity, nonvanishing of L_N^(2),
coefficient choice or small E_n hypothesis is assumed.

## Conclusion

There exist finite constants D>=0, C=320+8D and an integer n_0>=64,
independent of c,z,n, such that the following holds for n>=n_0.
The onset and D are existential; no effective n_0=64 is asserted.
For t in the two original windows put

    x=t/(4N),
    a_N(t)=sqrt((N+1)(N+2))/N * t^(-1)/sqrt(2pi N)
                                      *[x(1-x)]^(-1/4),
    theta_N(t)=3 arccos(sqrt(x))
          +2N[arccos(sqrt(x))-sqrt(x(1-x))]-pi/4,
    omega_N(t)=-1/2 sqrt((1-x)/x)-3/(8N sqrt(x(1-x))).    (1)

All square roots and arccosines here are real, with arccos in (0,pi/2).
For beta=3/8 or -3/8, lambda=beta+iz, define

    P_beta(a,b;z)=1/2 sum_(s in {-1,1})
       [ a_N(t) exp(lambda t+is theta_N(t))
                         /(lambda+is omega_N(t)) ]_(t=a)^(t=b),
    S_beta(a,b;z)=[exp((lambda-1/2)b)-exp((lambda-1/2)a)]
                                                   /(lambda-1/2),
    J_beta(a,b;v)=[exp((beta-v)b)-exp((beta-v)a)]/(beta-v),
    W_n(c,v)=exp(-cn/4) sum_(beta in {-3/8,3/8})
                   [J_beta(cn,c(n+2);v)+J_beta(n,n+2;v)]. (2)

Every denominator is nonzero. In particular J_beta is positive. Retain
ALL four physical endpoints in the following signed expression:

    k_n^end(c,z)=-exp(-cn/4) sum_(beta in {-3/8,3/8}) {
       (-1)^N [P_beta(cn,c(n+2);z)-P_beta(n,n+2;z)]
         -[S_beta(cn,c(n+2);z)-S_beta(n,n+2;z)]/N }.

Then uniformly for c in I and z in Z,

    |k_n(c,z)-k_n^end(c,z)| <= C N^(-5/2) W_n(c,v).       (3)

The S terms are EXACT constant-subtraction integrals, not asymptotic
terms or discarded errors. Both beta contributions are retained.
Useful separate uniform envelopes are

    W_n(c,1/8)<=W_*(n):=9exp(9/8)+4exp(1/2)exp(-3n/16),
    W_n(c,0)<=W_E(n):=9exp(27/16)exp(9n/32)
                              +4exp(3/4)exp(-n/16).       (4)

For any ORIGINAL capped coefficients sum_j|A_j|<=B_n, let R_A and
R_A^end denote the target-minus-band combinations of k_n and k_n^end.
Then

    ||R_A-R_A^end||_C(I)
          <= C N^(-5/2)[W_*(n)+exp(sqrt(n))W_E(n)].        (5)

The right side divided by exp(-n/64) tends to infinity; its logarithm
is (19/64)n+sqrt(n)-(5/2)log N+O(1). Thus this absolute-error allowance
DOES NOT establish E_n=O(exp(-n/64)). Its excess is not a lower bound
on the actual error or E_n, and does not rule out cancellation.

Step408, 11 November2026: RESEARCH / REPRODUCTION / ADVANCE under the
pre-existing SPECIALIZE review406, separately approved step407. This is
a local signed formula specialized from known asymptotics, not a claim
of progress beyond the checked literature. The new specialization is
UNAUDITED at step408; the step410 conceptual audit below accepts
(1)-(5) without correction. The source constants/onset are ineffective here. No RH
candidate or exponentially accurate integrated approximation is claimed.

## Proof

### Imported source and required normalization

Import M. Vanlessen, *Strong asymptotics of Laguerre-type orthogonal
polynomials and applications in random matrix theory*,
[arXiv:math/0504604v2, 29 August2005](https://arxiv.org/pdf/math/0504604v2),
Theorem2.4(b), equation(2.13), Remarks2.5-2.7, and the bulk proof in
Section5.2, Proposition5.1/(5.5)-(5.6), with the uniform error supplied
by Theorem3.32. These primary statements and relevant proof were
inspected in review405/step406 and approved for this specialization by
review406/step407. No general asymptotic theorem is reproved here.
Use the [versioned HTML](https://arxiv.org/html/math/0504604v2) for its
numbered formulas as well. The theorem assumes alpha>-1 and a real
polynomial Q with positive leading coefficient; Q(t)=t, alpha=2 meet
these hypotheses.

The imported bulk expression for positive-leading orthonormal p_N has
prefactor t^(-1)exp(t/2)/sqrt(2pi N)*[x(1-x)]^(-1/4), x=t/(4N),
and two cosines with separately O(1/N) coefficients: the first is
cos(theta_N)(1+O(1/N)) and the second is cos(theta_N-2arccos(sqrt(x)))
O(1/N). This is an additive error assertion, including zeros of the
first cosine. The source's upper-side convention is essential.

For clarity, the source phase reduction is as follows. Its monomial
MRS formula, Remark3.5, gives beta_N=4N. Its (3.12),(3.18), with
m=1, A_0=1, give V_N(x)=4x and h_N(x)=4. Hence (2.8)/(3.23) give the
upper real value psi_N,+(x)=(2/pi)sqrt((1-x)/x). Substitution
s=cos^2(u) gives

    integral_1^x psi_N,+(s)ds
        =-(2/pi)[arccos(sqrt(x))-sqrt(x(1-x))].

Insert this in (2.13) and use arccos(2x-1)=2arccos(sqrt(x)) on (0,1)
to obtain (1)'s theta. The second source cosine differs by
arccos(2x-1), as stated above. The coefficient definitions just used
are part of the same source's scaling, not a new asymptotic input;
(3.18)/(3.23) were narrowly extracted during this specialization to
make the already assessed phase explicit.

Import [DLMF Table18.3.1](https://dlmf.nist.gov/18.3#T1), Laguerre row:
the squared norm at alpha=2 is (N+1)(N+2), and the leading coefficient
is (-1)^N/N!. Thus

    L_N^(2)(t)=(-1)^N sqrt((N+1)(N+2)) p_N(t).

This sign and norm, division by N and multiplication by exp(-t/2)
produce exactly a_N(t) in (1). Importing p_N as L_N^(2) would lose
both essential factors.

### Uniform domain and additive polynomial error

The union of the physical windows is contained in
[n,9(n+2)/4]. For n>=64 its rescaling lies in [1/5,3/5]: the lower
inequality follows from n/(4(n+1))>=1/5 for n>=4, and the upper from
9(n+2)/(16(n+1))<=3/5 for n>=14. Choose a sufficiently small FIXED
source bulk parameter delta so this entire compact interval lies in
the source bulk region. Real arguments use upper boundary values.
The source uniformity then supplies ONE onset n_0 and finite D,
independent of t,c,z, such that

    exp(-t/2)L_N^(2)(t)/N
         =(-1)^N a_N(t)[cos(theta_N(t))+r_N(t)],
    |r_N(t)|<=D/N.                                       (6)

Indeed each source cosine has modulus at most one on this real compact
interval, so the sum of the two absolute O(1/N) constants suffices for
D. The frequency z changes no Laguerre argument. It is unnecessary to
claim differentiability or analytic bounds for r_N. No division by a
cosine or polynomial is made.

### Explicit amplitude and phase bounds

On x in [1/5,3/5], x(1-x)>=4/25 and t=4Nx>=4N/5. Since
sqrt((N+1)(N+2))/N<=3 for N>=1, [x(1-x)]^(-1/4)<2 and
1/sqrt(2pi)<1, the explicit amplitude obeys

    0<a_N(t)<=8N^(-3/2).

Direct differentiation of the explicit formulas gives

    a_N'(t)/a_N(t)=-1/t-(1-2x)/(16N x(1-x)),
    theta_N'(t)=omega_N(t),
    omega_N'(t)=1/(16N x sqrt(x(1-x)))
                    +3(1-2x)/(64N^2[x(1-x)]^(3/2)).

Consequently

    |a_N'|<=16N^(-5/2), |omega_N'|<=2/N.                  (7)

For the first inequality, the absolute logarithmic derivative is at
most (5/4+25/64)/N<2/N. For the second, the first summand is at most
25/(32N); the absolute second summand is at most375/(512N^2), using
|1-2x|<=1. Their sum is <2/N for N>=1. These intentionally loose
bounds hold on the entire fixed compact interval, including every
window endpoint.

### Endpoint integration of the explicit leading expression

Let beta be either sign of3/8 and s either sign of1. Write
q(t)=lambda+is omega_N(t). Since omega_N is real,
Re(q)=beta-v and |beta-v|>=1/4 on Z. Thus |q|>=1/4 and

    |(a_N/q)'| <= 4|a_N'|+16a_N|omega_N'|
                                      <=320N^(-5/2).     (8)

All functions differentiated in (7)-(8) are explicit smooth functions
on the fixed real bulk, not the source remainder. The fundamental
theorem of calculus applied to a_N exp(lambda t+is theta_N)/q gives

    integral_a^b a_N(t)exp(lambda t+is theta_N(t))dt
       =[a_N(t)exp(lambda t+is theta_N(t))/q(t)]_a^b
          -integral_a^b exp(lambda t+is theta_N(t))(a_N/q)'dt.

Take the half-sum over s. Since |exp(is theta_N)|=1, the leading
cosine integral differs from P_beta(a,b;z) by at most
320N^(-5/2)J_beta(a,b;v). Equation(6)'s remainder integral is bounded
in absolute value by 8D N^(-5/2)J_beta(a,b;v). It receives no assumed
cancellation or derivative estimate.

Finally, expand cosh(3t/8)=(exp(3t/8)+exp(-3t/8))/2. The factor1/2
cancels k's -2. The polynomial's -1 contributes exactly S_beta/N
inside each window, with its sign as displayed in k_n^end. Its
exponent lambda-1/2 has real part beta-v-1/2<=-1/8, so its denominator
is nonzero. Apply the previous bounds separately to BOTH original
windows and BOTH beta terms, then multiply by exp(-cn/4). This proves
(3), with the signed endpoint expression and C=320+8D unchanged.
Only finite sums and finite interval integrals were used.

### Separate target/band envelopes and cap payment

For v=1/8 and t>=0,

    sum_beta exp((beta-v)t)=exp(t/4)+exp(-t/2)<=2exp(t/4).

The upper window has length2c, so its contribution to W is at most
4c exp(-cn/4+c(n+2)/4)=4c exp(c/2)<=9exp(9/8).
The lower window has length2 and contributes at most
4exp((1/4-c/4)n+1/2)<=4exp(1/2)exp(-3n/16).
This gives W_* without dropping the reflected beta term.

For v=0 the analogous inequality is sum_beta exp(beta t)<=2exp(3t/8).
The upper contribution is at most4c exp(cn/8+3c/4), maximized at9/4;
the lower one is at most4exp((3/8-c/4)n+3/4), maximized at7/4.
These are exactly W_E in(4). Every maximization includes the closed
endpoints. All dependence on Im(z) is retained first in(2), then
specialized to each permitted value in(4).

Apply(3) to the target and each band column. Finite summation and the
ORIGINAL complex norm sum|A_j|<=exp(sqrt(n)) give(5). Because the first
term in W_E is positive and dominates all other displayed terms, the
right side of(5), divided by exp(-n/64), has logarithm

    (9/32+1/64)n+sqrt(n)-(5/2)log N+log(9C exp(27/16))+o(1).

This proves the claimed19/64 comparison for the error ALLOWANCE. It
proves neither a positive lower bound for the true error nor failure
of the true capped E_n objective. A later cancellation construction
must pay its own complete error; this fixed-order additive expansion
alone does not do so. Growing truncation, differentiation of r_N,
and exponential accuracy are outside the approved specialization.

E_n, C997a's selected transfer, actual reconstruction, both-sign
transfer, complements/regulators, L993, L984(H), forcing and actual-Xi
positivity remain unresolved. Earlier scalar, norm, finite-generator
and pointwise spectral-envelope stops retain their original scopes.

### Independent conceptual audit — step410, 11 November 2026

RESEARCH / REPRODUCTION under the unchanged, separately approved
SPECIALIZE review408. The audit accepts exactly the stated existential
tail, closed frequency set, two windows and original coefficient cap.
It establishes reliability of a local known-theorem specialization, not
progress beyond the inspected sources or a proof of the E_n rate.

The primary contracts were checked against the cited versioned source:
Section1/(1.1)-(1.2), Theorem2.4(b)/(2.13), Remark2.5, (2.8),
Remarks3.5/3.7, (3.18)/(3.23), Theorem3.32/(3.110), and the bulk
proof (5.5)-(5.6). DLMF Table18.3.1 was checked for the norm and sign.
This is source-to-proof verification within the approved audit, not
a new literature assessment or a reproof of the asymptotic theorem.

1. **Normalization and phase.** At alpha=2 the norm squared is
   Gamma(N+3)/N!=(N+1)(N+2). Positive leading coefficient therefore
   gives the displayed factor (-1)^N sqrt((N+1)(N+2)). The source
   prefactor sqrt(2/(pi beta_N)), with beta_N=4N, becomes
   1/sqrt(2pi N); its spatial power is t^(-1). Division by N and
   multiplication by exp(-t/2) give a_N exactly. On the upper boundary,
   sqrt(x-1)=i sqrt(1-x), so (2.8) yields the POSITIVE density
   (2/pi)sqrt((1-x)/x). If u=arccos(sqrt(x)), substitution s=cos^2(v)
   gives integral_1^x psi_+(s)ds=-(2/pi)(u-sin(u)cos(u)). Thus the
   source's minus sign before that integral gives +2N(u-sqrt(x(1-x))).
   The two cosine phases are theta_N and theta_N-2u, with separate
   error coefficients. Both cosines are real and have absolute modulus <=1,
   including at every zero of the leading cosine. This validates (6)
   with one finite D, without a relative-error interpretation.

2. **Uniformity.** The minimum scaled argument is n/(4(n+1)); the
   maximum is 9(n+2)/(16(n+1)). The former is >=1/5 for n>=4 and
   the latter <=3/5 for n>=14. Both original windows and every one
   of their endpoints therefore lie in the fixed real bulk for n>=64.
   Choose one fixed source delta and increase the onset once. Neither
   c nor z changes that choice. Upper boundary values and source
   uniformity cover the real interval; no effective onset is inferred.

3. **Differentiation and constants.** Writing r=sqrt(x(1-x)), one has
   u_x=-1/(2r), r_x=(1-2x)/(2r), x_t=1/(4N). These identities give
   theta_N'=omega_N and both other derivatives in (7) with the stated
   signs. The amplitude bound uses 3*(5/4)*2=15/2<8. Its logarithmic
   derivative has modulus at most (5/4+25/64)/N=105/(64N)<2/N.
   The omega derivative bound uses
   25/(32N)+375/(512N^2)<=775/(512N)<2/N.
   Hence all bounds in (7) hold simultaneously, and (8)'s constant is
   exactly 4*16+16*8*2=320. Only explicit functions are differentiated.

4. **Denominators and endpoints.** As beta and v vary, beta-v is one
   of 3/8,-3/8,1/4,-1/2. Thus q=lambda+is omega_N and J's denominator
   have modulus at least 1/4, for both s and the entire CLOSED band.
   The real parts of lambda-1/2 are -1/8,-7/8,-1/4,-1, so S is also
   nonsingular. Since b>a and beta-v is real and nonzero, J is the
   positive integral of exp((beta-v)t). Direct differentiation of
   a_N exp(lambda t+is theta_N)/q gives the original leading integrand
   plus exp(lambda t+is theta_N)(a_N/q)'. Thus the displayed integration
   identity has the correct minus sign; the half-sum over s creates
   no extra factor in the absolute error. The polynomial error costs
   8D N^(-5/2)J, independently of the endpoint error.

5. **Complete kernel and cap.** In each window the exact integrand is
   exp(lambda t)[exp(-t/2)L_N^(2)(t)/N-exp(-t/2)/N]. Expansion of
   cosh cancels k's factor -2 against 1/2. The subtraction is therefore
   -S/N inside the braces, with upper window minus lower window and
   the common outer minus sign exactly as written. Applying the four
   absolute window/beta bounds gives C=320+8D in (3). For the target,
   the upper/lower exponential rates in W are 0 and at most -3n/16;
   for the real band they are at most 9n/32 and -n/16. The respective
   length factors and endpoint constants are precisely those in (4).
   Finite summation under sum|A_j|<=exp(sqrt(n)) proves (5) for every
   admissible complex vector, not merely a proposed optimizer.

Finally C>=320, so the leading positive term in the DISPLAYED allowance
really gives logarithmic rate 9/32+1/64=19/64 relative to exp(-n/64),
with the stated sqrt(n) and logarithmic terms. This verifies a limitation
of that allowance only. There is no lower bound here for the true
residual, no exclusion of cancellation and no conclusion about optimal
E_n. Source-error derivatives, growing-order control and effective
constants remain outside the result. The direct local mathematical
inputs remain C997c and C997s; earlier counterexamples are comparisons.
No additional DAG edge or new lemma is needed. All independent Xi,
arithmetic, reconstruction and transfer gaps listed above remain open.

## Mathlib

Full matching coverage for either the Vanlessen uniform bulk theorem
or this complete-kernel specialization has not been checked and is
unknown. DLMF normalization and the cited primary theorem are informal
external inputs. The explicit real differentiation, finite-window
fundamental theorem of calculus and absolute bounds above are the
specialization; no Mathlib theorem name or absence claim is asserted.
