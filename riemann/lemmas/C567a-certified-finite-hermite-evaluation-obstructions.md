# Corollary 567a: three complete finite Hermite evaluation obstructions

## Hypotheses

Use the actual Xi coefficients, physicists' Hermite polynomials and
P_N of L564, with D(P_N)=P_N'^2-P_N P_N''. Use the complete allowed
Hermite-square cone of L567. No RH assumption, coefficient asymptotic,
zero-free estimate or signed Xi transfer is assumed. Romik's expansion
and coefficient normalization remain imported as qualified in L564.

The analytic inputs used below are Cauchy's derivative formula,
[NIST DLMF 1.9.30–31](https://dlmf.nist.gov/1.9.E31), for a function
analytic inside and continuous on a simple closed contour, and the real
Lagrange interpolation remainder,
[NIST DLMF 3.3.5](https://dlmf.nist.gov/3.3.E5), for distinct real nodes
and a continuous derivative of order one more than the interpolant's
degree on their containing interval. Their use requires the domain and
derivative bounds proved here, not an assumption of positive weights.

## Conclusion

The following are rigorous enclosures; the terminating scientific
notations denote exact rational endpoints.

| N | x | Enclosure of complete D(P_N)(x) |
|---|---|---|
| 64 | 163/4 | [-2.728e-22, -2.726e-22] |
| 128 | 271/4 | [-8.226e-38, -8.224e-38] |
| 256 | 447/4 | [-2.006e-69, -2.004e-69] |

Thus, at each indicated cutoff, the complete polynomial D(P_N) is
outside even the unrestricted global real SOS cone, and hence outside
L567's parity-preserving bandwidth-two Gram cone. Evaluation at each
x is a functional nonnegative on every allowed square and strictly
negative on the complete discriminant.

These are three finite computer-assisted rational certificates. The
analytic enclosure and full computation passed the independent audit
below on 2026-10-31. No unbounded family is proved. The x lie outside L564's
corresponding [T,2T], where T=sqrt(N/16)-1; no interval positivity,
Xi sign, multiplicity conclusion or RH resolution follows. The
result is a local obstruction beyond the outcomes asserted by the
sources checked, not a claim of certified literature originality.

## Proof

Write g(u)=exp(-u^2/4)Phi_R(u) using the positive-u theta formula
in L564 and mu_n=2 integral_0^infinity u^(2n)g(u)du. Then
b_(2n)=mu_n/[2^(2n)(2n)!]. All n=0,...,256 are retained.

### Complex bound and interpolation remainder

On the union of closed radius-1/2 disks centered at [0,4], put
z=a+ib. We have -1/2<=a<=9/2, |b|<=1/2 and

    Re(exp(2z))=exp(2a)cos(2b)>1/(2e).

Indeed cos(1)>1/2 and exp(2a)>=exp(-1). With pi>3 and e<3,
pi/(2e)>1/2. Thus each theta exponential has modulus at most
exp(-k^2/2). Also |exp(-z^2/4)|<=exp(1/16)<2.
Dropping signs and using pi<4, exp(81/4)<3^21,
exp(45/4)<3^12, and k^2<=k^4 gives

    |g(z)| <= 2(64*3^21+24*3^12) sum_(k>=1)k^4 exp(-k^2/2)
            < 2(64*3^21+24*3^12)*10000 < 2^60.

For the sum, exp(1/2)>3/2, k^2>=k and differentiation of the
geometric series gives sum k^4(2/3)^k=2190<10000. The same uniform
majorant proves normal convergence of the analytic theta summands on
these disks, so g is analytic in an open neighborhood of every disk.
This uses the positive-u formula's analytic continuation locally; no
estimate for the even extension on a complex half-plane is assumed.

On a radius-1/2 disk centered at v in [0,4], the triangle inequality
gives |z|<=v+1/2<=9/2. For f_n(z)=z^(2n)g(z), the bound is
B_n=2^60(9/2)^(2n). Cauchy's derivative estimate gives
|f_n^(257)(v)|/257!<=B_n/(1/2)^257 for every real v in [0,4].
On each of the 128 panels of length Delta=1/32, interpolate f_n at
257 equally spaced nodes by its degree-256 Lagrange interpolant.
The standard real interpolation remainder, obtained by repeated
Rolle's theorem, is f_n^(257)(v)/257! times the product of the
257 distances to the nodes, each at most Delta. Therefore the
pointwise error is at most B_n*16^(-257). Integrating over total
length 4 and doubling for the full-line even moment bounds its
quadrature error by

    R_n=8*2^60*(9/2)^(2n)*16^(-257).

The rule's weights are exact integrals of Lagrange basis polynomials;
signed weights cause no problem because every node value is enclosed
before multiplying by its signed weight. The program constructs them
by integer polynomial division and checks all 257 monomial moments.
This applies the standard interpolation remainder and Cauchy integral
formula, not agreement between numerical meshes or a new quadrature
theorem. The bound covers the FULL theta kernel g, while the node
values omit theta indices k>=25. Their additional error is below.

### Complete omitted tails

For 0<=u<=4, positivity of every original theta bracket and pi<4
give

    0<=Phi_R(u)-Phi_(<=24)(u)
      <=64*3^18 sum_(k>=25) k^4 exp(-3k^2)
      <=64*3^18*2^(-1849).

Here k^4<=2^k for k>=25: check the initial integer inequality
and propagate using (1+1/k)^4<2. The first term of
sum 2^(k-3k^2) is 2^(-1850), and its successive ratio is
at most 2^(-152)<1/2. Let A=sum_(i=0)^256 |w_i| for the unit-panel
Lagrange integration weights. The sum of absolute composite weights
is at most 128*(1/32)*A=4A (merging shared nodes can only reduce it).
Since u^(2n)<=4^(2n), the full-line QUADRATURE error from these
indices has absolute value at most

    Theta_n=512*A*3^18*2^(-1849)*4^(2n).

The node-truncation error in a SIGNED quadrature rule needs this
absolute weight norm and both error signs. The first running code
used the integral theta bound without this norm; its node values
and raw finite-theta quadrature totals remain valid, but its initial
moment/pairing enclosures must not be used. The corrected code
reprocesses those totals with the formula above before any claim.

For the spatial tail use L564's whole-kernel bound

    Phi_R(u)<=9600 exp(9u/2)exp(-(3/2)exp(2u)).

For n<=256 and u>=4, the logarithmic derivative of
u^(2n)exp(9u/2)exp(-(3/2)exp(2u)) is
2n/u+9/2-3exp(2u)<=128+9/2-3exp(8)<-1.
Integrating this differential upper bound controls the tail by its
value at 4. Also e>8/3 by its first five Taylor terms,
(8/3)^8>2048, e<3, and exp(-3072)<2^(-3072). Dropping
exp(-u^2/4)<=1 yields the full-line moment bound

    S_n=19200*3^18*4^(2n)*2^(-3072).

### Rational arithmetic and complete signed sums

The implementation uses scale 2^2048, with integer outward floor
and ceiling on every arithmetic operation. The existing local
interval rules are imported from the N=2 certificate implementation,
not its result or its insufficient quadrature accuracy. For
0<=x<=1 the exponential uses terms through order 320 and error
<=3/321!. Positive arguments are halved then squared back;
negative arguments are halved in magnitude, reciprocated with
outward endpoints before repeated squaring. Arguments <=-2048
use [0,2^(-2048)], valid since e>2. Monotonicity encloses exp of
an interval. No floating-point underflow is used.

Pi uses Machin's identity and alternating arctangent sums with 512
terms at 1/5 and 150 terms at 1/239, including the next term.
For completeness, double-angle identities give
tan(4 atan(1/5))=120/119 and
tan(4 atan(1/5)-atan(1/239))=1. The angle is positive and at most
4/5<pi/2, which selects pi/4 and proves the identity's branch.

At each exact rational node, enclose all 24 theta terms, the Gaussian,
and u^(2n), including n=0 and 256. Accumulate signed-weight interval
products. If [Q_lo,Q_hi] is the finite-theta half-line quadrature
interval, the complete moment enclosure is

    [2 Q_lo-R_n-Theta_n, 2 Q_hi+R_n+Theta_n+S_n].

Only the genuine positive spatial integral uses a one-sided error;
the quadrature theta error and interpolation error are two-sided.
Enclose every b_(2n) by exact rational
division; do not round tiny coefficients to a fixed absolute scale
before multiplying by the potentially enormous Hermite values.

At each x=p/4 compute H_0=1, H_1=2x,
H_(j+1)=2x H_j-2j H_(j-1), all exactly rational. Use the complete
sums for P_N, P_N', P_N'', with derivative multipliers 2j and
4j(j-1). Their interval products enclose P_N'^2-P_N P_N'';
if an interval for P_N' contains zero, its squared lower bound is
zero. No coefficient asymptotic, omitted mixed term, floating sign,
or unproved interchange enters these finite calculations.

### Complete certificate and decisive inequalities

The implementation is `scripts/hermite-gram/global-dual-pairing-certificate.py`.
A fresh reproduction, using only Python 3 standard-library integer and
Fraction arithmetic, is

    python3 scripts/hermite-gram/global-dual-pairing-certificate.py

The complete output is
`scripts/hermite-gram/global-dual-pairing-certificate.json`. It stores
all 32769 finite-theta node enclosures, 257 exact unit-rule weights,
their absolute norm, all raw moment sums, all three error bounds for
every n, all 257 full moment and coefficient enclosures, and exact
rational P_N, P_N', P_N'' and D(P_N) enclosures at all three points.
All 257 rule moment conditions pass; all three complete upper bounds
are negative and all full enclosures are contained in the displayed
coarse rational intervals. The reported failure list is empty.
Scientific-notation previews are not used as evidence for these signs.

The current artifact retains the freshly computed node bounds and
reprocesses their raw finite-theta sums after the signed-theta correction
above, using

    python3 scripts/hermite-gram/global-dual-pairing-certificate.py --reuse-nodes

This mode verifies matching parameters and exact weights but trusts
retained raw node values and sums; it is not an independent node replay.
The fresh command or an independent enclosure is required to audit
those values. The earlier provisional tail/pairing output was not a
valid certificate and is not the evidence claimed here. The retained
node calculation is unchanged by the corrected postprocessing.

The full finite sums include every n=0,...,N. Inserting the complete
coefficient intervals into the exact Hermite recurrence and both
exact derivative sums, then applying the outward interval-product
rules, proves the displayed bounds. In particular their upper
endpoints -2.726e-22, -8.224e-38 and -2.004e-69 are strictly negative.
This is an exact finite rational calculation with the explicit
analytic errors above, not a solver status or numerical convergence
claim.

Finally, for any real polynomial A and any of the three real x,
A(x)^2>=0. Thus evaluation is nonnegative on every individual
Hermite square and on every square of a real combination of two
allowed Hermite polynomials. Its edge blocks in L567 are the exact
outer products (h_j(x),h_(j-2)(x))(h_j(x),h_(j-2)(x))^T, including
zero diagonals and singular determinants. This verifies every
allowed-square constraint, without an inverse pivot or a PSD-completion
assumption. The earlier full integer constraint certificate remains
at `scripts/hermite-gram/global-dual-evaluation-constraints.json`
(896 diagonals and 890 edge blocks); the direct square argument also
proves all constraints independently of those counts. A global SOS
identity would evaluate to a nonnegative number, contradicting the
certified negative complete pairing. No closed-image or generic
strict-separation theorem is needed for this direct obstruction.

### Independent conceptual and arithmetic audit, 2026-10-31

The complete analytic and arithmetic audit passes without changing any
bound or withdrawing any of the three finite obstructions. This is
independent validation of the existing local result, not a new theorem,
a manuscript audit of Romik's expansion, or an Xi sign conclusion.

**Analytic domain and interpolation.** The positive-u theta formula
defines a holomorphic function on the open strip |Im z|<pi/4.
Indeed, on each compact subset, Re(exp(2z)) has a strictly positive
minimum and Re z is bounded. Each summand and the Gaussian are entire,
and the absolute series is dominated there by C k^4 exp(-c k^2) with
c>0. Normal convergence therefore proves holomorphy on this open strip.
All the closed disks used above lie inside it, since 1/2<pi/4. This
justifies an open analytic neighborhood of each contour; a bound only
on a closed set would not by itself justify the Cauchy application.

On these disks the original bound is valid: Re(exp(2z))>=e^(-1)cos(1),
cos(1)>1/2, and pi/(2e)>1/2. The exact comparison is
2(64*3^21+24*3^12)*10000=13389507191520000<2^60.
The dominating geometric fourth-moment sum is exactly 2190. For each
0<=n<=256, |z|<=9/2 gives B_n as stated. Cauchy's formula on radius
1/2 yields a uniform bound for the real 257th derivative at every
v in [0,4]. Each real panel and its 257 distinct nodes satisfy the
cited interpolation theorem. Bounding each factor in its remainder by
1/32 and integrating gives exactly R_n, including both panel endpoints.
This argument applies to the full theta function, before node truncation.

**Rule and omitted terms.** Dividing prod_(j=0)^256(t-j) by t-i
gives the numerator of the i-th Lagrange cardinal polynomial. Its
denominator is (-1)^(256-i)i!(256-i)!. Integrating from 0 to 256 and
dividing by 256 produces the unit-panel weights used in the program.
Independent exact checks verify all 257 moments, including degrees
0 and 256, their symmetry, and the full absolute norm A. Exactly 127
weights are negative, so positivity cannot replace that norm. The final
composite endpoint uses w_0 rather than w_256; these are exactly equal.
Internal shared endpoints use their sum. Thus the complete composite
norm is at most 4A, even with signed weights.

For the omitted theta terms, 25^4=390625<2^25 and
(26/25)^4=456976/390625<2; the latter ratio decreases with k.
The comparison series starts at 2^(-1850) with successive ratios
at most 2^(-152). Its sum is below 2^(-1849). The omitted true
node values are positive, but their signed weighted sum has either
sign, so precisely the stated two-sided Theta_n is needed. The
corrected certificate uses that bound at every index, including n=0.

For the spatial tail, (8/3)^8=16777216/6561>2048, so its logarithmic
derivative is at most 128+9/2-3*2048=-12023/2<-1 on [4,infinity).
The value-at-4 comparison therefore bounds the full integral by S_n.
This integral is nonnegative and only this error is one-sided.
The constant checks are recorded in
`scripts/hermite-gram/c567a-audit-analytic-checks.json`; they supplement
the analytic reasoning, not replace it.

**Interval implementation.** The inherited arithmetic functions use
floor for lower endpoints and ceiling for upper endpoints, with positive
denominators; multiplication takes all four endpoint products, including
negative weights. For the exponential, the Taylor error on [0,1] is
bounded by e/321!<3/321!. Every term is enclosed before addition.
Halving, positive reciprocal with reversed endpoints, and repeated
interval multiplication retain inclusion. If the argument is <=-2048,
0<=exp(x)<=2^(-2048) justifies the stored interval [0,1] at scale S.
The modified exp_point is assigned to the imported arithmetic module,
so exp_interval calls this same 2048-bit, order-320 implementation.
No cached lower-precision exponential routine is used.

The two alternating arctangent sums include their next terms and use
the correct crossed endpoints in 16 atan(1/5)-4 atan(1/239).
The branch verification above is valid. At a node u=i/8192, u and
u^2 are exact at this binary scale. Powers of exp(u/2) enclose the
three required exponentials, and powers of exp(-pi exp(2u)) enclose
all 24 theta exponentials. Replacing a bracket's lower endpoint by
max(0,lower) is valid because the true bracket is positive for u>=0.

**Independent complete contractions.** The retained node intervals
were independently contracted using u^2=i^2/2^26, with integer outward
division for every signed multiplication. Every one of the 257 raw
moment intervals agrees exactly. All R_n, Theta_n, S_n, two-sided
full moments and coefficient divisions were then recomputed exactly.
For each of the three points, the complete finite formula

    2^j H_j(p/4)=sum_(r=0)^floor(j/2)
       (-1)^r j! 4^r p^(j-2r)/[r!(j-2r)!]

was used independently of the recurrence, through degree 2N. Inserting
the enclosed b_(2n), n=0,...,N, into all three derivative sums gives
exactly the retained P, P', P'' intervals. Squaring with a zero lower
bound when necessary and taking all four P P'' products recovers the
complete D intervals. Dependence between coefficients can widen these
intervals but cannot invalidate their inclusion. All three intervals
are contained in the stated coarse rational bounds, strictly below zero.
The full arithmetic evidence is
`scripts/hermite-gram/c567a-audit-independent-arithmetic.json`.

**Allowed squares.** Fresh replay of the earlier constraint program
agrees field-for-field with its historical certificate; its old
uncertified-pairing flags concern that earlier screen only. The new
copy is `scripts/hermite-gram/c567a-audit-constraints-replay.json`.
It includes all 896 diagonal squares and 890 singular PSD edge blocks,
and independently checks every integer Hermite value by the finite
formula. More generally, evaluation of every real square is nonnegative,
so the unrestricted global SOS obstruction does not require the generic
closed-image assertion in L567. No pivot division, missing edge or
completion hypothesis enters this application.

**Fresh complete node replay.** The existing pairing program was rerun
from scratch, without --reuse-nodes, preserving the original artifact:

```bash
python3 -u - <<'PY'
import importlib.util
from pathlib import Path
p = Path('scripts/hermite-gram/global-dual-pairing-certificate.py').resolve()
s = importlib.util.spec_from_file_location('c567a_replay', p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)
m.OUT = p.with_name('c567a-audit-fresh-replay.json')
m.main()
PY
```

The fresh artifact has node_values_reused=false. Comparison with the
original establishes exact equality of all 32769 node intervals, all
257 raw sums, weights, moments, three tail bounds per index and
coefficient enclosures, pi bounds, and all three complete pairings.
Only elapsed time, node-reuse flag and software metadata were excluded
from mathematical comparison. All three coarse enclosures are retained:
their upper bounds are -2.726e-22, -8.224e-38 and -2.004e-69,
respectively, against the required threshold 0. No audit failure was
found. Full comparison and input hashes are in
`scripts/hermite-gram/c567a-audit-replay-comparison.json`.

Replaying the same enclosure algorithm alone would not independently
justify it; that justification is the analytic/interval audit above,
together with the separate exact contraction using the finite Hermite
formula. Conversely, the contraction alone would not validate raw
node enclosures; the full replay addresses that distinct requirement.
All computations are finite exact rational/integer operations. This is
a computer-assisted informal audit, not kernel-checked formal proof.
The interval, unbounded-height, zero/multiplicity and higher-form gaps
stated in the conclusion remain unchanged.

## Mathlib

Coverage of this full actual-coefficient finite certificate and its
quantitative analytic enclosure has not been checked. Availability
is unknown, not absent; no formal verification is claimed. Cauchy's
derivative estimate, real interpolation, rational arithmetic and
Hermite derivative results would be supporting inputs, not a matching
actual-coefficient theorem. General reference:
https://leanprover-community.github.io/mathlib4_docs/
