# C750g: Actual-source pivot pilot and separate-channel payment failure

## Hypotheses

Use the complete EVEN matrix in bramble_trace, *Source-Gram control
and complete Weil positivity at radius 9/4*, rStation paper162, v1,
15 November 2026, [Section2(8)-(12)](https://rstation.ai/problems/riemann_hypothesis/papers/162).
Its matrix identity is the external input, not its fixed-window sign
theorem. Here P=101 and a=log(P)/2>9/4. No full-operator positivity
at this radius is assumed or concluded. The finite certificate below
certifies the particular positive cores needed for its inverse uses.

For exact reproducibility put gamma_0=1/sqrt(2), gamma_q=1 for q>0,
x_q=pi*q/a, c_l=2l+1/2, alpha=sinh(a/2)^2, and

    w_n=Lambda(n)/sqrt(n), phi_n=pi*log(n)/a,
    s_q=sum_(n<P) w_n*sin(q*phi_n),
    z_x=1/4+i*x/2,
    F(x)=x*Im psi(z_x)/2
         -sum_(l>=0) x^2*exp(-2a*c_l)/(c_l^2+x^2)
         -alpha/(1/4+x^2),
    R(x)=Im psi(z_x)/(4x)+Re psi'(z_x)/8
         -sum_(l>=0) c_l^2*exp(-2a*c_l)/(c_l^2+x^2)^2
         +alpha/(1/4+x^2)^2.                              (1)

At x=0 the first two terms of R together mean psi'(1/4)/4.
The entries are

    v_q=gamma_q,
    u_q=gamma_q*(2q*s_q/pi+2a*F(x_q)/pi^2),
    A_qr=(u_q*v_r-v_q*u_r)/(q^2-r^2), q!=r,
    A_qq=Re psi(z_(x_q))-log(pi)+(2/a)*gamma_q^2*R(x_q)
         -2 sum_(n<P) w_n*(1-log(n)/(2a))*cos(q*phi_n)
         +s_q/(pi*q), q>0.                               (2)

For q=0 omit the last term only. The 35 nonzero arithmetic terms are
the prime powers

    2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,
    37,41,43,47,49,53,59,61,64,67,71,73,79,81,83,89,97.

The n=101 endpoint has zero overlap and is not included. All continuous
responses and the even pole in(1) are retained. These are the Fourier
source conventions of the cited identity. No interpretation as
physical endpoint functionals is used.

Let M_j=(A_qr)_(0<=q,r<j), B_j have rows (u_q,v_q), and set

    m_j=(A_qj)_(q<j), b_j=(u_j,v_j)^T,
    G_j=B_j^T M_j^(-1) B_j,
    p_j=A_jj-m_j^T M_j^(-1)m_j,
    r_j=b_j-B_j^T M_j^(-1)m_j,
    E_j=r_j^T adj(G_j)r_j, H_j=101^2*(j+1)^5*p_j.         (3)

Inverse expressions are used only after the relevant positive core
has been certified. All objects in(1)-(3) are exact, not rounded
data. The computer-assisted assertions use MPFR4.2.2 with directed
rounding and the explicit analytic tails proved below; they assume
the installed MPFR and Python arithmetic implement their documented
semantics. Audit1138 below verifies the retained finite claims; it
does not remove these library assumptions.

## Conclusion

All leading cores M_k, 1<=k<=9, are positive definite. For every
j=2,...,8 the fixed pilot satisfies

    0<=E_j/H_j<3/5<1.                                   (4)

This is a finite passing pilot for assessment1135's proposed (H),
not its universal estimate for primes P>=101 and 2<=j<P.

There is also a specific informative failure. Split u in(2) into
its prime, digamma, exponential-response and pole contributions
u^(pr),u^(dg),u^(ex),u^(po), with their original signs. For
t_j=M_j^(-1)m_j define

    r_j^(h)=u_j^(h)-sum_(q<j)u_q^(h)*(t_j)_q,
    U_j=(sqrt(G_j,vv)*sum_h |r_j^(h)|
         +sqrt(G_j,uu)*|r_j,v|)^2.                       (5)

Then E_j<=U_j, but

    U_j/H_j>10^7 for every tested j,
    U_8/H_8>4*10^25.                                    (6)

Thus paying the four residual channels separately with this triangle
bound cannot prove even the passing pilot. This does not refute (H),
joint signed estimates, exact Schur complementation, positivity of
the complete form or RH. The obstruction concerns this precise
upper-budget mechanism. It is actual-source evidence beyond the
generic positive-displacement counterexample, not a claimed new
general theorem or certified originality. No growth law is inferred.

## Proof

### 1. Known Schur algebra and its exact specialization

Import Jean Gallier, *The Schur Complement and Symmetric Positive
Semidefinite (and Definite) Matrices*, 24 August2019,
[Section1, printed p2, and Proposition2.2, p4](https://www.cis.upenn.edu/~jean/schur-comp.pdf).
For the real block matrix M_(j+1)=[M_j,m_j;m_j^T,A_jj], positive
definiteness implies M_j>0 and p_j>0. Gallier's inverse formula is

    M_(j+1)^(-1)=
      [ M_j^(-1)+t_j*t_j^T/p_j, -t_j/p_j;
        -t_j^T/p_j,              1/p_j ].

Multiplying on both sides by the actual augmented source B_(j+1)
gives G_(j+1)=G_j+r_j*r_j^T/p_j. This uses the exact same u,v and
the last row b_j^T; no sign or spectral floor is inserted.
For G=[g,h;h,k] and r=(s,t)^T, direct expansion gives

    det(G+rr^T/p)
    =(g+s^2/p)*(k+t^2/p)-(h+st/p)^2
    =det(G)+(k*s^2-2h*s*t+g*t^2)/p.

The quartic terms cancel. Hence E_j/p_j is the determinant increment.
This is standard algebra, included to identify what the target would
control. Its reproduction is not the substantive result of this turn.
The initial determinant, later cores and complete covariance costs
are not controlled by(4).

### 2. Complete source enclosures

The reproducible implementation and full certificate are
[certify_1136.py](../scripts/pivot-area/certify_1136.py) and
[certificate-1136.json](../scripts/pivot-area/certificate-1136.json).
Run from this notebook:

    python3 scripts/pivot-area/certify_1136.py

The script uses MPFR at 384 bits through its C interface. Each
interval operation encloses its exact real result by RNDD/RNDU.
Products take extrema of all four endpoint products; reciprocals
reject intervals containing zero. Monotone elementary functions
use endpoint evaluation. For sine/cosine on [l,h], evaluate at the
exact binary endpoint l and widen by h-l: their derivative magnitude
is at most one. This avoids any assumption about monotonicity over
a phase interval. Printed certificate endpoints are rounded outwards
again to 105 decimal digits. Binary64 conversion is used only for
console display, never for a mathematical comparison. See the
[MPFR4.2.2 manual, Section4.4](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Rounding)
for the directed-rounding semantics. The ctypes layout and rounding
codes match the installed mpfr.h on this 64-bit platform.

For completeness, the special-function error budget is explicit.
Use [DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) with k=1,...,31
and [DLMF5.11(ii)](https://dlmf.nist.gov/5.11#ii)'s first-neglected-term
bound. At z=128+1/4+i*y write

    T(z)=log(z)-1/(2z)-sum_(k=1)^31 B_(2k)/(2k*z^(2k)),
    psi(z)=T(z)+epsilon(z).

Every point w of the closed radius-one disk about z satisfies
Re(w)>=127+1/4>127, |w|>127, |arg(w)|<pi/2. The principal log and
psi are holomorphic on a neighborhood of this disk. Consequently

    |epsilon(w)| <= (|B_64|/64)*127^(-64)*2^65 =: E_*.

Here sec(arg(w)/2)<2 supplies the deliberately loose sector factor.
Cauchy's derivative estimate on radius1 also gives
|epsilon'(z)|<=E_*. Thus T'(z)=1/z+1/(2z^2)+
sum_(k=1)^31 B_(2k)/z^(2k+1) approximates psi'(z) with that same
explicit bound. This is not differentiation of an unspecified error
term. Exact rational Bernoulli numbers are generated by
B_0=1 and B_m=-sum_(k<m)binom(m+1,k)B_k/(m+1).
The retained outward value satisfies E_*<3*10^(-79).

Translate back to 1/4+i*y using the finite recurrence
[DLMF5.5.2](https://dlmf.nist.gov/5.5.E2): subtract
sum_(h=0)^127(1/4+h+i*y)^(-1) for psi, and add the corresponding
squares of reciprocals for psi'. The latter also follows from
[DLMF5.15.5](https://dlmf.nist.gov/5.15.E5), n=1.
All recurrence denominators have positive real part. The logarithm
of z is evaluated as log(Re(z)^2+Im(z)^2)/2+i*atan(Im(z)/Re(z)),
valid because Re(z)>0. Both real and imaginary components are widened
by E_*. The exact x=0 limit in(1) is handled separately.

Retain l=0,...,31 in the exponential responses. Since the summands
are nonnegative before their minus sign, the remaining contribution
to F lies in [-delta_F,0], and that to R in [-delta_R,0], where

    c_32=129/2,
    delta_F=exp(-2a*c_32)/(1-exp(-4a)),
    delta_R=delta_F/c_32^2.                              (7)

These are paper162(12), or directly the geometric sum after bounding
x^2/(c_l^2+x^2)<=1 and c_l^2/(c_l^2+x^2)^2<=1/c_32^2.
At x=0 the F tail is exactly zero. The certificate checks
delta_F<6*10^(-130) and delta_R<2*10^(-133).
There is no unevaluated pole or prime tail: the prime-power list is
exhaustive and the pole is explicit. The low source rows and original
9-by-9 matrix, all four source channels, all tails and exact Bernoulli
fractions are retained in the JSON.

### 3. Positive-core certification and the finite test

The implementation constructs interval LDL^T factors recursively
from the original matrix enclosures, using

    d_k=A_kk-sum_(h<k)L_kh^2*d_h,
    L_ik=(A_ik-sum_(h<k)L_ih*L_kh*d_h)/d_k, i>k.

The diagonal of L is one. Inductively every computed interval
contains its corresponding exact factor, and every division is
made only after its divisor's lower bound is positive. The following
strict lower bounds on the nine exact pivots are checked:

| k | lower bound for d_k |
|---:|---:|
| 0 | 0.027 |
| 1 | 7.59e-7 |
| 2 | 5.84e-10 |
| 3 | 9.01e-13 |
| 4 | 4.21e-15 |
| 5 | 4.36e-17 |
| 6 | 5.32e-19 |
| 7 | 1.16e-20 |
| 8 | 4.40e-22 |

Positive exact LDL pivots prove each leading core positive by the
same block congruence as Gallier Proposition2.2. These are interval
enclosures of exact recursive pivots, not positive rounded point
pivots. No smallest-eigenvalue inference is made from their sizes.

Outward forward/diagonal/back substitutions enclose M_j^(-1)m_j
and both source solves. Every G entry, residual and p_j is then
enclosed by (3). The two computations of the symmetric off-diagonal
Gram entry are intersected, as are the direct Schur pivot and d_j;
each intersection contains the same exact number. The signed
quadratic E_j=G_vv*r_u^2-2G_uv*r_u*r_v+G_uu*r_v^2 is evaluated
before any magnitude bound. Since G_j is positive semidefinite,
its two-by-two adjugate is positive semidefinite, proving E_j>=0.

The complete endpoint computations, including all solves, are in
the certificate. Its `/claims` field checks these simpler strict
bounds against the full intervals, using no rounded display values:

| j | upper bound for E_j/H_j | lower bound for U_j/H_j |
|---:|---:|---:|
| 2 | 0.288210 | 1.38e7 |
| 3 | 0.433150 | 4.06e10 |
| 4 | 0.460314 | 6.02e13 |
| 5 | 0.439972 | 5.76e16 |
| 6 | 0.557627 | 6.40e19 |
| 7 | 0.599685 | 5.51e22 |
| 8 | 0.469076 | 4.00e25 |

All seven cases pass and the certificate has an empty failure list.
This proves(4) under the stated computation assumptions. It pays
exactly the finite pilot and does not certify M_10 or any other P.

### 4. Why separate-channel payment fails

The four pieces used in(5) are, in order,

    gamma_q*2q*s_q/pi,
    gamma_q*(2a/pi^2)*(x_q*Im psi(z_(x_q))/2),
    -gamma_q*(2a/pi^2)*sum_l x_q^2*exp(-2a*c_l)/(c_l^2+x_q^2),
    -gamma_q*(2a/pi^2)*alpha/(1/4+x_q^2).

Their sum is exactly u_q; the same tail enclosure(7) is attached
to the exponential piece. For the seminorm induced by adj(G_j),
the triangle inequality applied to
r_j=sum_h r_j^(h)*(1,0)^T+r_j,v*(0,1)^T gives sqrt(E_j)<=sqrt(U_j).
This uses ||(1,0)||=sqrt(G_vv) and ||(0,1)||=sqrt(G_uu), so it also
holds if G is singular. The square root and absolute value operations
are outward enclosed; the table's lower bounds for the exact U_j
therefore prove(6), rather than merely reporting a loose computed
upper endpoint. Any payment replacing each summand in(5) by a larger
independent upper bound is at least as costly.

The discrepancy involves actual cancellation across the full source.
At j=8 the prime, digamma, exponential and pole residuals have
respective approximate sizes +125880.7,-14807.5,+1373.0,-112446.2.
These rounded values only illustrate the cancellation; the proof
uses the complete signed enclosures. They are not a uniform
arithmetic suppression estimate. We obtained no such estimate from
the normal equations or the separated source representation.

The bounded attempt therefore parks the universal-envelope route
pending a materially new signed estimate. It rejects the specific
separate-channel triangle budget and preserves the passing pilot.
Neither more passing samples nor changing the coefficient/exponent
would repair the missing universal argument. C750c's scalar-floor
stop and C750f's fixed-domain import are contrasts, not inputs here.
The main L030-L032/C032a positivity gap, growing positive cores,
initial area, individual Gram-entry costs, complete middle/remainder
budgets, odd sector and actual-Xi realization remain open.

### 5. Finite-certificate audit1138

On16November2026 the approved audit1136/1137 checked every line of
the440-line implementation against(1)-(7). Paper162/v1 Section2
(8)-(12), including its exceptional zero mode, was retrieved again:
epsilon=+1, omega=0 gives exactly the retained matrix conventions.
The support cutoff is n<101, with all35 prime powers; no endpoint
term, continuous channel or pole was dropped. This imports the source
identity, not the source's fixed-window positivity theorem.

The analytic inclusion argument in Section2 survives: termination
at k=31 means first omitted index n=32, hence B_64/(64*z^64)
and sector exponent65 in DLMF5.11(ii). On every radius-one disk
about128+1/4+i*y the real part exceeds127, so the same bound applies
to the holomorphic remainder throughout the disk; Cauchy's estimate
bounds its derivative at the center by E_*. This works for every
real y in the input interval, rather than at one rounded center.
The finite recurrences subtract reciprocals for psi and add their
squares for psi'; their poles are avoided. The x=0 combined limit
and the one-sided exponential tails agree with the implementation.
All three claimed tail thresholds survive the unchanged replay.

The interval wrapper's endpoint operations, signs, integer powers,
reciprocals, monotone evaluations, Lipschitz trigonometric widening
and decimal serialization were checked. The C declarations in the
installed mpfr.h agree with the ctypes signatures used for their
arguments and used return values. An independently compiled header
probe gives struct size32, precision/exponent/limb sizes8, offsets
0,8,16,24 and rounding codes RNDD=3,RNDU=2, exactly as the wrapper.
No binary64 display value enters an inequality. Installed MPFR4.2.2
and Python/Decimal correctness remain explicit assumptions.

Run the retained audit from this notebook:

    python3 scripts/pivot-area/audit_1138.py

It executes identical original script bytes in a temporary directory,
retains the complete output in scripts/pivot-area/replay-1138.json,
and verifies equality with every field of certificate-1136.json.
The original certificate and script remain unchanged. The audit
then uses a separate110-digit directed Decimal interval implementation
to reconstruct all off-diagonals from the serialized source rows,
factor the nine-mode matrix, and recompute every required solve,
Gram entry, signed residual, pivot, E,H,U and ratio. Exact decimal
endpoints are loaded without binary64 conversion. Square-root results
are widened to adjacent decimal endpoints; exact Fraction arithmetic
then checks that the lower square is at most the input lower endpoint
and the upper square is at least the input upper endpoint. This
certifies their inclusion without relying solely on square-root
rounding. All other audit arithmetic uses explicit floor/ceiling
contexts; see the [Python3.15 Decimal/Context reference](https://docs.python.org/3.15/library/decimal.html#context-objects).

Only enclosures of the same exact entry are intersected. Positive
lower pivots precede divisions in the new factorization; positive
Gram diagonals precede square roots. Induction through the displayed
LDL and substitution recurrences proves these fresh intervals contain
the exact factors and solves. Their input inclusion rests on the
source/analytic code audit above. Overlap checks consume every
original solve, Gram entry, channel residual and test quantity, but
overlap by itself is only a consistency check and is not used as
a proof of inclusion. The fresh intervals independently satisfy
all nine pivot lower bounds and all seven ratio bounds in Section3.
The complete110-digit evidence is scripts/pivot-area/audit-1138.json;
both replay and audit have empty failure lists.

In particular the largest E/H in this pilot has j=7 and lies between
0.59968467885455 and0.59968467885456, below3/5. The j=8 U/H lower
endpoint exceeds40001796840929838382036213, hence exceeds4*10^25.
The last pivot exceeds4.4085654128370*10^(-22). These outward
weakenings summarize the full endpoints, not rounded sign tests.
The exact separate-channel budget, rather than an oversized interval
upper endpoint, therefore fails the proposed payment. The PSD
adjugate/seminorm proof gives E>=0 and E<=U without assuming a
positive determinant of G. The audit validates(4) and(6) only at
the stated finite scope; no uniform suppression or other main-gap
input has been established.

## Mathlib

Full matching Mathlib coverage of this source matrix, finite numerical
pilot and four-channel failure was not checked. Schur inversion,
positive congruences, Cauchy's derivative estimate and elementary
interval arithmetic are standard supporting mathematics; no exact
Mathlib theorem name or Lean verification is asserted. Unknown
coverage is not evidence of absence. The source formulas and scalar
estimates above are imported by precise primary citations, while the
finite bounds are a local computation under assessment1135, without
a claim of originality beyond the sources checked.
