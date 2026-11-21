# C998c: A finite-cosine point certificate and its all-series cost stop

## Hypotheses

Use C998a's unchanged three real frozen middle trials q_j, EXACT neutral
completion, and both reflected parity densities v_(j,+),v_(j,-). Set
a=log(3)/4, ell=2a, tau=a*2^-80. The free coordinates n=2,...,255 are
the exact dyadics in `free_middle_dyadics` of
`scripts/separation-seven/frozen-reference-proposal-652.npz`, SHA256
`2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
All C998a/C999/C999q/C999y/C999z/C744v qualifications are retained:
analytic-response, arithmetic, source-to-Xi, whole-core and unreplayed
c_* contracts are not independently verified here. No result of the
unaudited C998b is assumed.

The point input is an integer T with a caller-certified enclosure

    |t-T*2^-1024|<=2^-1024,    tau<=t<=a.              (1)

Every such t has such an encoding. Generation/validation of an outer
quadrature node's code is NOT supplied by this lemma. A wide real interval
or an uncertified approximate input does not meet (1). This is an
explicit finite-precision input contract, not access to an exact real.

The invocation-start SPECIALIZE assessment658 (including repaired primary
links659) covers this REPRODUCTION. Import NIST DLMF
[6.6.5-6](https://dlmf.nist.gov/6.6), version1.2.8,15September2026:
the convergent series for Si(z) and Ci(z)-gamma-log(z), with definitions
and branches [6.2.9,11-13](https://dlmf.nist.gov/6.2#ii). Only positive
real arguments are used. The finite tail estimate is a direct instance
of the term-ratio method in Johansson, *Computing hypergeometric
functions rigorously*, [arXiv:1606.06977v2](https://arxiv.org/pdf/1606.06977v2),
Section4.1, Theorem1 and proof. These general results are not reproved.
Setup uses the already covered positive atanh series and Machin formula
for pi (C999q Section3's scalar construction, reused by review658).
Directed rational/dyadic inclusion arithmetic is the method imported by
reviews655/656/658; its elementary integer implementation is explicit
below. No optimized library cutoff or requested precision is treated
as an accuracy or work guarantee.

Declare an operational ceiling100000000 bounded integer scalar operations
for a prospective11174=302*37-point batch. An operation means an integer
addition/subtraction, multiplication, division, shift or comparison, on
registers of at most16384 bits in the NUMERICAL setup/point algorithm.
Integer square roots are expanded into bounded bisection. This is a
chosen work test, not elapsed time, bit complexity or the contribution
unit of657. Proof-certificate verification is a separate finite planning
calculation; its factorial integers need larger registers and are not
hidden numerical oracles used by a point call.

## Conclusion

There is an explicit fixed algorithm with N=2048 series terms,
P=4096 fractional bits, and no precision doubling, which returns all six
Carleman values

    integral_0^a v_(j,epsilon)(s)/(t+s) ds

with centers of absolute error less than2^-425, uniformly under (1).
Radius2^-400 is therefore valid and is smaller than the required2^-53.
The zero mode, both parity signs, all modes through255, exact neutral
completion, constants, input uncertainty and final accumulation are paid.

Numerical setup costs at most10000000 scalar operations, including the
finite constant/normalization computations and all coefficient intervals.
One six-density point costs at most70000000 operations. Even after sharing
ALL mode transforms across the three columns and two parities, this
particular unconditional all-series algorithm requires at least4175880
operations per point. Its prospective batch consequently costs between

    46661283120 and782190000000 operations,             (2)

including setup in the upper bound. The lower bound alone exceeds the
declared ceiling. STOP this prescription before a batch. This is new
negative evidence about this explicit implementation, not a necessary
complexity bound for Carleman evaluation. Finite asymptotic expansions,
different precisions and other algorithms remain untested here.

No point or norm batch was run. No outer quadrature/forcing/projection
ledger, actual residual norm, inverse pairing, signed S3 comparison or
RH assertion follows. This result has not had a separate critical audit.
All higher/mixed endpoint, C744q/H2, non-neutral and global gaps remain.

## Proof

### 1. Exact finite transform, including neutrality and both parities

Put k_n=n*pi/(2a). From C998a(4),(6), write each parity as the appropriate
even or odd part of sum_(n=0)^255 b_n cos(k_n s), where

    b_0=q_0/sqrt(a),
    b_n=(-1)^n sqrt(2/a) q_n, n>=1;
    q_0=-sum_(even n>=2) [sqrt(2)a^2/(a^2+n^2*pi^2)]q_n,
    q_1=-sum_(odd n>=3) [(a^2+pi^2)/(a^2+n^2*pi^2)]q_n. (3)

Thus the odd sign is negative, as required by reflection; the completion
is algebraic, not a saved rounded raw vector. The two parity transforms
can share each scalar mode integral. C998a's free coefficient estimate
gives sum|b_n|<=6 sum_(n>=2)|q_n|<16 for each whole column. The complete
654/655 dyadics independently verify this strict bound below.

For s=t/a in [2^-80,1], let L(s)=log((1+s)/s). The zero mode is L(s).
For n>0 put z0=n*pi*s/2,z1=n*pi*(1+s)/2, and C(z)=Ci(z)-gamma-log(z).
Then the mode integral is exactly

    I_n(s)=cos(z0)[L(s)+C(z1)-C(z0)]
                       +sin(z0)[Si(z1)-Si(z0)].        (4)

Indeed substitute u=t+r in the original integral in r. The cosine
addition formula gives cos(k_n(u-t))/u. The primitives are Ci(k_n u)
and Si(k_n u), whose derivatives are cos(k_n u)/u and sin(k_n u)/u.
Evaluating at u=t,t+a gives (4); gamma and log(k_n) cancel exactly.
Both limits are positive, and no Ci(0) or branch crossing occurs. This
is the necessary finite-data applicability calculation, not a general
special-function reproof. Also |I_n(s)|<=L(s)<81, directly from the
integral and s>=2^-80, log2<1.

### 2. Finite setup and the input contract

All setup interval endpoints lie on the2^-1024 lattice. Basic operations
round lower/upper endpoints outwards. For square root, bisect the integer
inequality m^2<=X, with an initial power-of-two bracket; each of the
two endpoints takes at most1026 iterations. Add one to the upper integer
root when its square is smaller than X. There is no free sqrt call.

Compute log2,log3 with512 positive atanh terms, z=(r-1)/(r+1), and tail
2z^1025/[1025(1-z^2)] for r=2,3. Compute pi=16atan(1/5)-4atan(1/239)
with256 alternating terms and the next-term absolute remainder. Interval
recurrences include argument-rounding errors. These known elementary
series are used only to construct constants; convergence is not the
accuracy certificate. The full replay verifies the resulting enclosures
for a,pi,log2 have width PLUS one lattice unit less than2^-980.
It also verifies1/4<a<3/10 and3<pi<4.

Use these intervals in (3), with directed division and root intervals
for sqrt(2),sqrt(1/a),sqrt(2/a). All denominators are strictly positive.
For EACH of768 coefficients, the certificate verifies interval width
plus one lattice unit less than2^-900. Choose its dyadic midpoint rounded
down. Its error is therefore less than2^-900. The complete enclosing
absolute coefficient mass is also strictly below16 for each column.
Every exact free dyadic is on the setup lattice. No unchecked coefficient
or normalization is replaced by an approximate neutral vector.

Let a0 be the rounded midpoint of a's interval. From (1), t<.3 and
a,a0>.25, the error in (T*2^-1024)/a0 relative to s=t/a is at most
4*2^-1024+4.8*2^-980<2^-977. Divide, round DOWN to the2^-512 lattice,
and clamp to [2^-80,1], obtaining s0. Clamping does not increase distance
to a point in this interval, so |s0-s|<2^-510. For the ENTIRE density,

    |d/ds integral_0^a v(r)/(as+r) dr|
       <=a*16 integral_0^a (as+r)^(-2)dr<=16/s.

The segment between s,s0 stays in [2^-80,1]. Thus the entire input error
is less than16*2^80*2^-510=2^-426. This does not require cancellation
inside (4). Input code generation by an outer quadrature remains the
caller's separate obligation; its uncertainty is already paid here.

### 3. Fixed series, cancellation and rounding

Set u=2^-4096, with floor rounding R to the u lattice. For an EXACT
dyadic z in (0,1024), use factorial terms

    A_0=z, B_0=1,
    A_(j+1)=R[-A_j*z^2/((2j+2)(2j+3))],
    B_(j+1)=R[-B_j*z^2/((2j+1)(2j+2))].              (5)

The square z^2 and each numerator are formed exactly, followed by ONE
integer division to round; a separately rounded square is not used.
For j=0,...,N-1 accumulate A_j,B_j exactly as dyadics for sin,cos;
accumulate R(A_j/(2j+1)) for Si and R(B_j/(2j)) for C, omitting j=0
in the latter. These are precisely the imported DLMF series.

After N terms the first omitted cosine degree is4096. The absolute
successive ratios from there are less than1/16, and all four omitted
tails are bounded by

    2*1024^4096/4096! < 2^-1023.                       (6)

The strict last comparison is checked on the COMPLETE exact integers;
it is not inferred from a floating approximation or a partial series.
For sine the first omitted degree is4097 and the extra ratio is at
most1024/4097<1; the Si/C denominators only reduce their bounds.

To pay recurrence rounding despite very large intermediate terms, any
product of r consecutive recurrence magnitudes is at most
z^(2r)/(2r)!<=exp(z)<2^2048. Here all denominator factors start at
least as large as1,...,2r, and exp(1024)<4^1024. A local rounding
perturbation has absolute magnitude<u. Therefore each computed term
differs from its exact factorial term by at most N*2^2048*u. Summing
N such errors, and paying N extra divisions for Si/C, bounds the error
of EACH accumulated function by

    (N^2*2^2048+N)u < 2^-2025.                        (7)

This uniform bound pays cancellation, rather than relying on a requested
working precision. Combining (6),(7), each returned function differs
from its exact value at the dyadic argument by less than2^-1022.

### 4. Arguments, logarithm and complete six-density error

Form the two arguments in (4) from s0 and the midpoint pi0, rounded to
the u lattice. They are strictly positive and less than1024 since
n<=255, pi0<4 and s0<=1. Their errors relative to the exact pi
arguments at s0 are less than2^-970 (255*2^-980 plus rounding).

For L(s0), normalize the EXACT rational (1+s0)/s0=2^e r with
1<=r<=2 and1<=e<=81, using bit lengths and one comparison. Evaluate
log r by512 positive atanh terms. Its z=(r-1)/(r+1) satisfies0<=z<=1/3;
floor it to the u lattice, iterate the exact dyadic square with one
rounding per power, divide terms and sum. The power ratio is at most1/9;
the power error is less than(9/8)u and log's argument sensitivity
2/(1-z^2) is less than3. The entire power/division error is less
than6*512u. The positive omitted tail is less than2^-1600, checked
exactly. Add e times the setup log2 midpoint. Consequently the complete
L error is less than2^-970, including that constant's uncertainty.

On [0,1024], |Si'|<=1 and |C'|<=1. For C', use
|cos z-1|/z<=min(z/2,2/z)<=1; the value at zero is removable.
Also |C(z)|<=z^2/4<=2^18, |Si(z)|<=z<=1024, and sin/cos have
Lipschitz constant1 on the real axis. Applying these inequalities
to (4), including both argument errors, the logarithm, (6),(7) and
the final rounded product sum, gives mode error less than2^-940:
each trigonometric perturbation is multiplied by a bracket less than
2^20, each C/Si perturbation has coefficient at most2, and all these
terms together are less than2^25*2^-970<2^-940. The smaller product
roundings fit this strict allowance. This argument uses real points,
not a wide interval extension or an unproved complex-box estimate.

Accumulate (3),(4) with fixed-point products and exact dyadic additions,
sharing all255 nonzero-frequency transforms across six outputs. Their
coefficient mass is below16. The mode errors and final rounding are
therefore less than2^-930. Replacing exact coefficients by their
midpoints costs less than256*81*2^-900. For each complete output,

    total error < 2^-426 +256*81*2^-900+2^-930
                < 2^-425 < 2^-400 < 2^-53.            (8)

This covers all six sums, including their zero modes. It does not
certify any other component of the full residual or a residual norm.

### 5. Complete scalar work test and reproduction boundary

The numerical implementation is explicit in
`scripts/separation-seven/finite-cosine-point-660.py`. Directed setup
operations are charged64 integer operations per call, except roots
charged20000 for their two explicit bisections. The executed conservative
charge is984736. Allowing exact input conversion, denominator construction,
loop comparisons, midpoint extraction and all finite coefficient bookkeeping
still fits the stated10000000 setup bound (fewer than100000 additional
elementary operations charged64 each). No special-function calls remain.

Each argument's series uses at most64N+64 scalar operations, including
term denominators, both factorial recurrences, Si/C divisions, all four
accumulators and loop overhead. There are510 arguments per point.
Charge64(512+256+16) for the log recurrence, normalization, argument
formation/assembly, and64*6*256 for all six weighted sums. The total
is less than70000000 per point. Setup registers are below2100 bits.
Point factorial terms and exact dyadic sums have magnitude below
2^(2048+11), so their scaled integers need fewer than6156 bits.
Multiplying by an exact argument square adds at most8212 bits.
Thus16384-bit registers suffice for every numerical operation,
including its division numerator; subsequent product sums are smaller.
This pays precision as well as the scalar count, without a runtime claim.

For an independent LOWER bound, the specified unconditional program
performs two factorial updates per j<N-1, at both arguments for each
n=1,...,255, even though it shares all modes across outputs. Each update
uses a multiplication and division. Hence at least

    2*255*2*(2048-1)*2=4175880 operations/point.

Multiplication by11174 gives (2)'s lower bound. Setup plus11174 times
70000000 gives its upper bound. The execution ceiling fails by the
lower bound, independently of how sharp the upper allowances are.
No other evaluator is ruled out; in particular this does not test the
covered finite-asymptotic option. There is no claim of intrinsic large
cost or a large residual. This precise all-series prescription stops.

Reproduce only the setup and exact planning certificate with

    python3 scripts/separation-seven/finite-cosine-point-660.py

It saves `scripts/separation-seven/finite-cosine-point-660.json` and
prints bounds, failures and its path. All799 checks pass. The complete
certificate retains every constant interval, all768 coefficient intervals,
all error terms and the full factorial ratio, plus input/script hashes.
The analytic error/operation proof above is essential; the script does
not validate it merely by reporting pass. Optional single-point code is
provided but was not executed. The default run computes no point values,
no norms and no batch. Prior files,652/657 stops and unfinished work
are preserved. Local standard-method specialization is the only claim;
no progress beyond the inspected general numerical methods is asserted.

## Mathlib

Full matching coverage of this frozen six-density algorithm, input/error
contract and work bound has not been checked. Unknown availability is
not evidence of absence. No matching Mathlib theorem is used; the precise
primary analytic series, definitions and error method are cited above.
