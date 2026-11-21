# Corollary 999e: the prescribed finite target-Radau test fails its penalty screen

## Hypotheses

Use C997c's COMPLETE kernel and C997s's original complex cap:

    k_n(c,z)=-2 exp(-cn/4) [int_(cn)^(c(n+2)) g_n(t) exp(izt)dt
                                  -int_n^(n+2) g_n(t) exp(izt)dt],
    g_n(t)=P_n(t) exp(-t/2) cosh(3t/8),
    P_n(t)=(L_(n+1)^(2)(t)-1)/(n+1).

Here n=64 or 128, I=[7/4,9/4] with ordinary Lebesgue measure,
z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n,
t(c)=k_n(c,z_star), b_j(c)=k_n(c,gamma_j), B=exp(sqrt(n)).
Use inner product <f,g>=int_I conjugate(f)g and define

    G_ij=<b_i,b_j>, h_i=<b_i,t>, d=<t,t>, lambda=exp(-n/16),
    H=G+lambda Id,
    F=d-h^*H^(-1)h-lambda B^2,
    E=inf_(sum |A_j|<=B) ||t-sum A_j b_j||_C(I).

Every column is included in these definitions, although no entry of G
or h is numerically evaluated below. No actual-Xi, nonvanishing,
simplicity, spectral-support or positivity hypothesis is assumed.

## Conclusion

The exact continuum target norms and original penalties satisfy

| n | rigorous d upper bound | rigorous lambda B^2 lower bound | rigorous F upper bound |
|---|---|---|---|
| 64 | 1.323e-6 | 162754 | -162754 |
| 128 | 1.683e-7 | 2252197 | -2252197 |

All inequalities in this table are strict. The F column is checked
against the complete certificate, not obtained by subtracting the
coarsened second and third columns of the table.

Thus neither prescribed finite degree can give F>0, even with an exact
inverse form. The approved at-most-eight-step Gauss/left-Radau attempt
is parked at this necessary-condition screen, using ZERO Lanczos steps.
No Gauss/Radau enclosure, cyclic-compression specialization or inverse
form was constructed or claimed. The scalar screen's arithmetic width
is less than 2^-60; the d, lambda and B widths are less than 2^-256.

Step414, 11 November 2026: RESEARCH / REPRODUCTION, outcome NEGATIVE,
under pre-existing SPECIALIZE review412. This is a local finite
obstruction, not a discovery beyond the checked general sources.
Independent critical audit was pending at step414; step416 below accepts
the complete finite integration and stated bounds. This gives no upper
bound on E, no unbounded-n rate and no RH candidate. Negative F makes
the lower certificate below vacuous.

## Proof

### Known quadratic input and the stopping inequality

Use the standard finite-dimensional spectral theorem and the normal-
equation/minimizer theorem of Christian Clason, *Regularization of
Inverse Problems*, arXiv:2001.00617v2 (8 February 2021), Lemma6.3 and
Theorem6.5, printed pp59-62,
[primary PDF](https://arxiv.org/pdf/2001.00617v2#page=62).
The generic minimization theorem is imported, not reproved.

Define T:C^(n+1)->L2(I,C) by TA=sum A_j b_j. Continuity of the
complete kernel on the compact interval makes each column square
integrable. Cauchy-Schwarz gives
||TA||_2<=(sum ||b_j||_2^2)^(1/2)||A||_2, so T is bounded and compact
because its domain is finite dimensional. Its adjoint convention gives
T*T=G and T*t=h. These verify the source's Hilbert-space assumptions
for arbitrary target t, including components outside the column range.

For completeness, realification uses A=x+iy -> (x,y), preserving
squared norm sum(x_j^2+y_j^2) exactly. A Hermitian matrix G becomes
[[Re G,-Im G],[Im G,Re G]], and the real pairing is Re(A*G A).
There is no factor two and no replacement of sum|A_j| by a different
cap. Directly, A*G A=||TA||_2^2>=0; hence H>=lambda Id>0.
The spectral theorem gives H^(-1)>0, including all repeated-eigenvalue
and nullspace cases. If h=0 its inverse form is zero; otherwise it is
strictly positive. No Lanczos normalization or division is used.
Consequently, in every case,

    F <= d-lambda B^2.                                    (1)

Clason's minimizer is A_lambda=H^(-1)h. Substitution in the quadratic
functional gives min_A (||t-TA||_2^2+lambda||A||_2^2)
=d-h*H^(-1)h. For any ORIGINAL cap-feasible A,
||A||_2<=sum|A_j|<=B. Therefore ||t-TA||_2^2>=F.
Since |I|=1/2, ||t-TA||_C(I)^2>=2||t-TA||_2^2. Taking the
infimum yields E^2>=max{0,2F}. This checks the cap relaxation,
penalty sign and L2-to-sup conversion without claiming useful positivity.
A negative upper bound in (1) settles the stated finite sign test;
it does not require the separate cyclic-compression and quadrature
applicability arguments that would be necessary to use numerical
Gauss/Radau signs. Those arguments were not executed here.

### Exact complete target products

The defining polynomial coefficients, as in C997s(2), are

    p_j=(-1)^j binomial(n+3,n+1-j)/(j!(n+1)), 0<=j<=n+1,

with 1/(n+1) subtracted from p_0. At z_star the two exponents after
expanding cosh are a=-1/4+i and a=-1+i. For each a set q_(n+2)=0
and q_j=(p_j-(j+1)q_(j+1))/a, downward. Then Q_a(t)=sum q_j t^j
satisfies Q_a'+a Q_a=P_n coefficient by coefficient. Thus
Phi_a(t)=exp(at)Q_a(t) is an exact primitive.

Put L=sum_a (Phi_a(n+2)-Phi_a(n)). The exact target is the sum of
FIVE terms P_l(c)exp(alpha_l c): for each a take

    P_(a,n)(c)=Q_a(nc),       alpha_(a,n)=a n-n/4,
    P_(a,n+2)(c)=-Q_a((n+2)c),alpha_(a,n+2)=a(n+2)-n/4,

and take the fifth term P_4(c)=L, alpha_4=-n/4. This identity retains
both beta terms, the moving window, the lower window, K's -1 and both
endpoints; it follows by substitution in the complete kernel, with no
asymptotic or numerical quadrature approximation.

Multiply these finite expressions BEFORE integrating in c. If
P_l(c)=sum_j u_(l,j)c^j, then the product for indices l,m has
coefficients sum_(j+k=r) conjugate(u_(l,j))u_(m,k) and exponent
alpha=conjugate(alpha_l)+alpha_m. Conjugation acts on coefficients
and exponents; c is real. Set a0=7/4, b=9/4. Its exact moments are

    M_0(alpha)=(exp(alpha b)-exp(alpha a0))/alpha,
    M_r(alpha)=(b^r exp(alpha b)-a0^r exp(alpha a0)
                                          -r M_(r-1)(alpha))/alpha.

These follow by evaluating the primitive for r=0 and integration by
parts for r>=1. All actual Re alpha_l<=-n/4, so Re alpha<=-n/2<0:
every division here excludes zero. The code also handles alpha=0
by the exact polynomial integral (b^(r+1)-a0^(r+1))/(r+1);
that branch is not invoked at either degree.

The norm d is the sum of the five diagonal product integrals plus
twice the REAL PART of the ten off-diagonal integrals. This uses
int conjugate(f_m) f_l=conjugate(int conjugate(f_l) f_m), valid for
these continuous functions. Hence fifteen complete product integrals
suffice. No infinite interchange, sign assumption on P_n or sampled
slope value is involved.

### Directed arithmetic and complete evidence

Run from the notebook:

    python3 scripts/target-radau/finite-penalty-screen-414.py
    python3 scripts/target-radau/check-penalty-screen-414.py

The first script reuses C997s's primitive-coefficient and rectangle
operations from `scripts/adaptive-slope/direct-kernel-atomic-371.py`,
with one FIXED precision of 660 decimal digits (>2048 bits), and the
following new exponential truncation. After repeated halving ensures
|z|_1<=1/8, sum through degree256. The remaining modulus is bounded by
2/(8^257*257!), because the subsequent absolute-term ratios are at
most 1/8. Enlarge both coordinates by the outward upper bound of this
number and square back. All finite coefficient operations, products,
recurrences and endpoint evaluations use directed Decimal contexts.
Each real multiplication takes the extrema of all four endpoint
products; division rejects a denominator containing zero. Complex
division encloses (x+iy)/(u+iv) using u^2+v^2 and that same guard.
Thus cancellation is enclosed, including cancellation between large
product integrals. No empirical precision agreement is used.

For B, compute r=floor(2^2048 sqrt(n)) by exact integer square root.
The rational interval [r/2^2048,(r+1)/2^2048] encloses sqrt(n);
applying the exponential enclosure and then the positive interval
product lambda B B encloses the ORIGINAL penalty. Lambda uses the
same exponential algorithm at the exact rational -n/16.

Full certificates, including all five target terms, all fifteen product
coefficient lists and moment lists, all product integrals and scalar
intervals, are `scripts/target-radau/finite-penalty-screen-64-414.json`
and `scripts/target-radau/finite-penalty-screen-128-414.json`.
The complete /d, /screen_d_minus_penalty and /checks values were inspected
with `python3 ../scripts/loop/inspect_json.py <certificate> --pointer
<field> --full`. The upper endpoint of the latter interval is a valid
upper bound for F by (1), not a two-sided enclosure of F.

Actual d widths are <3.7760e-600 and <4.0088e-541, respectively;
the required bound is 2^-256>8.6361e-78. Actual screen widths are
<3.7760e-600 and <4.0088e-541, respectively; the required bound is
2^-60>8.6736e-19. Lambda and B also meet the entry-width bound.
The scalar screens are approximately -162754.791417681 and
-2252197.576013362; their complete certified upper endpoints imply
the strict F bounds stated above. No quadrature gap has been discarded:
no quadrature endpoint was computed, so its 2^-64 width condition is
inapplicable to this early-stop certificate.

The second script reads the COMPLETE saved interval data and uses exact
rational arithmetic to check product aggregation, penalty multiplication,
subtraction directions, all width thresholds and the strict safe table
bounds. It checks all fifteen product indices and exponent cases and
that each diagonal imaginary interval contains zero. All 17 checks per
degree pass; no failures. Its full certificate is
`scripts/target-radau/check-penalty-screen-414.json`. This is a terminal
aggregation check, not an independent recomputation of the exponential
or polynomial primitives. The separate critical implementation audit
required at step414 is completed below.

### Independent complete arithmetic and proof audit — step416

11 November2026: RESEARCH / REPRODUCTION / proof_audit under unchanged,
separately approved SPECIALIZE review414. The verdict is ACCEPT on the
stated finite scope, with no mathematical correction. This closes a local
verification gap, not a gap in RH or a result beyond the checked sources.

The audit reads the complete original evidence and reimplements the
calculation in `scripts/target-radau/audit-penalty-screen-416.py`, importing
neither the step414 generator nor any step371 arithmetic. Its real
interval endpoints are integers divided by S=2^4096. Addition and negation
are exact; products take all four endpoint products and round the minimum
down and maximum up after division by S. For a divisor [l/S,h/S]
excluding zero, the reciprocal endpoints are floor(S^2/h)/S and
ceil(S^2/l)/S. This applies also to negative divisors. Every real divisor
excludes zero; every complex division first certifies a positive lower
endpoint of its squared-modulus interval. Thus elementary interval
inclusion follows inductively without Decimal contexts or floating point.

For its independent exponential, halve the input rectangle until its
coordinate absolute-upper-bound sum is at most 1/16. Sum degrees 0 through
512, enlarge each coordinate by the upward dyadic rounding of
2/(16^513*513!), then square back. The first omitted term has modulus at
most 1/(16^513*513!), and successive absolute terms have ratio at most
1/16; their sum is strictly below the stated remainder. Directed halving
and squaring retain all rounding uncertainty. This independently encloses
the exponentials used in both windows and in every combined moment.

Primitive coefficients are recomputed as exact Gaussian rationals, and
every coefficient identity Q'+aQ=P is checked exactly, including P's
constant subtraction. Polynomial endpoint evaluations for the fixed
window are Gaussian rational before multiplication by exponential
intervals. The five-term signs and exponents agree with the complete
kernel above: the cosh factor 1/2 cancels the kernel's -2, leaving the
positive cn endpoint, negative c(n+2) endpoint and positive fixed-window
term. Products conjugate both coefficients and exponents; every actual
combined real exponent is at most -n/2, so the zero-exponent branch is
unneeded. The integration-by-parts recurrence above is exact at each
degree and is replayed for every moment. Only finite operations occur.

For EACH saved real and imaginary coefficient, moment and integral
interval, the checker requires containment of the ENTIRE independently
computed interval, not overlap or agreement of midpoints. It checks all
five target terms, all fifteen indexed products, all their coefficient
and moment lists and lengths, and the complete norm aggregation. Diagonal
imaginary intervals contain zero. Exact integer square root at scale S
encloses sqrt(n), with the perfect-square case retained exactly. Lambda
and B are independently enclosed, and the penalty is independently
computed as exp(2 sqrt(n)-n/16), rather than by multiplying the saved
lambda and B endpoints. The identity with the original positive penalty
is the real exponential addition law. Its interval and the independently
computed screen are contained in their original saved intervals.

The complete replay certificates, storing every independent term,
product coefficient, moment, integral, scalar and comparison, are
`scripts/target-radau/audit-penalty-screen-64-416.json` and
`scripts/target-radau/audit-penalty-screen-128-416.json`. Their summary and
hashes are `scripts/target-radau/audit-penalty-screen-416.json`. Reproduce
with `python3 scripts/target-radau/audit-penalty-screen-416.py`.
All 6924 comparisons at 64 and 13580 at 128 pass; no failures. The saved
entry widths are checked from their full rational endpoints against
2^-256, and the saved screen widths against 2^-60. The full original
F_upper values independently satisfy the strict bounds in the table.
Complete selected F_upper/entry-width and audit-summary fields were also
inspected with the JSON inspector; the implementation processes ALL
relevant certificate arrays, not bounded previews.

The symbolic audit accepts the realification, adjoint convention, PSD
and positive regularization, arbitrary-data minimizer, original complex
l1-to-l2 cap relaxation, factor 2 from |I|=1/2, and inequality (1).
Nonnegative inverse forms suffice, including h=0 and singular G; no
cyclic compression, Radau applicability or numerical inverse is needed.
Zero Lanczos steps and the absence of G,h/inverse/quadrature data are
verified explicitly. The strict negative screen parks this fixed test;
it does not establish that the best capped residual is small or that an
asymptotic certificate cannot work. All remaining gaps below survive.

### Scope and remaining gaps

The finite negative result parks precisely the prescribed n=64,128,
lambda=exp(-n/16) test. It does not exclude an asymptotic positive F,
other independently assessed mechanisms or the desired E_n threshold.
There is no lower conclusion about E from these negative F values beyond
E>=0. No parameter, degree, precision, iteration or node sweep was made.
Stops341/410 retain their original scope. Unbounded target-mass rates,
C997a(8), selected/both-sign transfer, reconstruction, complements and
regulators, L993, L984(H), L966/L968 forcing and actual-Xi positivity
remain unpaid. There is no cross-notebook input.

## Mathlib

Full matching coverage of this complete-kernel finite obstruction is
unchecked and unknown. Standard finite-dimensional spectral theory,
Hilbert adjoints and the generic quadratic minimizer are supporting
inputs, not a claimed matching theorem. No absence claim or Mathlib
completion claim is made.
