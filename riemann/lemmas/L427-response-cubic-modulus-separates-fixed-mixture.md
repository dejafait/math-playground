# Lemma 427: the cubic response-modulus weight separates the fixed mixture

## Hypotheses

Use the actual ordinary order-zero critical function f=F_0/A of
L389 (3), Z(t)=zeta(5/2+it), W(t)=|Z(t)|^2, ell=log H, and
E=H^(-1) integral_[H,2H], for real H tending to infinity. For the
comparison use exactly L423's law nu_H: its fixed g0 and alpha in
(5), actual response, uniform height marginal, unchanged high and
intermediate components, and full bulk correction (9)--(10).
The variable x is the first critical coordinate of that law.
No retuning, growing parameter, conditional independence or realization
by a global critical function is assumed. Use

    C_j=sum_(n>=1) d_j(n)^2 n^-5,
    S=zeta(5)zeta(3)^2/zeta(6), R_k=C_(k+1)/C_k,
    theta_k=(S-C_1)/(R_k-C_1),
    B_k=C_2+theta_k(C_(k+2)/C_k-C_2),
    T_2=sum_(m,n>=1) d_2(m)d_2(n)gcd(m,n)/(m^3 n^3),
    alpha=(B_14-T_2)/(B_14-B_13).

These constants are the unchanged constants of L419/L422/L423.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-response-cubic-modulus-second-moment.md`.

## Conclusion

The actual sharp mean and the complete comparison-law mean satisfy

    E[W^3 f^2]=T_3 ell+o(ell),
    T_3=sum_(m,n>=1) d_3(m)d_3(n)gcd(m,n)/(m^3 n^3),       (1)
    E_nu[W^3 x^2]=D_mix ell+O(sqrt(ell)),
    D_k=C_3+theta_k(C_(k+3)/C_k-C_3),
    D_mix=D_14+alpha(D_13-D_14),                          (2)
    T_3-D_mix>7/1000.                                    (3)

Thus this specified fixed mixture cannot also match the leading
coefficient of the additional correlation (1). The separate step-203
critical audit below validates this local diagnostic. It reproduces known moment tools;
it is not a new general zeta moment theorem or a claim of originality.
L421/L423 remain valid on their original selected lists. Other
covariance weights, actual clipping, global function realization,
L413's full-error regulator margin, global mixed positivity and RH
remain unresolved. No new actual-theta sign or zero-exclusion range
is asserted.

## Proof

### Known moment input and full-response sharp passage

Import M. P. Young, *A short proof of Levinson's theorem*, Arch.
Math. 95 (2010), 539--548, DOI 10.1007/s00013-010-0199-9,
[Lemmas 4--5, (4.1)--(4.5), pp. 542--543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
in the audited order-zero specialization L381 (7). With U(t)=
zeta(1/2+it), fixed positive m,n and fixed-shape smooth 0<=w<=1
supported in [H/2,3H], it gives

    integral w(t)(m/n)^(-it)|U(t)|^2 dt
      =gcd(m,n)/sqrt(mn) integral w log(t/(2pi)) dt
         +O_(m,n,w)(H).                                 (4)

At the source scale 2H this support lies in [H/2,4H], derivatives
O_j(H^-j) meet its weaker (H/log H) scale, and fixed mn eventually
satisfies mn<=(2H)^(2vartheta) for any fixed 0<vartheta<1/2.
As in L381, the two functional-equation diagonals are combined
holomorphically before taking zero shifts. This imports that theorem
and specialization; no reproof or higher moment is needed.

L389 (3) gives f^2=|U|^2 also at zeros. Absolute Dirichlet
multiplication on Re s=5/2 gives Z^3=sum d_3(n)n^(-5/2-it).
Put V_N=sum_(n<=N)d_3(n)n^(-5/2-it). Expansion of its entire
modulus square in (4) gives

    integral w |U V_N|^2
      =T_(3,N) integral w log(t/(2pi))dt+O_(N,w)(H),
    T_(3,N)=sum_(m,n<=N)d_3(m)d_3(n)gcd(m,n)/(m^3 n^3).

Every rational twist and gcd collision is retained. For fixed
epsilon in (0,1/4), bracket the whole nonnegative |U V_N|^2
by smooth minorants and majorants of [H,2H], with transition strips
of length epsilon H at both endpoints and integrals H+O(epsilon H).
Their supports fit (4), and log(t/(2pi))=ell+O(1) there.
First take H to infinity at fixed N,epsilon, and then epsilon to
zero. Thus E|U V_N|^2/ell tends to T_(3,N).

Writing M=zeta(5/2), absolute multiplication also gives

    delta_N=sum_(n>N)d_3(n)n^-5/2 ->0,
    sup|Z^3-V_N|<=delta_N, sup(|Z^3|+|V_N|)<=2M^3.

L381 (9) therefore bounds the sharp difference by

    |E|UZ^3|^2-E|UV_N|^2|<=2M^3 delta_N E|U|^2
                           =O(delta_N ell),             (5)

with constant independent of N. Since gcd(m,n)<=sqrt(mn), the
positive double sum in (1) is at most M^6. Hence T_(3,N) increases
to T_3. The limsup of the normalized error from T_3 is at most
C delta_N+|T_3-T_(3,N)| for every fixed N, and tends to zero.
This proves (1) without a growing head or an interchange of
uncontrolled limits.

### All three law components

Here W^3<=M^6 is bounded independently of H. L421 (4),(6)
give unnormalized high and intermediate second integrals O(ell^-2)
and O(sqrt(ell)). Weighting them by W^3 preserves these bounds.
They are not conditional moments divided by rare probability.

For the bulk retain its fiber mass w, bounded mean m, and entire
Sigma=ell g_H K+A_H, with K_11=1 and ||A_H||=O(sqrt(ell)).
Its raw first-coordinate second contribution is exactly

    E[w W^3(Sigma_11+m_1^2)]
      =ell E[w g_H W^3]+O(sqrt(ell)).

L423 (9) applies to the bounded response expression W^3, giving
E[w g_H W^3]=E[g0 W^3]+O(H^-1+ell^-5/2). The resulting
error multiplied by ell is o(1). For each fixed k=13,14,
L419 (3), at powers 3 and k+3, gives

    E[g_k W^3]=(1-theta_k)C_3+theta_k C_(k+3)/C_k
                  +O(H^-1)=D_k+O(H^-1).

The unchanged g0=alpha g_13+(1-alpha)g_14 then proves (2).
The mean square and full covariance correction are retained;
the constants and one eventual onset may depend on this fixed
mixture. No source moment theorem is applied to artificial states.

### The order-three local factor and omitted primes

Positive multiplicative expansion of the convergent double sum gives
T_3=product_p T_(3,p). Put u=p^-3, v=p^-5, and d(e)=
binom(e+2,2). Separate equal exponents e from positive excess r
in either direction. As
d(e+r)=d(e)+(2e+3)r/2+r^2/2, geometric differentiation gives

    A(v)=sum d(e)^2 v^e=(1+4v+v^2)/(1-v)^5,
    B(v)=sum d(e)(2e+3)v^e=3(1+v)/(1-v)^4,
    C(v)=sum d(e)v^e=(1-v)^-3,
    T_(3,p)=A(v)(1+u)/(1-u)
             +B(v)u/(1-u)^2+C(v)u(1+u)/(1-u)^3.          (6)

For example B=2v C'+3C. The formula for A follows by expanding
d(e)^2=(e^4+6e^3+13e^2+12e+4)/4 and applying powers of
v d/dv to (1-v)^-1. All these series converge absolutely.
This is the changed local factor; L422's order-two factor is used
only for T_2 in alpha.

To bound omitted primes, d(e+r)<=d(e)d(r): adding two weak
three-part compositions of totals e,r maps onto all compositions
of total e+r (split any such composition greedily at total e).
Consequently

    T_(3,p)<=A(v)[2(1-u)^-3-1]
            <=(1-v)^-9(1-u)^-6.                         (7)

Indeed 1+4v+v^2<=(1-v)^-4 coefficientwise, proving the
first factor bound; 2q-1<=q^2 at q=(1-u)^-3 proves the second.
Using -log(1-z)<=z/(1-z) and replacing primes above P by all
integers above P bounds the omitted logarithmic product by

    r_T3=3/[P^2(1-(P+1)^-3)]
             +9/[4P^4(1-(P+1)^-5)].                    (8)

For T_2 reuse L422 (8),(12), whose logarithmic tail is
2/[P^2(1-(P+1)^-3)]+1/[P^4(1-(P+1)^-5)]. For C_j use
its factor sum_(e>=0)binom(j+e-1,e)^2 p^-5e, truncated at
e=E (retaining e=0,...,E). The successive ratio is decreasing; with
r=((j+E)/(E+1))^2 p^-5<1 the local remainder lies in
[0,t_E r/(1-r)]. Its omitted-prime logarithmic bound is

    r_C(j)=j^2/[4P^4(1-j^2(P+1)^-5)],                   (9)

using binom(j+e-1,e)<=j^e. For zeta(s), s=3,5,6, the
corresponding bound is
1/[(s-1)P^(s-1)(1-(P+1)^-s)]. All these r lie in (0,1)
at the cutoffs used. An omitted product is in [1,1/(1-r)],
since its log is at most r and exp(r)<=1/(1-r).

### Rational comparison, failures and implementation contract

The generator is
`scripts/discriminant/check_response_cubic_modulus_second_moment.py`.
It reuses only the inspected exact Fraction interval primitives and
prime sieve of L422's audited generator. It computes C_j for
j=1,2,3,13,14,15,16,17, S, T_2, T_3, both theta values,
B_13,B_14,D_13,D_14, the exact defining alpha and D_mix.
It rounds each interval arithmetic operation outward to multiples
of 10^-18; division requires a strictly positive denominator interval.
The bounds (6)--(9), not decimal previews, justify the calculations.

The first P=200,E=40 run did not certify a gap. At the single
allowed refinement P=1000,E=80, separately boxing alpha and
1-alpha still gave an overlapping enclosure. The exact identity
D_mix=D_14+alpha(D_13-D_14) preserves this shared dependence
and yields the following strict separation at the same refinement.
The final certificate retains the overlapping independent-box
enclosure; neither failed enclosure was treated as nonseparation.

Reproduction command:

    python3 scripts/discriminant/check_response_cubic_modulus_second_moment.py --cutoff 1000 --order 80

Full certificate:
`scripts/discriminant/response-cubic-modulus-second-moment-1000-80.json`.
Its complete `/bounds`, `/checks`, `/log_tail_upper_bounds` and
`/failures` fields were inspected. All seven comparisons pass;
the failure list is empty. In exact rationals it proves

    T_3 >= 3474983372117534637/10^18,
    D_mix <= 3467058691456416067/10^18,
    T_3-D_mix >= 792468066111857/10^17 > 7/1000.          (10)

The saved alpha interval is
[106536606546744291/250000000000000000,
 107141551773819101/250000000000000000], contained in (0,1).
Thus no independent fitted alpha is substituted. The finite factors,
local remainders and omitted-prime bounds for every required power
are saved in full. This is an exact-arithmetic computational proof
under correct execution of the displayed generator and Python's
integer/Fraction operations; the independent step-203 audit below
checks it, but it is not formally verified. The analytic bounds above
specify its contracts. Equations (1),(2),(10) prove the stated
asymptotic diagnostic under these implementation contracts.

### Separate critical audit — 2026-10-17, step 203

This RESEARCH / REPRODUCTION / proof_audit uses the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-17-response-cubic-modulus-audit.md`.
Equations (1)--(10) pass within their stated scope; no mathematical
repair is needed. This validates an existing local necessary-condition
test, not new mathematics beyond the checked sources or an RH result.

**The imported moment and sharp full tail.** L389's phase comparison
never divides by the critical zeta value, so f^2=|U|^2 includes zeros.
Young's precisely cited theorem is reused through audited L381 (7):
the fixed weights fit the support and derivative conditions at scale
2H, every fixed twist meets the length restriction eventually, and
both diagonals are combined before zero shifts. Multiplying the
coefficient gcd(m,n)/sqrt(mn) by the two coefficients of Z^3 gives
exactly d_3(m)d_3(n)gcd(m,n)/(m^3 n^3). Reducing a twist does not
remove any of its occurrences in the finite double sum. There is
no gamma carrier in the weight and no critical derivative here.

For fixed N and epsilon, both smooth brackets are applied to the
whole nonnegative |UV_N|^2, not to its individual complex twists.
After division by H ell the error is O_(N,epsilon)(1/ell), and the
bracket integrals divided by H are 1+O(epsilon). This proves the
sharp fixed-N limit by taking H first and epsilon second. For the
last limit, | |Z^3|^2-|V_N|^2 |<=2M^3 delta_N pointwise, and
L381 (9) bounds E|U|^2/ell uniformly in H. The entire positive
double sum is bounded by M^6. Hence the limsup error from T_3 is
at most C delta_N+|T_3-T_(3,N)|, which tends to zero. This proves
the full sharp limit for all sufficiently large real heights without
any N(H), uniform finite-twist error or independence assumption.

**The complete law.** The imported L421 high and intermediate
second integrals are respectively O(ell^-2) and O(sqrt(ell)), with
their probabilities included. The bound W^3<=M^6 preserves these
orders. The bulk has raw second entry Sigma_11+m_1^2, fiber mass
w, K_11=1, bounded m and the full O(sqrt(ell)) matrix A_H. Thus
its leading term is ell E(w g_H W^3) with error O(sqrt(ell)).
L423 (9) applies to this bounded response expression even on fibers
where the high probability is not small: its integrated error times
ell is O(ell/H+ell^-3/2)=o(1). L419 (3) uses the absolutely
convergent fixed powers 3,16,17, with their full O(H^-1) errors.
The mixture parameter is exactly L423 (5), still defined by T_2,
and not fitted to T_3. These observations verify (2) with one onset
for the fixed law, including all three components and the full mean
and covariance correction. No moment theorem is imposed on artificial
states and no stronger O(1) correction is claimed.

**Local factors and analytic tails.** With e the common minimum
exponent and r the positive excess, the double-sum weight is v^e u^r.
The diagonal contributes d(e)^2 and the two excess directions together
contribute 2d(e)d(e+r). Expanding d(e+r) yields exactly (6);
in particular B=2v C'+3C=3(1+v)/(1-v)^4. Independently, multiplying
the coefficient series by (1-v)^5(1-u)^3 gives numerator

    (1+3u-3u^2+u^3)
      +v(4-6u-6u^2+4u^3)+v^2(1-3u+3u^2+u^3).

This equals (6)'s numerator. The coefficient polynomial has degree
four in e and degree two in r>0; the special r=0 term is retained.
Finite differences therefore prove the numerator terminates, rather
than merely testing a finite power-series prefix. The analogous
order-two numerator is 1+2u-u^2+v(1-2u-u^2), agreeing with L422 (8).

The composition map in (7) is surjective: split any weak three-part
composition of total e+r into a component of total e and the
nonnegative remainder of total r. It proves d(e+r)<=d(e)d(r).
The coefficient comparison 1+4v+v^2<=(1-v)^-4 and
2q-1<=q^2 establish the stated T_3 bound. For T_2, the inherited
bound follows from D=(1+v)/(1-v)^3<=(1-v)^-4 and
(1+2u-u^2)(1-u)^2<=1 for 0<=u<=1. In both cases summing
the logarithmic bounds over all integers above P gives (8) and
the stated T_2 tail. For C_j, the ratio (j+e)/(e+1) decreases
(is constant for j=1), and binom(j+e-1,e)<=j^e. These prove
both its local geometric remainder and (9). The zeta tails use
the same integral comparison. All tail denominators are positive;
each logarithmic upper bound r is in (0,1), where
r<=-log(1-r) justifies exp(r)<=1/(1-r). Thus every omitted
product has a valid rational enclosure, including the powers through 17.

**Independent exact certificate check.** Reproduce with

    python3 scripts/discriminant/audit_response_cubic_modulus_second_moment.py

The verifier imports neither generator nor their interval primitives.
It obtains the complete prime lists by trial division, each C_j local
sum by direct binomial coefficients, and both T local factors from
the finite-difference numerators just described. It recomputes every
local remainder, omitted-prime logarithmic bound, zeta product,
positive denominator and global interval with independently implemented
outward rational rounding. Products check all four endpoint corners;
division requires a strictly positive lower denominator. It compares
every saved rational endpoint, not decimal previews or only booleans.

Its complete record is
`scripts/discriminant/response-cubic-modulus-second-moment-audit-203.json`.
At P=1000,E=80 it verifies all 1344 C local factors, 336 T local
factors, 13 logarithmic tails, all derived bounds and all seven checks.
The full certificate fields are processed without truncation. At the
historical P=200,E=40 it additionally verifies 368 C factors and 92 T
factors, all tails and the original failed enclosure. That older file
uses independent alpha boxes and the failed test named
`gap_exceeds_1_over_100000`; it predates the final generator's correlated
expression and 7/1000 test. It is preserved and verified in that form,
not overwritten by rerunning a later generator. At P=1000 the saved
independent box likewise overlaps the actual interval. These failures
remain failures of enclosures, not evidence of equality.

The final correlated identity uses D_13-D_14<0 with the exact
W^2-defined alpha. All dependencies are enclosed even though interval
reuse still loses some correlation; it can only widen the bound.
The independent exact interval for the actual-minus-law difference is

    [792468066111857/10^17, 3995833056072847/(5*10^17)].

Its lower endpoint exceeds 7/1000 by 92468066111857/10^17.
The opposite saved interval is law-minus-actual, so its upper endpoint
must be negative; the orientations agree. The audit has 13546 passing
field comparisons and no failures. Python integer/Fraction execution
remains an implementation contract, not a formal proof assistant check.
The original source files and both historical certificates are unchanged.

This validates only the exclusion of this extra leading correlation for
the unchanged law. L423's selected constraints, alternative covariance
weights, actual clipping, global realization and the full regulator
margin retain exactly their prior qualifications. The main positivity
gap is unchanged, so the argument assembly and direct DAG inputs do
not change.

## Mathlib

Full matching coverage for this actual-response coefficient and
fixed-law comparison has not been checked; no absence is asserted.
Young's theorem is imported by the precise citation above. The
elementary Euler-factor specialization and rational comparison are
written out here. Supporting results do not constitute a Lean
verification of the complete argument.
