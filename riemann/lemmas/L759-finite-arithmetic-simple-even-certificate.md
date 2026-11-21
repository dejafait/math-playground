# L759 — one finite arithmetic simple-even certificate

## Hypotheses

Let lambda=sqrt(13), L=2 log(lambda)=log(13), N=120. Use exactly
Connes--Consani--Moscovici, *Zeta Spectral Triples*,
[arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1),
Lemma2.3, (3.10)/(3.13), and (4.1)-(4.4). In particular the real
symmetric matrix A=QW_lambda^N is in the orthonormal basis

    V_j(u)=L^(-1/2) exp(2 pi i j log(lambda u)/L), -120<=j<=120,

extended by zero outside [lambda^-1,lambda]. Its sign convention is
A=W_(0,2)-W_R-sum_p W_p. The even block uses V_0 and
(V_j+V_-j)/sqrt(2); the odd block uses (V_j-V_-j)/sqrt(2), 1<=j<=120.
Write their ordered eigenvalues as mu_plus_j and mu_minus_j.

This is a computer-assisted finite calculation, using the documented
correct-rounding semantics of Python's standard-library Decimal.
The mathematical reduction, full entry enclosures and interval LDL
certificate are supplied below. Step361 independently audited the analytic
reduction and implementation and replayed inertia with integer intervals
and a different LDL recurrence; see section6. Python/Decimal and integer
arithmetic semantics remain software trust assumptions.
No zero location, Weil positivity or eigenfunction limit is assumed.

## Conclusion

For this cell only,

    mu_plus_0 < 5*10^-56,
    mu_plus_1 > 10^-55,       mu_minus_0 > 10^-55.

Consequently min(mu_plus_1,mu_minus_0)-mu_plus_0 > 5*10^-56.
The minimum of A is simple and even, in Definition5.3 of the source.
There is no assertion that this minimum is positive. In particular,
this is neither a sign certificate for the unshifted Weil form nor an
RH argument. It supplies one finite instance of a source hypothesis,
not a general parity theorem or a discovery beyond the inspected sources.

## Proof

### 1. Exact entries and their reduction to scalar integrals

The cited Lemma2.3 gives, for 0<=y<=L,

    q_nm(y)=(sin(a_m y)-sin(a_n y))/(pi(n-m)), n!=m,
    q_nn(y)=2(1-y/L)cos(a_n y),   a_n=2 pi n/L.

The point contribution, imported from (4.2), is

    32 L sinh(L/4)^2 (L^2-16 pi^2 mn)
       / ((L^2+16 pi^2 m^2)(L^2+16 pi^2 n^2)).

The prime sum (4.3) is sum Lambda(k)/sqrt(k) q_nm(log k), over the
complete prime powers 2,3,4,5,7,8,9,11,13, where Lambda(p^r)=log p.
The endpoint k=13 is retained; its exact contribution vanishes.

Set rho(y)=exp(y/2)/(2 sinh y) and, for 0<=n<=120, define

    S_n=int_0^L rho(y) sin(a_n y) dy,
    C_n=int_0^L rho(y) (cos(a_n y)-1) dy,
    D_n=int_0^L y rho(y) cos(a_n y) dy,
    B=int_0^L (exp(y/2)-1)/(2 sinh y) dy.

These are proper integrals after removable endpoint cancellation.
Extend S_-n=-S_n. Direct substitution into the DEFINING (4.4) gives

    (W_R)_nm=(S_m-S_n)/(pi(n-m)), n!=m,
    (W_R)_nn=gamma+log(4 pi*6/7)+2(C_|n|-D_|n|/L+B).

Here (exp(L)-1)/(exp(L)+1)=6/7. Thus the exterior correction is included.
These equalities reconcile the scalar reductions with (4.4) directly;
the source's special-function shorthand is not used or presumed correct.

### 2. Absolutely justified series, with explicit tails

For y>0, rho(y)=sum_{k>=0} exp(-b_k y), b_k=2k+1/2. Put
E_k=exp(-b_k L)=13^(-2k)/sqrt(13). Since a_n L=2 pi n,
termwise elementary integrations give

    S_n=sum a_n(1-E_k)/(b_k^2+a_n^2),
    C_n=-sum a_n^2(1-E_k)/(b_k(b_k^2+a_n^2)),
    D_n=sum [(1-E_k)(b_k^2-a_n^2)/(b_k^2+a_n^2)^2
                         -L E_k b_k/(b_k^2+a_n^2)],
    B=sum [(1-E_k)/b_k-(1-E_k/sqrt(13))/(b_k+1/2)].

All sums run over k>=0. These interchanges are absolute: before
integration, bound |sin(ay)| by |a|y, |cos(ay)-1| by a^2 y^2/2,
and |y cos(ay)| by y. The resulting integral sums are bounded by
|a| sum b_k^-2, a^2 sum b_k^-3, and sum b_k^-2 respectively.
For B use 0<=1-exp(-y/2)<=y/2, giving (1/2)sum b_k^-2.
This also justifies differentiation-free evaluation at n=0.

Use K=512, R=160, b_*=2K+1/2. For the tail put
T_s=sum_{k>=K} b_k^-s, s>=2, and z=a_n^2/b_*^2<0.09.
Keep k<K exactly as displayed. Ignoring exponential terms momentarily,
the tail approximations, with r=0,...,R-1, are

    S: sum (-1)^r a^(2r+1) T_(2r+2),
    C: -sum (-1)^r a^(2r+2) T_(2r+3),
    D: sum (-1)^r (2r+1) a^(2r) T_(2r+2),
    B: sum (-1)^r 2^(-r-1) T_(r+2).

Finite geometric expansion gives respective absolute remainders at most

    |a|^(2R+1) T_(2R+2),
    a^(2R+2) T_(2R+3),
    a^(2R) T_(2R+2) [(2R+1)/(1-z)+2z/(1-z)^2],
    2^(-R-1) T_(R+2).

For D expand (1-t)/(1+t)^2=sum_{r>=0}(-1)^r(2r+1)t^r;
bound its absolute tail by t^R[(2R+1)/(1-z)+2z/(1-z)^2].
For S,C,B use the exact finite geometric remainder with t>=0.

The omitted exponential tail has ratio E_(k+1)/E_k=1/169.
Interval evaluation verifies exp(-b_* L)<10^-1100. With |a|<302,
L<3 and b_*>1024, the S,C,D,B exponential losses are bounded,
respectively, by

    |a| delta/(b_*^2(1-1/169)),
    a^2 delta/(b_*^3(1-1/169)),
    delta(b_*^-2+L/b_*)/(1-1/169),
    2 delta/(b_*(1-1/169)),        delta=exp(-b_*L).

Each is less than 10^-1090. The script adds that error to EVERY
scalar integral, including zero frequencies, as well as the geometric
tail bounds above. No infinite-series tail is inferred from numerical
stability or sampling.

### 3. Inverse-power tails, constants and directed rounding

Bernoulli numbers are computed as exact rational numbers. With m=80,
Euler--Maclaurin gives an enclosure for T_s centered at

    b_*^(1-s)/(2(s-1)) + b_*^-s/2
    + sum_{r=1}^{m-1} B_(2r)/(2r)! * 2^(2r-1)
                              * (s)_(2r-1) b_*^(-s-2r+1),

with radius twice the absolute value of the same r=m summand.
Here (s)_j is the rising factorial. This deliberately allows two
last-term losses. For precise standard inputs see
[DLMF 2.10.1](https://dlmf.nist.gov/2.10.E1) and
[DLMF 24.8.1](https://dlmf.nist.gov/24.8.E1).
The latter implies |B_(2m)({x})|<=|B_(2m)|. In the former,
|B_(2m)-B_(2m)({x})|<=2|B_(2m)|. For
f(x)=(2x+1/2)^(-s) its absolute 2m-th derivative integral on
[K,infinity) is
2^(2m-1)(s)_(2m-1)b_*^(-s-2m+1), proving exactly this radius.
All derivatives are integrable and the boundary terms at infinity vanish.

Likewise gamma is enclosed by

    H_K-log K-1/(2K)
         +sum_{r=1}^{m-1} B_(2r)/(2r K^(2r)),

with radius 2|B_(2m)|/(2m K^(2m)). Apply the same finite
Euler--Maclaurin formula to 1/x on [K,M], subtract log M and let
M tend to infinity; its 2m-th derivative has integral
(2m-1)! K^(-2m). No unproved favorable remainder sign is used.

Pi uses Machin's identity pi=16 arctan(1/5)-4 arctan(1/239).
Its principal-angle identity follows from tangent addition, and each
arctangent uses 400 alternating terms with the next-term error bound.
log and sqrt endpoints are rounded to nearest by Decimal, then expanded
by one adjacent representable number in each outward direction.
The same safeguard is applied to exp. These operations are monotone on
the positive/real domains used. All +,-,*,/ operations use separate
170-digit floor and ceiling contexts, with division rejecting an
interval containing zero. Thus every expression encloses its exact value.
The required semantics are documented in the primary
[Python Decimal reference](https://docs.python.org/3/library/decimal.html),
Decimal.ln/exp/sqrt, Context and rounding modes; this is a software trust
assumption, not a formal verification of the interpreter.

Prime terms use sin/cos(2 pi n log k/L). Subtract any selected integer
from n log k/L (exact periodicity); the retained interval argument has
absolute value <4. Taylor terms through degree519 for sin and degree518
for cos are interval evaluated. Subsequent absolute term ratios are
less than 1/2, so twice the next term's absolute bound encloses the
whole remainder. Rounding the integer selection affects efficiency
only; the reduced interval is retained, not replaced by its midpoint.

### 4. Complete matrix and inertia certificate

Reproduce using the standard library only, from this notebook:

    python3 scripts/spectral-triples/finite-parity-359.py

The complete artifact is
`scripts/spectral-triples/finite-parity-359.json`. It records constants,
all T_s, all scalar integrals, every full/parity entry interval, every
LDL pivot, exact shift strings, counts, bounds and failures. The script
hash is saved. Its matrices have dimensions 241, 121 and 120.
All entry widths are <4*10^-165 (full maximum 3.7009*10^-165;
parity maximum 3.7135*10^-165). Signed terms are never discarded.

For each shifted exact parity matrix, interval symmetric elimination
updates its Schur complement by M_ij <- M_ij-M_jk M_ik/p_k.
No pivot interval contains zero. Induction on k proves every Schur
entry and pivot enclosure valid for the exact original matrix; stored
entries are treated as simultaneous enclosures, without assuming their
errors independent. Sylvester's law of inertia then identifies the
number of eigenvalues strictly below the shift with the number of
negative pivots. Nonsingular pivots also exclude equality at the shift.
There is no eigensolver tolerance or additional Weyl-error term to pay:
every entry error is already propagated through the interval elimination.

The complete successful counts are

| Block | Shift | Negative pivots | Total nonzero pivots |
| --- | --- | ---: | ---: |
| Even | 10^-55 | 1 | 121 |
| Odd | 10^-55 | 0 | 120 |
| Even | 5*10^-56 | 1 | 121 |

Across these 362 pivots the minimum endpoint distance from zero is
greater than 3.7*10^-11, and the maximum interval width divided by
its endpoint distance is less than 2*10^-36. These pivot margins are
not eigenvalue lower bounds. Full saved fields were also checked for
entry ordering, symmetric interval overlap, pivot sign/count consistency
and script hash in `scripts/spectral-triples/finite-parity-359-evidence-check.json`.
That is a consistency check, not an independent analytic proof or replay.

The finite-dimensional spectral theorem and these counts imply the
three strict bounds in the conclusion. Their difference is strictly
greater than 10^-55-5*10^-56=5*10^-56>0. Symmetry and parity invariance
are imported from the source's Lemmas5.1-5.2. The simple even minimum
therefore follows, without presuming a favorable sign of its eigenvalue.

### 5. Qualifications and retained unsuccessful evidence

An initial binary-floating screen could not distinguish small levels.
The first interval pass used thresholds a decade apart and was
inconclusive for separation; its saved artifact is
`scripts/spectral-triples/finite-parity-359-first-pass.json`.
Its Euler--Maclaurin remainder inflation was subsequently enlarged
from one to TWO last terms before the successful run. Accordingly its
counts are preliminary diagnostics only, and do not support this proof.
The successful certificate uses the corrected two-term inflation and
three separating shifts; it does not depend on that first pass.

This calculation reproduces a finite source hypothesis, not the
source's high-accuracy zeta-zero comparisons. General simplicity and
parity, N->infinity boundary-normalized convergence, lambda->infinity
ground-state approximation and actual-Xi signs all remain unresolved.
No other lambda or N was tested, and no finite agreement is promoted
to an asymptotic or creative mechanism. The original pending-audit state
is retained in the step359 history; the completed audit follows.

### 6. Independent conceptual and computational audit (step361)

The exact scope is the approved assessment
`drafts/literature/2026-11-04-finite-parity-certificate-audit.md`.
This is REPRODUCTION: independent validation of the finite certificate,
not a further theorem about the limiting arithmetic family.

**Defining-integral cases.** In the source's (4.4), write omega=q_nm.
For n!=m, omega(0)=0 and the integral is exactly
(S_m-S_n)/(pi(n-m)), including n=0 or m=0. Indeed omega(y)=-2y/L+O(y^3),
so its integrand tends to -1/L. For n=m, omega(0)=2 and

    exp(y/2)omega(y)-2
      =2[exp(y/2)(cos(a_n y)-1)
          -(y/L)exp(y/2)cos(a_n y)+(exp(y/2)-1)].

After division by 2 sinh y, integration gives 2(C_n-D_n/L+B).
The canceled integrands for S,C,D,B tend respectively to a_n/2,0,1/2,1/4
at zero; thus the diagonal limit is 1/2-1/L, also for n=0.
At n=0, S_0=C_0=0 exactly, while D_0 and B are retained. The exterior
integral is (1/2)log(7/6), giving the stated log(4pi*6/7) term.
At y=L all q_nm vanish, so retaining the k=13 prime term, with an
interval enclosing its exact zero, is valid. The prime powers listed
in section1 are exhaustive through 13. The sign of each component,
the pole term (4.2), and the translated orthonormal basis agree with
the source's (3.13), (3.21), and (4.1)-(4.4).

**Series and constants.** To check all four elementary integrations,
put b=b_k, a=a_n, E=exp(-bL), and aL=2pi n. The sine integral is
a(1-E)/(b^2+a^2); the cosine integral is b(1-E)/(b^2+a^2).
Subtracting (1-E)/b gives C's summand. Integrating y exp(-by)cos(ay)
gives D's displayed summand. Subtracting the zero-frequency integrals
at b and b+1/2 gives B's summand, since exp(-(b+1/2)L)=E/sqrt(13).
The absolute integral estimates in section2 justify every interchange.
Writing t=a^2/b^2 gives the three rational geometric expansions;
writing t=1/(2b) gives the fourth. The D coefficients are 2r+1, and
their absolute tail sums to the stated expression. The exponential
tail estimates follow from |b^2-a^2|/(b^2+a^2)^2<=b^-2 and
b/(b^2+a^2)<=b^-1, together with E's ratio 1/169.
The certified constants imply 5/2<L<3 and pi<22/7, hence |a|<302,
z<0.09. The program checks delta<10^-1100. These inequalities give
each exponential loss <10^-1090, including zero frequencies.

The full Euler--Maclaurin expressions and gamma sign were checked
against the two cited DLMF formulas. Their finite-endpoint remainders
are absolutely dominated by the derivative integrals in section3;
all boundary derivatives vanish in the upper-endpoint limit.
Independent exact rational Bernoulli recurrence

    B_0=1, B_n=-sum_{j=0}^{n-1} binom(n+1,j)B_j/(n+1)

matches every even coefficient B_0,...,B_160 used by the generator.
Its different B_1 convention is irrelevant because only even indices
are used. Machin's identity also has the right branch: if
theta=atan(1/5), beta=atan(1/239), then tan(4theta)=120/119 and
tan(4theta-beta)=1; elementary alternating bounds put 4theta-beta
strictly between 0 and pi/2. The 400-term and trigonometric Taylor
remainders therefore enclose the intended constants and functions.

**Implementation and complete replay.** Every line of the original
347-line program was inspected. Arithmetic inputs are integers, exact
decimal strings or existing Decimal objects, never binary floats.
Negation uses exact copy_negate; ordinary arithmetic uses directed
contexts. Multiplication checks all four endpoint products, reciprocal
is decreasing on either component of R minus zero, and every divisor
is rejected if its interval meets zero. Repeated squaring is enclosing
even for intervals crossing zero. The monotone ln/exp/sqrt endpoints
are widened by adjacent representable values under the documented
[Python3.15 Decimal contract](https://docs.python.org/3.15/library/decimal.html).
The integer chosen for trigonometric reduction need not be exact-nearest:
periodicity holds for any integer and the retained argument is checked
to have absolute value <4. Its interval is never replaced by a midpoint.
No claim of interpreter conformance beyond that contract is made.

Run the independent audit from this notebook:

    python3 scripts/spectral-triples/finite-parity-audit-361.py

It copies the original generator to a temporary directory, preserves
the original artifacts, and saves the complete new output to
`scripts/spectral-triples/finite-parity-replay-361.json`. All 19 fields
other than elapsed time match the original exactly, including every
constant, all 322 T_s intervals, all 121 scalar triples, all matrix
entries and all 362 original pivots. The original script hash matches.
Decimal contexts have exponent limits +/-999999; only Rounded and
Inexact flags occur, with no underflow, overflow, invalid operation,
division by zero, subnormal result or clamping. The complete original
pivot signs, counts, distances and relative-width bounds in section4
were checked, not inferred from a preview.

**Independent inertia.** The second arithmetic implementation represents
[l/10^220,u/10^220] by integer endpoint pairs. Fraction parsing is exact;
integer floor/ceiling divisions enclose all endpoint products and
quotients. Addition/subtraction are exact on the grid. No Decimal
arithmetic or original interval class is used by this implementation.
An integer-square-root enclosure of sqrt(2) independently checks every
parity-basis conversion against the saved intervals. All 58081 full,
14641 even and 14400 odd entries are checked for ordering and symmetric
intersection. Their widths are bounded as in section4.

Instead of the original evolving Schur complements, use the unchanged
input B=A_parity-shift*I and compute unit-lower-triangular H and pivots d:

    d_j=B_jj-sum_{r<j} H_jr^2 d_r,
    H_ij=(B_ij-sum_{r<j} H_ir H_jr d_r)/d_j, i>j.

Inductively the interval recurrence encloses the exact LDL factors;
no computed d_j interval meets zero. For the exact symmetric B this
gives B=H diag(d) H^T, so congruence proves its inertia. The full audit
artifact `scripts/spectral-triples/finite-parity-audit-361.json` contains
all factor intervals and all 362 independently computed pivots. It
reports counts 1,0,1 at the same three shifts, every pivot nonzero,
no failures, and AUDIT_PASSED. The strict gap conclusion follows by
the finite-dimensional spectral theorem exactly as in section4.
Independent arithmetic and recurrence validate the inertia of the
entry enclosures; the source reduction and analytic audit above are
still essential to identifying those entries with the intended matrix.

The first audit harness incorrectly demanded identical rounded
intervals at transposed parity positions. Different addition order
can produce unequal endpoints while both intervals enclose the same
exact entry. Its stopped script/report are retained as
`scripts/spectral-triples/finite-parity-audit-361-precheck.py/.json`.
The final harness checks nonempty symmetric intersections; exact
symmetry is supplied by the source formulas. This was a checker defect,
not a mathematical defect in L759 and not negative spectral evidence.
No new parameter cell, unshifted sign or limiting conclusion is asserted.

## Mathlib

Matching theorem and verification-library coverage were not checked.
Finite-dimensional spectral theory, Sylvester inertia and elementary
series estimates are standard inputs; no claim is made that Mathlib
contains this matrix or this interval certificate. The present proof is
informal and computer-assisted, not a Lean formalization.
